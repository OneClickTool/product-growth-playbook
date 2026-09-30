---
name: research-review-mining
description: Mine competitors' reviews (App Store, Google Play, Chrome Web Store, Mac App Store, G2, Capterra, Reddit threads) for pain points, wished-for features, switching reasons and the exact words users use, and turn them into a ranked opportunity table. Use when validating an idea, planning features, positioning against competitors, writing store copy, or when someone asks "what do users hate about X", "analyze competitor reviews", "find feature gaps", or "what should my app do better".
license: MIT
metadata:
  category: research
  difficulty: beginner
  time: 60 min
  version: 1.0.0
  author: nvminhtu
---

# Review Mining

> In an hour you will have 100+ competitor reviews sorted into pain points, a ranked table of opportunities,
> and a list of phrases real users use.

## Goal
Learn what users love, hate and wish for in the tools you compete with, in their own words, before you build
or rewrite anything.

## When to use
- Before building: is there a real gap?
- Planning your next feature or your positioning ("the X that doesn't Y").
- Writing store listings, landing pages and ads. User words convert better than yours.
- **Not for:** finding where people ask for tools in general → [research-where-users-ask](../research-where-users-ask/SKILL.md).

## Inputs
- 3–5 competitors and their store or review-site pages.
- Your product idea in one sentence.

## Where to read reviews

| Product type | Where | Tip |
|---|---|---|
| iPhone / iPad / Mac apps | App Store product page → Ratings & Reviews | Read by *Most Recent* and *Most Critical*. Check each country you care about |
| Android apps | Google Play → Ratings and reviews | Filter by star rating and "latest" |
| Browser extensions | Chrome Web Store → Reviews | Low-star reviews often describe exact bugs and missing features |
| Mac / Windows software | [MacUpdate](https://www.macupdate.com/), vendor forums, [r/macapps](https://www.reddit.com/r/macapps/), [r/software](https://www.reddit.com/r/software/) | Look for "switched from" posts |
| SaaS / business tools | [G2](https://www.g2.com/), [Capterra](https://www.capterra.com/) | Reviews have *likes* / *dislikes* fields, which are pre-sorted for you |
| Any | `site:reddit.com "X" review`, `"X" vs`, `"switched from X"` | Honest long-form experiences |

## Steps
1. **Collect (20 min).** For each competitor, copy about 30 reviews: 10 × 1–2★, 10 × 3★, 10 × 5★, mostly from the last
   12 months. Keep the star rating, date and source with each one.
2. **Tag (20 min).** Give each review 1–2 tags: `bug`, `missing-feature`, `price`, `ads`, `privacy`, `sync`, `ux`,
   `support`, `praise:<thing>`. Keep a column for **exact quotes** you might reuse.
3. **Count and rank (10 min).** For each tag: how many reviews, across how many competitors, and the average star rating.
   An opportunity = a pain point that appears across **several** competitors and that you can solve well.
4. **Find switching triggers (5 min).** What made people leave, or threaten to leave? ("After the price
   increase…", "since they added an account…")
5. **Write it up (5 min).** A research note ([research-doc-organization](../research-doc-organization/SKILL.md))
   with the opportunity table, the top 10 quotes, and what you'll do about it.

Don't copy other people's reviews into your marketing word for word. Use the *words and themes*, not the quotes.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are a product researcher. Analyze these competitor reviews.

My idea: {{one sentence}}
Reviews (each with competitor, stars, date, source): {{paste 50-150 reviews}}

1. Tag each review with 1-2 of: bug, missing-feature, price, ads, privacy, sync, ux, support, performance,
   praise:<thing>. Suggest new tags if needed.
2. Table: tag | # reviews | # competitors affected | avg stars | one representative quote.
   Sort by (# competitors affected, then # reviews).
3. Top 5 opportunities for my idea: the pain, the evidence (counts + quote), and how my product could solve it.
4. Switching triggers: what made users leave or threaten to leave.
5. 15 phrases users use to describe the problem or the outcome they want (for keywords and copy).
Only use what's in the reviews. Don't invent quotes or numbers.
````

## Example output

> **Illustrative example.** Fictional competitors and counts, shown for format.

120 reviews of 4 habit-tracker apps (last 12 months).

| Pain point | Reviews | Competitors | Avg ★ | Quote |
|---|---|---|---|---|
| Forced account / sign-in | 23 | 3 of 4 | 1.8 | "Why do I need an account to tick a box?" |
| Subscription for basic features | 19 | 4 of 4 | 2.1 | "Was free, now $5/month for reminders" |
| Streak lost after a sick day | 11 | 2 of 4 | 2.6 | "One missed day and 200 days are gone" |
| Widget doesn't update | 9 | 2 of 4 | 2.4 | "Widget shows yesterday" |

**Opportunity:** no account + a one-time Pro purchase + "streak freeze". The positioning writes itself:
*"The habit tracker that doesn't punish a sick day."*

## Common mistakes
- **Reading only 1★ reviews.** 5★ reviews tell you what *must not* break when you compete.
- **Too few reviews.** Ten reviews give you anecdotes. You need 100+ across several competitors to see patterns.
- **Solving a pain only one competitor has.** That's their bug, not a market gap.
- **Ignoring dates.** A complaint from 3 years ago may already be fixed.

## Related skills
- [research-where-users-ask](../research-where-users-ask/SKILL.md): threads where people compare tools.
- [aso-keyword-research](../../aso/aso-keyword-research/SKILL.md): user phrases become keyword seeds.
- [monetization-free-trial-vs-freemium](../../monetization/monetization-free-trial-vs-freemium/SKILL.md): price complaints tell you where the free/paid line hurts.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu).
