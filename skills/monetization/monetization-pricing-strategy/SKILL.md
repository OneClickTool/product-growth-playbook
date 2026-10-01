---
name: monetization-pricing-strategy
description: Set a first price, or re-price, for an app, SaaS, AI tool or extension, using alternatives, value to the customer, a willingness-to-pay survey and store fees, and produce a price table with the reasoning and a plan to test it. Use when someone asks "how much should I charge", "pricing my app", "monthly vs yearly price", "is my price too low", or before launching paid plans.
license: MIT
metadata:
  category: monetization
  difficulty: intermediate
  time: 60 min (plus survey time)
  version: 1.0.0
  author: nvminhtu
---

# Pricing Strategy

> In an hour you will have a monthly and yearly price (and lifetime or one-time if relevant), the reasoning behind
> them, what you keep after fees, and how you'll know if you got it wrong.

## Goal
Pick a price anchored to the value you deliver and what people pay for alternatives, not to your costs or to
"the lowest price wins". You can change the price later. Not charging enough for a long time is the most common mistake.

## When to use
- Before turning on paid plans.
- Revenue is flat and you suspect the price.
- Adding a yearly plan or changing plan structure.
- **Not for:** deciding what's free vs paid → [monetization-free-trial-vs-freemium](../monetization-free-trial-vs-freemium/SKILL.md).
  Designing multiple tiers → [monetization-subscription-tiers](../monetization-subscription-tiers/SKILL.md).

## Inputs
- Who pays (a consumer, a freelancer, a company) and what problem the product solves in money or time.
- 3–5 alternatives and what they cost, **including doing it manually or hiring someone**.
- Where you sell: App Store, Google Play, web (Stripe, Paddle, Lemon Squeezy…), Chrome extension with web checkout.
- Optional: 20+ answers to the 4-question survey in step 3.

## Steps
1. **Map the alternatives (10 min).** List what people use today and its price per month. Include "spreadsheet +
   2 hours a week" and value that time. Your price sits relative to these. If you're clearly better at one thing,
   you don't need to be the cheapest.
2. **Estimate value (10 min).** What does the product save or earn the user per month? B2B tools are often priced
   at 10–20% of the value they create. Consumer apps compare against everyday spending ("less than one coffee a month").
3. **Ask willingness to pay (setup 10 min).** Send the Van Westendorp questions to 20+ people in your target audience:
   - At what price would it be **so expensive** you wouldn't consider it?
   - At what price would it be **so cheap** you'd doubt the quality?
   - At what price would it start to feel **expensive**, but you'd still consider it?
   - At what price would it be a **bargain**?
   The acceptable range sits between where "too cheap" and "expensive" cross and where "bargain" and "too expensive" cross.
   With few answers, just look at the medians.
4. **Choose the structure (10 min).**
   - Monthly plus yearly. The yearly plan is usually priced at the equivalent of 6–10 months. Show it as the default
     if you want commitment and cash up front.
   - Lifetime or one-time only if the product has low ongoing costs, like a utility app or a desktop tool. Price it at
     roughly 2–4 years of the yearly plan.
   - Pick price points your storefront supports (App Store and Google Play have fixed price points per country).
5. **Calculate what you keep (5 min).**
   - App Store: 15% if you're in the Small Business Program (under $1M proceeds per year) and for subscriptions after
     a subscriber's first year, otherwise 30%.
   - Google Play: 15% on subscriptions, and 15% on your first $1M per year for other purchases.
   - Web: payment processor fees (a few percent + a fixed fee), or a merchant-of-record fee that includes sales tax.
6. **Decide the test and the signal (5 min).** Launch at the price, then watch paywall conversion and refund or cancel
   reasons for 4 weeks. If almost nobody objects to the price, it's probably too low. Test **higher** first.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are a pricing strategist for software products. Help me set my price.

Product: {{what it does}}   Buyer: {{consumer / freelancer / business, and who exactly}}
Value to the buyer: {{time or money saved/earned per month}}
Alternatives and their prices (incl. doing it manually): {{...}}
Sales channel(s): {{App Store / Google Play / web + processor}}
Survey answers (Van Westendorp, if any): {{paste or "none"}}
Current price and conversion (if live): {{...}}

1. Place my product relative to the alternatives. Where can I charge more, and why?
2. Recommend monthly and yearly prices (and lifetime/one-time only if it suits the product), using store price points.
   Show the yearly discount as a percentage.
3. Table: price | store/processor fee | what I keep per sale/month.
   Use: App Store 15% (Small Business Program or after year 1 of a subscription) else 30%; Google Play 15% on subscriptions.
4. If I have survey data, compute the acceptable price range. If not, give me the 4 Van Westendorp questions to send.
5. A 4-week test plan: what to watch, and what result means raise or lower the price.
State clearly which numbers are assumptions.
````

## Example output

> **Illustrative example.** Fictional product and numbers, shown for format.

*Invoicely Lite*, for freelance designers. Alternatives: spreadsheet + manual emails (~2 h/month), FreshBooks-class tools
($19–33/mo). Survey (n = 26) median "expensive but OK": $12/mo.

| Plan | Price | Discount | Web fee (≈3.5%) | You keep |
|---|---|---|---|---|
| Monthly | $9 | — | $0.32 | $8.68 |
| Yearly | $72 | 33% (= 8 months) | $2.52 | $69.48 |

Reasoning: under full accounting suites, and a clear saving against 2 hours of chasing. Test: if more than 8% of
paywall viewers start a trial and fewer than 1 in 10 cancellations mention price, try $12 / $96.

## Common mistakes
- **Cost-plus pricing.** Your server costs are irrelevant to what the value is worth to the customer.
- **Racing to the bottom.** Low prices attract price-sensitive users who churn and complain most.
- **Only a monthly plan.** You lose committed users and the cash to grow.
- **Changing price for existing subscribers without care.** Stores have specific rules and user-consent flows for
  price increases. Read them first, or keep existing users on their price.

## Related skills
- [monetization-paywall-design](../monetization-paywall-design/SKILL.md): how the price is presented.
- [monetization-subscription-tiers](../monetization-subscription-tiers/SKILL.md): when one plan isn't enough.
- [monetization-free-trial-vs-freemium](../monetization-free-trial-vs-freemium/SKILL.md): what's free.
- [monetization-payment-setup](../monetization-payment-setup/SKILL.md): a provider that can actually pay you from your country.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Commission rates from Apple (App Store Small Business Program,
auto-renewable subscriptions) and Google Play Console Help ("Service fees"). Rates change, so check before you set prices.
Van Westendorp Price Sensitivity Meter (Peter van Westendorp, 1976).
