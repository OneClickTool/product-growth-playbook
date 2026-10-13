# 02 · Profile setup: business account, claimed site, boards

About 30 minutes, once. Facts and sources: [reference/pinterest-facts.md](../reference/pinterest-facts.md).

## 1. Business account
Switch your account to a business account (free) or create one. You need it for Pinterest Trends and analytics
([Pinterest Help: Trends](https://help.pinterest.com/en/business/article/pinterest-trends)), and Pinterest recommends
one for claiming a website.

## 2. Claim your website
Claiming tells Pinterest you own the site. You get insight into how often your content is saved, your profile
picture next to pins saved from your site, and a follow link on those pins
([Pinterest Help: Claim your website](https://help.pinterest.com/en/business/article/claim-your-website)).

| Method | When to use it |
|---|---|
| HTML tag in `<head>` | You can edit the site template (most static sites, WordPress, Next.js) |
| HTML file in the root folder | You can upload files but not edit the template |
| DNS TXT record | You manage the domain's DNS (works for every page on the domain) |

You must own the domain and be able to edit it; marketplace stores (Etsy, Amazon) and most social profiles can't be
claimed, and one site belongs to one Pinterest account (same source).

## 3. Name, bio, cover

| Field | What to write | Example (illustrative) |
|---|---|---|
| Display name | Brand + what it helps with, using a search word | `Clipnest · Mac productivity` |
| About | Who it's for, what they'll find on your boards, one proof line | "Mac shortcuts, desk setups and free templates for students and remote workers. By the maker of Clipnest." |
| Website | Your claimed site, the page that best explains the product | `https://example.com/?utm_source=pinterest&utm_medium=profile` |
| Cover / featured boards | Your 3 boards closest to the product | — |

> **Illustrative example.** Fictional product.

## 4. Boards
Name 5–10 boards after what people search, not after your brand
([04-keywords-and-boards.md](04-keywords-and-boards.md)). Each gets a one-or-two-sentence description using the
same words. Use the [board plan template](../templates/board-plan.md).

## 5. Rich Pins (optional)
If your pages have Open Graph or schema.org markup, you can apply for Rich Pins so pins pull the title and
description from the page. Third-party guides describe the validator and the article / product / recipe / app types
([Yoast](https://yoast.com/how-to-earn-money-on-pinterest/)); check the current steps in Pinterest's developer docs
before relying on them.

## Checklist

```text
[ ] business account
[ ] website claimed (tag / file / DNS) and verified
[ ] name with a search word, about line, website with UTM
[ ] 5–10 boards with search-word names and descriptions
[ ] 3 landing pages picked (how-to, template, landing)
```
