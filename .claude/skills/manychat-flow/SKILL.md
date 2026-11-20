---
name: manychat-flow
description: "Sets up the ManyChat comment-keyword DM flow for a SHORT-FORM video before it gets scheduled. Reads the keyword from the spoken CTA in the final export, finds and checks the resource links the video promises, then in the real Chrome (Claude-in-Chrome MCP) duplicates the most recent promo flow, sets it to Next Post or Reel with the new keyword, rewrites the DMs, tag, and follow-up, publishes it, and turns it on. Short form only: long-form never gets a ManyChat flow. Run it before auto-poster. Triggers: set up the manychat, manychat flow, manychat for this short, comment keyword automation, dm automation for this reel, keyword cta flow, set up the dm flow, manychat before posting."
---

# ManyChat Flow

Every short form ends with a spoken "comment KEYWORD" CTA. This skill builds the ManyChat automation that DMs the promised resource to anyone who comments that word. It runs **before** `auto-poster` schedules the reel.

`final short-form export -> keyword + promise -> checked links -> duplicated flow -> live on Next Post or Reel -> auto-poster`

## Scope

- **Short form only.** If the video is long-form (horizontal, over 3 minutes, a YouTube upload), stop and say so. Long-form CTAs live in the YouTube description (`yt-description`), never in ManyChat.
- One flow per short form. Never edit a live flow that's already attached to an older reel; always work on a duplicate.

## 1. Pin down the keyword and the promise

