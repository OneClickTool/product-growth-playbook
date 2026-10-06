---
name: email-cold-outreach
description: Reach the exact people who need your product with cold email, without burning your domain or breaking the law. Builds a narrow target list from sources you're allowed to use (public business contact pages, people who asked in public on Reddit/forums, LinkedIn conversations, compliant B2B data tools), sets up a separate sending domain, writes a short 3–4 email sequence with real personalization, and tracks reply rate per segment. Use when someone asks "cold email", "outbound", "how to find customers' emails", "email prospects", "B2B outreach", "reach agencies/shops/developers directly", "get my first paying customers by email", "lấy email khách hàng", "gửi email lạnh", or has a B2B or prosumer product and no inbound yet.
license: MIT
metadata:
  category: email
  difficulty: intermediate
  time: "2-3 h setup + 2 weeks domain warm-up"
  version: 1.0.0
  author: nvminhtu
---

# Cold Email Outreach: Reach the Exact Buyer

> A list of 50–100 people who clearly have the problem you solve, a warmed-up sending domain separate from your
> main one, a 3–4 email sequence that gets replies, and a sheet that shows which segment is worth scaling.

## Goal
Cold email is the one channel where **you** pick who hears about the product, down to the person. That makes it
the fastest way to test a B2B or prosumer idea and land the first paying customers. It only works when the list is
narrow, the reason to write is real, and the sending setup can't hurt your main domain.

## When to use
- Your buyer is a business or a professional (agency, shop owner, developer, recruiter, clinic, creator) and you can
  describe them in one line.
- You have no inbound yet, or inbound is too slow to test pricing and positioning.
- You want 10–20 customer conversations this month, not a viral moment.
- **Not for:** emailing people who signed up → [email-onboarding-sequence](../email-onboarding-sequence/SKILL.md).
  Consumer apps (B2C): cold email to individuals is mostly illegal in the EU/UK and ignored elsewhere; use
  [launch-reddit-posting](../../launch/launch-reddit-posting/SKILL.md) or [social-short-video](../../social/social-short-video/SKILL.md).

## Inputs
- One sentence: who the product is for and the problem it removes.
- 1–3 candidate segments (e.g. "Shopify stores with 50–500 products that sell in 2+ languages").
- A trigger you can see from outside: hiring for a role, a bad competitor review, a public question, a new launch.
- A second domain (e.g. `getyourapp.com` if the product is on `yourapp.com`) and 2 mailboxes on it.
- One proof point: a result, a customer quote, a demo video, or "free for the first 10 teams".

## The rules (official sources)

