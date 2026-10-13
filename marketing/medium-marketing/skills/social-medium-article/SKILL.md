---
name: social-medium-article
description: Write one Medium article that readers finish and that sends the right ones to your site, without breaking Medium's rules on promotion and AI. Starts from a real question, picks one of eight article types (how-to, fix, comparison, build story, lesson, deep dive, checklist, case study), writes the title, subtitle and first three lines, outlines and drafts it, runs a five-check test on mentioning your product, adds topics, a canonical link if it's on your blog, and one UTM link at the end. Use when someone asks "write a Medium article", "turn this into a Medium post", "Medium tutorial for my app", "Medium title", "how do I mention my app on Medium", "my Medium stories get views but no clicks", "viết bài Medium", or wants a weekly Medium article for a product.
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: "2–3 h per article"
  version: 1.0.0
  author: nvminhtu
---

# One Medium Article That Earns Its Readers

> Bring a real question; leave with a finished, rule-safe Medium article and one link that sends readers to your site.

## Goal
On Medium, the article itself is the marketing: it's read for months, editors decide whether to spread it, and a
good one is something you'll link from your README, emails and Reddit answers. This skill writes one article at a
time, built for the reader, with your product in its honest place.

## When to use
- You have a question your users keep asking, or something you learned building the product.
- You want to republish a blog post and adapt the title and intro for Medium.
- Your Medium stories get views but no reads, or reads but no site visits.
- **Not for:** deciding whether Medium fits at all → [social-medium](../social-medium/SKILL.md) `fit`. Short posts →
  [X kit](../../../x-marketing/README-X-Marketing.md).

## Inputs
- A real question and where it came from (Reddit thread, support email, search query).
- Your product facts: what it does, price, platform, and what it does **not** do.
- What you can show: your screenshots, code, numbers you measured.
- Your blog URL if the article lives there first; the publication you'll submit to.

## Steps
1. **Write the reader and the question** in one line each. If there's no real question, pick another topic.
2. **Pick one type** from [05-article-playbook.md](../../docs/05-article-playbook.md): how-to · fix · comparison ·
   build story · lesson · deep dive · checklist · case study. Prefer the first three for search readers.
3. **Write 3 titles and pick one:** specific problem or result, no clickbait. Add a subtitle: who it's for + what
   they'll get.
4. **Write the first 3 lines:** the problem in their words, then the promise.
5. **Outline, then draft** in your voice: headings, real steps, your screenshots or code, measured numbers only.
6. **Run the product test** (all yes, or no mention): useful without it · mention fits the article's question ·
   "I make this" in the same sentence · a free or manual alternative is included · at most one mention in the body.
7. **Finish:** last paragraph with who you are and one link
   `?utm_source=medium&utm_medium=article&utm_campaign=<slug>`; 5 topics, specific first; canonical link if it's a
   republish ([04](../../docs/04-canonical-and-republishing.md)); fill the [article file](../../templates/article-file.md).
8. **Publish or submit by hand** to one publication ([06](../../docs/06-publications-and-boost.md)), then share it
   2–3 times outside Medium (Friend Link if paywalled).

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You help me write one Medium article as an indie developer. Write like a person who did the work, not a brand.
Never invent numbers, users, quotes, features or experiences; write <CHECK> where you need a fact from me.

Reader: {{who}}
Their real question (and where I saw it): {{...}}
What I can show: {{screenshots, code, numbers I measured}}
My product: {{name · what it does · price · platform · what it does NOT do · landing URL}}
Original on my blog: {{URL or "none"}}   Publication I'll submit to: {{name or "none"}}

1. Pick ONE article type (how-to, fix, comparison, build story, lesson, deep dive, checklist, case study) and say why.
2. Give 3 titles (specific, no clickbait) and a subtitle; recommend one.
3. Write the first 3 lines: the problem in the reader's words, then the promise.
4. Give the outline, then the full draft with headings. Short paragraphs. No "In today's world", no emoji, no
   em dashes, no marketing words.
5. Product test, yes/no each: useful without my product · the mention fits the article's question · "I make this"
   in the same sentence · a free or manual alternative is included · at most one mention in the body.
   Mention my product only if all are yes.
6. Last paragraph: one line on who I am and one link with
   utm_source=medium&utm_medium=article&utm_campaign=<slug>.
7. Suggest 5 Medium topics, most specific first, and remind me to set the canonical link if it's on my blog.
````

## Example output

> **Illustrative example.** Fictional product (Clipnest) and question.

1. Reader: Mac users who lose copied text. Question (r/MacOS): *"Is there any way to get back something I copied an
   hour ago?"* Type: **how-to**, because they asked for steps.
2. Title: **How to Get Clipboard History on a Mac (Built-in Tricks and 3 Apps)** · Subtitle: *macOS keeps only the last
   thing you copied. Here's how to keep the rest, free and paid.*
3. First lines: *You copied a link an hour ago, then copied something else, and it's gone. macOS keeps exactly one
   item. Here are the free workarounds and the apps that fix it for good.*
4. Outline: why macOS forgets → free trick: Universal Clipboard and Notes → free trick: Shortcuts → three apps
   compared (privacy, price, image search) → which to pick.
5. Product test: useful without it ✔ · fits ✔ · disclosed ✔ · free options included ✔ · one mention ✔ → mention as
   one of three apps: *"Clipnest (I make this; free for 50 clips) is the only one of the three that searches text
   inside copied images <CHECK>."*
6. End: *I build small Mac utilities. More at clipnest.app?utm_source=medium&utm_medium=article&utm_campaign=mac-clipboard-history*
7. Topics: `Mac`, `macOS`, `Productivity`, `Apple`, `Software` · canonical: set to the blog post.

## Common mistakes
- **The product is the article.** Medium gives no distribution to content marketing. One mention, disclosed.
- **Five links to your site.** One link at the end; other links go to sources.
- **Pasting an AI draft.** Mostly-AI writing can't be paywalled and isn't Boosted. Use AI to outline and check;
  write it yourself.
- **Linking the home page.** Link the page that continues the article (the feature, the free template).
- **Republishing without a canonical link.** Set it, then check View source.

## Related skills
- [social-medium](../social-medium/SKILL.md): the router for every Medium job.
- [social-reddit-comment](../../../reddit-marketing/skills/social-reddit-comment/SKILL.md): answer the thread that
  inspired the article, and link it where the subreddit allows.
- [social-credible-posting](../../../../skills/social/social-credible-posting/SKILL.md): the proof ladder behind every
  claim.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources:
[Help: Distribution](https://help.medium.com/hc/en-us/articles/360006362473),
[Help: AI content policy](https://help.medium.com/hc/en-us/articles/22576852947223-Artificial-Intelligence-AI-content-policy),
[Help: Reasons for suspensions](https://help.medium.com/hc/en-us/articles/21308869037975-Reasons-for-Suspensions-or-Restrictions)
(checked 2026-10-13).
