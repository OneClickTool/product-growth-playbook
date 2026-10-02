---
name: strategy-spend-and-timing
description: Decide what a small product should spend money and time on, and when. Splits costs into must-pay, pays-back and nice-to-have, finds the one bottleneck worth funding, reads momentum signals (a channel or post that suddenly works) and slump signals (rising cost, falling reach or retention), and sets rules for when to double down hard, when to cap, and when to stop. Ends with a 2-week "finishing sprint" plan that puts everything behind the one thing that's working. Use when someone asks "what should I spend money on", "should I run ads", "is it worth paying for X", "when do I double down", "something is working, what now", "my numbers are dropping", "when to quit a channel", "điểm bứt tốc", "điểm rơi phong độ", or has a small budget and too many options.
license: MIT
metadata:
  category: strategy
  difficulty: intermediate
  time: "45 min to set up · 15 min every Monday"
  version: 1.0.0
  author: nvminhtu
---

# Spend and Timing: Pay for What Matters, Push When It Works

> A spend list sorted into must-pay / pays-back / skip, one bottleneck to fund, and written rules for when to go
> all-in, when to cap, and when to stop.

## Goal
Small products rarely die from spending too little. They die from spending evenly: a bit on ads, a bit on tools,
a bit on every channel, so nothing gets enough to work. This skill makes spending **lumpy on purpose**: almost
nothing until a signal appears, then a lot, fast, on that one thing.

## When to use
- You have a small budget (money or hours) and a list of things you "should" pay for.
- Something suddenly worked (a post, a keyword, a partner) and you don't know how hard to push.
- Numbers are sliding and you can't tell if it's a dip or the end of a channel.
- **Not for:** setting the money goal itself → [strategy-revenue-target](../strategy-revenue-target/SKILL.md).
  Finding cheap channels → [launch-quick-download-wins](../../launch/launch-quick-download-wins/SKILL.md).

## Inputs
- Your current monthly costs and anything you're thinking of paying for.
- Your funnel numbers per week (from [strategy-revenue-target](../strategy-revenue-target/SKILL.md) if you have it).
- A list of channels you use, with what each brought in the last 4 weeks (visits, installs, paying users).
- Your monthly budget ceiling: the amount you can lose without it hurting.

## Steps
1. **Sort every cost into three buckets.**

   | Bucket | Rule | Typical items |
   |---|---|---|
   | **Must-pay** | Without it you can't ship, get paid or stay legal | Developer accounts, domain, own-domain email with SPF/DKIM/DMARC, a real test device, payment provider |
   | **Pays-back** | You can name the number it moves, and check it in 30 days | A tool that saves hours you'd otherwise spend weekly, a paid test of a channel that already shows organic signal |
   | **Skip for now** | "Everyone has it", "might help", or for a stage you're not in | Premium analytics before 1,000 users, paid ads before activation works, logo redesign, a 5th SaaS subscription |

   Anything in the third bucket waits until a checkpoint moves it up. Write the reason next to each item.
2. **Find the one bottleneck.** Look at the funnel: which step is furthest below plan? Spend **only** there this
   month. If installs are fine but nobody pays, ads make the problem bigger, not smaller.
3. **Define your momentum signal** before it happens, so you recognise it. A momentum signal is a **2× jump** in
   one channel's result for the same effort, sustained for at least 3 days or 2 posts. Examples: a post that brings
   3× the usual sign-ups, a keyword that starts ranking, a partner who sends paying users, an organic share wave.
4. **Define your slump signals.** Any one of these for 2 weeks in a row: cost per paying user up 50%+, reach per post
   down by half, week-1 retention dropping, refunds or 1-star reviews rising. A slump in one channel means
   *rotate that channel*. A slump in retention means *fix the product before spending more on traffic*.
