---
name: listing-browser-extension
description: List a browser extension step by step on the Chrome Web Store, Microsoft Edge Add-ons and Firefox Add-ons (AMO), in three levels (1 get approved, 2 get found, 3 grow), with store fees, required images, the single-purpose and permission rules that cause most rejections, and Firefox's source-code rule. Use when publishing or updating a Chrome/Edge/Firefox extension, when an extension was rejected, or when someone asks "how do I publish a Chrome extension", "Chrome Web Store listing", "publish to Firefox add-ons", or "extension store checklist".
license: MIT
metadata:
  category: listing
  niche: browser extensions
  difficulty: beginner → advanced (3 levels)
  time: "Level 1: 1-2 h per store · Level 2: 1 h · Level 3: ongoing"
  version: 1.0.0
  author: nvminhtu
---

# Browser Extension Listing (Chrome · Edge · Firefox)

> Build once, list on three stores. Level 1 gets you approved, Level 2 gets you found, Level 3 grows installs.

## Goal
Get the same extension approved on Chrome, Edge and Firefox without the classic rejections (vague purpose,
unjustified permissions, missing privacy disclosures), and with a listing that converts.

## When to use
- First publish or a big update of a Manifest V3 extension.
- A rejection that mentions purpose, permissions, privacy or code.
- **Not for:** mobile apps → [listing-app-store](../listing-app-store/SKILL.md), [listing-google-play](../listing-google-play/SKILL.md).

## Where to list

| Store | Cost | Review | Notes | Link |
|---|---|---|---|---|
| Chrome Web Store | One-time registration fee (US$5 at the time of writing) | Yes, from hours to weeks (longer with broad permissions) | Biggest audience | [Developer Dashboard](https://chrome.google.com/webstore/devconsole/) |
| Microsoft Edge Add-ons | Free | Yes | Usually the same package as Chrome | [Partner Center](https://partner.microsoft.com/dashboard/microsoftedge) |
| Firefox Add-ons (AMO) | Free | Yes | Minified or bundled code → **upload the source code + build steps** | [addons.mozilla.org](https://addons.mozilla.org/developers/) |

## Inputs
- A ZIP of the extension (Manifest V3), a privacy policy URL if you touch user data, and a support email or site.
- Images: icon **128×128** (96×96 artwork with transparent padding), **screenshots 1280×800 or 640×400** (1–5),
  **small promo tile 440×280** (required on Chrome), marquee **1400×560** (optional, needed to be featured).

## Steps

### Level 1: Get approved (required)
1. **Write the single purpose (5 min).** One sentence: what the extension does. Every feature must serve it.
   Stores reject extensions that bundle unrelated features.
2. **Trim permissions (15 min).** Remove anything you don't use. Prefer `activeTab` and optional permissions over
   `<all_urls>` host access. Broad permissions mean slower reviews and scarier install prompts.
3. **Justify each permission (10 min).** In the Chrome dashboard *Privacy* tab, write one plain sentence per permission
   ("`storage`: saves your tab groups locally").
4. **Privacy practices (10 min).** Declare what data you collect (usually "none"), certify the limited-use policy,
   and link your privacy policy if you handle any user data.
5. **Listing (30 min).** Name, a **summary of up to 132 characters**, a detailed description (what it does, how to
   use it, what it does *not* do with data), category, language, icon, screenshots and the 440×280 promo tile.
6. **Submit to Chrome, then Edge** (same ZIP in most cases), **then Firefox**. For Firefox, test in Firefox first,
   and if you use a bundler or minifier, attach the source code and exact build instructions.

### Level 2: Get found
1. **Keywords live in the name, summary and description.** Use the words people search for ("tab manager",
   "dark mode") → [aso-keyword-research](../../aso/aso-keyword-research/SKILL.md) works the same way.
2. **Screenshots that explain:** caption + the extension in action, 5 of them → [aso-screenshot-strategy](../../aso/aso-screenshot-strategy/SKILL.md).
3. **Ratings:** ask after a success moment (e.g. the 5th time they use it), link straight to the review tab, and reply to every review.
4. **Localize** the listing for your top languages.

### Level 3: Grow
- **Aim for the "Featured" badge on Chrome:** follow the best-practice listing, keep the extension fast and
  permission-light, and update it regularly.
- **Add a marquee tile (1400×560)** so the store can feature you in collections.
- **List it for free elsewhere:** [listing-free-directories](../listing-free-directories/SKILL.md) (AlternativeTo, Product Hunt, r/chrome_extensions).
- **An uninstall survey URL** (`chrome.runtime.setUninstallURL`) tells you why people leave.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are a browser-extension store expert. Prepare my Chrome / Edge / Firefox listing.

Extension: {{what it does}}   Manifest permissions: {{paste permissions + host_permissions}}
Data it touches: {{none / what}}   Uses a bundler or minifier? {{yes/no}}   Target keywords: {{...}}

1. Write the single-purpose sentence.
2. For each permission: is it needed? Suggest a narrower alternative (activeTab, optional permissions) where possible,
   and write a one-sentence justification.
3. Listing: name (≤ 45 chars incl. keyword), summary (≤ 132 chars), detailed description (what it does, how to use,
   privacy in plain words), category, and 5 screenshot captions.
4. Privacy practices answers, and whether I need a privacy policy.
5. Firefox notes: what source code and build instructions I must include.
Mark anything you're unsure about as TODO. Don't invent features.
````

## Example output

> **Illustrative example.** Fictional extension, shown for format.

```text
Single purpose: Group open tabs by project and restore them later.
Permissions: tabs (read titles/URLs to group) · storage (save groups locally) · removed <all_urls> (not needed)
Summary (98/132): Group tabs by project in one click. Save, restore and search tab groups. Private: nothing leaves your browser.
Screenshots: 1 "One click, tidy tabs" · 2 "Restore any project later" · 3 "Search all saved tabs" · …
Firefox: Vite build → uploaded src.zip + README-build.md (node 22, npm ci, npm run build:firefox)
```

## Common mistakes
- **`<all_urls>` "just in case".** It slows reviews and scares users. Ask for access only when you need it.
- **A vague or multi-purpose description** ("productivity toolkit"). It can be rejected under the single-purpose policy.
- **Privacy tab left blank** or out of sync with what the code does.
- **Minified Firefox upload without source code.** AMO reviewers need to rebuild it.
- **Keyword-stuffed names.** Both Chrome and Firefox policies prohibit misleading or spammy metadata.

## Related skills
- [listing-free-directories](../listing-free-directories/SKILL.md): free places to list the extension.
- [launch-quick-download-wins](../../launch/launch-quick-download-wins/SKILL.md): first installs this week.
- [case-study-competitor-teardown](../../case-study/case-study-competitor-teardown/SKILL.md): study the top extensions in your category.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: Chrome Web Store [listing requirements](https://developer.chrome.com/docs/webstore/program-policies/listing-requirements/),
[image guidelines](https://developer.chrome.com/docs/webstore/images), [best listing](https://developer.chrome.com/docs/webstore/best-listing);
Firefox Extension Workshop [source code submission](https://extensionworkshop.com/documentation/publish/source-code-submission/).
Fees and rules change, so check them before submitting.
