---
name: email-onboarding-sequence
description: Write the welcome and onboarding email sequence for the first 14 days after sign-up, built around one activation event, with behavior-based branches (did the key action / didn't), subject lines, send timing and the events to track. For SaaS, web apps, Mac apps, browser extensions and mobile apps with accounts. Use when new users sign up but never come back, when setting up a welcome email or drip campaign, or when someone asks "what emails should I send after signup", "welcome email", "onboarding emails", "drip sequence" or "how do I activate new users".
license: MIT
metadata:
  category: email
  difficulty: beginner
  time: 45-60 min
  version: 1.0.0
  author: nvminhtu
---

# Onboarding Email Sequence

> In under an hour you will have 5–6 onboarding emails, each tied to one action, with the send rules that skip
> emails a user doesn't need.

## Goal
Get a new user to the **activation event**: the first moment they get the product's main value (sent the first
invoice, cleaned the first 1,000 tabs, exported the first report). Every email pushes toward that single action,
and stops once it's done.

## When to use
- Sign-ups are fine but most users never return after day 1.
- You're about to launch and have only a "Welcome!" email (or nothing).
- **Not for:** a time-limited trial that must convert to paid → [email-trial-sequence](../email-trial-sequence/SKILL.md)
  (run both: onboarding for activation, trial for the payment decision).
- **Not for:** apps with no account or email (most free mobile apps). Use in-app onboarding and push instead.

## Inputs
- Your activation event, in one sentence, and the 2–3 setup steps before it.
- The events you can send to your email tool (signed_up, completed_setup, activation_event…).
- The most common reason people get stuck (from support emails, session recordings or beta feedback).
- A real person to send from, with a reply-to that is read.
- Deliverability done first → [email-list-and-deliverability](../email-list-and-deliverability/SKILL.md).

## Steps
1. **Define activation (10 min).** Write: "A user is activated when they {{action}} within {{N}} days." Check it
   against your data or beta results: activated users should come back far more often than the rest.
2. **List the friction (10 min).** For each setup step, what stops people? (No data to import, unclear first step,
   needs a teammate, permission prompt.) Each email answers one of these.
3. **Lay out the sequence (15 min).** Start from this skeleton and cut what you don't need:

   | Day | Email | Send if | Goal |
   |---|---|---|---|
   | 0 (instantly) | Welcome: the one first step | everyone | do setup step 1 |
   | 1 | "Here's the fastest way to {{value}}" | not activated | reach activation |
   | 3 | Unblock: the #1 friction, solved | not activated | remove the main blocker |
   | 5 | Proof: a short story or example of the result | not activated | show what's possible |
   | 7 | Personal check-in: "Anything I can help with?" | not activated | get a reply |
   | after activation | Next step: the second most valuable feature | activated | build the habit |
   | 14 | "Here's what you did this week" or a tip | activated | come back again |

4. **Write each email (15 min).** One idea, one link, under 120 words, from a person. Subject lines say the benefit,
   not "Day 3 of onboarding". Plain text often beats designed templates for this.
5. **Add exit rules.** Activation event fired → stop the "not activated" branch. Unsubscribed or deleted the account →
   stop everything. Don't send onboarding to users who came back from a paid plan.
6. **Measure after 2–4 weeks.** Activation rate (activated ÷ sign-ups) with and without the sequence if you can,
   and click → action per email. Rewrite the weakest email first.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are a lifecycle marketer for a small software product. Write my onboarding email sequence.

Product: {{what it does, for whom}}   Platform: {{web / Mac / extension / mobile with account}}
Activation event: {{the action}} within {{N}} days
Setup steps before it: {{1, 2, 3}}
Main reasons people get stuck: {{list}}
Events I can track: {{signed_up, ...}}
Sender: {{name, role}}   Tone: {{friendly / direct / playful}}

1. Confirm or sharpen my activation event in one sentence.
2. Give me the sequence as a table: day, email name, send condition, exit condition, goal.
3. Write every email: subject (under 45 characters) + preview text + body under 120 words + one CTA.
   Use {{first_name}} and the real product terms I gave you. No fake statistics or testimonials;
   leave a [placeholder] where a real customer quote should go.
4. List the events and tracking I need in my email tool to run the branches.
5. Tell me which single email to rewrite first if activation stays low, and why.
````

## Example output

> **Illustrative example.** Fictional product, shown for format.

*Invoicely Lite*, invoicing for freelance designers. Activation: "sends the first invoice within 3 days".

| Day | Email | Send if | Subject |
|---|---|---|---|
| 0 | Welcome | everyone | "Your first invoice takes 2 minutes" |
| 1 | Fastest path | no invoice yet | "Copy this invoice template" |
| 3 | Unblock | no invoice yet | "Not sure what to charge? Use this" |
| 7 | Check-in | no invoice yet | "Can I help? (reply to me)" |
| after 1st invoice | Next step | invoice sent | "Get paid 2× faster with reminders" |

Body of day 0: "Hi {{first_name}}, I'm Lan, I built Invoicely. One thing to do now: add your first client and hit
*Send*. It takes about 2 minutes. [Create my first invoice] Reply if anything's confusing, I read every email."

## Common mistakes
- **A feature tour.** Ten features in one email means none get used. One email, one action.
- **Same emails for everyone.** Users who already activated get "have you tried…?" emails and unsubscribe. Branch on events.
- **Sending from `noreply@`.** Onboarding replies are your best source of friction insights.
- **No exit rules.** Onboarding emails to a user who churned and came back, or deleted the account, look broken.
- **Judging by open rate.** Opens are unreliable (privacy features inflate them). Judge by clicks and activation.

## Related skills
- [email-list-and-deliverability](../email-list-and-deliverability/SKILL.md): domain and consent setup first.
- [email-trial-sequence](../email-trial-sequence/SKILL.md): the payment-decision emails for trials.
- [case-study-award-winning-design](../../case-study/case-study-award-winning-design/SKILL.md): onboarding patterns from award winners.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sequence structure is a common lifecycle-marketing pattern; no
external numbers are used.
