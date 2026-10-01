---
name: monetization-in-app-purchase-setup
description: Set up in-app purchases and subscriptions inside iOS, macOS and Android apps, and decide how to build them. Three routes are compared: code StoreKit 2 and Google Play Billing Library yourself, use a free open-source wrapper (Flutter in_app_purchase, react-native-iap, expo-iap, cordova-plugin-purchase, Unity IAP), or use a subscription SDK (RevenueCat, Adapty, Qonversion, Superwall). Work goes in three levels (1 first sandbox purchase, 2 production-ready with restore, acknowledge, server notifications and App Review, 3 offers, paywall tests and web purchases). Use when adding in-app purchases, "StoreKit 2 or RevenueCat", "how to implement subscriptions in my app", "Play Billing Library version", "Google Play Billing integration", "restore purchases", "IAP rejected by App Review", "in-app purchase Flutter / React Native / Expo / Capacitor", or before turning on paid features in a mobile or Mac App Store app.
license: MIT
metadata:
  category: monetization
  difficulty: intermediate → advanced (3 levels)
  time: "Level 1: 2-4 h · Level 2: 1-3 days · Level 3: ongoing"
  version: 1.0.0
  author: nvminhtu
---

# In-App Purchase Setup (StoreKit 2 · Play Billing · SDKs)

> By the end you'll have chosen your route (code it yourself, a free wrapper, or an SDK), and you'll have a working
> purchase in the sandbox. Then you'll get it through App Review without the usual rejections.

## Goal
Charge inside the app the way Apple and Google require, and don't spend weeks on it. Stores rarely reject for bad
code. They reject for the details around it: no Restore button, a purchase the reviewer can't find, a Google purchase
refunded because it was never acknowledged. This skill covers the code and those details.

## When to use
- You're adding paid features, a subscription, or coins to an iOS, iPadOS, macOS (App Store) or Android app.
- You're choosing between StoreKit 2, Play Billing and RevenueCat, Adapty or Superwall.
- Google warned you about an old Play Billing Library version, or App Review rejected your IAP.
- **Not for:** getting paid, bank accounts or country support → [monetization-payment-setup](../monetization-payment-setup/SKILL.md).
  Web, desktop outside the App Store, or extensions → also [monetization-payment-setup](../monetization-payment-setup/SKILL.md).
  The paywall screen → [monetization-paywall-design](../monetization-paywall-design/SKILL.md).

## Inputs
- A developer account on each store: Apple Developer Program, Google Play Console.
- **Paid Apps Agreement signed** (Apple) and a **payments profile** linked (Google). Without these, products don't
  load at all → [monetization-payment-setup](../monetization-payment-setup/SKILL.md).
- The product list: product IDs, type (consumable, non-consumable, subscription), price, trial.
- Your stack: Swift / Kotlin / Flutter / React Native / Expo / Capacitor / Unity / KMP.
- Whether you have (or want) a backend.

## What the stores require (checked 2026-10-01)

| | Apple (iOS, iPadOS, macOS, visionOS) | Google Play (Android) |
|---|---|---|
| Must use for digital goods | In-App Purchase (Guideline 3.1.1). US storefront may link out since May 2025 | Play Billing (Payments policy). US: alternative billing / external links programs since Dec 2025 |
| Current API | **StoreKit 2** (iOS 15+ / macOS 12+). Original StoreKit and `verifyReceipt` are **deprecated** | **Play Billing Library 9.1** (June 2026). **PBL 8+ required** for new apps and updates since 31 Aug 2026 (extension to 1 Nov 2026) |
| Ready-made UI | `StoreView`, `SubscriptionStoreView`, `ProductView` (iOS 17+) | None. Google shows its own purchase sheet |
| Must do after a purchase | `transaction.finish()`. Listen to `Transaction.updates` from app launch | **Acknowledge within 3 days** or it's refunded automatically. Consumables: consume |
| Restore | Required. A Restore button calling `AppStore.sync()` | `queryPurchasesAsync()` on launch |
| Server (optional but recommended) | App Store Server API + **Server Notifications V2** (V1 deprecated). Official library: Swift, Java, Python, Node | Play Developer API (`purchases.subscriptionsv2.get`) + **RTDN** via Cloud Pub/Sub |
| Local testing | `.storekit` file in Xcode. No App Store Connect needed | None. A build with PBL must be on a track (internal is fine) before you can create products |
| Sandbox | Sandbox Apple Account. 1 month = 5 min by default | License testers, test cards. 1 month = 5 min |
| Mac apps | IAP works **only** for Mac App Store builds, not Developer ID | — |

