# Facebook Marketing for Indie Devs

> Part of [Marketing & Social](../README-marketing-social.md): every channel kit and how they link to each other.


**On Facebook, the people who buy small software are in groups, not in your Page's feed.** A Page with no
followers reaches almost no one, but a hobby, local or job group of 50,000 members asks "is there an app for…"
every week. This kit is groups first: answer there, earn the right to post, make your Page and profile look real
for the people who click through, and later run a small group of your own. Every fact here cites Meta's own
policy, help or investor pages, or is labelled as practice to test.

```text
a group member asks  →  your helpful answer (+ product only if it fits, disclosed)  →  your profile / Page  →  landing (UTM)  →  email or trial  →  paid
                     ↘  admins see you help, approve your one post a month  ↘  later: your own group, where users stay
```

## One command

```text
/social-facebook today           → today's 20 minutes: which groups, which threads, one Page post or none
/social-facebook groups <topic>  → 10–20 groups worth joining, scored on fit, activity and rules
/social-facebook reply <thread>  → an answer worth thanking, with or without the product
/social-facebook post <group>    → one post in that group's allowed format, rules checked, admin ask if needed
/social-facebook page            → Page or professional profile: name, bio, cover, pinned post, link with UTM
/social-facebook own-group       → start your own group: name, rules, entry questions, the first 30 days
/social-facebook numbers         → weekly table: answers, posts, profile visits, clicks, signups
/social-facebook fit             → is Facebook worth it for this product? (yes / test / no, with why)
/social-facebook risk            → post declined, muted, removed from a group, link blocked? what to do
```

Router skill: [social-facebook](skills/social-facebook/SKILL.md). Installed as a plugin the command is
`/product-growth-hack:social-facebook today`; or copy the `skills/social-facebook*` folders into `~/.claude/skills/`.

## Start in 3 steps
1. **Today (30 min):** check the fit, fix your profile and Page so a stranger sees a real maker, write your
   one-line answer intro → [docs/01-strategy.md](docs/01-strategy.md) · [docs/02-page-and-profile-setup.md](docs/02-page-and-profile-setup.md).
2. **This week (1 hour):** find 10–20 groups, read their rules, join the best 5, save the rules to a
   [group tracker](templates/group-tracker.md) → [social-facebook-groups](skills/social-facebook-groups/SKILL.md).
3. **Every day after (15–20 min):** 2–3 useful answers in your groups, product only when it truly fits; one
   rule-checked post per group per month at most; numbers on Sunday → [flow/weekly-flow.md](flow/weekly-flow.md).

## What's in this folder

| Folder | What's inside |
|---|---|
| [docs/](docs/01-strategy.md) | The method, one topic per file (below) |
| [flow/](flow/weekly-flow.md) | The daily 20 minutes, the weekly post slot, the Sunday numbers |
| [skills/](skills/README.md) | [social-facebook](skills/social-facebook/SKILL.md) (router) · [social-facebook-groups](skills/social-facebook-groups/SKILL.md) (find, answer, post in groups) |
| [templates/](templates/group-tracker.md) | [Group tracker](templates/group-tracker.md) · [post file](templates/post-file.md) · [weekly numbers](templates/weekly-numbers.md) |
| [reference/](reference/facebook-facts.md) | Facts with sources: spam rules, Feed demotions, link test, messaging, branded content, users |

Already in the main library, used by this kit:
[social-credible-posting](../../skills/social/social-credible-posting/SKILL.md) (tone and proof for every post) ·
[research-where-users-ask](../../skills/research/research-where-users-ask/SKILL.md) (where the questions are) ·
[community posting](../../skills/growth/action/06-community-posting.md) (the action-plan step this kit expands) ·
[email-list-and-deliverability](../../skills/email/email-list-and-deliverability/SKILL.md) (where the visitors
should end up).

## Docs, in reading order
1. [Strategy: is Facebook for your product?](docs/01-strategy.md)
2. [Page and profile setup](docs/02-page-and-profile-setup.md)
3. [How Facebook decides who sees a post, in plain words](docs/03-how-feed-distribution-works.md)
4. [Groups: find, join, answer, post](docs/04-groups-playbook.md)
5. [Post formats: 8 kinds of post for software](docs/05-post-formats.md)
6. [Your own group](docs/06-your-own-group.md)
7. [Metrics and stop rules](docs/07-metrics-and-stop-rules.md)
8. [Rules and risks](docs/08-rules-and-risks.md)

## Five things to remember
- Groups first, Page second. A Page is the shop sign people check after they meet you in a group.
- Answer the question fully before you mention anything. Say you made it, every time.
- Read the group's rules before every post, and ask an admin when the rules don't say. One post per group a month.
- Never "like and share to get the link". Meta calls engagement gating spam, and it demotes engagement bait.
- UTM on every link (`utm_source=facebook&utm_medium=group|page|profile|messenger`), or you'll never know which
  group brings buyers.
