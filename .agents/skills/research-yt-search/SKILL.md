---
name: research-yt-search
description: "Explores YouTube search via yt-dlp — pulls 20 results per search term with `ytsearch20:`, fetches full metadata for every candidate in parallel, filters out shorts (duration > 60s), picks the top 5 by views per term, then sorts the global pool high-to-low and writes the report directly. No browser, no subagent. Use this when you want to discover what's working in a niche by topic/keyword rather than by tracked competitor channel. Triggers: yt search research, youtube search research, what's trending for the keyword, explore youtube search, search-based youtube research, research yt search, youtube niche keyword research."
---

# YT Search Research — Top 5 Long-Form Videos by Views Per Search Term

The orchestrator pulls `ytsearch20:<term>` for each search term via `yt-dlp --flat-playlist`, then fetches full metadata for every candidate video in parallel with `xargs -P 20`. Filters shorts out (duration ≤ 60s), sorts each term's pool by view count, takes the top 5, then sorts the global pool high-to-low and writes the report directly.

## How to Trigger
- "research yt search for <terms>"
- "what's trending on youtube for <term>"
- "explore yt search around <topic>"
- "yt keyword research"

## When to Use This vs research-yt-competitors

| Use this skill | Use research-yt-competitors |
|---|---|
| You want to explore a topic/niche by keyword | You want to track specific channels you already know |
| You're looking for fresh creators you don't follow | You want week-over-week tracking of known competitors |
| You want to see how the algorithm ranks a topic | You want each channel's recent best regardless of topic |

## Prerequisites

- **`yt-dlp`** installed and on PATH. Already used by `transcribe-url` and `research-yt-competitors`. Update if it warns about being >90 days old: `pip install -U yt-dlp` or `brew upgrade yt-dlp`.
- **`jq`** installed (for parsing/sorting the metadata JSON).
- **Search terms** — either supplied inline by the user, or read from `competitor-list.md`'s `## YouTube Search Terms` section. Each line in that section that starts with `- ` is treated as one search term (everything after the dash, trimmed).
- **A `research/`** directory at the project root (created if missing).

## Inputs

### Search terms
Default: read `competitor-list.md`, find the `## YouTube Search Terms` section, and extract every line starting with `- `. Each line is one term.
Override: user can name terms inline ("research yt search for 'ai automation', 'n8n agent', 'Codex agents'").

If the section is missing/empty AND no inline terms, ask the user.

---

## Architecture

```
Orchestrator → yt-dlp --flat-playlist (per term, ytsearch20)
            → parallel yt-dlp -J --skip-download (all URLs across all terms)
            → jq filter shorts + sort + slice top 5 per term
            → jq dedupe by URL + global sort by views
            → write report
            → research/YT-Search-Research_YYYY-MM-DD.md
```

**Why this design:**
- **Same architecture as research-yt-competitors.** No browser, no subagent — orchestrator runs the bash directly. Eliminates the entire failure class around hidden tabs, hydration races, DOM selector drift, and Chrome MCP focus issues.
- **`ytsearch20:` per term.** yt-dlp's native search prefix. Returns results in YouTube's default relevance ranking, mirroring what shows up on the search results page. We pull 20 (vs the ~20 visible tiles in browser) to give room for shorts filtering and view sorting (top 5 of 20 by views ≠ top 5 by relevance).
- **Shorts filtered post-fetch via `duration > 60`.** yt-dlp doesn't have a search-side `&sp=EgIQAQ%253D%253D` long-form filter — search returns mixed results. We pull everything and drop anything ≤60s in the jq step.
- **Parallel fetch with `xargs -P 20`.** 20 candidates × N terms finishes in ~10-30s total, regardless of term count (network-bound).
- **No session cookies** means yt-dlp's search ranking ≠ what a logged-in user sees on youtube.com (no personalization, no watch-history bias). For pure "what's getting views on this topic" research, that's actually cleaner.
- **Top 5 by views per term** (vs top 3 per channel in competitor research). Search results pool is more diverse — wider net per term gives better signal.

---

## Main Skill Flow

### 1. Resolve search terms
Read `competitor-list.md` from the project root. Find the `## YouTube Search Terms` section, extract every line starting with `- `, and use everything after the dash (trimmed) as the term. If the user named terms inline, use those instead. If the section is missing/empty and no inline terms, ask the user.

### 2. Compute paths
- Today's date: `YYYY-MM-DD`
- Report path: `<project_root>/research/YT-Search-Research_<DATE>.md`
- Scratch dir: `/tmp/yt-search-research-<DATE>/`
- Create both if missing. Same-day rerun overwrites the report — that's fine.

### 3. Stage the terms file
Write the resolved terms to `terms.txt`, one per line. Substitute the actual terms into the heredoc:

