# Skill template

Copy this into `skills/<area>/<area>-<task>/SKILL.md` and fill it in.
Every skill must pass `python3 scripts/validate_skills.py` and the checklist in
[CONTRIBUTING.md](CONTRIBUTING.md#definition-of-done).

- **Folder name = `name`**, lowercase with hyphens, prefixed with the area: `aso-keyword-research`.
- **`description`** is what an AI agent reads to decide whether to use the skill. Say *what it does* and
  *when to use it*, and include the words people actually type. Keep it under 1024 characters.
- Anything that is not `name` / `description` / `license` goes under `metadata`.
- Wrap prompts in **four** backticks so they can contain code blocks without breaking the page.
- Keep `SKILL.md` under 500 lines. Put long reference material in `references/`, templates in `assets/`,
  and helper scripts (standard library only) in `scripts/`.

````markdown
---
name: area-task-name
description: One or two sentences. What the skill produces, and when to use it (list trigger phrases).
license: MIT
metadata:
  category: aso | launch | monetization
  difficulty: beginner | intermediate | advanced
  time: 30-60 min
  version: 1.0.0
  author: your-github-handle
---

# Skill title

> One sentence: what you will have when you are done.

## Goal
What the finished output is and why it matters (1–2 sentences).

## When to use
- Situation 1
- Situation 2
- **Not for:** the case where another skill fits better (link it).

## Inputs
- What the user must have ready before starting.

## Steps
1. A concrete action with a checkable result.
2. ...

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

```text
You are ... Given {{input}}, do ...
```

## Example output
A short, real example of the finished output. If the numbers are not from a real product, start the
section with `> **Illustrative example.** Numbers are made up to show the format.`

## Common mistakes
- Mistake, and what to do instead.

## Related skills
- [other-skill](../other-skill/SKILL.md): when to use it next.

## Credits
Written by @handle. Sources: links.
````
