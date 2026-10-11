# Revenue screenshots and scams on X: how to check

X is full of "$X in 30 days" screenshots. Some are real, some are sandbox purchases, some are edited, and some exist
to sell a course. You can't prove a screenshot is real, so judge the **source**, not the image. Checked 2026-10-11.

## 1 · Check the screenshot itself (2 min)

| Check | Real-looking | Red flag |
|---|---|---|
| Math | Day totals equal the rows; currency and decimals consistent | Totals that don't add up; mixed formats |
| Tool UI | Matches the real app (RevenueCat, App Store Connect, Stripe) today: fonts, badges, spacing | Old UI, odd font in the numbers only, blurry numbers but sharp UI |
| Size | Small, uneven amounts, gaps between dates, local-price conversions ($3.21, $5.80) | Round, smooth, every day up and to the right |
| Context | Shows the boring parts: refunds, empty days, churn | Only the best day, cropped dates, no app name |
| Sandbox | — | RevenueCat and Stripe both have a test / sandbox view; a test purchase looks the same in a screenshot ([RevenueCat sandbox](https://www.revenuecat.com/docs/test-and-launch/sandbox)) |
| One buyer | Many countries and times | Several purchases from one country within minutes can be one person, or the dev testing |

None of these proves anything. They only tell you how much weight to give it.

## 2 · Check the source (5 min)

| Check | How |
|---|---|
| Is the product real and findable? | Search the store; look at ratings count, release date, last update. No app name = no proof |
| Verified revenue | [TrustMRR](https://trustmrr.com) reads revenue through a read-only key from Stripe, LemonSqueezy, Polar or DodoPayment ([terms](https://trustmrr.com/terms)). A founder who's really doing well often links a verified page. App Store revenue isn't covered there |
| Account history | On a profile, tap "Joined …" → **About this account**: country, join date, number of @handle changes (rolled out Nov 2025, [TechCrunch](https://techcrunch.com/?p=3070014)). New account + many handle changes + "growth guru" = careful |
| What they sell | Course, paid community, "DM me", agency, affiliate link? The screenshot is the ad. Fine, but it's marketing, not data |
| Track record | Scroll back 3 months: same products, same story, numbers that grow plausibly? Or a new "I made $10K" every week with a new app |

## 3 · Scams that target indie devs on X

| Pattern | What it looks like | Do |
|---|---|---|
| "Promotion" sellers | "Love your app! I can promote it to 200K followers for $X" in replies or DMs | Ignore. Bought promotion is usually bots, and paid endorsements must be disclosed ([FTC](https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking)) |
| Reviews / ratings for sale | "5-star reviews, real users" | Never. Against [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) (manipulating reviews), can get you removed |
| Fake acquirer / investor | "We want to buy your app" → asks for App Store Connect access, a "valuation fee" or a file to download | Only through escrow or a known marketplace; never pay a fee up front, never share logins or download their files |
| Fake support / copyright | DM "your account will be suspended, verify here" | Treat any DM with a login or "verify" link as phishing. Log in only by typing x.com yourself |
| Engagement farms | "Drop your link, follow everyone who likes" | Engagement spam under the [Authenticity policy](https://help.x.com/en/rules-and-policies/authenticity); see [06-reply-playbook.md](../docs/06-reply-playbook.md#what-are-you-building-posts-drop-your-link-or-not) |
| "Copy my system" courses | Screenshot → "the exact playbook, $99" | Ask for verified revenue first. Most of it is free in places like this repo |

## 4 · Keep motivation from real numbers

- Compare yourself with **your own last 4 weeks** ([templates/weekly-numbers.md](../templates/weekly-numbers.md)),
  not with someone's best day.
- For a market picture, use reports built from many apps' data, e.g. RevenueCat's yearly
  [State of Subscription Apps](https://www.revenuecat.com/state-of-subscription-apps/), not single screenshots.
- A list of $1–8 purchases with empty days in between is what a real small app's transactions look like when someone
  shows the whole list. If yours looks like that, you're on the same road, not behind it.
- Posting your own real numbers, small ones included, is what builds trust with you ([talk bank E](../posts/talk-bank.md)).
