---
name: social-credible-posting
description: Write posts on X, Threads, Facebook (pages and groups) and LinkedIn that people trust and act on, without hype, fake proof or "get rich quick" tricks. Covers the proof ladder (claim → number → screenshot → method others can repeat), five post formats that earn trust (lesson, teardown, before/after with data, "I was wrong", useful thread), a red-flag word list, a pre-post credibility checklist, the disclosure rules for affiliate links, sponsorships and income claims (FTC), and how each platform differs. Use when someone asks "how do I post on X without sounding like a scammer", "write a credible Threads post", "how to promote in Facebook groups", "my posts sound salesy", "how to share revenue numbers honestly", "build trust on social media", "chém gió sao cho đáng tin", "không phải lùa gà", or when a draft is full of hype.
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: "Setup 30 min · each post 15-30 min"
  version: 1.0.0
  author: nvminhtu
---

# Credible Posting: Persuasive Without the Hype

> A checklist and 5 post formats that make strangers trust you, plus a list of phrases that make them scroll past
> or report you.

## Goal
Feeds are full of "I made $50k in 30 days with this one trick". Readers have learned that most of it is a funnel
into a course. The way to stand out is the opposite: **specific, provable, modest claims** and the failures next
to the wins. Trust grows slowly but compounds, and it's the only thing that turns followers into users and buyers.

## When to use
- You're starting to post about your product or your journey on X, Threads, Facebook or LinkedIn.
- Your drafts sound like ads, or your posts get likes from other builders but no users.
- You want to share revenue or user numbers and don't want to look like you're selling a dream.
- **Not for:** a weekly progress habit → [social-build-in-public](../social-build-in-public/SKILL.md). Reddit, which
  has its own rules → [launch-reddit-posting](../../launch/launch-reddit-posting/SKILL.md). Launch-day posts →
  [launch-post-writing](../../launch/launch-post-writing/SKILL.md).

## Inputs
- Your product and who it's for.
- Real things you can show: numbers, screenshots of dashboards, reviews (with permission), a mistake you made.
- Any money relationship to what you mention: your own product, affiliate links, sponsors, free products received.

## The rules that apply to everyone
- **Disclose money relationships, clearly, in the post itself.** The FTC's
  [Endorsement Guides FAQ](https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking)
  and [Disclosures 101](https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers) say
  a material connection (payment, free product, affiliate commission, family or business ties) must be easy to
  notice, not hidden in a profile or behind "more". Other countries have similar rules.
- **Endorsements must be honest**, and when you show an unusual result, make clear what results people should
  generally expect. A screenshot of your best month as if it were normal is misleading.
