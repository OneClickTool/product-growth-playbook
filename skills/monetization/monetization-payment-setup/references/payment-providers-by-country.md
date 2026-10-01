# Payment providers by country: research notes

The source file behind [monetization-payment-setup](../SKILL.md). Every fact links to the provider's own page.
**Checked 2026-10-01.** "Unconfirmed" means no official page confirmed it. Re-check before you rely on it, and
update this file (with the date) when something changes.

## 1. Web checkout: merchants of record and processors

| Provider | Type | Headline fee | Vietnam | India · Indonesia · Philippines · Pakistan · Nigeria |
|---|---|---|---|---|
| [Stripe](https://stripe.com/pricing) | Processor (Stripe Tax is an add-on) | 2.9% + 30¢ US cards; +1.5% intl cards, +1% FX | ❌ Not listed ([global](https://stripe.com/global)) | IN, ID "preview" (contact sales); PH, PK not listed; NG via Paystack |
| [Stripe Managed Payments](https://stripe.com/managed-payments) | MoR | Stripe fees + 3.5% | ❌ | None. Only US, CA, EU/EEA, GB, CH, NO, LI, AU, HK, JP, SG ([eligibility](https://docs.stripe.com/payments/managed-payments/eligibility)) |
| [Paddle](https://www.paddle.com/pricing) | MoR | 5% + 50¢; custom pricing under $10 | ⚠️ Not on the blocked list, not confirmed ([countries](https://www.paddle.com/help/start/intro-to-paddle/which-countries-are-supported-by-paddle)) | None of the five blocked |
| [Lemon Squeezy](https://www.lemonsqueezy.com/pricing) | MoR (Stripe-owned) | 5% + 50¢, extra fees in some cases | ✅ Bank payouts ([countries](https://docs.lemonsqueezy.com/help/getting-started/supported-countries)) | ID, PH, PK, NG bank; IN PayPal only |
| [Polar](https://polar.sh/docs/merchant-of-record/fees) | MoR | Orgs from 27 May 2026: 5% + 50¢, +1.5% non-US cards. Older orgs: 4% + 40¢ (+0.5% subs) | ✅ ([countries](https://polar.sh/docs/merchant-of-record/supported-countries)) | All five |
| [Creem](https://www.creem.io/pricing) | MoR | 3.9% + 40¢ | ✅ ([countries](https://docs.creem.io/merchant-of-record/supported-countries)) | All five (PK: bank-partner limits) |
| [Dodo Payments](https://dodopayments.com/pricing) | MoR | 4% + 40¢ US; +1.5% intl, +0.5% subs, +3% PayPal/BNPL | ✅ ([countries](https://docs.dodopayments.com/miscellaneous/accepted-countries-and-territories)) | IN, ID, PH yes; PK not listed; NG existing accounts only |
| [Gumroad](https://gumroad.com/pricing) | MoR since 1 Jan 2025 | 10% + 50¢ direct; 30% via Discover | ✅ VND to local bank ([getting paid](https://gumroad.com/help/article/13-getting-paid)) | All five, local bank |
| [FastSpring](https://fastspring.com/pricing/) | MoR | Quote only (unconfirmed) | Unconfirmed | Unconfirmed |
| [PayPal Vietnam](https://www.paypal.com/vn/webapps/mpp/merchant-fees) | Processor | 4.40% + fixed ($0.30 USD) on payments from abroad (page updated 28 May 2026) | ✅ Withdraw to VN bank, 60,000đ; conversion adds 4% | Unconfirmed |
| [Payhip](https://payhip.com/pricing) | Store; handles EU/UK VAT and US/CA sales tax only ([tax](https://help.payhip.com/article/127-digital-eu-vat)) | Free plan 5%; Plus $29/mo + 2%; Pro $99/mo + 0%; PayPal/Stripe fees extra | Via PayPal; Vietnam needs a **business** PayPal account ([help](https://help.payhip.com/article/64-connecting-your-paypal-account)) | Via PayPal |

## 2. Payouts

| Provider | Methods | Minimum · schedule | Source |
|---|---|---|---|
| Paddle | Wire, Payoneer, Wise-style bank details (PayPal unconfirmed) | $100 · created on the 1st, sent by the 15th; $15 SWIFT fee in some countries | [how you get paid](https://www.paddle.com/help/manage/get-paid/when-and-how-do-i-get-paid) |
| Lemon Squeezy | Bank or PayPal | Unconfirmed | [countries](https://docs.lemonsqueezy.com/help/getting-started/supported-countries) |
| Polar | Stripe Connect Express | Not stated · Stripe payout fees passed on: $2/month with payouts, 0.25% + $0.25 per payout, 0.25–1% cross-border | [fees](https://polar.sh/docs/merchant-of-record/fees) |
| Gumroad | Local bank (local currency) or PayPal USD (2%); no Payoneer/Wise/wire | $100 · daily, weekly, monthly or quarterly; sales held ≥ 7 days on non-daily schedules | [getting paid](https://gumroad.com/help/article/13-getting-paid) |
| Creem | Bank (7 USD/EUR or 1%, whichever is higher) or USDC on Polygon (2%) | $50 · 1st and 15th | [payouts](https://docs.creem.io/merchant-of-record/finance/payouts) |
| Dodo | Bank; free normally, $5 under $1,000, $25 USD SWIFT | $50 (fixed) · twice a month | [payout structure](https://docs.dodopayments.com/features/payouts/payout-structure) |
| FastSpring | Wire, PayPal, ACH, check (Hyperwallet portal) | You set it | [payouts portal](https://developer.fastspring.com/docs/fastspring-payouts-portal) |
| Payhip | Straight to your PayPal/Stripe after each sale | — | [pricing](https://payhip.com/pricing) |

## 3. Verification: what they ask for and how long it takes

| Provider | What's checked | Typical time | Source |
|---|---|---|---|
| Paddle | ID via Sumsub (ID, proof of address, sometimes liveness video); sometimes business ownership. Domain review: product description, pricing, T&Cs with your legal name, refund policy, privacy policy, HTTPS | ID: instant to 1–3 business days. Domain: mostly automatic, manual 5–7 business days | [identity](https://www.paddle.com/help/start/account-verification/what-is-identity-verification), [domain](https://www.paddle.com/help/start/account-verification/what-is-domain-verification) |
| Lemon Squeezy | Business questionnaire + government ID | 2–3 business days | [activate your store](https://docs.lemonsqueezy.com/help/getting-started/activate-your-store) |
| Polar | ID + selfie via Stripe Identity | First review up to 14 days | [account reviews](https://polar.sh/docs/merchant-of-record/account-reviews) |
| Creem | KYC; KYB if you have a company; payout account. Faster when the product is live and legal pages are visible | 24–48 h, up to 72 h | [account reviews](https://docs.creem.io/merchant-of-record/account-reviews/account-reviews) |
| Dodo | Government ID + business registration, manual review; eligibility depends on the ID's country | 1–3 business days | [verification](https://docs.dodopayments.com/miscellaneous/verification-process) |
| Gumroad | KYC (via Stripe) once you pass time/sales thresholds | — | [getting paid](https://gumroad.com/help/article/13-getting-paid) |
| Stripe Managed Payments | Business eligibility review; direct integration only; fully automated digital product with a tax code | Unconfirmed | [eligibility](https://docs.stripe.com/payments/managed-payments/eligibility) |

## 4. App stores

**Apple App Store**
- 30% standard; **15%** in the [Small Business Program](https://developer.apple.com/app-store/small-business-program/)
  (≤ $1M proceeds last year, or new). Enroll as Account Holder after accepting the Paid Apps Agreement; 15% starts
  15 days after the end of the fiscal month you're approved.
- To be paid: Paid Apps Agreement, [bank info](https://developer.apple.com/help/app-store-connect/manage-banking-information/enter-banking-information/),
  [tax forms](https://developer.apple.com/help/app-store-connect/manage-tax-information/provide-tax-information/) (W-8BEN etc.),
  and the [minimum threshold](https://developer.apple.com/help/app-store-connect/reference/reporting/minimum-payment-threshold)
  ($40 default for countries not in Apple's table; Vietnam isn't in it). Paid within 45 days of the fiscal month end
  ([overview](https://developer.apple.com/help/app-store-connect/getting-paid/overview-of-receiving-payments/)).
- Vietnamese bank accounts: **unconfirmed** on a public page (you pick the country in App Store Connect).
- No US–Vietnam tax treaty in force ([IRS list](https://www.irs.gov/businesses/international-businesses/united-states-income-tax-treaties-a-to-z)).
- Vietnam storefront taxes from Aug 2025: individual developers in Vietnam have 2% PIT withheld, plus 5% FCT on
  Apple's commission ([Apple news](https://developer.apple.com/news/?id=yo2104n5)).
- US storefront allows external purchase links since 1 May 2025 ([Apple news](https://developer.apple.com/news/?id=9txfddzf)).
  EU: new unified terms from 1 Oct 2026 ([DMA page](https://developer.apple.com/support/dma-and-apps-in-the-eu/)).

**Google Play**
- 15% on the first $1M per year **if you enroll**; auto-renewing subscriptions 15%
  ([service fees](https://support.google.com/googleplay/android-developer/answer/112622)). New tiers for users in
  the EEA, UK, US (from 30 Jun 2026), Australia and Japan (from 30 Sep 2026) are on the same page.
- Enroll: Account Group → declare associated accounts → Review and enroll ([help](https://support.google.com/googleplay/android-developer/answer/10632485)).
- Payments profile: legal name, physical address, bank in the same country; **country can't be changed later**
  ([help](https://support.google.com/googleplay/android-developer/answer/7161426)). Personal accounts verify with
  government ID; organizations need a D-U-N-S number ([help](https://support.google.com/googleplay/android-developer/answer/13628312)).
- Vietnam **is supported** for developer and merchant registration ([countries](https://support.google.com/googleplay/android-developer/answer/9306917)),
  paid by USD wire with a **$100 minimum** ([payouts](https://support.google.com/googleplay/android-developer/answer/2700656)).
- Vietnam: Google withholds **5%** on gross sales to Vietnamese users for individual/household developers and needs
  your Vietnam tax code ([help](https://support.google.com/paymentscenter/answer/9384608)).

**RevenueCat:** SDK + backend for in-app subscriptions; Apple/Google still pay you. Free up to $2,500 monthly tracked
revenue, then 1% ([pricing](https://www.revenuecat.com/pricing/)).

**Chrome Web Store:** paid items were removed (no new paid items from 21 Sep 2020, charging stopped 1 Feb 2021,
[notice](https://groups.google.com/a/chromium.org/g/chromium-extensions/c/XLeZ6iKiuVI)). If you charge, the policy
requires you to say you are the seller and publish terms of sale ([policy](https://developer.chrome.com/docs/webstore/program-policies/accepting-payment/)).

## 5. Vietnam: local gateways for VND buyers

| Gateway | Who can register | Fee | Source |
|---|---|---|---|
| payOS (VietQR, bank to bank) | Individual, household business or company; CCCD or tax code, no business licence | Free tier; paid packages or a % "Flex" plan | [payos.vn](https://payos.vn/thu-tuc-dang-ky-cong-thanh-toan/) |
| SePay (bank API + VietQR) | Individual, household business or company | Free: 50 transactions/month; paid from 120,000đ/month | [pricing](https://sepay.vn/bang-gia.html) |
| VNPay | Company or household business (licence, representative ID, premises photos, bank account); 5–10 working days | Not public | [register](https://vnpay.vn/dang-ky-qr-thanh-toan-ho-kinh-doanh-0py2hr0eb3ja) |
| MoMo Business | Merchant profile on the M4B portal; households verified by eKYC + business licence | Not public | [onboarding](https://developers.momo.vn/v3/vi/docs/payment/onboarding/merchant-profile/) |
| ZaloPay | Business account; documents reviewed in about 2 working hours (5–7 days for special sectors) | Not public | [zalopay.vn](https://zalopay.vn/hop-tac-doanh-nghiep) |

## 6. Receiving money from abroad (Vietnam residents)

- **PayPal:** receive at 4.40% + fixed fee, withdraw to a VN bank for 60,000đ ([fees](https://www.paypal.com/vn/webapps/mpp/merchant-fees)).
- **Payoneer:** receiving accounts in 13 currencies incl. USD; $29.95/year if you receive < $6,000 in 12 months; 1% to
  receive in a non-local currency; 1.2–4% to withdraw with conversion ([pricing](https://www.payoneer.com/pricing/)).
  Paddle pays to Payoneer; Gumroad doesn't. Withdrawing VND to a Vietnamese bank: unconfirmed on an official page.
- **Wise:** Vietnam is **not** on the list of countries whose residents can hold money
  ([help](https://wise.com/help/articles/2813542/where-do-i-need-to-live-to-hold-money-with-wise)). Sending *to* VND works.
- **Stripe Atlas:** $500 one-time (+$100/year registered agent after year 1) for a Delaware C-corp or LLC, EIN and
  paperwork; open to founders in 175+ countries ([atlas](https://stripe.com/atlas), [terms](https://stripe.com/legal/atlas)).
  It creates US tax filing duties; talk to an accountant.

## 7. Vietnam tax: high level, not advice

- Decree 117/2025/NĐ-CP (from 1 Jul 2025): e-commerce and digital platforms with a payment function withhold tax for
  households and individuals ([baochinhphu.vn](https://baochinhphu.vn/quy-dinh-quan-ly-thue-doi-voi-ho-ca-nhan-kinh-doanh-tren-nen-tang-thuong-mai-dien-tu-102250611153921023.htm),
  [EY summary](https://www.ey.com/vi_vn/technical/tax/tax-and-law-updates/tin-nhanh-tu-van-thue-nhan-su-thang-6-nam-2025-nghi-dinh-117-ve-quan-ly-thue-doi-voi-hoat-dong-kinh-doanh-tren-nen-tang-thuong-mai-dien-tu-nen-tang-so)).
- From 1 Jan 2026: households and individuals with revenue up to **1 billion VND/year** pay no VAT or PIT; lump-sum
  tax is replaced by self-declaration ([baochinhphu.vn](https://baochinhphu.vn/chinh-thuc-nang-nguong-chiu-thue-voi-ho-kinh-doanh-len-01-ty-dong-nam-ap-dung-tu-1-1-2026-102260429185517215.htm)).
- How to declare income from foreign MoRs (Gumroad, Polar, Creem…) as an individual: **unconfirmed**; ask a local accountant.

## Notable changes 2024–2026
- Stripe bought Lemon Squeezy (July 2024). In January 2026 its CEO wrote that support is slower, updates are fewer,
  and migration to Stripe Managed Payments is the goal ([2026 update](https://www.lemonsqueezy.com/blog/2026-update)).
- Gumroad became merchant of record on 1 Jan 2025.
- Polar changed pricing for organizations created from 27 May 2026 ([plans](https://polar.sh/blog/introducing-polar-plans)).
- Stripe India has been invite-only for new accounts since May 2024 (per Lemon Squeezy's countries page).
