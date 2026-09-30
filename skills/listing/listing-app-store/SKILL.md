---
name: listing-app-store
description: Step-by-step App Store listing in App Store Connect, in three levels (1 get approved, 2 optimize, 3 advanced) with a fill-in listing sheet covering every field, character limit, screenshot size and review requirement. Use when publishing an iPhone, iPad or Mac app for the first time, preparing a version update, fixing a rejected submission, or when someone asks "how do I list my app on the App Store", "App Store Connect step by step", "what do I need to submit to Apple", or "App Store listing checklist".
license: MIT
metadata:
  category: listing
  difficulty: beginner → advanced (3 levels)
  time: "Level 1: 2-3 h · Level 2: 1-2 h · Level 3: ongoing"
  version: 1.0.0
  author: nvminhtu
---

# App Store Listing

> Fill one listing sheet, then paste it into App Store Connect in the right order. Level 1 gets you approved,
> Level 2 gets you found, Level 3 is for when the app is already growing.

## Goal
A complete, approved App Store listing with no last-minute surprises: every field prepared in advance, within
limits, and consistent with the app.

## When to use
- First submission of an iPhone, iPad or Mac app.
- A new version with listing changes.
- A rejection that mentions metadata, privacy or subscriptions.
- **Not for:** choosing keywords → [aso-keyword-research](../../aso/aso-keyword-research/SKILL.md).
  Writing the name and subtitle → [aso-title-subtitle-optimization](../../aso/aso-title-subtitle-optimization/SKILL.md).

## Inputs
- An Apple Developer Program membership and a signed build uploaded (Xcode → Archive → Distribute, or Transporter).
- A privacy policy URL and a support URL that open in a browser.
- `assets/app-store-listing-sheet.md` from this skill, copied into your project and filled in.

## Levels at a glance

| Level | Goal | You do | Time |
|---|---|---|---|
| **1. Get approved** | Live on the App Store | Every required field, privacy, age rating, review notes | 2–3 h |
| **2. Get found** | Rank and convert | Keywords, screenshots with captions, preview video, localizations | 1–2 h |
| **3. Grow** | Test and target | Product page tests, custom product pages, in-app events, offer codes | ongoing |

## Steps

