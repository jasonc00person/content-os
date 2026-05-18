---
name: research-yt-competitors
description: "Scans YouTube competitors via yt-dlp — pulls each channel's 10 most recent uploads, fetches full metadata for every candidate in parallel, picks the top 3 by views per channel, then sorts the global pool high-to-low and writes the report directly. No browser, no subagent. Triggers: youtube competitor research, yt research, what's working on youtube, youtube outliers, research yt competitors, youtube niche research."
---

# YT Competitor Research — Top 3 Long-Form Videos by Views Per Channel

The orchestrator pulls each competitor's recent uploads via `yt-dlp --flat-playlist`, then fetches full metadata for every candidate video in parallel with `xargs -P 20`. Sorts each channel's pool by view count, takes the top 3, then sorts the global pool high-to-low and writes the report directly.

## How to Trigger
- "research my yt competitors" / "run yt content research"
- "what's working on youtube in my niche"
- "find yt outliers on @handle, @handle, @handle"

## Prerequisites

- **`yt-dlp`** installed and on PATH. Already used by `transcribe-url`. Update if it warns about being >90 days old: `pip install -U yt-dlp` or `brew upgrade yt-dlp`.
- **`jq`** installed (for parsing/sorting the metadata JSON).
- **A `competitor-list.md`** in the project root with a `## YouTube` section listing channels via `youtube.com/@handle` URLs.
- **A `research/`** directory at the project root (created if missing).

## Inputs

### Competitor handles
Default: read `competitor-list.md`, find the `## YouTube` section, extract `@handle`s from `youtube.com/@handle` URLs in that section, and use the **first 3 listed** (top of the list = highest priority). Don't ask — just take the top 3.
Override: user can name specific handles inline ("just nick and patrick", "research @creator_one and @creator_two") or say "all" to scrape every channel listed.

---

## Architecture

```
Orchestrator → yt-dlp --flat-playlist (per channel, get newest 10 URLs)
            → parallel yt-dlp -J --skip-download (all URLs across all channels)
            → jq sort + slice top 3 per channel
            → jq global sort by views
            → write report
            → research/YT-Competitor-Research_YYYY-MM-DD.md
```

**Why this design:**
- **No browser.** Eliminates the entire failure class around hidden tabs, sticky sort state, hydration races, DOM selector drift, and Chrome MCP focus issues.
- **yt-dlp doesn't carry session cookies**, so YouTube can't serve it the "Popular" sort it remembers from a prior manual visit. `/videos` returns chronological newest-first by default — no Latest-chip click needed.
- **Parallel fetch with `xargs -P 20`.** 10 candidates × N channels finishes in ~5-15 seconds total, regardless of channel count (network-bound, not concurrency-bound).
- **Full description, exact metadata.** `yt-dlp -J` returns the complete description (no 160-char `og:description` truncation), exact view + like counts, and ISO upload date.
- **No subagent needed.** Orchestrator runs the bash directly — skill is self-contained, no model-budget concerns, no agent handoff.

---

## Main Skill Flow

