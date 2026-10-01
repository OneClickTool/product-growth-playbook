---
name: email-beta-program
description: Run a beta program for an app, SaaS, browser extension or Mac app, by email: recruit testers from your waitlist, invite them through TestFlight, Google Play closed testing or Chrome Web Store trusted testers, track every tester in one sheet, ask for feedback at the right moments, and turn beta users into first paying customers. Includes the invite, reminder, feedback and "beta is over" emails. Use when you need beta testers, are setting up TestFlight or a closed test, need the 12 testers for Google Play, testers sign up and go silent, or someone asks "how do I manage beta users", "beta invite email", "how to get feedback from testers" or "beta to paid".
license: MIT
metadata:
  category: email
  difficulty: intermediate
  time: 2 h setup + 2-6 weeks running
  version: 1.0.0
  author: nvminhtu
---

# Beta Program by Email

> In two hours you will have a tester sheet, an invite flow for your platform, five ready emails, and a clear plan
> for ending the beta and converting testers.

## Goal
A beta should give you three things: bugs found before launch, proof that people use the core feature, and your
first paying customers. Most betas fail because testers are invited and then forgotten. This skill keeps every
tester moving from *invited → installed → used → gave feedback → converted*.

## When to use
- You have a working build and want 10–200 real people to try it before launch.
- A new Google Play personal account needs a closed test (see the rule below).
- Testers signed up but almost nobody installed or replied.
- **Not for:** collecting the waitlist itself → [email-list-and-deliverability](../email-list-and-deliverability/SKILL.md).
  Finding people in the first place → [launch-get-first-100-users](../../launch/launch-get-first-100-users/SKILL.md).

## Inputs
- A build testers can install, and the platform(s).
- A list of people who opted in to hear from you (waitlist, community, friends).
- The **one core action** you want testers to do (e.g. "create and export one invoice").
- Your offer for testers at the end (e.g. 50% off the first year, a free lifetime license for top testers).

## Where testers install (official limits)

