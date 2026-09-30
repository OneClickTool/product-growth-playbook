---
name: monetization-paywall-design
description: Design or audit a subscription paywall for an app or web product, covering placement, layout, copy, plan selection and trial messaging, and check it against App Store and Google Play subscription disclosure rules. Use when building a paywall, when trial or purchase conversion is low, when a paywall was rejected in review, or when someone asks "how should my paywall look", "paywall best practices", "improve paywall conversion", or "why was my subscription screen rejected".
license: MIT
metadata:
  category: monetization
  difficulty: intermediate
  time: 45-60 min
  version: 1.0.0
  author: nvminhtu
---

# Paywall Design

> In under an hour you will have a paywall wireframe with copy, a placement plan, a compliance checklist,
> and one A/B test to run first.

## Goal
Show the right offer at the moment users feel the value, explain it clearly, and never trick anyone.
Trickery gets apps rejected and drives refunds, chargebacks and 1★ reviews.

## When to use
- Building your first paywall.
- Paywall views → trial or purchase is low.
- A build was rejected over subscription wording.
- **Not for:** choosing the price → [monetization-pricing-strategy](../monetization-pricing-strategy/SKILL.md).

## Inputs
- Plans and prices, trial length if any.
- The 3 premium benefits users care about most (from interviews, reviews, feature usage).
- Where the paywall appears now, and its conversion if live.

## Anatomy of a paywall that converts
1. **Headline = the outcome,** not "Go Premium". ("Get paid on time, every time.")
2. **3 benefit bullets**, each an outcome, with an icon. Not a 12-row feature table.
3. **Plan picker:** 2–3 options. Pre-select the plan you want most people on (often yearly). Show the savings.
4. **The billed amount is the most prominent price.** A per-month equivalent ("$6/mo") can appear, but smaller and
   secondary.
5. **Trial explained plainly:** "Free for 7 days, then $72/year. Cancel anytime." A timeline (today → reminder
   day → billing day) builds trust.
6. **One primary button** with specific text ("Start my free week"), and a visible close button.
7. **Required links and actions:** Restore Purchases, Terms of Use (EULA), Privacy Policy.

## Compliance checklist (App Store and Google Play)
- [ ] Subscription name, duration, and the price per period are shown before purchase.
- [ ] The amount that will be billed is the most prominent pricing element.
- [ ] Trial terms say when billing starts and at what price.
- [ ] Restore Purchases is available.
- [ ] Links to Terms of Use and Privacy Policy are in the app **and** in the store metadata.
- [ ] No fake timers, pre-checked add-ons, hidden close buttons or misleading "free" claims.

## Steps
1. **Choose placements (10 min).** Pick 2–3: after onboarding (the highest-traffic spot for most subscription apps),
   when a user taps a premium feature (contextual, strong intent), and at a usage limit. Every placement gets its own
   headline that matches the moment.
2. **Write the copy (15 min)** using the anatomy above. The headline and bullets come from what users actually value.
3. **Wireframe (10 min).** Headline, benefits, plan picker and CTA all above the fold on a small phone.
4. **Run the compliance checklist (5 min).**
5. **Pick the first test (5 min).** In order of usual impact: placement/timing → headline and benefits → default
   plan → trial vs no trial. One variable at a time, new users only. Paywall tools (RevenueCat, Superwall, Adapty or
   your own flags) can split traffic.
6. **Measure:** paywall view → trial or purchase, trial → paid, refunds, and revenue per install (the metric that
   combines everything).

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are a subscription paywall designer who also knows App Store and Google Play review rules.

App: {{what it does}}   Platform(s): {{iOS / Android / web}}
Plans: {{e.g. monthly $9, yearly $72, 7-day trial on yearly}}
Top premium benefits users care about: {{...}}
Current placement and conversion (if any): {{...}}
Screenshot or description of the current paywall: {{...}}

1. Recommend 2-3 placements and a headline for each that matches that moment.
2. Write paywall copy: outcome headline, 3 benefit bullets, plan labels, CTA text, trial explanation
   ("Free for X days, then $Y/period. Cancel anytime."), and the small print.
3. Describe the layout top to bottom (must fit above the fold on a small phone).
4. Audit against this checklist and flag every failure: billed amount most prominent; name, duration and price
   shown; trial terms clear; Restore Purchases; Terms + Privacy links; no dark patterns.
5. Propose the first A/B test with hypothesis, variable and success metric.
````

## Example output

> **Illustrative example.** Fictional app, shown for format.

```text
Get paid on time, every time.
 ✓ Automatic, polite reminders
 ✓ Unlimited clients and invoices
 ✓ See who's late at a glance

 ◉ Yearly  $72.00 / year   (just $6/mo, save 33%)   BEST VALUE
 ○ Monthly $9.00 / month

 Today: full access · Day 5: we remind you · Day 7: billed $72.00
 [ Start my free week ]
 Restore Purchases · Terms · Privacy                           ✕
```
First test: the post-onboarding headline "Get paid on time, every time" vs "Stop chasing clients".

## Common mistakes
- **"$6/mo" in huge text when the charge is $72/year.** It can get rejected and triggers refund requests.
- **One paywall for every moment.** A user who just hit a limit needs a different message than a brand-new user.
- **A hidden or delayed close button.** Reviewers and users both punish it.
- **Judging tests on trial starts only.** A variant that doubles trials but halves trial → paid is a loss.

## Related skills
- [monetization-pricing-strategy](../monetization-pricing-strategy/SKILL.md): the numbers on the paywall.
- [monetization-free-trial-vs-freemium](../monetization-free-trial-vs-freemium/SKILL.md): whether to offer a trial.
- [monetization-subscription-tiers](../monetization-subscription-tiers/SKILL.md): more than one paid plan.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Rules from Apple's App Store Review Guidelines (3.1.1, 3.1.2
Subscriptions) and Google Play's Subscriptions policy. Re-check both before submitting.
