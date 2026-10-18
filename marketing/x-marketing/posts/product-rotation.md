# Product rotation: 5 products, one post each a week

> Disclosure: all five are made by the maintainer of this repo (OneClickTool). Every feature and offer below is
> copied from the product's own page, **checked 2026-10-11**. No user counts, no reviews, no results. Re-check the
> store before quoting a price. How the rotation fits the day: [flow/a-day-on-x.md](../flow/a-day-on-x.md).
> Blank template: [templates/product-rotation.md](../templates/product-rotation.md).

## The five

| Slot | Product | Who on X | Offer (checked 2026-10-11) | Post day |
|---|---|---|---|---|
| Hero | [Sweepy](https://oneclicktool.app/macos/sweepy?utm_source=x&utm_medium=post&utm_campaign=sweepy) | Mac users with a messy Downloads / Desktop | Free for 2 folders. Pro $9.99 once (US price), in-app | Tue + Sun ask |
| Hero 2 | [Markdown Everywhere](https://oneclicktool.app/desktop/markdown-everywhere?utm_source=x&utm_medium=post&utm_campaign=markdown-viewer) | Devs with folders of .md notes, docs, AI skill files | Free app. Pro: 14-day trial, then $9.99 once | Thu |
| Reach | [AgentBell](https://oneclicktool.app/macos/agentbell?utm_source=x&utm_medium=post&utm_campaign=agentbell) | Devs running Claude Code / Codex in a terminal | Free, every feature | Mon |
| Reach 2 | [Edge Tabs](https://oneclicktool.app/macos/quickcheck?utm_source=x&utm_medium=post&utm_campaign=quickcheck) | Mac users who juggle small to-dos | Free, no ads, no in-app purchases | Wed |
| Story | [Redliner](https://oneclicktool.app/macos/redliner?utm_source=x&utm_medium=post&utm_campaign=redliner) | Freelancers, people who sign contracts | In development. Planned: first 3 pages free, Pro $14.99 once | Sat |

Which hook goes in which week is set in [plan-30-days.md](plan-30-days.md) (week 1 =
[week-01-starter.md](week-01-starter.md) already used AgentBell A + C, Sweepy A, Markdown Everywhere A, Redliner's
long post). After the D/E hooks, write new ones from the [fact bank](../templates/fact-bank.md). Never post the same
text twice.

---

## AgentBell · Reach · Monday

**Facts from the page:** sound + large banner when Claude Code waits or an agent finishes · shows over full-screen
apps · click the banner → terminal comes to the front · one-click Connect, saves a config backup first, Remove
restores it · reminders if you don't answer · "Quiet for 1 hour" · Terminal, iTerm2, Ghostty, Warp, VS Code
terminal · Codex only reports when it finishes, not when it waits for approval · macOS 14+ · free, no account.

**Demo shot list (15 s):** Claude Code running → switch to browser full screen → banner drops in with sound →
click → back in the terminal at the approval prompt.

**Hook A · pain**
```text
Claude Code asked for approval 20 minutes ago. You were in another window. It's still waiting.

Made a free menu bar app for that: AgentBell plays a sound and shows a big banner, even over full-screen apps. Click it and you're back in the terminal.
```

**Hook B · honest limit (builds trust)**
```text
What AgentBell can and can't do, straight:

Claude Code: alerts when it's waiting for you AND when it's done.
Codex: only when it finishes. Codex doesn't report "waiting for approval", so no app can catch that yet.

Free, Mac. Works in Terminal, iTerm2, Ghostty, Warp and the VS Code terminal.
```

**Hook C · behind the scenes**
```text
Design rule for AgentBell: "Connect" edits your Claude Code config, so it saves a backup first, and "Remove" puts the file back exactly as it was.

If your tool touches someone's config, give them a way back.
```

**Hook D · the small settings**
```text
Two settings I added to AgentBell after using it myself:
· reminders, if you still haven't answered the agent
· "Quiet for 1 hour", for meetings

An alert app that can't be quieted gets uninstalled.
```

**Hook E · question (works as a reply magnet)**
```text
Which terminal do you run Claude Code in?
Terminal, iTerm2, Ghostty, Warp, or the VS Code terminal?

(Asking because my free alert app has to bring the right one to the front when you click the banner.)
```

First reply: `https://oneclicktool.app/macos/agentbell?utm_source=x&utm_medium=reply&utm_campaign=agentbell`

**Link it in a reply when someone…** complains they missed an approval prompt, asks how to get notified when Claude
Code / an agent finishes, or shares a "came back after an hour and it was waiting" story.

---

## Sweepy · Hero · Tuesday (+ Sunday ask)

**Facts from the page:** finds duplicates byte for byte, even across folders · keeps the plain-named first copy ·
flags .dmg/.pkg older than 7 days · flags files not opened in 90+ days and files of 500 MB+ (never pre-selected) ·
real thumbnails · sorts loose files by type and month (e.g. `Images/2026-09`) · skips live downloads ·
moves to Trash, never deletes · undo for 7 days (Free) / 30 days (Pro) · Free watches 2 folders, Pro unlimited ·
macOS 14+, Mac App Store.

**Demo shot list (20 s):** Downloads full of `report (1).pdf, report (2).pdf…` → Sweepy scan → duplicates and old
`.dmg` marked → clean → Undo → files back.

**Hook A · lesson**
```text
What fills a Mac's Downloads folder, from building a cleaner for it:
1. the same file downloaded again and again
2. .dmg installers you ran once
3. one forgotten screen recording eating gigabytes

Sweepy sends them to the Trash, never deletes for good, and can undo the whole cleanup.
```

**Hook B · the fear (why people don't clean)**
```text
Nobody cleans Downloads because one wrong delete hurts more than 40 GB of junk.

So Sweepy never deletes: everything goes to the Trash, and a whole cleanup can be undone for 7 days (30 on Pro). Big and old files are flagged but never pre-selected.
```

**Hook C · small detail**
```text
Tiny rule I like in Sweepy: duplicates are matched byte for byte, not by name, and it keeps the plain-named copy you downloaded first. "report (3).pdf" goes, "report.pdf" stays.
```

**Hook D · organizing, not deleting**
```text
Cleaning isn't only deleting. Sweepy can also sort loose files by type and month, so the Desktop pile becomes Images/2026-09, Documents/2026-10…

And it leaves files that are still downloading alone (.crdownload, .part).
```

**Sunday ask**
```text
If your Downloads folder is a mess: Sweepy is free on the Mac App Store for 2 folders. Pro is $9.99 once, no subscription. Link in reply.
```

First reply: `https://oneclicktool.app/macos/sweepy?utm_source=x&utm_medium=reply&utm_campaign=sweepy`

**Link it in a reply when someone…** asks how to free up Mac storage, shows a "Storage full" screenshot, or asks
for a duplicate-file finder.

---

## Edge Tabs · Reach · Wednesday

**Facts from the page:** paste lines → a clean checklist (bullets, numbers, blank lines removed) · up to 10 notes as
colored tabs on the right edge · slide out on hover · never steals focus · in every Space, even full screen ·
progress bar per note · toss with Undo · history 30 days · ⌘N, ⌘1–⌘9, Space to tick · offline, no account ·
macOS 14+ · free, no ads, no in-app purchases.

**Demo shot list (15 s):** copy 5 lines from a chat → paste → checklist appears as a tab on the screen edge →
hover → tick with Space → tab tucks away.

**Hook A · pain**
```text
Small tasks shouldn't need a big app.

Edge Tabs: paste a few lines, get a checklist that lives as a colored tab on the edge of your Mac screen. Hover to open, Space to tick. Never steals focus. Free, no account.
```

**Hook B · workflow**
```text
My AI-agent workflow on a Mac: ask the agent for a plan → copy the steps → paste into a sticky tab on the screen edge → tick them off while it works.

Bullets and numbers get cleaned up on paste. Free app, called Edge Tabs.
```

**Hook C · behind the scenes**
```text
Rule I kept for Edge Tabs: it must never steal focus. You're typing in another app, a note slides out on hover, and your cursor stays where it was.

Small utilities live or die on that one detail.
```

First reply: `https://oneclicktool.app/macos/quickcheck?utm_source=x&utm_medium=reply&utm_campaign=quickcheck`

**Link it in a reply when someone…** asks for a simple to-do / sticky-note app for Mac, or says their to-do app is
too heavy.

---

## Markdown Everywhere · Hero 2 · Thursday

**Facts from the page:** map view (each file a card, arrows for links, orange dot on files nothing links to) · table
view with links in/out and last update · reader for tables, code, task lists, local images · full-text search ·
free app is read-only, up to 10 folders · Pro adds editing, notes, unlimited folders and a Claude panel that uses
your own Claude Code login (Mac download from the site only) · Pro: 14-day trial, then $9.99 once, one key on 2
computers · macOS 11+ and Windows 10/11.

**Demo shot list (20 s):** open a folder of AI skill files → map view with arrows → orange dot on an orphan file →
switch to table → sort by last update.

**Hook A · question**
```text
Devs who live in Markdown: where do your notes and AI skill files end up?
One repo, a notes app, or 10 folders you never open again?

(I made a free viewer that shows a whole folder as a map and a table, Mac & Windows.)
```

**Hook B · the orphan file**
```text
Opened my AI skills folder as a link map. Files with an orange dot = nothing links to them.

Half of my "documentation" was notes no other file pointed to. Nobody was ever going to find them.

Free app: Markdown Everywhere, Mac & Windows.
```
> Before posting B: keep the "half" only if it's true for your folder; otherwise write your real count or cut it.

**Hook C · offer (use on a week it's the Sunday product instead of Sweepy)**
```text
Markdown Everywhere Pro adds editing, notes on the map, unlimited folders, and a Claude panel that knows your CLAUDE.md and skills, using your own Claude Code login, no API key.

14-day free trial, then $9.99 once. The viewer stays free.
```

**Hook D · safe to open anything**
```text
Opening a random repo's docs folder to read it? The free Markdown Everywhere viewer is read-only: it can't edit, move or delete a file, and it strips scripts before showing anything.

Mac & Windows, free.
```

First reply: `https://oneclicktool.app/desktop/markdown-everywhere?utm_source=x&utm_medium=reply&utm_campaign=markdown-viewer`

**Link it in a reply when someone…** asks how to organize CLAUDE.md / skills / docs folders, or asks for a Markdown
viewer that shows a whole folder.

---

## Redliner · Story · Saturday (long post)

**Planned, not shipped:** say "building", never "available". Details as on the page (checked 2026-10-11): old and new
side by side, every added / removed / changed word highlighted with its page · PDF, Word, RTF, text, scanned PDFs ·
the two files don't need the same format · filter for changed amounts, dates and percentages · runs on the Mac, no
account · planned: first 3 pages free, Pro $14.99 once.

**Hook A · long post**: use the Saturday post in [week-01-starter.md](week-01-starter.md).

**Hook B · poll**
```text
Building a Mac app that compares two versions of a document and highlights every change.

What do you compare most?
· contracts
· quotes / invoices
· policies / terms
· my own drafts
```

**Hook C · the one number**
```text
The change that hurts in a contract is never a paragraph. It's one number: 30 days → 15, 2% → 3%.

So the app I'm building has a filter that shows only changed amounts, dates and percentages.
```

**Hook D · mixed formats**
```text
The other side sends a Word file. You signed the PDF. Sometimes the old version is a scan.

The Mac app I'm building compares them anyway: PDF vs Word vs RTF vs text, scanned PDFs included, every change highlighted with its page.
```

Link (waitlist / landing): `https://oneclicktool.app/macos/redliner?utm_source=x&utm_medium=reply&utm_campaign=redliner`

---

## Checklist before any product post
- [ ] Offer matches the store / page **today**.
- [ ] Clip shows no personal files, emails, paths or notifications.
- [ ] Only one product post today; this product hasn't been posted this week.
- [ ] Link is in the first reply, with `utm_medium=reply`.
