# Post file template

One file per post, `marketing/instagram/NN-<day>-<topic>.md` in the product's repo, next to its slide images.
Same frontmatter idea as the [X post file](../../x-marketing/templates/post-file.md), so one campaign tool can read
both.

````markdown
---
where: Instagram
stage: share          # warmup | share | discuss | update | results | deal
date: {{YYYY-MM-DD HH:MM}}
link: bio             # bio | story | dm | none — WHERE the link goes, never the URL itself
status: planned       # planned | posted YYYY-MM-DD <link to the post> | skipped | removed
kind: carousel        # carousel | reel | single | story
format: I01           # I01 … I12, see docs/05-post-formats.md
slides: 8             # carousel only
trial: false          # true = Trial Reel (non-followers first)
day: mon
product: {{slug}}
aim: save             # send | save | visit | tap
---
# {{NN}} — Instagram · {{topic}}

> Files: `{{NN-slug}}-s01.png` … `-s08.png` (or `.mp4` + `-cover.png`). Check before posting: {{numbers to verify}}.

## Slides
1. {{text}} — {{image}}
2. …

## Caption
```text
{{line 1, ≤125 chars, search words}}

{{steps, one per line}}

{{ask}}
{{path: "… → link in bio"}}

#tag1 #tag2 #tag3
```

## Alt text
1. {{…}}
2. …

## Story (+1–3 h)
```text
1 tease: share the post — "{{…}}"
2 proof: {{screenshot / clip}} — poll "{{…}}"
3 path: "{{…}}" — link sticker "{{sticker text}}"
```

## Links
```text
bio:   {{landing}}?utm_source=instagram&utm_medium=bio&utm_campaign={{slug}}&utm_content={{NN-slug}}
story: {{landing}}?utm_source=instagram&utm_medium=story&utm_campaign={{slug}}&utm_content={{NN-slug}}
```
````

- `link:` says **where** the visit happens. URLs live in `## Links`, never in the caption (they aren't clickable).
- `format:` lets you compare formats every Sunday ([07](../docs/07-metrics-and-stop-rules.md)).
- `stage:` uses the same values as the X kit: demo / tip → `share`, poll → `discuss`, numbers → `results`, offer → `deal`.
