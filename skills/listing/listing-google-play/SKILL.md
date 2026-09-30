---
name: listing-google-play
description: Step-by-step Google Play listing in Play Console, in three levels (1 get approved, 2 optimize, 3 advanced) with a fill-in listing sheet covering app content declarations, Data safety, graphics sizes, the closed-testing requirement for new personal accounts, and release steps. Use when publishing an Android app for the first time, preparing an update, fixing a policy rejection, or when someone asks "how do I publish on Google Play", "Play Console step by step", "12 testers 14 days", or "Google Play listing checklist".
license: MIT
metadata:
  category: listing
  difficulty: beginner → advanced (3 levels)
  time: "Level 1: 2-3 h + 14-day test · Level 2: 1-2 h · Level 3: ongoing"
  version: 1.0.0
  author: nvminhtu
---

# Google Play Listing

> Fill one listing sheet, finish the *App content* declarations, run the required test, then release.
> Level 1 gets you live, Level 2 gets you found, Level 3 is for when the app is already growing.

## Goal
A complete, approved Google Play listing, with the long-lead items (closed testing, declarations) started early
enough that they don't delay the launch.

## When to use
- First Android release, or a new developer account.
- An update with listing changes.
- A policy rejection (Data safety, permissions, metadata).
- **Not for:** keyword and copy strategy → [aso-keyword-research](../../aso/aso-keyword-research/SKILL.md).

## Inputs
- A Google Play developer account (one-time registration fee, plus identity verification).
- A signed Android App Bundle (`.aab`).
- A privacy policy URL, a support email, and `assets/google-play-listing-sheet.md` filled in.

## Levels at a glance

| Level | Goal | You do | Time |
|---|---|---|---|
| **1. Get approved** | Live in production | App content declarations, store listing, closed test, release | 2–3 h + 14 days of testing |
| **2. Get found** | Rank and convert | Keyword-rich description, screenshots, localized listings, experiments | 1–2 h |
| **3. Grow** | Target and engage | Custom store listings, promotional content, pre-registration | ongoing |

## Steps

