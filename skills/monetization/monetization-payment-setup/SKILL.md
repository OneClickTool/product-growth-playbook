---
name: monetization-payment-setup
description: Pick a payment provider you can actually use from your country and get your first payout, in three levels (1 take a first real payment this week, 2 a proper checkout with verification done, 3 lower fees, local payments and taxes). Covers Stripe and why it doesn't work in Vietnam and many other countries, merchants of record (Paddle, Lemon Squeezy, Polar, Creem, Dodo Payments, Gumroad), App Store and Google Play payouts, local gateways (payOS, SePay, VNPay, MoMo), what documents and legal pages to prepare, and how long each review takes. Use when setting up payments, "how do I get paid", "Stripe not available in my country", "Stripe Vietnam", "Paddle vs Lemon Squeezy", "which payment provider for indie devs", "merchant of record", "Polar vs Creem", or before turning on paid plans.
license: MIT
metadata:
  category: monetization
  difficulty: beginner → intermediate (3 levels)
  time: "Level 1: 1-2 h · Level 2: 2-3 h + 1-14 days review · Level 3: ongoing"
  version: 1.0.0
  author: nvminhtu
---

# Payment Setup

> In one evening you'll know which provider works from your country, what it costs, what to prepare for
> verification, and you'll have a real payment link. In two weeks, a verified checkout and your first payout.

## Goal
Get paid before you "feel ready". Watching a real payment arrive, even $5, is the thing that turns a side project
into something you work on every night. Most builders put payments last, then lose weeks when Stripe says their country
isn't supported or a review asks for pages they don't have. This skill makes that a one-time, planned job.

## When to use
- Before you launch paid plans, or as soon as you have something people would pay for.
- Stripe isn't available in your country (for example Vietnam, Pakistan, the Philippines).
- You're choosing between Paddle, Lemon Squeezy, Polar, Creem, Gumroad and the rest.
- A payment provider rejected you or asked for more documents.
- **Not for:** what to charge → [monetization-pricing-strategy](../monetization-pricing-strategy/SKILL.md).
  What's free vs paid → [monetization-free-trial-vs-freemium](../monetization-free-trial-vs-freemium/SKILL.md).

## Inputs
- **Where you live and whose ID you hold.** Providers decide by the country of your ID and bank, not your customers.
- **Individual or company** (and which country the company is in).
- **What you sell and where:** mobile app, web SaaS, desktop app, browser extension, template/ebook, and whether buyers
  are mostly local or international.
- A bank account in your name. Optionally PayPal or Payoneer.
- A website (or at least a landing page) you control.
- `assets/payment-setup-sheet.md` and [references/payment-providers-by-country.md](references/payment-providers-by-country.md) from this skill.

## Step 0: Your product type decides half the answer

| You sell… | You must use | Choice left to you |
|---|---|---|
| Digital content or features **inside an iOS/Android app** | Apple In-App Purchase / Google Play Billing (store rules) | Code it yourself or use an SDK like RevenueCat → [monetization-in-app-purchase-setup](../monetization-in-app-purchase-setup/SKILL.md) |
| Web SaaS, desktop app, license keys, API | Nothing forced | A merchant of record (MoR) or a processor like Stripe |
| Browser extension | Nothing: Chrome Web Store payments were removed in 2020–2021 | Same as web. Say clearly that you, not Google, are the seller |
| Templates, ebooks, courses, files | Nothing forced | Gumroad or Payhip (store + checkout), or an MoR |
| To buyers **in Vietnam** paying in VND | Nothing forced | VietQR bank transfer via payOS or SePay, or VNPay / MoMo / ZaloPay |

**Merchant of record vs processor, in one line:** an MoR (Paddle, Lemon Squeezy, Polar, Creem, Dodo, Gumroad) is the
legal seller, so it collects and pays sales tax/VAT worldwide and handles chargebacks. It costs about 4–10%. A processor
(Stripe, PayPal) is cheaper per sale, but the tax is your job. **Solo and outside the US/EU? Start with an MoR.**

## Which provider can I use? (checked 2026-10-01)

