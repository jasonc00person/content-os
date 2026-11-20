#!/usr/bin/env python3
"""Slice title-corpus/titles.json — the long-form counterpart to find_hooks.py.

    find_titles.py --list                              # archetypes: count, median breakout, best example
    find_titles.py --archetype experiment --top 12     # top titles in one archetype (by breakout)
    find_titles.py --keyword "motion graphics" --top 15
    find_titles.py --own --top 15                      # the creator's own winners
    find_titles.py --days 120 --top 20                 # what's breaking out recently
    find_titles.py --pattern "^I (taught|let|made)" --top 10

Ranking is by BREAKOUT (views / that channel's median), so a 100K video on a 2K-median
channel outranks a 300K video on a 350K-median channel. Raw views shown alongside.
"""
import argparse, json, os, re, statistics, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))
CORPUS = os.path.join(ROOT, "title-corpus", "titles.json")

# first match wins — order from most specific to most generic
ARCHETYPES = [
    ("experiment",  r"^\s*i (taught|let|made|forced|told|asked|gave|tried|tested|spent|paid|built|replaced|hired|fired|ran|used|automated|turned)\b|\bi (taught|let|made|replaced|fired) \b"),
    ("cost",        r"\$\s?\d|\b\d+ ?(k|m)\b.*\b(cost|spent|paid|revenue|per month|/mo|a month)\b|\bfor (just )?\$|\bfree\b.*\b(vs|instead)\b|\bcost me\b|\bworth (it|the price)\b"),
    ("news-shock",  r"\b(just (killed|dropped|changed|broke|leaked|launched|released|ended|replaced)|is (dead|over|finished|here|insane|cooked)|killed|officially|new .{0,25}(just|is here)|game.?changer|changes everything|the end of)\b"),
    ("warning",     r"\b(stop|never|don'?t|should be illegal|before you|mistake|wrong|why you|the truth|nobody tells|lie|scam|warning|red flag|beware)\b"),
    ("versus",      r"\bvs\.?\b|\bversus\b|\bor\b.{0,20}\?|\bwhich (is|one)\b|\bcompared\b|\bbetter than\b|\bbeats\b"),
    ("course",      r"\b(full course|crash course|complete guide|masterclass|\d+ ?(hour|hr) course|everything you need|for beginners|beginner'?s guide|from scratch|a to z|explained)\b"),
    ("listicle",    r"^\s*\d+ |\b\d+ (ways|tools|things|tips|prompts|skills|agents|apps|ideas|mistakes|habits|secrets|steps|reasons|use cases|workflows|hacks|examples)\b"),
    ("how-to",      r"^\s*how (to|i|we|you)\b|\bhow (to|i) \b|\bstep.by.step\b|\btutorial\b|\bsetup\b|\bfull (setup|build|walkthrough)\b"),
    ("outcome",     r"\b(in \d+ (min|minute|hour|day|week)s?|\bwithout\b|\bfrom zero\b|\bin one prompt\b|\bautomat(e|ed|ically)\b|\bon autopilot\b|\bwhile you sleep\b|\breplac(e|es|ing)\b)"),
    ("question",    r"\?\s*$"),
]
ARCH_C = [(n, re.compile(p, re.I)) for n, p in ARCHETYPES]


def archetype(title):
    for n, p in ARCH_C:
        if p.search(title or ""):
            return n
    return "other"


def fmt(n):
    n = n or 0
    if n >= 1_000_000: return f"{n/1_000_000:.1f}M".replace(".0M", "M")
    if n >= 1_000: return f"{n/1_000:.0f}K"
    return str(n)


def month(ts):
    if not ts: return "????-??"
    import datetime
    return datetime.datetime.fromtimestamp(ts, datetime.timezone.utc).strftime("%Y-%m")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true", help="archetype table")
    ap.add_argument("--archetype", help="one archetype name, or 'all' for a spread")
    ap.add_argument("--keyword", help="substring in title (case-insensitive); comma = OR")
    ap.add_argument("--pattern", help="regex on title")
    ap.add_argument("--own", action="store_true", help="only the creator's own channel")
    ap.add_argument("--handle", help="only this @handle")
    ap.add_argument("--days", type=int, help="only titles newer than N days")
    ap.add_argument("--min-breakout", type=float, default=1.0)
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--corpus", default=CORPUS)
    a = ap.parse_args()

    if not os.path.exists(a.corpus):
        sys.exit(f"no corpus at {a.corpus} — run: python3 title-corpus/build.py")
    d = json.load(open(a.corpus, encoding="utf-8"))
    vids = [v for v in d["videos"] if v.get("breakout") is not None]
    for v in vids:
        v["arch"] = archetype(v["title"])
    print(f"corpus built {d['built']} · {len(vids)} scoreable titles · {len(d['channels'])} channels\n")

    if a.list:
        rows = []
        for n, _ in ARCHETYPES + [("other", None)]:
            g = [v for v in vids if v["arch"] == n]
            if not g: continue
            g.sort(key=lambda v: -v["breakout"])
            big = sum(1 for v in g if v["breakout"] >= 3)
            rows.append((n, len(g), statistics.median(v["breakout"] for v in g), big, g[0]))
        rows.sort(key=lambda r: -r[2])
        print(f"{'archetype':<12}{'n':>5}{'median':>8}{'≥3x':>6}   best example")
        for n, c, med, big, best in rows:
            print(f"{n:<12}{c:>5}{med:>7.2f}x{big:>6}   [{best['breakout']:.1f}x] {best['title'][:70]}  @{best['handle']}")
        print("\nmedian = typical breakout of titles in that shape · ≥3x = how many were real outliers")
        return

    sel = vids
    if a.own: sel = [v for v in sel if v["is_own"]]
    if a.handle: sel = [v for v in sel if v["handle"].lower() == a.handle.lstrip("@").lower()]
    if a.days: sel = [v for v in sel if v.get("age_days") is not None and v["age_days"] <= a.days]
    if a.keyword:
        kws = [k.strip().lower() for k in a.keyword.split(",") if k.strip()]
        sel = [v for v in sel if any(k in (v["title"] or "").lower() for k in kws)]
    if a.pattern:
        rx = re.compile(a.pattern, re.I)
        sel = [v for v in sel if rx.search(v["title"] or "")]
    sel = [v for v in sel if v["breakout"] >= a.min_breakout]

    def show(rows):
        for v in rows:
            own = " ★" if v["is_own"] else ""
            print(f"[{v['breakout']:>5.1f}x] {fmt(v['views']):>5}  {month(v['ts'])}  {v['arch']:<11} @{v['handle']}{own}\n         {v['title']}")

    if a.archetype and a.archetype != "all":
        sel = [v for v in sel if v["arch"] == a.archetype]
    sel.sort(key=lambda v: -v["breakout"])

    if a.archetype == "all":
        per = max(2, a.top // len(ARCHETYPES))
        for n, _ in ARCHETYPES:
            g = [v for v in sel if v["arch"] == n][:per]
            if not g: continue
            print(f"── {n}")
            show(g); print()
    else:
        show(sel[:a.top])
        if not sel:
            print("(nothing matched — loosen --keyword / --min-breakout)")
    print("\n★ = own channel · breakout = views ÷ that channel's median")


if __name__ == "__main__":
    main()
