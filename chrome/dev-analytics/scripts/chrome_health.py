#!/usr/bin/env python3
"""Chấm sức khỏe một Chrome extension từ các file CSV export ở Chrome Web Store Developer Dashboard.

Chỉ dùng thư viện chuẩn. Cách chạy:
    python3 chrome_health.py --installs installs.csv --uninstalls uninstalls.csv [--users weekly-users.csv]

Không cần đúng tên cột: mỗi dòng có một ô ngày (2026-10-22, 10/22/2026, Oct 22, 2026 ...) thì mọi ô số còn lại
trong dòng được cộng lại thành tổng của ngày đó. Nhờ vậy file theo quốc gia / ngôn ngữ / OS (mỗi cột một nhóm)
cũng đọc được như file tổng.
"""
import argparse
import csv
import re
import sys
from datetime import date, datetime

DATE_FORMATS = ("%Y-%m-%d", "%Y/%m/%d", "%m/%d/%Y", "%d/%m/%Y", "%b %d, %Y", "%B %d, %Y", "%Y%m%d")


def parse_date(cell):
    cell = cell.strip()
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(cell, fmt).date()
        except ValueError:
            pass
    return None


def parse_number(cell):
    cell = cell.strip().replace(",", "")
    return float(cell) if re.fullmatch(r"-?\d+(\.\d+)?", cell) else None


def read_daily(path):
    """{date: total} từ một file CSV export."""
    daily = {}
    with open(path, newline="", encoding="utf-8-sig") as f:
        for row in csv.reader(f):
            day = next((d for d in map(parse_date, row) if d), None)
            if not day:
                continue  # dòng tiêu đề hoặc dòng tổng
            values = [n for c in row if not parse_date(c) and (n := parse_number(c)) is not None]
            daily[day] = daily.get(day, 0) + sum(values)
    if not daily:
        sys.exit(f"{path}: không tìm thấy dòng nào có ngày. Mở file kiểm tra lại cột ngày.")
    return daily


def window(daily, end, days):
    return sum(v for d, v in daily.items() if 0 <= (end - d).days < days)


def pct_change(new, old):
    return None if old == 0 else (new - old) / old * 100


def fmt_pct(x):
    return "—" if x is None else f"{x:+.1f}%"


def verdict(uninstall_ratio, trend_7d, users_trend):
    """Quy tắc kinh nghiệm của playbook, không phải chuẩn của Google. Xem 04-suc-khoe-extension.md."""
    points = 0
    if uninstall_ratio is not None:
        points += 2 if uninstall_ratio < 30 else 1 if uninstall_ratio < 60 else 0
    if trend_7d is not None:
        points += 2 if trend_7d > 10 else 1 if trend_7d > -10 else 0
    if users_trend is not None:
        points += 2 if users_trend > 2 else 1 if users_trend > -2 else 0
    max_points = 2 * sum(x is not None for x in (uninstall_ratio, trend_7d, users_trend))
    if not max_points:
        return "Chưa đủ dữ liệu"
    share = points / max_points
    return "🟢 Khỏe" if share >= 0.75 else "🟡 Cần theo dõi" if share >= 0.4 else "🔴 Đáng lo"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--installs", required=True, help="CSV export của biểu đồ Installs")
    ap.add_argument("--uninstalls", help="CSV export của biểu đồ Uninstalls")
    ap.add_argument("--users", help="CSV export của biểu đồ Weekly users (tuỳ chọn)")
    args = ap.parse_args()

    installs = read_daily(args.installs)
    uninstalls = read_daily(args.uninstalls) if args.uninstalls else {}
    end = max(installs)

    i30, i30_prev = window(installs, end, 30), window(installs, date.fromordinal(end.toordinal() - 30), 30)
    i7, i7_prev = window(installs, end, 7), window(installs, date.fromordinal(end.toordinal() - 7), 7)
    u30 = window(uninstalls, end, 30) if uninstalls else None
    ratio = None if u30 is None or i30 == 0 else u30 / i30 * 100

    users_trend, users_line = None, ""
    if args.users:
        users = read_daily(args.users)
        days = sorted(users)
        last = users[days[-1]]
        old = next((users[d] for d in reversed(days) if (days[-1] - d).days >= 28), users[days[0]])
        users_trend = pct_change(last, old)
        users_line = f"Weekly users        : {last:.0f} (so với ~4 tuần trước: {fmt_pct(users_trend)})\n"

    peak_day = max(installs, key=installs.get)
    avg = i30 / 30
    spike = installs[peak_day] >= max(3 * avg, avg + 5)

    print(f"Đến ngày            : {end.isoformat()}")
    print(f"Installs 30 ngày    : {i30:.0f} (kỳ trước: {i30_prev:.0f}, {fmt_pct(pct_change(i30, i30_prev))})")
    print(f"Installs 7 ngày     : {i7:.0f} (7 ngày trước đó: {i7_prev:.0f}, {fmt_pct(pct_change(i7, i7_prev))})")
    if u30 is not None:
        print(f"Uninstalls 30 ngày  : {u30:.0f}")
        print(f"Net 30 ngày         : {i30 - u30:+.0f}")
        print(f"Uninstall / install : {'—' if ratio is None else f'{ratio:.0f}%'}")
    print(users_line, end="")
    print(f"Ngày cao nhất       : {peak_day.isoformat()} = {installs[peak_day]:.0f} installs "
          f"(trung bình {avg:.1f}/ngày){' ← đột biến, tìm nguyên nhân' if spike else ''}")
    print(f"Kết luận            : {verdict(ratio, pct_change(i7, i7_prev), users_trend)}")


if __name__ == "__main__":
    main()