```bash
SCRATCH="/tmp/yt-search-research-$(date +%Y-%m-%d)" && rm -rf "$SCRATCH" && mkdir -p "$SCRATCH/urls" "$SCRATCH/meta" && cat > "$SCRATCH/terms.txt" <<'EOF'
ai automation
n8n agent
Codex agents
EOF
wc -l "$SCRATCH/terms.txt"
```

Why a file (not `$TERMS` env var like the competitor skill does for handles): terms contain spaces and special characters, so they can't be safely passed through a space-split env var. Writing them to a file once means the rest of the pipeline can iterate without quoting headaches.

### 4. Pull candidate URLs (per term)
**One Bash call. Single `while read` loop, one slug-derive + one yt-dlp + one printf in the body — no nested loops.**

```bash
SCRATCH="/tmp/yt-search-research-$(date +%Y-%m-%d)" && : > "$SCRATCH/slug_term.tsv" && while IFS= read -r term; do [ -z "$term" ] && continue; slug=$(printf '%s' "$term" | tr '[:upper:]' '[:lower:]' | tr -c 'a-z0-9' '-' | sed 's/-\{2,\}/-/g; s/^-//; s/-$//'); yt-dlp --flat-playlist --print url "ytsearch20:${term}" 2>/dev/null > "$SCRATCH/urls/${slug}.txt"; printf '%s\t%s\n' "$slug" "$term" >> "$SCRATCH/slug_term.tsv"; done < "$SCRATCH/terms.txt" && wc -l "$SCRATCH/urls/"*.txt
```

The slug is a filename-safe version of the term (lowercase, alphanumeric, hyphens). It keys the URL files, the metadata files, and the slug→term mapping in `slug_term.tsv`.

A few hundred ms per term. Don't parallelize this step — the per-video fetch in step 6 is the heavy lift.

If a term's URL file is empty, the search returned nothing. Note it and skip in the report.

### 5. Build slug+URL TSV
**Use `awk` over the URL files. Do NOT use a nested `for ... do ... while read ... done` shell loop — those silently get rejected by the harness.**

```bash
awk 'FNR==1{s=FILENAME; sub(/.*\//,"",s); sub(/\.txt$/,"",s)} {print s"\t"$0}' "$SCRATCH/urls/"*.txt > "$SCRATCH/all_urls.tsv" && wc -l "$SCRATCH/all_urls.tsv"
```

`FNR==1` triggers per-file: it strips the directory and `.txt` extension to derive the slug, then awk prepends it to every URL line in that file.

### 6. Parallel fetch full metadata
One JSON file per video, named `<slug>__<videoId>.json`:

```bash
awk -F'\t' '{print $1, $2}' "$SCRATCH/all_urls.tsv" | xargs -P 20 -L 1 sh -c 'slug=$1; url=$2; id=$(echo "$url" | grep -oE "v=[^&]+" | cut -d= -f2); yt-dlp -J --skip-download "$url" 2>/dev/null > "'"$SCRATCH"'/meta/${slug}__${id}.json"' _ && ls "$SCRATCH/meta" | wc -l
```

`-P 20` is the sweet spot. Higher gives diminishing returns and risks YT rate-limiting (HTTP 429). Set Bash `timeout: 300000` (5 min) — 20 videos × N terms parallelized 20-wide finishes in ~15-30s, but allow headroom.

### 7. Filter shorts, attach term, top 5 per term, dedupe, global sort
**Two Bash calls. Single-line `for` loop with one jq inside the body — no nested loops.**

```bash
for f in "$SCRATCH"/meta/*.json; do slug=$(basename "$f" .json | sed 's/__.*//'); term=$(awk -F'\t' -v s="$slug" '$1==s{print $2; exit}' "$SCRATCH/slug_term.tsv"); jq -c --arg s "$slug" --arg t "$term" 'select(type=="object" and .view_count != null and (.duration // 0) > 60) | {slug:$s, term:$t, url:.webpage_url, title:.title, channel:.channel, views:.view_count, likes:.like_count, upload_date:.upload_date, duration:.duration, description:((.description // "") | gsub("https?://\\S+"; "[LINK]"))}' "$f"; done > "$SCRATCH/all_meta.jsonl" && wc -l "$SCRATCH/all_meta.jsonl"
```

```bash
jq -s 'group_by(.slug) | map(sort_by(-.views) | .[0:5]) | add | group_by(.url) | map({url:.[0].url, title:.[0].title, channel:.[0].channel, views:.[0].views, likes:.[0].likes, upload_date:.[0].upload_date, duration:.[0].duration, description:.[0].description, terms:(map(.term) | unique)}) | sort_by(-.views)' "$SCRATCH/all_meta.jsonl" > "$SCRATCH/all_top5.json" && jq 'length' "$SCRATCH/all_top5.json"
```

`$SCRATCH/all_top5.json` is now a single JSON array of up to 5×N videos (minus duplicates), globally view-sorted. Each entry has a `terms` array listing every search term that surfaced it in its top-5 — the dedupe step folds duplicates and unions their source terms.

