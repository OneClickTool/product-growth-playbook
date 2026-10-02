---
name: email-segments-and-tools
description: Split an email list into segments that each get the right emails (by lifecycle stage, by product, by source and by interest), set up the tags and events that keep segments up to date automatically, plan one retention email per segment, clean the list every month, and choose an email tool that fits (creator newsletter tools like Kit, beehiiv, MailerLite, Buttondown; product lifecycle tools like Loops, Customer.io, Brevo; developer and transactional APIs like Resend, Postmark, Amazon SES; self-hosted Listmonk). Use when someone asks "which email tool should I use", "Mailchimp alternative", "Kit vs MailerLite vs Loops", "how to segment my email list", "send different emails to free and paid users", "email list for multiple apps", "how to keep customers with email", "quản lý email list theo tệp", "dùng tool email nào", or has one big list that gets the same email.
license: MIT
metadata:
  category: email
  difficulty: intermediate
  time: "60-90 min + tool setup"
  version: 1.0.0
  author: nvminhtu
---

# Email Segments and Tools: The Right Email to the Right People

> A segment map with the tags and events that fill it, one retention email per segment, a monthly cleanup rule,
> and an email tool chosen for your situation, not for its ads.

## Goal
One list getting one newsletter treats a paying customer, a trial user who never activated and someone who signed
up for a free template two years ago the same. They need different emails, or they unsubscribe. Segments make
each email relevant, which keeps people subscribed, keeps spam complaints low, and keeps your emails landing
in the inbox.

## When to use
- Your list has 200+ contacts, or contacts from 2+ products or sources.
- Free and paying users, or users of different apps, get the same emails.
- You're choosing (or leaving) an email tool.
- **Not for:** the legal and technical basics (consent, SPF/DKIM/DMARC, unsubscribe) →
  [email-list-and-deliverability](../email-list-and-deliverability/SKILL.md), which comes first. Writing the sequences
  themselves → [email-onboarding-sequence](../email-onboarding-sequence/SKILL.md) and [email-trial-sequence](../email-trial-sequence/SKILL.md).

## Inputs
- Where contacts come from today: signup forms, apps, purchases, waitlists, downloads.
- Your products and plans (free, trial, paid, churned).
- Whether your app or backend can send **events** (e.g. "activated", "purchased") to an email tool, via API,
  webhooks, or a connector like Zapier/Make.
- Your current tool, list size, and monthly budget.

## Steps
1. **Map 4 kinds of segments.** You don't need all of them on day one; lifecycle comes first.

   | Kind | Segments | How a contact gets there |
   |---|---|---|
   | **Lifecycle** (most important) | lead → trial/free → activated → paying → at-risk → churned | Events from your app or payment provider |
   | **Product** | One tag per app/game/tool they came from | Tag set by the signup form or app |
   | **Source** | repo, Reddit, short video, store, referral… | Hidden form field or UTM saved at signup |
   | **Interest** | Topics they chose ("Mac tips", "new games") | A preference page or click on a topic link |

2. **Use tags and events, not separate lists.** One list of people, with tags and fields on each person. Separate lists
   for each product cause duplicates, double-charging by contact count in many tools, and missed unsubscribes.
3. **Wire the lifecycle events.** Send at least: `signed_up`, `activated`, `started_trial`, `purchased`,
   `cancelled`, and `last_active_at`. Sources: your backend, your payment provider's webhooks, or app
   events forwarded by a server. Without events, segments go stale in a week.
4. **Write one retention email per lifecycle segment.**

   | Segment | Email | Goal |
   |---|---|---|
   | Lead (no product yet) | What's coming + one useful thing now | Keep interest |
   | Free, not activated | The single step to the value moment | Activation |
   | Activated free | A tip that uses a paid feature's outcome | Upgrade |
   | Paying | "What's new" + how to get more from it, no upsell | Retention, reviews, referrals |
   | At-risk (no activity in N days) | "Here's what you're missing" or "is something broken?" | Win back usage |
   | Churned | One honest win-back after a real improvement | Return |

