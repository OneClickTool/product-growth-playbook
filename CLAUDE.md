# CLAUDE.md

Rules for AI agents working in this repository. [AGENTS.md](AGENTS.md) points here.

## What this repo is
A library of **growth skills** for people building digital products. Every skill is an Agent Skill
(`skills/<area>/<name>/SKILL.md`) that a human can read on GitHub and an agent can install.
The plan and roadmap live in [docs/PLAN.md](docs/PLAN.md) (Vietnamese). Public content is in English.

## Hard rules
- Follow [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md) exactly: frontmatter, section order, four-backtick prompt fence.
- Folder name == `name` == `<area>-<task>`, lowercase with hyphens.
- **Never invent data and present it as real.** Made-up numbers go under an `> **Illustrative example.**` label.
  Store limits, policies and prices must cite an official source.
- Don't create empty folders or list planned skills as if they exist. Mark them *planned*.
- When you add or rename a skill, update `.claude-plugin/marketplace.json`, the area README,
  the router table in `skills/growth/SKILL.md` and the root README.
- Scripts in `skills/**/scripts/` use the Python standard library only.
- Product mentions from the maintainer (Markdown Viewer, Shotmatic) appear only where the plan allows, are
  disclosed as the maintainer's own, and go at the end.

## Before you finish
```bash
python3 scripts/validate_skills.py
```
It must print `OK`.
