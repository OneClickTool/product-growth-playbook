---
name: aso-title-subtitle-optimization
description: Write an App Store title and subtitle (or Google Play title and short description) that rank for chosen keywords, persuade people scrolling search results, and pass store metadata rules. Use when keyword research is done, before a store update, or when someone asks "what should my app name be", "improve my app subtitle", "Google Play short description", or "my listing got rejected for metadata".
license: MIT
metadata:
  category: aso
  difficulty: beginner
  time: 30-45 min
  version: 1.0.0
  author: nvminhtu
---

# Title & Subtitle Optimization

> In 30–45 minutes you will have a title and subtitle (or short description) that fit the limits, carry your top
> keywords, read well to a human, and follow the store rules.

## Goal
The title and subtitle do two jobs at once: they are the strongest ranking signal, and they are the words
people read in search results before deciding to tap. Optimize for both, not just keywords.

## When to use
- You finished [aso-keyword-research](../aso-keyword-research/SKILL.md) and have a ranked keyword list.
- Your conversion from search results to page views or installs is low.
- A listing was rejected for its name or subtitle.
- **Not for:** choosing keywords in the first place → [aso-keyword-research](../aso-keyword-research/SKILL.md).

## Inputs
- Brand name, and whether it's already known.
- Top 5 keyword phrases from keyword research, in priority order.
- The single benefit that makes someone choose you over the top 3 results.
- Current title, subtitle and conversion numbers, if the app is live.

## Store rules (the ones that cause rejections)

| | App Store | Google Play |
|---|---|---|
| Limits | Title 30 · subtitle 30 characters | Title 30 · short description 80 characters |
| Not allowed | Other apps' names, trademarks you don't own, prices or offers, unverifiable claims | Emoji and emoticons, repeated special characters, ALL CAPS (unless it's the brand), ranking or performance claims such as "#1", "best", "top", "free", prices and promotions in the title |
| Tip | Words in the title and subtitle don't need repeating in the keyword field | The short description is indexed and shown under screenshots, so write it as a sentence |

## Steps
1. **Choose the title pattern (5 min).**
   - Unknown brand: `Brand: Keyword Phrase` ("Sipwell: Water Reminder"). The phrase does the ranking.
   - Known brand, or the brand says what it does: brand alone or `Brand – Short Phrase`.
   Put the most valuable keyword phrase in the title, not the subtitle.
2. **Write the subtitle as a benefit (10 min).** Use the next 1–2 keyword phrases, but make it a reason to tap:
   an outcome ("Drink more, feel better"), a differentiator ("No ads, works offline") or the audience ("For
   night-shift nurses"). Avoid repeating title words, since they add no ranking value on iOS.
3. **Generate 10 combinations and score them (10 min).** For each, check: character count ✔, top-2 keywords
   covered ✔, reads naturally ✔, differentiates from the top 3 results ✔, no rule violations ✔.
4. **Test by looking at it in context (5 min).** Put your top 3 candidates next to the current top 5 search results
   (a screenshot or a quick mock). Ask 3 people from your audience which one they'd tap and why.
5. **Ship one change and measure.** Neither store lets you A/B test the title. Change it with an app update, then
   compare impressions, page-view rate and installs for 2–4 weeks before vs after. On Google Play you *can* A/B
   test the short description with store listing experiments.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are an ASO copywriter. Write my app's title and subtitle.

App: {{what it does, who for}}   Brand: {{brand name}}   Brand is known? {{yes/no}}
Store(s): {{App Store / Google Play}}   Language + country: {{...}}
Keyword phrases in priority order: {{from keyword research}}
Why people should pick us over the top results: {{one benefit}}
Top 3 competitor titles and subtitles: {{...}}

Rules: App Store title ≤30, subtitle ≤30; Google Play title ≤30, short description ≤80.
No competitor names or trademarks, no prices or promotions, no "#1/best/top/free", no emoji,
no unverifiable claims. On iOS, don't repeat words between title and subtitle.

Give 10 options as a table: title | subtitle/short description | char counts | keywords covered |
why someone would tap it. Then recommend one and explain in two sentences.
Finally list the keywords now covered, so I can remove them from the iOS keyword field.
````

## Example output

> **Illustrative example.** Fictional app, shown for format.

| Title (chars) | Subtitle (chars) | Keywords covered | Verdict |
|---|---|---|---|
| Sipwell: Water Reminder (23) | Drink Tracker & Hydration Log (29) | water reminder, drink tracker, hydration, water log | ✅ Pick: ranks for the top 4 phrases, and the subtitle says what you get |
| Sipwell – Hydration App (23) | Stay Healthy Every Day (22) | hydration | ❌ "app" is wasted, and the subtitle is generic |
| #1 Water Tracker – Sipwell (26) | Best Free Drink Reminder (24) | water tracker | ❌ "#1", "Best" and "Free" break the rules |

## Common mistakes
- **Brand only, when nobody knows the brand.** You give up the strongest ranking slot.
- **Keyword soup.** "Water Tracker Drink Reminder Log" might rank, but people won't tap it and reviewers may reject it.
- **Changing title, icon and screenshots in the same update.** You won't know which change moved the numbers.
- **Copying a competitor's pattern word for word.** You'll look like the copy, not the choice.

## Related skills
- [aso-keyword-research](../aso-keyword-research/SKILL.md): pick the phrases first.
- [aso-screenshot-strategy](../aso-screenshot-strategy/SKILL.md): the next thing people see in search results.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Rules from Apple's App Store Review Guidelines (2.3.7, metadata)
and Google Play's Metadata policy. Check both before submitting.
