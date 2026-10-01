# Playbook: ASO Optimization

A 4-week route to more installs from App Store and Google Play search, then a monthly loop to keep improving.
It's for apps that are already live. Not published yet? Do [listing-app-store](../skills/listing/listing-app-store/SKILL.md) /
[listing-google-play](../skills/listing/listing-google-play/SKILL.md) (Level 1) first, then come back.

## The funnel you're fixing
ASO moves three numbers. Know which one is weakest before you change anything.

| Step | App Store Connect (App Analytics) | Google Play Console (Store listing acquisition) | Fixed by |
|---|---|---|---|
| People **see** you in search | Impressions | Store listing visitors (by traffic source: search) | Keywords, title, subtitle |
| People **open** your page | Product page views | Store listing visitors | Title, icon, first screenshots, rating |
| People **install** | Conversion rate | Store listing conversion rate | Screenshots, rating, reviews |

Metric names change between console versions. Check the current help pages:
[App Store Connect Help](https://developer.apple.com/help/app-store-connect/) ·
[Play Console Help](https://support.google.com/googleplay/android-developer/).

## The route

| Week | Goal | Skill | You end the week with |
|---|---|---|---|
| Week 0 *(1 h)* | Baseline, so you can tell if anything worked | none, see [Measure](#measure-the-baseline-week-0) | Last 28 days of the funnel numbers, saved |
| Week 0 *(optional)* | Know what users love and hate | [research-review-mining](../skills/research/research-review-mining/SKILL.md) → [case-study-competitor-teardown](../skills/case-study/case-study-competitor-teardown/SKILL.md) | User phrases, top complaints, what top competitors show |
| Week 1 | Rank for words people actually search | [aso-keyword-research](../skills/aso/aso-keyword-research/SKILL.md) | Scored keyword sheet, keyword field |
| Week 1 | Turn keywords into a name that ranks and sells | [aso-title-subtitle-optimization](../skills/aso/aso-title-subtitle-optimization/SKILL.md) | Title, subtitle / short description; update submitted |
| Week 2 | Make the page convert | [aso-screenshot-strategy](../skills/aso/aso-screenshot-strategy/SKILL.md) | New screenshot set + one A/B test running |
| Week 3 | Ratings that help, not hurt | [aso-review-and-rating-strategy](../skills/aso/aso-review-and-rating-strategy/SKILL.md) | Review prompt live, 1–3★ reviews answered |
| Week 4 | Read the results, pick the next change | [the monthly loop](#the-monthly-loop) | A one-page ASO log with before/after numbers |

**Where to start if you only have one week:** find your weakest step in the funnel table.
Few impressions → keywords. Views but few installs → screenshots. Rating under 4★ → reviews first,
because a low rating drags down every other fix.

## Measure the baseline (week 0)
1. Pick a **28-day window** that ends before you change anything. Avoid launch spikes, sales and featuring.
2. Write down, per store and for your top country: impressions (or search visitors), product page views,
   conversion rate, installs from search, average rating, number of new ratings.
3. Write down your rank for your 5 most important keywords (search them on a phone, signed out if you can, or
   use an ASO tool you already have).
4. Save it as `growth/aso-log.md`. Every later change gets a line in the same file.

## Store rules that shape the plan
- **App Store:** title, subtitle and keyword field change **only with a new app version** you submit for review.
  Promotional text can change any time without a new version.
  Bundle your keyword and title changes with a release, and plan them a week ahead.
  [App Store Connect Help](https://developer.apple.com/help/app-store-connect/).
- **Google Play:** you can edit the store listing without a new app release. Changes still go through review.
  [Play Console Help](https://support.google.com/googleplay/android-developer/).
- **Both:** don't stuff competitor brand names or misleading claims into metadata. It's the most common rejection.
  [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) ·
  [Developer Program Policy](https://play.google.com/about/developer-content-policy/).
- **Tests:** Apple's Product Page Optimization and Google's store listing experiments test screenshots and graphics
  on real traffic. Use them for week 2 instead of guessing.

## The monthly loop
After week 4, run this every month. It takes about an hour.

1. **Read (15 min).** Compare the last 28 days with your baseline in `growth/aso-log.md`. Same window length,
   same countries.
2. **Find the weakest step (5 min).** Use the funnel table. One step, not three.
3. **Change one thing (30 min).** Re-run only the skill for that step. One change per cycle, or you won't know what worked.
4. **Log it (5 min).** Date, what changed, why, and which number you expect to move.
5. **Wait.** Give a metadata change at least 2–4 weeks before judging it; rankings settle slowly. Let A/B tests run
   until the console reports a result.

> **Illustrative example.** A made-up log line, to show the format. These are not real numbers.
>
> | Date | Change | Why | Before (28 d) | After (28 d) | Keep? |
> |---|---|---|---|---|---|
> | 2026-03-02 | Subtitle: "Water tracker" → "Drink reminder & water log" | "reminder" had more searches in keyword sheet | 12,400 impressions · 3.1% CVR | 15,900 impressions · 3.0% CVR | Yes |

## Rules of the road
- **One change at a time.** Two changes in one release = no idea which one worked.
- **Compare like with like.** Same 28-day length, same countries, no launch spikes or holidays in only one window.
- **Fix the product before the page.** If the top review complaint is a bug, no screenshot will outsell it.
- **Localize last, not never.** Once your main language converts, repeat weeks 1–2 for your next biggest country.

## With an AI agent
Installed the skills? Tell your agent: *"Follow the aso-optimization playbook for my app. Start with the week 0
baseline and keep `growth/aso-log.md` up to date."*
Using a chat AI? Open each skill in order and paste its prompt, then paste your funnel numbers when you reach the loop.

## Keep ASO in your repo
Save each output next to your code: `growth/keywords.md`, `growth/listing.md`, `growth/screenshots.md`,
`growth/aso-log.md`. Next month your agent can read the log and tell you what to change.
