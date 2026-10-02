---
name: strategy-product-as-funnel
description: Treat each app, game, extension or free tool as an entry point that turns strangers into users you can reach again (email list, account, community), instead of a one-off download. Maps every product's "give → get" (what the user gets first, what you ask in return), adds one owned-audience capture point per product at the moment of value, links products to each other with honest cross-promotion, and tracks owned users as the long-term number. Use when someone has several small apps or games, says "my apps get downloads but no lasting users", "how do I build a user base, not just apps", "app portfolio strategy", "cross-promote my apps", "turn free users into an audience", "build long term", "giữ chân người dùng", "húp user", or wonders why each launch starts from zero.
license: MIT
metadata:
  category: strategy
  difficulty: intermediate
  time: "60-90 min, then one capture point per product"
  version: 1.0.0
  author: nvminhtu
---

# Product as Funnel: Apps Are Tools, Users Are the Asset

> A one-page map of every product you own, what each one gives users and asks back, where it captures an owned
> contact, and how the products send users to each other.

## Goal
A single app can be removed from a store, lose its ranking or go out of fashion. People who chose to stay in touch
with you can't be taken away. The goal is to make every product, including small free ones, earn trust first and
then turn some of its users into an **owned audience**: an email subscriber, an account, a community member, so
the next launch doesn't start from zero.

## When to use
- You have 2+ products (or plan to), and every launch starts with no one to tell.
- A product gets installs but you have no way to reach those users again.
- You're deciding whether to build a free tool, a game or a utility "just for traffic".
- **Not for:** the email setup itself → [email-list-and-deliverability](../../email/email-list-and-deliverability/SKILL.md)
  and [email-segments-and-tools](../../email/email-segments-and-tools/SKILL.md). Pricing a single product →
  [monetization-pricing-strategy](../../monetization/monetization-pricing-strategy/SKILL.md).

## Inputs
- A list of your products: platform, users per month, and how each makes money (if it does).
- Whatever owned channels you have today: an email list, accounts, a Discord or Facebook group, a newsletter.
- The audience you want to own long term, in one sentence ("indie Mac users", "parents of young kids", "solo devs").

## Steps
1. **Pick one audience.** Products that serve the same people can feed each other. Products for unrelated people
   can't. Write the audience sentence at the top of the map. Products that don't fit it are fine, but they don't
   get capture work.
2. **Write each product's "give → get".** The user must get something **before** you ask for anything:

   | Product | Gives (value, first) | Moment of value | Gets (the ask, after) |
   |---|---|---|---|
   | e.g. free game | 5 minutes of fun | finishes level 3 | "Get new levels by email" |

   If you can't name the moment of value, fix the product before adding any capture point.
3. **Add one capture point per product, at the moment of value.** Choose one:
   - **Email** with a specific promise ("monthly new levels", "tips for X, 1 email a month"), double opt-in, clear
     consent. Rules → [email-list-and-deliverability](../../email/email-list-and-deliverability/SKILL.md).
   - **Account / sync** when it truly helps the user (backup, multiple devices).
   - **Community** (Discord, group) when users help each other.
   Never block the core feature behind the ask, and never pre-tick consent.
4. **Tag the source.** Each capture point tags the contact with the product it came from and what they asked
   for. That's how you segment later ([email-segments-and-tools](../../email/email-segments-and-tools/SKILL.md)).
5. **Connect the products honestly.** Add a small "More from the developer" screen or link in each product, and
   in emails announce a new product **only** to segments it fits. Follow each store's rules for links and
   promotions (e.g. the [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) and
   [Google Play policies](https://play.google.com/about/developer-content-policy/)). No interstitials that trick
   users into installing another app.
6. **Give the audience a reason to stay.** An owned contact you never write to goes cold. Set a rhythm you can
   keep: one useful email a month, early access to new products, small free extras. Value first, sales second.
7. **Track the long-term numbers** monthly in `growth/audience.md`:
   owned contacts (total and new per product), the capture rate per product (new contacts ÷ active users), the share
   of a new launch's first-week users that came from your own audience, and unsubscribes.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are a product strategist who helps indie builders turn a set of small apps and games into a long-term
audience. Value comes before any ask. Never suggest dark patterns, pre-ticked consent, forced sign-up for the
core feature, or misleading cross-promotion.

My products: {{name, platform, users/month, how it makes money}}
Owned channels today: {{email list size, accounts, community}}
The audience I want to own long term: {{one sentence}}

1. Say which products fit that audience and which don't (and should get no capture work).
2. For each fitting product, write the "give → get" row: the value, the exact moment of value, and the ask.
   Flag any product where the moment of value is unclear.
3. Suggest ONE capture point per product (email / account / community), with the exact wording of the promise.
4. Design honest cross-promotion between the products: where it appears, the copy, and which segment sees it.
5. Propose a monthly rhythm to keep the audience warm that I can keep up alone.
6. Give me the monthly tracking table: owned contacts, capture rate per product, share of launch users from my audience.
````

## Example output

> **Illustrative example.** Fictional products and numbers.

**Audience:** families with kids aged 4–8.

| Product | Gives | Moment of value | Ask |
|---|---|---|---|
| Kids drawing game (iOS) | Drawing fun, no ads | Child saves a drawing | Parent gate → "Get a printable colouring pack each month" (email) |
| Bedtime story app | Story read aloud | Story finishes | "New stories every Friday" (email) |
| Chore chart web tool | A printable chart | Chart downloaded | "Send me new chart templates" (email) |
| Crypto price widget | — | — | Doesn't fit the audience. No capture work |

Monthly: 1 email with a free printable + 1 line about what's new. Next launch (a reading app) goes first to the
2,100 parents on the list. Goal: 30% of first-week users from the list.

## Common mistakes
- **Asking before giving.** A sign-up wall on first launch loses users who never saw the value.
- **Capturing for "later" with no promise.** "Join our newsletter" is weak; say what they'll get and how often.
- **Building products for unrelated audiences.** They can't feed each other, so each one starts from zero.
- **Spamming the whole list with every launch.** Send each announcement only to the segment it fits.
- **Measuring downloads only.** Downloads are rented attention; owned contacts and repeat users are the asset.

## Related skills
- [strategy-revenue-target](../strategy-revenue-target/SKILL.md): put a number on what the audience is worth.
- [email-segments-and-tools](../../email/email-segments-and-tools/SKILL.md): segment by product and pick an email tool.
- [email-onboarding-sequence](../../email/email-onboarding-sequence/SKILL.md): the first emails a new contact gets.
- [launch-open-source-funnel](../../launch/launch-open-source-funnel/SKILL.md): the same idea for free repos.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu).
