# X Marketing for Indie Devs

> Part of [Marketing & Social](../README-marketing-social.md): every channel kit and how they link to each other.

![A maker at a desk sends posts up like lanterns toward a lighthouse and a small shop](../../docs/images/illustrations/04-x-kit-hero.jpg)

**Post daily about what you built, use X Premium on purpose, and turn profile visits into the first paying
subscribers.** Everything here is either from X's own code and help pages, or labelled as practice to test.

```text
post / reply  →  profile visit  →  link click  →  landing  →  trial  →  paid
```

## One command

```text
/social-x today      → today's 2 posts, links, reply sessions, hourly checklist
/social-x week       → next week's posts from your fact bank
/social-x reply      → paste a post, get 3 replies
/social-x drop       → paste a "what are you building?" post: link or not, and what to write
/social-x month      → the 30-day plan, day by day
/social-x profile    → bio, pinned demo, link
/social-x promo <p>  → hooks + demo shot list for one product
/social-x talk       → 5 non-promo posts for reach and trust
/social-x numbers    → weekly numbers, the weakest step, what to fix
```

Router skill: [social-x](skills/social-x/SKILL.md). Installed as a plugin the command is
`/product-growth-hack:social-x today`; or copy `skills/social-x*` folders into `~/.claude/skills/` for `/social-x`.

## A day on X: promote 3–5 products, spend the rest earning trust

Hour-by-hour: [flow/a-day-on-x.md](flow/a-day-on-x.md). The mix per week: ~14 posts, **4–5 about products (one each)**,
the rest tips, questions, takes and build log; ~10 replies a day, at most one with a link; one ask, on Sunday.

```text
07:30 answer overnight → 08:00 post 1 (product slot or tip) → 08:05 reply session (5–7, bigger accounts)
12:30 answer + 3 peer replies → 17:30 post 2 (talk only) + 5 buyer-source replies → 21:30 answer, follow 3–5, fact bank
```

**30 days, day by day:** [posts/plan-30-days.md](posts/plan-30-days.md) (Oct 12 → Nov 8, from the real baseline).

Ready to copy: [5-product rotation with hooks and links](posts/product-rotation.md) ·
[talk bank, 40 non-promo posts](posts/talk-bank.md) · [week 2, both mixed](posts/week-02-mix.md).

## Start in 3 steps
1. **Today (45 min):** set up the profile and pinned demo → [docs/02-profile-setup.md](docs/02-profile-setup.md)
   or the skill [social-x-profile-funnel](skills/social-x-profile-funnel/SKILL.md).
2. **This Sunday (30 min):** fill a [fact bank](templates/fact-bank.md) per product, then write the week with
   [social-x-growth](skills/social-x-growth/SKILL.md). No time? Copy [posts/week-01-starter.md](posts/week-01-starter.md).
3. **Every day (25–60 min):** `/social-x today`, or follow [flow/a-day-on-x.md](flow/a-day-on-x.md) by hand.

## What's in this folder

| Folder | What's inside |
|---|---|
| [docs/](docs/) | The X marketing flow, one topic per file (below) |
| [reference/](reference/) | [Fake revenue screenshots and scams: how to check](reference/fake-proof-and-scams.md), research log, raw facts on the ranker and Premium, tips by evidence level, [trends](reference/trends.md), articles, repos, glossary |
| [skills/](skills/) | Agent Skills for X: [**social-x** (router)](skills/social-x/SKILL.md) · [daily](skills/social-x-daily/SKILL.md) · [growth](skills/social-x-growth/SKILL.md) · [reply](skills/social-x-reply/SKILL.md) · [profile funnel](skills/social-x-profile-funnel/SKILL.md) |
| [flow/](flow/) | [A day on X, hour by hour](flow/a-day-on-x.md), the [daily / weekly / monthly routine](flow/daily-flow.md), the [real analytics pattern](flow/analytics-pattern.md) it produced, the [cross-channel funnel](flow/cross-channel-funnel.md) (Reddit, email signatures, stores → X profile → free trial), and the [tools](flow/tools.md) to use (X's own, outside, and ones the maintainer builds) |
| [resources/](resources/) | [Links ready to paste on X](resources/links.md): products, stores, extensions, articles, channels, videos |
| [templates/](templates/) | [Fact bank](templates/fact-bank.md) · [product rotation](templates/product-rotation.md) · [post file](templates/post-file.md) · [20 post variants](templates/variants/README.md) · [weekly numbers](templates/weekly-numbers.md) · [reply targets](templates/reply-targets.md) |
| [posts/](posts/) | Ready to copy: [product rotation](posts/product-rotation.md), [talk bank](posts/talk-bank.md), [week 1](posts/week-01-starter.md), [week 2](posts/week-02-mix.md) |

## Docs, in reading order
1. [Strategy: zero followers → first paid subscriber](docs/01-strategy-first-dollar.md)
2. [Profile setup checklist](docs/02-profile-setup.md)
3. [How X ranks posts, in plain words](docs/03-how-x-ranks-posts.md)
4. [X Premium: 30-day plan](docs/04-premium-30-day-plan.md)
5. [Post formats: the 7-day rotation](docs/05-post-formats.md)
6. [Reply playbook (the Premium lever)](docs/06-reply-playbook.md)
7. [Metrics and stop rules](docs/07-metrics-and-stop-rules.md)
8. [Rules and risks](docs/08-rules-and-risks.md)
9. [Post variants: 20 kinds of post and when to use each](docs/09-post-variants.md)
10. [Best practices, on one page](docs/10-best-practices.md)

## Five things to remember
- Shares and replies move ranking; likes barely do. Mutes and reports cost far more than anything earns.
- A post lives 48 hours in For You. One good post a day beats five.
- Premium's documented growth feature is **reply prioritization**. Use it every day, by hand.
- Six posts give, one asks. The pinned post sells the rest of the time.
- UTM on every link, or you'll never know if X (and Premium) pays.

## Keep it current
- Monthly: check [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) "Notable Updates" and
  [About X Premium](https://help.x.com/en/using-x/x-premium); update [reference/](reference/) with the date.
- New research goes in `reference/research-YYYY-MM-DD-<topic>.md`.
- Links that die get removed from [resources/links.md](resources/links.md).

<sub>The tools and products in `flow/tools.md`, `resources/` and `posts/` are made by the maintainer of this repo
and are marked as such.</sub>
