# V14 · Behind the scenes / decision

💬 Talk · `stage: share` · `link: none` · details and when to use: [09-post-variants.md](../../docs/09-post-variants.md)

A choice others face too: pricing, a stack, a feature cut. Show the reasoning.

Copy the block below into `marketing/x/NN-thu-<topic>.md` and fill the `{{ }}`.

````markdown
---
where: X
stage: share
date: {{YYYY-MM-DD HH:MM}}
link: none
status: planned
kind: post
variant: v14
day: thu
product: {{slug}}
aim: reply
---
# {{NN}} — X · Behind the scenes / decision: {{topic}}

> Attach: Screenshot of notes, a diff or a design.
> Check before posting: No private data in the screenshot.

## Body
```text
Decided to {{decision}} in {{Product}}.

Option A: {{…}} — {{why not}}
Option B: {{…}} — {{why yes}}

{{What would make you change your mind}}.
```
````

## Example

> **Illustrative example.** Fictional product (Clipnest, a Mac clipboard app) and made-up numbers.

```text
Decided Clipnest stays one-time purchase, no subscription.

Subscription: steadier income, but my users said "just a utility".
One-time $19: fewer buyers, no churn emails.

I'd switch if sync costs real server money.
```
