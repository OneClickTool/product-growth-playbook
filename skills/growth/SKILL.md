---
name: growth
description: Entry point for the Product Growth Playbook. Asks what stage a digital product (app, SaaS, game, AI tool, website, browser extension) is at and routes to the right growth skill: ASO, launch or monetization. Use when someone says "how do I grow my app", "get more users", "where do I start with marketing", "I just launched and nobody downloads it", or is unsure which growth skill to use.
license: MIT
metadata:
  category: router
  difficulty: beginner
  time: 5 min
  version: 1.0.0
  author: nvminhtu
---

# Growth: where to start

> Five minutes to pick the one growth task that matters most for your product right now.

## Goal
Point the user to a single next skill and explain why. Do not run through every skill.

## When to use
- The user is not sure what to work on next.
- The user asks a broad question ("how do I grow?").

## Inputs
Ask these, **one message, at most 4 questions**. Skip any the user already answered:
1. What is the product, and where does it live (App Store, Google Play, web, Chrome Web Store…)?
2. Stage: just an idea · building, not launched · launched < 3 months · launched longer?
3. Rough numbers: users or downloads per week, and whether it makes money yet.
4. The one thing that feels most broken right now.

## Steps
1. Ask the questions above and wait for the answer.
2. Match the answer against the table below. Pick **one** skill (two at most) and give the reason in one sentence.
3. If nothing in the table fits (SEO, retention, analytics…), say the repo doesn't cover it yet, give the 3–5 most
   important actions from general knowledge, and point to the repo's issues page so the user can request it.
4. When the user finishes a skill, come back here and pick the next one. For a full launch route, suggest
   [playbooks/launch-a-product.md](../../playbooks/launch-a-product.md).

| Situation | Skill |
|---|---|
| **Idea / research** | |
| Not sure people want it; looking for a niche | [research-where-users-ask](../research/research-where-users-ask/SKILL.md) |
| Want to know what users hate about competitors | [research-review-mining](../research/research-review-mining/SKILL.md) |
| Need facts or sources you can trust | [research-source-finding](../research/research-source-finding/SKILL.md) |
| Research is scattered across tabs and chats | [research-doc-organization](../research/research-doc-organization/SKILL.md) |
| **Pre-launch** | |
| Launch is weeks away, not sure what's missing | [launch-pre-launch-checklist](../launch/launch-pre-launch-checklist/SKILL.md) |
| Need launch posts for HN / Reddit / X / LinkedIn | [launch-post-writing](../launch/launch-post-writing/SKILL.md) |
| Considering Product Hunt | [launch-product-hunt-launch](../launch/launch-product-hunt-launch/SKILL.md) |
| **Just launched** | |
| Fewer than 100 real users | [launch-get-first-100-users](../launch/launch-get-first-100-users/SKILL.md) |
| **App store growth** | |
| Few installs from store search | [aso-keyword-research](../aso/aso-keyword-research/SKILL.md) |
| Has keywords, needs a better name / subtitle | [aso-title-subtitle-optimization](../aso/aso-title-subtitle-optimization/SKILL.md) |
| Store visitors don't install | [aso-screenshot-strategy](../aso/aso-screenshot-strategy/SKILL.md) |
| Low rating or few ratings | [aso-review-and-rating-strategy](../aso/aso-review-and-rating-strategy/SKILL.md) |
| **Making money** | |
| Unsure what should be free / trial length | [monetization-free-trial-vs-freemium](../monetization/monetization-free-trial-vs-freemium/SKILL.md) |
| Unsure what to charge | [monetization-pricing-strategy](../monetization/monetization-pricing-strategy/SKILL.md) |
| Has a paywall, low conversion or rejected | [monetization-paywall-design](../monetization/monetization-paywall-design/SKILL.md) |
| One plan, very different customers | [monetization-subscription-tiers](../monetization/monetization-subscription-tiers/SKILL.md) |

## Prompt (copy-paste)
For chat assistants that can't install skills:

````text
You are a growth advisor for people building digital products. Ask me at most 4 short questions:
what the product is and where it's distributed, its stage (idea / pre-launch / <3 months / longer),
rough weekly users and revenue, and what feels most broken. Then recommend ONE growth task to
focus on for the next two weeks, explain why in one sentence, and give me the first 3 concrete steps.
Choose from: where users ask about software, competitor review mining, source finding,
research doc organization, pre-launch checklist, launch post writing, Product Hunt launch, getting the first 100 users,
ASO keyword research, ASO title & subtitle, ASO screenshots, ratings & reviews, free trial vs freemium,
pricing strategy, paywall design, subscription tiers.
````

## Example output
> You're 6 weeks after launch with ~15 installs a week, almost all from friends. The store isn't sending
> you anyone, so start with **aso-keyword-research**: your title currently only contains the brand name.
> Come back after the update ships and we'll look at screenshots.

## Common mistakes
- Recommending five things at once. One focus for two weeks beats five half-done tasks.
- Jumping to monetization before anyone uses the product.

## Related skills
See the table in *Steps*, and the full list in the repository [README](../../README.md).

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu).
