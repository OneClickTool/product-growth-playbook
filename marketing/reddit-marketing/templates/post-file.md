# Post file template

One file per post, `marketing/reddit/NN-<subreddit>-<topic>.md` in the product's repo. Same frontmatter as campaign
tools that read post files from a repo (`where`, `stage`, `date`, `link`, `status`), plus Reddit fields.

````markdown
---
where: Reddit
subreddit: r/{{name}}
variant: r01            # r01 … r10, see docs/06-post-variants.md
stage: share            # warmup | share | discuss | update | results | deal
date: {{YYYY-MM-DD HH:MM}}
flair: {{exact flair}}
link: direct            # direct | first-comment | bio | none — WHERE the link goes, never the URL itself
status: planned         # planned | posted YYYY-MM-DD <link to the post> | skipped | removed
rules_checked: {{YYYY-MM-DD}} · {{wiki page or rules URL}}
---
# {{NN}} — Reddit · r/{{name}} · {{topic}}

> Rules that shaped this post: {{promo allowed? day? title tag? karma minimum?}}.
> Attach: {{GIF / screenshots}}. Check before posting: {{numbers, price, platform}}.

## Title
```text
{{title, in the subreddit's format}}
```

## Body
```text
{{body; say you're the developer; end with a real question}}
```

## Reply 1
```text
{{only if link: first-comment — the URL with ?utm_source=reddit&utm_medium=post&utm_campaign={{name}}}}
```
````

- `stage:` R01/R04/R08 → `share`, R02/R05 → `discuss`, R03/R09 → `results`, R06/R07 → `deal`.
- After posting, set `status: posted <date> <url>`; if a moderator removes it, `status: removed` and note why.
