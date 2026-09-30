---
name: monetization-free-trial-vs-freemium
description: Decide between free trial, freemium, reverse trial, or paid-only for an app, SaaS or AI product, then define exactly what's free, the trial length and the upgrade triggers. Use when setting up monetization, when free users never convert, when trials don't convert, or when someone asks "free trial or freemium", "how long should my trial be", "what should be free", or "reverse trial".
license: MIT
metadata:
  category: monetization
  difficulty: intermediate
  time: 30-45 min
  version: 1.0.0
  author: nvminhtu
---

# Free Trial vs Freemium

> In 30–45 minutes you will have a model (trial, freemium, reverse trial or paid-only), what's free vs paid,
> the trial length, and the moments that trigger an upgrade.

## Goal
Pick the model that fits how quickly your product delivers value and what each free user costs you, then draw the
free/paid line so free users get enough value to stay but have a clear reason to pay.

## When to use
- Before launching paid plans.
- Lots of free users, almost none converting (the free tier may be too generous).
- Trials start but don't convert (the trial may be too short or value too slow).
- **Not for:** the price itself → [monetization-pricing-strategy](../monetization-pricing-strategy/SKILL.md).

## Inputs
- Time to first value: how long until a new user gets the main benefit?
- Cost per active free user per month (servers, AI tokens, support).
- Whether users bring in other users (sharing, collaboration, public output).
- How often people need the product: daily, weekly, occasionally.

## The four models

| Model | How it works | Fits when |
|---|---|---|
| **Free trial** | Full product for N days, then pay | Value is clear within days; free users are expensive (AI, heavy compute) |
| **Freemium** | A free plan forever, paid unlocks more | Free users are cheap; they spread the product (sharing, virality, SEO); habit forms slowly |
| **Reverse trial** | Start with the full paid product for N days, then drop to the free plan | You want freemium's reach **and** users to experience premium |
| **Paid only** | Pay before use (maybe with a refund guarantee) | Niche professional tool; high trust from content or referrals |

## Steps
1. **Score your product (10 min).** Answer: time to value (minutes / days / weeks)? cost per free user (≈0 / low /
   high)? virality (none / some / core)? usage frequency?
   - High cost per user → trial or paid.
   - Strong virality with near-zero cost → freemium or reverse trial.
   - Fast time to value → a short trial works (3–7 days). Slow → 14–30 days, or freemium.
2. **If there's a free plan, draw the line (15 min).** Free covers the **core loop** so users form the habit.
   Paid covers **more** (limits), **better** (power features) or **together** (teams, sharing). Never cripple the core
   loop so badly that free users can't see the value.
3. **Set upgrade triggers (10 min).** List the 3 moments where a free user naturally hits the line: a usage limit,
   a premium feature tap, a team invite. These are your contextual paywall placements.
4. **Pick trial details (5 min).** Length based on time to value. Card-up-front (fewer trials, higher conversion) vs
   no card (more trials, lower conversion). App store subscriptions use introductory offers and require payment
   details up front.
5. **Define success and revisit in 4–8 weeks.** Freemium: free → paid conversion rate and the cost of free users.
   Trial: trial start rate and trial → paid. Compare revenue per new user, not just conversion.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are a monetization strategist. Help me choose between free trial, freemium, reverse trial and paid-only.

Product: {{what it does}}   Platform: {{app stores / web}}
Time to first value: {{minutes / days / weeks, and what the value is}}
Cost per active free user per month: {{estimate, incl. AI/API costs}}
Virality: {{does using it expose it to others? how?}}
Usage frequency: {{daily / weekly / occasional}}
Current model and results (if live): {{...}}

1. Score my product on those four factors and recommend one model, with the two strongest reasons
   and the main risk.
2. If a free plan is involved: a table of Free vs Paid features and limits. The free plan must include the core loop.
3. Three upgrade trigger moments and what the user sees at each.
4. Trial details (if any): length, card up front or not, reminder before billing.
5. The metrics to judge it after 4-8 weeks and the thresholds that would make you switch models.
````

## Example output

> **Illustrative example.** Fictional product, shown for format.

*Snapnote AI*, which turns meeting audio into notes. Time to value: 1 meeting (same day). Cost per free user: high
(transcription + LLM). Virality: medium (shared notes). → **Reverse trial:** 14 days of Pro, then Free.

| | Free | Pro ($12/mo · $96/yr) |
|---|---|---|
| Meetings per month | 3 | Unlimited |
| Summary + action items | ✓ | ✓ |
| Share notes by link | ✓ ("Made with Snapnote" footer) | ✓ no footer |
| Search across all meetings | — | ✓ |
| Integrations (Notion, Slack) | — | ✓ |

Triggers: 4th meeting of the month · tapping Search · removing the share footer.

## Common mistakes
- **A free plan that costs you more than it earns** in reach. With AI products, every free user has a real cost.
- **Paywalling the core loop.** Users never form the habit, so they never pay.
- **A trial shorter than time to value.** A 3-day trial for a weekly-use product converts almost nobody.
- **Judging only on conversion rate.** Freemium converts a smaller percentage of a much bigger base. Compare revenue per new user.

## Related skills
- [monetization-pricing-strategy](../monetization-pricing-strategy/SKILL.md): the price of the paid plan.
- [monetization-paywall-design](../monetization-paywall-design/SKILL.md): what users see at each trigger.
- [monetization-subscription-tiers](../monetization-subscription-tiers/SKILL.md): if one paid plan isn't enough.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). "Reverse trial" as popularized by Elena Verna. Introductory offer
rules from Apple's "Auto-renewable subscriptions" and Google Play's "Subscription offers" documentation.
