---
name: strategy-revenue-target
description: Turn a money goal ("$X in N months") into a funnel you can check every week. Works backward from the target to paying customers, trials or installs, visitors and the work each channel must deliver, flags goals that the numbers can't support, and sets weekly checkpoints with a go / fix / kill rule. Includes a standard-library script that does the math. Use when someone says "I want to make $X by <date>", "set a revenue goal", "how many users do I need to make $1,000 a month", "is my income target realistic", "work backward from revenue", "kiếm X tiền trong X tháng", or keeps working without a clear number to hit.
license: MIT
metadata:
  category: strategy
  difficulty: beginner
  time: 45-60 min
  version: 1.0.0
  author: nvminhtu
---

# Revenue Target: X Money in X Time

> In under an hour you'll have one money goal with a deadline, the funnel numbers it needs, and a weekly
> checkpoint that tells you to keep going, fix one step, or stop.

## Goal
Replace "I hope it makes money" with a target you can check. A goal without funnel math is a wish: you can't tell
in week 3 whether you're on track. With the math, every week answers one question: *which number is behind?*

## When to use
- You're starting a product, a new channel or a new year, and want a concrete money goal.
- You work hard on a product but can't say whether it's going well.
- You have several products and need to decide which one gets your time.
- **Not for:** choosing a price → [monetization-pricing-strategy](../../monetization/monetization-pricing-strategy/SKILL.md).
  Deciding where to spend money and when to double down → [strategy-spend-and-timing](../strategy-spend-and-timing/SKILL.md).

## Inputs
- The goal: an amount, a currency, a deadline, and whether it's **monthly recurring** ($1,000 MRR by March) or a
  **total** ($5,000 in the next 90 days).
- Your price and model: one-time, subscription (monthly / yearly), ads, or a mix.
- Your current numbers, even if small: visitors or store page views, installs or sign-ups, trials, paying customers.
  If you have none yet, use the conservative starting rates in step 3 and replace them after 2 weeks of data.
- Hours per week you can actually spend on growth.

## Steps
1. **Write the goal as one line.** `$<amount> <MRR | total> by <date>, from <product>.` One product per line. If
   you have three products, write three lines and pick one to lead.
2. **Turn money into customers.** Divide by what one customer pays you in the period, after store or payment fees
   (check your provider's fee page; store commission is often 15% or 30%).
   - Subscription: `customers needed = MRR target ÷ (monthly price × (1 − fee))`. Yearly plans count as price ÷ 12.
   - One-time: `customers needed = total target ÷ (price × (1 − fee))`.
   - Ads: `daily active users needed = daily target ÷ (revenue per daily user)`, using your own ad network's numbers.
3. **Walk the funnel backward.** Write each step and its conversion rate. Use **your own** rates if you have 2+
   weeks of data. If you don't, start from a low guess and label it `ASSUMED` until real data replaces it.
   `visitors → installs/sign-ups → activated → trial/paywall → paid`
   Run the script to do the math and the "is this possible" check:

   ```bash
   python3 scripts/revenue_backsolve.py --target 1000 --price 5 --fee 0.15 \
     --rates visit_to_install=0.25,install_to_activated=0.4,activated_to_paid=0.04 --weeks 12 \
     --current-visitors 900
   ```

4. **Check capacity.** Compare the visitors per week you need with what your channels bring today. If the gap is
   more than ~5× and you have no new channel planned, the goal is not realistic **for this funnel**. Change one
   lever, not all of them: raise the price, add a yearly plan, fix the weakest conversion step, add one channel, or
   move the deadline. Write down which lever you chose.
5. **Assign each channel a number.** `Reddit: 400 visits/week · ASO: 600 · email: 150 clicks`. A channel without a
   number is a hobby. Use [launch-quick-download-wins](../../launch/launch-quick-download-wins/SKILL.md) to find channels.
6. **Set the weekly checkpoint.** Every Monday, fill one row: actual vs needed for each funnel step. Rules:
   - **Go:** every step ≥ 80% of plan → keep going.
   - **Fix:** one step < 50% of plan → spend the week only on that step.
   - **Kill or pivot:** 3 checkpoints in a row with the *same* step < 50% after fixing it → change the product,
     price or audience. Don't change the target to hide the gap.
7. **Save it** as `growth/revenue-target.md` in your project so your AI agent sees it every session.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are a no-nonsense growth analyst for a solo builder. Never invent my numbers: if a rate is unknown, use a
conservative assumption, mark it ASSUMED, and tell me how to measure it.

Product: {{what it is, platform}}
Goal: {{amount, currency, MRR or total, deadline}}
Price and model: {{e.g. $4.99/month + $29.99/year, or $9 one-time, or ads}}
Store / payment fee: {{e.g. 15%}}
Current numbers per week: {{visitors, installs/sign-ups, activated, trials, paid}} (or "none yet")
Channels I use now and their weekly visitors: {{...}}
Hours per week for growth: {{...}}

1. Convert the goal into paying customers needed (show the formula).
2. Work the funnel backward to visitors per week. Show a table: step, rate, source (MY DATA / ASSUMED), needed per week.
3. Compare with my current traffic. Say plainly whether the goal is realistic. If not, give the ONE lever that
   closes most of the gap and the new numbers with it.
4. Give each channel a weekly number.
5. Write my Monday checkpoint table and the go / fix / kill rules.
Output as Markdown I can save as growth/revenue-target.md.
````

## Example output

> **Illustrative example.** Numbers are made up to show the format.

**Goal:** $1,000 MRR by 31 March, from a habit-tracker iOS app. $4.99/month, 15% store fee → $4.24 per customer.

| Step | Rate | Source | Needed / week (12 weeks) |
|---|---|---|---|
| Paying customers (total) | | | 236 total → ~20 / week |
| Activated → paid | 4% | ASSUMED | 492 activated / week |
| Install → activated | 40% | MY DATA (2 weeks) | 1,230 installs / week |
| Page view → install | 25% | MY DATA | 4,917 page views / week |

Today: ~900 page views / week → gap 5.5× (output of `revenue_backsolve.py`). **Not realistic as is.** Lever chosen: add a $29.99 yearly plan and move
the paywall to after the first completed habit (activation step). Re-run in 2 weeks with real rates.

| Week | Page views | Installs | Activated | Paid | Verdict |
|---|---|---|---|---|---|
| W1 | 950 / 4,917 | 230 / 1,230 | 95 / 492 | 4 / 20 | Fix: traffic |

## Common mistakes
- **A goal without a deadline** ("make money from apps"). It can't be checked, so it never fails and never improves.
- **Copying someone else's conversion rates** from a blog post. Your funnel is yours: label guesses and replace them.
- **Forgetting fees and refunds.** Gross revenue isn't what lands in your bank account.
- **Fixing every step at once.** You won't know what worked. One weak step per week.
- **Moving the target to feel better.** Move the lever, or move the date on purpose and write down why.

## Related skills
- [strategy-spend-and-timing](../strategy-spend-and-timing/SKILL.md): where to put money and time once you know the gap.
- [strategy-product-as-funnel](../strategy-product-as-funnel/SKILL.md): when the real goal is owned users, not this month's revenue.
- [monetization-pricing-strategy](../../monetization/monetization-pricing-strategy/SKILL.md): the price lever.
- [aso-keyword-research](../../aso/aso-keyword-research/SKILL.md): the most common traffic lever for store apps.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Method: standard funnel math, worked backward from the target.