Details and every source: [references/iap-platform-facts.md](references/iap-platform-facts.md).

## Step 0: Pick your route

| Route | What it is | Cost | Choose it when |
|---|---|---|---|
| **A. Code it yourself** | StoreKit 2 (Swift) + Play Billing Library (Kotlin) | Free | One platform, simple products (a lifetime unlock, a few consumables), you're comfortable in native code |
| **B. Free wrapper** | Flutter `in_app_purchase` (official), `flutter_inapp_purchase`, `react-native-iap`, `expo-iap`, `cordova-plugin-purchase`, `@capgo/native-purchases`, Unity IAP | Free, open source | Cross-platform app, and you'll build validation and entitlements yourself (or skip the server) |
| **C. Subscription SDK** | RevenueCat, Adapty, Qonversion, Superwall, Apphud | Free up to a revenue threshold, then about 1% | **Subscriptions on both stores**, you have no backend, or you want remote paywalls and A/B tests |

**SDK free tiers** (from their pricing pages): RevenueCat free up to $2,500/month tracked revenue, then 1% ·
Adapty up to $5K/month, then 1% · Qonversion up to $7K/month, then 0.8% of all tracked revenue · Superwall's
subscription backend is free at any scale, and its paywalls are free up to $10K/month of paywall revenue, then 1%.
Glassfy **shut down** at the end of 2024; don't pick it.

**Even with an SDK you still do Level 1 on both stores:** agreements, products, testers. The SDK replaces your
code and server, not the store setup.

### What indie devs pick (opinion, not data)
- **One non-consumable on iOS only:** StoreKit 2 directly, no server, one small `Store` class. `Transaction.currentEntitlements`
  tells you who owns it.
- **Subscriptions on iOS + Android, no backend:** RevenueCat has an SDK for every stack in this skill. Superwall if you
  also want paywall tests and a backend that stays free. Adapty or Qonversion give you a higher free tier.
- **Flutter / React Native, one-time purchases only:** the free wrapper is enough.
- **Expo:** IAP doesn't run in Expo Go, so you need a development build (`expo-iap` or `react-native-purchases`).
- **Unity games:** Unity IAP 5.x (StoreKit 2, PBL 9).
- **Capacitor / Ionic:** RevenueCat's Capacitor SDK, or `cordova-plugin-purchase` with its StoreKit 2 add-on.

## Steps

### Level 1: First sandbox purchase (2–4 h)
**Apple**
1. App Store Connect → Business: the Account Holder signs the **Paid Apps Agreement**, then adds tax forms and bank.
2. Your app → Monetization → create the products (IAP or subscription group). Write the product IDs down;
   you can't reuse them. Add a **review screenshot** for each.
3. Xcode: add a **StoreKit configuration file** (synced with App Store Connect, or local) and select it in the scheme.
   You can now buy in the Simulator before anything else is approved.
4. Load products with `Product.products(for:)`. **An empty list almost always means a wrong ID or unsigned agreement.**
5. Buy, verify, `finish()`, unlock. See [references/minimal-code.md](references/minimal-code.md).

**Google**
1. Link a **payments profile** to Play Console.
2. Add Play Billing Library **8 or 9** (`com.android.billingclient:billing-ktx`) and upload an AAB to **internal
   testing**. Monetization features only unlock after a build with billing exists on a track.
3. Monetize with Play → Products: create one-time products or subscriptions (base plan + offers).
4. Settings → License testing: add your Google account. Install from the internal testing link.
5. Query product details, launch the billing flow, **acknowledge**. See [references/minimal-code.md](references/minimal-code.md).

