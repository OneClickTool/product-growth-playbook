# GA4 setup checklist

Copy this file into your own repo (e.g. `growth/analytics-setup.md`) and fill the last two columns.
Menu names are from the Google help pages below, checked **2026-10-19**. Google renames menus from time to time;
if a path doesn't match, open the linked help page.

| # | Setting | Where (Admin → …) | What to set | How to verify | Official source | Verified / date |
|---|---|---|---|---|---|---|
| 1 | Web data stream | Data collection and modification → Data streams → Add stream → Web | Main URL, stream name, enhanced measurement on | Stream shows a Measurement ID `G-…` | [Set up a web stream](https://support.google.com/analytics/answer/9304153) | |
| 2 | Google tag | (on your site) | One method: CMS field **or** snippet after `<head>` **or** Tag Manager | Realtime shows your visit (allow up to 30 min) | same as above | |
| 3 | Enhanced measurement | Data streams → your stream → Enhanced measurement (gear icon) | Keep on; turn off form interactions if another tool fires form events | `scroll` / `click` appear in Realtime | [Enhanced measurement events](https://support.google.com/analytics/answer/9216061) | |
| 4 | Internal traffic rule | Data streams → stream → Configure tag settings → Show more → Define internal traffic | `traffic_type = internal`, your IP or CIDR range | Rule listed | [Filter out internal traffic](https://support.google.com/analytics/answer/10104470) | |
| 5 | Internal traffic filter | Data collection and modification → Data filters | *Internal Traffic*, Exclude, **Testing** for 1 day → **Active** | Explore → dimension *Test data filter name* shows your visits | same as above (24–36 h to apply; max 10 filters) | |
| 6 | Cross-domain | Data streams → stream → Configure tag settings → Configure your domains | Every domain users move between | Destination URL has `_gl=` | [Cross-domain measurement](https://support.google.com/analytics/answer/10071811) | |
| 7 | Unwanted referrals | Data streams → stream → Configure tag settings → Show all → List unwanted referrals | Payment provider / login domains | Checkout returns don't show as Referral | [Unwanted referrals](https://support.google.com/analytics/answer/10327750) | |
| 8 | Data retention | Data collection and modification → Data retention | Event data: **14 months** (standard properties: 2 or 14) | Setting shows 14 months | [Data retention](https://support.google.com/analytics/answer/7667196) | |
| 9 | Consent mode | (your consent banner / CMP) | `analytics_storage` (+ ad types if you run ads); basic or advanced | Decline → no `_ga` cookie | [Consent mode](https://developers.google.com/tag-platform/security/concepts/consent-mode) | |
| 10 | Search Console link | Product links → Search Console links → Link | Search Console property + web stream (1 ↔ 1) | Link listed | [Connect Search Console](https://support.google.com/analytics/answer/10737381) | |
| 11 | Publish Search Console reports | Left menu → Library → Search Console collection → Publish | Publish (unpublished by default) | Reports → Search Console → Queries (after 48 h) | same as above | |
| 12 | DebugView | Data display → DebugView | Debug mode via Tag Assistant or `debug_mode: true` (accept cookies on the test device) | Events appear in the seconds stream with parameters | [DebugView](https://support.google.com/analytics/answer/7201382) | |
| 13 | Key events | Admin → Key events (or Events → mark as key event) | 1–3 events from your [tracking plan](../../analytics-tracking-plan/SKILL.md) | Key events column fills in reports | [About key events](https://support.google.com/analytics/answer/13965727) | |

## Limits worth knowing (standard GA4 property)

From [event collection limits](https://support.google.com/analytics/answer/9267744) and
[custom dimensions and metrics](https://support.google.com/analytics/answer/10075209), checked 2026-10-19:

| Item | Limit |
|---|---|
| Event name length | 40 characters |
| Parameter name length | 40 characters |
| Parameter value length | 100 characters (`page_title` 300, `page_referrer` 420, `page_location` 1,000) |
| Parameters per event | 25 |
| User properties | 25 per property |
| Event-scoped custom dimensions | 50 |
| User-scoped custom dimensions | 25 |
| Item-scoped custom dimensions | 10 |
| Custom metrics | 50 |
| Key events | 30 ([GA4 limits](https://support.google.com/analytics/answer/11202874)) |
| Audiences | 100 (same page) |
| Data filters | 10 per property ([internal traffic](https://support.google.com/analytics/answer/10104470)) |
| Cross-domain conditions | 100 ([cross-domain](https://support.google.com/analytics/answer/10071811)) |
| Unwanted referral conditions | 50 per data stream ([unwanted referrals](https://support.google.com/analytics/answer/10327750)) |

## Waiting times (so you don't judge too early)

| What | Delay | Source |
|---|---|---|
| First data after adding the tag | up to 30 minutes | [web stream help](https://support.google.com/analytics/answer/9304153) |
| A new data filter taking effect | 24–36 hours | [internal traffic help](https://support.google.com/analytics/answer/10104470) |
| Search Console data in GA4 | 48 hours after Search Console collects it | [Search Console link help](https://support.google.com/analytics/answer/10737381) |
| Search Console's own reports | 2–3 days for collected data | [Search Console data help](https://support.google.com/webmasters/answer/96568) |

## Numbers look wrong? Check in this order

1. **Tag missing or doubled.** View the page source on 3 templates (home, article, checkout) and count the `G-` IDs.
2. **Consent.** Low numbers mostly from EEA / UK visitors → check consent defaults with Tag Assistant.
3. **Your own traffic.** Filter still in Testing, or your IP changed.
4. **Self-referrals.** Your checkout or payment domain in Referral → cross-domain missing, or add it to *List
   unwanted referrals*.
5. **Thresholding.** A card shows "Google Analytics has applied thresholding" → widen the date range or drop
   demographic dimensions ([data thresholds](https://support.google.com/analytics/answer/9383630)).
