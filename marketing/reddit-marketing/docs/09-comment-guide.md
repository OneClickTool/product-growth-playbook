# 09 · Reddit comments: the complete guide

Everything about answering on Reddit in one page: what comments actually bring, how Reddit decides who sees them,
which threads to pick, how to write one that ends up on top, when to mention your product, and how to tell if it's
working. Short version: [05-comment-playbook.md](05-comment-playbook.md). Agent version with a prompt:
[social-reddit-comment](../skills/social-reddit-comment/SKILL.md).

Labels, as in [03-how-reddit-ranks.md](03-how-reddit-ranks.md): **Code** (Reddit's archived open-source code),
**Help** (Reddit's rules and help pages), **Secondary** (news, mod announcements read via mirrors, third-party
guides), **Practice** (what builders see; test it yourself). Sources at the end.

## 1. Does commenting actually help?

Yes, if "commenting" means answering real questions well. No, if it means dropping your link under every thread you
can find. Honest expectations:

**What comments give you**
- **Karma in the subreddits you'll post in later.** Many buyers' subreddits set karma or account-age minimums, and
  AutoModerator removes posts from accounts below them (**Help** + subreddit rules). Comments are how you get there
  without spamming.
- **Answers that keep being read.** A thread that ranks in Google for a question gets new readers for years. Reddit
  content is surfaced in Google products under a 2024 partnership (**Help**, Reddit blog), and Reddit's own AI search,
  Reddit Answers, summarizes conversations and links back to them (**Secondary**).
- **Profile visits.** A reader who liked your answer clicks your name. That's where your X account, your landing page
  and your other answers are ([02-profile-setup.md](02-profile-setup.md)). The comment doesn't need a link for this
  to happen.
- **Users' own words.** Every "is there an app that…" thread tells you the problem, the words people search with and
  what they already tried. That feeds your landing page, store listing and next post.
- **A reputation you can point to.** "I've been answering clipboard questions here for months" is believable when
  your history shows it.

**What comments don't give you**
- **Instant traffic.** Most answers are read by a few dozen people at most (**Practice**). The value adds up over
  weeks, not days.
- **Buyers from builders' subreddits.** r/SideProject or r/indiehackers give karma, feedback and peers, rarely
  customers ([01-strategy.md](01-strategy.md#buyers-vs-builders)).
- **Anything, if the answer is generic.** "There are many apps for this" earns nothing on any subreddit.

**Fair test:** 2–3 good answers a day in 3–5 buyers' subreddits for 6–8 weeks, then judge with the numbers in
[§10](#10-is-it-working). Less than that, and you're judging noise.

## 2. How Reddit decides who sees your comment

- **"Best" is the usual default sort for comments** (**Secondary**, many subreddits change it). It ranks a comment by
  how sure Reddit is that people like it: the lower bound of a confidence interval on the share of upvotes (the
  Wilson score, described by Evan Miller and adopted by Reddit in 2009). In plain words: a comment with 1 upvote and
  0 downvotes is not trusted yet and stays low; one with 10 up and 1 down can beat one with 40 up and 20 down.
  **So a clearly useful answer can rise even if it's not first, but it needs some readers to vote early.**
- **Threads go quiet fast.** Posts drop out of "hot" on a fixed clock (**Code**). Fewer readers means fewer votes,
  so a great answer 10 hours late is seen by few. Exception: old threads that rank in Google, which keep getting
  readers.
- **"Top", "New", "Controversial"** are other sorts readers can pick. On "New", the newest answer is first, which
  helps late answers in small threads.
- **Specific beats long.** The top answer is usually the one with steps, a number, a menu path or a clear
  comparison (**Practice**).
- **Replies to the top comment are also read.** If the top answer is mostly right, a reply that adds the missing
  step can get more views than a new top-level comment buried below (**Practice**).

## 3. Hidden filters that can make your comment invisible

You can post a comment and nobody else sees it. Common reasons:

- **AutoModerator rules** per subreddit: account age, karma, links, keywords. You usually get no message
  (**Practice**).
- **Contributor Quality Score (CQS).** Since 2023 moderators can filter by Reddit's internal score, which sorts
  accounts into 5 tiers using signals such as past actions on the account and whether it's verified, for example
  with an email (**Secondary**, r/modnews announcement). New, unverified accounts that only post links score low.
- **Crowd Control**, a per-subreddit setting that collapses or filters comments from people new to that community
  (**Secondary**).
- **Reddit's spam filter**, for repeated text, masked links and link shorteners (**Help**).

**Habits that keep you visible:** verify your email, set up the profile before your first comment, comment without
links for the first 1–2 weeks, never paste the same text twice, and check every comment logged out (private window)
after 10 minutes. Gone? See [08-rules-and-risks.md](08-rules-and-risks.md#is-my-account-hidden).

## 4. Picking threads worth answering

Full search method: [04-finding-threads.md](04-finding-threads.md). Before writing, run this quick check.

**Answer if all are true**
1. Someone asks something you know first-hand (you built for it, tested it or fixed it).
2. The thread is fresh (a few hours old, still getting views) **or** old but ranks in Google for that question.
3. The current answers are missing something you can add: a step, a number, a gotcha, a free option, a comparison.
4. The subreddit allows the kind of answer you'd give.

**Skip if**
- the top answer is already complete and you'd only repeat it,
- it's a rant without a question, homework, politics or a fight,
- you'd only be there to mention your product.

**Good thread types for a software maker (Practice)**
- "Is there an app that…" / "any app for…"
- "Alternative to X?" (especially after a price change or a shutdown)
- "How do I stop my Mac / phone / browser from…"
- "X vs Y?" and "What do you use for…?"
- A bug or limitation you fixed in your own product. You know the root cause.

## 5. Anatomy of a comment that ends up on top

```text
Line 1      The answer, in one sentence. No "Great question!".
Body        How: steps with exact menu names, versions, sizes, prices. 2–5 short lines or a numbered list.
Proof       One first-hand detail: "I tested this on a 2021 MacBook Air", "took me about 2 minutes".
Caveat      When it won't work, or who should pick something else.
Optional    Your product, last, with a disclosure line (only if §7 says yes).
Optional    One question back, if it helps them ("Are you on Sonoma or Sequoia?").
```

**Length:** match the thread. A one-line question gets a short, exact answer; "what's the best app for…" earns a
comparison of 3 options (**Practice**). Long is fine when every line is useful, but most good answers fit on one
phone screen.

**Formatting that helps on Reddit:** numbered lists for steps, `code` for commands and paths, **bold** for the
one thing they must not miss. One link at most, only if needed.

## 6. Six shapes, with worked examples

Pick one shape per answer. The table version is in [05-comment-playbook.md](05-comment-playbook.md#six-answer-shapes).

> **Illustrative example.** Every thread, product and number below is fictional. Clipnest is a made-up Mac
> clipboard app.

**Direct fix:** there's a built-in way.

> *Thread (r/MacOS):* "How do I see the full path of a file in Finder?"
>
> *Answer:* "View → Show Path Bar puts it at the bottom of every Finder window. To copy it, right-click the file,
> hold Option, and pick 'Copy … as Pathname'. No app needed."

**Steps:** it takes a few actions.

> *Thread (r/applehelp):* "My Downloads folder is 40 GB, how do I clean it safely?"
>
> *Answer:* "1. In Finder, open Downloads. 2. Switch to list view (Cmd+2) and click the Size column to sort; the
> top 10 files are usually most of it (old .dmg installers, videos). 3. Move them to the Trash,
> not delete straight away, and empty it after a week. 4. To stop it filling again, Safari → Settings → General →
> 'Remove download list items: after one day' only clears the list, not the files, so set a reminder or use a
> cleaner app."

**Honest comparison:** "what's the best app for…".

> *Answer:* "Depends on what you need most. Free and simple: the built-in way above. Search inside images: you
> need an app with text recognition; App A does it but is subscription-only. Privacy: pick one that keeps history
> only on your Mac, App B does. I'd try two free tiers for a week and keep the one you actually open."

**First-hand experience:** you lived it.

> *Answer:* "I had the same thing after upgrading: Spotlight indexing ate the CPU for about a day. It stopped on its
> own; if it doesn't after 48 hours, System Settings → Spotlight → Search Privacy, add the drive, wait a minute,
> remove it. That rebuilds the index."

**Product answer:** your app genuinely is the answer (all five checks in §7 passed).

> *Answer:* "macOS only keeps the last thing you copied, so it's gone once replaced. Any clipboard history app fixes
> it; look for one that stores history locally. Disclosure: I made one, Clipnest, free for 50 clips. The free ones
> work too."

**Clarifying question:** the question is vague.

> *Answer:* "Is this on battery or plugged in? If battery: it's probably Low Power Mode, which throttles background
> apps (battery icon in the menu bar). If plugged in, check Activity Monitor → Energy for the app at the top."

## 7. Mentioning your product without getting removed

**The five checks** (all must be yes), from [05-comment-playbook.md](05-comment-playbook.md#when-to-mention-your-product-all-must-be-yes):
1. It answers the exact question, not a nearby one.
2. The comment is already useful without it.
3. The subreddit's rules allow it.
4. After this one, fewer than 1 in 10 of your recent comments there mention your products.
5. You say it's yours.

**How to count the ratio:** keep a [thread tracker](../templates/thread-tracker.md) per subreddit. 9 answers with no
mention, then 1 with a mention, is the safe pattern. Many subreddits use this 10% rule, and Reddit's own help pages
describe it as a common community rule (**Help**).

**Where it goes:** last. The reader should get their answer before they see your name.

**Disclosure lines that read naturally**
- "Disclosure: I made this one, so take it with salt."
- "I'm the developer of X, which does this, but the free way above works too."
- "Full disclosure, it's mine. Happy to answer anything about it."

**Link or no link?**
- No-promotion subreddits: no product name, no link. Your profile does the work.
- Allowed with disclosure: the name is often enough; people search it. Add a link only if the rules allow, never
  shortened or masked, with UTM: `?utm_source=reddit&utm_medium=comment&utm_campaign=<subreddit>`.
- Someone asks "what's the app called?" in a reply: answer it there. A reply to a direct question is the most
  natural place for a link.

**Never:** "I found this cool app" about your own app (Rule 5, misleading about who you are), friends or other
accounts upvoting (Rule 2, vote manipulation), DMing people who didn't ask (spam).

## 8. Writing so it reads like a person

Subreddits remove posts and comments that read like AI or ads, and readers downvote them (**Practice**, and many
rules pages say so). Avoid:

- openers like "Great question!", "As someone who…", "Absolutely!",
- marketing words: "game-changer", "seamless", "powerful", "revolutionize", "boost your productivity",
- a perfect three-part structure with a summary line at the end,
- emoji bullets, headings in a short comment, many bold phrases,
- the same opening sentence in every answer,
- features or numbers you can't back up.

Do: short sentences, your own opinion ("I'd skip X, it nags for a subscription"), one small imperfection is fine,
exact names and numbers. If an AI helped you draft, rewrite it in your words and check every fact; posting with
bots or AI tools on your behalf is spam under Reddit's rules (**Help**).

## 9. After you post

1. **10 minutes later:** open it logged out. Not there? [§3](#3-hidden-filters-that-can-make-your-comment-invisible).
2. **Same day:** come back once and answer every reply. Follow-ups are where readers decide to try something.
3. **Wrong about something?** Edit and add "Edit: corrected the menu path, thanks u/…". Don't delete a useful
   answer because it got few votes.
4. **Removed by a moderator?** Don't argue in the thread or repost. Re-read the rules; message the moderators
   politely if you can't see why.
5. **Log it** in the [comment file](../templates/comment-file.md): the answer, its shape, whether the product was
   mentioned, score after 2 days. Good answers are reusable later, rewritten in new words for the new thread.

## 10. Is it working?

Weekly table: [templates/weekly-numbers.md](../templates/weekly-numbers.md). Stop rules:
[07-metrics-and-stop-rules.md](07-metrics-and-stop-rules.md).

| Signal | Where to see it | Means |
|---|---|---|
| Answers removed | thread tracker, checked logged out | Should be 0. One = re-read that subreddit's rules |
| Score after 2 days | your profile | Rising over weeks = you're picking the right threads |
| Karma in each target subreddit | profile, the subreddit's minimums | When you pass the minimum, you can post there |
| Replies asking "what app is that?" | inbox | People want what you make |
| Landing visits `utm_source=reddit` | analytics, split by `utm_medium` (comment / profile) and `utm_campaign` (subreddit) | Which subreddit and which route send people |
| Trials or installs from Reddit | store or checkout, same UTM | Which subreddit sends **buyers** |

Use `utm_medium=profile` on your profile links and `utm_medium=comment` on comment links. Visits from `profile`
are the comments working even though they had no link.

## 11. The 15-minute daily routine

Full flow: [flow/daily-flow.md](../flow/daily-flow.md).

1. **5 min:** keyword alerts + your 3–5 subreddits sorted by *new*. Pick 2–3 threads.
2. **10 min:** answer them with this page's checklist below. Product in at most 1 of 10.
3. **Evening, 2 min:** reply to replies; update the tracker.

## 12. Common mistakes

- **Link-dropping.** A link with one line of text reads as an ad, gets removed, and teaches moderators your
  name.
- **Copy-paste answers.** Same text in many threads is spam under Reddit's rules, even if each is "helpful".
- **Answering only where you can mention the product.** Your history shows it, and the 1-in-10 ratio breaks.
- **Late answers to dead threads** that don't rank in Google. Few readers, no votes.
- **Fighting a downvote or a moderator.** It never wins and gets noticed.
- **Judging after a week.** Comments compound; give it 6–8 weeks.

## Checklist before you hit Reply

```text
[ ] I know this first-hand, and the thread is fresh or ranks in Google
[ ] Line 1 is the answer
[ ] Specifics: menu path / version / number / price
[ ] Useful without my product
[ ] Product mention: all 5 checks yes? Last, with disclosure? (else: none)
[ ] No shortened link; UTM if any link
[ ] Doesn't read like an ad or AI; not a copy of another answer
[ ] I'll check it logged out in 10 min and come back for replies
```

## Sources

Checked 2026-10-26. More with dates: [reference/reddit-facts.md](../reference/reddit-facts.md).

- [Reddit Rules](https://redditinc.com/policies/reddit-rules): Rule 2 (no spam, no vote manipulation), Rule 5
  (don't mislead about who you are). **Help**
- [Reddit Help: Spam](https://support.reddithelp.com/hc/en-us/articles/360043504051-Spam): repeated posting,
  unsolicited DMs, bots or AI posting for you, masked links. **Help**
- [Reddit Help: keeping spam out of a community](https://support.reddithelp.com/hc/en-us/articles/28012014962580-How-do-I-keep-spam-out-of-my-community):
  the 10% self-promotion ratio. **Help**
- [Reddit blog, 2024](https://redditinc.com/blog/expanding-our-partnership-with-google): Reddit content in Google
  products. **Help**
- [Evan Miller, "How Not To Sort By Average Rating"](https://www.evanmiller.org/how-not-to-sort-by-average-rating.html)
  and [Amir Salihefendic, "How Reddit ranking algorithms work"](https://medium.com/hacking-and-gonzo/how-reddit-ranking-algorithms-work-ef111e33d0d9):
  the Wilson lower bound behind the "Best" comment sort, introduced by Reddit in October 2009. **Secondary**
- r/modnews, Sep 2023, "Contributor Quality Score available to all" (read via a
  [mirror](https://lr.vern.cc/r/modnews/comments/16is6dh/contributor_quality_score_available_to_all/)): 5 tiers,
  signals. **Secondary**
- [Engadget, Dec 2024](https://www.engadget.com/social-media/reddit-introduces-ai-powered-reddit-answers-search-feature-140028655.html):
  Reddit Answers summarizes conversations and links to them. **Secondary**
- [reddit-archive/reddit](https://github.com/reddit-archive/reddit) `r2/r2/lib/db/_sorts.pyx`: the archived "hot"
  and "confidence" sorts. **Code**
