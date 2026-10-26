# 05 · Comment playbook

Comments are 80% of the work on Reddit and most of the trust. Agent version with a prompt:
[social-reddit-comment](../skills/social-reddit-comment/SKILL.md). File format to keep them:
[templates/comment-file.md](../templates/comment-file.md). The long version, with what comments bring, how Reddit
sorts them, hidden filters and worked examples: [09-comment-guide.md](09-comment-guide.md).

## Six answer shapes

| Shape | Use when | Opening |
|---|---|---|
| **Direct fix** | There's a built-in way to do it | "You can do this without any app: …" |
| **Steps** | It takes a few actions | "1. … 2. … 3. …" with exact menu names |
| **Honest comparison** | "What's the best app for…" | 3 options, what each is best and worst at, who should pick which |
| **First-hand experience** | You've lived the problem | "I had the same issue with … What fixed it was …" |
| **Product answer** | Your app is genuinely the answer | The answer first, then "I made an app for this, so I'm biased: …" |
| **Clarifying question** | The question is vague | One question that helps them, plus a short answer for the most likely case |

## When to mention your product (all must be yes)
1. It directly answers the question asked, not a nearby one.
2. You've already given a useful answer in the same comment that works without it.
3. The subreddit's rules allow it (no-promotion subreddits: never).
4. In this subreddit, fewer than 1 in 10 of your recent comments mention your products (many subreddits use this
   ratio, see [08-rules-and-risks.md](08-rules-and-risks.md)).
5. You say it's yours, in plain words.

If any is no: answer without it. Your profile still carries the link for those who want to know more.

## Disclosure lines that read naturally
- "Disclosure: I made this one, so take it with salt."
- "I'm the developer of X, which does this, but the free way above works too."
- "Full disclosure, it's mine. Happy to answer anything about it here."

## Writing rules
- **Lead with the answer.** No "Great question!".
- **Be specific:** menu paths, version numbers, file sizes, minutes, prices.
- **Sound like a person:** short paragraphs, plain words, your own opinion. Subreddits remove posts that read like
  AI or ads, and readers downvote them.
- **No link unless it's needed**, and never a shortened or masked link. If you link your product, add UTM:
  `?utm_source=reddit&utm_medium=comment&utm_campaign=<subreddit>`.
- **Stay for replies.** Answer follow-up questions; that's where readers decide to try your app.
- **Never DM people** who didn't ask you to. Unsolicited messages are spam under Reddit's rules.

> **Illustrative example.** Fictional product (Clipnest, a Mac clipboard app).
>
> *Thread (r/MacOS):* "Is there a way to get back something I copied an hour ago?"
>
> *Answer:* "macOS only keeps the last thing you copied, so once it's replaced it's gone. Two ways around it:
> 1. Paste important things into a note right away (Notes has a quick note on the hot corner).
> 2. Use a clipboard history app. Free options exist; look for one that keeps history only on your Mac.
>
> Disclosure: I made one called Clipnest, it's free for 50 clips. But any of them fixes this."