| Platform | Channel | Limits and rules | Source |
|---|---|---|---|
| iOS / Mac App Store | TestFlight | Up to 100 internal testers and 10,000 external testers; the first external build needs TestFlight App Review; invite by email or public link; a build expires after 90 days | [TestFlight](https://developer.apple.com/testflight/), [TestFlight overview](https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview) |
| Android | Play internal / closed / open testing | Internal: up to 100 testers, by email list. Closed: email lists or Google Groups. Open: anyone can join from Play or an opt-in link | [Play Console: set up testing](https://support.google.com/googleplay/android-developer/answer/9845334) |
| Android, new personal account | Closed test before production | At least 12 testers opted in for 14 continuous days (see [listing-google-play](../../listing/listing-google-play/SKILL.md)) | [Play Console Help](https://support.google.com/googleplay/android-developer/) |
| Chrome extension | Private visibility + trusted testers | Trusted testers are set on the account (Developer Dashboard → Account), Google Groups can be added; set the item's visibility to Private | [CWS: set up distribution](https://developer.chrome.com/docs/webstore/cws-dashboard-distribution) |
| Web / SaaS / Mac outside the store | Invite code or allow-list | Your own sign-up with a beta flag | — |

Use a **Google Group** as the tester list on Android and Chrome: you add people to the group once and they get access.

## Steps
1. **Set up the tester sheet (15 min).** One row per tester, these columns:
   `email · name · source · platform/device · invited (date) · installed (Y/N) · did core action (Y/N) · feedback (link) · NPS/score · offer sent · converted · notes`.
   Use the platform's dashboard (TestFlight, Play Console) to fill *installed*; your analytics or a simple event to
   fill *did core action*.
2. **Recruit (30 min).** Email your waitlist with the *recruit* email below. Ask 2–3 qualifying questions (device,
   what they use today, how often they have the problem). Pick testers who have the problem now, not only friends.
   Aim for 2–3× the testers you need: about half will never install.
3. **Invite in small waves (ongoing).** Wave 1: 10–20 people. Fix what breaks. Then the next wave. Each invite email
   has one link and one task.
4. **Nudge on a schedule (automate it).** Day 2 after invite: not installed → *reminder*. Day 5: installed but no core
   action → a short "stuck?" email with a GIF of the core action. Never more than one email every 3 days.
5. **Ask for feedback at the moment of value (ongoing).** After the core action, ask 3 questions max: *What did you
   expect to happen? What almost made you stop? Would you be disappointed if you couldn't use it anymore?*
   Reply personally to every answer within a day: that is what keeps testers active.
6. **Report back weekly (10 min/week).** A short "what we fixed this week" email to all testers. Name the testers who
   found bugs (with permission). It turns testers into fans.
7. **End the beta (1 week before launch).** Send the *beta is over* email: what you shipped, the launch date, the
   tester offer with a clear deadline, and a request to rate or review on launch day (asking for an honest review,
   never a 5-star one). Then move testers who don't convert to your normal newsletter only if they opted in to it.
8. **Score the beta.** Install rate (installed ÷ invited), activation (core action ÷ installed), feedback rate, and
   tester → paid conversion. Write it down for the next launch.

## The five emails (templates)
Keep each one short, from a real person, plain text or near-plain.

| # | When | Subject idea | Body (1–4 lines) + one CTA |
|---|---|---|---|
| 1 Recruit | To waitlist | "Want early access to {{product}}?" | What it does, what testers get, 3 questions → *Apply* |
| 2 Invite | On approval | "You're in: your {{product}} beta invite" | The link, the one task, how to send feedback → *Install* |
| 3 Reminder | Day 2, not installed | "Your invite is waiting" | One line + the link again + "reply if something's wrong" |
| 4 Feedback | After core action | "Quick question about {{core action}}" | The 3 questions; "just hit reply" |
| 5 Beta over | 1 week before launch | "Thank you, and your tester offer" | What changed, launch date, offer + deadline → *Claim* |

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are a product manager running a beta program for a small software product.

Product: {{what it does}}   Platform(s): {{iOS / Android / Chrome extension / Mac / web}}
Core action testers must do: {{one action}}
Testers needed: {{number}} (Google Play new personal account? {{yes/no}})
Who's on my list: {{waitlist size, where they came from}}
Tester offer at the end: {{discount / lifetime license / none}}
Launch date: {{date}}

1. Tell me which install channel to use per platform and the steps to invite testers there.
2. Give me the tester tracking sheet as a table header plus 3 example rows.
3. Write the 5 emails (recruit, invite, reminder, feedback, beta over): subject + body under 80 words each,
   one CTA each, friendly first-person tone. Use {{first_name}} placeholders.
4. Give me the nudge schedule as rules ("if invited 2 days ago and not installed → email 3").
5. List the 4 metrics to judge the beta and a good-enough target for each, labelled as rough guidance.
Do not promise testers anything the stores forbid (e.g. paying for reviews or ratings).
````

## Example output

> **Illustrative example.** Fictional product and numbers, shown for format.

*Plainbudget* (iOS + Android). Core action: "add 5 expenses in one week". Target 40 testers, Play account is new.

| email | source | platform | invited | installed | core action | feedback | converted |
|---|---|---|---|---|---|---|---|
| ana@… | waitlist | iPhone 13 | 03 Oct | Y | Y | 4 bugs, "would be disappointed" | Y (50% off yr) |
| ben@… | r/personalfinance | Pixel 7 | 03 Oct | Y | N | — | — |
| chi@… | friend | Galaxy S22 | 05 Oct | N | — | — | — |

Results after 3 weeks: 64 invited → 41 installed (64%) → 27 core action (66%) → 19 replied → 9 paid at launch.

## Common mistakes
- **Inviting everyone at once.** The first build always has a blocker; wave 1 should be small.
- **Only friends as testers.** They're polite, not representative. Mix in people who have the problem.
- **Feedback forms with 15 questions.** Ask 3, at the moment of value, and let people reply by email.
- **Going silent.** Testers who hear nothing for two weeks stop opening the app. Send the weekly "what we fixed".
- **Rewarding reviews.** Offering anything in exchange for ratings breaks store rules. Ask for an *honest* review.
- **Recruiting exactly 12 for the Play closed test.** Some testers opt out or never accept; recruit a buffer so you
  stay at or above the minimum for the whole 14 days.

## Related skills
- [email-list-and-deliverability](../email-list-and-deliverability/SKILL.md): set up the list and domain first.
- [email-trial-sequence](../email-trial-sequence/SKILL.md): for testers who move to a trial at launch.
- [listing-google-play](../../listing/listing-google-play/SKILL.md) · [listing-app-store](../../listing/listing-app-store/SKILL.md): the store steps after the beta.
- [aso-review-and-rating-strategy](../../aso/aso-review-and-rating-strategy/SKILL.md): asking for ratings at launch.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: [Apple TestFlight](https://developer.apple.com/testflight/),
[App Store Connect: TestFlight overview](https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview),
[Play Console: set up an open, closed or internal test](https://support.google.com/googleplay/android-developer/answer/9845334),
[Chrome Web Store: set up distribution](https://developer.chrome.com/docs/webstore/cws-dashboard-distribution). The
"would you be disappointed" question follows Sean Ellis's product/market fit survey. Checked 2026-10-01.
