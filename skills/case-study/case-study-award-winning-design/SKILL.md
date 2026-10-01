---
name: case-study-award-winning-design
description: Study award-winning and top-ranked products (Apple Design Awards, App Store Awards, Google Play Best of, Product Hunt Golden Kitty and top-of-the-day launches, Chrome Web Store Featured) to find the design patterns they share at the moments that drive growth (store page, onboarding, paywall, launch page, shareable moments), check them against real growth signals, and turn 3 of them into an apply plan. Produces a result report, an apply plan and a reference list. Use when redesigning onboarding, a paywall or a store page, when preparing a Product Hunt launch, or when someone asks "what do Apple Design Award winners have in common", "learn from top Product Hunt products", "Google Play best apps design", "design inspiration that converts", or "design case study".
license: MIT
metadata:
  category: case-study
  difficulty: intermediate
  time: 2-3 h
  version: 1.0.0
  author: nvminhtu
---

# Award-Winning Design Study

> In 2–3 hours you will have 8–10 award winners and top launches tagged by design pattern, the 3 patterns that also
> show real growth signals, and a plan to apply them to your product with one skill and one metric each.

## Goal
Learn *growth-relevant* design from products that editors, juries or the community already picked as the best, without
confusing "won a design award" with "grew". The output is a result report, an apply plan and a reference list you can
reuse next quarter.

## When to use
- You are redesigning onboarding, a paywall, the store page or a launch page and want proven patterns, not taste.
- You are about to launch on Product Hunt and want to see how top products present themselves.
- You want design ideas you can defend with evidence ("3 of 10 winners do this, and all 3 have 10k+ ratings").
- **Not for:** your direct rivals → [case-study-competitor-teardown](../case-study-competitor-teardown/SKILL.md).
  Founder growth stories with revenue → [case-study-success-story-analysis](../case-study-success-story-analysis/SKILL.md).
  Pure visual inspiration (colors, fonts) with no growth goal: use a gallery, not this skill.

## Inputs
- Your product: platform, category, price model, audience.
- **One growth moment** to improve (pick one): store page · onboarding / first run · paywall · launch page ·
  shareable moment (what makes people show it to a friend).
- A device or browser to open the winners yourself, and a private folder for your own screenshots.

## Where to find winners

Full list with what each source proves and doesn't: [references/sources.md](references/sources.md).

