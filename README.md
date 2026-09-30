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
| Launching soon | [Playbook: Launch a Product](playbooks/launch-a-product.md), a 6-week route |
| Launched, but nobody's using it | [Get Your First 100 Users](skills/launch/launch-get-first-100-users/SKILL.md) |
| Get more installs from App Store / Google Play search | [ASO Keyword Research](skills/aso/aso-keyword-research/SKILL.md) |
| Start making money | [Free Trial vs Freemium](skills/monetization/monetization-free-trial-vs-freemium/SKILL.md) → [Pricing Strategy](skills/monetization/monetization-pricing-strategy/SKILL.md) |

## Skills

| Area | Skills |
|---|---|
| 📱 [ASO](skills/aso/) | [Keyword Research](skills/aso/aso-keyword-research/SKILL.md) · [Title & Subtitle](skills/aso/aso-title-subtitle-optimization/SKILL.md) · [Screenshot Strategy](skills/aso/aso-screenshot-strategy/SKILL.md) · [Reviews & Ratings](skills/aso/aso-review-and-rating-strategy/SKILL.md) |
| 🚀 [Launch](skills/launch/) | [Pre-launch Checklist](skills/launch/launch-pre-launch-checklist/SKILL.md) · [Launch Post Writing](skills/launch/launch-post-writing/SKILL.md) · [Product Hunt Launch](skills/launch/launch-product-hunt-launch/SKILL.md) · [First 100 Users](skills/launch/launch-get-first-100-users/SKILL.md) |
| 💰 [Monetization](skills/monetization/) | [Free Trial vs Freemium](skills/monetization/monetization-free-trial-vs-freemium/SKILL.md) · [Pricing Strategy](skills/monetization/monetization-pricing-strategy/SKILL.md) · [Paywall Design](skills/monetization/monetization-paywall-design/SKILL.md) · [Subscription Tiers](skills/monetization/monetization-subscription-tiers/SKILL.md) |

**Playbooks:** [Launch a Product](playbooks/launch-a-product.md)

### 📖 Read the whole playbook as a map

27 Markdown files link to each other here. Open the repo in **[Markdown Viewer](https://oneclicktool.app/macos/markdown-viewer?utm_source=github&utm_medium=readme&utm_campaign=growth-playbook&utm_content=skills-hook)**
(free, Mac) and you can see which skill leads to which, browse folders like in Finder, and ★ star the skills you
use most. It's read-only, and nothing leaves your computer.

[![This repo in Markdown Viewer: every skill and the links between them](docs/images/mv-map.png)](https://oneclicktool.app/macos/markdown-viewer?utm_source=github&utm_medium=readme&utm_campaign=growth-playbook&utm_content=screenshot-map)

<details>
<summary>More screenshots: table view · Finder-style folders + reader with Favorites</summary>

[![Table view: every file with links in and out, and when it last changed](docs/images/mv-table.png)](https://oneclicktool.app/macos/markdown-viewer?utm_source=github&utm_medium=readme&utm_campaign=growth-playbook&utm_content=screenshot-table)

[![Folder view and reader: drill into skills like Finder, read the rendered skill, star it](docs/images/mv-reader.png)](https://oneclicktool.app/macos/markdown-viewer?utm_source=github&utm_medium=readme&utm_campaign=growth-playbook&utm_content=screenshot-reader)

</details>

<sub>I made Markdown Viewer. It's free, and it's how I keep this repo organized. → [Download Markdown Viewer](https://oneclicktool.app/macos/markdown-viewer?utm_source=github&utm_medium=readme&utm_campaign=growth-playbook&utm_content=skills-hook-cta)</sub>

**[Roadmap](ROADMAP.md):** SEO · Content · Retention · Analytics · Competitor research, prioritized by what people ask for
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

> **Tip:** every skill is a Markdown file, and most produce one (a checklist, a keyword sheet, a plan). To browse a folder
> of them as a table or a map of links, try [Markdown Viewer](https://oneclicktool.app/macos/markdown-viewer?utm_source=github&utm_medium=readme&utm_campaign=growth-playbook&utm_content=how-to-use) (free, Mac). I made it at
> [OneClickTool](https://oneclicktool.app/?utm_source=github&utm_medium=readme&utm_campaign=growth-playbook&utm_content=how-to-use).

## What makes a skill here

Every skill has the same parts: **Goal · When to use · Inputs · Steps · Prompt · Example output · Common mistakes**.
No theory dumps, no "10 generic tips". If you can't finish it in an hour and end up with something concrete,
it isn't done. Example numbers are either real or clearly labelled *Illustrative*.

## Contributing

New skills, real-world examples and corrections are all welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md)
and [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md), or pick a [`good first issue`](https://github.com/OneClickTool/product-growth-playbook/labels/good%20first%20issue).

## Author

Maintained by [Tu Nguyen (@nvminhtu)](https://github.com/nvminhtu), who builds and ships small apps and tools
at [OneClickTool](https://oneclicktool.app/?utm_source=github&utm_medium=readme&utm_campaign=growth-playbook).

Two tools I made that fit this repo:
- Reading lots of skills and Markdown files? [Markdown Viewer](https://oneclicktool.app/macos/markdown-viewer?utm_source=github&utm_medium=readme&utm_campaign=growth-playbook) (free, Mac) shows a whole folder at a glance.
- Running many projects with AI agents? [ShotMatic](https://shotmatic.app/?utm_source=github&utm_medium=readme&utm_campaign=growth-playbook) (Mac) shows every repo's next steps, blockers and uncommitted changes on one screen, and reopens the right Claude session.

## Support this project

The playbook is free and always will be. If a skill saved you time or helped you ship, you can support the work:

[![Support on Ko-fi](https://img.shields.io/badge/Ko--fi-Support%20this%20project-FF5E5B?logo=ko-fi&logoColor=white)](https://ko-fi.com/icecraftdigital)
<!-- Add once GitHub Sponsors is approved:
[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Sponsor-EA4AAA?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/nvminhtu)
-->

- [Ko-fi](https://ko-fi.com/icecraftdigital): one-time support, no account needed.
- Use a [OneClickTool](https://oneclicktool.app/?utm_source=github&utm_medium=readme&utm_campaign=growth-playbook&utm_content=support) app. *Free knowledge, paid tools.*
- Free ways that help just as much: ⭐ star the repo, share a skill that worked, or add a real example.

Support pays for the time spent writing new skills, keeping store rules up to date, and answering issues.

## License

[MIT](LICENSE). Use it, fork it, teach with it.
