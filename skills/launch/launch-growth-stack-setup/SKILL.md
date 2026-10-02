---
name: launch-growth-stack-setup
description: Set up the growth plumbing every app needs before launch, and verify each piece works: Firebase (Analytics with a small event plan, Crashlytics, Remote Config), AdMob (test ads, app-ads.txt, GDPR/UMP consent, iOS App Tracking Transparency, placement rules) and payments (provider or in-app purchases, one real test transaction), plus the privacy labels these SDKs require. Ends with a "verified" checklist so nothing is half set up on launch day. Use when someone asks "what do I need to set up before launching my app", "set up Firebase analytics", "add AdMob to my app", "AdMob account disabled / invalid traffic", "app-ads.txt", "UMP consent", "ATT prompt", "which events should I track", "Firebase + AdMob + payment setup", "setup Firebase, AdMob, Payment đầy đủ", or is about to ship an iOS or Android app without analytics.
license: MIT
metadata:
  category: launch
  difficulty: intermediate
  time: "3-5 h spread over a week (store and AdMob reviews add waiting time)"
  version: 1.0.0
  author: nvminhtu
---

# Growth Stack Setup: Firebase, AdMob, Payments

> In about a week you'll have analytics that answer "where do users drop off?", crash reports, a remote switch for
> experiments, ads that won't get your account flagged, a payment path with one real test transaction, and privacy
> labels that match.

## Goal
Launch day is the one traffic spike you can't recreate. If analytics, crash reporting, ads or payments are broken
that day, you lose the data and the money. This skill sets up the minimum stack and, more importantly,
**verifies** each part, because "installed the SDK" and "it works" are different things.

## When to use
- An iOS or Android app is 1–3 weeks from launch (or live without analytics).
- You plan to earn from ads, in-app purchases, or both.
- Your AdMob account got an invalid-traffic warning, or ads don't show.
- **Not for:** choosing a payment provider for a web product → [monetization-payment-setup](../../monetization/monetization-payment-setup/SKILL.md).
  Coding in-app purchases → [monetization-in-app-purchase-setup](../../monetization/monetization-in-app-purchase-setup/SKILL.md).
  Web apps and extensions can follow steps 1–2 with web analytics instead of Firebase.

## Inputs
- The app's bundle ID / package name, and access to App Store Connect / Play Console.
- A website on your own domain (needed for `app-ads.txt` and the privacy policy).
- Your revenue model: ads, in-app purchases / subscriptions, paid upfront, or a mix.
- Your **activation event**: the action that means a user got value (e.g. "first habit completed").
- Firebase and AdMob accounts (Google account). Check each product's [pricing](https://firebase.google.com/pricing) page;
  Analytics, Crashlytics and Remote Config are in the free tier at the time of writing.

## Decide first: ads, purchases, or both
| Model | Fits | Watch out |
|---|---|---|
| **Ads only** | Casual games, utilities used briefly by many people | Needs volume; bad placement hurts ratings and can get ads disabled |
| **Purchases only** | Tools people use often, niche or pro users | Needs a clear paid value; see [free trial vs freemium](../../monetization/monetization-free-trial-vs-freemium/SKILL.md) |
| **Both** | Free with ads + "remove ads" or Pro purchase | Make sure paying users really see no ads, and restore works |

## Steps

