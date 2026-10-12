# V10 · Number with context

📊 Prove · `stage: results` · `link: none` · details and when to use: [09-post-variants.md](../../docs/09-post-variants.md)

A metric moved and you know why. Always the base, the time range, and what didn't work.

Copy the block below into `marketing/x/NN-tue-<topic>.md` and fill the `{{ }}`.

````markdown
---
where: X
stage: results
date: {{YYYY-MM-DD HH:MM}}
link: none
status: planned
kind: post
variant: v10
day: tue
product: {{slug}}
aim: reply
---
# {{NN}} — X · Number with context: {{topic}}

> Attach: Screenshot of the dashboard (crop personal data).
> Check before posting: Numbers match the screenshot; base and dates stated.

## Body
```text
{{Metric}} went from {{A}} to {{B}} in {{time}}. Small base: {{n}}.

What changed: {{one specific change}}.
What didn't work: {{one thing}}.
```
````

## Example

> **Illustrative example.** Fictional product (Clipnest, a Mac clipboard app) and made-up numbers.

```text
Clipnest trial → paid went from 3% to 9% in 3 weeks. Small base: 212 trials.

What changed: the paywall shows your own clip count.
What didn't work: a cheaper yearly plan.
```