### 8. Tag + write the report
Read `$SCRATCH/all_top5.json`. For each video, add:
- **Topic tag** — Education / Journey / Hot take / Lifestyle / Behind-the-scenes / Build-in-public / Story / Tutorial
- **CTA type** — Comment-bait / Subscribe-bait / Watch-next / Link-in-desc / DM / None
- **Why it ranked** — one line on hook archetype, format mechanic, topic angle, or engagement trigger that likely got it ranked for this search

Add a **Pattern paragraph** at the top — 2-3 sentences on what's repeating across the pool: dominant themes, hook archetypes, format mechanics, title patterns, channel size mix (big channels dominating vs small channels breaking through), etc. If a term returned zero long-form results (all shorts, or empty search), call it out in the Pattern line.

Write to: `<project_root>/research/YT-Search-Research_<DATE>.md`

Format EXACTLY:

```
# YT Search Research — Top Videos By Search Term

**Generated:** YYYY-MM-DD | **Terms searched:** N | **Videos in report:** M (top 5 long-form by views per term, deduped)

> **Pattern:** <2-3 sentences on what's repeating across the pool — dominant themes, hook archetypes, title patterns, format mechanics, channel-size dynamics. Be specific.>

**Search terms:** `<term 1>` · `<term 2>` · `<term 3>` …

---

### 1. [<TITLE>](<URL>) — <CHANNEL>

`<views> views · <likes> likes` · <like%> like rate · posted <date> · ranked for: `<term>`

**Topic:** <tag> · **CTA:** <type>

**Why it ranked:** <one line>

> <full description, blockquoted. Preserve line breaks. Don't truncate.>

---

### 2. [<TITLE>](<URL>) — <CHANNEL>

[same structure, repeat for every video in the pool, ordered by views high-to-low]
```

RULES:
- Format view counts human-readable (1.1M, 296K, 47.3K). Likes same.
- Like rate: likes ÷ views × 100, rounded to 1 decimal (e.g. "1.8%"). If likes is null, write "n/a like rate".
- Date: convert `YYYYMMDD` from `upload_date` to `YYYY-MM-DD`.
- TITLE is the full title from yt-dlp. Trim emojis only if they break the markdown link.
- "ranked for" shows which search term(s) surfaced this video. If the video appeared in multiple terms' top-5s, list all of them separated by ` · `.
- Strict view-sort across the whole pool — no editorial reordering.
- No closing wrap-up. The list IS the report.

### 9. Cleanup
```bash
rm -rf "$SCRATCH"
```

### 10. Report file path back to the user.

---

## Rules of Thumb
- yt-dlp must be reasonably fresh. The `>90 days old` warning is harmless for one-off scrapes but YouTube's extractor changes — if `ytsearch20:` suddenly returns nothing, update yt-dlp first before assuming the search is broken.
- `-P 20` parallelism is plenty. Beyond that you risk YT rate-limiting (HTTP 429).
- A term returning fewer than 5 long-form videos (after shorts filtering) is fine — niche terms just have less long-form coverage. Take what's there.
- **Why 20 candidates per term (not 50)?** Mirrors what's visible on a single search results page without scrolling. Going deeper risks pulling stale "all-time" results that aren't representative of current ranking.
- **Why filter shorts?** Search-results page in browser uses the long-form filter chip (`&sp=EgIQAQ%253D%253D`); we replicate that post-fetch since yt-dlp's search prefix doesn't support it natively.
- Live streams and premieres show `view_count: null` until they end — the jq `select(.view_count != null)` filter drops them automatically.
- Same video may appear in multiple terms' top-5s. The dedupe step folds it into one entry with all source terms in `ranked for`.
- Research is research-skills only. Don't reach for Apify, browser scraping, or other fallbacks. If yt-dlp breaks, surface it — don't paper over.
- Create `research/` if missing. Don't inspect or clean up prior reports — every run writes a new dated file.
- Report contains every unique top-5-per-term video. No padding, no editorial cuts.

## Bash hygiene (this skill burned a lot of cycles on this — read it)
- **Never nest shell loops in a single Bash call.** A `for` containing a `while IFS= read -r ...` (or any `do...done` inside another `do...done`) will silently get rejected by the harness with "user doesn't want to proceed" and no actual permission prompt. The user just sees you hang.
- **Iterate with `awk` or `find | xargs`, not nested `for/while`.** Step 5's awk-with-FILENAME is the canonical pattern: zero shell loops, derives the slug from the filename.
- **Single-line `for` or `while read` loops with one logical body are fine.** Steps 4 and 7 use that pattern — passes.
- **Keep each Bash call atomic — one logical step.** Don't chain "stage terms then fetch URLs then parallel-fetch metadata then sort" in one giant `&&` block. Each step gets its own Bash tool call so failures localize and the user can see progress.
- If a Bash call comes back with "user doesn't want to proceed" but the user says they got no prompt, the command shape is the problem — simplify and split, don't retry the same call.
