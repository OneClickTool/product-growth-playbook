# 07 · Metrics and stop rules

Template: [templates/weekly-numbers.md](../templates/weekly-numbers.md). 10 minutes every Sunday.

## What to track (and where)

| Metric | Where | Healthy direction |
|---|---|---|
| Posts / replies written | your log | 7 posts, 35–70 replies a week |
| Impressions | X analytics | Rising slowly; don't optimise for it |
| Profile visits | X analytics | The real reach number |
| Link clicks | X analytics | ÷ profile visits = how good the bio/pin is |
| Landing visits `utm_source=x` | GA4 / Plausible / your analytics | ≈ link clicks (if far lower: slow or broken page) |
| Trials / installs | App Store Connect, Play Console, checkout | ÷ landing visits = landing quality |
| Paid | store / checkout | The only number that pays for Premium |

## Stop and fix rules
- **Profile visits flat for 3 weeks:** change who you reply to, not how much you post.
- **Visits up, clicks flat:** rewrite bio promise and pinned post.
- **Clicks up, trials flat:** landing doesn't match the pin, or the offer is unclear.
- **Trials up, paid flat:** paywall, price or trial length
  ([monetization-paywall-design](../../skills/monetization/monetization-paywall-design/SKILL.md)).
- **60 days, zero trials from X while visits grew:** pause the extra effort on X and fix offer/landing first.
- **Premium cost > X revenue after 90 days** and replies don't bring visits: downgrade the tier, keep posting.
