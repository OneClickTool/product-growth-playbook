---
name: launch-product-hunt-launch
description: Plan a Product Hunt launch end to end, including whether to launch at all, the day, listing copy, gallery, maker comment, supporter list and a 24-hour schedule, without breaking Product Hunt's rules on vote solicitation. Use when someone says "launch on Product Hunt", "PH launch", "Product Hunt tips", "should I launch on Product Hunt", or is preparing a launch day for a SaaS, app, AI tool or extension.
license: MIT
metadata:
  category: launch
  difficulty: intermediate
  time: 60 min to plan, 2-3 weeks to prepare
  version: 1.0.0
  author: nvminhtu
---

# Product Hunt Launch

> In an hour you will have a go/no-go decision, the listing copy, a supporter list plan and an hour-by-hour
> launch-day schedule.

## Goal
Use Product Hunt for what it is good at: a burst of early adopters, feedback, backlinks and social proof.
Don't bet the whole launch on the rank.

## When to use
- The product is live and someone can try it in under 2 minutes.
- Your audience overlaps with Product Hunt's: makers, developers, designers, marketers, AI and productivity tools.
- **Probably skip or delay** if the product is niche for non-tech users (e.g. a local-bakery app), or if you have
  nobody to tell on the day. Use [launch-get-first-100-users](../launch-get-first-100-users/SKILL.md) first.

## Inputs
- Live product URL, pricing, and any launch-day offer.
- Logo, 3–6 gallery images or a short video, a demo GIF.
- Your audience: email list, social followers, communities, friends who are active Product Hunt members.

## How the day works
- A Product Hunt day runs from **12:01 a.m. to 11:59 p.m. Pacific Time**. Everyone launching that day competes on
  that 24-hour clock.
- Launches are reviewed, and not every product is **featured** on the homepage. A clear, finished product with a good
  listing is more likely to be featured.
- Product Hunt prohibits asking people to **upvote** and detects vote rings and new accounts voting in bursts.
  Ask people to **check it out and share feedback**. Votes from brand-new accounts may be discounted.
- You can hunt your own product. You don't need a famous hunter.

## Steps
1. **Go / no-go (5 min).** Can a stranger get value in 2 minutes without talking to you? Do you have 100+ people to
   notify? If both are no, fix those first.
2. **Pick the day (5 min).** Tuesday–Thursday gets the most traffic and the most competition. Weekends are
   quieter and easier to rank on, with less traffic. For a first launch with a small audience, a weekend or Monday is fine.
3. **Write the listing (20 min).**
   - **Name + tagline:** the tagline says what it does for whom, not a slogan. "Invoices that chase late clients for
     you" beats "The future of billing". Keep it within the form's character limit.
   - **Gallery:** image 1 = the result/outcome, 2 = how it works, 3 = what makes it different, then a 30–60 s video.
   - **Maker comment:** why you built it (a personal story in 2–3 sentences), what it does, what's free / the launch
     offer, and one specific question you want feedback on.
4. **Build the supporter list (2–3 weeks before).** List everyone who might care, split into: email list, personal
   contacts, communities, and people you helped before. Warm them up with a "launching on <date>, would love your
   feedback" note a week ahead.
5. **Schedule the launch** in Product Hunt a few days early and check the preview on desktop and mobile.
6. **Launch-day schedule.**
   - 00:01 PT: launch goes live. Post the maker comment immediately.
   - 00:05–02:00 PT: send the first wave (email list, closest supporters). Link to the PH page, ask for feedback.
   - Morning PT / Europe afternoon: social posts, communities where it's allowed, second email to people who didn't open.
   - All day: **reply to every comment** within an hour. Thoughtful replies attract more visitors than anything else.
   - Evening: thank-you post with what you learned. Screenshot results for later.
7. **Day after.** Add a "Featured on Product Hunt" badge if you were featured, email new sign-ups personally, and turn
   the feedback into a changelog post.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are a Product Hunt launch coach. Help me prepare.

Product: {{what it does, who for, URL}}
Pricing / launch offer: {{...}}
Time to first value for a new user: {{e.g. 1 minute, no signup}}
Audience I can notify: {{email list size, followers, communities}}
Timezone: {{my timezone}}

1. Go/no-go: judge whether I'm ready based on time-to-value and audience size. If not ready, say what to fix.
2. Recommend a launch day and explain the traffic vs competition trade-off for my case.
3. Write: 5 tagline options (what it does + for whom, no hype), a 3-image gallery plan with the headline for
   each image, and a maker comment (under 150 words) ending with one specific feedback question.
4. Write a "launching next week" message and a launch-day message for supporters. Ask for feedback,
   NEVER ask for upvotes (Product Hunt forbids it).
5. A launch-day schedule in Pacific Time AND my timezone, with who does what.
````

## Example output

> **Illustrative example.** Fictional product, shown for format.

**Tagline:** Invoices that politely chase late clients for you
**Gallery:** ① "Get paid 2× faster" (dashboard with paid invoices) ② "Set reminders once" (reminder settings)
③ "Built for freelance designers" (templates)
**Maker comment:**
> Hi PH 👋 I'm a freelance designer who once waited 94 days for an invoice. Invoicely Lite sends friendly reminders
> on a schedule you set, so you never have to write the awkward email. Free for 3 clients, and 50% off Pro for PH
> this week. **Question for you:** what's the one reminder you'd never want sent automatically?

## Common mistakes
- **Asking for upvotes.** It breaks the rules, can get the launch penalised, and annoys your supporters.
- **Launching something people can't try.** A waitlist or "book a demo" gets far less engagement than a live product.
- **Going quiet after 9 a.m.** Unanswered comments stall a launch. Block the whole day.
- **Treating the rank as the goal.** Measure sign-ups, activated users and feedback, not the badge.

## Related skills
- [launch-pre-launch-checklist](../launch-pre-launch-checklist/SKILL.md): tracking and assets before the day.
- [launch-post-writing](../launch-post-writing/SKILL.md): posts for other channels on the same day.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Rules from Product Hunt's help center and community guidelines
(launch timing, featuring, vote solicitation). Check the current versions before launching.
