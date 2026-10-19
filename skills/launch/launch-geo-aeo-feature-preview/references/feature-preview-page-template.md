# Feature preview page: template

> One page per feature you are designing but haven't built. Honest status, real mockups, answer-first sections,
> one clear action. Copy it into your site (Markdown, MDX, CMS) and replace everything in `{{ }}`.

## URL and title
- URL: `/features/{{feature-slug}}` (short, the words people search; no dates in the slug).
- `<title>`: `{{Feature name}}: {{what it does in 5–8 words}} ({{Product}})`, under 60 characters.
- Meta description: the short answer below, cut to about 150 characters.

## Page

```markdown
# {{Feature name}}: {{what it does, in the user's words}}

**Status: In design · not available yet.** Planned for {{month year}}. Last updated {{date}} by {{name, role}}.

## The short answer
{{40–60 words. What the feature will do, for whom, and the one thing that makes it different. No hype words.
Example: "Batch Rename will rename hundreds of photos by date, place or camera in one step on Mac. Unlike Finder's
rename, it previews every new name before applying it and can undo the whole batch."}}

![Design mockup: {{what the mockup shows}}]({{mockup-1.png}})
*Design mockup, not the final app.*

## What problem does {{feature}} solve?
{{2–4 sentences in the words people used in the threads, reviews and searches you collected. Link 1–2 of those
public threads as evidence that the problem is real.}}

## How will {{feature}} work?
1. {{Step 1, one line}}
2. {{Step 2}}
3. {{Step 3}}

![Design mockup: {{screen 2}}]({{mockup-2.png}})
*Design mockup.* {{Optional: 30-second prototype video with captions.}}

## {{Feature}} vs. {{what people use today}}
| | {{Today's way / competitor}} | {{Feature}} (planned) |
|---|---|---|
| {{criterion users care about}} | {{fact, with source link}} | {{planned behaviour}} |
| {{criterion}} | {{fact}} | {{planned}} |
| Price | {{fact, source}} | {{planned price or "not decided"}} |

## Design decisions so far
From our design review on {{date}}:
- **{{Decision}}**: {{why, in one line}}. {{Optional quote: "…" — {{name, role}}}}
- **{{Decision}}**: {{why}}.
- **Not doing:** {{what you cut and why}}.

## What it won't do (yet)
- {{Limit 1}}
- {{Limit 2}}

## FAQ
### When will {{feature}} be available?
{{Honest answer: target month, and "we'll email the waitlist first".}}
### How much will it cost?
{{Planned price, or "Not decided yet. Waitlist members get {{offer}}."}}
### Does it work on {{platform / offline / with X}}?
{{Short answer first.}}

## Want it? Help shape it
[Join the waitlist]({{form-url}}?utm_source={{source}}&utm_campaign=preview-{{feature-slug}}) · or
[vote on the mockup / leave a comment]({{feedback-url}}). {{N}} design questions are still open: {{list 1–2}}.
```

## Checklist before you publish
- [ ] Status line at the top says it's not available yet, with a target month.
- [ ] Every image is labelled **Design mockup**. No fake device frames with fake ratings.
- [ ] No "Download", "Buy" or "Start trial" buttons. The only action is waitlist / vote / feedback.
- [ ] No reviews, user counts or logos you don't have.
- [ ] The short answer is 40–60 words and makes sense on its own.
- [ ] Each H2 is a question someone actually asked; the answer is the first sentence under it.
- [ ] Every outside fact has a link to its source.
- [ ] Text is HTML (not baked into images); images have `alt` text.
- [ ] "Last updated" date and a named author.
- [ ] The page is in the sitemap, linked from your home page or a `/roadmap` page, and not `noindex`.
- [ ] Waitlist form fires a GA4 key event (for example `generate_lead` with `feature={{slug}}`).

## Optional structured data
Only if it matches the visible page. Google says it isn't required for AI features.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "When will {{feature}} be available?",
    "acceptedAnswer": { "@type": "Answer", "text": "{{same text as on the page}}" }
  }]
}
```

Don't mark a feature that doesn't exist as a `SoftwareApplication` with ratings or offers.
