# V15 · Failure / bug story

💬 Talk · `stage: share` · `link: none` · details and when to use: [09-post-variants.md](../../docs/09-post-variants.md)

Something broke or got rejected. Symptom, cause, fix, lesson. People trust builders who show this.

Copy the block below into `marketing/x/NN-thu-<topic>.md` and fill the `{{ }}`.

````markdown
---
where: X
stage: share
date: {{YYYY-MM-DD HH:MM}}
link: none
status: planned
kind: post
variant: v15
day: thu
product: {{slug}}
aim: reply
---
# {{NN}} — X · Failure / bug story: {{topic}}

> Attach: Screenshot of the error, rejection or graph dip.
> Check before posting: Store or user names removed if not public.

## Body
```text
{{What failed}}.

Symptom: {{…}}
Cause: {{plain words}}
Fix: {{…}}

{{One lesson}}.
```
````

## Example

> **Illustrative example.** Fictional product (Clipnest, a Mac clipboard app) and made-up numbers.

```text
App Review rejected Clipnest twice in one week.

Symptom: "app requests accessibility without reason"
Cause: I asked on first launch, before any feature needed it
Fix: ask only when the user turns on paste shortcuts

Ask for permissions at the moment they make sense.
```
