---
name: research-doc-organization
description: Set up and keep a clean research folder in Markdown, with one note per question, a sources file, a decision log and an index, so research stays findable, citable and readable by both people and AI agents. Use when research is scattered across tabs, chats and docs, when starting research for a new product, when handing research to a teammate or AI agent, or when someone asks "how should I organize my research", "research notes template", or "where do I keep sources".
license: MIT
metadata:
  category: research
  difficulty: beginner
  time: 30 min to set up, 5 min per note
  version: 1.0.0
  author: nvminhtu
---

# Research Doc Organization

> In 30 minutes you will have a `research/` folder with an index, a sources list, a decision log and a note
> template, ready for your AI agent to read and add to.

## Goal
Every piece of research answers a question, cites its sources and leads to a decision, and anyone (you in three
months, a teammate, an AI agent) can find it in under a minute.

## When to use
- Research lives in 30 browser tabs, three chats and a notes app.
- Starting a new product, market or feature.
- An AI agent keeps re-researching things you already found.
- **Not for:** finding sources → [research-source-finding](../research-source-finding/SKILL.md).

## Inputs
- The product repo (or any folder) where the research should live.
- The 3–5 open questions you're researching right now.

## The structure

```text
research/
├── README.md            # index: open questions, finished notes, latest decisions
├── sources.md           # every source once: link, date, level, one-line summary
├── decisions.md         # decision log: date, decision, why, which notes
└── notes/
    ├── 2026-09-pricing-competitors.md
    ├── 2026-09-where-users-ask.md
    └── 2026-10-aso-keywords-us.md
```

- **One note = one question.** The file name is `YYYY-MM-<topic>.md`, so notes sort by date and read like a sentence.
- **Frontmatter on every note** (template in `assets/research-note.md`):
  `question`, `status` (open / answered / outdated), `confidence` (high / medium / low), `updated`, `sources`.
- **Link, don't copy.** Notes link to `sources.md#anchor` and to each other with relative links. The links turn
  the folder into a map.
- **Answer first.** Every note starts with a 2–3 line answer, then the evidence.

## Steps
1. **Create the folder (5 min).** Copy `assets/research-note.md`, `assets/sources-template.md` and
   `assets/decisions-template.md` into `research/`. Rename them to `notes/_template.md`, `sources.md` and `decisions.md`.
2. **Write the index (5 min).** `research/README.md` has three lists: *Open questions*, *Answered* (with a link to
   each note), and *Latest decisions*.
3. **Move existing research in (15 min).** For each open tab or chat worth keeping: which question does it answer?
   Add it to that note, and add its link to `sources.md`. Close the tab.
4. **Tell your AI agent (2 min).** Add to your `CLAUDE.md` / `AGENTS.md`:
   *"Research lives in `research/`. Read `research/README.md` first. New findings go in a note from
   `notes/_template.md`; cite sources from `sources.md`."*
5. **Keep it alive (5 min a week).** Set notes older than 6 months to `outdated` or re-check them. Every decision
   gets a line in `decisions.md` with links to the notes behind it.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are my research librarian. Organize my research into a Markdown folder.

Product: {{what it is}}
Open questions: {{3-5 questions}}
Raw research to sort (links, notes, chat excerpts): {{paste}}

1. Propose the file tree for research/ (README.md index, sources.md, decisions.md, notes/YYYY-MM-topic.md).
2. For each open question, create a note with this frontmatter:
   question, status (open/answered/outdated), confidence (high/medium/low), updated (today), sources (list).
   Start each note with a 2-3 line answer (or "Not answered yet" + what's missing), then evidence with links.
3. Put every link from my raw research into sources.md once: title, URL, publish date if known, date checked,
   level (1 official, 2 data, 3 users, 4 practitioners, 5 articles), one-line summary.
   Never invent a URL or a date. Write "unknown" instead.
4. Write research/README.md with Open / Answered / Latest decisions sections, all linked.
Output each file in its own code block with the file path as the heading.
````

## Example output

> **Illustrative example.** Fictional product, shown for format.

```markdown
---
question: Which paid tier do competitors put "export to PDF" in?
status: answered
confidence: medium
updated: 2026-09-30
sources: [notion-pricing, obsidian-pricing, r-productivity-export-thread]
---

**Answer:** 3 of 4 competitors keep PDF export free; only one paywalls it. Keep it free and paywall sync instead.

## Evidence
| Competitor | Export PDF | Source |
|---|---|---|
| Notion | Free | [notion-pricing](../sources.md#notion-pricing) |
| ...
```

## Common mistakes
- **One giant `research.md`.** It can't be linked, dated or marked outdated piece by piece.
- **Notes without an answer at the top.** Nobody reads 2 pages to find the conclusion.
- **Copying the same source into five notes.** When it changes, four copies are wrong. Link to `sources.md` instead.
- **Research that never becomes a decision.** If it didn't change a decision, ask whether it was worth doing.

## Related skills
- [research-source-finding](../research-source-finding/SKILL.md): find the sources that go into `sources.md`.
- [research-where-users-ask](../research-where-users-ask/SKILL.md) and [research-review-mining](../research-review-mining/SKILL.md): common notes to start with.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu).

**Tool (made by the maintainer at [OneClickTool](https://oneclicktool.app/?utm_source=github&utm_medium=skill&utm_campaign=growth-playbook&utm_content=research-doc-organization)):**
[Markdown Viewer](https://oneclicktool.app/macos/markdown-viewer?utm_source=github&utm_medium=skill&utm_campaign=growth-playbook&utm_content=research-doc-organization)
(free, Mac) opens a `research/` folder as a table, a map of which note links to which, or Finder-style columns,
with ★ favorites for the notes you use most.
