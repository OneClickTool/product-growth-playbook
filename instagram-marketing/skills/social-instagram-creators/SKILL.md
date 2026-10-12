---
name: social-instagram-creators
description: Run a creator program for an app or digital product on Instagram (and the same creators' TikToks) - the lever behind the fastest consumer-app growth stories, such as Cal AI's reported 250+ paid creators. Builds a list of 100 micro-creators whose Reel views beat their follower count, writes short DMs for 60-100 outreach messages a week, sets up gifted, paid-pack, retainer and affiliate deals with usage rights for partnership ads, a one-page brief with real facts only, Paid partnership disclosure, one UTM or code per creator, and a renew-the-top-20% rule. Use when someone asks "find influencers for my app", "UGC creators for my app", "influencer marketing for indie apps", "how much to pay micro influencers", "creator outreach DM", "partnership ads", "tìm KOL cho app", "booking creator Instagram", "UGC cho app", or wants other people's audiences to sell their product.
license: MIT
metadata:
  category: social
  difficulty: intermediate
  time: "Setup 2-3 h · 2-4 h/week"
  version: 1.0.0
  author: nvminhtu
---

# Instagram Creators: Other People's Audiences, Tracked

> A list of 100 creators, outreach that gets replies, deals you can afford, a brief that keeps them honest, and a
> tracker that tells you who to renew.

## Goal
Your own account starts at zero reach; a creator's starts at their audience. Reported founder interviews say Cal AI
grew on 250+ paid fitness creators posting simple product demos, then reused the best clips as ads. Meta reports
partnership ads average 19 % lower CPA than brand ads. This skill runs a small, tracked version of that for any
product with a result you can show on screen.

## When to use
- Your product shows a result in 2 seconds on a phone (before/after, a card, a game moment, a satisfying action).
- Your own posts work a little and you want 10× the reach this month.
- You have $0–2,000 a month, or free licenses to give.
- **Not for:** dev-only tools whose buyers aren't on Instagram → [social-x-growth](../../../x-marketing/skills/social-x-growth/SKILL.md).
  The full multi-engine plan → [social-instagram-engine](../social-instagram-engine/SKILL.md).

## Inputs
- The product's visual result, 3–5 true facts, offer, landing URL; free Pro codes if you can give them.
- Budget and a payment method that works for creators in your target countries.
- The niche words buyers use (for finding creators).

## Steps
1. **Build the list (60 min):** 100 creators, 5k–100k followers, Reels with views above their follower count, real
   "what app is that?" comments, screens on camera. Sources: Instagram search for buyer queries, niche hashtags,
   "suggested accounts", TikTok creators who also post Reels, Meta's creator marketplace if available. Log in
   [templates/creator-tracker.md](../../templates/creator-tracker.md).
2. **Outreach (60–100 DMs/week):** short, specific DM (their Reel, your product in one line, free trial, paid if they
   like it, honest take), one follow-up after 4 days, email if listed. Expect ~1 % replies (Reported).
3. **Deal:** gifted (free license, post only if they want) → paid pack of 3–5 Reels, 50 % upfront, priced on their
   average views → retainer + view/trial bonus for winners → affiliate code for long tails. Always get **usage
   rights** in writing for partnership ads (60–90 days) and the raw file.
4. **Brief (one page, [template](../../templates/creator-brief.md)):** the result to show in 2 s, true facts they may
   say, the offer and their link / code, what not to claim, **Paid partnership** label + `#ad` where required,
   Collab invite to your account.
5. **Track:** `utm_source=instagram&utm_medium=creator&utm_campaign=<product>&utm_content=<handle>` and/or a code per
   creator; at +7 days log views, shares, landing visits, trials.
6. **Scale:** renew the top 20 % by trials, run their best Reel as a partnership ad, ask them for 3 new hooks on the
   same video. Drop the bottom half.

Full program: [docs/10-creator-program.md](../../docs/10-creator-program.md).

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are my creator-program manager. Product: {{name}} · {{one line}} · visual result in 2 s: {{...}} · offer today:
{{...}} · landing: {{url}} · slug: {{slug}}. True facts creators may use: {{3-5 facts}}.
Budget: {{$0 / $500 / $2000}} a month. Target countries: {{...}}. Buyer words: {{...}}.

1. Give me 25 Instagram search queries and 10 hashtags to find micro-creators (5k-100k) in this niche, and the 4
   signals that a creator is worth a DM (views vs followers, real comments, screens on camera, niche fit).
2. Write DM 1 (≤ 45 words, mentions their specific Reel, no hype) and one follow-up. Write an email version.
3. Propose deal tiers for my budget: gifted / paid pack / retainer / affiliate, with how to price on average views,
   upfront split, and the usage-rights line for partnership ads.
4. Fill the one-page brief: result to show, facts, offer, link with utm_medium=creator&utm_content=<handle>,
   don'ts, the Paid partnership + #ad disclosure, Collab invite, raw file.
5. Give the weekly tracking table and the renew/drop rule.
Never suggest fake reviews, scripts that make creators claim results they didn't see, hidden paid posts, or
buying shoutouts from accounts with fake followers.
````

## Example output

> **Illustrative example.** Fictional product (Tidybox, a Mac cleaner); made-up budget, no results.

**DM 1:**
```text
Hey Jo, your "desk reset Friday" Reel is exactly how my users talk about their cluttered Macs.
I make Tidybox (finds duplicate files, moves them to Trash with undo). Want to try Pro free?
If you like it I'd pay for 3 Reels, your honest take.
```

**Deal ($500/mo):** 5 creators × 3-Reel pack at ~$100 each pack, 50 % upfront; partnership-ad rights 60 days;
renew the 1–2 with the most trials via their `utm_content`.

## Common mistakes
- **Choosing by followers.** Price and pick by average Reel views.
- **Scripts.** Creators' own words convert; scripted reads look like ads.
- **No disclosure.** Paid or gifted posts need the Paid partnership label (FTC Endorsement Guides, US).
- **No usage rights.** Without them you can't turn the winning Reel into a partnership ad.
- **One creator, one shot.** Volume finds winners: plan for most deals not paying back.

## Related skills
- [social-instagram-engine](../social-instagram-engine/SKILL.md): where creators fit among the 8 engines.
- [social-instagram-image-flow](../social-instagram-image-flow/SKILL.md): your own posts that creators' viewers land on.
- [social-credible-posting](../../../skills/social/social-credible-posting/SKILL.md): FTC disclosure basics.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources (checked 2026-10-12): [Latka interview with Cal AI's founder](https://getlatka.com/interviews/cal-ai-zach-yadegari-2025),
[eMarketer on partnership ads](https://www.emarketer.com/content/meta-expands-partnership-ads-turn-creator-content-performance),
[FTC Endorsement Guides 2023 summary](https://www.manatt.com/insights/newsletters/advertising-law/an-in-depth-look-at-the-ftcs-updates-to-the-endor).
