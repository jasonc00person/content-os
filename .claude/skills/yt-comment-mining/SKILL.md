---
name: yt-comment-mining
description: "Mines YouTube comments for what the audience is actually asking for, then turns the demand into video ideas. yt-dlp pulls every comment off Jason's own recent uploads plus tracked competitors (free, no API key, no browser, no Apify); a script strips praise/noise/spam, tiers each survivor by intent (blocker > buyer > request > objection > constraint > how-to > question), scores it, and flags suspected shill campaigns; then you cluster the survivors into content ideas and a reply queue. Builds a self-contained HTML report in research/ with every comment verbatim, its source video, and a copy-able search string so Jason can go find and answer it on YouTube. Triggers: comment mining, mine my comments, mine the comments, scrape my comments, comment research, what are my viewers asking for, what does my audience want, audience demand, demand research, what should I make next based on comments, comment ideas, reply queue."
---

# YT Comment Mining — Turn the Comment Section Into a Content Queue

The comment section is the only place the audience tells you what to make in their own words. This skill reads it at scale, throws away the praise, and hands back clustered demand plus a list of people worth replying to today.

Three phases. Scripts own the mechanical work; you own the judgment.

- **Phase 1 — Scrape & filter:** `mine-comments.py` pulls comments with yt-dlp, drops noise/praise/spam/uploader replies, tiers + scores every survivor, flags suspected astroturf, writes `signals.json`.
- **Phase 2 — Cluster:** you read `signals.json` (text only, it's small) and write `clusters.json` — named demand clusters, a verdict per cluster, the video idea it implies, and a reply queue.
- **Phase 3 — Build:** `build-report.py` renders `signals.json` + `clusters.json` into a self-contained HTML report in `research/` and opens it.

**Own channel and competitor channels answer different questions.** Comments on Jason's videos are demand from an audience he already has: what to make next, what's broken, who's ready to buy. Comments on competitors are topic validation and poaching material: proof a subject performs, and complaints their creator hasn't answered. Always scrape both, and never blend them in the same cluster without saying which side each comment came from (the report badges own-channel comments automatically).

**A blocker outranks a request.** Someone who tried to build the thing and hit a wall ("the command prompt just is not working") already believes the pitch and is one fix away from converting. Someone asking for a Final Cut video is browsing. The tier weights encode this — don't re-sort by likes.

**Comment volume is a flop signal.** A video pulling 3 comments on 1.1K views told the same story views did, faster. Note it when a video in the scope table is conspicuously quiet.

---

## Prerequisites

- **`yt-dlp`** on PATH (`./setup.sh` from the project root installs it; already used by `transcribe-url` and `yt-competitor-research`). Update when it warns about being >90 days old: `brew upgrade yt-dlp` (macOS), `winget upgrade yt-dlp.yt-dlp` (Windows), `uv tool upgrade yt-dlp` (Linux / uv).
- **Python 3**, stdlib only. No venv, no pillow, no network beyond yt-dlp. Both scripts run anywhere python3 does.
- **`competitor-list.md`** in the project root with a `## YouTube` section, for the competitor half.
- No API key, no OAuth, no browser. YouTube's Data API caps comment reads and needs a key; yt-dlp has neither limit.

---

## PHASE 1 — Scrape & Filter

1. **Resolve targets.** Jason's own channel is **always** in scope: `@jasoncooperson`. For competitors, read `competitor-list.md`, find `## YouTube`, and **default to the first 3 channels** (order = priority — don't ask). Skip any `###` block whose heading starts with `EXAMPLE`. Inline handles override; "just mine" / "only my channel" drops the competitor half; "all" uses every handle.
2. **Stamp a unique run.** Run `date +%Y-%m-%d_%H%M%S` once, call it `<RUN>`. `<RUN_DIR>` = `/tmp/yt-comments/<RUN>/`; `mkdir -p "<RUN_DIR>"`. Final report = `<project_root>/research/Comment-Mining_<RUN>.html` (create `research/` if missing). Every run is its own dir and its own report file — never inspect, reuse, or clean up a prior run.
3. **Mine (ONE command).** Substitute the literal path — shell state does not survive between Bash calls:

   ```
   python3 <SKILL_DIR>/scripts/mine-comments.py "<RUN_DIR>" "@jasoncooperson" "@handle_b" "@handle_c" "@handle_d" --own jasoncooperson --videos 3
   ```

   Set Bash `timeout: 600000` (10 min). About 8-12s per video; 12 videos clears in ~90s. Flags: `--videos N` (per channel, default 5), `--max-comments N` (per video, default 400), `--min-score N` (default 5, raise to 8 for a tighter set on a big scrape). `--own` marks which handle is Jason's so the report can badge it.

   The script prints a per-video line (`channel · N comments → N signals · title`), then the totals, the drop breakdown, and any suspected campaign. A video that returns 0 comments is either brand new or has comments disabled — note it and move on. If yt-dlp errors on the channel listing, that's a tool problem, not a dead channel: surface it.

