---
name: social-x-growth
description: Grow on X (Twitter) as an indie developer and turn that attention into the first paying subscribers. Builds a product fact bank from what you already shipped, a 7-day post rotation you batch in 30 minutes a week, a reply routine that uses X Premium's reply prioritization, rules taken from X's open-source For You ranker (what the weights reward and punish, the 48-hour window, author diversity), a Premium 30-day plan, and a bio → pinned post → landing → trial funnel with UTM tracking. Also lists the best open-source X skills and repos to install. Use when someone asks "write my daily X posts", "what should I tweet about my app", "how does the X algorithm work", "is X Premium worth it", "how to use X Premium for growth", "get followers on X as an indie dev", "sell subscriptions from X", "first dollar from Twitter", "đăng X mỗi ngày", "tận dụng Premium X", or wants a copy-ready week of X posts.
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: "Setup 60 min · 30 min/week batching · 20 min/day replies"
  version: 1.1.0
  author: nvminhtu
---

# X Growth: Daily Posts, Premium Reach, First Subscribers

> A week of copy-ready X posts about products you already built, a daily reply routine, and a funnel that turns
> profile visits into paid trials.

## Goal
Most indie devs on X either post nothing or post "I built X, check it out" ten times. Both stall. What works is a
steady mix of useful posts, honest building updates and real replies, with **one** clear path from your profile to
something people can pay for. This skill sets that system up once, then keeps it to 30 minutes of batching a week
plus 20 minutes of replies a day.

## When to use
- You have one or more shipped products (apps, extensions, tools, templates) and want to post about them daily
  without running out of ideas.
- You pay for X Premium and want a plan that actually uses it.
- You sell subscriptions or one-off licences and want X to send buyers, not only likes.
- **Not for:** the trust rules behind every post → [social-credible-posting](../../../skills/social/social-credible-posting/SKILL.md) (read
  it once first). A weekly progress habit across several platforms → [social-build-in-public](../../../skills/social/social-build-in-public/SKILL.md).
  Launch-day posts → [launch-post-writing](../../../skills/launch/launch-post-writing/SKILL.md).

## Inputs
- A list of your products with: one-line pitch, who it's for, price/trial, landing URL, 3–5 real screenshots or a
  short screen recording.
- Real facts you can share: changelog lines, install/user/revenue numbers with dates, a bug you fixed, a review
  (with permission).
- Your X Premium tier (Basic, Premium or Premium+): it changes which features you have, see
  [reference/x-algorithm-and-premium-facts.md](../../reference/x-algorithm-and-premium-facts.md).
- A landing page with a trial or a buy button, and a way to see visits by source (UTM in your analytics).

## What the ranker rewards (from X's own code)
X publishes the For You ranker at [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm). The model predicts
how likely *each viewer* is to take each action on your post, multiplies those predictions by weights and adds
them up. The defaults in the repo (checked 2026-10-11, production may tune them) say:

| Action the viewer is predicted to take | Default weight | What it means for you |
|---|---|---|
| Share via copy link | 20 | Write things people want to send to someone: checklists, tools, numbers |
| Reply (×15 boost if you follow each other) | 5 | Ask a real question; talk with mutuals |
| Quote · share via DM | 5 · 5 | Give people something to add their take to |
| Follow you from the post | 4 | Every post should show what you're about |
| Repost · share | 1 · 2 | Nice, not the main lever |
| Like | 0.5 | Likes alone barely move ranking |
| Open link | 0.2 | Links are allowed, just weakly rewarded; the post has to earn reach on its own |
| Not interested · mute · block | −47.5 · −58.8 · −31.2 | Spammy, repetitive or rage-bait posts cost far more than they earn |
| Report | −234 | Never risk it |

Three more rules from the same code: posts **older than 48 hours** are dropped from For You, so a post's life is two
days; each extra post from the same author in one feed is **decayed** (author diversity), so 1 strong post beats 5
weak ones; and authors with few impressions get a **new-author boost**, so small accounts do get tested. Full notes
and the caveats are in [reference/x-algorithm-and-premium-facts.md](../../reference/x-algorithm-and-premium-facts.md).

