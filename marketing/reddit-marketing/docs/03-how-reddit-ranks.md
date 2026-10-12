# 03 · How Reddit ranks posts and comments, in plain words

Reddit doesn't publish its current ranking. What's public: the historical "hot" formula in Reddit's archived
open-source code, its rules and help pages. Raw notes and sources: [reference/reddit-facts.md](../reference/reddit-facts.md).
Labels: **Code** (Reddit's archived open-source code, may have changed), **Help** (Reddit's rules or help pages),
**Practice** (what builders see, test it yourself).

## Posts

| What | Label | What to do |
|---|---|---|
| "Hot" mixes votes and age. Votes count on a log scale: the first 10 upvotes weigh as much as the next 90 | **Code** | The first hour decides most of a post's life. Post when the subreddit is awake, and be there to answer |
| Age keeps pushing old posts down on a fixed clock | **Code** | A post has about a day in "hot". Don't delete and repost to "try again": that's spam |
| Each subreddit's AutoModerator removes posts by rules you can't see (account age, karma, links, keywords) | **Practice** | Read the rules and pinned posts first; check your post logged out after 10 minutes |
| Many subreddits require karma *in that subreddit* before you post | **Help** + subreddit rules | Comment there for 1–2 weeks first ([01-strategy.md](01-strategy.md)) |
| Flair and title format are often required | subreddit rules | Use the exact tag; wrong flair = removal |
| Upvote ratio and early comments signal a good post | **Practice** | End with a real question; answer every comment in the first hour |

## Comments
- **Code** · Comments are sorted by votes and age too ("best" / "top" / "new"). Early, useful comments rise to the
  top and stay there; a great answer 10 hours late is seen by few.
- **Practice** · Answer threads that are less than a few hours old and still getting views (sort a subreddit by *new*
  or *rising*), or old threads that rank in Google for a question you can answer: those keep getting readers.
- **Practice** · The top answer is usually the most *specific* one: steps, a number, a comparison, a screenshot.

## Karma
- **Help / Practice** · Karma is built from votes on your posts and comments, but Reddit doesn't publish the exact
  formula, and it isn't one point per upvote ([reference](../reference/reddit-facts.md#karma)).
- **Practice** · What matters is karma *in the subreddit* where you want to post, and account age. Total karma from
  joke comments elsewhere doesn't help you get past r/macapps' minimum.

## Things to stop believing
- "Post at 9am EST and you'll hit the front page." Each subreddit has its own busy hours; look at when its *new*
  queue moves.
- "Upvote your own post from another account." Vote manipulation: Rule 2, suspension.
- "Shadowbans are gone." Reddit replaced sitewide shadowbans with suspensions in 2015, but spam filters and subreddit
  AutoModerator can still hide what you post without telling you ([08-rules-and-risks.md](08-rules-and-risks.md)).