---

## PHASE 2 — Cluster (you, the orchestrator)

4. **Read the signals.** `jq -r '.signals[] | "\(.id)\t[\(.score)] \(.tiers|join(","))\t\(.text|gsub("\n";" ")|.[0:160])"' "<RUN_DIR>/signals.json"` — pipe through `head -40` for the own-channel set first (`select(.is_own_channel)`). It's text, it's small, read it directly. Never read the raw `meta/*.info.json` blobs; they're megabytes of unfiltered comments.
5. **Judge any suspected campaign.** The script flags a subject requested by multiple authors across multiple channels and **does not drop it** — a false positive would cost a real topic. Look at the actual comments: recycled phrasing, near-identical account names, and requests that never come with any discussion of the thing = shill campaign, exclude it from every cluster. Genuine demand phrased differently each time = keep it, and say so.
6. **Write `clusters.json`** in ONE `Write` call to `<RUN_DIR>/clusters.json`:

   ```json
   {"headline": "one or two sentences, lead with the takeaway",
    "clusters": [{"name": "Windows / WSL",
                  "verdict": "what this cluster means, 1-2 sentences, grounded in the comments",
                  "video_idea": "the actual video title it implies, or the reason it isn't a video",
                  "signal_ids": ["Ugz...", "Ugy..."]}],
    "reply_queue": ["Ugw...", "Ugx..."]}
   ```

   - **3-6 clusters.** A cluster needs at least 2 comments. One-off asks stay unclustered (the report collects them in a collapsible).
   - **`video_idea` is a real title, not a topic.** "I Taught Claude to Edit in Premiere Pro on Windows (No WSL)" is a video. "Windows support" is a changelog. If a cluster is better answered inside an already-planned video or on a call, say that instead of inventing a title.
   - **`reply_queue` is blockers and high-intent buyers**, capped at ~8. These are people to answer on YouTube today, not video fuel. Ordinary requests don't belong here.
   - **IDs must be copied exactly**, including any `.SUFFIX` on reply comments. `build-report.py` warns on stderr for any id it can't find; fix and re-run.

---

## PHASE 3 — Build

7. **Render + open (ONE command).**

   ```
   python3 <SKILL_DIR>/scripts/build-report.py "<RUN_DIR>" "<project_root>/research/Comment-Mining_<RUN>.html" --open
   ```

   Stdlib only, no venv. Renders the headline, reply queue, clusters, unclustered leftovers, suspected campaigns, and a scope table (channel / video / views / comments / signals, own-channel rows highlighted). Every comment card carries its tier badges, likes, age, source-video link, and a **copy search string** button.
8. **Report back in chat:** the file path, the headline, the cluster names with counts, and the reply queue as verbatim quotes with their video links. **Verbatim matters** — Jason acts on these by searching the exact phrase in his own comment section, so never paraphrase a comment he's meant to go find.

---

## Rules of Thumb
- **yt-dlp end to end — free, no key, no browser.** If yt-dlp breaks, surface it. Don't reach for the YouTube Data API, Apify, or browser scraping.
- **Scripts own the mechanical work.** You never filter a comment by hand, compute a score, or count a cluster. You resolve targets, run two commands, and write one `clusters.json`.
- **Default 3 competitor channels + Jason's channel, 3 videos each.** ~12 videos, ~800-1000 comments, ~100 signals. Enough to cluster, small enough to read.
- **Own channel is never optional.** Competitor-only mining tells you what topics work but nothing about what your own audience is blocked on.
- **Flag campaigns, never auto-drop them.** An early version silently binned "motion graphics" as astroturf. Losing a real topic is worse than surfacing one junk idea, so the script flags and you judge.
- **Praise with a question in it is signal; praise alone is noise.** The filter keeps "Great video, but which MCP did you use?" and drops "Great video." Don't second-guess it by re-reading the dropped set.
- **Never invent a comment, an author, or a count.** Everything in the report traces to a scraped comment. If a cluster feels thin, it is thin — say so in the verdict.
- Create `research/` if missing. Never delete or overwrite a prior report — every run writes a new dated file.
- Intermediates (`meta/`, `signals.json`, `clusters.json`) live in `<RUN_DIR>` = `/tmp/yt-comments/<RUN>/`, timestamped and disposable. The HTML in `research/` is the durable artifact.

## Bash hygiene
- **Never nest shell loops in one Bash call.** A `for` containing a `while read` gets silently rejected by the harness and the user just sees a hang. Both scripts here take their whole target list as arguments precisely so no loop is needed.
- **Keep each Bash call atomic.** Mine, then read, then build — three calls, so failures localize and progress is visible.
- **Substitute literal paths.** `<RUN_DIR>` is not a shell variable that survives between calls.
