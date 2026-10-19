#!/usr/bin/env python3
"""Read a daily traffic log and say whether preview pages are growing. Prints Markdown.

Standard library only.

The log is a CSV with one row per day x page x source (see assets/daily-traffic-log.csv):
  date,page,source,sessions,signups
  2026-10-01,/features/batch-rename,google,4,0
  2026-10-01,/features/batch-rename,chatgpt.com,1,1

Sources are grouped into channels: ai (chatgpt.com, perplexity.ai, claude.ai, gemini, copilot),
search (google, bing, duckduckgo...), social, direct, other.

Examples:
  # compare the 7 days before publishing (baseline) with the latest 7 days
  python3 traffic_trend.py daily-traffic-log.csv --start 2026-10-08

  # only one page, 14-day windows
  python3 traffic_trend.py daily-traffic-log.csv --start 2026-10-08 --page /features/batch-rename --window 14
"""
import argparse
import csv
import sys
from collections import defaultdict
from datetime import date, timedelta

AI = ("chatgpt", "openai", "perplexity", "claude.ai", "gemini", "copilot", "bing.com/chat", "you.com", "deepseek")
SEARCH = ("google", "bing", "duckduckgo", "yahoo", "ecosia", "brave", "yandex", "baidu")
SOCIAL = ("reddit", "facebook", "instagram", "tiktok", "youtube", "x.com", "twitter", "t.co", "linkedin",
          "pinterest", "medium", "threads", "news.ycombinator")


def channel(source):
    s = source.strip().lower()
    if any(k in s for k in AI):
        return "ai"
    if any(k in s for k in SEARCH):
        return "search"
    if any(k in s for k in SOCIAL):
        return "social"
    if s in ("", "(direct)", "direct", "(none)", "(not set)"):
        return "direct"
    return "other"


def load(path, page_filter):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        lines = (line for line in f if line.strip() and not line.startswith("#"))  # GA4 exports start with # notes
        for r in csv.DictReader(lines):
            if page_filter and r.get("page", "").strip() != page_filter:
                continue
            try:
                d = date.fromisoformat(r["date"].strip()[:10])
                sessions = float(r.get("sessions") or 0)
                signups = float(r.get("signups") or 0)
            except (KeyError, ValueError) as e:
                raise SystemExit(f"bad row {r}: {e}")
            rows.append((d, r.get("page", "").strip() or "(all)", channel(r.get("source", "")), sessions, signups))
    if not rows:
        raise SystemExit("no rows to read (check the file and --page)")
    return rows


def window_sum(by_day, start, days):
    tot = defaultdict(float)
    for i in range(days):
        for k, v in by_day.get(start + timedelta(days=i), {}).items():
            tot[k] += v
    return tot


def pct(new, old):
    if old == 0:
        return "new" if new else "0"
    return f"{(new - old) / old * 100:+.0f}%"


def verdict(base, last, days):
    visits, signups = last["sessions"], last["signups"]
    rate = signups / visits * 100 if visits else 0
    if visits / days < 3:
        return "Too little traffic to judge. Keep the page, work on presence (answers, directories), check in 2 weeks."
    if base["sessions"] and visits < base["sessions"] * 1.1:
        return "Flat. Rewrite the short answer and H2s around the questions people ask; change one thing, log the date."
    if rate < 2:
        return "Growing, but few sign-ups. People find the page but don't want it enough: sharpen the offer or rethink the feature."
    return "Growing with sign-ups. Good signal to keep designing; ask waitlist people 3 questions before you build."


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("csv", help="daily traffic log (date,page,source,sessions,signups)")
    p.add_argument("--start", required=True, help="date the page went live or was changed (YYYY-MM-DD)")
    p.add_argument("--page", help="only this page path")
    p.add_argument("--window", type=int, default=7, help="days per comparison window (default 7)")
    a = p.parse_args()

    start = date.fromisoformat(a.start)
    rows = load(a.csv, a.page)
    by_day = defaultdict(lambda: defaultdict(float))
    for d, _page, ch, s, su in rows:
        by_day[d]["sessions"] += s
        by_day[d]["signups"] += su
        by_day[d][ch] += s

    w = a.window
    last_day = max(by_day)
    base = window_sum(by_day, start - timedelta(days=w), w)
    last = window_sum(by_day, last_day - timedelta(days=w - 1), w)
    days_live = (last_day - start).days + 1

    print(f"# Traffic trend {'for ' + a.page if a.page else '(all pages)'}\n")
    print(f"Live since {start} ({days_live} days). Baseline = {w} days before; latest = last {w} days to {last_day}.\n")
    if days_live < 28:
        print(f"> Only {days_live} days of data. Judge a page after 28 days; AI citations lag behind search.\n")

    print("| Metric | Baseline | Latest | Change |\n|---|---|---|---|")
    for key, label in [("sessions", "Visits"), ("search", "  from search"), ("ai", "  from AI assistants"),
                       ("social", "  from social"), ("direct", "  direct"), ("other", "  other"),
                       ("signups", "Sign-ups")]:
        print(f"| {label} | {base[key]:.0f} | {last[key]:.0f} | {pct(last[key], base[key])} |")
    rate_b = base["signups"] / base["sessions"] * 100 if base["sessions"] else 0
    rate_l = last["signups"] / last["sessions"] * 100 if last["sessions"] else 0
    ai_share = last["ai"] / last["sessions"] * 100 if last["sessions"] else 0
    print(f"| Sign-ups per 100 visits | {rate_b:.1f} | {rate_l:.1f} | |")
    print(f"| AI share of visits | | {ai_share:.0f}% | |\n")

    print(f"## 7-day rolling average (visits per day)\n\n| Date | Visits | 7-day avg | AI visits |\n|---|---|---|---|")
    first_day = min(by_day)
    d = max(first_day, last_day - timedelta(days=20))
    while d <= last_day:
        roll = window_sum(by_day, d - timedelta(days=6), 7)
        print(f"| {d} | {by_day.get(d, {}).get('sessions', 0):.0f} | {roll['sessions'] / 7:.1f} | "
              f"{by_day.get(d, {}).get('ai', 0):.0f} |")
        d += timedelta(days=1)

    if not a.page:
        pages = defaultdict(lambda: [0.0, 0.0, 0.0])
        for d0, page, ch, s, su in rows:
            if d0 > last_day - timedelta(days=w):
                pages[page][0] += s
                pages[page][1] += su
                pages[page][2] += s if ch == "ai" else 0
        print(f"\n## Pages, last {w} days\n\n| Page | Visits | AI visits | Sign-ups | Per 100 visits |\n|---|---|---|---|---|")
        for page, (s, su, ai) in sorted(pages.items(), key=lambda x: -x[1][0]):
            print(f"| {page} | {s:.0f} | {ai:.0f} | {su:.0f} | {su / s * 100 if s else 0:.1f} |")

    print(f"\n**Read:** {verdict(base, last, w)}")
    print("\nNote: AI visits are a floor. Some assistants send no referrer, so their visits show as direct.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
