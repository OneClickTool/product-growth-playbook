---
name: analytics-ga4-setup
description: Set up a Google Analytics 4 (GA4) property right, once, for a website, landing page, blog or web app, and verify every setting works. Covers the web data stream and Google tag, enhanced measurement, the internal-traffic filter, cross-domain (site + checkout or app domain), data retention, consent mode, the Search Console link (Queries and organic traffic reports) and a check in Realtime and DebugView. Ends with a "verified" checklist. Use when someone says "GA4 setup", "install Google Analytics", "set up Google Analytics 4 for my site", "connect Search Console to GA4", "GA4 shows no data", "my own visits are counted", "exclude internal traffic", "cross-domain tracking", "data retention 14 months", "consent mode", or has GA4 installed but never checked it is correct.
license: MIT
metadata:
  category: analytics
  difficulty: beginner
  time: 60-90 min (filters and the Search Console data take 1-2 days to show)
  version: 1.0.0
  author: nvminhtu
---

# GA4 Setup: a property you can trust

> In about an hour you'll have a GA4 property that counts real visitors (not you), keeps 14 months of data for
> explorations, shows Google search queries next to your pages, and has been checked in Realtime.

## Goal
Every later analytics skill reads numbers from this property. If your own visits are counted, data expires after
2 months, or Search Console isn't linked, every report after that is wrong or missing. This skill sets up the few
settings that matter and **verifies** each one, because "the tag is on the page" and "the data is right" are
different things.

## When to use
- You have a website, landing page, blog, docs site or web app and no GA4 yet.
- GA4 is installed but you've never checked the settings (most common case).
- Numbers look odd: traffic on days nobody visited, your own country at the top, a checkout domain showing as a
  referral.
- **Not for:** mobile apps (Firebase Analytics → [launch-growth-stack-setup](../../launch/launch-growth-stack-setup/SKILL.md)).
  Choosing which events to track → [analytics-tracking-plan](../analytics-tracking-plan/SKILL.md) (do it right after
  this one).