| Rule | What it means for cold email | Source |
|---|---|---|
| US: CAN-SPAM | Allowed without prior consent, **including B2B**, if: honest From and subject, says it's an ad (a plain sentence is fine), your postal address, a clear opt-out honored within 10 business days | [FTC CAN-SPAM guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business) |
| UK: PECR | Companies, LLPs and government bodies ("corporate subscribers") can be emailed without consent; you must say who you are and give an opt-out. Sole traders and some partnerships count as individuals: they need consent. UK GDPR still applies to a named person's work email | [ICO: business-to-business marketing](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/) |
| Gmail | Spam rate below 0.3% in Postmaster Tools, SPF/DKIM, one-click unsubscribe for bulk senders. Above 0.3%, delivery to Gmail drops | [Gmail sender guidelines](https://support.google.com/a/answer/81126) |
| LinkedIn | Bots, crawlers and browser extensions that scrape profiles are not allowed; accounts get restricted | [LinkedIn: prohibited software and extensions](https://www.linkedin.com/help/linkedin/answer/a1341387) |
| Facebook / Meta | Automated collection (scraping) is banned without written permission, logged in or out | [How Meta combats scraping](https://about.fb.com/news/2021/04/how-we-combat-scraping/) |

EU countries outside the UK each have their own rule for B2B email; some require consent even for business
addresses. If your list is in the EU, check the country's regulator page before sending. This skill is not legal advice.

## Where emails can come from

The question is never "where can I get emails", it's "who has a visible reason to want this, and how do I reach them
in a way they won't report". Ranked from warmest to coldest:

| # | Source | How | Allowed? |
|---|---|---|---|
| 1 | **People who asked in public** (Reddit, forums, GitHub issues, Stack Overflow, Indie Hackers) | Reply in the thread with real help first. If it fits, ask in a DM on that platform whether you can email a demo. Find threads with [research-where-users-ask](../../research/research-where-users-ask/SKILL.md) | ✅ Warmest; they asked |
| 2 | **Competitor reviewers** who complained about the exact thing you fix | Find them with [research-review-mining](../../research/research-review-mining/SKILL.md). Reach businesses via their own site's contact page, not via the review site | ✅ If you use public business contacts |
| 3 | **LinkedIn, by hand** | Search, read, send a connection request with a one-line reason. After they accept, have the conversation there, or ask for an email. No scraping extensions, no auto-connect tools | ✅ Manual only |
| 4 | **Company websites and business listings** (team page, contact page, Google Maps business profile, app store "developer contact", GitHub org email) | Use the address the business publishes for contact. Prefer role or named work addresses | ✅ B2B, with opt-out |
| 5 | **B2B data tools** (e.g. Apollo, Hunter, Prospeo) | Search by role + company type, then verify each address. Read the tool's terms and where it got the data | ⚠️ Check the tool's compliance and your region |
| ✗ | Scraping LinkedIn or Facebook, buying "leads" lists, harvesting personal Gmail addresses from groups | | ❌ Bans, spam traps, illegal in the EU/UK |

Bought and scraped lists don't just break rules: they're full of dead addresses and spam traps, so your bounce and
spam rates jump and the domain stops landing in the inbox, for every list.

## Steps
1. **Pick one segment (15 min).** Write it as *role + company type + visible trigger*: "Founders of Mac apps that
   launched in the last 90 days and have under 20 ratings." If you can't name the trigger, the segment is too broad.
2. **Set up the sending domain (30 min + 2 weeks).** Buy a second domain that redirects to your site. Create 2
   mailboxes on it with a real name, a photo and a signature. Add SPF, DKIM and DMARC (see
   [email-list-and-deliverability](../email-list-and-deliverability/SKILL.md)). Warm it up for ~2 weeks: real
   back-and-forth emails, then a few cold sends a day. Never cold-email from your main product domain.
3. **Build the list (60 min for 50 people).** Use sources 1–4 first. For each row: name, company, role, email,
   where you found them, **the trigger you saw**, and one personal observation. Verify every address with an email
   verifier; drop anything "risky" or "catch-all" for the first sends.
4. **Write the sequence (30 min).** 3–4 emails, each under ~90 words, plain text, no images, at most one link:
   - **Email 1:** observation → problem → small proof → low-effort ask ("Worth a 2-min video?").
   - **Email 2 (+3 days):** a new angle (a different pain or a quick result), not "just bumping this".
   - **Email 3 (+5 days):** a useful give: a teardown, a checklist, a free slot.
   - **Email 4 (+7 days, optional):** a polite close ("Should I stop writing?").
   Subject lines: 2–4 words, lowercase, sound like a colleague ("your ratings prompt"). Footer: one line with your
   company, postal address and "Reply 'no' and I won't email again."
5. **Send slowly (ongoing).** Start at about 20 new people per mailbox per day and only raise it while the bounce
   rate stays under ~2% and nobody reports spam (a common practitioner rule of thumb, not an official limit). Stop
   the sequence the moment someone replies, and add every "no" to a do-not-email list.
6. **Track (10 min a week).** One row per segment: sent, bounced, replied, positive replies, calls, customers. Kill a
   segment after ~100 sends with no positive reply; rewrite email 1 or change the trigger.
7. **Turn replies into proof.** Each yes is a case study, a testimonial, or a better trigger for the next segment.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are a cold email strategist for a small software product. You only use contact sources that are legal and
allowed by each platform's terms (no scraping LinkedIn or Facebook, no bought lists).

Product: {{one sentence: what it does and for whom}}
Price / offer: {{price, free tier, or "free for the first 10 teams"}}
Proof I have: {{result, quote, demo link, or "none yet"}}
Candidate segments: {{1-3 segments}}
Where my buyers are: {{US / UK / EU country / other}}

1. Score each segment on: pain intensity, a trigger visible from outside, how easy it is to find contacts legally,
   and deal size. Pick ONE and rewrite it as "role + company type + visible trigger".
2. List 5 concrete places to find these people (subreddits, forums, directories, LinkedIn searches, public pages),
   and for each say what the trigger looks like there and how to get a business contact without scraping.
3. Write a 4-email sequence: under 90 words each, plain text, 2-4 word lowercase subject lines, one ask per email,
   each follow-up with a new angle. Use {{first_name}}, {{company}} and {{observation}} placeholders.
4. Write a compliant footer for my region (sender identity, postal address placeholder, opt-out line), and tell me
   which official rule applies, with the source link. If my region needs consent for B2B email, say so plainly.
5. Give me a tracking table (sent, bounced, replied, positive, calls, customers) and the rule for when to kill or
   scale the segment.
Never invent statistics. If you give a benchmark, label it as a rule of thumb.
````

## Example output

> **Illustrative example.** Fictional product and numbers, shown for format.

*Rateline*, a $19/month tool that asks Mac app users for a rating at the right moment. Buyers in the US and UK.

**Segment:** indie Mac app developers (company or LLC) who launched in the last 90 days and have under 20 ratings.
**Trigger:** a recent "Show HN" / r/macapps launch post, or under 20 ratings on the Mac App Store page.
**Where:** r/macapps and r/SideProject launch threads → help in the thread first; developer website contact pages;
the "developer website" link on the App Store page.

```text
subject: ratings on notchpad

Hi Sam, saw Notchpad on r/macapps last week. Nice launch, 140 upvotes.
The App Store page shows 6 ratings though, so most of that traffic left no trace.
Rateline asks at the moment a user finishes a task, not on launch. A 2-min video of how it'd look in Notchpad?

Tu, Rateline
Rateline LLC, <postal address> · Reply "no" and I won't email again.
```

| Segment | Sent | Bounced | Replied | Positive | Calls | Customers |
|---|---|---|---|---|---|---|
| Mac apps, launched < 90 days | 80 | 1 | 11 | 6 | 4 | 2 |
| iOS games, < 20 ratings | 100 | 4 | 3 | 0 | 0 | 0 → kill |

## Common mistakes
- **"Spray and pray" lists of thousands.** Fifty people with a visible trigger beat 5,000 scraped addresses, and
  won't wreck your domain.
- **Sending from the main domain.** One bad week and your login and receipt emails start landing in spam too.
- **Fake personalization** ("Loved your website!"). If you can delete the first line and the email still makes
  sense, it isn't personal.
- **Follow-ups that only say "bumping this".** Each one needs a new reason to reply, or stop.
- **No opt-out, or ignoring a "no".** That's the CAN-SPAM line, and the fastest way to get reported.
- **Adding cold contacts to your newsletter.** They didn't sign up. Only people who replied yes can be invited.

## Related skills
- [research-where-users-ask](../../research/research-where-users-ask/SKILL.md): find people asking for what you built.
- [research-review-mining](../../research/research-review-mining/SKILL.md): find the competitor pain to open with.
- [email-list-and-deliverability](../email-list-and-deliverability/SKILL.md): SPF, DKIM, DMARC for the sending domain.
- [social-credible-posting](../../social/social-credible-posting/SKILL.md): the LinkedIn profile prospects will check.
- [case-study-write-your-own](../../case-study/case-study-write-your-own/SKILL.md): turn the first customers into proof.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sequence structure inspired by the
[cold-email skill in coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/main/skills/cold-email/SKILL.md) (MIT).
Sources: [FTC CAN-SPAM guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business),
[ICO: business-to-business marketing](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/),
[Gmail sender guidelines](https://support.google.com/a/answer/81126),
[LinkedIn: prohibited software and extensions](https://www.linkedin.com/help/linkedin/answer/a1341387),
[Meta: how we combat scraping](https://about.fb.com/news/2021/04/how-we-combat-scraping/). Checked 2026-10-05.
