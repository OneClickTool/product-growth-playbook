# Post file template

One file per post, `marketing/x/NN-<day>-<topic>.md` in the product's repo. Same frontmatter as campaign
tools that read post files from a repo (e.g. Promo Desk's Campaign tab, see [flow/tools.md](../flow/tools.md)).

````markdown
---
where: X
stage: share          # warmup | share | discuss | update | results | deal
date: {{YYYY-MM-DD HH:MM}}
link: first-comment   # direct | first-comment | bio | none — WHERE the link goes, never the URL itself
status: planned       # planned | posted YYYY-MM-DD <link to the post> | skipped | removed
kind: post            # post | thread | long | reply
variant: v01          # v01 … v20, see templates/variants/README.md
day: tue              # mon … sun (7-day rotation)
product: {{slug}}
aim: reply            # reply | share | follow | visit
---
# {{NN}} — X · {{topic}}

> Attach: {{screenshot / 10–30 s clip}}. Check before posting: {{numbers to verify}}.

## Body
```text
{{the post, under 280 characters unless kind: long. No URL here when link: first-comment}}
```

## Reply 1
```text
{{landing}}?utm_source=x&utm_medium=reply&utm_campaign={{slug}}
```
````

- `link:` says **where** the link goes. The URL itself lives in `## Reply 1` (`first-comment`), in the body (`direct`),
  or nowhere (`bio`, `none`). A URL in `link:` is rejected by tools that read this format.
- Default to `first-comment` or `bio`: links are weakly rewarded by the ranker
  ([03-how-x-ranks-posts.md](../docs/03-how-x-ranks-posts.md)), and the same link in many posts looks like spam
  ([08-rules-and-risks.md](../docs/08-rules-and-risks.md)).
- `stage:` maps the 7-day rotation: demo / tip / behind the scenes → `share`, question → `discuss`, weekly numbers →
  `results`, the one offer of the week → `deal`, posts before the product is out → `warmup`.
- `kind`, `variant`, `day`, `product`, `aim` are extra fields for your own sorting. `variant` lets you compare
  results by post type every Sunday. A ready file per variant: [templates/variants/](variants/README.md).
- For a thread, number each part `1/`, `2/` … on its own line inside the `text` block.
