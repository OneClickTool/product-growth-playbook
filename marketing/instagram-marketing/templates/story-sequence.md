# Story sequence (3 frames, the link path)

Post 1–3 h after a feed post. Why and rules: [docs/06-stories-and-links.md](../docs/06-stories-and-links.md).
Canvas 1080 × 1920; keep text and stickers out of the top 250 px and bottom 350 px.

````markdown
# Story · {{NN-slug}} · {{date}}

## Frame 1 · Tease
- Share the feed post to Story (it taps through to the post).
- Text: "{{New post: …}}"

## Frame 2 · Proof
- Image / 5 s clip: {{the result, real screenshot}}
- Sticker: poll "{{question}}" · {{option A}} / {{option B}}   (or question sticker)

## Frame 3 · Path
- Text: "{{offer in one line, e.g. Free for 2 folders. Try it ↓}}"
- Link sticker text: "{{Get Tidybox}}"
- URL: {{landing}}?utm_source=instagram&utm_medium=story&utm_campaign={{slug}}&utm_content={{NN-slug}}

## After
- [ ] Added to Highlight: {{product}}
- [ ] Tapped the sticker on my phone: lands right, UTM in the URL
- [ ] At +24 h: sticker taps = {{…}}, replies = {{…}}, poll votes = {{…}}
````