### 1. Resolve handles
Read `competitor-list.md` from the project root. Find the `## YouTube` section, extract `@handle`s from `youtube.com/@handle` URLs in that section, and **default to the first 3** (top of the list = highest priority — don't ask). If the user named specific handles inline, use those. If the user explicitly said "all", use every handle in the section. If the section is missing/empty and no inline handles, ask the user.

### 2. Compute paths
- Today's date: `YYYY-MM-DD`
- Report path: `<project_root>/research/YT-Competitor-Research_<DATE>.md`
- Scratch dir: `/tmp/yt-research-<DATE>-$$/`
- Create both if missing. Same-day rerun overwrites the report — that's fine.

### 3. Pull candidate URLs (per channel)
**One Bash call. Single-line `for` loop, one operation in the body.**

```bash
SCRATCH="/tmp/yt-research-$(date +%Y-%m-%d)" && rm -rf "$SCRATCH" && mkdir -p "$SCRATCH/urls" "$SCRATCH/meta" && for h in $HANDLES; do yt-dlp --flat-playlist --print url --playlist-end 10 "https://www.youtube.com/@${h}/videos" 2>/dev/null > "$SCRATCH/urls/${h}.txt"; done && wc -l "$SCRATCH/urls/"*.txt
```

Few hundred ms per channel. Don't parallelize this step — the per-video fetch is the heavy lift.

If a handle's URL file is empty, the channel doesn't exist or has no public uploads. Note it and skip in the report.

### 4. Build handle+URL TSV
**Use `awk` over the URL files. Do NOT use a nested `for ... do ... while read ... done` shell loop — those silently get rejected by the harness.**

```bash
awk 'FNR==1{h=FILENAME; sub(/.*\//,"",h); sub(/\.txt$/,"",h)} {print h"\t"$0}' "$SCRATCH/urls/"*.txt > "$SCRATCH/all_urls.tsv" && wc -l "$SCRATCH/all_urls.tsv"
```

`FNR==1` triggers per-file: it strips the directory and `.txt` extension to derive the handle, then awk prepends it to every URL line in that file.

### 5. Parallel fetch full metadata
One JSON file per video, named `<handle>__<videoId>.json`:

```bash
awk -F'\t' '{print $1, $2}' "$SCRATCH/all_urls.tsv" | xargs -P 20 -L 1 sh -c 'handle=$1; url=$2; id=$(echo "$url" | grep -oE "v=[^&]+" | cut -d= -f2); yt-dlp -J --skip-download "$url" 2>/dev/null > "'"$SCRATCH"'/meta/${handle}__${id}.json"' _ && ls "$SCRATCH/meta" | wc -l
```

`-P 20` is the sweet spot. Higher gives diminishing returns and risks YT rate-limiting (HTTP 429). Set Bash `timeout: 300000` (5 min) — 20 videos × ~3-5s each parallelized 20-wide finishes in ~10-15s, but allow headroom for larger channel lists.

### 6. Pick top 3 per channel, then pool globally
**Two Bash calls. Single-line `for` loop with a single jq inside the body — no nested loops.**

```bash
for f in "$SCRATCH"/meta/*.json; do h=$(basename "$f" .json | sed 's/__.*//'); jq -c --arg h "$h" 'select(type=="object" and .view_count != null) | {handle:$h, url:.webpage_url, title:.title, views:.view_count, likes:.like_count, upload_date:.upload_date, description:((.description // "") | gsub("https?://\\S+"; "[LINK]"))}' "$f"; done > "$SCRATCH/all_meta.jsonl"
```

```bash
jq -s 'group_by(.handle) | map(sort_by(-.views) | .[0:3]) | add | sort_by(-.views)' "$SCRATCH/all_meta.jsonl" > "$SCRATCH/all_top3.json" && jq 'length' "$SCRATCH/all_top3.json"
```

`$SCRATCH/all_top3.json` is now a single JSON array of up to 3×N videos, globally view-sorted.

### 7. Tag + write the report
Read `$SCRATCH/all_top3.json`. For each video, add:
- **Topic tag** — Education / Journey / Hot take / Lifestyle / Behind-the-scenes / Build-in-public / Story / Tutorial
- **CTA type** — Comment-bait / Subscribe-bait / Watch-next / Link-in-desc / DM / None
- **Why it worked** — one line on hook archetype, format mechanic, topic angle, or engagement trigger

Add a **Pattern paragraph** at the top — 2-3 sentences on what's repeating across the pool: dominant themes, hook archetypes, format mechanics, title patterns. Be specific. If a channel had a fetch error, omit it from the body but call it out in the Pattern line.

Write to: `<project_root>/research/YT-Competitor-Research_<DATE>.md`

Format EXACTLY:

```
# YT Competitor Research — Top Long-Form Videos

**Generated:** YYYY-MM-DD | **Channels scraped:** N | **Videos in report:** M (top 3 by views per channel)

> **Pattern:** <2-3 sentences on what's repeating across the pool — dominant themes, hook archetypes, title patterns, format mechanics. Be specific.>

---

### 1. [<TITLE>](<URL>) — @handle

`<views> views · <likes> likes` · <like%> like rate · posted <date>

**Topic:** <tag> · **CTA:** <type>

**Why it worked:** <one line>

> <full description, blockquoted. Preserve line breaks. Don't truncate.>

---

### 2. [<TITLE>](<URL>) — @handle

[same structure, repeat for every video in the pool, ordered by views high-to-low]
```

RULES:
- Format view counts human-readable (1.1M, 296K, 47.3K). Likes same.
- Like rate: likes ÷ views × 100, rounded to 1 decimal (e.g. "1.8%"). If likes is null, write "n/a like rate".
- Date: convert `YYYYMMDD` from `upload_date` to `YYYY-MM-DD`.
- TITLE is the full title from yt-dlp. Trim emojis only if they break the markdown link.
- Strict view-sort across the whole pool — no editorial reordering.
- No closing wrap-up. The list IS the report.

### 8. Cleanup
```bash
rm -rf "$SCRATCH"
```

### 9. Report file path back to the user.

---

## Rules of Thumb
- yt-dlp must be reasonably fresh. The `>90 days old` warning is harmless for one-off scrapes but YouTube's extractor changes — if a channel suddenly returns nothing, update yt-dlp first before assuming the channel's gone.
- `-P 20` parallelism is plenty. Beyond that you risk YT rate-limiting (HTTP 429).
- A channel returning fewer than 10 videos is fine — small/new channels just have fewer uploads. Take what's there.
- **Why 10 (not 30)?** We want signal on what's working *recently*, not the channel's all-time hits within a deeper feed. With 30, a 3-month-old viral video drowns out the last few weeks of work. Don't bump this back up.
- Live streams and premieres show `view_count: null` until they end — the jq `select(.view_count != null)` filter drops them automatically.
- Research is research-skills only. Don't reach for Apify, browser scraping, or other fallbacks. If yt-dlp breaks, surface it — don't paper over.
- Create `research/` if missing. Don't inspect or clean up prior reports — every run writes a new dated file.
- Report contains every top-3-per-channel video. No padding, no editorial cuts.

## Bash hygiene (this skill burned a lot of cycles on this — read it)
- **Never nest shell loops in a single Bash call.** A `for` containing a `while IFS= read -r ...` (or any `do...done` inside another `do...done`) will silently get rejected by the harness with "user doesn't want to proceed" and no actual permission prompt to the user. The user just sees you hang.
- **Iterate with `awk` or `find | xargs`, not nested `for/while`.** Step 4's awk-with-FILENAME is the canonical pattern: zero shell loops, derives the handle from the filename.
- **Single-line `for` loops with one operation in the body are fine.** Steps 3 and 6 use `for h in $HANDLES; do <one command>; done` — that pattern passes.
- **Keep each Bash call atomic — one logical step.** Don't chain "build TSV then fetch metadata then sort" in one giant `&&` block. Each step gets its own Bash tool call so failures localize and the user can see progress.
- If a Bash call comes back with "user doesn't want to proceed" but the user says they got no prompt, the command shape is the problem — simplify and split, don't retry the same call.
