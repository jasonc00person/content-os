# Notion Content Pipeline — Schema Reference

Live schema for the Notion content database. **Pure reference — no execution logic.** Skills that read/write the pipeline (scriptwriter, post-content, ideate) load this file for IDs and property shapes.

> Last verified against live Notion: **2026-05-08** via `mcp__notion__API-retrieve-a-database`. If something feels off, re-fetch the database and update this file.

---

## Identity

| Field | Value |
|-------|-------|
| **Database name** | Jason Content Database |
| **Database ID** | `21bf6585-5e6b-81df-b692-e0321083dffa` |
| **Data source ID** | `21bf6585-5e6b-81df-b692-e0321083dffa` (same as DB — legacy 1:1) |
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
| **Source URL** | `url` | Link to the source video being recreated/twisted (the format model). Set by `ideate` and `scriptwriter` for TWIST/recreation pairs. Distinct from `Raw Footage`. |
| **Raw Footage** | `url` | Link to raw clips Jason filmed (Drive, Frame.io, etc). Filled later, not on script creation. |
| **Edited Video** | `url` | Link to final edit (replaces old "Frame Link") |
| **IG Link** | `url` | Public Instagram URL after posting |
| **Created time** | `created_time` | Auto |
| **Created by** | `created_by` | Auto |
| **Page last edited time** | `last_edited_time` | Auto — use for staleness checks |
| **Page last edited by** | `last_edited_by` | Auto |

---

## Status flow

```
Idea → Scripted → To Edit → Editing → To Review → Ready To Post → Posted → Archived
```

### Kanban groups
| Group | Statuses |
|-------|----------|
| **To-do** | Idea |
| **In progress** | Scripted, To Edit, Editing, To Review, Ready To Post |
| **Complete** | Posted, Archived |

`Ready To Post` is the handoff point for the `post-content` skill. Buffer is the source of truth for scheduling — once handed off, status flips straight to `Posted` with `Post Date` = the publish date Buffer assigned. There is intentionally no "Scheduled" status.

---

## Property write shapes (for `API-post-page` / `API-patch-page`)

```jsonc
{
  "Title":        { "title": [{ "text": { "content": "..." } }] },
  "Status":       { "status": { "name": "Idea" } },
  "Format":       { "select": { "name": "Short-form" } },
  "Type":         { "multi_select": [{ "name": "TOF" }, { "name": "Viral" }] },
  "Post Date":    { "date": { "start": "2026-05-08" } },
  "Source URL":   { "url": "https://..." },
  "Raw Footage":  { "url": "https://..." },
  "Edited Video": { "url": "https://..." },
  "IG Link":      { "url": "https://..." }
}
```

### Creating a new page
```jsonc
parent:     { "database_id": "21bf6585-5e6b-81df-b692-e0321083dffa" }
icon:       { "type": "emoji", "emoji": "📦" }   // top-level — required by scriptwriter on every create
properties: { /* shapes above */ }
children:   [ /* block objects for the page body */ ]
```

---

## Querying — known gotchas

- **Prefer `API-post-search`** over `API-query-data-source`. Query-data-source has been flaky on this DB; post-search with a `page` filter + client-side filter on `parent.database_id == 21bf6585-5e6b-81df-b692-e0321083dffa` is the reliable path.
- **Pagination is mandatory.** `post-search` caps at 100 results. Always check `has_more` and re-call with `start_cursor: next_cursor` until `has_more` is `false`. Skipping this silently drops pages.
- **Title matching is fuzzy.** Users won't type exact titles — match on closest hit within the content database, and if multiple plausible matches exist, list them and ask.

---

## When to update this file

Re-fetch and rewrite whenever:
- A property is added, renamed, or its options change in Notion
- A new status is added to the pipeline
- The database is migrated or its ID changes

Quick re-verify command (paste into Claude):
> "Re-fetch Notion content DB schema with `mcp__notion__API-retrieve-a-database` and diff against `notion-pipeline.md`."
