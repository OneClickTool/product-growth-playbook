---
name: monetization-subscription-tiers
description: Design 2-3 subscription tiers (good / better / best) for a SaaS, app or AI product, choosing the value metric, target persona per tier, feature and limit fences, and the tier most people should pick. Use when one plan leaves money on the table, when adding a Team or Business plan, or when someone asks "how many plans should I have", "design pricing tiers", "Pro vs Business plan", or "what goes in each tier".
license: MIT
metadata:
  category: monetization
  difficulty: advanced
  time: 45-60 min
  version: 1.0.0
  author: nvminhtu
---

# Subscription Tiers

> In under an hour you will have a tier table: who each tier is for, what it includes, its price, and why
> most people will pick the middle one.

## Goal
Let different customers pay what the product is worth to *them*: light users a low price, heavy users and teams more,
without confusing anyone.

## When to use
- You have one paid plan and clearly different kinds of customers (hobbyists vs pros vs teams).
- Heavy users pay the same as light users.
- Adding a Team or Business plan.
- **Not for:** your first price with no users yet. Start with one plan → [monetization-pricing-strategy](../monetization-pricing-strategy/SKILL.md).

## Inputs
- Current plan, price, and usage data: what do the top 20% of users do differently?
- 2–4 customer types and what each one values.
- Costs that grow with usage (AI tokens, storage, seats).

## Steps
1. **Choose the value metric (10 min).** The thing that grows as the customer gets more value: seats, projects,
   usage (credits, minutes, documents), or features. A good value metric is easy to understand, grows with the
   customer's success, and tracks your costs.
2. **Define 2–3 personas (10 min).** For example: *Solo* (one person, occasional use), *Pro* (relies on it for work),
   *Team* (several people, needs admin and billing). Each tier exists for one persona. Don't create a tier without one.
3. **Fence the tiers (15 min).** Each higher tier adds something its persona can't live without:
   - **Limits** on the value metric (10 → 100 → unlimited projects).
   - **Power features** for pros (automation, integrations, export).
   - **Team features** (seats, shared workspaces, SSO, admin, invoices).
   Keep the core loop in every tier.
4. **Price the tiers (10 min).** A common pattern is roughly 2–3× between neighbouring tiers. Make the middle tier the
   obvious best value for most people. The top tier also anchors it, so the middle feels reasonable.
5. **Stay simple.** 3 paid tiers at most (plus a free plan if you have one). On iOS, put tiers in the same
   subscription group so users can upgrade and downgrade cleanly. Decide whether to enable Family Sharing.
6. **Present it:** highlight the recommended tier, one line per tier on who it's for, and the same row order in every
   column.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are a SaaS/app pricing architect. Design my subscription tiers.

Product: {{what it does}}   Platform: {{app stores / web}}
Current plan(s) and price: {{...}}
Customer types I see: {{...}}
What heavy users do differently: {{usage data or observations}}
Costs that scale with usage: {{AI tokens, storage, seats...}}

1. Recommend a value metric and explain why it grows with customer value and with my costs.
2. Define 2-3 personas, one per tier.
3. A tier table: Tier | For (persona) | Price monthly/yearly | Limits | Key features | Why upgrade to this tier.
   The core loop must stay in every tier. The middle tier should be the best value for most customers.
4. Point out any feature that sits in the wrong tier, and any tier that has no clear persona.
5. Implementation notes for my platform (e.g. iOS subscription groups, upgrade/downgrade handling).
````

## Example output

> **Illustrative example.** Fictional product and prices, shown for format.

*Snapnote AI*, value metric: **meeting hours per month**.

| | Solo | **Pro** (recommended) | Team |
|---|---|---|---|
| For | Occasional meetings | People who live in meetings | Teams sharing notes |
| Price | $8/mo · $64/yr | **$16/mo · $128/yr** | $14/seat/mo (min 3) |
| Meeting hours/month | 5 | 40 | 40 per seat |
| Summaries + action items | ✓ | ✓ | ✓ |
| Search all meetings | — | ✓ | ✓ |
| Notion / Slack integrations | — | ✓ | ✓ |
| Shared workspace, admin, invoices | — | — | ✓ |

Why Pro wins: 8× the hours of Solo for 2× the price. Team costs less per seat but needs 3 seats.

## Common mistakes
- **Tiers without personas.** "Basic / Plus / Premium" with random features makes customers do the thinking.
- **Too many tiers.** More than 3 paid options slows the decision.
- **A value metric that punishes success,** like charging per invoice sent in a tool meant to help people send more invoices.
- **Putting the core loop only in higher tiers.** Low-tier users churn before they ever upgrade.

## Related skills
- [monetization-pricing-strategy](../monetization-pricing-strategy/SKILL.md): price one plan first.
- [monetization-paywall-design](../monetization-paywall-design/SKILL.md): present the tiers.
- [monetization-free-trial-vs-freemium](../monetization-free-trial-vs-freemium/SKILL.md): whether there's a free tier.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Subscription group behaviour from Apple's "Auto-renewable
subscriptions" documentation. "Good-better-best" is a long-standing pricing pattern.
