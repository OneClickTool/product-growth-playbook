# In-app purchase facts: Apple, Google, SDKs, other stores

The source file behind [monetization-in-app-purchase-setup](../SKILL.md). **Checked 2026-10-01.** "Unconfirmed" means
no official page confirmed it. When you re-check something, update the line and the date.

## 1. Apple: StoreKit

**StoreKit 2 vs original StoreKit**
- The original In-App Purchase API is **deprecated**. StoreKit 2 needs iOS 15, macOS 12, tvOS 15, watchOS 8 or
  visionOS 1. Apple says to use the original API only if your app still supports iOS 14 / macOS 11 or earlier
  ([choosing an API](https://developer.apple.com/documentation/storekit/choosing-a-storekit-api-for-in-app-purchases)).
- `SKPaymentQueue` is marked deprecated in iOS 18 / macOS 15 ([docs](https://developer.apple.com/documentation/storekit/skpaymentqueue)).
- App Store receipts and `verifyReceipt` are deprecated. Use the App Store Server API or signed `Transaction` /
  `AppTransaction` data instead ([docs](https://developer.apple.com/documentation/appstorereceipts)).
  No shutdown date has been published. It was announced at [WWDC23](https://developer.apple.com/videos/play/wwdc2023/10141/).
- Only StoreKit 2 has StoreKit views, the refund request sheet, renewal status, intro-offer eligibility, the Manage
  Subscriptions sheet and JWS transactions.

**Key APIs**
- [`Product.products(for:)`](https://developer.apple.com/documentation/storekit/product/products(for:)): IDs that
  don't exist are silently dropped, so you get an empty list rather than an error.
- [`Transaction.updates`](https://developer.apple.com/documentation/storekit/transaction/updates): start listening at launch.
- [`Transaction.currentEntitlements`](https://developer.apple.com/documentation/storekit/transaction/currententitlements):
  covers non-consumables, active or grace-period subscriptions and non-renewing subscriptions. It never includes
  consumables or refunded purchases.
- [`finish()`](https://developer.apple.com/documentation/storekit/transaction/finish()) ·
  [`AppStore.sync()`](https://developer.apple.com/documentation/storekit/appstore/sync()) (restore) ·
  [`VerificationResult`](https://developer.apple.com/documentation/storekit/verificationresult) (the JWS is verified on
  the device; `jwsRepresentation` can also be verified on your server) ·
  [`AppTransaction`](https://developer.apple.com/documentation/storekit/apptransaction).
- Since iOS 18.2 a purchase needs a UI context. In SwiftUI, use the `purchase` environment action
  ([WWDC25 · 241](https://developer.apple.com/videos/play/wwdc2025/241/)).
- SwiftUI views [`StoreView`](https://developer.apple.com/documentation/storekit/storeview), `SubscriptionStoreView`
  and `ProductView` need iOS 17 / macOS 14.
  [`SubscriptionOfferView`](https://developer.apple.com/documentation/storekit/subscriptionofferview) needs iOS 26.

**Recent changes**
- WWDC25: `SubscriptionOfferView`, `appTransactionID`, offer codes for all product types, JWS-signed promotional
  offers, and the [Advanced Commerce API](https://developer.apple.com/documentation/advancedcommerceapi) for very
  large catalogs.
- Offer codes work for all IAP types. **Promo codes for IAPs can't be created from 26 Mar 2026**
  ([news](https://developer.apple.com/news/?id=gf6mgrs6)).
- WWDC26: monthly subscriptions with a 12-month commitment (not available in the US or Singapore;
  [news](https://developer.apple.com/news/?id=agq42lxe)), and Bundles and Suites in iOS 27
  ([news](https://developer.apple.com/news/?id=likeohx4), [session 210](https://developer.apple.com/videos/play/wwdc2026/210/)).

**Product types** ([docs](https://developer.apple.com/documentation/storekit/original-api-for-in-app-purchase))
- Consumable.
- Non-consumable (can be Family Shared).
- Auto-renewable subscription (can be Family Shared). Up to 100 per
  [subscription group](https://developer.apple.com/help/app-store-connect/manage-subscriptions/offer-auto-renewable-subscriptions/);
  a user has one active subscription per group.
- Non-renewing subscription. **Your app** has to sync and restore it.

**Offers**
- [Introductory](https://developer.apple.com/documentation/storekit/implementing-introductory-offers-in-your-app):
  one per subscription group per user.
- [Promotional](https://developer.apple.com/documentation/storekit/implementing-promotional-offers-in-your-app):
  must be signed with a key.
- [Win-back](https://developer.apple.com/documentation/storekit/supporting-win-back-offers-in-your-app).
- [Family Sharing](https://developer.apple.com/documentation/storekit/supporting-family-sharing-in-your-app):
  up to 5 members. **Once you turn it on for a product, you can't turn it off.** Handle `REVOKE`.

**Server**
- [App Store Server API](https://developer.apple.com/documentation/appstoreserverapi): transaction info and history,
  all subscription statuses, refund history, consumption info, notification history, test notification, extend
  renewal date, look up order ID.
- [Server Notifications V1 is deprecated](https://developer.apple.com/documentation/appstoreservernotifications/app-store-server-notifications-v1).
  New apps can't choose V1 ([TN3180](https://developer.apple.com/documentation/technotes/tn3180-reverting-app-store-server-notifications-v1)).
- [App Store Server Library](https://developer.apple.com/documentation/appstoreserverapi/simplifying-your-implementation-by-using-the-app-store-server-library)
  in Swift, Java, Python and Node: an API client, `verifyAndDecodeTransaction` and `verifyAndDecodeRenewalInfo`,
  receipt migration, and offer signing.
- The [In-App Purchase key](https://developer.apple.com/documentation/appstoreserverapi/creating-api-keys-to-authorize-api-requests)
  lives in App Store Connect → Users and Access → Integrations. **You can download it only once.** Never put it in
  the app or in a repo.
- Apple doesn't require a server. On-device `VerificationResult` + `currentEntitlements` works without one.
  Apple recommends a server for subscriptions
  ([receipt validation](https://developer.apple.com/documentation/storekit/choosing-a-receipt-validation-technique)).

**Testing**
- [StoreKit Testing in Xcode](https://developer.apple.com/documentation/xcode/setting-up-storekit-testing-in-xcode):
  uses a local `.storekit` file, needs no App Store Connect setup, and runs in the Simulator or on a device
  (Developer Mode on iOS 16+).
- [Sandbox](https://developer.apple.com/documentation/storekit/testing-in-app-purchases-with-sandbox): needs the
  Paid Apps Agreement. Product changes can take up to 1 hour to show up.
  [Renewal rate](https://developer.apple.com/help/app-store-connect/test-in-app-purchases/manage-sandbox-apple-account-settings/):
  1 month = 5 min by default (adjustable), up to 12 renewals.
- [TestFlight](https://developer.apple.com/help/app-store-connect/test-a-beta-version/testing-subscriptions-and-in-app-purchases-in-testflight/):
  renews once a day, up to 6 times.

**App Store Connect and App Review**
- [Sign the Paid Apps Agreement](https://developer.apple.com/help/app-store-connect/manage-agreements/sign-and-update-agreements/)
  first, then tax forms, then banking.
- The [first IAP of each type goes out with a new app version](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-in-app-purchase).
- Each IAP needs a [review screenshot](https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-information/).
- [Guidelines](https://developer.apple.com/app-store/review/guidelines/):
  - 2.1: IAPs must be complete and visible to the reviewer.
  - 3.1.1: use IAP for digital unlocks, and provide a restore mechanism.
  - 3.1.2: subscriptions last at least 7 days and work on all the user's devices.
  - 3.1.2(c): describe clearly what the user gets for the price.
  - The exact wording about Terms and Privacy links is unconfirmed. Include both links anyway.
- US storefront external purchase links have been allowed since 1 May 2025 ([news](https://developer.apple.com/news/?id=9txfddzf)).
- [Mac](https://developer.apple.com/macos/distribution/): IAP works in the Mac App Store and isn't available with
  Developer ID distribution.

## 2. Google Play Billing

**Play Billing Library** ([release notes](https://developer.android.com/google/play/billing/release-notes))
- 9.1.0 (18 Jun 2026): Billing Choice APIs.
- 9.0.0 (19 May 2026): targetSdk 35; `BILLING_UNAVAILABLE` when the Play Store is blocked.
- 8.3.0 (Dec 2025): external payments APIs.
- 8.1.0 (Nov 2025): suspended subscriptions, `KEEP_EXISTING`, minSdk 23.
- 8.0.0 (30 Jun 2025): multiple purchase options and offers for one-time products, `enableAutoServiceReconnection()`,
  and "in-app items" renamed to "one-time products".

**Deprecation** ([FAQ](https://developer.android.com/google/play/billing/deprecation-faq)): each version is supported
for 2 years. New apps and updates must be on at least:

| Version | Required from | Extension until |
|---|---|---|
| PBL 8 | 31 Aug 2026 | 1 Nov 2026 |
| PBL 9 | 31 Aug 2027 | 1 Nov 2027 |
| PBL 10 | 31 Aug 2028 | 1 Nov 2028 |

**Integration** ([guide](https://developer.android.com/google/play/billing/integrate))
- Artifacts: `billing` / `billing-ktx`.
- Client setup: `enablePendingPurchases(PendingPurchasesParams…enableOneTimeProducts())` and
  `enableAutoServiceReconnection()`.
- Calls: `queryProductDetailsAsync`, `launchBillingFlow`, `queryPurchasesAsync`. `querySkuDetailsAsync` doesn't work
  with multiple offers.
- **Acknowledge non-consumables and subscriptions within 3 days, or they're refunded automatically.** Consume
  consumables. Grant access only in the `PURCHASED` state.

**Products**
- [One-time products](https://developer.android.com/google/play/billing/one-time-products): consumable or
  non-consumable. PBL 8+ adds [purchase options and offers](https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers):
  Buy / Rent, Discount, Pre-order.
- [Subscriptions](https://developer.android.com/google/play/billing/subscriptions): a base plan (auto-renewing,
  prepaid, or installment in BR/FR/IT/ES) plus offers (free trial, intro price), with replacement modes for upgrades.

**Server**
- [Security](https://developer.android.com/google/play/billing/security): verify the `purchaseToken` on your server
  before granting access.
- Endpoints: `purchases.products.get` and
  [`purchases.subscriptionsv2.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get).
  Access is through a service account with "View financial data"
  ([setup](https://developer.android.com/google/play/billing/getting-ready)).
- RTDN setup:
  1. Create a Pub/Sub topic.
  2. Grant `google-play-developer-notifications@system.gserviceaccount.com` the Publisher role on it.
  3. Enter the topic in Play Console → Monetize → Monetization setup, then send a test message.
  4. Notifications only tell you something changed. Call the API for the details.
- [Voided Purchases API](https://developers.google.com/android-publisher/voided-purchases): covers the last 30 days only.

**Testing** ([test guide](https://developer.android.com/google/play/billing/test))
- [License testers](https://support.google.com/googleplay/android-developer/answer/6062777) aren't charged. Test cards
  cover approve, decline, slow approve/decline, and chargeback.
- A build with PBL must be on a track (internal is fine) before you can create products.
- Test renewal times: a 1-week or 1-month period renews every 5 min, a 1-year period every 30 min. At most 6 renewals.
- Play Billing Lab app: change country, reset trials, test price changes.

**Policy**
- [Payments policy](https://support.google.com/googleplay/android-developer/answer/9858738): digital goods go through
  Play Billing. Physical goods don't.
- [US changes after Epic v. Google](https://support.google.com/googleplay/android-developer/answer/15582165):
  alternative billing and external content links programs since Dec 2025. The fee rates are unconfirmed.
  API docs: [alternative](https://developer.android.com/google/play/billing/alternative),
  [external links](https://developer.android.com/google/play/billing/externalcontentlinks).
  EEA and other regions: [user choice / external offers](https://support.google.com/googleplay/android-developer/answer/16505463).
- [Subscriptions policy](https://support.google.com/googleplay/android-developer/answer/9900533): state the price,
  billing frequency and auto-renewal clearly, make cancellation easy, and link to
  `https://play.google.com/store/account/subscriptions?sku=…&package=…`.
- [Service fees](https://support.google.com/googleplay/android-developer/answer/112622):
  - Most markets: 15% on the first $1M if you're enrolled; subscriptions 15%.
  - EEA, UK and US (from 30 Jun 2026) and AU and JP (from 30 Sep 2026): a new structure, for example 10% + 5%
    billing fee for new installs on the first $1M. Read that page before you calculate.

## 3. Subscription SDKs

| SDK | Free tier → paid | Notes | Source |
|---|---|---|---|
| RevenueCat | ≤ $2,500/mo tracked revenue, then 1% | Entitlements, webhooks, paywalls, experiments, Web Billing (Stripe), Paddle integration. SDKs: iOS, Android, RN, Expo, Flutter, KMP, Cordova, Capacitor, Unity, Web | [pricing](https://www.revenuecat.com/pricing/), [install](https://www.revenuecat.com/docs/getting-started/installation) |
| Adapty | < $5K/mo, then 1% | Paywall builder, A/B tests, web payments via Stripe/Paddle. iOS, Android, RN, Flutter, Unity, KMP, Capacitor | [pricing](https://adapty.io/pricing/), [docs](https://adapty.io/docs/) |
| Qonversion | ≤ $7K/mo, then 0.8% of total | Paywall builder, experiments, Web SDK + Stripe. iOS, Android, Flutter, RN, Unity, Cordova, Capacitor | [pricing](https://qonversion.io/pricing) |
| Superwall | Backend free at any scale; paywalls free up to $10K/mo paywall revenue, then 1% of that | Own StoreKit 2 / Play Billing purchase APIs, entitlements from ASSN V2 + RTDN, web checkout with Stripe | [pricing](https://superwall.com/pricing), [docs](https://superwall.com/docs) |
| Apphud | Pricing page text contradicts itself; check it live | Webhooks only on higher plans | [pricing](https://apphud.com/pricing) |
| Purchasely · Nami ML | Sales / enterprise only | — | [Purchasely](https://www.purchasely.com/pricing), [Nami](https://www.nami.ml/pricing) |
| Glassfy | **Shut down end of 2024** | Repo archived | [GitHub](https://github.com/glassfy/ios-sdk) |

## 4. Free libraries by framework (versions checked 2026-10-01)

| Stack | Library | Version | Notes |
|---|---|---|---|
| Flutter | [in_app_purchase](https://pub.dev/packages/in_app_purchase) (official) | 3.3.1 | StoreKit 2 by default. No backend, so validation is up to you |
| Flutter | [flutter_inapp_purchase](https://pub.dev/packages/flutter_inapp_purchase) | 10.7.2 | StoreKit 2 + PBL 9.1, iOS 15+ |
| Flutter | [purchases_flutter](https://pub.dev/packages/purchases_flutter) (RevenueCat) | 10.13.2 | |
| React Native | [react-native-iap](https://www.npmjs.com/package/react-native-iap) | 16.7.2 | Nitro modules, [OpenIAP](https://github.com/hyodotdev/openiap) |
| Expo | [expo-iap](https://www.npmjs.com/package/expo-iap) | 5.8.2 | Needs a dev build. [Expo Go isn't supported](https://docs.expo.dev/guides/in-app-purchases/) |
| RN / Expo | [react-native-purchases](https://www.npmjs.com/package/react-native-purchases) (RevenueCat) | 10.10.2 | UI in `react-native-purchases-ui` |
| Capacitor / Cordova | [cordova-plugin-purchase](https://github.com/j3k0/cordova-plugin-purchase) | 13.18.0 | StoreKit 2 through the `cordova-plugin-purchase-storekit2` add-on |
| Capacitor | [@revenuecat/purchases-capacitor](https://www.npmjs.com/package/@revenuecat/purchases-capacitor) | 13.6.1 | |
| Capacitor | [@capgo/native-purchases](https://github.com/Cap-go/capacitor-native-purchases) | 8.8.1 | StoreKit 2 + PBL 7.x. Check PBL 8 support before you ship |
| Unity | [Unity IAP](https://docs.unity3d.com/Packages/com.unity.purchasing@5.4/changelog/CHANGELOG.html) | 5.4.3 | StoreKit 2; PBL 9.0.0 |
| KMP | [purchases-kmp](https://github.com/RevenueCat/purchases-kmp) (RevenueCat) | 3.10.1 | Adapty and Superwall also have KMP SDKs |

## 5. Other stores

| Store | Commission | API | Source |
|---|---|---|---|
| Microsoft Store | 12% games, 15% apps. Non-game apps may use their own commerce and keep 100% | Store APIs (`Windows.Services.Store`, not confirmed on the fetched page) | [MS Learn](https://learn.microsoft.com/en-us/windows/apps/publish/publish-your-app/why-distribute-through-store) |
| Steam | 30% / 25% / 20% tiers. Thresholds for microtransactions unconfirmed | Steamworks Microtransactions, `ISteamMicroTxn` | [docs](https://partner.steamgames.com/doc/features/microtransactions), [announcement](https://steamcommunity.com/groups/steamworks/announcements/detail/1697191267930157838) |
| Meta Quest | Set in the revenue-share agreement (unconfirmed publicly) | Platform SDK IAP, S2S Add-on APIs | [docs](https://developers.meta.com/horizon/documentation/unity/ps-monetization-overview/) |
