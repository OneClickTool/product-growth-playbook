# Medium Marketing for Indie Devs

> Part of [Marketing & Social](../README-marketing-social.md): every channel kit and how they link to each other.

**Write the article people search for, put your product in its honest place, and keep the original on your own
site.** Medium brings readers who follow topics and publications, and its articles stay findable for months. It's a
support channel: strong for dev tools, AI tools, SaaS and tutorials; weak for games and consumer apps; weak at
sending clicks. Everything here cites Medium's own help and policy pages, or is labelled as practice to test.

```text
real question  →  useful article (product once, disclosed)  →  last paragraph + profile  →  landing  →  trial  →  paid
your blog post ↗  (imported with a canonical link)           ↘  publication + Boost  →  followers  →  next article
```

## Is Medium worth it? (verdict)

| | |
|---|---|
| **Yes, as support** | Dev tools, APIs, plugins, AI tools, productivity / B2B SaaS; anyone with a blog to mirror |
| **Maybe** | Mac apps, browser extensions, templates: one tutorial a month, the rest in mirror mode |
| **No** | Casual games and consumer mobile apps: their buyers don't read Medium |
| **Never as** | An ad board. Stories made mainly to send traffic to a product get no distribution and can get you suspended |

Details and the 3-phase plan: [docs/01-strategy.md](docs/01-strategy.md).

## One command

```text
/social-medium fit            → is Medium worth it for this product, and why
/social-medium start          → profile, import 2–3 posts, first article
/social-medium write <topic>  → one article: type, title, first lines, draft, product test, topics, UTM link
/social-medium mirror <url>   → republish your blog post with a canonical link
/social-medium pubs <topic>   → find and vet publications, write the pitch
/social-medium profile        → bio, about page, link with UTM, featured story
/social-medium numbers        → weekly table: reads, followers, site visits, trials
/social-medium risk           → no distribution, restricted, suspended? what happened and what to do
```

Router skill: [social-medium](skills/social-medium/SKILL.md). Installed as a plugin the command is
`/product-growth-hack:social-medium fit`; or copy the `skills/social-medium*` folders into `~/.claude/skills/`.

## Start in 3 steps
1. **Today (20 min):** profile, about page and one link with UTM → [docs/02-profile-setup.md](docs/02-profile-setup.md).
2. **This week (1 hour):** import 2–3 of your best blog posts with canonical links, and list 3–5 publications →
   [docs/04-canonical-and-republishing.md](docs/04-canonical-and-republishing.md) ·
   [docs/06-publications-and-boost.md](docs/06-publications-and-boost.md).
3. **Then weekly:** one article from a real question → [flow/weekly-flow.md](flow/weekly-flow.md) ·
   [social-medium-article](skills/social-medium-article/SKILL.md). Short on time? Mirror mode: 15 minutes per blog post.

## What's in this folder

| Folder | What's inside |
|---|---|
| [docs/](docs/01-strategy.md) | The method, one topic per file (below) |
| [flow/](flow/weekly-flow.md) | The weekly routine, mirror-only mode, the monthly check |
| [skills/](skills/README.md) | [social-medium](skills/social-medium/SKILL.md) (router) · [social-medium-article](skills/social-medium-article/SKILL.md) (one article) |
| [templates/](templates/article-file.md) | [Article file](templates/article-file.md) · [publication tracker](templates/publication-tracker.md) · [weekly numbers](templates/weekly-numbers.md) |
| [reference/](reference/medium-facts.md) | Facts with sources: rules, AI policy, distribution, Boost, canonical links, nofollow, Partner Program |

## Docs, in reading order
1. [Strategy: is Medium worth it, and the 3-phase plan](docs/01-strategy.md)
2. [Profile setup](docs/02-profile-setup.md)
3. [How Medium decides who sees your story](docs/03-how-medium-distributes.md)
4. [Write once, publish twice: canonical links](docs/04-canonical-and-republishing.md)
5. [Article playbook: 8 article types](docs/05-article-playbook.md)
6. [Publications and Boost](docs/06-publications-and-boost.md)
7. [Metrics and stop rules](docs/07-metrics-and-stop-rules.md)
8. [Rules and risks](docs/08-rules-and-risks.md)

## Five things to remember
- The article must be worth reading if your product didn't exist. Product once, "I make this" in the same sentence.
- Keep the original on your own site; Medium gets a copy with a canonical link.
- Links from Medium are nofollow: they bring readers, not Google ranking. Link the page that continues the article.
- Publications first, Boost follows. You can't ask for Boost; editors and curators pick it.
- Write it yourself. Mostly-AI articles can't be paywalled and aren't Boosted.
