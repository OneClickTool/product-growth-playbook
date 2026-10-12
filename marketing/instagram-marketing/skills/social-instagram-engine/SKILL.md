---
name: social-instagram-engine
description: Run Instagram in Operator mode, the multi-engine system teams use to push many products, instead of one account posting a few times a week. Plans and runs 8 engines in parallel - a content factory (1 fact → 10 assets), a hook lab of 10-15 Trial Reels a week, 2-4 disclosed niche accounts you own, a creator engine (gifted, paid packs, retainers), weekly collab posts, comment-to-DM link flows and a broadcast channel, a paid amplifier that boosts only organic winners plus partnership ads and retargeting, and search captions for Instagram and Google - with a 7-day operator schedule, budget tiers ($0 / $500 / $2k a month), a Sunday dashboard and kill rules. Stays inside Meta and FTC rules (no bots, bought followers, fake reviews or hidden accounts). Use when someone says "scale Instagram", "push hundreds of products", "aggressive Instagram growth", "Instagram growth hacking", "go viral on Instagram with my app", "đẩy mạnh Instagram", "chơi lớn Instagram", "growth hack Instagram", or finds the starter plan too slow.
license: MIT
metadata:
  category: social
  difficulty: advanced
  time: "Setup 1 day · 12-15 h/week + 60-90 min/day"
  version: 1.0.0
  author: nvminhtu
---

# Instagram Engine: Operator Mode

> Eight growth engines running in parallel, a week that fits them, a budget, and a Sunday dashboard that tells you
> which engine to feed and which to kill.

## Goal
One account posting five times a week grows slowly. Accounts that scale apps push volume across several topic
accounts, test hooks on strangers before followers see them, borrow audiences through creators and collabs, turn
comments into DMs with links, and spend ad money only on posts that already won. This skill sets up that system and
runs it weekly, without the shortcuts that get accounts limited.

## When to use
- Starter mode ([social-instagram-growth](../social-instagram-growth/SKILL.md)) is running and you want 5–10× the output.
- You have several products, a visible result to show, and 12–15 hours a week (or a helper).
- You can spend $0–2,000 a month on creators and ads and want a rule for every dollar.
- **Not for:** a single post → [social-instagram-image-flow](../social-instagram-image-flow/SKILL.md). Only the
  creator part → [social-instagram-creators](../social-instagram-creators/SKILL.md).

## Inputs
- Products with facts, offers and landing URLs; a design kit; a fact bank per product.
- Current numbers: followers (Trial Reels need ≥ 1,000, public account, Reported), 28-day reach, profile visits,
  link taps, landing visits from `utm_source=instagram`.
- Monthly budget tier and weekly hours.
- Meta pixel + Conversions API on the landing pages (or a plan to add them before engine 7).