**SDK route:** do steps 1–3 on each store, then connect the stores in the SDK dashboard (Apple: In-App Purchase key;
Google: service account with financial-data access) and follow its quickstart.

### Level 2: Production-ready (1–3 days)
1. **Listen for purchases at launch.** Apple: start a `Transaction.updates` task at launch (Ask to Buy, renewals,
   offer codes and purchases on other devices arrive there). Google: `queryPurchasesAsync()` in `onResume`.
2. **One source of truth for "is Pro".** Apple: `Transaction.currentEntitlements`. Google: active purchases + your
   server. SDK: its entitlements. Never store "isPro = true" locally as the only proof.
3. **Handle every state:** pending (Google: grant only on `PURCHASED`), cancelled, failed, refunded / revoked
   (Family Sharing), grace period and billing retry for subscriptions.
4. **Restore Purchases button** on the paywall and in settings. Apple requires it for restorable purchases.
5. **Server (recommended for subscriptions):**
   - Apple: App Store Server Notifications **V2** → your endpoint. Verify with the App Store Server Library.
     Keep the In-App Purchase key server-side only; it downloads once.
   - Google: RTDN → Pub/Sub topic → your endpoint. Then call `purchases.subscriptionsv2.get` for the real status.
     Use the Voided Purchases API (last 30 days) for refunds.
   - No backend? Use an SDK (route C) rather than building a half-server.
6. **Test the ugly paths:** in Xcode (StoreKit Testing: refunds, failed renewals, Ask to Buy), Apple sandbox,
   TestFlight (renews once a day, up to 6 times), and Google test cards (declined, slow, chargeback) plus Play Billing Lab.
7. **App Review checklist before you submit:**
   - [ ] The **first IAP of each type is submitted together with a new app version**.
   - [ ] The reviewer can reach every product in 2 taps, and it works (Guideline 2.1).
   - [ ] Restore button present.
   - [ ] The paywall states what the user gets, the price, billing period, trial length and that it auto-renews (3.1.2).
   - [ ] Links to Terms of Use and Privacy Policy on the paywall and in the store listing.
   - [ ] Subscriptions are at least 7 days and work on all the user's devices.
   - [ ] Google: easy cancellation + a link to `play.google.com/store/account/subscriptions`.
   - [ ] Google: Play Billing Library 8+ in the release.
8. **Enroll in the 15% programs** (Apple Small Business Program, Google 15% tier) if you haven't already.

