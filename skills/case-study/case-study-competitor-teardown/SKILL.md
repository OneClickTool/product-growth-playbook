---
name: case-study-competitor-teardown
description: Learn from the competition by tearing down 3 competitors (a leader, a fast riser and one that stalled) across positioning, store listing, onboarding, pricing and paywall, growth channels, ads, changelog and reviews, using free public tools, and turn it into a Copy / Beat / Avoid list. Use when about to build or reposition, when a competitor is growing faster, when planning pricing or a launch, or when someone asks "analyze my competitors", "competitor teardown", "what are competitors doing", "learn from competitors", or "why is X growing".
license: MIT
metadata:
  category: case-study
  difficulty: intermediate
  time: 2-3 h (about 45 min per competitor)
  version: 1.0.0
  author: nvminhtu
---

# Competitor Teardown: Learn From the Enemy

> In 2–3 hours you will know what 3 competitors do at every step from first impression to payment, which of it
> works, and a short list of what to **copy**, where to **beat** them, and what to **avoid**.

## Goal
Your competitors have already paid to test positioning, pricing, onboarding and channels. Study those results so
you start from their lessons instead of repeating their experiments.

## When to use
- Before building, repositioning or re-pricing.
- A competitor is suddenly growing, or suddenly quiet.
- Before a launch, to see where they launched and what worked.
- **Not for:** mining their reviews in depth → [research-review-mining](../../research/research-review-mining/SKILL.md).
  Learning from successful products outside your niche → [case-study-success-story-analysis](../case-study-success-story-analysis/SKILL.md).

## Inputs
- 3 competitors: **a leader** (the one everyone mentions), **a riser** (newer and growing fast), and **one that
  stalled** (no updates in a year, falling ratings). Failures teach as much as winners.
- A test device or browser, and a throwaway email for sign-ups.
- `assets/teardown-sheet.md` from this skill.

## What to look at (and the free tools)