## Steps
1. **Pick the tier and ramp** ([docs/09](../../docs/09-growth-engine.md#ramp-so-you-dont-burn-out-in-week-2)): weeks 1–2 factory + DM +
   search; 3–4 add one niche account, one collab a week, first creator DMs; 5–8 add the hook lab, a paid creator
   pack and boosts; 9+ scale the two engines with the best cost per trial.
2. **Engine 1 · Factory (Sunday, 4–6 h):** 5–7 facts → 5–7 packs of 10 assets (master carousel, music slideshow cut,
   3 hook Reels, cover/single, Story with link, broadcast message, X post, TikTok slideshow).
3. **Engine 2 · Hook lab:** each Reel idea as 3 Trial Reels (pain / number / before-after hook); at +24 h the
   highest shares per view wins → share to followers → candidate for paid. Log in
   [templates/hook-tests.md](../../templates/hook-tests.md). Hooks to start from: [docs/11](../../docs/11-hook-bank.md).
4. **Engine 3 · Owned niche network:** 2–4 topic accounts (tips pages), 1 original post a day each, 80 % value /
   20 % product, **bio discloses who runs them**, no reposts, kill after 6 flat weeks.
5. **Engine 4 · Creators:** 60–100 DMs a week, gifted → paid packs → retainers for the top 20 %; Paid partnership
   label; usage rights for ads ([social-instagram-creators](../social-instagram-creators/SKILL.md)).
6. **Engine 5 · Collabs:** 1 maker collab + 1 creator collab a week; a monthly roundup with 4–5 makers.
7. **Engine 6 · DM + broadcast:** 1–2 posts a week with a comment keyword → opener + button → real resource + UTM
   link (`utm_medium=dm`); weekly broadcast message.
8. **Engine 7 · Paid:** boost only engine-2 winners or posts above the 30-day sends-per-reach average ($10–20/day,
   3–5 days); partnership ads from top creator posts; retarget 30-day Instagram engagers and site visitors; kill at
   2× target cost per trial.
9. **Engine 8 · Search:** 30 buyer queries per product; every carousel targets one in line 1, slide 1 and alt text.
10. **Sunday dashboard (20 min):** one number per engine ([docs/09](../../docs/09-growth-engine.md#the-operator-dashboard-sunday-20-min)),
    the funnel impressions → profile → link tap → landing → trial → paid; feed the best engine, cut the weakest.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are my Instagram growth operator. I sell my own apps. Plan next week in Operator mode with 8 engines. Be
concrete (counts, days, assets, budgets). Never invent product facts, numbers, users or reviews; write <NUMBER?>.
Never suggest bought followers, bots, engagement pods, fake reviews, reposting others' content, accounts that hide
who runs them, or paid posts without the Paid partnership label.

Products (pitch · who for · offer today · landing URL · slug · visual result): {{...}}
Fact bank: {{...}}
Accounts: brand @{{...}} ({{followers}}), niche accounts: {{list or none}}
Last week: Trial Reel results {{...}}, creator results {{...}}, ads {{spend, cost per trial}}, funnel {{...}}
Budget this month: {{$0 | $500 | $2000}}   Hours this week: {{...}}   Ramp week: {{1-12}}

Output:
1. Which engines are ON this week (by ramp week and budget) and why.
2. Factory: 5-7 facts → for each, the 10-asset pack (titles + hooks + where each goes + day).
3. Hook lab: each Reel idea with 3 hooks (pain / number / before-after), ≤ 8 words, same body.
   If followers < 1000, say where to test instead.
4. Niche accounts: per account, 7 posts (topic, format, whether it mentions a product) and the bio disclosure line.
5. Creators: 20 search queries to find creators, the DM text, which existing creators to renew/drop and why.
6. Collabs: 1 maker collab idea + 1 creator collab, with the shared post outline.
7. DM: which post gets a comment keyword, the keyword, message 1 + button, message 2 with the UTM link.
8. Paid: which post to boost (only proven winners), daily budget, audience (engagers 30 d / site visitors 30 d /
   lookalike), and the kill rule.
9. Search: the query each carousel targets.
10. A 7-day schedule table (brand / niche / hook lab / creators-collabs / paid) and the Sunday dashboard numbers
    to fill.
````

## Example output

> **Illustrative example.** Fictional products (Tidybox, a Mac cleaner; Pinlog, an iPhone places app); made-up
> plan, no results.

**Engines on (ramp week 5, $500):** 1 factory, 2 hook lab (brand at 1,240 followers), 3 one niche account
(`@macfixdaily`, bio `Mac tips by the makers of Tidybox`), 4 one paid pack (3 Reels), 5 one maker collab, 6 DM on
Wednesday, 7 boost last week's winner at $15/day × 4, 8 search captions.

| Day | Brand | @macfixdaily | Hook lab | Creators / collabs | Paid |
|---|---|---|---|---|---|
| Mon | Carousel "7 things filling your Mac" + Story link | "3 Finder settings" | 3 × idea A | 20 DMs | — |
| Tue | Last week's winner Reel | "Clean Desktop in 1 min" (music slideshow) | 3 × idea B | Brief @macsetupjo | Boost winner $15/day |
| Wed | Before/after + **comment CLEAN** | "Menu bar apps under $10" (Tidybox 1 of 5) | pick A | Collab: "5 small Mac apps" with 4 makers | — |

**Kill rule:** boost stops if cost per trial > $8 (2× the $4 target).

## Common mistakes
- **Turning on all 8 engines in week 1.** You burn out in week 2. Follow the ramp.
- **Paying to boost a post that lost organically.** Paid multiplies winners; it doesn't fix losers.
- **Niche accounts that repost.** Since Apr 2026, mostly-repost accounts aren't recommended (Reported). Original only.
- **Hiding that you run the niche accounts.** That's deceptive under Meta's inauthentic-behavior policy and the FTC;
  one bio line fixes it.
- **Creators without tracking.** No UTM or code per creator = you renew the wrong ones.
- **Volume without the hook lab.** More bad posts don't grow; more tested hooks do.

## Related skills
- [social-instagram-creators](../social-instagram-creators/SKILL.md): engine 4 in detail.
- [social-instagram-image-flow](../social-instagram-image-flow/SKILL.md): every asset's 10 steps.
- [social-instagram-growth](../social-instagram-growth/SKILL.md): Starter mode, the base this builds on.
- [strategy-spend-and-timing](../../../../skills/strategy/strategy-spend-and-timing/SKILL.md): when to put money in.
- [social-short-video](../../../../skills/social/social-short-video/SKILL.md): Reel formats for the hook lab.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources (checked 2026-10-12): [Buffer posting-frequency study](https://buffer.com/resources/how-often-to-post-on-instagram/),
[Meta Inauthentic Behavior policy](https://transparency.meta.com/policies/community-standards/inauthentic-behavior/),
[engagement custom audiences](https://www.facebook.com/business/help/1090330204367211/?id=2469097953376494),
[eMarketer on partnership ads](https://www.emarketer.com/content/meta-expands-partnership-ads-turn-creator-content-performance),
and the rest in [reference/instagram-facts.md](../../reference/instagram-facts.md).
