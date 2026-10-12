# V04 · Screenshot tour

🎬 Show · `stage: share` · `link: first-comment` · details and when to use: [09-post-variants.md](../../docs/09-post-variants.md)

A product with several screens (or a new landing page). Four images, each one caption.

Copy the block below into `marketing/x/NN-mon-<topic>.md` and fill the `{{ }}`.

````markdown
---
where: X
stage: share
date: {{YYYY-MM-DD HH:MM}}
link: first-comment
status: planned
kind: post
variant: v04
day: mon
product: {{slug}}
aim: visit
---
# {{NN}} — X · Screenshot tour: {{topic}}

> Attach: Exactly 4 images, in the order of the text, readable on a phone.
> Check before posting: Screens match the current version; price matches the store.

## Body
```text
{{Product}} in 4 screens:

1. {{screen 1: what you do there}}
2. {{screen 2}}
3. {{screen 3}}
4. {{screen 4}}

{{Price / free tier in one line}}
```

## Reply 1
```text
{{landing}}?utm_source=x&utm_medium=reply&utm_campaign={{slug}}
```
````

## Example

> **Illustrative example.** Fictional product (Clipnest, a Mac clipboard app) and made-up numbers.

```text
Clipnest in 4 screens:

1. Everything you copied, searchable
2. Pin the ones you reuse
3. Paste as plain text with ⇧
4. Sync off by default

Free for 50 clips, Pro $19 once
```
