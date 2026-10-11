# Talk bank: non-promo posts for reach, follows and trust

The 9–10 posts a week that **don't sell anything** ([flow/a-day-on-x.md](../flow/a-day-on-x.md)). Written for an
indie dev who makes Mac apps and uses AI coding agents; change the topics to your buyers' world.

> Rules: every tip below was checked to work on 2026-10-11 (macOS 14+, current Claude Code, git 2.x). Re-test before
> you post it, in your own words. Lines with `<…>` need **your real** number or story, or delete them. Never post the
> same text twice. Product posts live in [product-rotation.md](product-rotation.md).

Pick by what you want from the post:

| Want | Section | Ranker signal it aims for (Code) |
|---|---|---|
| Shares, bookmarks | A · Tips | copy-link share (weight 20), dwell |
| Replies | B · Questions & polls, C · Takes | reply (5, +15 between mutuals) |
| Follows, trust | D · Build log, E · Honest numbers | profile click, follow |
| Reach on other people's posts | F · Reply openers | reply prioritization (Premium) |

---

## A · Tips (people save and send these)

**A1 · Mac**
```text
Mac tip: in Finder press ⌘⇧. (Command-Shift-Period) to show hidden files. Same keys again to hide them.
```

**A2 · Mac**
```text
Mac: you can "cut and paste" files in Finder.
⌘C to copy, then ⌥⌘V (Option-Command-V) to move them instead of copying.
```

**A3 · Mac**
```text
Need the full path of a file on a Mac?
Select it in Finder, press ⌥⌘C (Option-Command-C). Path is on your clipboard.
```

**A4 · Mac**
```text
Mac: ⌘⇧5 opens the screenshot toolbar, and it also records the screen.
Options → "Save to" lets you stop screenshots from landing on your Desktop.
```

**A5 · Mac terminal**
```text
Keep a Mac awake while a long build or an AI agent runs:

caffeinate -i <your command>

It stays awake until the command finishes, then goes back to normal.
```

**A6 · Mac terminal**
```text
Pipe anything to your Mac clipboard from the terminal:

git diff | pbcopy

pbpaste does the reverse.
```

**A7 · Mac terminal**
```text
Spotlight search from the terminal, faster than find for big folders:

mdfind -name invoice -onlyin ~/Documents
```

**A8 · Mac**
```text
Mac: press Space on any file in Finder to preview it (Quick Look).
Arrow keys move to the next file while the preview stays open.
```

**A9 · git**
```text
git tip: go back to the branch you were just on.

git switch -

Works like "cd -".
```

**A10 · git**
```text
Find the commit that added or removed a string anywhere in history:

git log -S "functionName" --oneline
```

**A11 · Claude Code**
```text
Claude Code tip: press Shift+Tab to cycle into plan mode.
It reads and plans first, then waits for your OK before touching files.
```

**A12 · Claude Code**
```text
Claude Code tip: put the rules you keep repeating in a CLAUDE.md at the repo root.
It's loaded every session, so you stop typing "use pnpm, not npm" every morning.
```

**A13 · Claude Code**
```text
Claude Code going the wrong way? Press Esc to stop it mid-step.
Press Esc twice to jump back to an earlier message and try again from there.
```

**A14 · indie checklist (thread / long post)**
```text
Before you post your app anywhere, check 5 things:
1. The store page says who it's for in the first line
2. The first screenshot shows the result, not the menu
3. The price on your site matches the store
4. Your link has UTM tags so you know what worked
5. Someone who isn't you installed it today
```

---

## B · Questions & polls (people answer these)

**B1**
```text
Devs using AI agents: do you read every diff before you accept it, or only the ones that "look big"?
Honest answers only.
```

**B2 · poll**
```text
Where do you keep your to-dos while coding?
· a to-do app
· a text file
· sticky notes / paper
· my head, unfortunately
```

**B3**
```text
What's the one Mac app you install first on a new machine?
Not counting the browser.
```

**B4 · poll**
```text
Paying for a small Mac utility, you prefer:
· one-time price
· subscription with updates
· free + one Pro unlock
· free only, I don't pay for utilities
```

**B5**
```text
Claude Code or Codex users: what's the longest you've left an agent waiting for you without noticing?
```

**B6**
```text
Indie devs: what's the feature you built that nobody used?
Mine: <your real one>.
```

**B7 · poll**
```text
How many apps do you really need to ship before one pays rent?
· 1, pick well
· 3–5
· 10+
· it's not about count
```

---

## C · Takes (opinions you'd defend in the replies)

Post only takes you actually hold. A take with a reason gets replies; a hot take for engagement gets mutes.

**C1**
```text
Small apps don't need more features. They need fewer clicks between opening the app and the first "oh nice".
```

**C2**
```text
The best marketing for a utility app is the screenshot of the problem, not the app.
People recognize their own messy Downloads folder faster than your UI.
```

**C3**
```text
AI agents made writing code cheap. They didn't make deciding what to build cheap.
That's still the whole job.
```

**C4**
```text
If your app touches a user's files or config, "Undo" is not a feature. It's the price of being trusted.
```

**C5**
```text
"Free" with no account, no ads and no tracking is a real selling point now. Say it on the first screen.
```

---

## D · Build log (follows come from watching you build)

**D1 · bug story**
```text
Spent <time> on a bug: <symptom>.
Cause: <cause, plain words>. Fix: <fix>.
Lesson: <one line>.
```

**D2 · before / after**
```text
<Screen> before vs. after this week.
What changed: <one thing>. Why: <what users / you noticed>.
```
Attach both screenshots.

**D3 · decision**
```text
Decided not to add <feature> to <app>.
Reason: <one honest reason>.
Would you have added it?
```

**D4 · tools I use**
```text
What I use to ship small Mac apps as one person:
· editor: <…>
· AI agent: <…>
· screen recording: <…>
· analytics: <…>
What would you swap?
```

**D5 · review / rejection**
```text
App Store review this week: <approved in N h / rejected because …>.
What I changed: <…>.
```

---

## E · Honest numbers (trust; only real, dated numbers)

**E1 · weekly**
```text
Week <N> of posting here daily:
Impressions: <A> → <B>
Profile visits: <A> → <B>
What moved it: <one thing>
What didn't: <one thing>
```

**E2 · the flop**
```text
Launched <thing> on <date>. Result: <real small number>.
What I think went wrong: <…>. What I'm trying next: <…>.
```
Flops posted honestly tend to earn more trust than wins (**Practice**, test it).

**E3 · pattern from your own analytics**
```text
28 days of my X analytics in one line: <fill from flow/analytics-pattern.md>.
Replies did more than posts. Here's the chart.
```

---

## F · Reply openers (for the reply sessions, not your own posts)

Start the reply with one of these, then add the real content. Never paste the same reply twice.

| Shape | Opener |
|---|---|
| Number | "Same here, with numbers: <…>" |
| Counter-example | "Didn't work for me: tried <…>, got <…>, because <…>." |
| Screenshot | "Here's what that looks like on my side:" + image |
| How-to | "The 2-step version: 1) <…> 2) <…>" |
| Question | "How did you handle <specific thing>? I got stuck on it." |
| Add a tip | "One more for the list: <tip from section A>." |

Full playbook: [docs/06-reply-playbook.md](../docs/06-reply-playbook.md) ·
skill: [social-x-reply](../skills/social-x-reply/SKILL.md).
