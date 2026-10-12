# Resources: links ready to share

Everything you paste into X lives in [links.md](links.md): product pages, store links, extensions, free apps,
articles, and (once they exist) channels and videos. Open it, copy, post.

## How to make a new X link

```text
<page URL>?utm_source=x&utm_medium=<bio|post|reply|pinned|thread>&utm_campaign=<product-slug>&utm_content=<YYYY-MM-DD or post number>
```

- `utm_medium` says *where on X* the click happened; `utm_content` tells two posts apart.
- Store pages (App Store, Google Play, Chrome Web Store) drop UTM. Link to your landing page in posts, or use the
  store's own campaign links (App Store Connect `pt`/`ct`, Google Play `referrer`).
- Keep the bio link stable; change `utm_content` in posts instead.

## Rules for this folder
- Only links that are live today. Re-check monthly (`curl -I` or open them).
- A price or offer in a post must match the store, not this file.
- No private links (dashboards, admin pages, drafts), no emails, no personal accounts that aren't public.
