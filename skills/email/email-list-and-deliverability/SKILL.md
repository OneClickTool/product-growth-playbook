---
name: email-list-and-deliverability
description: Build an email list the legal way (waitlist, opt-in, double opt-in), pick a sending tool, and set up SPF, DKIM, DMARC and one-click unsubscribe so emails land in the inbox instead of spam. Covers the Gmail and Yahoo bulk-sender rules, CAN-SPAM and EU/UK consent. Use when starting a waitlist or newsletter, before sending a first launch or trial email, when emails go to spam, or when someone asks "how do I collect emails", "which email tool", "SPF DKIM DMARC", "why are my emails in spam" or "do I need consent".
license: MIT
metadata:
  category: email
  difficulty: beginner
  time: 60-90 min + DNS propagation
  version: 1.0.0
  author: nvminhtu
---

# Email List & Deliverability

> In about an hour you will have a signup form, a sending tool on your own domain with SPF, DKIM and DMARC
> passing, a working unsubscribe, and a one-page compliance note.

## Goal
Every other email skill (onboarding, trial, beta) depends on two things: people who agreed to hear from you, and
mail that actually reaches the inbox. Set both up once, before the first real send.

## When to use
- You are about to start a waitlist, beta list or newsletter.
- You are about to send your first launch, onboarding or trial email.
- Open rates suddenly dropped, or replies say "this was in my spam folder".
- **Not for:** what to write in the emails → [email-onboarding-sequence](../email-onboarding-sequence/SKILL.md),
  [email-trial-sequence](../email-trial-sequence/SKILL.md), [email-beta-program](../email-beta-program/SKILL.md).

## Inputs
- A domain you control (and access to its DNS settings).
- Where signups happen: landing page, in-app account creation, checkout.
- Rough volume: how many emails per day you expect to send in 3 months.
- Where your users live (US, EU/UK, elsewhere): it decides the consent rules.

## Rules you must meet (official sources)