### 1. Firebase Analytics: a small event plan (60 min)
Track **5–8 events**, not 50. Some events are collected automatically, including `first_open`, `in_app_purchase`
for App Store / Google Play purchases, and `ad_impression` for AdMob ads
([automatically collected events](https://support.google.com/analytics/answer/9234069)). Add only what's missing:

| Event | When | Why |
|---|---|---|
| `sign_up` (if accounts) | Account created | Funnel step |
| `activation` (your name, e.g. `first_habit_done`) | User reaches the value moment | **The most important event you'll log** |
| `paywall_view` | Paywall shown, with a `source` parameter | Which screen sells |
| `purchase` check | Verify `in_app_purchase` shows up; if not, log purchases yourself | Revenue in the funnel |
| `share` / `invite` | User shares | Viral loop |
| `rewarded_ad_complete` (if rewarded ads) | User finishes a rewarded ad | Ad value vs churn |

Follow [Get started with Analytics](https://firebase.google.com/docs/analytics/get-started), then **verify** in
[DebugView](https://firebase.google.com/docs/analytics/debugview): run a debug build, do each action, and watch each
event arrive. Mark the activation and purchase events as key events (conversions) in the console.

### 2. Crashlytics and Remote Config (45 min)
- **Crashlytics:** follow [the setup](https://firebase.google.com/docs/crashlytics/get-started), then force a test crash
  and confirm it appears in the console. Upload dSYMs (iOS) / mapping files (Android) or the stack traces are unreadable.
- **Remote Config:** add 2–3 switches you'll want after launch without a new build: `paywall_variant`,
  `ad_frequency_cap`, `show_rating_prompt`. Defaults in the app, values in the console
  ([Remote Config](https://firebase.google.com/docs/remote-config)). Later, [A/B Testing](https://firebase.google.com/docs/ab-testing)
  can test them.

### 3. AdMob without getting flagged (90 min + review wait)
1. **Test ads only during development.** Google warns that clicking too many live ads outside test mode can get
   the account flagged for invalid activity. Use Google's demo ad units or register your test devices
   ([Android](https://developers.google.com/admob/android/test-ads) · [iOS](https://developers.google.com/admob/ios/test-ads)).
   **Never click your own live ads**, and don't ask friends to ([invalid traffic](https://support.google.com/admob/answer/3342054)).
2. **app-ads.txt:** add your developer website to both store listings, then publish `app-ads.txt` at the root of that
   domain with the line AdMob gives you. Verification can take up to 24 hours
   ([app-ads.txt guide](https://support.google.com/admob/answer/9363762)).
3. **Consent (EEA, UK, Switzerland):** create a GDPR message in AdMob's *Privacy & messaging* and add the Google UMP SDK
   so it shows before ads load ([UMP quick start](https://developers.google.com/admob/ump/android/quick-start),
   [iOS privacy](https://developers.google.com/admob/ios/privacy)). Without consent, limited ads serve.
4. **iOS tracking:** if any SDK uses the advertising identifier (IDFA), you must ask with
   [App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency) and add
   `NSUserTrackingUsageDescription`. Show the prompt after the user has seen some value, not on first launch.
5. **Placement:** follow the [AdMob program policies](https://support.google.com/admob/answer/6128543). Don't put banners
   next to buttons ([banner guidance](https://support.google.com/admob/answer/6128877)), don't show interstitials on
   app launch or mid-action, and cap their frequency (use the Remote Config switch from step 2).
6. **Remove ads for payers:** if you sell "remove ads", check the entitlement **before** loading any ad, on every launch.

### 4. Payments: one real transaction (60 min + provider review)
- In-app purchases or subscriptions → [monetization-in-app-purchase-setup](../../monetization/monetization-in-app-purchase-setup/SKILL.md)
  (sandbox purchase, restore, server notifications).
- Web checkout, or a country Stripe doesn't support → [monetization-payment-setup](../../monetization/monetization-payment-setup/SKILL.md).
- **Verify:** one sandbox purchase *and* one real low-price purchase (refund it yourself), and check that the purchase
  event appears in Analytics and the entitlement unlocks the feature.

### 5. Privacy labels must match the SDKs (30 min)
Every SDK you added collects data you must declare: App Store [privacy details](https://developer.apple.com/app-store/app-privacy-details/)
and [privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files), Google Play
[Data safety](https://support.google.com/googleplay/android-developer/answer/10787469). Firebase publishes what its SDKs
collect for [App Store](https://firebase.google.com/docs/ios/app-store-data-collection) and
[Google Play](https://firebase.google.com/docs/android/play-data-disclosure); AdMob documents its own. Update your
privacy policy to name them.

### 6. The verified checklist (do it on the release build)
- [ ] Every planned event appears in DebugView with the right parameters
- [ ] Activation and purchase are marked as key events
- [ ] A test crash appears in Crashlytics with a readable stack trace
- [ ] Remote Config values change app behaviour without a new build
- [ ] Release build uses **live** ad unit IDs; debug build uses **test** ads
- [ ] `app-ads.txt` shows as verified in AdMob
- [ ] The consent message appears for an EEA/UK test (use the UMP debug geography setting)
- [ ] ATT prompt (iOS) appears at the planned moment, and the app works if the user declines
- [ ] One sandbox + one real purchase done; restore works; paying users see no ads
- [ ] App privacy details / Data safety / privacy policy list every SDK

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are a mobile growth engineer who has shipped many iOS and Android apps with Firebase and AdMob without account
problems. Cite the official doc for every rule. Don't invent SDK APIs; if unsure, tell me which doc to check.

App: {{what it does, platform(s): iOS / Android / Flutter / React Native / Unity}}
Revenue model: {{ads / in-app purchases / subscriptions / mix}}
Activation event (value moment): {{...}}
Screens where a paywall or ads could appear: {{...}}
Users in EEA/UK expected: {{yes/no}}   Uses IDFA on iOS: {{yes/no/don't know}}
Already set up: {{...}}

1. Write my event plan: 5–8 events with names, parameters and why. Mark which are collected automatically.
2. List the exact setup steps for Firebase Analytics, Crashlytics and Remote Config for my platform, with the
   2–3 Remote Config switches I should add.
3. For AdMob: ad formats and placements that fit my app, a frequency cap, and the steps for test ads,
   app-ads.txt, UMP consent and ATT. Flag any placement that risks invalid clicks.
4. Point me to the right payment path (in-app purchases or web provider) and the test transactions to run.
5. List the privacy label / Data safety items my SDK list implies.
6. Give me the verified checklist for my release build.
````

## Example output

> **Illustrative example.** A fictional app.

*Habit tracker, iOS + Android (Flutter), free with banner ads + $2.99 "Pro: no ads + unlimited habits".*

| Event | Auto? | Parameters |
|---|---|---|
| `first_open` | ✅ | — |
| `first_habit_done` (activation) | — | `template_used` |
| `paywall_view` | — | `source`: limit_reached / settings / onboarding |
| `in_app_purchase` | ✅ (verified in DebugView) | — |
| `share_streak` | — | `days` |

Remote Config: `paywall_variant` (a/b), `banner_enabled` (true), `rating_prompt_after_days` (5).
AdMob: one banner at the bottom of the stats screen only (no buttons nearby), no interstitials in v1.
ATT: not needed (no IDFA); UMP consent: yes, EEA/UK users expected.
Checklist: 10/10 passed on build 1.0.0 (42), 3 days before launch.

## Common mistakes
- **Testing with live ads.** The fastest way to an invalid-traffic warning. Test ads in every debug build.
- **Logging 50 events.** You'll never read them. 5–8 events that map to the funnel.
- **No activation event.** Without it you can't tell "installed" from "got value".
- **Interstitial on app launch.** Annoys users, risks policy problems, and costs ratings.
- **Forgetting app-ads.txt.** Your ads earn less or not at all until it's verified.
- **Privacy labels that don't match the SDKs.** A common rejection reason, and a trust problem.
- **"Remove ads" that still loads ads** for a moment on launch. Check the purchase before the first ad request.

## Related skills
- [launch-pre-launch-checklist](../launch-pre-launch-checklist/SKILL.md): put this setup on the launch calendar.
- [monetization-in-app-purchase-setup](../../monetization/monetization-in-app-purchase-setup/SKILL.md): the purchase code and tests.
- [monetization-payment-setup](../../monetization/monetization-payment-setup/SKILL.md): web payments and payouts by country.
- [strategy-revenue-target](../../strategy/strategy-revenue-target/SKILL.md): the funnel these events measure.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: Firebase docs, Google AdMob Help and developer guides,
Apple and Google Play privacy docs, all linked inline (checked 2026-10-02).
