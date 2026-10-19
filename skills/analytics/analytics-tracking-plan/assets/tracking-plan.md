# Tracking plan — {{product}}

Property: {{GA4 property name}} · Stream: {{url}} · Owner: {{name}} · Last updated: {{YYYY-MM-DD}}

**Success means:** {{the one action, e.g. "a visitor clicks the App Store badge"}}

## Events (max 8)

| Event | Trigger (exact user action) | Parameters (max 3) | Key event? | Custom dimension registered | Added via | Tested (date) |
|---|---|---|---|---|---|---|
| `{{event_name}}` | {{click on … / form sent / page …}} | `{{param}}` | {{primary / secondary / —}} | {{yes: name, scope / no}} | {{gtag / GTM / CMS}} | |
| | | | | | | |

Collected already by enhanced measurement (don't re-add): `page_view`, `scroll`, `click` (outbound),
`view_search_results`, `video_*`, `file_download`, `form_start`, `form_submit`.

## UTM links

Convention: [utm-convention.md](../references/utm-convention.md). Approach chosen: {{kit mediums + custom channel group / utm_medium=social + utm_content}}.

| Channel | Link | Lands in channel (checked in Traffic acquisition) |
|---|---|---|
| {{x}} | `{{url}}?utm_source={{x}}&utm_medium={{post}}&utm_campaign={{campaign}}` | {{Organic Social / Unassigned → fixed on date}} |
| | | |

## Test checklist

- [ ] Each event seen in Realtime → *Event count by event name*
- [ ] Each event seen in DebugView with its parameters
- [ ] Key events marked in Admin → Key events
- [ ] Custom dimensions registered (Admin → Custom definitions)
- [ ] One tagged link per channel clicked and seen in Realtime with the right source / medium
- [ ] No personal data (email, name, phone) in any parameter

## Change log

| Date | Change | Why |
|---|---|---|
| {{YYYY-MM-DD}} | First version | |
