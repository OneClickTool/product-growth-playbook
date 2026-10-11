# 03 · How X ranks posts, in plain words

Source: X's own For You code, [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) (checked 2026-10-11).
Raw numbers and caveats: [reference/x-algorithm-and-premium-facts.md](../reference/x-algorithm-and-premium-facts.md).

## The idea
For each person scrolling, X guesses how likely *they* are to like, reply, share, follow, mute or report your post.
Each guess is multiplied by a weight and added up. Higher score, higher in their feed. It's personal: the same post
scores differently for different people.

## What that means when you write

| Rule from the code | What to do |
|---|---|
| Copy-link share weighs 20, DM share 5 | Make posts people want to send to a friend: checklists, tools, a number that surprises |
| Reply 5, plus 15 between mutual follows | End with a real question; build mutual follows with peers your size |
| Quote 5 | Give a take people want to add to |
| Follow-from-post 4 | Every post should make clear what you're about |
| Like 0.5 | Likes are a weak signal; don't chase them |
| Open link 0.2 | Links are fine, but the post must be good without the click |
| Not interested −47.5, mute −58.8, block −31.2, report −234 | Repetition, bait and rage cost far more than they earn |
| Posts older than 48 h are filtered out | A post has two days. Repurpose good ones later with new words |
| Author diversity decay | One strong post a day beats five weak ones |
| New-author boost | Small accounts get a chance; make the first posts count |
| Out-of-network discount | Turning viewers into followers matters; replies help you meet them |

## What the code does not say
- It doesn't show Premium boosting your posts in For You. Premium's documented reach feature is **reply
  prioritization** ([About X Premium](https://help.x.com/en/using-x/x-premium)).
- The repo shows defaults; production can run other values in experiments.
- "Hashtags are penalized", "posting at 9am is magic", "external links kill reach by 50%": none of these numbers
  are in the code. Test on your own account instead.