### Level 3: Earn more from the same users (ongoing)
- **Offers:** Apple intro offers, promotional offers (need a server to sign), **win-back offers**, offer codes
  (now for all IAP types; IAP promo codes can't be created after 26 Mar 2026). Google: base plans + offers, prepaid
  plans, and discounts and pre-orders on one-time products (PBL 8+).
- **Paywall experiments:** change one thing at a time → [monetization-paywall-design](../monetization-paywall-design/SKILL.md).
  SDKs with remote paywalls let you test without shipping a new build.
- **Web purchases:** US storefronts on both stores can now link to web checkout. RevenueCat, Adapty, Qonversion,
  Apphud and Superwall can grant the same entitlement from Stripe or Paddle purchases. Check fees and rules per
  region first.
- **Keep versions current:** each Play Billing Library major version is supported for 2 years (PBL 8 until
  31 Aug 2027). Put a reminder in your calendar.
- **Other stores:** Microsoft Store (12% games / 15% apps; non-game apps may use their own payments and keep 100%),
  Steam microtransactions, Meta Quest. Sources are in the reference file.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are a senior mobile engineer who ships in-app purchases on the App Store and Google Play.
Use only current APIs: StoreKit 2 (not original StoreKit / verifyReceipt) and Play Billing Library 8 or later.
Tell me to confirm versions and fees on Apple/Google's official docs, because they change.

App: {{what it does}}   Platforms: {{iOS / Android / macOS}}   Stack: {{Swift, Kotlin, Flutter, RN, Expo, Capacitor, Unity}}
Products: {{e.g. pro_lifetime non-consumable $19; pro_monthly $4.99 with 7-day trial; coins_100 consumable}}
Backend: {{none / Firebase / my own API in ...}}   Expected revenue in 12 months: {{...}}

1. Recommend ONE route (code StoreKit 2 + Play Billing myself / a free wrapper / RevenueCat, Adapty, Qonversion or
   Superwall) and say why, including what it costs me at my expected revenue.
2. List the store setup steps for each platform, in order (agreements, products, testers, tracks, keys).
3. Write the minimal purchase code for my stack: load products, buy, verify, finish/acknowledge, restore,
   listen for updates at launch, and one `isPro` source of truth. Show where server verification goes.
4. List the states I must handle (pending, cancelled, refunded, grace period, billing retry, Family Sharing revoke).
5. Give me the App Review / Play policy checklist for my paywall and products, and a test plan
   (Xcode StoreKit Testing, sandbox, TestFlight, Google license testers and test cards).
````

## Example output

> **Illustrative example.** A fictional app and figures, shown to demonstrate the format.

*Habit tracker, Flutter, iOS + Android, `pro_monthly` $3.99 with a 7-day trial and `pro_lifetime` $29, Firebase only.*

- **Route: C, RevenueCat** (`purchases_flutter`). Subscriptions on two stores and no real backend, and the app is
  expected to stay under $2,500/month tracked revenue for a while, so it costs $0.
- **Store setup:** Apple Paid Apps Agreement ✅ · subscription group "Pro" + non-consumable · StoreKit config file ·
  Google payments profile ✅ · AAB with PBL 8 on internal testing · base plan `monthly` + free-trial offer ·
  2 license testers · RevenueCat: In-App Purchase key + Google service account connected.
- **One entitlement `pro`** unlocked by either product. The app only checks `customerInfo.entitlements["pro"].isActive`.
- **Review fixes caught before submitting:** the paywall didn't mention auto-renew, and there was no Restore button in Settings.

| Day | Milestone |
|---|---|
| 1 | Products created on both stores, first sandbox purchase on iOS |
| 2 | Android internal test purchase acknowledged, restore works on a second device |
| 3 | Refund / expiry tested, paywall copy fixed, submitted with the new version |

## Common mistakes
- **Starting new code on original StoreKit or `verifyReceipt`.** Both are deprecated. Use StoreKit 2.
- **Not acknowledging Google purchases.** After 3 days they're refunded and the user loses access.
- **Granting access while a Google purchase is `PENDING`.**
- **Listening for transactions only on the paywall.** Renewals, Ask to Buy and purchases on other devices arrive at
  any time. Start the listener at app launch.
- **Submitting the first IAP without a new app version.** Apple reviews them together.
- **Products don't load and you debug code for hours.** Check the agreement, the product IDs, and that the product is
  "Ready to Submit" (Apple) or active with a build on a track (Google).
- **Shipping the In-App Purchase key or service-account JSON in the app.** Those stay on the server.
- **Using a Developer ID build to test Mac IAP.** StoreKit only works for Mac App Store distribution.
- **Forgetting Play Billing Library deadlines.** Old versions block your next update.

## Related skills
- [monetization-payment-setup](../monetization-payment-setup/SKILL.md): agreements, bank, tax and getting paid, before this skill.
- [monetization-pricing-strategy](../monetization-pricing-strategy/SKILL.md): which prices to create as products.
- [monetization-paywall-design](../monetization-paywall-design/SKILL.md): the screen that sells the product.
- [listing-app-store](../../listing/listing-app-store/SKILL.md) · [listing-google-play](../../listing/listing-google-play/SKILL.md): the submission around it.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: Apple Developer Documentation (StoreKit, App Store
Server API, App Store Server Notifications, App Review Guidelines, WWDC25 session 241, WWDC26 session 210),
Android Developers (Play Billing Library integration, release notes, deprecation FAQ, testing), Play Console Help
(Payments policy, subscriptions policy, service fees), and vendor pricing and docs pages. All links are in
[references/iap-platform-facts.md](references/iap-platform-facts.md). Checked 2026-10-01.
