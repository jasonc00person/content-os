# transcripts/ — conventions

Raw video transcripts, organized by **where they came from** (not who made them).
Keep this folder self-maintaining: every transcript lands in one of the three
subfolders below with the standard filename. **Nothing loose at the top level.**

## Where it goes

| Subfolder | Holds | Produced by |
|-----------|-------|-------------|
| `url/` | Transcript of any video pulled from a URL — YouTube, IG, TikTok, X, etc. Jason's own *and* competitors both live here. | `transcribe-url` skill (default output dir), `ig-competitor-research` enrichment, ad-hoc yt-dlp pulls |
| `local/` | Transcript of a file already on disk (e.g. something in `~/Downloads`). | local faster-whisper runs |
| `analysis/` | Video-*derived* docs that are **not** raw transcripts — script-structure beat-maps, packaging breakdowns. | scripting/research passes |

Jason's own content is **not** split out here — find it by handle in the filename
(`video-by-jasoncooperson_*`, etc.). His curated top performers live in `voice-corpus/`.

## Filename

```
<title-slug>_<YYYY-MM-DD>.md          # transcripts (url/ and local/)
<title-slug>_<YYYY-MM-DD>_STRUCTURE.md # analysis/ (script-structure docs)
```

- **slug** = the video title, lowercased, non-alphanumerics → `-`, collapsed, max 60 chars.
  (`transcribe-url.sh` builds this automatically.)
- **date** = the date you pulled it, *not* the upload date. Two videos with the same
  title are distinguished by date; the real source URL is always in the file's header.
- No video IDs in the filename — the canonical URL lives inside the file.

## Rules

- **Don't re-transcribe.** Search `transcripts/` for the URL/title first; if it's already
  here, read the existing file.
- **Never delete** existing transcripts. A repeat pull just writes a new dated file.
- Every transcript file starts with an H1 title and a metadata block (Source URL,
  Uploader, Uploaded, Duration), then `## Transcript` / `## Timestamped`.
