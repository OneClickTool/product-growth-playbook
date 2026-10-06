---
name: growth
description: Entry point for the Product Growth Playbook. Asks what stage a digital product (app, SaaS, game, AI tool, website, browser extension) is at and routes to the right growth skill: strategy, research, listing, ASO, launch, social, monetization or email. Use when someone says "how do I grow my app", "get more users", "where do I start with marketing", "I just launched and nobody downloads it", "I want to make $X in N months", or is unsure which growth skill to use.
license: MIT
metadata:
  category: router
  difficulty: beginner
  time: 5 min
  version: 1.1.0
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
   [playbooks/launch-a-product.md](../../playbooks/launch-a-product.md). For a live app that needs more store installs,
   suggest [playbooks/aso-optimization.md](../../playbooks/aso-optimization.md). For a live product that feels stuck
   across channels (SEO too slow, no reach on X, unsure about Reddit, no ads yet), suggest the step-by-step
   [action plan](action/README.md). For the whole picture (skills, tools,
   official references and templates per stage), point to [playbooks/growth-map.md](../../playbooks/growth-map.md).

| Situation | Skill |
|---|---|
| **Strategy (any stage, start here if there's no target)** | |
| No clear money goal; "I want $X in N months" | [strategy-revenue-target](../strategy/strategy-revenue-target/SKILL.md) |
| Small budget, too many options; something suddenly worked or is sliding | [strategy-spend-and-timing](../strategy/strategy-spend-and-timing/SKILL.md) |
| Crowded niche; the usual channels didn't work; wants unconventional ideas | [strategy-contrarian-marketing](../strategy/strategy-contrarian-marketing/SKILL.md) |
| Several apps or games, every launch starts from zero; wants long-term users | [strategy-product-as-funnel](../strategy/strategy-product-as-funnel/SKILL.md) |
| **Idea / research** | |
| Not sure people want it; looking for a niche | [research-where-users-ask](../research/research-where-users-ask/SKILL.md) |
| Want to know what users hate about competitors | [research-review-mining](../research/research-review-mining/SKILL.md) |
| Need facts or sources you can trust | [research-source-finding](../research/research-source-finding/SKILL.md) |
| Research is scattered across tabs and chats | [research-doc-organization](../research/research-doc-organization/SKILL.md) |
| **Pre-launch** | |
| Launch is weeks away, not sure what's missing | [launch-pre-launch-checklist](../launch/launch-pre-launch-checklist/SKILL.md) |
| App needs Firebase analytics, Crashlytics, AdMob, consent and payments set up and verified | [launch-growth-stack-setup](../launch/launch-growth-stack-setup/SKILL.md) |
| Need launch posts for HN / Reddit / X / LinkedIn | [launch-post-writing](../launch/launch-post-writing/SKILL.md) |
| Want to post on Reddit without getting removed; which subreddits fit; more users from fewer posts | [launch-reddit-posting](../launch/launch-reddit-posting/SKILL.md) |
| Considering Product Hunt | [launch-product-hunt-launch](../launch/launch-product-hunt-launch/SKILL.md) |
| A competitor is winning and you want to know why | [case-study-competitor-teardown](../case-study/case-study-competitor-teardown/SKILL.md) |
| Want proven tactics from products like yours | [case-study-success-story-analysis](../case-study/case-study-success-story-analysis/SKILL.md) |
| Redesigning onboarding, a paywall, the store page or a launch page; want to learn from award winners | [case-study-award-winning-design](../case-study/case-study-award-winning-design/SKILL.md) |
| An experiment or launch just finished | [case-study-write-your-own](../case-study/case-study-write-your-own/SKILL.md) |
| **Publishing** | |
| Submitting to the App Store (first time or update) | [listing-app-store](../listing/listing-app-store/SKILL.md) |
| Submitting to Google Play (incl. 12 testers / 14 days) | [listing-google-play](../listing/listing-google-play/SKILL.md) |
| Publishing a browser extension | [listing-browser-extension](../listing/listing-browser-extension/SKILL.md) |
| Publishing a Mac app | [listing-mac-app](../listing/listing-mac-app/SKILL.md) |
| Publishing an indie game | [listing-indie-game](../listing/listing-indie-game/SKILL.md) |
| Publishing a plugin, CLI or dev tool | [listing-dev-plugin](../listing/listing-dev-plugin/SKILL.md) |
| Publishing an AI tool, GPT, agent skill or MCP server | [listing-ai-product](../listing/listing-ai-product/SKILL.md) |
| Selling a Notion template or digital download | [listing-digital-template](../listing/listing-digital-template/SKILL.md) |
| Want free places to list the product | [listing-free-directories](../listing/listing-free-directories/SKILL.md) |
| **Just launched** | |
| Live, but almost no downloads; need some this week | [launch-quick-download-wins](../launch/launch-quick-download-wins/SKILL.md) |
| Fewer than 100 real users | [launch-get-first-100-users](../launch/launch-get-first-100-users/SKILL.md) |
| Open-source repo with few stars; want to seed it | [launch-github-repo-seeding](../launch/launch-github-repo-seeding/SKILL.md) |
| Repo has stars but no business; wants a free repo to bring users to a product | [launch-open-source-funnel](../launch/launch-open-source-funnel/SKILL.md) |
| **Audience & social** | |
| Wants users from TikTok, Reels or Shorts; videos get few views | [social-short-video](../social/social-short-video/SKILL.md) |
| Posts on X, Threads, Facebook or LinkedIn sound salesy or get ignored | [social-credible-posting](../social/social-credible-posting/SKILL.md) |
| Building, wants an audience waiting on launch day | [social-build-in-public](../social/social-build-in-public/SKILL.md) |
| **App store growth** | |
| Few installs from store search | [aso-keyword-research](../aso/aso-keyword-research/SKILL.md) |
| Has keywords, needs a better name / subtitle | [aso-title-subtitle-optimization](../aso/aso-title-subtitle-optimization/SKILL.md) |
| Store visitors don't install | [aso-screenshot-strategy](../aso/aso-screenshot-strategy/SKILL.md) |
| Low rating or few ratings | [aso-review-and-rating-strategy](../aso/aso-review-and-rating-strategy/SKILL.md) |
| **Making money** | |
| Unsure what should be free / trial length | [monetization-free-trial-vs-freemium](../monetization/monetization-free-trial-vs-freemium/SKILL.md) |
| Need to get paid; Stripe not in your country; which provider | [monetization-payment-setup](../monetization/monetization-payment-setup/SKILL.md) |
| Adding in-app purchases / subscriptions to an iOS or Android app | [monetization-in-app-purchase-setup](../monetization/monetization-in-app-purchase-setup/SKILL.md) |
| Unsure what to charge | [monetization-pricing-strategy](../monetization/monetization-pricing-strategy/SKILL.md) |
| Has a paywall, low conversion or rejected | [monetization-paywall-design](../monetization/monetization-paywall-design/SKILL.md) |
| One plan, very different customers | [monetization-subscription-tiers](../monetization/monetization-subscription-tiers/SKILL.md) |
| **Email & beta** | |
| Starting a waitlist; emails land in spam; SPF / DKIM / DMARC; consent | [email-list-and-deliverability](../email/email-list-and-deliverability/SKILL.md) |
| Need beta testers; TestFlight / Play closed test / Chrome trusted testers; testers go silent | [email-beta-program](../email/email-beta-program/SKILL.md) |
| One big list gets the same email; which email tool; segments by product or plan | [email-segments-and-tools](../email/email-segments-and-tools/SKILL.md) |
| Users sign up but never come back; welcome / onboarding emails | [email-onboarding-sequence](../email/email-onboarding-sequence/SKILL.md) |
| Trials don't convert; trial ending / expired / win-back emails | [email-trial-sequence](../email/email-trial-sequence/SKILL.md) |
| B2B product, no inbound; wants to email exact buyers; cold email / outbound; where to find emails | [email-cold-outreach](../email/email-cold-outreach/SKILL.md) |

## Prompt (copy-paste)
For chat assistants that can't install skills:

````text
You are a growth advisor for people building digital products. Ask me at most 4 short questions:
what the product is and where it's distributed, its stage (idea / pre-launch / <3 months / longer),
rough weekly users and revenue, and what feels most broken. Then recommend ONE growth task to
focus on for the next two weeks, explain why in one sentence, and give me the first 3 concrete steps.
Choose from: revenue target (work backward from $X in N months), spend and timing (what to pay for, when to push),
contrarian marketing, products as a funnel to an owned audience, where users ask about software, competitor review mining, source finding,
research doc organization, competitor teardown, success story analysis, award-winning design study, writing a case study, App Store listing, Google Play listing, browser extension / Mac app / indie game / plugin / AI product / Notion template listing, free directories, pre-launch checklist, launch post writing, Reddit posting by product type, Product Hunt launch, quick download wins, getting the first 100 users, GitHub repo seeding, open-source funnel (free repo → users),
Firebase + AdMob + payments setup, short video (TikTok / Reels / Shorts), credible social posts, build in public,
ASO keyword research, ASO title & subtitle, ASO screenshots, ratings & reviews, free trial vs freemium,
payment setup (which provider works from my country), in-app purchase setup (StoreKit 2 / Play Billing / RevenueCat), pricing strategy, paywall design, subscription tiers,
cold email outreach, email list & deliverability, email segments and tools, beta program by email, onboarding email sequence, free-trial email sequence.
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
