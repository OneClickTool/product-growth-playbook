# X analytics pattern: what daily posting + replies actually did

Real numbers from the maintainer's X account (indie dev, Mac apps and games, X Premium), X analytics screenshot taken
**2026-10-11**, 28-day window (Sep 14 → Oct 11). Totals are as X shows them. Per-day values are read off X's bar
charts, so they're approximate (±10%). Use this as a pattern to check your own account against, not as a promise.

## The 28-day totals

| Metric | Value | What it says |
|---|---|---|
| Impressions | 2K | ~80% of them came in the last 3 days |
| Engagement rate | 1.6% | 33 engagements / ~2K impressions |
| Engagements | 33 | |
| Likes | 18 | Weakest signal for ranking ([03-how-x-ranks-posts.md](../docs/03-how-x-ranks-posts.md)) |
| Replies received | 6 | |
| Bookmarks | 2 | |
| Reposts · Shares | 0 · 0 | Nothing yet that people want to send on |
| **Profile visits** | **7** | 0.35% of impressions: **the bottleneck** |
| Verified followers | 55 / 1.5K | |
| Active followers (24 h) | 352 / 1.5K | ~23% of followers were active that day: an audience is there |

## Three phases

| Phase | Days | Activity | Impressions / day | Follows |
|---|---|---|---|---|
| A · Silent | Sep 14 → Sep 30 | ~2 posts, ~2 replies in 17 days | ~0–10 (one ~30 spike on the day with 1 post + 2 replies) | ~+2 |
| B · Light | Oct 1 → Oct 8 | ~1–2 posts most days, a few replies | ~15–95 (avg ~45) | ~0 net |
| C · Daily routine | Oct 9 → Oct 11 | 3 → 5 → 6 posts, 5 → 7 → 9 replies a day | ~195 → ~855 → ~580 | ~+21, then ~+7 (a few unfollows) |

```text
activity / day      ▏ 0–1        ▏ 1–2          ▏ 8 → 15
impressions / day   ▏ ~5         ▏ ~45          ▏ ~200 → ~850
                      A silent      B light        C posts + replies
```

## What the pattern says

1. **Nothing in, nothing out.** Phase A: no posts, no reach. Followers alone don't bring impressions.
2. **Replies are the multiplier.** Phase C had roughly 4× the actions of phase B and about 10–15× the impressions per
   day. The days with the most replies were the days with the most reach. This matches the Premium reply lever in
   [06-reply-playbook.md](../docs/06-reply-playbook.md).
3. **Reach isn't the problem now, the profile is.** 2K impressions → 7 profile visits. Before doing more volume, fix
   the bio, banner and pinned post so a visit turns into a click
   ([social-x-profile-funnel](../skills/social-x-profile-funnel/SKILL.md)).
4. **Zero shares, zero reposts.** Shares weigh far more than likes. Add Wednesday posts people want to send to someone:
   checklists, tools, numbers ([05-post-formats.md](../docs/05-post-formats.md)).
5. **Speed has a price.** On the same day as the jump, X put a temporary reach label on the account (removed about
   2 hours later after review), and a profile photo change removed the checkmark until re-review. Ramp up over weeks,
   and never change photo / name / handle in a push week ([08-rules-and-risks.md](../docs/08-rules-and-risks.md),
   [02-profile-setup.md](../docs/02-profile-setup.md)).

## The routine to keep (from phase C, made safe)

| Daily | Target |
|---|---|
| Original posts | 1–3 (one good one beats five) |
| Replies to target accounts | 5–10, by hand, each adds a fact, number or screenshot |
| Answer replies on your own post | All, within 1 hour |
| Links | Bio or first reply only |
| Follows | Only people you'd actually reply to; no bursts |

Daily steps: [daily-flow.md](daily-flow.md).

## Next 4 weeks: targets, not results

> These are goals to work toward, set from the baseline above. They are not results and not a forecast.

| Metric | Baseline (28 d to 2026-10-11) | Target (28 d to 2026-11-08) |
|---|---|---|
| Impressions | 2K | 10K |
| Profile visits | 7 | 50 |
| Profile visits ÷ impressions | 0.35% | 0.5% |
| Bookmarks + shares + reposts | 2 | 15 |
| Link clicks → landing (`utm_source=x`) | not tracked | tracked every week |
| Temporary labels | 1 | 0 |

## Log (add a row every 4 weeks)

Copy the numbers from X analytics on the same weekday each time, so windows compare.

| 28 days to | Posts / day | Replies / day | Impressions | Eng. rate | Profile visits | Bookmarks + shares | Followers | Note |
|---|---|---|---|---|---|---|---|---|
| 2026-10-11 | ~1 (C: ~5) | ~1 (C: ~7) | 2K | 1.6% | 7 | 2 | 1.5K | Baseline. Started the daily routine Oct 9; label + checkmark review Oct 11 |
| 2026-11-08 | | | | | | | | |

Weekly numbers go in [templates/weekly-numbers.md](../templates/weekly-numbers.md); what to do when a number is
stuck: [07-metrics-and-stop-rules.md](../docs/07-metrics-and-stop-rules.md).
