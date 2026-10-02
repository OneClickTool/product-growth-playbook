---
name: strategy-contrarian-marketing
description: Find growth and money-making moves your competitors aren't making, by listing what everyone in your niche does and deliberately inverting it. Uses inversion ("how would we guarantee failure?"), channel gaps, side-door distribution (free tools, integrations, marketplaces, other people's audiences), price and offer inversion, and "do things that don't scale", then turns the best ideas into 3 cheap, honest experiments with a pass/fail number. Use when someone says "think differently about marketing", "traditional marketing doesn't work for us", "everyone does the same thing", "how to stand out", "unconventional growth ideas", "growth hacks that aren't spam", "reverse thinking", "tư duy ngược", "đừng đi theo lối mòn", or has tried the usual channels without results.
license: MIT
metadata:
  category: strategy
  difficulty: intermediate
  time: 60 min
  version: 1.0.0
  author: nvminhtu
---

# Contrarian Marketing: Go Where Others Don't

> In an hour you'll have a map of what everyone in your niche does, the inverted version of each move, and 3 cheap
> experiments that only you are running.

## Goal
When every competitor posts the same content in the same places with the same offer, the cheapest attention is
wherever they aren't. This skill is a structured way to find those gaps without crossing into spam, fake scarcity
or anything you'd be embarrassed to explain to a user.

## When to use
- Your niche is crowded and every product sounds the same.
- You tried the "standard" launch (Product Hunt, a few posts, maybe ads) and it didn't move.
- You want ideas that cost time and thinking, not money.
- **Not for:** ranking cheap, proven channels → [launch-quick-download-wins](../../launch/launch-quick-download-wins/SKILL.md).
  Learning what one competitor does in detail → [case-study-competitor-teardown](../../case-study/case-study-competitor-teardown/SKILL.md).

## Inputs
- Your product, who it's for, and your price.
- 3–5 competitors (names and links).
- What you've already tried and what happened.
- Your unfair advantages, however small: a skill, a language, a community you belong to, a niche you know well.

## Steps
1. **Map the herd (15 min).** For your 3–5 competitors, fill one row each: where they get users, what content they
   post, their offer (free / trial / price), their message (the main claim), and who they ignore. Look at their
   store pages, social accounts, ad libraries and launch history.
