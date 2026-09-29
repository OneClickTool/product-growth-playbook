# Anatomy of a skill

```text
skills/aso/aso-keyword-research/
├── SKILL.md        # the skill: frontmatter + guide + prompt (required)
├── assets/         # files the user copies: sheets, templates
├── references/     # long background an agent loads only when needed
└── scripts/        # small helpers, Python standard library only
```

**Why a folder and not a single `.md` file?** A folder that contains a `SKILL.md` follows the open
[Agent Skills](https://agentskills.io) format. The same folder reads as a guide on GitHub and installs into
Claude Code, Codex, Cursor, Gemini CLI and other agents.

**Why is `description` so important?** An agent sees only `name` + `description` until it decides to load a
skill. If the description doesn't include the words people actually use ("ASO keywords", "no one finds my app"),
the skill never gets used.

**Why the `<area>-` prefix?** People install skills from many repos side by side. A bare name like
`keyword-research` could collide with another repo's skill. `aso-keyword-research` won't.

**Why four backticks around prompts?** Prompts often contain code blocks. A three-backtick fence inside a
three-backtick fence breaks the page on GitHub.