| Source | Picked by | Best for | Link |
|---|---|---|---|
| Apple Design Awards | Apple jury, 6 categories (e.g. Interaction, Visuals and Graphics) | Onboarding, interaction, visual identity on Apple platforms | [developer.apple.com/design/awards](https://developer.apple.com/design/awards/) |
| App Store Awards | App Store editors, per device, plus Cultural Impact | Polished apps with broad appeal | [Apple Newsroom, 2025 winners](https://www.apple.com/newsroom/2025/12/apple-unveils-the-winners-of-the-2025-app-store-awards/) |
| Google Play Best of | Google Play editors, many categories (e.g. Best Hidden Gem, Best for Large Screens) | Android apps and games; varies by country | [blog.google, Best of 2025](https://blog.google/products-and-platforms/platforms/google-play/best-apps-games-2025/) |
| Product Hunt Golden Kitty | Community vote, by category | Web, SaaS, AI and dev tools; launch pages | [producthunt.com/golden-kitty-awards](https://www.producthunt.com/golden-kitty-awards/hall-of-fame) |
| Product Hunt leaderboard | Daily / weekly / monthly upvotes | How top launches present themselves today | [producthunt.com/leaderboard](https://www.producthunt.com/leaderboard) |
| Chrome Web Store Featured badge | Chrome team | Browser extensions | [developer.chrome.com/docs/webstore/discovery](https://developer.chrome.com/docs/webstore/discovery) |

## Steps
1. **Set the lens (10 min).** Write one line: *"I study {{growth moment}} for a {{platform}} {{category}} app with
   {{price model}}."* Everything you collect must be about that moment. One moment per study.
2. **Pick 8–10 winners + 2–3 controls (30 min).** Use at least 2 sources. Prefer the same platform and a similar
   price model, and prefer the last 3 years (design ages fast). **Controls** are finalists that didn't win, or popular
   apps in the same category with no award. They tell you whether a pattern actually makes a difference.
3. **Capture evidence (45 min).** For each product, open it and go through the growth moment yourself. Save: link,
   award and year (with the source link), date you looked, and your own screenshots **in your private research folder**.
   Don't publish other companies' screenshots; link to them.
4. **Tag patterns (20 min).** Use the fixed tags in [references/pattern-taxonomy.md](references/pattern-taxonomy.md)
   so products can be compared. Add a new tag only if 2+ products share it.
5. **Count (10 min).** Build the pattern × product matrix in [assets/result-report.md](assets/result-report.md). Keep
   the patterns used by **3+ winners** and note whether the controls use them too. If the controls do it just as much,
   the pattern is table stakes, not a differentiator.
6. **Check growth signals (20 min).** An award is a jury's opinion, not growth. For each product, add what is
   **public**: rating count, rank, Product Hunt upvotes and rank, review snippets that mention the pattern. Write
   `no public data` when there is none. Never estimate downloads or revenue. Grade each pattern:
   **High** (3+ winners, public growth signal, rare in controls) · **Medium** (3+ winners, no growth signal) ·
   **Low** (fewer than 3, or common in controls).
7. **Write the apply plan (20 min).** Pick up to 3 High/Medium patterns. For each: **Copy / Adapt / Skip**, why it fits
   your product, the skill in this repo that carries it out, the metric you'll watch and the baseline today. Use
   [assets/apply-plan.md](assets/apply-plan.md).
8. **Save and revisit (5 min).** Save the report and plan as research notes
   ([research-doc-organization](../../research/research-doc-organization/SKILL.md)). Re-check the metric after 30 days,
   then write up what happened with [case-study-write-your-own](../case-study-write-your-own/SKILL.md).

### Where each pattern goes next

| Growth moment | Apply it with |
|---|---|
| Store page (icon, screenshots, preview) | [aso-screenshot-strategy](../../aso/aso-screenshot-strategy/SKILL.md) · [aso-title-subtitle-optimization](../../aso/aso-title-subtitle-optimization/SKILL.md) |
| Onboarding / first run | No onboarding skill yet: test the change by hand with [launch-get-first-100-users](../../launch/launch-get-first-100-users/SKILL.md) (step 5, onboard people yourself) and watch day-1 retention |
| Paywall | [monetization-paywall-design](../../monetization/monetization-paywall-design/SKILL.md) |
| Launch page | [launch-product-hunt-launch](../../launch/launch-product-hunt-launch/SKILL.md) · [launch-post-writing](../../launch/launch-post-writing/SKILL.md) |
| Shareable moment | [launch-get-first-100-users](../../launch/launch-get-first-100-users/SKILL.md) |

## Prompt (copy-paste)
Works best with web browsing. Replace everything in `{{ }}`.

````text
You are a product designer who cares about growth. Help me learn from award-winning and top-ranked products.

My product: {{what it does}}   Platform: {{iOS / Android / web / extension / ...}}
Category: {{...}}   Price model: {{...}}   Growth moment to study: {{store page / onboarding / paywall / launch page / shareable moment}}

1. From at least 2 of these sources, find 8-10 winners from the last 3 years that are comparable to my product:
   Apple Design Awards (developer.apple.com/design/awards), App Store Awards (Apple Newsroom), Google Play Best of
   (blog.google), Product Hunt Golden Kitty and leaderboard, Chrome Web Store Featured. Also find 2-3 controls
   (finalists that didn't win, or popular apps in the category without an award).
   For each: name, link, award + year, and the source link for the award. Never invent a winner, award, link or
   number. If you can't browse, give me the exact pages and searches to check instead.
2. For each product, describe the {{growth moment}} using these tags: first-value time, sign-up wall, permission
   timing, personalization question, demo/sample content, progress indicator, mascot/character, signature
   motion, empty state, paywall timing, plan layout, social proof, share prompt, store screenshot narrative,
   launch tagline, launch gallery. Mark anything you could not verify as "unverified".
3. Build a table: pattern | # winners using it | # controls using it | public growth signal (with link, or
   "no public data") | evidence grade (High / Medium / Low).
4. Recommend up to 3 patterns for my product. For each: Copy / Adapt / Skip, why it fits, the first concrete change,
   and one metric to measure before and after.
5. End with a reference list of every link used.
````

## Example output

> **Illustrative example.** Product names and counts are made up to show the format. Use real winners and cite them.

*Lens:* onboarding for an iOS habit app, freemium subscription. 9 winners (ADA, App Store Awards, Google Play Best of),
3 controls.

| Pattern | Winners (of 9) | Controls (of 3) | Public growth signal | Grade |
|---|---|---|---|---|
| Value before sign-up (use the app, then create an account) | 7 | 1 | 6 of 7 have 10k+ ratings (store pages, looked 2026-10-01) | **High** |
| One personalization question that changes the first screen | 5 | 0 | Reviews mention "felt made for me" (4 apps) | **High** |
| Mascot or character that reacts to progress | 4 | 0 | no public data | **Medium** |
| Notification permission asked after the first win, not at launch | 6 | 2 | no public data | **Medium** |
| 4-screen swipe tutorial before the app | 1 | 3 | none | **Low**, skip |

**Apply plan**

| # | Pattern | Decision | First change | Skill | Metric (baseline) |
|---|---|---|---|---|---|
| 1 | Value before sign-up | Copy | Let people log 1 habit before the account screen | [launch-get-first-100-users](../../launch/launch-get-first-100-users/SKILL.md) (watch 5 users try it) | Day-1 retention (31%) |
| 2 | One personalization question | Adapt | Ask "morning or evening?" and pre-fill 3 habits | same | Onboarding completion (58%) |
| 3 | Permission after first win | Copy | Move the push prompt after the first check-in | same | Push opt-in rate (40%) |

## Common mistakes
- **Treating an award as proof of growth.** Juries judge craft. Always add a growth signal or mark it `no public data`.
- **Studying everything at once.** Onboarding, paywall and store page in one study turns into a mood board. One moment.
- **No controls.** Without them you can't tell a differentiator from table stakes.
- **Non-comparable winners.** A big-studio game's onboarding rarely fits a solo developer's utility.
  Match platform and price model first.
- **Copying the look, not the mechanism.** Copy *why* it works (value before sign-up), not the colors.
- **Publishing other companies' screenshots** in your repo, blog or report. Link to the store page instead.
- **Stale winners.** Design conventions change; prefer the last 3 years and note the year on every row.

## Related skills
- [case-study-competitor-teardown](../case-study-competitor-teardown/SKILL.md): the same method for your direct rivals.
- [case-study-success-story-analysis](../case-study-success-story-analysis/SKILL.md): growth tactics, not design.
- [research-review-mining](../../research/research-review-mining/SKILL.md): find reviews that mention the pattern.
- [research-source-finding](../../research/research-source-finding/SKILL.md): judge how strong each signal is.
- [case-study-write-your-own](../case-study-write-your-own/SKILL.md): share the result after 30 days.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: [Apple Design Awards](https://developer.apple.com/design/awards/),
[2025 App Store Awards](https://www.apple.com/newsroom/2025/12/apple-unveils-the-winners-of-the-2025-app-store-awards/),
[Google Play Best of 2025](https://blog.google/products-and-platforms/platforms/google-play/best-apps-games-2025/),
[Product Hunt Golden Kitty Awards](https://www.producthunt.com/golden-kitty-awards/hall-of-fame),
[Chrome Web Store discovery](https://developer.chrome.com/docs/webstore/discovery). Full list in
[references/sources.md](references/sources.md).