1. Find the final export (usually `projects/<job>/outputs/<job>.final.mp4` in the `video-editor` project; the job's `RUN.md` export row names the CTA).
2. Transcribe it with the shared engine and read the last 30 seconds:
   ```bash
   TRANSCRIPT_FILE=$(.claude/skills/auto-poster/scripts/transcribe_for_caption.sh "/abs/path/final.mp4")
   ```
   The keyword is the word after "comment". The promise is what it says it will send (template, repo, Notion walkthrough, full YouTube video). The spoken audio wins over `RUN.md` or any earlier draft, because the CTA gets re-recorded.
3. Find every link the promise needs. Look in the job folder (`RUN.md`, `graphics-plan.json`), the Notion workspace (`notion-search`; lead magnets live in the free-resources database), `descriptions/`, and the long-form's YouTube ID if it promises "the full video". If a promised link can't be found, stop and ask. Never ship a flow with a missing or placeholder link.
4. Check each link as a stranger would see it:
   - Notion: open the page, click through to its public `*.notion.site/<Title-slug>-<id>` URL in a new Chrome tab, and confirm the page title renders. A `curl` 200 proves nothing on notion.site.
   - GitHub: `curl -s -o /dev/null -w "%{http_code}"` must be 200 (a private repo is 404).
   - YouTube: resolve the ID and confirm the title. Scheduled/private is fine if it goes public before the reel.
   - Scan the resource page for `PLACEHOLDER` or `<<` leftovers and flag them. Commenters land there tomorrow.

## 2. Build the flow in ManyChat (real Chrome)

Load the Chrome tools in one ToolSearch (`tabs_context_mcp`, `tabs_create_mcp`, `navigate`, `computer`, `find`, `read_page`, `get_page_text`, `javascript_tool`, `browser_batch`, `tabs_close_mcp`). Use `app.manychat.com`; it redirects to the account.

1. **Automations list** (`/cms?path=/&field=modified&order=desc`). The newest promo flow is at the top. Its trigger must read **"specific Post or Reel"**, which means it already locked onto its own reel. If it still reads **"next Post or Reel"**, its reel hasn't gone out, and a second next-post flow would fight it for the next upload. Stop and tell the user.
2. **Duplicate** it: hover the row, open the ⋮ menu, click Duplicate. The copy lands on top as `<name> copy`, STOPPED, trigger off. Open it, then click **Edit Automation** (or the "Edit" link on the "viewing a published version" banner).
3. **Trigger** (click the "When..." block):
   - Step 1: **Next Post or Reel** (the reel isn't live yet, so it can't be picked). Continue.
   - Step 2: click the keyword chip. It's a textarea (`placeholder="Add text"`). Set it to the keyword with the setter below. Continue.
   - Step 3: leave the public comment replies as they are. **Save**.
   - Saving **turns the trigger ON by itself** while the old copy is still in the DMs. Flip the toggle at the bottom of the panel off right away.
4. **Opening DM** (first Send Message): keep the greeting and the "Send the Link!" button. Rewrite only the promise line so it names what this video gives away.
5. **Actions → Add Tag**: click the tag field, **+ Tag**, name it after the topic (lowercase, e.g. `ai receptionist build`), Create.
6. **Link message (#2)**: one labelled line per link, the label ending in an emoji, the URL on its own line under it.
7. **Community message (#3, after the 30-second wait)**: leave it alone. Open its button once and confirm it still points at the general community link, not something tied to the old video.
8. **Smart Delay (1 hour)**: leave it alone. **Follow-up message**: make the question match what was sent ("did you get a chance to check out the build?" and not "watch the yt video" if no video went out).
9. **Rename**: click the pencil next to the title and name it `<topic> promo`, matching the existing names. Set it with the setter and press Enter.
10. **Update** (top right) publishes the content. Then switch the trigger toggle **on** (open the "When..." block, toggle in the trigger card).
11. **Verify** in the Automations list. The row should read LIVE, "User comments on next Post or Reel and comment contains `<keyword>`". Close your tab.

### Copy rules

- Match the flow being duplicated: keep its greeting word for word, lowercase and casual, emoji at the end of a label, ⤵️ pointing at the button. It ships under the creator's name, so **no em dashes**. Use a comma, colon, or period instead.
- Say only what the video promised. No new offers, no prices.

Reference, the flow as shipped for the AI receptionist reel (keyword `agent`):
```
Opening DM:  yooooo what up it's Jason 👋

             Just tap the button below to get my FREE AI receptionist build: the GitHub repo + the full Loom walkthrough ⤵️
Link DM:     here's the FREE AI receptionist build 🎁 full Loom walkthrough + every step
             <public notion.site URL>

             and the GitHub repo 💻
             <github URL>
Follow-up:   yoooo did you get a chance to check out the receptionist build? curious what you think
```

## Browser gotchas (hard-won, 2026-09-23)

**Text fields drop the first typed character** ("agent" landed as "gent"). Never `type` into ManyChat fields. Set the value directly:
```js
const ta = document.querySelector('textarea[placeholder="Enter your text..."]'); // message body; keyword chip = "Add text", tag dialog input = "Enter tag name"
ta.focus();
Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set.call(ta, TEXT); // HTMLInputElement for <input>
ta.dispatchEvent(new Event('input', {bubbles: true}));
await new Promise(r => setTimeout(r, 500)); ta.blur();
```
Write emoji as `\u{1F44B}` escapes in the JS string. Read every value back afterwards.

**Hidden tab = blank canvas.** When the Chrome window is covered or the user is away (`document.visibilityState === 'hidden'`), the flow canvas (WebGL) never paints and screenshots show a spinner forever. Don't bring Chrome to the front and don't ask for computer-use access. Work around it in the page:
1. Patch the render loop, then **re-open the flow through in-app navigation** (breadcrumb "Automations", then the row link). A full reload wipes the patch.
   ```js
   window.requestAnimationFrame = cb => setTimeout(() => cb(performance.now()), 16);
   window.cancelAnimationFrame = id => clearTimeout(id);
   ```
2. Before every screenshot, mirror the canvas into an `<img>` placed right after it. That keeps side panels on top, and `pointer-events:none` lets clicks through to the real nodes:
   ```js
   window.__snap = () => { const c = document.querySelector('canvas'); document.getElementById('__cvsnap')?.remove();
     const img = document.createElement('img'); img.id = '__cvsnap';
     img.style.cssText = 'position:absolute;left:0;top:0;width:100%;height:100%;pointer-events:none;';
     img.src = c.toDataURL('image/png'); c.after(img); return 'snap'; };
   ```
   Edit mode mounts a fresh canvas a few seconds after entering, so re-run `__snap()` after each click that changes the canvas. Coordinate clicks on the snapshot hit the real nodes.
3. If clicking an Automations row does nothing (the row title is an `<h1>`, not a link, and hidden-tab clicks sometimes don't register; hit 2026-09-28), route in-app instead, which keeps the patch: `history.pushState({}, '', '/<account>/cms/files/<contentId>'); dispatchEvent(new PopStateEvent('popstate', {state: {}}))`. The contentId is in the flow URL from any earlier visit.

## Hand-off

- Tell the user nothing else can go up on Instagram before this reel. "Next Post or Reel" attaches to whatever posts first. Stories don't count.
- Then run `auto-poster` for the reel. Its caption opens and closes with the same `Comment "KEYWORD"` line.
- Report: flow name, keyword, each link sent, the tag, and anything flagged on the resource page.
