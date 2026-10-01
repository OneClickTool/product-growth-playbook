---
name: email-trial-sequence
description: Write the free-trial email sequence that turns trial users into paying customers: trial started, value reminder, mid-trial check, trial ending soon (with a clear billing reminder for card-up-front trials), trial ended, and a win-back offer, with timing for 7-, 14- and 30-day trials and branches for active vs inactive users. Works for SaaS, web apps, Mac apps sold outside the App Store and browser extensions with paid plans; explains what to do instead for App Store / Google Play subscription trials. Use when trials don't convert, when setting up trial emails, or when someone asks "trial ending email", "trial expiration email", "free trial reminder", "how to convert trial users" or "win-back email".
license: MIT
metadata:
  category: email
  difficulty: intermediate
  time: 45-60 min
  version: 1.0.0
  author: nvminhtu
---

# Free-Trial Email Sequence

> In under an hour you will have a 6–8 email trial sequence with timing for your trial length, active/inactive
> branches, and a billing reminder your customers won't feel tricked by.

## Goal
During a trial, users decide one thing: *is this worth paying for?* The sequence makes sure they reach the value
before the trial ends, know exactly when it ends and what happens next, and get one fair second chance afterwards.

## When to use
- You run a time-limited trial (with or without a card up front) and sell through your own checkout
  (Stripe, Paddle, Lemon Squeezy, Gumroad…).
- Trials start but few convert, or customers complain about surprise charges.
- **Not for:** choosing trial vs freemium or the trial length → [monetization-free-trial-vs-freemium](../../monetization/monetization-free-trial-vs-freemium/SKILL.md).
- **App Store / Google Play subscription trials:** the store runs billing, and you usually don't have the user's
  email. Put the reminders **in the app** (a banner or a screen with the end date, push notifications if the user
  opted in) and keep the store's subscription management link one tap away. Use emails only if the user created an
  account and agreed to get them.

## Inputs
- Trial length, card up front or not, and what happens at the end (charged automatically / locked / downgraded to free).
- The activation event (see [email-onboarding-sequence](../email-onboarding-sequence/SKILL.md)) and 2–3 paid features users love.
- Price, plans, and any discount you are willing to offer once.
- Events you can send to the email tool: trial_started, activation_event, plan_upgraded, trial_ended.

## Steps
1. **Write the facts block (5 min).** Trial end date, the price after it, what happens automatically, and how to
   cancel or upgrade in one click. Every trial email reuses these exact words, so nothing is a surprise.
2. **Pick the timing for your length (10 min).**

   | Email | 7-day trial | 14-day trial | 30-day trial | Send to |
   |---|---|---|---|---|
   | 1 Trial started + first step | day 0 | day 0 | day 0 | everyone |
   | 2 Value: "do this one thing" | day 1 | day 2 | day 3 | not activated |
   | 3 Mid-trial: what you've done / a power feature | day 3 | day 7 | day 14 | activated |
   | 4 Rescue: "stuck? reply to me" | day 4 | day 8 | day 15 | not activated |
   | 5 Ending soon (+ billing reminder) | day 5 | day 11 | day 25 | everyone not yet paid |
   | 6 Last day | day 7 | day 14 | day 30 | everyone not yet paid |
   | 7 Trial ended | +1 | +1 | +1 | not converted |
   | 8 Win-back (one offer) | +7 to +14 | +14 | +14 to +30 | not converted, opted in to marketing |

3. **Card-up-front trials: make the billing reminder impossible to miss.** Email 5 states the charge date, the
   amount and the cancel link in the first two lines. Consumer-protection rules and card-network rules in many
   places expect a clear notice before a trial turns into a charge; check the ones for your market and your payment
   provider's guidance. It is also what keeps refund requests and chargebacks down.
4. **Write each email (20 min).** One idea, one CTA, under 120 words. Active users: show their own progress and the
   paid feature they'll lose. Inactive users: the fastest route to value, plus "reply if something's in the way".
   Ending emails: the facts block, then *one* reason to stay.
5. **Exit rules.** Upgraded → stop and send a thank-you/receipt. Cancelled → stop the sequence, send one short
   confirmation, and ask one question ("What was missing?"). Account deleted or unsubscribed → stop all marketing.
6. **Win-back, once.** One email 1–2 weeks after the end: what changed since they tried it, and at most one offer
   with a real deadline (extended trial or a first-month discount). Then stop.
7. **Measure after a month.** Trial → paid rate for active vs inactive users, refund/chargeback rate, replies to the
   rescue email. Fix the inactive branch first: it is usually the biggest group.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are a lifecycle marketer. Write the free-trial email sequence for my product.

Product: {{what it does, for whom}}   Sold through: {{Stripe / Paddle / Lemon Squeezy / other}}
Trial: {{N}} days, card up front: {{yes/no}}, at the end: {{charged / locked / drops to free plan}}
Price after trial: {{plans and prices}}
Activation event: {{the action}}   Paid features users love: {{2-3}}
One-time offer I can make: {{e.g. 7 extra days, 20% off first month, or none}}
Sender: {{name, role}}   Tone: {{friendly / direct}}

1. Write the facts block (end date, price, what happens, how to cancel) I'll reuse in every email.
2. Give me the timing table for my trial length with send and exit conditions (active vs inactive).
3. Write every email: subject (under 45 characters), preview text, body under 120 words, one CTA.
   Put the billing facts in the first two lines of the "ending soon" email if a card is on file.
4. Write the cancellation confirmation and the single win-back email.
5. List the events my email tool needs, and the 3 metrics to check after a month.
No fake urgency (fake countdowns, invented "spots left"), no invented testimonials; use [placeholders].
````

## Example output

> **Illustrative example.** Fictional product, shown for format.

*Snapnote AI*, 14-day trial, card up front, $12/month after.

Facts block: "Your trial ends on **Tue 14 Oct**. If you keep it, you'll be charged **$12/month** from that day.
Cancel anytime in one click: [Manage plan]."

Email 5, day 11, subject "Your trial ends Tuesday":
"Hi {{first_name}}, a heads-up: your Snapnote trial ends on Tue 14 Oct, and your card will be charged $12/month
from then. Don't want that? [Cancel in one click]. Keeping it? You've summarized 9 meetings so far; Pro keeps your
search across all of them. — Mai, founder"

## Common mistakes
- **Surprise charges.** A buried date or price turns customers into chargebacks. Put the facts first.
- **Same emails for active and inactive users.** Active users need a reason to pay; inactive users need help to start.
- **Discounting in every email.** It trains people to wait. One offer, after the trial, with a real deadline.
- **Stopping at the last day.** Many users decide after the trial ends; the ended + win-back emails catch them.
- **Emailing App Store trial users you never collected consent from.** Use in-app reminders there instead.

## Related skills
- [monetization-free-trial-vs-freemium](../../monetization/monetization-free-trial-vs-freemium/SKILL.md): trial length and card-up-front choice.
- [monetization-paywall-design](../../monetization/monetization-paywall-design/SKILL.md): the in-app upgrade screen the emails link to.
- [email-onboarding-sequence](../email-onboarding-sequence/SKILL.md): activation emails that run alongside.
- [email-list-and-deliverability](../email-list-and-deliverability/SKILL.md): unsubscribe and consent rules for the win-back email.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Unsubscribe and consent rules: see the sources in
[email-list-and-deliverability](../email-list-and-deliverability/SKILL.md). No external numbers are used.
