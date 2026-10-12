#!/usr/bin/env python3
"""Read a TikTok slideshow post log (CSV) and print a Markdown report: what to fix per post, and a verdict per hook
formula (scale / keep / retest / drop). Standard library only.

Usage:
    python3 slideshow_loop.py post-log.csv [--high-views 10000] [--last 30]

CSV columns (header row required; extra columns are ignored; empty cells are fine):
    date, hook, formula, cta, views, saves, shares, profile_visits, link_clicks, installs, paid

Rules come from docs/06-metrics-and-decisions.md (the "Larry loop"):
    views high + installs low  -> fix the CTA slide
    views low  + installs high -> fix the hook
    both low                   -> new hook formula and new CTA
    both high                  -> scale
Hook verdicts by best views: >= 50K scale, 10K-50K keep, 1K-10K retest, < 1K on 2+ posts drop.
"""
import argparse
import csv
import statistics
import sys
from collections import defaultdict

SCALE, KEEP, RETEST = 50_000, 10_000, 1_000


def num(value):
    try:
        return float(str(value).replace(",", "").strip())
    except ValueError:
        return None


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = []
        for row in csv.DictReader(f):
            row = {(k or "").strip().lower(): (v or "").strip() for k, v in row.items()}
            row["views"] = num(row.get("views", ""))
            if row["views"] is None:
                continue  # not measured yet
            for key in ("saves", "shares", "profile_visits", "link_clicks", "installs", "paid"):
                row[key] = num(row.get(key, ""))
            row["formula"] = row.get("formula") or row.get("hook", "")[:40] or "unknown"
            rows.append(row)
    return rows


def per_1k(part, views):
    return None if part is None or not views else part / views * 1000


def diagnose(row, high_views, median_rate):
    high_v = row["views"] >= high_views
    rate = per_1k(row["installs"], row["views"])
    if rate is None or median_rate is None:
        return "scale" if high_v else "fix hook", "no install data: judged on views only"
    high_i = rate >= median_rate
    if high_v and high_i:
        return "scale", "views and installs both strong"
    if high_v:
        return "fix CTA", "people watch but don't install: slide 5 (app name, one action, show the result)"
    if high_i:
        return "fix hook", "the right people convert, too few see it: new person / conflict on slide 1"
    return "fix both", "new hook formula and new CTA, or a different niche angle"


def verdict(views_list):
    best = max(views_list)
    if best >= SCALE:
        return "scale"
    if best >= KEEP:
        return "keep"
    if sum(v < RETEST for v in views_list) >= 2:
        return "drop"
    return "retest"


def fmt(n):
    return "—" if n is None else f"{n:,.0f}" if n >= 10 else f"{n:.2f}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv")
    ap.add_argument("--high-views", type=float, default=10_000, help="views counted as 'high' (default 10000)")
    ap.add_argument("--last", type=int, default=0, help="only the last N measured posts")
    args = ap.parse_args()

    rows = load(args.csv)
    if args.last:
        rows = rows[-args.last:]
    if not rows:
        print("No measured posts (rows need a number in 'views').")
        return 1

    rates = [r for r in (per_1k(x["installs"], x["views"]) for x in rows) if r is not None]
    median_rate = statistics.median(rates) if rates else None
    total = lambda key: sum(r[key] or 0 for r in rows)

    print(f"# Slideshow loop report ({len(rows)} posts)\n")
    print(f"- Views: {fmt(total('views'))} · median {fmt(statistics.median(r['views'] for r in rows))} per post")
    if median_rate is not None:
        print(f"- Installs: {fmt(total('installs'))} · median {median_rate:.2f} per 1K views")
    if any(r["paid"] is not None for r in rows):
        print(f"- Paid: {fmt(total('paid'))}")
    print(f"- 'High views' threshold: {fmt(args.high_views)}\n")

    print("## Per post\n")
    print("| Date | Hook | Views | Installs/1K | Do next | Why |")
    print("|---|---|---|---|---|---|")
    counts = defaultdict(int)
    for r in rows:
        action, why = diagnose(r, args.high_views, median_rate)
        counts[action] += 1
        hook = r.get("hook", "")[:60].replace("|", "/")
        print(f"| {r.get('date', '')} | {hook} | {fmt(r['views'])} | {fmt(per_1k(r['installs'], r['views']))} | **{action}** | {why} |")

    print("\n## Per hook formula\n")
    print("| Formula | Posts | Best views | Median views | Verdict |")
    print("|---|---|---|---|---|")
    groups = defaultdict(list)
    for r in rows:
        groups[r["formula"]].append(r["views"])
    ranked = sorted(groups.items(), key=lambda kv: max(kv[1]), reverse=True)
    for formula, views in ranked:
        print(f"| {formula} | {len(views)} | {fmt(max(views))} | {fmt(statistics.median(views))} | **{verdict(views)}** |")

    print("\n## Next week\n")
    scale = [f for f, v in ranked if verdict(v) == "scale"]
    keep = [f for f, v in ranked if verdict(v) == "keep"]
    drop = [f for f, v in ranked if verdict(v) == "drop"]
    if scale:
        print(f"- Make 3–5 variations of: {', '.join(scale)} (same formula, new person / scene).")
    if keep:
        print(f"- Use again with a new scene: {', '.join(keep)}.")
    if drop:
        print(f"- Stop: {', '.join(drop)}.")
    if counts["fix CTA"] > counts["fix hook"]:
        print("- Most posts lose people after the view: rewrite slide 5 first (app name, one action, show the result).")
    elif counts["fix hook"] or counts["fix both"]:
        print("- Most posts don't reach enough people: write 10 new slide-1 hooks with a person + doubt.")
    if not scale and len(rows) >= 20 and max(r["views"] for r in rows) < KEEP:
        print("- Stop rule: 20+ posts and none over 10K views. Change the niche angle, not just the hooks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