| Provider | Type | Fee (headline) | Vietnam seller? | Review time | Payout min |
|---|---|---|---|---|---|
| Stripe | Processor | 2.9% + 30¢ US cards; +1.5% intl, +1% FX | ❌ | — | — |
| Stripe Managed Payments | MoR | Stripe fees + 3.5% | ❌ (US, CA, EU, UK, AU, JP, SG, HK… only) | Eligibility review | — |
| **Polar** | MoR | 5% + 50¢, +1.5% non-US cards (orgs from 27 May 2026) | ✅ | Up to 14 days (first review) | Not stated |
| **Creem** | MoR | 3.9% + 40¢ | ✅ | 24–72 h | $50 |
| **Dodo Payments** | MoR | 4% + 40¢; +1.5% intl, +0.5% subs | ✅ | 1–3 business days | $50 |
| Paddle | MoR | 5% + 50¢ | ⚠️ Not blocked, not confirmed | ID: instant–3 days · domain: auto or 5–7 days | $100 |
| Lemon Squeezy | MoR (owned by Stripe) | 5% + 50¢ + extras | ✅ | 2–3 business days | Not stated |
| **Gumroad** | MoR (since 2025) | 10% + 50¢ direct; 30% via Discover | ✅ (VND to your bank) | No upfront review; KYC later | $100 |
| PayPal (VN account) | Processor | 4.4% + $0.30 on payments from abroad | ✅ | — | 60,000đ fee per withdrawal |
| App Store | Store | 15% (Small Business Program) / 30% | ⚠️ Bank country not listed publicly | App review | ~$40 |
| Google Play | Store | 15% first $1M/yr; subs 15% | ✅ (USD wire) | ID verification | $100 |
| payOS / SePay | VN bank transfer (VietQR) | Free tier, then packages | ✅ (VND buyers) | CCCD / tax code only | Paid straight into your bank |

Full details, other countries (India, Indonesia, Philippines, Pakistan, Nigeria) and every source:
[references/payment-providers-by-country.md](references/payment-providers-by-country.md). **Fees change. Open the
pricing page before you decide.**

### What indie devs pick in 2026 (opinion, not data)
- **Web SaaS or desktop app, outside Stripe countries:** Polar or Creem. Both are MoRs built for developers, confirm
  Vietnam, and have short reviews. Dodo is a similar option. Paddle if you sell B2B and want the most established name.
- **Templates, ebooks, small files:** Gumroad. Zero setup, and payouts reach Vietnamese banks in VND.
- **Think twice about starting new on Lemon Squeezy.** Its own CEO wrote in January 2026 that support is slower,
  updates are fewer, and the plan is migration to Stripe Managed Payments, which isn't open to Vietnam.
- **Mobile subscriptions:** Apple/Google billing + RevenueCat.
- **In a Stripe country (US, EU, UK, SG…):** Stripe + Stripe Tax, or Stripe Managed Payments if you want MoR.

## Steps

### Level 1: A real payment this week (1–2 h)
The goal is proof, not a perfect setup.
1. **Pick the fastest path (5 min):** templates/files → Gumroad. Software → Creem or Polar. Local VN buyers →
   payOS or a SePay VietQR code.
2. **Create one product (20 min):** one price, one sentence of what they get, delivery (a file, a license key, or
   "access in 24 h by email" done by hand).
3. **Buy it yourself or ask a friend (10 min)** with a real card, then refund it. You've now tested checkout, receipt,
   delivery and refunds, and seen your net amount.
4. **Put the link where people already are:** your landing page, README, a reply to someone who asked for it.
5. **Write down the date and amount of your first real sale** in the setup sheet. That number is your motivation.

### Level 2: A proper checkout, verified (2–3 h of work + review time)
1. **Choose your main provider** with the table above and Step 0. Check the official country list yourself.
2. **Prepare the verification pack before you apply (60–90 min).** Reviews stall on missing pages far more than on ID:
   - Government ID (passport is safest), a selfie or liveness check, proof of address (bank statement or utility bill, recent).
   - Business documents if you have a company (for a Vietnamese household business: the business-household certificate).
   - **On your website, reachable from the footer:** what the product does, the price, Terms of Service with your
     legal name, a Refund policy, a Privacy policy, a contact email, HTTPS. Paddle's domain review checks them, and Creem approves faster when they're visible.
   - A product that works, or a clear demo. "Coming soon" pages get rejected.
   - A support email on your own domain if you can.
3. **Apply and note the date.** Typical reviews: Creem 24–72 h, Dodo 1–3 business days, Lemon Squeezy 2–3 business
   days, Paddle domain review auto or 5–7 business days, Polar up to 14 days.
