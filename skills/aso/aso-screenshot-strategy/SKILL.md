---
name: aso-screenshot-strategy
description: Plan the App Store and Google Play screenshot set (order, captions, visual style and what to test) so the first two or three screenshots sell the app in search results. Use when preparing a first release, when store page conversion is low, when redesigning screenshots, or when someone asks "what should my app screenshots show", "screenshot captions", "why do people view my page but not install", or "product page optimization".
license: MIT
metadata:
  category: aso
  difficulty: intermediate
  time: 45-60 min to plan
  version: 1.0.0
  author: nvminhtu
---

# Screenshot Strategy

> In under an hour you will have a shot list: each screenshot's message, caption, visual, plus which variant to test.

## Goal
Most people decide from the first 2–3 screenshots, often as small thumbnails in search results, without reading
the description. Each of those screenshots should sell one benefit you can read at a glance.

## When to use
- First release, or a redesign.
- Plenty of impressions or page views, but a low install rate.
- **Not for:** words in search results → [aso-title-subtitle-optimization](../aso-title-subtitle-optimization/SKILL.md).

## Inputs
- The 3–5 reasons people choose your app. Use reviews ("I love that it…") and support emails, not your feature list.
- Your top competitors' first 3 screenshots (screenshot them from search results on a phone).
- Real app screens for each benefit.
- Current store conversion rate if live (App Store Connect → App Analytics; Play Console → Store performance).

## Know the canvas

| | App Store | Google Play |
|---|---|---|
| Screenshots | Up to 10 per device size | 2–8 per device type |
| Video | Up to 3 app previews, 15–30 seconds each | 1 YouTube promo video |
| Other | — | Feature graphic 1024 × 500 |
| Built-in A/B test | Product Page Optimization: up to 3 treatments against the original | Store listing experiments |

Required sizes change with new devices. Check the current screenshot specifications before exporting.

## Steps
1. **List benefits, not features (10 min).** Turn each feature into an outcome: "Reminders" → "Never forget to
   drink water". Rank them by how often reviews mention them.
2. **Assign the first three slots (10 min).**
   1. The core outcome: the main reason to install, shown in the hero screen.
   2. The key differentiator: what the top competitors don't do or don't say.
   3. Proof or ease: "Set up in 30 seconds", ratings, awards, or a second strong benefit.
   Slots 4+ cover secondary features for people who scroll. Fewer people see them.
3. **Write captions (10 min).** 2–6 words, large enough to read on a thumbnail, verb or outcome first
   ("Track every sip", not "Tracking feature"). One idea per screenshot.
4. **Pick a visual style (10 min).** A background colour that stands out against competitors' in search results.
   Device frame or no frame. Real UI, zoomed to the part that matters. Keep it the same across the whole set.
   If most competitors use light backgrounds, a dark set stands out, and vice versa.
5. **Localize the captions** for your top markets. Captions are text people read, so translate them like copy.
6. **Plan one test (5 min).** Test *one* variable, usually screenshot 1's message or the overall style, using
   Product Page Optimization or store listing experiments. Run it until the console shows a confident result.
   Don't stop it after a couple of days.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are an ASO creative strategist. Plan my app store screenshots.

App: {{what it does, who for}}
Store(s): {{App Store / Google Play}}
Why users love it (from reviews / support): {{quotes}}
Top 3 competitors' first screenshots (describe captions + style): {{...}}
Current conversion rate (if known): {{...}}

1. Turn features into ranked benefits (use the review quotes as evidence).
2. Shot list for screenshots 1-6: slot | message | caption (2-6 words, outcome first) |
   which screen to show and what to zoom in on | why it's in this position.
   Slot 1 = core outcome, slot 2 = differentiator vs the competitors above, slot 3 = proof or ease.
3. Visual direction that stands out from those competitors in search results (colour, framing, typography).
4. One A/B test: the single variable, the hypothesis, and the metric.
````

## Example output

> **Illustrative example.** Fictional app, shown for format.

| Slot | Message | Caption | Screen |
|---|---|---|---|
| 1 | Core outcome | **Drink more water, effortlessly** | Today ring at 80%, zoomed |
| 2 | Differentiator | **Reminders that fit your workday** | Schedule with meetings greyed out |
| 3 | Ease | **Log a glass in one tap** | Widget on the lock screen |
| 4 | Secondary | **See your week at a glance** | Weekly chart |
| 5 | Secondary | **No ads. No account needed.** | Settings / privacy screen |

Test: slot 1 caption *"Drink more water, effortlessly"* vs *"Hit your water goal every day"*. Metric: conversion rate.

## Common mistakes
- **Raw screenshots with no captions.** People don't understand your UI at thumbnail size.
- **Leading with onboarding or a login screen.** Your first slot is the most valuable space on the page.
- **Captions that list features** ("Statistics, Widgets, Themes"). Sell the outcome instead.
- **Testing five things at once,** or stopping the test early.

## Related skills
- [aso-title-subtitle-optimization](../aso-title-subtitle-optimization/SKILL.md): the text next to your screenshots.
- [aso-review-and-rating-strategy](../aso-review-and-rating-strategy/SKILL.md): reviews show up on the same page.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Limits from App Store Connect Help ("Screenshot specifications",
"App preview specifications", "Product page optimization") and Play Console Help ("Add preview assets", "Store listing
experiments").
