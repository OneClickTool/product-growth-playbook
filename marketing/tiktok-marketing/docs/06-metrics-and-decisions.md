# 06 · Metrics and the decision table

## What to log per post (after 48–72 hours)
| Column | Where | Why |
|---|---|---|
| views | TikTok analytics | Reach: is the hook pulling strangers? |
| saves, shares | TikTok analytics | Strong "I want this" signals |
| profile_visits | TikTok analytics (post → more data) | Did the CTA move people off the post? |
| link_clicks | Your UTM / link tool | Bio link traffic |
| installs | App Store Connect / Play Console (source = web referrer) or your attribution | Did they try it? |
| paid | RevenueCat / Stripe / store | The only number that pays rent |

Per-post installs are hard to attribute when you post several times a day. Use daily totals and compare days, or one
link per week. Put everything in [templates/post-log.csv](../templates/post-log.csv).

## The decision table (the "Larry loop")
From the Larry skill ([Stack Junkie](https://www.stack-junkie.com/blog/how-to-automate-tiktok-marketing-with-openclaw-larry-skill-deep-dive),
[ClawHub listing](https://clawhub.ai/OllieWazza/larry)):

| Views | Installs | Diagnosis | Change next |
|---|---|---|---|
| High | Low | People watch but don't act | **CTA slide** (5): name the app, one action, show the result again |
| Low | High (for its views) | The right people convert, too few see it | **Hook** (slide 1): new person / conflict |
| Low | Low | Both | New hook formula **and** new CTA, or a different niche angle |
| High | High | Working | Scale: 3 variations of this hook this week |
| — | Installs high, paid low | Not a TikTok problem | Onboarding or paywall → [monetization-paywall-design](../../../skills/monetization/monetization-paywall-design/SKILL.md) |

## Hook verdicts by views
The Larry skill's thresholds, for one consumer-app niche. Treat them as a starting rule and change the numbers once you
have 4 weeks of your own data:

| Views | Verdict |
|---|---|
| ≥ 50,000 | **Scale**: make 3–5 variations (same formula, new person/scene) |
| 10,000–49,999 | **Keep**: use again with a different scene |
| 1,000–9,999 | **Retest**: one more try with a new first line |
| < 1,000 twice | **Drop** the hook formula |

"High" and "low" for installs: compare to your own median. A post is "high" if its install-per-1K-views is above the
median of your last 20 posts. The [loop script](../skills/social-tiktok-slideshow-loop/scripts/slideshow_loop.py)
does this math.

## Stop rules
- **Three weeks, 20+ posts, no post over 10K views:** the niche angle is wrong, not the hooks. Go back to step 1
  of the loop with a different audience or product.
- **Views fine, zero installs after 2 weeks of CTA changes:** check the bio link on a phone, the store page
  ([aso-screenshot-strategy](../../../skills/aso/aso-screenshot-strategy/SKILL.md)), and that the slideshow shows the real app result.
- **Views drop to near zero on every post suddenly:** check the account's status and [07](07-rules-and-risks.md) before
  posting more.
