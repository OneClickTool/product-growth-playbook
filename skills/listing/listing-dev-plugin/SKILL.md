---
name: listing-dev-plugin
description: Publish a small plugin, extension or developer tool to the marketplace where its users already are (VS Code Marketplace and Open VSX for Cursor/VSCodium, JetBrains Marketplace, Raycast Store, Obsidian community plugins, Figma Community, npm, Homebrew), in three levels (1 get published, 2 get found, 3 grow), with each marketplace's submission process, review and required assets. Use when shipping a VS Code/JetBrains/Raycast/Obsidian/Figma plugin or a CLI/npm package, or when someone asks "how do I publish a VS Code extension", "submit an Obsidian plugin", "publish to the Raycast Store", or "where do I list my dev tool".
license: MIT
metadata:
  category: listing
  niche: plugins and developer tools
  difficulty: beginner → intermediate (3 levels)
  time: "Level 1: 1-2 h · Level 2: 1 h · Level 3: ongoing"
  version: 1.0.0
  author: nvminhtu
---

# Plugin & Dev Tool Listing

> Your users install plugins from inside the tool they already use. Get into that marketplace, then make the
> listing (usually your README) do the selling.

## Goal
Publish to the right marketplace on the first try, and turn the listing into installs.

## When to use
- A plugin for an editor or app, or a small CLI/library, is ready.
- **Not for:** browser extensions → [listing-browser-extension](../listing-browser-extension/SKILL.md).

## Inputs
- The plugin or tool in a public (or publishable) repository, with a LICENSE and a README.
- An icon, a GIF of it in action, and an account on each marketplace you'll use.

## Where to publish

| Marketplace | How you submit | Review | Cost | Docs |
|---|---|---|---|---|
| **VS Code Marketplace** | Create a publisher, then `vsce publish` | Automated checks | Free | [Publishing extensions](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) |
| **Open VSX** (Cursor, VSCodium, Windsurf…) | Sign in with GitHub, `npx ovsx create-namespace`, `npx ovsx publish` | Namespace ownership | Free | [open-vsx.org](https://open-vsx.org/) |
| **JetBrains Marketplace** | Vendor profile, then upload the first version manually | Approval before it's listed | Free (paid plugins possible) | [Uploading a plugin](https://plugins.jetbrains.com/docs/marketplace/uploading-a-new-plugin.html) |
| **Raycast Store** | `npm run publish` opens a PR to `raycast/extensions` | Human review, first contact usually within a week | Free | [Publish an extension](https://developers.raycast.com/basics/publish-an-extension) |
| **Obsidian community plugins** | GitHub release (`main.js`, `manifest.json`, optional `styles.css`), then submit in the community directory | Automated + human review | Free | [Submit your plugin](https://docs.obsidian.md/Plugins/Releasing/Submit+your+plugin) |
| **Figma Community** | Publish from the Figma desktop app (2FA required) | Human review | Free. Paid plugins need approved-creator status, $2 minimum, Stripe | [Publish plugins](https://help.figma.com/hc/en-us/articles/360042293394-Publish-plugins-to-the-Figma-Community) |
| **npm** | `npm publish` | None | Free for public packages | [npm docs](https://docs.npmjs.com/cli/commands/npm-publish) |
| **Homebrew** (CLI tools) | Pull request to homebrew-core / homebrew-cask, or your own tap | Maintainer review with acceptance criteria | Free | [Homebrew docs](https://docs.brew.sh/) |

## Steps

### Level 1: Get published
1. **Pick every marketplace your users use (5 min).** A VS Code extension should also go to **Open VSX**, otherwise
   Cursor and VSCodium users can't install it from their editor.
2. **Meet the basics (30 min):** a unique ID/name (Obsidian IDs can't contain "obsidian"), semantic versioning,
   a LICENSE, and a README that says what it does and how to use it.
3. **Assets (20 min):** an icon (128×128 is common: VS Code, Figma), a GIF of the plugin in action, and screenshots
   (Figma: a 1920×1080 thumbnail).
4. **Submit** using the table. For PR-based stores (Raycast, Homebrew), **answer reviewer comments quickly**. Stale PRs get closed.
5. **Automate releases** (optional): GitHub Actions can publish to VS Code + Open VSX on each tagged release.

### Level 2: Get found
1. **The README/description is the listing.** Open with a GIF, then one sentence, then install and usage steps.
2. **Search terms:** put the words people search for in the display name, the description and the
   keywords/categories fields (VS Code `keywords` and `categories` in `package.json`).
3. **Link from where users look:** the tool's forum or Discord "share your plugin" channels, relevant awesome lists
   (PR), and r/vscode, r/ObsidianMD, r/raycast (follow the rules).
4. **Ask for ratings/stars** in your changelog or after a successful action, never in exchange for anything.

### Level 3: Grow
- **Ship small updates often.** Changelogs appear in-app on several marketplaces.
- **Cross-publish:** a popular Obsidian plugin can become a Raycast command, and a VS Code extension can become a JetBrains plugin.
- **Sponsorship or a paid tier:** GitHub Sponsors or Ko-fi links in the README, or paid plugins where supported (JetBrains, Figma).
- **Case study your growth** → [case-study-write-your-own](../../case-study/case-study-write-your-own/SKILL.md).

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are a developer-tools distribution expert. Help me publish my plugin/tool.

What it is: {{e.g. VS Code extension that...}}   Works with: {{VS Code / JetBrains / Raycast / Obsidian / Figma / CLI}}
Repo: {{link}}   Paid or free: {{...}}

1. List every marketplace I should publish to (include Open VSX for VS Code extensions) with the exact submit steps
   and commands for each.
2. Check my metadata against each marketplace's rules: ID/name, version, license, required files, icon/assets.
3. Rewrite my README opening for the marketplace listing: GIF placeholder, one-sentence value, install, usage, settings.
4. Suggest search keywords/categories and 3 community places to announce it (with their self-promotion rules).
5. A GitHub Actions outline to publish on tagged releases (if relevant).
Mark anything uncertain as TODO.
````

## Example output

> **Illustrative example.** Fictional plugin, shown for format.

*md-linkmap*, a VS Code extension that shows Markdown backlinks → **VS Code Marketplace + Open VSX** via one GitHub Action
on tag `v*`. Keywords: `markdown, backlinks, wiki, notes, zettelkasten`. README opens with a 6-second GIF of the backlinks
panel. Announced on r/vscode and in the Obsidian forum's "share & showcase" section (as a related tool).

## Common mistakes
- **Publishing only to the VS Code Marketplace.** Open VSX editors can't install it.
- **A README without a GIF or usage steps.** It's your store page.
- **Ignoring PR review comments** on Raycast or Homebrew until the PR is closed as stale.
- **Obsidian: a release tag that doesn't match `manifest.json`'s version**, or missing release files.

## Related skills
- [listing-free-directories](../listing-free-directories/SKILL.md): DevHunt, Product Hunt, AlternativeTo for dev tools.
- [research-where-users-ask](../../research/research-where-users-ask/SKILL.md): where developers ask for tools.
- [launch-post-writing](../../launch/launch-post-writing/SKILL.md): a Show HN post for your tool.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources are linked in the table above. Processes change, so read each
marketplace's current guide before submitting.
