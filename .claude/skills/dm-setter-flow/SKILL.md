---
name: dm-setter-flow
description: "Jason's own comment-keyword DM automation for a SHORT-FORM video, built in DM Setter (his custom Instagram DM software in ~/Projects/dm-setter, which replaced Manychat's comment-to-DM for his account). Reads the keyword from the spoken CTA in the final export, finds and checks the resource links the video promises, duplicates the newest promo automation as a DRAFT with the new keyword, card, tag and links (no follow-up question), then right before the reel posts publishes it on Next Post or Reel so it locks onto that reel. Short form only. Jason-only: never shipped to clients (they use manychat-flow). Run before auto-poster. Triggers: set up the dm automation, dm automation for this reel, comment keyword automation, keyword cta flow, set up the dm flow, dm setter flow, dm setter automation, automation for this post, make the automation, arm the automation, put the automation live, publish the dm automation."
---

# DM Setter Flow

Every short form ends with a spoken "comment KEYWORD" CTA. DM Setter (`~/Projects/dm-setter`, a Cloudflare Worker on the official Instagram API) DMs the promised resource to anyone who comments it. This skill builds that automation. It is Jason's lane only: `manychat-flow` stays as is for clients, and the packager excludes this folder.

`final short-form export -> keyword + promise -> checked links -> DRAFT automation -> arm (LIVE on Next Post or Reel) -> auto-poster -> locks onto the reel`

## Scope

- **Short form only.** Long-form CTAs live in the YouTube description (`yt-description`).
- **Never also build it in Manychat.** The same keyword live in both = two DMs per commenter.
- One automation per short. The script always duplicates; it never edits a live automation tied to an older reel.

## Next Post or Reel (how it should be done, Jason 2026-10-30)

Every new short goes out on **Next Post or Reel** (DM Setter commit cbeaed9, post id `"next"`). Publishing arms it: it's LIVE from that moment and locks onto the **first post or reel published after it was armed** (ads skipped, stories don't count). The minute cron and every incoming comment both check, so the first commenter gets the DM even before the cron runs. Once locked it is an ordinary post trigger on that reel.

- **Only one can wait at a time.** Publish refuses a second one ("already waiting for the next post"). If one is already waiting, its reel hasn't gone out: stop and tell Jason.
- **Arm it when the reel is posted or scheduled** (Jason, 2026-11-11: for a scheduled reel just turn it on at scheduling time, no timed arming job). Anything else that goes up on Instagram first (a scheduled post, a reel posted by hand from the phone) steals the lock, so tell Jason nothing else goes on the feed until the reel is out. Check `python3 .claude/skills/auto-poster/scripts/post_to_zernio.py --status` shows nothing scheduled to Instagram ahead of this reel.
- A keyword comment that lands while nothing answers it is logged as ignored and never retried, so the order is always arm, then post.

## The script

`.claude/skills/dm-setter-flow/scripts/dmflow.py` (stdlib Python). Writes go through DM Setter's own admin routes (basic auth from `~/Projects/dm-setter/.env`); every graph is checked with the app's own `src/graph.ts` validator, so a draft that saves will publish. **Every call needs network: run Bash with the sandbox off.**

```bash
python3 .claude/skills/dm-setter-flow/scripts/dmflow.py list              # every comment automation: LIVE / OFF / DRAFT, keyword, post
python3 .claude/skills/dm-setter-flow/scripts/dmflow.py create spec.json  # [--from <id>] duplicate the newest promo as a DRAFT
python3 .claude/skills/dm-setter-flow/scripts/dmflow.py show <id>
python3 .claude/skills/dm-setter-flow/scripts/dmflow.py test <id>         # 3-digit code: DM it to the account to run the draft on yourself (15 min)
python3 .claude/skills/dm-setter-flow/scripts/dmflow.py arm <id>          # publish on Next Post or Reel, right before the reel posts
```

## 1. Pin down the keyword and the promise

