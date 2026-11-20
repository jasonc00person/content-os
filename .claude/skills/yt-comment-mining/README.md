# yt-comment-mining — setup

Reads the comment sections of your own recent uploads plus tracked competitors, strips the praise and noise, tiers what's left by intent, clusters it into video ideas, and builds a self-contained HTML report with a reply queue. Claude drives it — you just trigger it ("mine my comments", or name channels inline).

## Prerequisites

Free, no accounts, no API keys.

- **`yt-dlp`** — pulls the comments (`--write-comments`). Installed by `./setup.sh` from the project root; `./check-setup.sh` reports what's missing. Keep it fresh when it warns about being >90 days old: `brew upgrade yt-dlp` (macOS), `winget upgrade yt-dlp.yt-dlp` (Windows), `uv tool upgrade yt-dlp` (Linux / uv installs).
- **Python 3** — stdlib only. No venv, no pip, nothing to build.
- **`competitor-list.md`** in the project root with a `## YouTube` section, for the competitor half. Not needed if you only mine your own channel.

The YouTube Data API is deliberately not used: it needs a key, it quotas comment reads, and yt-dlp does neither.

## Output

Writes `research/Comment-Mining_<timestamp>.html` and opens it in your default browser. Sections: headline, reply queue (people blocked on your system right now), demand clusters with the video idea each implies, unclustered leftovers, suspected shill campaigns, and a scope table showing every video scraped with its comment and signal counts.

Every comment appears verbatim with its source video and a one-click **copy search string** button, so you can paste it into your own comment section and answer the person directly.

## Knobs

`--videos N` per channel (default 5, skill uses 3) · `--max-comments N` per video (default 400) · `--min-score N` intent floor (default 5, raise to 8 on a big scrape) · `--own <handle>` marks your channel so its comments get badged.
