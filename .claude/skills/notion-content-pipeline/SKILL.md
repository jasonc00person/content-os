---
name: notion-content-pipeline
description: "Manages Jason's Notion Content Database — view the pipeline, move content between stages, add new ideas, update properties, and do bulk operations. Triggers: show my pipeline, what's in the pipeline, move to, add idea, mark as posted, what needs attention, bulk move, content pipeline, notion pipeline, update content."
---

# Notion Content Pipeline

Manages Jason's Notion Content Database — view the pipeline, move content between stages, add new ideas, update properties, and do bulk operations. All powered by the Notion MCP tools.

## How to Trigger
- **"show my pipeline"** or **"what's in the pipeline"** — view current status breakdown
- **"move [title] to [status]"** — advance a piece of content (e.g., "move bell curve to To Edit")
- **"add idea: [title]"** — create a new content idea
- **"update [title]"** — change properties on a page (format, type, post date, links)
- **"bulk move [status] to [status]"** — move all pages from one status to another
- **"what needs attention"** — show stale items and pipeline bottlenecks
- **"mark [title] as posted [date]"** — set status to Posted + set post date

---

## Database Reference

**Database ID:** `21bf6585-5e6b-81df-b692-e0321083dffa`

### Properties
| Property | Type | Options |
|----------|------|---------|
| **Title** | title | — |
| **Status** | status | Idea, Scripting/Filming, To Edit, Editing, To Review, Scheduled, Posted, Archived |
| **Format** | select | Short-form, Long-form |
| **Type** | select | Conversion, Viral |
| **Post Date** | date | YYYY-MM-DD |
| **Raw Footage** | url | Link to raw footage |
| **Frame Link** | url | Link to Frame.io or similar |

### Pipeline Flow
```
Idea → Scripting/Filming → To Edit → Editing → To Review → Scheduled → Posted → Archived
```

### Status Groups (Notion Kanban)
- **To-do:** Idea
- **In progress:** Scripting/Filming, To Edit, Editing, To Review, Scheduled
- **Complete:** Posted, Archived

---

## Execution Steps

### View Pipeline ("show my pipeline")

1. Search for all pages in the content database using `mcp__notion__API-post-search`:
   - `filter`: `{"property": "object", "value": "page"}`
   - `page_size`: 100
2. Filter results to only pages with `parent.database_id` = `21bf6585-5e6b-81df-b692-e0321083dffa`
3. Group by Status and display:
   - Count per status
   - List titles in each active status (skip Posted unless asked)
   - Flag anything stuck (in same status for 7+ days based on `last_edited_time`)

**Output format:**
```
Content Pipeline — [date]

Ideas (X)
  - Title 1
  - Title 2

Scripting/Filming (X)
  - Title 1

To Edit (X)
  - Title 1

Editing (X)
  - (none)

To Review (X)
  - Title 1

Scheduled (X)
  - (none)

Posted (X total)
Archived (X total)

Stale items (no edits in 7+ days):
  - "Title" — stuck in Scripting/Filming since [date]
```

---

### Move Content ("move [title] to [status]")

1. Search for the page by title using `mcp__notion__API-post-search` with the title as query
2. Confirm the match (fuzzy match OK — pick the closest title in the content database)
3. Update the status using `mcp__notion__API-patch-page`:
   ```
   page_id: [matched page ID]
   properties: {
     "Status": {
       "status": {
         "name": "[target status]"
       }
     }
   }
   ```
4. If moving to **Posted**, also prompt to set `Post Date` (default to today if not specified):
   ```
   properties: {
     "Status": { "status": { "name": "Posted" } },
     "Post Date": { "date": { "start": "YYYY-MM-DD" } }
   }
   ```
5. Confirm the move

---

### Add Idea ("add idea: [title]")

1. Create a new page in the database using `mcp__notion__API-post-page`:
   ```
   parent: { "database_id": "21bf6585-5e6b-81df-b692-e0321083dffa" }
   properties: {
     "Title": { "title": [{ "text": { "content": "[title]" } }] },
     "Status": { "status": { "name": "Idea" } },
     "Format": { "select": { "name": "Short-form" } }
   }
   ```
2. If the user specifies format (long-form) or type (conversion/viral), set those too

---

### Update Properties ("update [title]")

1. Search for the page by title
2. Apply the requested changes using `mcp__notion__API-patch-page`
3. Supported updates:
   - **Format**: `{ "Format": { "select": { "name": "Short-form" } } }`
   - **Type**: `{ "Type": { "select": { "name": "Conversion" } } }`
   - **Post Date**: `{ "Post Date": { "date": { "start": "2026-04-15" } } }`
   - **Raw Footage**: `{ "Raw Footage": { "url": "https://..." } }`
   - **Frame Link**: `{ "Frame Link": { "url": "https://..." } }`
   - **Title**: `{ "Title": { "title": [{ "text": { "content": "New Title" } }] } }`

---

### Bulk Move ("bulk move [from] to [to]")

1. Search and filter all pages in the `[from]` status
2. Update each page's status to `[to]` using `mcp__notion__API-patch-page`
3. List all titles that were moved

---

### What Needs Attention ("what needs attention")

1. Pull all pages from the database
2. Flag:
   - **Stale items**: Pages in active statuses (not Idea/Posted/Archived) with `last_edited_time` older than 7 days
   - **Missing metadata**: Pages missing Format or Type
   - **Pipeline bottlenecks**: Any status with 3+ items (stuff is piling up)
   - **Ideas backlog**: Total count of Ideas, suggest reviewing if > 20
3. Give 2-3 actionable recommendations based on what's found

---

### Mark as Posted ("mark [title] as posted [date]")

1. Search for the page by title
2. Update using `mcp__notion__API-patch-page`:
   ```
   properties: {
     "Status": { "status": { "name": "Posted" } },
     "Post Date": { "date": { "start": "[date or today]" } }
   }
   ```

---

## Important Notes
- Always search by title first, then filter to pages in the content database (parent.database_id = `21bf6585-5e6b-81df-b692-e0321083dffa`)
- Use fuzzy matching on titles — the user won't type exact titles every time
- When moving to Posted, always set or ask about Post Date
- Keep confirmations short — one line, not a paragraph
- If a search returns multiple possible matches, list them and ask which one
- The query-data-source endpoint has issues — use `post-search` with page filter instead and filter by parent database_id client-side