2. **Run inversion.** Answer two questions in writing:
   - *"How would we guarantee nobody ever uses this?"* (e.g. sound like everyone else, target everyone, hide the
     price, make sign-up long). Then do the opposite of each answer.
   - *"What does everyone here believe that might be wrong?"* (e.g. "you need a big launch", "users won't pay for
     this", "you need TikTok"). Each wrong belief is a possible edge.
3. **Look for gaps with these 6 lenses.** For each, write at least one idea:

   | Lens | Ask | Example move |
   |---|---|---|
   | **Channel gap** | Where are users that competitors don't post? | A non-English community, a niche forum, a professional group, offline meetups |
   | **Audience gap** | Who do competitors ignore or serve badly? | Older users, a specific job, a region, people who hate subscriptions |
   | **Side door** | Whose audience can you reach by being useful *inside* their product? | An integration, a template on a marketplace, a plugin, a free tool listed in a directory |
   | **Free-tool bait** | What small problem can a free tool or page solve that leads to your product? | A calculator, a checker, a generator, an open-source repo ([launch-open-source-funnel](../../launch/launch-open-source-funnel/SKILL.md)) |
   | **Offer inversion** | What do others charge for that you can give free, or give free that you can charge for? | A one-time price where everyone rents, a free tier where everyone has trials, a paid "done for you" version of a free tool |
   | **Unscalable** | What can you do by hand for 50 people that no company would do? | Personal onboarding calls, a hand-written reply to every review, custom setups for the first users |

4. **Run the honesty filter.** Drop any idea that needs fake scarcity, fake reviews, hidden self-promotion, scraped
   contact lists, mass DMs, or claims you can't prove. Contrarian means *different*, not *deceptive*.
   ([social-credible-posting](../../social/social-credible-posting/SKILL.md) covers the trust rules.)
5. **Score what's left.** Each idea gets 1–5 on: cost (cheap = 5), speed to a signal (days = 5), how hard it is for
   competitors to copy, and fit with your unfair advantage. Keep the top 3.
6. **Write each as an experiment.** One line each: *"If we do X for Y days, we expect Z. Pass if ≥ N; otherwise stop."*
   Run them one after another, not all at once, so you know what worked.
7. **Save** as `growth/contrarian-bets.md`, and log the results in
   [strategy-spend-and-timing](../strategy-spend-and-timing/SKILL.md)'s Monday review.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are a contrarian growth strategist for indie products. Your ideas must be honest: no fake scarcity, no fake
reviews, no hidden self-promotion, no spam or scraped lists. Don't invent facts about competitors; if you don't
know, say what I should check.

My product: {{what, who for, platform, price}}
Competitors: {{names + links}}
What they do (my notes): {{channels, content, offer, message}}
What I tried and the results: {{...}}
My unfair advantages: {{skills, language, communities, niche knowledge}}

1. Make a "herd map" table: what most competitors do for channel, content, offer, message, and who they ignore.
2. Inversion: list 6 ways to guarantee failure in this niche, and the opposite of each.
3. List 5 beliefs everyone in this niche holds that might be wrong, and how I'd test each cheaply.
4. Give at least one idea per lens: channel gap, audience gap, side door, free-tool bait, offer inversion, unscalable.
5. Remove anything that fails the honesty filter, score the rest (cost, speed, hard to copy, fits my advantage),
   and write the top 3 as experiments: "If we do X for Y days, we expect Z. Pass if >= N."
````

## Example output

> **Illustrative example.** A fictional product and niche.

*Invoice app for freelancers. Competitors: big subscription tools, all advertising "save time" in English, on Google Ads and YouTube.*

| Herd does | Inverted move |
|---|---|
| Monthly subscription | One-time license, "pay once, own it", aimed at people tired of subscriptions |
| English, global | Vietnamese and Thai first, posted in local freelancer Facebook groups (with admin permission) |
| "Save time" message | "Get paid faster": shows days-to-payment before/after |
| Ads | Free "late-payment reminder email generator" page that ranks for the exact phrase |

**Top 3 experiments**
1. Free reminder-email generator page, 14 days, expect 300 visits from search and groups. Pass if ≥ 30 app sign-ups.
2. Vietnamese version + 3 value posts in freelancer groups, 10 days. Pass if ≥ 20 installs from the UTM link.
3. Personal 15-min setup call for the first 20 users. Pass if ≥ 8 of them still invoice in week 3.

## Common mistakes
- **Contrarian for its own sake.** The test is "do users get something better?", not "is it different?".
- **Confusing contrarian with sketchy.** Fake urgency and fake reviews are the oldest trick, not a new one, and
  they destroy trust (and can be illegal).
- **Running all 3 experiments at once.** You won't know which one worked.
- **No pass number.** Write it before you start, or every result will look "promising".
- **Ignoring your unfair advantage.** The best gap is the one competitors *can't* enter easily, like your language
  or your community.

## Related skills
- [strategy-product-as-funnel](../strategy-product-as-funnel/SKILL.md): free tools and apps as entry points to an owned audience.
- [launch-open-source-funnel](../../launch/launch-open-source-funnel/SKILL.md): a free repo as a side door.
- [research-where-users-ask](../../research/research-where-users-ask/SKILL.md): find the channels competitors miss.
- [case-study-competitor-teardown](../../case-study/case-study-competitor-teardown/SKILL.md): fill the herd map with evidence.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Inversion is a classic problem-solving method (often attributed
to the mathematician Carl Jacobi: "invert, always invert"). "Do things that don't scale" is from
[Paul Graham's essay](https://paulgraham.com/ds.html).
