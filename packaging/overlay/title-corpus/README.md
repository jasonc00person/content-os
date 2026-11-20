# title-corpus/ — the long-form title bank for `hook-generator`

`titles.json` is built here, not shipped: every long-form title on your own channel plus every
`## YouTube` channel in `competitor-list.md` (newest 400 each), with views, an approximate date, and
a per-channel **breakout** score (views ÷ that channel's median) so titles rank by how hard they
beat their own baseline, not by channel size.

Build it once the brand kit has filled `competitor-list.md` (about 30 seconds, yt-dlp only, no key):

```bash
python3 title-corpus/build.py
```

`--own` defaults to the YouTube handle in `CLAUDE.md`; pass it explicitly before the brand kit is
applied. Rebuild quarterly or whenever a batch of winners lands (recent uploads can't be scored until
their views settle, so a stale corpus always misses the newest wave). `hook-generator` reads it
through `find_titles.py`; nothing reads the raw file.