### Level 1: Get approved (required)
1. **Create the app.** In [Play Console](https://play.google.com/console/): *Create app* → name, default language,
   app or game, free or paid. **Free → paid can't be changed later.**
2. **Start testing early (long lead!).** New **personal** developer accounts must run a **closed test with at least
   12 testers opted in for 14 continuous days** before applying for production access. Upload a build to *Closed testing*,
   invite testers (an email list or Google Group), and start the clock on day one. Organization accounts are exempt.
3. **App content (Policy → App content).** Complete every declaration:
   privacy policy · app access (login instructions or a demo account for reviewers) · ads (does the app show ads?) ·
   content rating (IARC questionnaire) · target audience and content · **Data safety** (what the app **and its SDKs**
   collect or share, and why) · plus any that apply: news, health, financial features, government apps.
4. **Store listing (Grow → Store presence → Main store listing).**
   - App name (30), short description (80), full description (4,000).
   - App icon **512 × 512** PNG · feature graphic **1024 × 500** · phone screenshots **2–8** (add tablet screenshots if you
     support tablets) · optional YouTube promo video.
   - Category, tags, contact email (required), website and phone (optional).
5. **Pricing and countries.** Choose the countries. Set up in-app products and subscriptions under *Monetize*.
6. **Release.** After the closed-test requirement is met, apply for production access, answer the questions about your
   test, then create a **production release**: upload the `.aab`, write release notes, and use a **staged rollout**
   (e.g. 20% → 50% → 100%) while you watch crashes and ANRs.

### Level 2: Get found
1. **Title and short description** carry your main keywords: [aso-title-subtitle-optimization](../../aso/aso-title-subtitle-optimization/SKILL.md).
2. **Full description is indexed.** Use each target phrase 2–4 times, naturally. No keyword lists, no fake reviews,
   no "#1 / best / free" claims (Google Play Metadata policy).
3. **Screenshots with captions** and a strong feature graphic: [aso-screenshot-strategy](../../aso/aso-screenshot-strategy/SKILL.md).
4. **Translations** of the listing for your top markets (Store presence → translations).
5. **Store listing experiments:** A/B test icon, graphics, screenshots and descriptions (one variable at a time).
6. **Ratings:** In-App Review API → [aso-review-and-rating-strategy](../../aso/aso-review-and-rating-strategy/SKILL.md).

### Level 3: Grow
- **Custom store listings:** up to 50 variants, targeted by country, by URL (for ads and links), or for users who
  pre-registered or stopped using the app.
- **Promotional content (LiveOps):** events, offers and major updates shown on the store.
- **Pre-registration** for a new app or game: collect sign-ups before launch.
- **Deep links** from custom listings to the right screen.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are a Google Play Console expert. Fill my Google Play listing sheet (Level 1 + Level 2).

App: {{what it does, who for}}   Free or paid: {{...}}   Account type: {{personal, created when / organization}}
Brand: {{name}}   Default language + main markets: {{...}}
Target keywords (if researched): {{...}}
SDKs in the app: {{analytics, crash, ads, payments, login...}}
Login required? {{yes/no}}   Shows ads? {{yes/no}}   Target age group: {{...}}

Output:
1. Store listing fields with character counts: name (≤30), short description (≤80), full description (≤4000, uses
   each target phrase 2-4 times naturally, no "#1/best/free", no keyword lists).
2. A Data safety draft: data type | collected or shared | by which SDK | purpose | optional? | encrypted in transit?
   Flag anything I must verify in each SDK's docs.
3. App content answers: app access (reviewer instructions), ads, likely content rating, target audience.
4. If my account is personal and new: a 14-day closed-test plan for 12+ testers (where to find them, what to ask them
   to do daily, what to write in the production access questionnaire).
5. A staged-rollout plan with the metrics to check before each step.
Never invent facts about my app. Mark unknowns as TODO.
````

## Example output

> **Illustrative example.** Fictional app, shown for format.

```text
Name (23/30):        Sipwell: Water Reminder
Short (74/80):       Drink more water with gentle reminders that pause during your meetings.
Graphics:            icon-512.png · feature-1024x500.png · 6 phone screenshots with captions
Data safety:         Crash logs (Crashlytics, collected, not shared, app functionality)
                     Purchase history (RevenueCat, collected, not shared, app functionality)
App access:          No login needed
Ads:                 No ads · Content rating: Everyone · Target audience: 18+
Closed test:         15 testers (friends + r/androidapps beta thread), day 1: 3 Oct → production access from 17 Oct
Rollout:             20% (48 h, crash-free > 99.5%) → 50% → 100%
```

## Common mistakes
- **Starting the 14-day closed test the week before launch.** Start it the day you have a working build.
- **Data safety that ignores SDKs.** Analytics, crash and ads SDKs collect data even if your code doesn't.
- **Choosing "Free" for an app you might sell later.** Free → paid isn't possible. Use in-app purchases instead.
- **Keyword stuffing the description.** It can get the listing rejected under the Metadata policy.
- **100% rollout on day one.** A crash hits every user at once.

## Related skills
- [listing-app-store](../listing-app-store/SKILL.md): the same flow for iOS.
- [listing-free-directories](../listing-free-directories/SKILL.md): free places to list the app after launch.
- [launch-pre-launch-checklist](../../launch/launch-pre-launch-checklist/SKILL.md): put the 14-day test on your launch calendar.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: [Play Console Help](https://support.google.com/googleplay/android-developer/)
("App testing requirements for new personal developer accounts", "Data safety", "Add preview assets",
"Custom store listings"), and the [Google Play policy center](https://play.google.com/about/developer-content-policy/).
Requirements change, so check them before each release.
