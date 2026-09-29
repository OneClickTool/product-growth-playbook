# Product Growth Playbook

**Free, open-source growth skills for people building digital products: ASO, launch, monetization and more.**

[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-8A2BE2)](https://agentskills.io)

For people building apps, SaaS, games, AI products, websites and browser extensions.
Each skill does **one concrete growth task in under an hour** and gives you an output you can use right away:
a keyword list, a launch plan, a price. Read it like a guide, paste its prompt into any AI chat, or install
it as an agent skill.

## Quick start

| You want to… | Start here |
|---|---|
| Not sure where to start | [`growth`](skills/growth/SKILL.md): answer 4 questions, get one next step |
| Get more installs from App Store / Google Play search | [ASO Keyword Research](skills/aso/aso-keyword-research/SKILL.md) |

## Skills

| Area | Skills | Status |
|---|---|---|
| 📱 [ASO](skills/aso/) | [Keyword Research](skills/aso/aso-keyword-research/SKILL.md) | 1 available · 4 planned |
| 🚀 Launch | Pre-launch checklist · First 100 users · Product Hunt · Launch post | planned |
| 💰 Monetization | Pricing strategy · Paywall design · Free trial vs freemium · Tiers | planned |

**Roadmap:** SEO · Content · Retention · Analytics · Competitor research, prioritized by what people ask for
in [Discussions](https://github.com/OneClickTool/product-growth-playbook/discussions).

## Three ways to use a skill

**1. Any AI chat (Claude, ChatGPT, Gemini…):** open a skill, copy the *Prompt* block, fill in the `{{ }}` parts.

**2. Claude Code:**

```text
/plugin marketplace add OneClickTool/product-growth-playbook
/plugin install product-growth-playbook@product-growth-playbook
```

Then just describe your problem ("my app gets no search traffic"). The matching skill loads on its own.

**3. Codex, Cursor, Gemini CLI and other agents:**

```bash
npx skills add OneClickTool/product-growth-playbook
```

Or copy a skill folder into your agent's skills directory (for example `~/.claude/skills/`).

## What makes a skill here

Every skill has the same parts: **Goal · When to use · Inputs · Steps · Prompt · Example output · Common mistakes**.
No theory dumps, no "10 generic tips". If you can't finish it in an hour and end up with something concrete,
it isn't done. Example numbers are either real or clearly labelled *Illustrative*.

## Contributing

New skills, real-world examples and corrections are all welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md)
and [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md), or pick a [`good first issue`](https://github.com/OneClickTool/product-growth-playbook/labels/good%20first%20issue).

## Author

Maintained by [Tu Nguyen (@nvminhtu)](https://github.com/nvminhtu), who builds and ships small apps and tools.

<!-- TODO: add product links with UTM once URLs are final, e.g.
Working with lots of Markdown? Try [Markdown Viewer](URL?utm_source=github&utm_medium=readme&utm_campaign=growth-playbook). (I made it.)
-->

## License

[MIT](LICENSE). Use it, fork it, teach with it.