| Rule | What it requires | Source |
|---|---|---|
| Gmail, all senders | SPF **or** DKIM, valid forward/reverse DNS, TLS, spam rate in Postmaster Tools below 0.3% | [Gmail sender guidelines](https://support.google.com/a/answer/81126) |
| Gmail, bulk (more than 5,000 msgs/day to Gmail) | SPF **and** DKIM **and** DMARC (policy may be `p=none`), From domain aligned, one-click unsubscribe plus a visible unsubscribe link in marketing mail | [Gmail sender guidelines](https://support.google.com/a/answer/81126) |
| Yahoo | SPF and DKIM, DMARC at least `p=none`, one-click `List-Unsubscribe`, honor unsubscribes within 2 days, spam rate below 0.3% | [Yahoo sender best practices](https://senders.yahooinc.com/best-practices/) |
| US: CAN-SPAM | Honest From/subject, your valid physical postal address, a clear opt-out, honor opt-outs within 10 business days, opt-out must work for at least 30 days after sending | [FTC CAN-SPAM guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business) |
| EU / UK | Marketing email to individuals needs specific consent. UK "soft opt-in": existing customers who bought something similar, with an opt-out offered at signup and in every message | [ICO: electronic mail marketing](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/electronic-and-telephone-marketing/electronic-mail-marketing/) |

Transactional mail (password reset, receipt, "your trial ends tomorrow" as an account notice) is mostly exempt from
CAN-SPAM, but must still be honest. Keep marketing content out of it.

## Steps
1. **Pick a sending setup (10 min).** Split two kinds of mail:
   - *Transactional* (sign-in links, receipts, trial-ending notices): sent by your app through a transactional
     service, or by the store / payment provider.
   - *Marketing & sequences* (newsletter, onboarding, launch): an email marketing tool with automations, double
     opt-in and a built-in unsubscribe.
   Choose tools that let you send from **your own domain**, not a shared one. Check each tool's current free plan
   limits on its pricing page; they change often.
2. **Send from a subdomain (5 min).** Use for example `mail.yourdomain.com` or `news.yourdomain.com` for marketing,
   so a bad campaign doesn't hurt your login emails. Use a real reply-to address that someone reads.
3. **Add the DNS records (20 min + up to 48 h).** The tool gives you the exact values; paste them into your DNS:
   - **SPF**: one TXT record listing who may send for the domain. Only one SPF record per name; merge, don't add a second.
   - **DKIM**: the TXT/CNAME records the tool generates.
   - **DMARC**: a TXT record at `_dmarc.yourdomain.com`, start with `v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com`.
     Move to `p=quarantine` once reports show only your tools sending.
4. **Verify (10 min).** Send a test to a Gmail address → *Show original* → SPF, DKIM and DMARC must say `PASS`.
   Register the domain in Google Postmaster Tools to watch the spam rate once you have volume.
5. **Build the signup (15 min).** One field (email), one sentence that says exactly what they'll get and how often
   ("Launch news and one tip a month. Unsubscribe anytime."). Turn on **double opt-in** for waitlists and newsletters:
   it keeps fake and mistyped addresses out. Never pre-tick a marketing box at account creation.
6. **Footer and unsubscribe (5 min).** Every marketing email: who you are, your postal address (a business address
   or P.O. box works), why they get it, and a one-click unsubscribe. Test that it works.
7. **Write the one-page compliance note (10 min).** Where consent is collected, what text they saw, how unsubscribes
   are synced between tools, who deletes data on request. Keep it in your repo or docs.
8. **Keep the list healthy (monthly).** Remove hard bounces automatically, and after ~6 months of no opens, send one
   "still want these?" email, then remove the ones who don't respond.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are an email deliverability and compliance assistant for a small software product.

Product: {{what it is}}   Domain: {{yourdomain.com}}   DNS provider: {{Cloudflare / Namecheap / ...}}
Signups come from: {{landing page waitlist / in-app sign-up / checkout}}
Expected volume in 3 months: {{emails per day}}
Users are mostly in: {{US / EU / UK / other}}
Tools I'm considering or using: {{names, or "none yet"}}

1. Recommend a setup that separates transactional and marketing mail, and say which subdomain each should use.
2. Give me the DNS checklist (SPF, DKIM, DMARC) as a table: record type, host, what goes in the value, and how to
   verify it. Don't invent DKIM keys: tell me where in the tool I'll find them.
3. Write the signup form text (one sentence + button) and the double opt-in confirmation email.
4. Write a marketing email footer that meets CAN-SPAM and the Gmail/Yahoo unsubscribe rules.
5. List what consent I need for my users' region and anything I must not do (bought lists, pre-ticked boxes).
6. Give me a monthly list-hygiene checklist.
Cite the official page for every rule you state; if you're not sure a rule is current, say so.
````

## Example output

> **Illustrative example.** Fictional product, shown for format.

*Tabsy* (browser extension), waitlist on `tabsy.app`, US + EU users, ~50 emails/day.

| Record | Host | Value | Check |
|---|---|---|---|
| TXT (SPF) | `news.tabsy.app` | `v=spf1 include:<tool's SPF domain> ~all` | Gmail "Show original": SPF PASS |
| CNAME (DKIM) | `<selector>._domainkey.news.tabsy.app` | from the tool's *Domain* page | DKIM PASS |
| TXT (DMARC) | `_dmarc.tabsy.app` | `v=DMARC1; p=none; rua=mailto:dmarc@tabsy.app` | DMARC PASS, reports arrive weekly |

Signup: "Get an email when Tabsy launches, plus one tip a month. Unsubscribe anytime." → double opt-in on.

## Common mistakes
- **Sending from `@gmail.com` or the tool's shared domain.** Use your own domain, with SPF, DKIM and DMARC passing.
- **Two SPF records** on the same name. Receivers treat that as an error; merge them into one.
- **Importing contacts who never signed up** (event lists, LinkedIn exports, bought lists). Spam complaints follow,
  and in the EU/UK it's not allowed.
- **Hiding the unsubscribe link.** People press "Report spam" instead, which counts against your 0.3% limit.
- **Mixing marketing into transactional mail.** A receipt with a big promo block is treated as marketing.

## Related skills
- [email-onboarding-sequence](../email-onboarding-sequence/SKILL.md): the first emails a new user gets.
- [email-beta-program](../email-beta-program/SKILL.md): turning the waitlist into beta testers.
- [launch-pre-launch-checklist](../../launch/launch-pre-launch-checklist/SKILL.md): where the waitlist fits in the launch.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: [Gmail email sender guidelines](https://support.google.com/a/answer/81126),
[Yahoo sender best practices](https://senders.yahooinc.com/best-practices/),
[FTC CAN-SPAM Act compliance guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business),
[ICO guide to electronic mail marketing](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/electronic-and-telephone-marketing/electronic-mail-marketing/). Checked 2026-10-01.
