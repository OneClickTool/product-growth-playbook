# Reddit Marketing for Indie Devs

> Part of [Marketing & Social](../README-marketing-social.md): every channel kit and how they link to each other.

![A maker answers a question at one table in a busy town square, and people walk up to the maker's small shop](../../docs/images/illustrations/14-reddit-kit-hero.jpg)

**Answer first, post later, and let your profile do the selling.** On Reddit, people ask in public for exactly the
tool you built. A useful answer from a real account earns trust, the profile turns curious readers into visitors,
and a few strong posts a month reach the rest. Everything here cites Reddit's own rules and help pages, or is
labelled as practice to test.

```text
thread where someone asks  →  useful answer (no link)  →  your profile  →  X / landing  →  free trial  →  paid
                         ↘  later: one strong post per subreddit, in its format, on its day
```

## One command

```text
/social-reddit today          → 15-minute plan: threads to answer today + one post if it's your post day
/social-reddit find <topic>   → where people ask about it: subreddits, searches, alerts to set
/social-reddit reply <thread> → paste a thread, get an answer worth upvoting (+ whether to mention your app)
/social-reddit post <sub>     → one post for that subreddit, written to its rules and format
/social-reddit rules <sub>    → the subreddit's current rules (wiki page or fetch script)
/social-reddit profile        → username, avatar, bio, social links with UTM
/social-reddit numbers        → weekly table: answers, posts, removals, landing visits, trials
/social-reddit risk           → removed, banned, shadowbanned? what happened and what to do
```

Router skill: [social-reddit](skills/social-reddit/SKILL.md). Installed as a plugin the command is
`/product-growth-hack:social-reddit today`; or copy the `skills/social-reddit*` folders into `~/.claude/skills/`.

## Start in 3 steps
1. **Today (20 min):** set up the profile: avatar, one-line bio, social links to X and your landing page with UTM
   → [docs/02-profile-setup.md](docs/02-profile-setup.md).
2. **This week (15 min a day):** comments only. Find 2–3 threads a day where someone asks for what you know, and
   answer without a link → [flow/daily-flow.md](flow/daily-flow.md) ·
   [social-reddit-comment](skills/social-reddit-comment/SKILL.md).
3. **From week 3:** one post a week, one subreddit at a time, easiest first →
   [docs/06-post-variants.md](docs/06-post-variants.md) and the per-subreddit pages in
   [docs/subreddits](../../docs/subreddits/README.md).

## What's in this folder

| Folder | What's inside |
|---|---|
| [docs/](docs/01-strategy.md) | The method, one topic per file (below) |
| [flow/](flow/daily-flow.md) | The 15-minute daily routine, the weekly post and the monthly rules check |
| [skills/](skills/README.md) | [social-reddit](skills/social-reddit/SKILL.md) (router) · [social-reddit-comment](skills/social-reddit-comment/SKILL.md) (answers) |
| [templates/](templates/post-file.md) | [Post file](templates/post-file.md) · [comment file](templates/comment-file.md) · [thread tracker](templates/thread-tracker.md) · [weekly numbers](templates/weekly-numbers.md) |
| [reference/](reference/reddit-facts.md) | Facts with sources: rules, spam, karma, ranking, social links, Reddit Pro, ads |

Already in the main library, used by this kit:
[launch-reddit-posting](../../skills/launch/launch-reddit-posting/SKILL.md) (subreddits by product type, the rules
script, title and body formulas) · [docs/subreddits](../../docs/subreddits/README.md) (one page per subreddit) ·
[research-where-users-ask](../../skills/research/research-where-users-ask/SKILL.md) (where people ask for software).

## Docs, in reading order
1. [Strategy: comments first, posts later](docs/01-strategy.md)
2. [Profile setup](docs/02-profile-setup.md)
3. [How Reddit ranks posts and comments, in plain words](docs/03-how-reddit-ranks.md)
4. [Finding the threads worth answering](docs/04-finding-threads.md)
5. [Comment playbook](docs/05-comment-playbook.md)
6. [Post variants: 10 kinds of Reddit post](docs/06-post-variants.md)
7. [Metrics and stop rules](docs/07-metrics-and-stop-rules.md)
8. [Rules and risks](docs/08-rules-and-risks.md)

## Five things to remember
- Each subreddit is its own country with its own rules. Read them before every first post there.
- Say you're the developer, every time. "I found this cool app" about your own app is how accounts get banned.
- Ten good answers are worth more than one launch post. Answers stay findable in search for years.
- One post per subreddit per month is plenty. Different post, different subreddit, different day.
- UTM on every link (`utm_source=reddit`), or you'll never know which subreddit sends buyers.
