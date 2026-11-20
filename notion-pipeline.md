# Notion Content Pipeline — Schema Reference

Live schema for the Notion content database. **Pure reference — no execution logic.** Any skill that reads or writes the pipeline loads this file for IDs and property shapes.

> Last verified against live Notion: **2026-06-30** via `notion-fetch`. If something feels off, re-fetch the database and update this file.

---

## Identity

| Field | Value |
|-------|-------|
| **Database name** | Jason Content Database |
| **Database ID** | `21bf6585-5e6b-81df-b692-e0321083dffa` |
| **Data source ID** | `21bf6585-5e6b-81c2-b536-000b0adc0835` (differs from DB ID — re-verified 2026-06-30; used as `collection://…` for `notion-query-data-sources` and as the data source for `notion-create-pages`. The raw-API `API-post-page` tool 404s on it — use the **database ID** as `parent.database_id` there.) |
| **Parent page** | Content OS (`21bf6585-5e6b-8086-a2d7-df8494a043c2`) |
| **URL** | https://www.notion.so/21bf65855e6b81dfb692e0321083dffa |

---

## Properties

| Name | Type | Notes |
|------|------|-------|
| **Title** | `title` | Page title |
| **Status** | `status` | Pipeline stage — see flow below |
| **Format** | `select` | `Short-form` · `Long-form` |
| **Type** | `multi_select` | `TOF` · `MOF` · `BOF` · `Brainrot` · `Viral` · `Conversion` (multiple allowed) |
| **Post Date** | `date` | YYYY-MM-DD — set when status flips to Posted |
| **Source URL** | `url` | Link to the source video being recreated/twisted (the format model). Set on TWIST/recreation pairs during ideation/scripting. Distinct from `Raw Footage`. |
| **Raw Footage** | `url` | Link to raw clips Jason filmed (Drive, Frame.io, etc). Filled later, not on script creation. |
| **Edited Video** | `url` | Link to final edit (replaces old "Frame Link") |
| **Created time** | `created_time` | Auto |
| **Created by** | `created_by` | Auto |
| **Page last edited time** | `last_edited_time` | Auto — use for staleness checks |
| **Page last edited by** | `last_edited_by` | Auto |

---

## Status flow

```
Idea → Scripting → Filming → Editing → Review → Ready → Posted → Archived
```

> Renamed 2026-06-30: `To Review` → **`Review`**, `Ready To Post` → **`Ready`**. No other property changes.

### Kanban groups
| Group | Statuses |
|-------|----------|
| **To-do** | Idea |
| **In progress** | Scripting, Filming, Editing, Review, Ready |
| **Complete** | Posted, Archived |

`Ready` is the handoff stage: the edit is done and approved, waiting to publish. Posting goes through the `auto-poster` skill (Zernio), which takes a video path/URL directly and does **not** read Notion itself; the session that ran it flips `Ready → Posted` and sets `Post Date` (the go-live date) immediately after a successful post or schedule (standing rule in CLAUDE.md, "Videos live in Notion"). There is intentionally no "Scheduled" status.

---

## Views

The DB has 4 live views (all on the same data source):

| View | Type | Notes |
|------|------|-------|
| **Board** | board | Grouped by `Status`, ascending; cards show Title + Type. Default page template set. |
| **Calendar** | calendar | By `Post Date`; shows Title, Status, Format. |
| **Consistency** | chart | Daily count of `Posted` items, stacked by Format. |
| **Monthly Post Volume** | chart | Monthly count of `Complete`-group items, stacked by Format. |

---

## Property write shapes (Notion API property values)

These are the canonical property value shapes (raw `API-post-page` / `API-patch-page`, and what `ntn api PATCH` expects). The MCP `notion-create-pages` tool takes a flatter prop map instead and authors the page as Jason — prefer it for writes (see Querying below).

```jsonc
{
  "Title":        { "title": [{ "text": { "content": "..." } }] },
  "Status":       { "status": { "name": "Idea" } },
  "Format":       { "select": { "name": "Short-form" } },
  "Type":         { "multi_select": [{ "name": "TOF" }, { "name": "Viral" }] },
  "Post Date":    { "date": { "start": "2026-06-30" } },
  "Source URL":   { "url": "https://..." },
  "Raw Footage":  { "url": "https://..." },
  "Edited Video": { "url": "https://..." }
}
```

### Creating a new page
```jsonc
parent:     { "database_id": "21bf6585-5e6b-81df-b692-e0321083dffa" }
icon:       { "type": "emoji", "emoji": "📦" }   // top-level — set on every create
properties: { /* shapes above */ }
children:   [ /* block objects for the page body */ ]
```

---

## Querying — known gotchas

- **Writes → `notion-create-pages` (MCP).** Sets title + status + format + body in one call from a flat prop map, authored as Jason. Use the **data source ID** as the parent.
- **Reads/queries → `ntn datasources query` (CLI).** The MCP `notion-query-data-sources` is Enterprise-gated on Jason's plan (400 upsell), so it can't query this DB; the `ntn` CLI can. Pipe `--json | jq` for token-lean output.
- **Pagination is mandatory.** Any list path caps at 100 results. Always check `has_more` / `next_cursor` and re-call until exhausted. Skipping this silently drops pages.
- **Title matching is fuzzy.** Users won't type exact titles — match on closest hit within the content database, and if multiple plausible matches exist, list them and ask.

---

## When to update this file

Re-fetch and rewrite whenever:
- A property is added, renamed, or its options change in Notion
- A new status is added to the pipeline
- A view is added/removed or the database is migrated / its ID changes

Quick re-verify command (paste into Claude):
> "Re-fetch the Notion content DB schema with `notion-fetch` (id `21bf6585-5e6b-81df-b692-e0321083dffa`) and diff against `notion-pipeline.md`."
