---
name: analytics-tracking-plan
description: Write a one-page GA4 tracking plan for a website, landing page or web app - 5 to 8 events with GA4 recommended names, which 1 to 3 are key events, parameter names, the custom dimensions to register, one UTM convention shared by every channel, and a test checklist (Realtime + DebugView). Use when someone asks "which events should I track", "what should be a key event", "GA4 conversions", "tracking plan", "event naming", "how to use UTM", "UTM convention", "my traffic shows as Unassigned", "store button clicks in GA4", "track sign-ups / leads / downloads", or is about to add analytics code and wants to avoid tracking 50 things nobody reads.
license: MIT
metadata:
  category: analytics
  difficulty: beginner
  time: 45-60 min
  version: 1.0.0
  author: nvminhtu
---

# Tracking Plan: 5–8 events and one UTM rule

> In under an hour you'll have one page that says exactly what GA4 records, which actions count as success, and how
> every link you post is tagged, so every later report answers "what worked?".

## Goal
Most sites either track nothing beyond page views or track everything and read none of it. A tracking plan picks
the few actions that mean "this visit was worth it" (key events), names them the way GA4 expects, and makes every
channel tag its links the same way. Without it, the [weekly reports](../analytics-ga4-reports-101/SKILL.md) can't
say which channel or page brings results.

## When to use
- Right after [analytics-ga4-setup](../analytics-ga4-setup/SKILL.md), before writing any event code.
- GA4 works but the *Key events* column is empty or full of noise.
- Traffic from your posts lands in **Unassigned** or **Direct**.
- You post on several channels (X, Reddit, Instagram, email…) and can't tell which one sends sign-ups.
- **Not for:** mobile app events (Firebase → [launch-growth-stack-setup](../../launch/launch-growth-stack-setup/SKILL.md));
  store install attribution (App Store Connect / Play Console campaign links).

## Inputs
- A working GA4 property ([analytics-ga4-setup](../analytics-ga4-setup/SKILL.md)).
- The **one action** that means a visit succeeded: sign-up, lead form, store button click, download, purchase.
- The list of channels where you post links.
- Someone who can add code or Tag Manager tags to the site (you, a developer, or the CMS).

