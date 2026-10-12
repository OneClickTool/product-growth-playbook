---
name: social-x-profile-funnel
description: Turn an X (Twitter) profile into a funnel that sells your software, from profile visit to trial to first paid subscriber. Sets the name line, bio, one UTM link, banner, pinned demo post with the offer, a link hub when you have several products, and a weekly check of the numbers (profile visits → link clicks → landing visits → trials → paid). Use when someone asks "what should my X bio say", "pinned tweet for my app", "people visit my profile but nobody buys", "how to sell subscriptions from X", "link in bio for several apps", "first dollar from Twitter", "tối ưu profile X", "bio X bán app", or has X traffic but no sales.
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: "Setup 45 min · 10 min/week check"
  version: 1.0.0
  author: nvminhtu
---

# X Profile Funnel: From Profile Visit to First Subscriber

> A profile that says what you make, a pinned demo with one offer, and links you can trace to a sale.

## Goal
Posts and replies bring people to your profile. The profile decides whether they leave or try your product. Most
indie dev profiles say "building cool stuff 🚀" and link to a GitHub. This skill makes every profile visit count:
one clear promise, one proof, one link with tracking, and a pinned post that shows the product working.

## When to use
- You're starting to post on X about products you sell (subscriptions, one-time Pro, licences).
- X analytics shows profile visits but your landing page sees few visitors from X, or none buy.
- You have several products and don't know which one to put in the bio.
- **Not for:** what to post daily → [social-x-growth](../social-x-growth/SKILL.md). Choosing trial vs. freemium →
  [monetization-free-trial-vs-freemium](../../../../skills/monetization/monetization-free-trial-vs-freemium/SKILL.md).

## Inputs
- Your products, prices and trial terms (written exactly as on the store or checkout).
- A landing page per product, or one hub page listing them.
- A 10–40 second screen recording of the best product doing its main job.
- Analytics that shows UTM sources (GA4, Plausible, store campaign links, etc.).

## Steps
1. **Pick the hero product.** The one with a paid plan, a working trial and the clearest "aha" in 10 seconds. Other
   products live on a hub page, not in the bio.
2. **Name line:** your name + what you make, e.g. "Alex · small Mac & iOS utilities". It shows next to every reply.
3. **Bio (160 characters):** who you help + what you made + one proof. Example shape: "I make small Mac apps that
   fix one annoying thing. Dupefinder cleans duplicate files. 4 apps live, 1 more every month." (fictional) Proof must be true.
4. **One link with UTM:** `https://yoursite/?utm_source=x&utm_medium=bio&utm_campaign=profile`. For a store link,
   use the store's own campaign parameters (App Store `ct=`/`pt=`, Google Play `referrer=`) where you can.
5. **Banner:** a real screenshot of the hero product + one line of what it does. No quotes, no abstract art.
6. **Pinned post:** the demo clip + three lines: problem, what the app does, the offer ("Free, Pro is $9.99 once",
   "7-day free trial, then $3.99/month"). Link at the end or in the first reply. Re-pin a fresher demo every month.
7. **Hub page** when you have 3+ products: one page with each product, price and store link, so the bio link never
   has to change.
8. **Weekly 10-minute check** (template: [weekly-numbers.md](../../templates/weekly-numbers.md)):

   | Step | Where to read it | If it's low |
   |---|---|---|
   | Profile visits | X analytics | Post/reply more, or reply to different accounts |
   | Link clicks | X analytics (link clicks) | Rewrite bio promise and pinned post |
   | Landing visits from `utm_source=x` | your analytics | Link broken or slow page |
   | Trials / installs | store or checkout | Landing doesn't match the promise in the pin |
   | Paid | store or checkout | Paywall, price or trial length → [monetization-paywall-design](../../../../skills/monetization/monetization-paywall-design/SKILL.md) |

9. **Keep the checkmark in mind:** changing your profile photo, display name or @handle removes the blue checkmark
   until X reviews it again ([About X Premium](https://help.x.com/en/using-x/x-premium)). Settle them early.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You set up X profiles for indie developers who sell their own software. Be specific and modest. Never invent
numbers, users or reviews.

Me: {{name, what I make, where I live if relevant}}
Products (name · one line · price/trial exactly as on the store · link): {{...}}
Real proof I can claim: {{apps live, users, ratings, revenue, years building}}
Hub page URL (if any): {{...}}

1. Pick the hero product and say why (paid plan, trial, fastest "aha").
2. Write 3 name lines and 3 bios (max 160 characters each).
3. Give the bio link with UTM tags (utm_source=x, utm_medium=bio, utm_campaign=profile).
4. Write the pinned post: what the demo clip should show second by second (max 40 s), then 3 lines (problem,
   what it does, offer) under 280 characters.
5. Describe the banner in one sentence.
6. List what to check every week and the one fix for each weak step.
````

## Example output

> **Illustrative example.** Fictional developer and product.

- **Name line:** Mai · tiny Mac apps that fix one thing
- **Bio:** I make small Mac utilities that respect your files. Clipnest keeps your clipboard history, offline.
  3 apps live, all made solo.
- **Link:** `clipnest.example/?utm_source=x&utm_medium=bio&utm_campaign=profile`
- **Pinned post:** "Copied something, then lost it by copying the next thing? Clipnest keeps the last 1,000 copies,
  searchable, on your Mac only. 7-day free trial, then $3.99/month. [12 s clip: copy, copy, ⌘⇧V, search, paste]"
- **Weekly check, week 3:** 410 profile visits → 38 link clicks → 31 landing visits → 6 trials → 1 paid. Weakest
  step: clicks (9%). Fix: bio now names the problem, not the app.

## Common mistakes
- **Five links in the bio area.** One link, one promise. Everything else goes on the hub page.
- **Pinned post from launch day, six months ago.** Re-pin a current demo monthly.
- **Offer text that doesn't match the store.** Users who see "free" and then a paywall leave and don't come back.
- **No UTM.** You'll never know if Premium pays for itself.
- **Changing your handle every month.** You lose the checkmark during review and confuse people who search for you.

## Related skills
- [social-x-growth](../social-x-growth/SKILL.md): daily posts that send people to this profile.
- [social-x-reply](../social-x-reply/SKILL.md): replies that bring profile visits.
- [monetization-pricing-strategy](../../../../skills/monetization/monetization-pricing-strategy/SKILL.md): the price in the pinned post.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: [About X Premium](https://help.x.com/en/using-x/x-premium)
(checked 2026-10-11).
