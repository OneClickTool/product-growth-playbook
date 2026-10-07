# Auto-render: script → spec → video file

How to let an AI agent produce finished short videos for the **Auto** formats in [formats.md](formats.md) without an
editor. Any code-based video tool works; the example uses [Remotion](https://www.remotion.dev/) (React → MP4; free for
individuals and small companies, check its license for larger teams).

## The pipeline

```
post file (marketing/<platform>/NN-name.md)
  ## Title · ## Script · ## Caption · ## Production · ## Render  ← the agent writes all five
        │
        ▼  render script: extract the ## Render JSON → props.json
  video tool (one "Spec" composition that reads props)
        │
        ▼
  marketing/<platform>/out/NN-name.mp4   (1080×1920, 30 fps, music, big captions)
        │
        ▼  you: review, (optional) swap in a trending sound inside the app, turn on the promotion disclosure, post
```

Keep the assets the agent may use in one folder and list them in a short doc it reads first (for example
`marketing/video/RENDER.md`): the named scenes of your screen recording (start second, end second, caption), the stock
clips with what they show, and the music tracks with their license links.

## Spec format (example)

```json
{
  "music": "stock/upbeat-happy.mp3",
  "volume": 0.6,
  "beats": [
    { "kind": "stock", "file": "stock/frustrated-laptop.mp4", "from": 1.5, "sec": 2.0, "text": "Your Downloads folder right now" },
    { "kind": "app", "scene": 1, "text": "Duplicates, side by side", "sub": "Keeps the original, marks the copies" },
    { "kind": "app", "scene": 4, "text": "Everything goes to the Trash", "countdown": 0 },
    { "kind": "split", "sec": 6, "top": { "file": "stock/frustrated-laptop.mp4" }, "bottom": { "scene": 2 },
      "topLabel": "By hand", "bottomLabel": "With the app", "timers": [95, 4] },
    { "kind": "card", "text": "Free on the Mac App Store", "sec": 2 }
  ],
  "outro": true
}
```

| `kind` | Shows | Required fields |
|---|---|---|
| `stock` | a licensed stock clip, full screen, caption at the bottom | `file`, `sec` (+ `from`, `text`, `sub`) |
| `app` | a named scene of your real screen recording in a device frame, caption on top | `scene` (+ `text`, `sub`, `countdown` seconds) |
| `card` | big text on your brand color | `text`, `sec` |
| `split` | two sources stacked, labels, optional timers (real measured seconds only) | `sec`, `top`, `bottom` |
| `slide` | one text slide on a color or stock still (carousel) | `text`, `sec` |

Durations come from the beats, so the tool computes the video length; there is no separate timeline to keep in sync.

## Rules the agent must follow

- Only scenes that exist in your recording; never animate a feature the product doesn't have.
- Timers, counters and "X GB freed" must be real measurements, or left out.
- The first beat already shows the problem or the result (no logo intro).
- Captions readable on a phone with the sound off: 60–90 px on a 1080-wide frame, max ~8 words per line.
- Music only from the licensed folder; trending sounds are added later inside the app.

## What stays manual

Posting (each platform's own app or an approved API / scheduler), choosing a trending sound, Stitch / Duet, comment
replies, and any format that needs your face.
