# 06 · Post variants: 10 kinds of Reddit post

A post is a bigger bet than a comment: one per subreddit per month at most, often less. Pick the variant that fits
the subreddit's rules and readers, then write it against that subreddit's page in
[docs/subreddits](../../../docs/subreddits/README.md). Title and body formulas, and the rules script:
[launch-reddit-posting](../../../skills/launch/launch-reddit-posting/SKILL.md). File format:
[templates/post-file.md](../templates/post-file.md).

| # | Variant | Fits | Readers | Link |
|---|---|---|---|---|
| R01 | **Showcase: "I made…"** | Showcase subreddits (r/macapps, r/MacOSApps, r/SideProject…) | buyers / builders | In post, if allowed |
| R02 | **Build story: "How I built…"** | Developer subreddits (r/SwiftUI, r/webdev, r/gamedev…) | builders | End of post or comment |
| R03 | **Lesson with real numbers** | r/indiehackers, r/SaaS, r/EntrepreneurRideAlong | builders | Usually none |
| R04 | **Honest comparison / alternatives** | Buyers' subreddits, "best app for…" style | buyers | None, or yours disclosed among others |
| R05 | **Feedback or beta testers wanted** | r/alphaandbetausers, r/SideProject, some niche subs | builders / early adopters | Yes, it's the point |
| R06 | **Deal / promo codes** | Deal subreddits (r/AppHookup…) during a real price drop | buyers | Yes, in the required format |
| R07 | **Weekly-thread drop** | Subreddits with a self-promotion megathread | buyers | Yes, inside the thread only |
| R08 | **Tutorial without your product** | Audience subreddits that ban promotion | buyers | None |
| R09 | **Milestone / case study** | Builder subreddits, once you have real results | builders | Usually none |
| R10 | **AMA (ask me anything)** | Only with moderator approval, when you have a story people want | either | In the intro |

On r/macapps, "alternative to / comparison" posts had the highest average score in one third-party analysis of 496
top posts ([upvote.net, 2026](https://upvote.net/blog/macapps-reddit-analysis)). Treat it as a hint, not a law.

## Templates

**R01 · Showcase**
```text
Title: I made [what it is] that [does one specific thing] for [who]

[1–2 lines: the problem, in your own words]
[What it does: 3–5 bullets, concrete verbs]
[Demo GIF / screenshots]
Price: … · Platform: … · Privacy: … (only if true)
I'm the developer, [one line about you]. [A real question: what's missing? would you pay for X?]
```

**R02 · Build story**
```text
Title: How I [solved a technical problem] in [stack] (with code)

[The problem in one paragraph] → [what didn't work] → [what worked, with a code snippet] → [one lesson]
The app this is from: [name, one line] (link at the end or in a comment)
```

**R03 · Lesson with real numbers**
```text
Title: [N weeks / users / $] in: what worked and what didn't for [what you make]

[Context: what, for whom, since when] · [3 things that worked, each with a number and its base]
[2 things that didn't] · [what you'd do differently] · [question for readers]
```

**R04 · Honest comparison**
```text
Title: I tried [N] [kind of app] for [job]: here's what each is good at

[App A: best at / weak at / price] … [App B] … [App C]
[Who should pick which] · Disclosure if one is yours: "I make C, so weigh my take on it."
```

**R05 · Feedback / beta**
```text
Title: Looking for [N] [who] to test [what it does] (free, [platform])

[What it is in one line] · [what you need from testers, exactly] · [what they get: free Pro, credit]
[How to join: link / TestFlight / reply] · I'm the developer.
```

**R06 · Deal**: follow the subreddit's title tag exactly (price before/after, platform, end date). Only real,
time-limited drops.

**R07 · Weekly-thread drop**
```text
[Name] — [one line: who it's for, what it does] · [price] · [platform] · [link with UTM] · I'm the dev.
```

**R08 · Tutorial without your product**
```text
Title: [Platform] tip: [result] in [N] steps, no app needed
[Steps with exact menu names, a screenshot] · [one gotcha] · no link
```

**R09 · Milestone / case study**: the [case study template](../../../skills/case-study/case-study-write-your-own/SKILL.md),
shortened: context, baseline, what you did, before/after numbers, what failed.

**R10 · AMA**: message the moderators first with your story and proposed date; the intro says who you are, what you
built, and what people can ask about. Stay for hours, answer everything.

## Order to try them (first 2 months)
Weeks 1–2 comments only → R08 tutorial (no product) → R02 build story → R01 showcase in the easiest showcase
subreddit → R05 feedback → R01 in the main buyers' subreddit (your best post, once a month) → R03 / R09 when you have
numbers. R06 only during a real sale; R10 only when you have an audience.
