# Post file template

One file per post, `marketing/x/NN-<day>-<topic>.md` in the product's repo. Same frontmatter Promo Desk reads.

````markdown
---
stage: share
where: X
kind: post            # post | thread | long | reply
day: tue              # mon … sun (7-day rotation)
product: {{slug}}
aim: reply            # reply | share | follow | visit
date: {{YYYY-MM-DD}}
link: {{landing}}?utm_source=x&utm_medium=post&utm_campaign={{slug}}
status: planned       # planned | posted YYYY-MM-DD <link to the post>
---
# {{NN}} — {{topic}}

> Attach: {{screenshot / 10–30 s clip}}. Check before posting: {{numbers to verify}}.

## Body

```text
{{the post, under 280 characters unless kind: long}}
```
````

For a thread, number each part `1/`, `2/` … on its own line inside the `text` block.
