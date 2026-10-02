#!/usr/bin/env python3
"""Work a revenue target backward into a weekly funnel. Prints a Markdown table.

Standard library only.

Examples:
  # $1,000 MRR from a $5/month subscription, 15% store fee, reached over 12 weeks
  python3 revenue_backsolve.py --target 1000 --price 5 --fee 0.15 \
      --rates visit_to_install=0.25,install_to_activated=0.4,activated_to_paid=0.04 --weeks 12

  # $3,000 total in 8 weeks from a $19 one-time product, compared with today's traffic
  python3 revenue_backsolve.py --target 3000 --price 19 --fee 0.05 --model one-time \
      --rates visit_to_signup=0.05,signup_to_paid=0.08 --weeks 8 --current-visitors 1200
"""
import argparse
import math
import sys


def parse_rates(text):
    """'a_to_b=0.25,b_to_c=0.4' -> [('a_to_b', 0.25), ('b_to_c', 0.4)] in funnel order."""
    rates = []
    for part in text.split(","):
        name, _, value = part.partition("=")
        rate = float(value)
        if not 0 < rate <= 1:
            raise ValueError(f"rate '{name}' must be between 0 and 1, got {value}")
        rates.append((name.strip(), rate))
    return rates


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--target", type=float, required=True, help="money goal (MRR for subscription, total for one-time)")
    p.add_argument("--price", type=float, required=True, help="price per customer per month (subscription) or per sale")
    p.add_argument("--fee", type=float, default=0.0, help="store/payment fee as a fraction, e.g. 0.15")
    p.add_argument("--model", choices=["subscription", "one-time"], default="subscription")
    p.add_argument("--rates", required=True, help="funnel steps top to bottom: visit_to_install=0.25,...")
    p.add_argument("--weeks", type=int, required=True, help="weeks until the deadline")
    p.add_argument("--current-visitors", type=float, help="visitors per week today, for the reality check")
    args = p.parse_args()

    try:
        rates = parse_rates(args.rates)
    except ValueError as e:
        p.error(str(e))
    net = args.price * (1 - args.fee)
    if net <= 0 or args.weeks <= 0:
        p.error("price after fee and weeks must be positive")

    customers = math.ceil(args.target / net)
    per_week = customers / args.weeks
    what = "paying subscribers at the deadline" if args.model == "subscription" else "sales in total"
    print(f"Net per customer: {net:.2f} → **{customers} {what}** (~{per_week:.1f} new per week, ignoring churn)\n")

    rows = []
    needed = per_week
    for name, rate in reversed(rates):
        top = name.split("_to_")[0] if "_to_" in name else name
        needed = needed / rate
        rows.append((top, name, rate, needed))
    print("| Step | Rate | Needed per week |")
    print("|---|---|---|")
    for top, name, rate, n in reversed(rows):
        print(f"| {top} | {name} = {rate:.1%} | {math.ceil(n):,} |")
    print(f"| paid | | {math.ceil(per_week):,} |")

    if args.current_visitors:
        gap = needed / args.current_visitors
        print(f"\nTop of funnel needed: {math.ceil(needed):,}/week · today: {args.current_visitors:,.0f}/week · gap {gap:.1f}×")
        if gap > 5:
            print("Verdict: not realistic with this funnel. Change ONE lever (price, yearly plan, weakest step, new channel, date).")
        elif gap > 1:
            print("Verdict: possible if you close the gap; give each channel a weekly number.")
        else:
            print("Verdict: on track at today's traffic; protect the weakest conversion step.")
    if args.model == "subscription":
        print("\nNote: subscriptions churn. Add the customers you lose each month (your own churn rate) on top of this.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
