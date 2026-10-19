---
name: email-google-maps-leads
description: Find local businesses in one area (a city, a district, a street) on Google Maps that clearly need what you sell, get their contact from the business's own website, and email them a short, personal hello they won't report. Covers what Google's terms allow (browse Maps by hand, record contacts from the business's site, no scraping or bulk export), which countries let you cold-email a business and which need consent first (US, UK, EU, Vietnam), a lead sheet, a 3-email sequence and a weekly scorecard. Use when someone asks "Google Maps marketing", "find customers on Google Maps", "local leads", "lead list from Google Maps", "email local shops / salons / clinics / restaurants", "B2B prospecting by location", "tìm khách hàng trên Google Map", "lấy email khách hàng theo khu vực", "gửi mail chào khách", or sells an app, website, booking tool or service to local businesses.
license: MIT
metadata:
  category: email
  difficulty: intermediate
  time: "Setup 60 min · 30 leads ≈ 90 min · 3-week test"
  version: 1.0.0
  author: nvminhtu
---

# Google Maps Leads: Email Local Businesses That Need You

> A sheet of 30 qualified local businesses in one area, each with a contact taken from its own website and a reason
> to write that you saw yourself, plus a 3-email sequence and a rule for when to scale or switch area.

## Goal
Google Maps shows you every shop, salon, clinic and restaurant in an area, with its website and a picture of how it
runs (hours, booking link, photos, how it answers reviews). That makes it the best **finder** for selling to local
businesses. It is not a **database you may copy**: Google's terms forbid scraping and saving Maps content. So the
method is: find on Maps, qualify by eye, take the contact from the business's own site, and write one email that
proves you looked.

## When to use
- You sell to local businesses: a booking or ordering app, a website, a POS / check-in tool, a game or app they can
  white-label, marketing or design services.
- You can say which kind of business in which area: "nail salons in Austin, TX", "dental clinics in Manchester".
- You want 5–10 real conversations this month, not a mass mailing.
- **Not for:** consumers (people, not businesses) → [social-short-video](../../social/social-short-video/SKILL.md).
  Online businesses with no location (SaaS, Shopify stores) → [email-cold-outreach](../email-cold-outreach/SKILL.md).
  People who already gave you their email → [email-onboarding-sequence](../email-onboarding-sequence/SKILL.md).

## Inputs
- One sentence: what you sell and the result a business gets ("a booking page that fills empty chairs").
- One business type and one area. Start small: a district or a few zip codes, not a whole country.
- The country the businesses are in. It decides whether you may cold-email at all (table below).
- A separate sending domain with SPF, DKIM and DMARC, warmed up (step 2 of
  [email-cold-outreach](../email-cold-outreach/SKILL.md)).
- One proof point: a demo video, a screenshot, a result, or "free setup for the first 5 shops in {{area}}".
- The lead sheet from [assets/local-leads.csv](assets/local-leads.csv) (open it in Google Sheets or Excel).

## The rules (official sources)

**Google Maps.** You may look; you may not copy out.