## Steps
1. **Start from what GA4 already collects (5 min).** Enhanced measurement gives you `page_view`, `scroll`, outbound
   `click`, `file_download`, `form_start`, `form_submit`, site search and video events
   ([list](https://support.google.com/analytics/answer/9216061)). Don't rebuild these.
2. **Pick 5–8 events, using recommended names first (15 min).** GA4 has recommended event names such as
   `sign_up`, `login`, `generate_lead`, `purchase`, `begin_checkout`, `share`, `search`, `select_content`
   ([recommended events](https://support.google.com/analytics/answer/9267735)). Use them when they fit; reports and
   integrations understand them. Make your own name only when nothing fits (e.g. `store_click`). Names: lowercase,
   underscores, ≤ 40 characters, no spaces ([limits](https://support.google.com/analytics/answer/9267744)).
3. **Mark 1–3 key events (5 min).** A key event is "the visit did the thing" — not page views, not scrolls. Typical:
   one primary (`sign_up`, `generate_lead`, `purchase` or `store_click`) and at most two secondary. Mark them in
   Admin → **Key events** ([help](https://support.google.com/analytics/answer/13965727)). Standard properties allow
   30 key events ([limits](https://support.google.com/analytics/answer/11202874)); more than 3 makes every channel
   look good. Pick the primary one by product type:

   | Product | Primary key event | Secondary (optional) |
   |---|---|---|
   | App with a website (iOS / Android / Mac) | `store_click` (store badge) | `generate_lead` (email) |
   | SaaS / web app | `sign_up` | `begin_checkout`, `purchase` |
   | Browser extension | `store_click` (Chrome Web Store / Firefox Add-ons) | `generate_lead` |
   | Download, template, ebook | `file_download` or `purchase` | `generate_lead` |
   | Not built yet (waitlist) | `generate_lead` | — |
4. **Add 1–3 parameters per event, and register the ones you'll filter by (10 min).** E.g. `store_click` with
   `store` (`app_store` / `google_play` / `chrome`) and `placement` (`hero` / `footer`). A parameter is only usable in
   reports after you register it as a **custom dimension** (Admin → Custom definitions;
   [limits](https://support.google.com/analytics/answer/10075209)). Never send emails, names or other personal data
   as parameters.
5. **Adopt one UTM convention (10 min).** Use the table in [references/utm-convention.md](references/utm-convention.md):
   `utm_source` = the site (`x`, `reddit`, `newsletter`), `utm_medium` = the placement, `utm_campaign` = what you
   promote, lowercase, no spaces. Read the "Unassigned" note there: GA4's default channel rules look at
   `utm_medium` values like `social`, `email`, `referral`, `organic`
   ([channel rules](https://support.google.com/analytics/answer/9756891)), so decide once how your mediums map to
   channels.
6. **Fill the plan (10 min).** Copy [assets/tracking-plan.md](assets/tracking-plan.md) into your repo
   (e.g. `growth/tracking-plan.md`) and fill one row per event.
7. **Test every row before you call it done (10 min).** Trigger each event yourself; it shows in Realtime → *Event
   count by event name* and in Admin → **DebugView** (DebugView needs debug mode: the Google Tag Assistant browser
   extension or `debug_mode` in the tag). Tick *Tested* only when you've seen it, with its parameters.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are a GA4 tracking-plan writer. My product: {{what it is, one line}}. Site: {{url}}.
The one action that means a visit succeeded: {{sign-up / lead form / store button click / download / purchase}}.
Other actions I care about: {{list or "none"}}. Channels where I post links: {{x, reddit, instagram, newsletter, ...}}.
How events get added: {{gtag code / Tag Manager / CMS plugin}}.

Write a one-page tracking plan:
1. A table: event name | trigger (exact user action) | parameters (max 3) | key event? | custom dimension to register | tested?
   - At most 8 events. Use GA4 recommended event names (sign_up, generate_lead, purchase, ...) when they fit.
   - Do not re-add events enhanced measurement already collects (page_view, scroll, click, file_download, form_*).
   - Mark 1 to 3 key events and say why each one means success.
   - Names: lowercase_with_underscores, max 40 characters. No personal data in parameters.
2. A UTM table for my channels: channel | utm_source | utm_medium | example link. Lowercase, no spaces.
   Say which GA4 default channel each medium lands in, and flag any that would land in "Unassigned".
3. The code or Tag Manager steps for each custom event.
4. A test checklist (Realtime + DebugView) I can tick.
If you're not sure about a GA4 limit or rule, say so and link the official Google help page; don't guess.
````

**Agent mode.** With the Google Analytics MCP server, an agent can check the plan against the property, read-only:
`get_custom_dimensions_and_metrics` (are the parameters registered?), `run_report` with dimensions `eventName`,
`isKeyEvent` and metric `eventCount` for the last 7 days (does each event fire, is it marked?), and
`run_report` by `sessionSourceMedium` × `sessionDefaultChannelGroup` (do tagged links land in *Unassigned*?). It
reports gaps; the user changes the property.

## Example output

> **Illustrative example.** A made-up habit-tracker landing page, to show the format.

| Event | Trigger | Parameters | Key event? | Custom dimension | Tested |
|---|---|---|---|---|---|
| `store_click` | Click on App Store / Google Play badge | `store`, `placement` | ✅ primary | `store`, `placement` (event) | ✅ 10-19 |
| `generate_lead` | Waitlist form sent successfully | `form_id` | ✅ secondary | `form_id` (event) | ✅ 10-19 |
| `select_content` | Click on a feature tab | `content_type`, `item_id` | — | — | ✅ 10-19 |
| `video_start` | (enhanced measurement, YouTube demo) | — | — | — | ✅ 10-19 |
| `share` | Click on "share" button | `method` | — | `method` (event) | ⏳ |

UTM for this product: `?utm_source=reddit&utm_medium=social&utm_campaign=habit-launch&utm_content=comment`
(placement kept in `utm_content`, so GA4 files it under Organic Social).

## Common mistakes
- **Making `page_view` or `scroll` a key event.** Every visit "converts" and the number means nothing.
- **Inventing names for standard actions** (`signup_done`, `Lead`). Use `sign_up`, `generate_lead`.
- **Sending parameters you never registered.** They are collected but you can't filter or break down by them in
  standard reports until you add the custom dimension. Register them the day you add the event.
- **Ten key events.** Every channel then "converts". Keep 1–3, and keep the primary one fixed for months.
- **UTM tags on your own menu or footer links.** They start a new session from your own site and hide the real
  source. Tag only links that live *outside* your site.
- **Mixed-case or spaced UTMs** (`Reddit`, `reddit `, `r/`). GA4 shows them as separate sources. Pick one spelling.
- **Changing UTMs on links you already posted.** Old links keep the old values. Change the convention for new links
  only and note the date.
- **Calling the plan done without DebugView.** "I added the code" isn't "the event arrives with its parameters".

## Related skills
- [analytics-ga4-setup](../analytics-ga4-setup/SKILL.md): do this first.
- [analytics-ga4-reports-101](../analytics-ga4-reports-101/SKILL.md): read your key events by channel and page.
- [growth/action/01-measure-first.md](../../growth/action/01-measure-first.md): one tracked link per channel.
- Channel kits keep their own link tags in `07-metrics-and-stop-rules.md` (e.g.
  [X](../../../marketing/x-marketing/docs/07-metrics-and-stop-rules.md)); the
  [UTM convention](references/utm-convention.md) explains how they show up in GA4.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: Google Analytics Help (recommended events, enhanced
measurement, key events, event limits, custom dimensions, default channel group), linked inline (checked 2026-10-19).