| Area | Look at | Free tool / where |
|---|---|---|
| **Positioning** | Headline, first screenshot, who they say it's for, the one promise | Store page, homepage |
| **Store listing** | Title, subtitle, screenshot captions, rating and count, category rank | App Store / Google Play page |
| **Shipping pace** | What they released and how often, which tells you their priorities | App Store *Version History*, Play "What's new", public changelog |
| **Onboarding** | Steps to first value, sign-up wall, permissions, when the paywall appears | Install it and screenshot every screen |
| **Pricing and paywall** | Plans, trial, anchor price, past price changes | Paywall screens. Old versions of the pricing page on the [Wayback Machine](https://web.archive.org/) |
| **Web traffic and channels** | Rough traffic, top sources (search, social, referrals) | [Similarweb](https://www.similarweb.com/) (free tier), [Google Trends](https://trends.google.com/) for brand interest |
| **Ads** | Which ads they run, how long (long-running ads usually work) | [Meta Ad Library](https://www.facebook.com/ads/library/), [Google Ads Transparency Center](https://adstransparency.google.com/), [TikTok ad library](https://library.tiktok.com/ads) (ads shown in Europe) |
| **Launches and community** | Where they launched, what people said | Product Hunt page, Show HN thread, their subreddit or Discord |
| **Content and SEO** | Blog topics, comparison pages ("X vs Y"), free tools | `site:competitor.com` searches |
| **Tech stack** | Analytics, payments, support tools | [BuiltWith](https://builtwith.com/) (web) |
| **What users say** | Top complaints and praise | Reviews → [research-review-mining](../../research/research-review-mining/SKILL.md) |

## Steps
1. **Pick the 3 competitors (10 min)** and write one line on why each one matters.
2. **Be a new user (20 min each).** Search for the job your product does, find them, install, sign up and use the
   main feature. Screenshot **every screen** until you hit the paywall. Count the taps to first value.
3. **Fill the teardown sheet (20 min each)** using the table above. Facts only, with a link or screenshot for each.
4. **Look for proof, not opinions.** A pattern is worth copying if there's evidence it works: an ad running for
   3+ months, a feature every competitor converged on, a paywall layout they kept after a redesign, praise in reviews.
5. **Write Copy / Beat / Avoid (20 min).**
   - **Copy:** proven patterns that users now expect (not their brand, words or assets).
   - **Beat:** their weaknesses that users complain about and that you can fix.
   - **Avoid:** what the stalled competitor did, and anything the others tried and removed.
6. **Pick 3 actions for this month** and link them to skills (pricing, paywall, listing, launch).
7. **Repeat every quarter.** Put the sheet in your research folder ([research-doc-organization](../../research/research-doc-organization/SKILL.md))
   and note what changed since last time.

## Prompt (copy-paste)
Works best with web browsing. Replace everything in `{{ }}`. Paste your screenshots or notes if the AI can't browse.

````text
You are a product strategist doing a competitor teardown for me.

My product: {{what it does, platform, price model, stage}}
Competitors: leader {{name + link}}, riser {{name + link}}, stalled {{name + link}}
My notes and screenshots from using them: {{paste}}

For each competitor, fill this table with facts and a source for each (link or "from my notes"):
positioning (headline, promise, audience) · store listing (title, subtitle, first 3 screenshot captions, rating + count) ·
shipping pace (last 5 releases from version history/changelog) · onboarding (steps to first value, sign-up wall, paywall timing) ·
pricing (plans, trial, anchor, any past changes) · channels (launches, ads that have run for a long time, content/SEO, communities) ·
top 3 complaints and top 3 praises from reviews.
Then write:
- COPY: 5 proven patterns worth adopting, with the evidence for each (not their brand or wording).
- BEAT: 5 weaknesses users complain about that I could fix, with evidence.
- AVOID: 3 mistakes, especially from the stalled competitor.
- 3 actions for this month.
Never invent numbers, dates or quotes. Write "unknown" when you can't verify something.
````

## Example output

> **Illustrative example.** Fictional products and findings, shown for format.

*My product:* Sipwell, a water reminder (iOS, freemium).

| | Leader: *AquaDaily* | Riser: *Sippy* | Stalled: *DrinkUp* |
|---|---|---|---|
| Promise | "Hit your water goal" | "Hydration for busy people" | "Track your water" |
| Taps to first value | 9 (account required) | 3 (no account) | 6 |
| Paywall | After onboarding, 7-day trial, yearly default | On 3rd reminder setup | Ads + $2.99 remove-ads |
| Ships | Every 2 weeks | Weekly, widget-focused | Last update 14 months ago |
| Long-running ad | "Stop forgetting to drink" UGC video (5 months) | — | — |
| Top complaint | Forced account | Too few themes | Crashes on iOS 26 |

- **Copy:** yearly plan as the default with a trial timeline; a UGC-style ad hook about forgetting to drink; widgets.
- **Beat:** no account needed (their #1 complaint); fewer steps to first value (target: 3 taps).
- **Avoid:** an ads-only model and slow updates (DrinkUp's ratings fell from 4.6 to 3.9).

## Common mistakes
- **Copying their brand, words or screenshots.** Learn the pattern, and write your own version. Copying is unethical and can break store rules and trademarks.
- **Only studying the leader.** Their advantages (brand, budget) often aren't copyable. Risers and failures teach more.
- **Opinions without evidence.** "Their onboarding is bad" isn't useful. "9 taps and an account before first value, #1 complaint in 40 reviews" is.
- **A teardown that changes nothing.** End with 3 actions, or it was just reading.

## Related skills
- [research-review-mining](../../research/research-review-mining/SKILL.md): go deep on their reviews.
- [case-study-success-story-analysis](../case-study-success-story-analysis/SKILL.md): learn from winners in other niches.
- [monetization-pricing-strategy](../../monetization/monetization-pricing-strategy/SKILL.md) and [monetization-paywall-design](../../monetization/monetization-paywall-design/SKILL.md): act on what you found.
- [aso-title-subtitle-optimization](../../aso/aso-title-subtitle-optimization/SKILL.md): position against them in search.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Tool coverage and limits change (for example, the TikTok library
covers ads shown in Europe), so check each tool's help page.