4. **Set up payouts:** local bank where supported. Otherwise PayPal or Payoneer (Paddle pays to Payoneer; Gumroad
   doesn't). Wise can't hold money for Vietnam residents, so don't plan on Wise USD details.
5. **Connect the product:** checkout link or overlay, webhook → your app unlocks access, license key if desktop.
   Test in sandbox/test mode, then one real purchase and refund.
6. **App Store / Google Play:** accept the Paid Apps Agreement (Apple) / create the payments profile (Google, the
   country can't be changed later), add bank and tax info (W-8BEN for non-US individuals), and **enroll in both
   15% programs**. They are not automatic.

### Level 3: Lower fees, local money, taxes (ongoing)
- **A second provider for local buyers.** Vietnamese customers often prefer bank transfer: a VietQR via payOS or
  SePay costs far less than a card checkout. VNPay, MoMo and ZaloPay need business registration.
- **A US company when revenue justifies it.** Stripe Atlas ($500, then $100/year registered agent) gives you a
  Delaware LLC/C-corp and access to Stripe directly. That also brings US filing obligations; ask an accountant first.
- **Taxes at home.** Selling through an MoR solves your *customers'* tax, not yours. For Vietnam: households and
  individuals under 1 billion VND/year revenue pay no VAT/PIT from 2026, and Apple (2% PIT) and Google (5%) already
  withhold on sales to Vietnamese users. Rules changed in 2025–2026, so confirm with a local accountant.
- **Review fees every 6 months.** Providers changed pricing several times in 2025–2026 (Polar, Google Play, Apple EU).

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are a payments setup advisor for indie developers. Only recommend providers that accept sellers from my country,
and tell me to confirm on the provider's official supported-countries and pricing pages, because these change.

My country (ID + bank): {{e.g. Vietnam}}      Individual or company: {{...}}
What I sell: {{web SaaS / desktop app / mobile app / extension / template}}
Where buyers are: {{mostly international / mostly my country / both}}
Price and model: {{e.g. $9/month, $29 one-time}}     Expected sales in 6 months: {{...}}
Already have: {{website, legal pages, PayPal, Payoneer, company…}}

1. Say what the store rules force (Apple IAP / Google Play Billing) and what's my choice.
2. Recommend ONE main provider and ONE backup, with the reason. Prefer a merchant of record unless I'm in a Stripe
   country and willing to handle sales tax. Consider: Stripe, Stripe Managed Payments, Paddle, Lemon Squeezy, Polar,
   Creem, Dodo Payments, Gumroad, PayPal, and local gateways for my country.
3. Show what I keep per sale at my price for the main and backup provider, including payout fees.
4. Give me the verification checklist: documents, website pages (terms, refund, privacy, pricing, contact), and
   anything that commonly causes rejection for my product type.
5. Give a timeline: today, the review wait, first test purchase, first payout date.
6. List the tax questions I should ask an accountant in my country. Don't give tax advice yourself.
````

## Example output

> **Illustrative example.** A fictional Vietnamese solo developer; fees are from the providers' pricing pages on 2026-10-01.

*Markdown-to-PDF desktop app, $20 one-time, buyers mostly in the US/EU, developer is an individual in Vietnam.*

- **Main: Creem** (MoR, Vietnam supported, 24–72 h review). **Backup: Polar.** Gumroad as a 1-day fallback.
- Stripe ❌ (Vietnam not supported). Lemon Squeezy skipped (migrating to Stripe Managed Payments, not open to Vietnam).

| $20 sale | Fee | You keep (before payout fee) |
|---|---|---|
| Creem | 3.9% + $0.40 = $1.18 | $18.82 |
| Polar (new org, non-US card) | 5% + 1.5% + $0.50 = $1.80 | $18.20 |
| Gumroad (direct) | 10% + $0.50 = $2.50 | $17.50 |

| Day | Milestone |
|---|---|
| 1 | Gumroad product live; friend buys and gets refunded |
| 2 | Terms, Refund, Privacy pages in the site footer; apply to Creem |
| 4 | Creem approved; license keys + webhook tested in test mode |
| 5 | Real purchase + refund; Gumroad link replaced |
| 15 | First Creem payout to the Vietnamese bank |

## Common mistakes
- **Building payments last.** You finish the product, then wait two weeks for a review. Apply while you build.
- **Applying without legal pages.** Missing refund/terms/privacy pages is the most common reason for a delayed review.
- **Using a friend's account in a Stripe country.** It breaks the provider's terms; if it's found, the account can be
  frozen with your money in it.
- **Choosing by headline fee only.** Add international-card fees, subscription fees, payout and FX fees, and the
  tax work a processor leaves you.
- **Picking a provider that isn't growing.** Check its recent changelog and blog before you commit.
- **Not enrolling in Apple's and Google's 15% programs.** You pay 30% until you do.
- **Assuming "MoR" means "no taxes".** It covers your buyers' sales tax. Your own income tax at home is still yours.

## Related skills
- [monetization-pricing-strategy](../monetization-pricing-strategy/SKILL.md): set the price you'll put in the checkout.
- [monetization-in-app-purchase-setup](../monetization-in-app-purchase-setup/SKILL.md): building the purchase inside an iOS/Android app.
- [monetization-paywall-design](../monetization-paywall-design/SKILL.md): the screen before the checkout.
- [launch-pre-launch-checklist](../../launch/launch-pre-launch-checklist/SKILL.md): payments are one line of your launch checklist.
- [listing-digital-template](../../listing/listing-digital-template/SKILL.md): selling templates on Gumroad and Notion.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). All fees, countries and review times come from the providers'
official pages, listed in [references/payment-providers-by-country.md](references/payment-providers-by-country.md).
Checked 2026-10-01. Fees and country lists change often. Not legal or tax advice.