5. **Choose the tool by situation** (check each tool's current pricing and features; they change often):

   | Your situation | Look at | Why |
   |---|---|---|
   | You write a newsletter, audience is the product | [Kit](https://kit.com/) · [beehiiv](https://www.beehiiv.com/) · [Buttondown](https://buttondown.com/) | Built for creators: forms, tags, sequences, simple sending |
   | Small business, wants one easy tool | [MailerLite](https://www.mailerlite.com/) · [Brevo](https://www.brevo.com/) | Forms, automations and campaigns in one place |
   | SaaS or app, emails triggered by product events | [Loops](https://loops.so/) · [Customer.io](https://customer.io/) · [Brevo](https://www.brevo.com/) | Events and contact properties drive segments and flows |
   | Developer, transactional emails (receipts, logins) from code | [Resend](https://resend.com/) · [Postmark](https://postmarkapp.com/) · [Amazon SES](https://aws.amazon.com/ses/) | APIs for code-sent email; keep transactional separate from marketing |
   | Large list, tight budget, comfortable running a server | [Listmonk](https://listmonk.app/) (self-hosted) + SES | Open source; you own the deliverability and maintenance |

   Rule of thumb: product events → lifecycle tool; content → creator tool. Don't buy an enterprise tool for 500 contacts.
   Before you move, check that you can **export** contacts, tags and unsubscribes.
6. **Clean the list monthly.** Remove hard bounces, and move contacts who haven't opened or clicked in ~90–180 days
   to a "sunset" segment: send one "still want these?" email, then stop emailing those who don't respond.
   (Apple Mail privacy features inflate opens, so use clicks and product activity where you can.) A smaller
   engaged list delivers better than a big cold one.
7. **Track per segment** monthly: unsubscribe rate, spam complaints (stay well under the 0.3% limit in the
   [Gmail sender guidelines](https://support.google.com/a/answer/81126)), clicks, and the segment's conversion
   (activation, upgrade, return). Save in `growth/email-segments.md`.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are a lifecycle email strategist for indie products. Never recommend buying lists, emailing people without
consent, or hiding unsubscribe. Don't state tool prices; tell me to check each pricing page.

Products and plans: {{apps/tools, free / trial / paid}}
Where contacts come from: {{forms, apps, purchases, repos, waitlists}}
List size and current tool: {{...}}
Events my app/backend can send: {{none / via webhooks / via API}}
Budget per month: {{...}}   Can I run a server: {{yes/no}}

1. Design my segments: lifecycle (lead → free → activated → paying → at-risk → churned), product, source, interest.
   For each, say which tag, field or event puts a contact there.
2. List the exact events I need to send and from where (app, backend, payment provider webhook).
3. Write a one-paragraph retention email for each lifecycle segment (subject + body + one CTA).
4. Recommend 1–2 email tools for my situation from: Kit, beehiiv, Buttondown, MailerLite, Brevo, Loops,
   Customer.io, Resend, Postmark, Amazon SES, Listmonk. Explain why, and what to check before moving (export, limits).
5. Give me the monthly cleanup rule and the per-segment tracking table.
````

## Example output

> **Illustrative example.** Fictional products and numbers.

*Two iOS apps + a free Notion template. 3,400 contacts in one Mailchimp list, everyone gets the same monthly newsletter.*

| Segment | Size | Rule | Email this month |
|---|---|---|---|
| Template-only leads | 1,900 | tag `src:notion`, no app | "The app version of your template" (one send) |
| Free, not activated | 620 | `signed_up`, no `activated` in 7 days | "Do this one thing first" |
| Paying | 180 | `purchased`, not `cancelled` | What's new in 2.3, no upsell |
| At-risk paying | 40 | paying, `last_active_at` > 21 days | "Is something broken? Reply and I'll fix it" |
| Sunset | 410 | no clicks in 180 days | "Still want these?", then stop |

**Tool:** move to Loops (events from the backend drive segments); keep Resend for receipts and login emails.
Checked first: Mailchimp export includes tags and unsubscribes.

## Common mistakes
- **One list per product.** Duplicates, double counting, and an unsubscribe in one list that doesn't apply to the other.
- **Segments by hand.** If a person has to update a CSV, it's stale by next week. Use events.
- **Upselling paying customers in every email.** They already paid. Help them; the reviews and referrals come from that.
- **Keeping cold contacts forever.** They hurt deliverability for everyone else. Sunset them.
- **Choosing the tool first.** Map the segments and events first, then pick the tool that handles them.
- **Mixing receipts and marketing on one stream.** If marketing gets flagged as spam, your password-reset emails suffer too.

## Related skills
- [email-list-and-deliverability](../email-list-and-deliverability/SKILL.md): consent, authentication and unsubscribe first.
- [email-onboarding-sequence](../email-onboarding-sequence/SKILL.md): the flow for the "free, not activated" segment.
- [email-trial-sequence](../email-trial-sequence/SKILL.md): the flow for trial users.
- [strategy-product-as-funnel](../../strategy/strategy-product-as-funnel/SKILL.md): where product and source tags come from.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Spam-rate limit: [Gmail Email sender guidelines](https://support.google.com/a/answer/81126)
(checked 2026-10-02). Tool descriptions are general; check each tool's own site for current features and prices.