## Inputs
- Edit access to the site (theme, CMS settings, or the HTML `<head>`), or a Google Tag Manager container on it.
- A Google account with the **Editor** role (or higher) on the GA4 property. Linking Search Console also needs you
  to be a verified owner of the Search Console property ([help](https://support.google.com/analytics/answer/10737381)).
- The domains you own: main site, and any second domain users pass through (checkout, app, docs).
- Your office or home IP address (search "what is my IP") for the internal-traffic rule.
- Whether you have visitors in places that require consent (EU/EEA, UK…). If unsure, plan for a consent banner.

## Steps

The full click path for each setting, with the official link, is in
[references/setup-checklist.md](references/setup-checklist.md). Short version:

1. **Create the property and a web data stream (10 min).** Admin → *Data collection and modification* → Data
   streams → Add stream → Web. Enter the main URL, keep **enhanced measurement on**, create
   ([help](https://support.google.com/analytics/answer/9304153)). Copy the Measurement ID (`G-XXXXXXX`).
   *Check:* the stream shows your URL and a Measurement ID.
2. **Add the Google tag to every page (10 min).** CMS/site builder: paste the Measurement ID into its Google
   Analytics field. Custom site: paste the snippet right after `<head>` on every page, or use Tag Manager. One method
   only: two tags double-count page views.
   *Check:* open your site in a private window, then Reports → **Realtime** shows you within a few minutes (Google
   says collection can take up to 30 minutes to start).
3. **Review enhanced measurement (5 min).** It collects `page_view`, `scroll`, outbound `click`,
   `view_search_results`, `video_start` / `video_progress` / `video_complete`, `file_download`, `form_start` and
   `form_submit` ([help](https://support.google.com/analytics/answer/9216061)). Turn **off** form interactions if
   your forms are handled by a third-party script that fires its own events (otherwise you count twice).
   Single-page app (React, Vue, Next client routing)? Keep *page changes based on browser history events* on in the
   page views setting, or route changes won't count as page views.
   *Check:* scroll to the bottom of a page; `scroll` appears in Realtime → Event count by event name.
4. **Exclude your own visits (10 min).** Stream → Configure tag settings → Show more → **Define internal traffic** →
   rule with your IP (`traffic_type = internal`). Then Admin → **Data filters** → the *Internal Traffic* filter →
   leave it in **Testing** for a day, check, then switch to **Active**
   ([help](https://support.google.com/analytics/answer/10104470)). Active filters are permanent: excluded data is
   never processed. Filters take 24–36 hours to apply.
   *Check:* in Explore, the dimension *Test data filter name* shows your visits as matching before you activate.
5. **Cross-domain, only if users move between your domains (5 min).** Configure tag settings → **Configure your
   domains** → add each domain (e.g. `example.com`, `checkout.example-pay.com`). Also add your payment provider
   under *List unwanted referrals* so a return from checkout doesn't start a new "referral" session.
   *Check:* click from site to the second domain; the URL carries a `_gl=` parameter.
6. **Data retention to 14 months (1 min).** Admin → Data collection and modification → **Data retention** → Event
   data retention: **14 months** (the other option for standard properties is 2 months)
   ([help](https://support.google.com/analytics/answer/7667196)). It only affects explorations and funnel reports;
   standard reports are not cut. Do it on day 1, before you need to compare this quarter with the last one.
7. **Consent mode, if you need a banner (15–30 min).** Use a consent banner (CMP) that supports Google consent
   mode, and make sure it sets `analytics_storage` (and `ad_storage`, `ad_user_data`, `ad_personalization` if you
   run ads). *Basic* blocks tags until the visitor chooses; *advanced* loads tags with consent denied and sends
   cookieless pings until consent is granted
   ([consent mode](https://developers.google.com/tag-platform/security/concepts/consent-mode)). Consent mode v2
   needs all four signals ([consent guide](https://developers.google.com/tag-platform/security/guides/consent)).
   Ask a lawyer which
   one your region needs; this skill doesn't give legal advice.
   *Check:* decline the banner in a private window; no `_ga` cookie is set (DevTools → Application → Cookies).
8. **Link Search Console (10 min).** If the site isn't verified yet, add it at
   [search.google.com/search-console](https://search.google.com/search-console) (a **Domain** property covers
   `www`, non-`www` and subdomains). Then GA4 Admin → *Product links* → **Search Console links** → Link → pick the
   property and the web stream. One stream links to one Search Console property. Then open **Library** in the left
   menu and **publish the Search Console collection**: it is unpublished by default
   ([help](https://support.google.com/analytics/answer/10737381)).
   *Check:* after 48 hours, Reports → Search Console → *Queries* shows rows (Search Console keeps 16 months).
9. **Verify events in DebugView (15 min).** Turn on debug mode with [Tag Assistant](https://tagassistant.google.com)
   (it adds a parameter to your URL) or `gtag('config', 'G-XXXXXXX', { 'debug_mode': true })` on a test build.
   Remove the parameter to turn it off; setting it to `false` doesn't
   ([DebugView](https://support.google.com/analytics/answer/7201382)). Admin → **DebugView**: load a page, scroll to
   the bottom, click an outbound link, send a form. Each event should appear in the seconds stream with its
   parameters. **Accept analytics cookies on your test device first**: with consent mode and consent declined, your
   events won't show in DebugView.
10. **Write down what you set, and a baseline.** Copy the checklist in
    [references/setup-checklist.md](references/setup-checklist.md) into your repo (e.g. `growth/analytics-setup.md`)
    with the date and who did it. After 48 hours, add the last 28 days (or "unknown, started today"): sessions by
    channel, engaged sessions, top 10 landing pages. That's week 0. Next: build the
    [tracking plan](../analytics-tracking-plan/SKILL.md).

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are a careful Google Analytics 4 setup checker. My site: {{url}}. Built with: {{CMS / framework / Tag Manager}}.
Other domains users pass through: {{checkout or app domains, or "none"}}. Visitors from EU/EEA/UK: {{yes / no / unsure}}.
What I already did: {{paste what you see in GA4 Admin, or "nothing yet"}}.

Walk me through GA4 setup one step at a time, in this order: web data stream + Google tag, enhanced measurement,
internal-traffic rule + data filter (Testing first, then Active), cross-domain and unwanted referrals (only if I have
other domains), data retention 14 months, consent mode (only if needed; no legal advice), Search Console link and
publishing the Search Console collection in Library.

For each step: give the exact Admin menu path, what to enter for my site, and ONE check I can do to prove it works
(Realtime, DebugView, a cookie, a URL parameter). Wait for me to say "done" before the next step.
Rules: never invent numbers or settings you can't see; if a Google limit or default matters, link the official
Google help page instead of guessing. At the end, print a checklist table: setting | value | verified (yes/no) | date.
````

**Agent mode.** An agent with the Google Analytics MCP server may *read* the property to audit it
(`get_account_summaries`, `get_property_details`, `run_realtime_report`) and report what's missing. It never
changes settings, filters or links itself: it lists the change and the user makes it in GA4 Admin.

## Example output

> **Illustrative example.** The site and values are made up to show the format.

| Setting | Value | Verified | Date |
|---|---|---|---|
| Web stream + tag | `example-site.com`, tag via CMS field, one tag only | ✅ Realtime shows 1 user (me) | 2026-10-19 |
| Enhanced measurement | On; form interactions off (newsletter tool sends its own event) | ✅ `scroll` in Realtime | 2026-10-19 |
| Internal traffic | Rule `office`, IP `203.0.113.0/24`; filter **Testing** | ⏳ switch to Active on 10-20 | 2026-10-19 |
| Cross-domain | Not needed (no second domain); payment provider in unwanted referrals | ✅ | 2026-10-19 |
| Data retention | 14 months | ✅ | 2026-10-19 |
| Consent mode | Basic, via CMP; `analytics_storage` denied until accepted | ✅ no `_ga` cookie after decline | 2026-10-19 |
| Search Console | Domain property linked to web stream; collection published | ⏳ Queries report empty until 10-21 (48 h) | 2026-10-19 |

## Common mistakes
- **Two tags on the page** (CMS plugin + hand-pasted snippet). Page views double and engagement looks too good.
  Keep one.
- **Activating the internal filter without testing.** Active filters drop data forever. Use Testing for a day first.
- **Leaving retention at 2 months.** Explorations older than that come back empty, and the setting isn't
  retroactive.
- **Linking Search Console but not publishing the collection.** The link works, but you never see the reports.
- **Reading data the same day.** Filters take 24–36 hours, Search Console data 48 hours. Wait before you judge.
- **Copying a consent setup from a blog post.** Rules differ by region; check with someone qualified.
- **Debugging with analytics cookies declined**, then deciding "events don't fire". Accept on the test device.
- **Your own checkout showing as Referral.** Cross-domain is missing, or the payment provider isn't in *List
  unwanted referrals*.

## Related skills
- [analytics-tracking-plan](../analytics-tracking-plan/SKILL.md): next step — which events and key events to track,
  and one UTM convention for every channel.
- [analytics-ga4-reports-101](../analytics-ga4-reports-101/SKILL.md): learn to read the reports once data arrives.
- [launch-geo-aeo-feature-preview](../../launch/launch-geo-aeo-feature-preview/SKILL.md): adds an "AI assistants"
  channel group on top of this setup.
- [launch-growth-stack-setup](../../launch/launch-growth-stack-setup/SKILL.md): the same job for mobile apps
  (Firebase).

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: Google Analytics Help and Google Tag Platform docs,
linked inline and in [references/setup-checklist.md](references/setup-checklist.md) (checked 2026-10-19).