5. **Write the push rules.**
   - **Momentum → push within 72 hours.** Repeat the exact thing (same format, same audience, same hook) 3–5 times,
     put this week's hours behind it, and if it's paid, raise the budget in steps (for example double it) while
     cost per paying user stays under your limit.
   - **Cap:** stop raising the moment cost per paying user crosses the limit you wrote in step 1.
   - **Stop:** a channel with no signal after 2 honest cycles (2 weeks or 4–6 posts done properly) gets dropped,
     and the next one in your list gets its turn.
6. **Plan the finishing sprint.** When one channel clearly works, run a 2-week sprint where everything supports it:
   product fixes for the users it brings, a landing page for that audience, email capture on that path, and a
   clear offer. Close the gap to the target with the channel that already works, instead of starting a new one.
7. **Review every Monday** (15 min): one row per channel, signal / slump / nothing, and the action. Save as
   `growth/spend-and-timing.md`.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are a frugal growth operator who has run small products on tiny budgets. Be direct. Never invent my numbers.

Product and stage: {{...}}
Monthly budget I can lose without pain: {{amount}}
Current costs: {{list with monthly price}}
Things I'm thinking of paying for: {{list}}
Funnel per week (visitors → installs/sign-ups → activated → paid): {{numbers}}
Channels, last 4 weeks, with results: {{channel: visits / installs / paid}}
What changed recently: {{anything that suddenly worked or dropped}}

1. Sort every cost into Must-pay / Pays-back / Skip for now, with a one-line reason and, for Pays-back, the
   number it must move in 30 days.
2. Name my single bottleneck step and what to spend on it this month.
3. Check my channels for momentum signals (2x jump for the same effort) and slump signals. For each, say:
   push, cap, rotate or stop, and why.
4. If anything shows momentum, write a 2-week finishing sprint: daily actions, what to fix in the product,
   where to capture emails, and the budget steps with a stop limit.
5. Give me the Monday review table to fill in.
````

## Example output

> **Illustrative example.** Numbers are made up to show the format.

**Bottleneck:** activated → paid (1.5% vs 4% plan). This month's money goes to paywall copy and a yearly plan, not ads.

| Item | Bucket | Why / number it must move |
|---|---|---|
| Apple Developer Program | Must-pay | Can't ship without it |
| Paid ASO keyword tool | Skip for now | Store search is 70% of installs but conversion, not traffic, is the bottleneck |
| Short-video editing app | Pays-back | Cuts video time from 3 h to 1 h; check: 2 videos/week instead of 1 |
| Search ads test | Skip for now | Paid traffic into a 1.5% paywall loses money |

| Channel | Last 4 weeks | Signal | Action |
|---|---|---|---|
| Short video ("before/after" format) | 2 videos → 3× usual installs each | Momentum | Push: 4 more in the same format this week |
| Reddit | 3 posts, flat | None (cycle 2) | Stop for now, revisit with a milestone post |

## Common mistakes
- **Spreading the budget evenly.** Ten channels at 10% each means none gets enough to show a signal.
- **Buying traffic before activation works.** Paid users who leave on day 1 just make the bad number bigger.
- **Pushing too late.** Momentum fades in days. Decide the push rule now, so you act within 72 hours.
- **Pushing without a cap.** Write the cost limit before raising spend, not after the bill arrives.
- **Quitting after one try.** One post is noise. Two honest cycles, then decide.
- **Calling a product problem a channel problem.** If retention is falling, more traffic won't save it.

## Related skills
- [strategy-revenue-target](../strategy-revenue-target/SKILL.md): the target and funnel this skill spends against.
- [strategy-contrarian-marketing](../strategy-contrarian-marketing/SKILL.md): new channel ideas when everything slumps.
- [social-short-video](../../social/social-short-video/SKILL.md): a common source of momentum signals.
- [monetization-paywall-design](../../monetization/monetization-paywall-design/SKILL.md): when the bottleneck is the paywall.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). The thresholds (2×, 72 hours, 2 cycles) are starting rules of thumb,
not research results. Tune them to your own data.