### Level 1: Get approved (required)
Fill the listing sheet first, then enter it in this order in [App Store Connect](https://appstoreconnect.apple.com/):

1. **Create the app record.** *Apps → + → New App*: platform, **name (30 chars)**, primary language, bundle ID,
   SKU (any internal ID). The name must be unique on the store.
2. **App Information.** Subtitle (30), primary and secondary category, content rights (do you use third-party content?).
3. **Age rating.** Answer the questionnaire honestly. Apple's ratings are now 4+, 9+, 13+, 16+ and 18+, and the
   questions include in-app controls, user-generated content, medical/wellness and social media features.
   An update is blocked until the current questionnaire is answered.
4. **Pricing and Availability.** Price (or Free) and countries. For in-app purchases and subscriptions, create
   them under *Monetization* and add them to the version for review.
5. **App Privacy.** Privacy policy URL and the "nutrition label": every data type your app **and its SDKs**
   (analytics, crash reporting, ads, payments) collect, whether it's linked to the user, and whether it's used for tracking.
   Check each SDK's documentation. A label that doesn't match the SDKs you ship is a common rejection.
6. **Version page (the listing).**
   - Screenshots: **iPhone 6.9"** (1320 × 2868 portrait) is required. Add **iPad 13"** (2064 × 2752) if the app
     runs on iPad. Apple scales them down for smaller devices. Up to 10 per size.
   - Promotional text (170, can change anytime without review), description (4,000), **keywords (100 bytes**,
     comma-separated, no spaces. Accented letters and non-Latin scripts use more than one byte each).
   - Support URL (required), marketing URL (optional), copyright ("2026 Your Name").
7. **Build and export compliance.** Select the build. Answer the encryption question. Most apps that only use HTTPS
   qualify for the exemption, and you can set `ITSAppUsesNonExemptEncryption` in Info.plist to skip the question on
   later builds.
8. **App Review information.** Contact details, a **demo account** if there's a login, and notes that explain
   anything non-obvious: where the paywall is, how to reach a feature, why you need a permission.
9. **Release option.** Manual, automatic, or scheduled. For a first launch, choose *manual* so you control the day.
10. **Submit for review.** Most reviews finish within a day or two. Leave time for one rejection round.

### Level 2: Get found (after the first approval)
1. **Keywords:** run [aso-keyword-research](../../aso/aso-keyword-research/SKILL.md). Don't repeat words already in the name or subtitle.
2. **Name + subtitle:** [aso-title-subtitle-optimization](../../aso/aso-title-subtitle-optimization/SKILL.md).
3. **Screenshots with captions** and an optional app preview (15–30 s): [aso-screenshot-strategy](../../aso/aso-screenshot-strategy/SKILL.md).
4. **Localizations.** Add the languages of your top markets. Each localization has its own name, subtitle, keywords and
   screenshots, so it's extra keyword space as well as better conversion.
5. **"What's New"** on every update. Say what users will notice, not "bug fixes".
6. **Ratings:** [aso-review-and-rating-strategy](../../aso/aso-review-and-rating-strategy/SKILL.md).

### Level 3: Grow (once you have steady traffic)
- **Product Page Optimization:** A/B test icon, screenshots and preview against up to 3 treatments.
- **Custom product pages:** up to 70 variants with their own screenshots, promo text and deep link. Point ads and
  links at them, and assign keywords so a matching page can appear in organic search.
- **In-App Events:** time-limited events shown on your page and in search.
- **Offer codes** for subscriptions and in-app purchases. Apple is phasing out the old promo codes.
- **Phased release** for updates (rolls out over 7 days, can pause), and **pre-orders** for a new app.
- **Featuring nominations** in App Store Connect: tell Apple's editors about a launch or a big update.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are an App Store Connect expert. Fill my App Store listing sheet (Level 1 + Level 2).

App: {{what it does, who for}}   Platforms: {{iPhone / iPad / Mac}}   Price model: {{free / paid / subscription}}
Brand: {{name}}   Primary language + main markets: {{...}}
Target keywords (if researched): {{...}}
SDKs in the app: {{analytics, crash, ads, payments, login...}}
Login required? {{yes/no}}   User-generated content / social features? {{yes/no}}

Output the sheet with these fields and a character count for each:
name (≤30), subtitle (≤30), primary/secondary category, keywords (≤100 bytes, comma-separated, no spaces,
no words repeated from name/subtitle), promotional text (≤170), description (≤4000, first 3 lines matter most),
What's New, support URL / marketing URL placeholders.
Then: a draft App Privacy table (data type | collected by which SDK | linked to user? | tracking?),
flagging anything I must verify in each SDK's docs; the likely age-rating answers with the reason for each;
and App Review notes (demo account placeholder, where the paywall is, why each permission is needed).
Never invent facts about my app. Mark unknowns as TODO.
````

## Example output

> **Illustrative example.** Fictional app, shown for format.

```text
Name (23/30):      Sipwell: Water Reminder
Subtitle (29/30):  Drink Tracker & Hydration Log
Keywords (98/100): daily,intake,hydrate,bottle,cup,goal,health,alert,ounce,ml,fluid,sip,office,work,body,thirst,glass
Promo (61/170):    New: reminders that pause during your calendar meetings.
Category:          Health & Fitness / Productivity
Privacy:           Crash data (Crashlytics, not linked, no tracking) · Purchases (RevenueCat, linked, no tracking)
Age rating:        4+ (no UGC, no web access, no medical claims)
Review notes:      No login. Paywall: Settings → Sipwell Pro. Notifications are used only for reminders.
```

## Common mistakes
- **Privacy label doesn't match the SDKs.** Review checks what your SDKs actually collect.
- **No demo account** for an app with login, which means an instant rejection.
- **Subscription screen without price, period, Terms and Privacy links** → [monetization-paywall-design](../../monetization/monetization-paywall-design/SKILL.md).
- **Keywords with spaces, repeats or competitor names.** You waste bytes and risk a rejection.
- **Screenshots that aren't the real app,** or that show another platform's device.

## Related skills
- [listing-google-play](../listing-google-play/SKILL.md): the same flow for Android.
- [listing-free-directories](../listing-free-directories/SKILL.md): free places to list the app after launch.
- [launch-pre-launch-checklist](../../launch/launch-pre-launch-checklist/SKILL.md): schedule review time before launch day.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: [App Store Connect Help](https://developer.apple.com/help/app-store-connect/),
[App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/),
Apple Developer News on [updated age ratings](https://developer.apple.com/news/?id=ks775ehf) and
[submission and marketing enhancements](https://developer.apple.com/news/?id=gf6mgrs6). Limits change, so check them before each submission.