## Steps
1. **Fix the profile first (15 min).** Name + what you make ("builds small Mac and iOS utilities"). Bio: who you help,
   proof, one link with UTM (`?utm_source=x&utm_medium=bio`). Pinned post: a 20–40 second demo of your best product +
   the offer ("14-day free trial", "free tier, $X/mo for Pro"). Banner: product screenshots, not a quote.
2. **Build the product fact bank (30 min, once).** For each product, write 10–20 true, specific facts: a feature and
   the problem it solves, a number with a date, a decision and why, a bug and the fix, a user quote you may share.
   Pull them from your README, changelog, store listing and analytics. This is the raw material for every post; the
   prompt below never invents beyond it.
3. **Use the 7-day rotation.** One original post per day, same slot, rotating products:

   | Day | Format | Goal |
   |---|---|---|
   | Mon | Demo: one feature, 10–30 s screen recording | Follow + profile click |
   | Tue | Number or lesson with context (proof ladder rung 2–4) | Reply + bookmark |
   | Wed | Useful tip that works **without** your product | Copy link / share |
   | Thu | Behind the scenes: a decision, bug or teardown | Reply |
   | Fri | A real question or poll for your buyers | Reply (mutual boost) |
   | Sat | Long post (Premium) or thread: a how-to, payoff in the first 280 characters | Dwell + share |
   | Sun | Weekly numbers / what shipped + soft offer | Profile visit → landing |

   At most **one** post in seven asks for money. The rest earn the right to ask.