1. Find the final export (usually `~/Projects/video-editor/projects/<job>/outputs/<job>.final.mp4`; the job's `RUN.md` names the CTA).
2. Transcribe and read the last 30 seconds:
   ```bash
   TRANSCRIPT_FILE=$(.claude/skills/auto-poster/scripts/transcribe_for_caption.sh "/abs/path/final.mp4")
   ```
   Keyword = the word after "comment". Promise = what it says it will send. The spoken audio wins over `RUN.md`, `sponsors/<brand>/` notes or any draft, because CTAs get re-recorded.
3. Find every link the promise needs: the job folder, `sponsors/<brand>/production-notes.md` for sponsored reels, Notion's Free Sauce database (`notion-fetch` the page), `descriptions/`. A link you can't find = stop and ask. Never ship a placeholder.
4. Check each link as a stranger sees it, in Claude in Chrome:
   - Notion: open the public `creator-economy.notion.site/<Title-slug>-<id>` URL and confirm the page title renders with no login wall. A `curl` 200 proves nothing on notion.site.
   - GitHub: `curl -s -o /dev/null -w "%{http_code}"` = 200 (private repo = 404). YouTube: resolve the ID, confirm the title.
   - Scan the page for `PLACEHOLDER` or `<<` leftovers.

## 2. Write the spec (scratchpad JSON)

```json
{
  "keyword": "THUMBNAIL",
  "name": "THUMBNAIL: AI YouTube thumbnails in Krea",
  "tag": "krea ai thumbnails guide",
  "card": "yooooo what up it's Jason 👋\n\nJust tap the button below to get my FREE step-by-step AI thumbnail guide: the exact Krea + Canva process and every prompt ⤵️",
  "links": "here's the FREE AI thumbnail guide 🎁 the full Krea + Canva process + every prompt\nhttps://creator-economy.notion.site/AI-YouTube-Thumbnails-in-Krea-3fbf65855e6b8108925ed44c62ae3b45"
}
```
Optional `"public_reply"` (one per line, picked at random); left out, the template's three stay.

The shape it fills: **card** (first message, the private reply, with the "Send the Link! 🔗" tap button) → tap → **tag** → **links**, and it ends there. **No follow-up question, ever** (Jason, 2026-11-23: "deliver them the lead magnet and then just leave it there. I never respond to any of those."). The AI setter is retired until further notice, so nothing answers a reply; a question at the end only leaves people on read. The pause + "yo also curious..." opener was removed from all 26 live automations that had one on 2026-11-23 (their old graphs are in `~/Projects/fewchat/docs/backups/automations-before-opener-removal_2026-11-23.json` (the project folder was renamed from `dm-setter` to `fewchat` on 2026-11-23)), and `create` drops anything an older template still has after its links.

Copy rules:
- Name = `KEYWORD: topic`, like the rest of the list. Tag = lowercase topic.
- Card keeps the greeting word for word ("yooooo what up it's Jason 👋"), then one line naming exactly what the video promised, ⤵️ at the end.
- Links: one labelled line per link, label ends in an emoji, URL on its own line under it.
- Ships under Jason's name: **no em dashes** (the script refuses them). Say only what the video promised. No new offers, no prices.

## 3. Build the draft

```bash
python3 .claude/skills/dm-setter-flow/scripts/dmflow.py create /abs/path/spec.json
```
It duplicates the newest live promo (`--from <id>` to pick another), checks its shape, rewrites keyword, card, tag and links, sets the post to Next Post or Reel, validates, saves the draft, renames it, and reads every field back. The result is DRAFT: `enabled 0`, never published, nothing sends, and a draft never locks onto a post. Confirm the row in the console's Automations list (`/admin/automations`) reads DRAFT with the new keyword.

To try it on a phone before it goes live: `test <id>`, then DM the code to the account within 15 minutes. The run uses a hidden copy, so stats stay clean.

## 4. Arm it (right before the reel posts)

Check the Zernio queue (above), then:
```bash
python3 .claude/skills/dm-setter-flow/scripts/dmflow.py arm <id>
```
It refuses if an any-post automation already answers the same word, publishes on Next Post or Reel and checks the row reads LIVE with post `next`. The list line reads "User comments on next Post or Reel and comment contains KEYWORD". After the reel is up and a minute has passed, `show <id>` should name the reel's post id instead of "next Post or Reel". If it locked onto the wrong post, set the right one in the editor's When... step.

## Gotchas

- Cloudflare 1010-blocks Python's default user agent on the Worker; the script sends its own.
- `duplicate` copies the template's keyword and post id onto the new row, so the list would read the old reel. `create` rewrites the row's keyword and sets its post to `next` (only while it is an unpublished draft; the lock only reads live rows); publish rewrites everything from the draft anyway.

## Hand-off

- Arm, then run `auto-poster` for the reel straight away (caption opens and closes with `Comment "KEYWORD"`). Nothing else goes up on Instagram in between. For a scheduled post, arm it as soon as the post is scheduled and keep the IG queue clear until it goes out.
- Report: automation number + name, keyword, every link sent, the tag, and DRAFT, LIVE waiting on next post, or locked (with the post id).
