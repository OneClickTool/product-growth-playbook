#!/usr/bin/env python3
"""Pack keywords into the App Store 100-character keyword field.

Splits phrases into single words, drops words already in the title/subtitle,
drops duplicates and simple plurals, skips filler words, and keeps the
priority order you give until the field is full.

Usage:
  python3 pack_keywords.py --title "Sipwell: Water Reminder" \
      --subtitle "Drink Tracker & Hydration Log" \
      --keywords "water log, daily water intake, hydrate, bottle"
  python3 pack_keywords.py --title ... --file keywords.txt   # one keyword per line, best first
"""
import argparse
import re
import sys

FILLER = {"app", "apps", "free", "the", "and", "a", "an", "for", "of", "to", "with", "&", "my", "best"}


def words(text):
    return [w for w in re.split(r"[^\w']+", text.lower()) if w]


def singular(word):
    if len(word) > 3 and word.endswith("ies"):
        return word[:-3] + "y"
    if len(word) > 3 and word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


def pack(title, subtitle, keywords, limit=100):
    used = {singular(w) for w in words(title) + words(subtitle)}
    kept, skipped, length = [], [], 0
    for phrase in keywords:
        for w in words(phrase):
            if w in FILLER or singular(w) in used:
                continue
            extra = len(w) + (1 if kept else 0)
            if length + extra > limit:
                skipped.append(w)
                continue
            kept.append(w)
            used.add(singular(w))
            length += extra
    return ",".join(kept), skipped


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--title", default="")
    p.add_argument("--subtitle", default="")
    p.add_argument("--keywords", help="comma-separated, highest priority first")
    p.add_argument("--file", help="one keyword or phrase per line, highest priority first")
    p.add_argument("--limit", type=int, default=100)
    a = p.parse_args()

    if a.file:
        with open(a.file, encoding="utf-8") as f:
            kws = [line.strip() for line in f if line.strip()]
    elif a.keywords:
        kws = [k.strip() for k in a.keywords.split(",") if k.strip()]
    else:
        p.error("give --keywords or --file")

    field, skipped = pack(a.title, a.subtitle, kws, a.limit)
    print(f"Title    ({len(a.title):>3}/30): {a.title}")
    print(f"Subtitle ({len(a.subtitle):>3}/30): {a.subtitle}")
    print(f"Keywords ({len(field):>3}/{a.limit}): {field}")
    if skipped:
        print(f"Did not fit: {', '.join(skipped)}")
    over = [n for n, v in (("title", a.title), ("subtitle", a.subtitle)) if len(v) > 30]
    if over:
        print(f"WARNING: {' and '.join(over)} over 30 characters", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
