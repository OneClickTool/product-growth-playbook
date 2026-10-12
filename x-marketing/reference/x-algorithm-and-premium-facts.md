# X ranker and X Premium: what is confirmed

Everything here comes from X's own code or help pages, checked **2026-10-11**. X changes both often; re-check
before you quote a number publicly.

## The For You ranker

Source: [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) (Apache-2.0).

**How a feed is built** (README, *Overview* and *Scoring and Ranking*):
- Candidates come from accounts the viewer follows (Thunder) and from accounts they don't (Phoenix retrieval,
  SimClusters, a shared popular-posts list). Both are ranked by the same model.
- The model reads the viewer's recent engagement history and predicts a probability for each action.
  `Final Score = Σ (weight × P(action))`.
- The README warns: weights multiply the *predicted probability* for that viewer, not raw counts. "1 report cancels
  468 likes" is the wrong reading.

**Default weights** in `home-mixer/params/param.rs` (the README notes production may run different values via
experiments):

| Action | Weight |
|---|---|
| Share via copy link | 20.0 |
| Reply · quote · share via DM | 5.0 · 5.0 · 5.0 |
| Bidirectional-follow reply boost | 15.0 |
| Follow author | 4.0 |
| Share | 2.0 |
| Retweet | 1.0 |
| Favorite (like) | 0.5 |
| Click dwell time (continuous) | 0.4 |
| Click · open link | 0.3 · 0.2 |
| Video open · photo expand · dwell | 0.07 · 0.05 · 0.05 |
| Profile click · video quality view | 0.0 · 0.0 |
| Not dwelled | −0.02 |
| Block author · not interested · mute author | −31.2 · −47.52 · −58.8 |
| Report | −234.0 |

**Adjustments after scoring:** author diversity (each extra post by the same author is multiplied by a decaying
factor down to a floor); out-of-network discount (posts from accounts the viewer doesn't follow, and replies/reposts
from accounts they do, get a factor below 1); new-author boost (authors under an impressions threshold are lifted
toward a target position).

**Filters that matter to a poster:** posts older than **48 hours** are removed (`AgeFilter`); already-seen posts are
removed; for new accounts, out-of-network posts below an engagement threshold are removed
(`NewUserMinEngagementFilter`); a visibility-filtering layer can drop posts using labels from spam/inauthenticity
models. The **Under the Hood** tool (README) shows aggregate labels on your account and posts that can limit reach.

**What this does not tell you:** the production values of every experiment, or anything about Premium boosting
ranking in For You. Don't claim either.

## X Premium

Source: [About X Premium](https://help.x.com/en/using-x/x-premium).

| Tier | US price (web) | Features that matter for growth |
|---|---|---|
| Basic | $3/mo · $32/yr | Edit post (1 hour), longer posts (up to 25,000 characters), longer video, reply prioritization, text formatting, bookmark folders, create a Community |
| Premium | $8/mo · $84/yr | All Basic + blue checkmark (after review), **larger** reply prioritization, ~50% fewer ads, Media Studio, apply for Creator Subscriptions and Original Content Rewards, ID verification |
| Premium+ | $40/mo · $395/yr | All Premium + **largest** reply prioritization, no ads in most places, Radar Search, X Pro, SuperGrok |

Articles: listed under Premium+ on the help page when it was checked, but X opened them to all Premium tiers on
2026-01-07 ([X Creators](https://x.com/XCreators/status/2012306734568849653)); check your own composer.

Notes from the same page: prices are local and change; changing your photo, display name or @handle removes the
checkmark until it's reviewed again; Original Content Rewards pay on qualified impressions from Premium users;
Creator Subscriptions have their own eligibility rules (see the Monetization tab in the app).

Third-party studies claim Premium accounts get much more reach. They are not X data and mix cause and effect
(people who pay also post more); treat them as unproven.

How to use these facts day to day: [docs/03-how-x-ranks-posts.md](../docs/03-how-x-ranks-posts.md) and the
[30-day Premium plan](../docs/04-premium-30-day-plan.md).