- **No fake reviews or bought engagement.** The FTC treats fake reviews and bought followers as deceptive, and
  every platform bans inauthentic behaviour (e.g. Meta's [spam standard](https://transparency.meta.com/policies/community-standards/spam/)).
- **Groups have their own rules.** Most Facebook groups limit or ban promotion. Read the rules, or ask an admin first.

## Steps
1. **Climb the proof ladder.** For every claim in a draft, push it up at least one rung:

   | Rung | Example |
   |---|---|
   | 1. Claim | "My app is growing fast" |
   | 2. Number | "412 installs last week, up from 90" |
   | 3. Evidence | + a screenshot of the store dashboard, date visible |
   | 4. Method | + "what changed: I rewrote the subtitle around 'offline'. Here's the before/after" |
   | 5. Repeatable | + "you can test this in 20 minutes: …" |

   Rung 4–5 posts get saved and shared because the reader gets something even if they never use your product.
2. **Pick one of five trust formats.**
   - **Lesson:** "I did X, expected Y, got Z. What I'd do differently: …"
   - **Teardown:** what a successful product does well, with screenshots (credit them).
   - **Before/after with data:** one change, two numbers, one screenshot.
   - **"I was wrong":** a belief you dropped and the evidence that changed your mind. Rare, so it stands out.
   - **Useful thread / carousel:** a checklist or how-to that works without your product. Mention the product once, at the end.
3. **Delete the red flags.** If the draft has any of these, rewrite:
   "guaranteed", "passive income" without real numbers, "10×", "secret", "nobody is talking about this", "only 3
   spots left" (unless true and verifiable), "comment 'X' and I'll DM you", income screenshots with no time range,
   "I quit my job and you can too", ✅🚀🔥 every line, a link to a course in every post.
4. **Write for the platform.**

   | Platform | What works | Watch out for |
   |---|---|---|
   | **X** | Short, punchy first line; threads for how-tos; replies to bigger accounts that add real value | Link posts often get less reach; put the link in a reply if you want, and test |
   | **Threads** | Conversational, questions, behind-the-scenes; replies matter | Pure promotion gets ignored; talk like a person |
   | **Facebook page** | Longer stories, photos, local language | Organic reach for pages is low; use it as a home, not a channel |
   | **Facebook groups** | Value posts that answer the group's common questions; "I made this for this group, feedback welcome" (with admin OK) | Promo rules, admin approval, being reported as spam if you post the same text in 20 groups |
   | **LinkedIn** | Lessons with numbers, the professional angle | Engagement-bait ("Agree?") and copy-paste motivational posts |

5. **Run the 6-question check before posting.**
   - [ ] Is every number true, with a time range and the source I'd show if asked?
   - [ ] Did I show the context (one good month, a small base, luck)?
   - [ ] Is any money relationship disclosed in the post itself?
   - [ ] Would a reader get value even if they never click my link?
   - [ ] Would I be comfortable if a competitor or journalist screenshotted this?
   - [ ] Is there at most one link and one ask?
6. **Answer every reply in the first hour**, especially the sceptical ones. "Fair point, here's the raw data" wins
   more trust than the post did.
7. **Track what counts:** profile visits, link clicks with UTM, sign-ups, replies from real users. Not likes.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are an editor who makes builders' social posts credible. Remove hype, keep the energy. Never add numbers or
results I didn't give you. Flag anything that needs a disclosure under the FTC Endorsement Guides.

Platform: {{X / Threads / Facebook page / Facebook group (paste its rules) / LinkedIn}}
My product and audience: {{...}}
What I want to share: {{the story or result}}
Evidence I can show: {{numbers with dates, screenshots, reviews}}
Money relationships: {{own product / affiliate / sponsor / none}}
My draft (optional): {{...}}

1. Rewrite the post in the best of these formats for my content: lesson, teardown, before/after with data,
   "I was wrong", useful thread. Say which and why.
2. Push every claim up the proof ladder (claim → number → evidence → method → repeatable), and list what I need
   to screenshot.
3. Remove red flags (guarantees, fake scarcity, vague income claims, engagement bait) and add context for any
   unusual result.
4. Add the disclosure line if needed, in the post itself.
5. Give me 2 alternative first lines, and 3 sceptical replies I should expect with honest answers.
````

## Example output

> **Illustrative example.** Fictional numbers.

**Before (hype):**
> 🚀 My app went from 0 to $2k MRR in 30 days 🔥 Nobody talks about this ASO secret. Comment "ASO" and I'll DM you the playbook 👇

**After (credible, X thread opener):**
> My Mac app made $2,140 in September. In August: $310.
> One change did most of it: I rewrote the App Store subtitle around what people actually search for.
> Before/after screenshots and the 20-minute method below. (Yes, it's my app; the method works for any app.) 🧵

Context added in the thread: "September had a feature in a newsletter, so not all of it is the subtitle. Search
installs went from 41% to 63% of total."

## Common mistakes
- **Only posting wins.** A feed of wins looks like an ad. Share the failures; they're the most trusted posts.
- **Numbers without a time range or base.** "300% growth" from 3 to 12 users is technically true and misleading.
- **"DM me for the link" funnels.** Readers know it's a sales funnel. Put the useful part in the post.
- **Pasting the same promo into 20 groups.** It gets you reported and banned; write one tailored post with permission.
- **Hiding affiliate links.** It's a legal issue in many countries and a trust issue everywhere.

## Related skills
- [social-build-in-public](../social-build-in-public/SKILL.md): turn credible posts into a weekly habit.
- [social-short-video](../social-short-video/SKILL.md): the same principles, in video.
- [case-study-write-your-own](../../case-study/case-study-write-your-own/SKILL.md): turn a strong post into a full case study.
- [strategy-contrarian-marketing](../../strategy/strategy-contrarian-marketing/SKILL.md): the honesty filter for growth ideas.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Rules: [FTC Endorsement Guides FAQ](https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking),
[FTC Disclosures 101](https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers),
[Meta spam standard](https://transparency.meta.com/policies/community-standards/spam/) (checked 2026-10-02).