| Rule | What it means here | Source |
|---|---|---|
| Google Maps (the app / website) | You may not copy the content, "mass download or create bulk feeds", or use Maps to build a business listings database or mailing list for a service that substitutes for Maps | [Google Maps / Earth Additional Terms](https://www.google.com/help/terms_maps/) (checked 2026-10-14, last modified 2026-01-27) |
| Google Maps Platform (the API) | §3.2.3(a) **No Scraping**: don't "export, extract, or otherwise scrape" Maps content, including "copy and save business names, addresses, or user reviews". §3.2.3(b): no caching except where allowed | [Google Maps Platform Terms](https://cloud.google.com/maps-platform/terms) (checked 2026-10-14) |
| Places API storage | Place IDs may be stored indefinitely; other Places content may not be pre-fetched, cached or stored beyond the stated exceptions | [Places API policies](https://developers.google.com/maps/documentation/places/web-service/policies) |
| Places API price | Website and phone fields are in the Text Search **Enterprise** SKU: 1,000 free calls a month, then $35 per 1,000 (US list price). No email field exists | [Pricing](https://developers.google.com/maps/billing-and-pricing/pricing) · [Data fields](https://developers.google.com/maps/documentation/places/web-service/data-fields) |

So in your sheet: store the **Maps link or place ID** to find the place again, and type everything else (name,
email, contact page) from the **business's own website**. Never paste reviews, ratings or addresses from Maps, and
never use a "Google Maps scraper" or extractor extension.

**Email law, by the country the business is in.** This skill is not legal advice.

| Country | Cold email to a business? | Source |
|---|---|---|
| US | Allowed without consent if: honest From and subject, says it's an ad, a postal address, an opt-out honored within 10 business days | [FTC CAN-SPAM guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business) |
| UK | Companies and LLPs: allowed with your identity and an opt-out. **Sole traders and partnerships** (many salons, cafés, trades) count as individuals: consent needed | [ICO: business-to-business marketing](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/) |
| EU | Each country has its own rule; several need consent even for business addresses. Check the country's regulator first | Country regulator |
| Vietnam | Decree 91/2020/NĐ-CP: an advertising email sent **without the recipient's prior consent** is spam; every ad email needs an opt-out at the end, in Vietnamese and English. **Don't cold-email.** Ask first in person, by phone or through a channel they opened for inquiries, and email only after a yes | [Decree 91/2020/NĐ-CP (VCCI)](https://vanban.vcci.com.vn/nghi-dinh-912020nd-cp-ve-chong-tin-nhan-rac-thu-dien-tu-rac-cuoc-goi-rac) |
| Other | Look up the country's anti-spam law before sending. Some allow addresses a business publishes, but only for offers related to that business's role | Country regulator |

## Steps
1. **Pick one niche + one area + one visible trigger (15 min).** The trigger is something you can see on the Maps
   profile or the website that says "they need this": no booking link, "call to book" only, no website, a site that
   isn't mobile-friendly, hours that don't match the site, reviews that ask for online ordering, owner never replies
   to reviews. Write it as: "{{type}} in {{area}} that {{trigger}}". If you can't name a trigger, pick another niche.
2. **Search Maps by hand (30 min for ~50 listings).** Search "{{type}} in {{area}}", then zoom street by street, and
   try 2–3 wordings ("nail salon", "nail bar", "manicure"). Open each listing and check the trigger. Only qualified
   ones go into the sheet: a Maps link or place ID, the area, and **your own note** on the trigger ("booking = phone
   only; 3 reviews mention waiting"). Your words, not copied review text.
3. **Get the contact from the business's site (60 min for 30).** Click through to the website. Take the email from
   its contact page or footer and paste the page URL in `contact_source_url`. Prefer role addresses (info@,
   bookings@, hello@) or the owner's work address if the site lists it. No email on the site? Use the site's contact
   form, call, or visit; never guess addresses (firstname@…) and never take emails from review profiles or social
   comments.
4. **Check the law for that country (5 min).** Use the table above. Mark each row `country_rule = ok / consent-first`.
   For `consent-first` rows (Vietnam, UK sole traders, many EU countries) your first touch is a call, a visit or a
   contact-form question asking whether they'd like to hear about it; email only after a yes, and record that yes.
5. **Write the sequence (30 min).** 3 emails, plain text, under 90 words, one link at most, in the business's
   language:
   - **Email 1:** what you noticed (the trigger, in your words) → what it costs them → one proof → a tiny ask
     ("Want a 1-minute video of how it'd look for {{business}}?").
   - **Email 2 (+4 days):** a local angle: a nearby type of business it helped, or a free setup slot this week.
   - **Email 3 (+7 days):** a polite close ("Should I stop writing?").
   Footer: your name, company, postal address and "Reply 'no' and I won't email again." Add the line required by the
   country (e.g. Vietnam: the opt-out in Vietnamese and English).
6. **Send slowly (ongoing).** About 10–20 new businesses a day from the warmed-up domain (a practitioner rule of
   thumb, not an official limit). Stop the sequence on any reply. Every "no" or bounce goes to `do_not_contact`
   for good.
7. **Score the area every week (15 min).** Per niche + area: qualified, sent, bounced, replied, positive, calls,
   customers. After ~50 sends with no positive reply, change the trigger or the offer before changing the area.
   A yes becomes a local case study ("how {{business}} filled its Tuesday chairs") you can use in the next street.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`. The AI plans and writes; you do the Maps
search and copy contacts from websites yourself.

````text
You are a local B2B outreach coach. You follow Google's terms: Google Maps is used only to find and look at
businesses by hand; nothing is scraped, bulk-exported or copied from Maps except a link or place ID, and contact
details come only from the business's own website. You never invent statistics; any benchmark is labelled
"rule of thumb".

What I sell: {{one sentence: product/service and the result for the business}}
Proof I have: {{demo link, result, screenshot, or "none yet"}}
Offer: {{price, free setup, trial}}
Business type: {{e.g. nail salons}}
Area: {{city / district / zip codes}}
Country: {{country}}
Language of the businesses: {{language}}

1. Tell me whether cold email to these businesses is allowed in {{country}} or needs consent first, with the official
   source link. If consent is needed, give me a short script for a phone call, a visit and a website contact form
   that asks permission to send details.
2. Give me 6 Google Maps search phrases for this type in this area (synonyms, local terms).
3. List 6 triggers I can see on a Maps profile or the business website that show they need what I sell, and for each,
   what to write in my notes (my own words, no copied review text).
4. Write a 3-email sequence in {{language}}: under 90 words each, plain text, 2-4 word lowercase subject lines, one
   ask per email, placeholders {{business}}, {{first_name}}, {{trigger_note}}, {{area}}. Add a footer that meets the
   rule for {{country}} (sender, postal address placeholder, opt-out).
5. Give me a weekly scorecard (qualified, sent, bounced, replied, positive, calls, customers) and the rule for when
   to change the trigger, the offer, or the area.
````

## Example output

> **Illustrative example.** Fictional product, businesses and numbers, shown for format.

*Chairfill*, a $29/month booking page with SMS reminders for salons. Niche + area: **nail salons in South Austin,
TX (78704, 78745) where booking is by phone only.** Country rule: US, CAN-SPAM → ok with footer and opt-out.

Lead sheet (3 of 30 rows):

| business | maps_link | website | contact_email | contact_source_url | trigger_note | country_rule | status |
|---|---|---|---|---|---|---|---|
| Lotus Nail Studio | maps.app.goo.gl/… | lotusnails.example | hello@lotusnails.example | lotusnails.example/contact | Booking = phone only; site not mobile-friendly | ok | sent-1 |
| Bluebonnet Nails | maps.app.goo.gl/… | bluebonnet.example | (form only) | bluebonnet.example/contact | No online booking; closed Mondays | ok | form-sent |
| Glow Bar 78745 | maps.app.goo.gl/… | — | — | — | No website | ok | visit |

```text
subject: booking at lotus

Hi Mai, I was looking at nail studios in 78704. Lotus looks great, but the only way to book is a phone call,
and your site is hard to use on a phone.
Chairfill gives you a booking page with text reminders, set up in a day. Want a 1-minute video of how it'd
look for Lotus?

Tu, Chairfill
Chairfill LLC, <postal address> · Reply "no" and I won't email again.
```

| Niche + area | Qualified | Sent | Bounced | Replied | Positive | Calls | Customers |
|---|---|---|---|---|---|---|---|
| Nail salons, 78704/78745, phone-only booking | 30 | 26 | 1 | 5 | 3 | 2 | 1 |
| Barbers, 78704, no website | 20 | 6 | 0 | 0 | 0 | 0 | 0 → visit instead |

## Common mistakes
- **Using a "Google Maps scraper" or extractor extension.** It breaks Google's terms, gives you stale and duplicate
  data, and the addresses it guesses bounce. Find on Maps, copy from the business's site.
- **Copying reviews or ratings into the sheet or the email.** Write what you noticed in your own words.
- **Mailing a whole city.** One niche, one area, one trigger. 30 good rows beat 3,000.
- **Cold-emailing where consent is required** (Vietnam, UK sole traders, many EU countries). Ask first by phone,
  visit or contact form; email after a yes.
- **Guessing emails** like owner@ or firstname@ from a name in a review. Use the contact the business published.
- **Sending from your main domain.** Use the separate, warmed-up one from email-cold-outreach.
- **"I can build you a website!" to everyone.** Lead with the one thing you saw on their profile.

## Related skills
- [email-cold-outreach](../email-cold-outreach/SKILL.md): sending domain, warm-up and sequence rules this skill reuses.
- [email-list-and-deliverability](../email-list-and-deliverability/SKILL.md): SPF, DKIM, DMARC and unsubscribe.
- [research-review-mining](../../research/research-review-mining/SKILL.md): find the pain worth opening with.
- [case-study-write-your-own](../../case-study/case-study-write-your-own/SKILL.md): turn the first local customer into proof.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources (checked 2026-10-14):
[Google Maps / Earth Additional Terms](https://www.google.com/help/terms_maps/),
[Google Maps Platform Terms](https://cloud.google.com/maps-platform/terms),
[Places API policies](https://developers.google.com/maps/documentation/places/web-service/policies),
[Google Maps Platform pricing](https://developers.google.com/maps/billing-and-pricing/pricing),
[Places data fields](https://developers.google.com/maps/documentation/places/web-service/data-fields),
[FTC CAN-SPAM guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business),
[ICO: business-to-business marketing](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/),
[Decree 91/2020/NĐ-CP](https://vanban.vcci.com.vn/nghi-dinh-912020nd-cp-ve-chong-tin-nhan-rac-thu-dien-tu-rac-cuoc-goi-rac).