4. **Batch on one day (30 min/week).** Run the prompt with your fact bank, edit every draft in your own words, and
   schedule them (X's own scheduler on web or a tool that uses the official API). Never post the same text twice or
   across several accounts: X's [automation rules](https://help.x.com/en/rules-and-policies/x-automation) forbid
   duplicate posts and scripted website automation.
5. **Reply routine (20 min/day, the real Premium lever).** Keep a list of 20–30 accounts your buyers follow (bigger
   indie devs, tool reviewers, niche communities). Each day write 5–10 replies that add something: a number, a
   counter-example, a screenshot. Premium's reply prioritization puts these higher in the thread; a good one sends
   profile visits, which your pinned post turns into trials. Do this by hand: automated keyword replies are banned.
6. **Answer everyone in the first hour** after your post. Replies are weighted 5 and the conversation keeps the post
   alive inside its 48-hour window.
7. **Run the funnel and measure.** Bio and pinned links carry UTM tags; when you do link in a post, test link-in-post
   vs link-in-first-reply for a month and keep what gets more landing visits. Weekly, write down: impressions, profile
   visits, link clicks, landing visits from `utm_source=x`, trials, paid. If profile visits grow but trials don't, fix
   the pinned post and landing, not the posting.
8. **Use the Premium extras on purpose.** Longer posts for Saturday how-tos; edit (1 hour) to fix typos instead of
   deleting; Media Studio for your demo clips; Articles if your tier has them. Creator Subscriptions and revenue
   payouts exist, but for a dev selling software they're a side bonus: your product is the subscription. The 30-day
   plan is in [docs/04-premium-30-day-plan.md](../../docs/04-premium-30-day-plan.md).
9. **Review every 4 weeks.** Keep the 2 formats with the most profile visits and trials, drop the weakest, and refill
   the fact bank from what you shipped.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are my X (Twitter) ghost-editor. I'm an indie developer who sells my own software. Write like a real builder:
plain words, specific details, no hype. Never invent features, numbers, users, reviews or experiences that are not
in my fact bank. If a post needs a number I didn't give you, write <NUMBER?> and tell me.

My X tier: {{Basic / Premium / Premium+}}   Posting time zone: {{...}}
Who buys my products: {{e.g. Mac power users, iOS devs, small agencies}}
Products (pitch · who for · price/trial · landing URL with utm_source=x):
{{...}}
Fact bank (true, dated facts per product):
{{...}}
Banned words: game-changer, revolutionary, unlock, supercharge, delve, "in today's fast-paced world", "🚀" spam.

Write next week's 7 posts using this rotation:
Mon demo (say what to record) · Tue number/lesson with context · Wed tip that works without my product ·
Thu behind the scenes · Fri real question or poll · Sat long post or thread (payoff in the first 280 characters) ·
Sun weekly numbers + one soft offer.

Rules for every post:
1. First line works alone in the feed: a concrete claim, number or problem. No "Thread 🧵👇" openers.
2. Under 280 characters unless it's Saturday; one idea per post; max 1 emoji; no hashtags unless a community uses one.
3. Only Sunday may ask for money. Other days may mention the product once, at the end, if it's natural.
4. Give each post: the text, the image/clip to attach, which product it's about, and the action it aims for
   (reply / share / follow / profile visit).
5. Then write 10 reply openers I can adapt for big accounts in my niche: each adds a fact, example or counterpoint,
   never "Great post!".
6. Finish with a checklist of every number and claim I must verify before scheduling.
````

## Example output

> **Illustrative example.** Fictional product (a Mac clipboard app, "Clipnest") and made-up numbers.

**Tue (number with context):**
> Clipnest went from 3% to 9% trial → paid in 3 weeks. Small base: 212 trials.
> The change: the paywall now shows *your* clipboard history count ("You saved 1,431 clips this week") instead of a
> feature list.

**Wed (tip that works without the product):**
> macOS tip most people miss: hold ⌥ while clicking the Wi-Fi icon. You get the IP, router, channel and signal
> without opening any app.

**Fri (question):**
> Mac folks: do you want clipboard history to sync to iPhone, or should it stay on the Mac only? Building this
> week and genuinely split.

**Reply to a bigger account** asking "what's your paywall conversion?":
> 9% trial → paid on a $4/mo Mac utility, up from 3%. What moved it: showing the user's own usage on the paywall
> instead of features. Small sample (212 trials), so take it as a direction, not a law.

## Common mistakes
- **Posting the launch link every day.** Author diversity decay plus "not interested" (−47.5) bury you. One ask a week.
- **Paying for Premium and not replying.** Reply prioritization is the main thing you bought; posts alone use a fraction of it.
- **Engagement bait** ("Like if you agree", "Comment 'AI' and I'll DM you"). It earns likes (0.5) and risks mutes and reports.
- **Auto-reply or auto-DM tools.** Banned by X's automation rules; it can get posts removed from search or the account suspended.
- **Links without UTM.** You won't know whether X sent the buyers, so you can't decide whether to keep paying for Premium.
- **Copying viral templates word for word.** Readers recognise them. Use the structure, keep your own facts and voice.

## Related skills
- [social-credible-posting](../../../skills/social/social-credible-posting/SKILL.md): the proof ladder and red-flag list every post here relies on.
- [social-build-in-public](../../../skills/social/social-build-in-public/SKILL.md): the Sunday numbers post as a weekly habit.
- [social-short-video](../../../skills/social/social-short-video/SKILL.md): the Monday demo clip, made once and reused on TikTok/Reels/Shorts.
- [monetization-free-trial-vs-freemium](../../../skills/monetization/monetization-free-trial-vs-freemium/SKILL.md): what the pinned post should offer.
- [strategy-product-as-funnel](../../../skills/strategy/strategy-product-as-funnel/SKILL.md): move followers to an email list you own.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm)
(README and `home-mixer/params/param.rs`), [About X Premium](https://help.x.com/en/using-x/x-premium),
[X automation rules](https://help.x.com/en/rules-and-policies/x-automation) (all checked 2026-10-11).
Repos to install: [reference/x-repos.md](../../reference/x-repos.md).
