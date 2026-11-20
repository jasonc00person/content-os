#!/usr/bin/env python3
"""Assemble signals.json + clusters.json into a self-contained HTML report.

Usage: build-report.py <run_dir> <out.html> [--open]
Stdlib only — no venv, no pillow, no network.
"""
import html, json, os, sys, webbrowser
from datetime import date

TIER_COLOR = {
    "blocker": "#dc2626", "buyer": "#7c3aed", "request": "#2563eb", "objection": "#ea580c",
    "constraint": "#0891b2", "howto": "#059669", "question": "#64748b",
}


ZW = dict.fromkeys(map(ord, "\u200b\u200c\u200d\ufeff\u00a0"), " ")


def clean(t):
    """YouTube reply mentions carry zero-width chars that break a pasted search."""
    return " ".join(str(t or "").translate(ZW).split())


def esc(s):
    return html.escape(str(s if s is not None else ""))


def fmt(n):
    if not n:
        return "0"
    n = int(n)
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M".replace(".0M", "M")
    if n >= 1_000:
        return f"{n/1_000:.1f}K".replace(".0K", "K")
    return str(n)


def card(s, rank=None):
    tiers = "".join(
        f'<span class="tier" style="background:{TIER_COLOR.get(t, "#64748b")}">{esc(t)}</span>'
        for t in s.get("tiers", []))
    own = '<span class="own">your channel</span>' if s.get("is_own_channel") else ""
    reply = '<span class="meta-i">↳ reply</span>' if s.get("is_reply") else ""
    return f"""
<div class="card">
  <div class="card-top">
    <div class="who"><b>{esc(s.get('author'))}</b>{own}
      <span class="meta-i">♥ {esc(s.get('likes'))}</span>
      <span class="meta-i">{esc(s.get('posted'))}</span>{reply}</div>
    <div class="tiers">{tiers}</div>
  </div>
  <div class="text">{esc(s.get('text')).replace(chr(10), '<br>')}</div>
  <div class="card-bot">
    <a class="btn" href="{esc(s.get('video_url'))}" target="_blank">▶ {esc(s.get('video_title'))}</a>
    <button class="btn ghost" data-copy="{esc(clean(s.get('search_string')))}" onclick="cp(this)">⌕ copy search string</button>
  </div>
</div>"""


def main():
    run_dir, out_path = sys.argv[1], sys.argv[2]
    do_open = "--open" in sys.argv

    with open(os.path.join(run_dir, "signals.json")) as f:
        data = json.load(f)
    cl_path = os.path.join(run_dir, "clusters.json")
    clusters = {"headline": "", "clusters": [], "reply_queue": []}
    if os.path.exists(cl_path):
        with open(cl_path) as f:
            clusters = json.load(f)

    signals = data["signals"]
    by_id = {s["id"]: s for s in signals}
    stats = data["stats"]
    used = set()

    # ---- reply queue ----
    rq = [by_id[i] for i in clusters.get("reply_queue", []) if i in by_id]
    rq_html = ""
    if rq:
        rq_html = f"""<section><h2>🔧 Reply queue <span class="count">{len(rq)}</span></h2>
<p class="lede">People who tried to build it and hit a wall. They already believe you. Answer these before you make anything.</p>
{''.join(card(s) for s in rq)}</section>"""

    # ---- clusters ----
    cl_html = []
    for c in clusters.get("clusters", []):
        picks = [by_id[i] for i in c.get("signal_ids", []) if i in by_id]
        used.update(s["id"] for s in picks)
        idea = f'<div class="idea"><span class="idea-l">Video</span>{esc(c.get("video_idea"))}</div>' if c.get("video_idea") else ""
        cl_html.append(f"""<section class="cluster">
  <h2>{esc(c.get('name'))} <span class="count">{len(picks)}</span></h2>
  <p class="verdict">{esc(c.get('verdict'))}</p>{idea}
  {''.join(card(s) for s in picks)}
</section>""")

    # ---- leftovers ----
    rest = [s for s in signals if s["id"] not in used and s["id"] not in {r["id"] for r in rq}]
    rest_html = ""
    if rest:
        rest_html = f"""<section><h2>Unclustered signals <span class="count">{len(rest)}</span></h2>
<details><summary>Everything else that scored above the floor</summary>{''.join(card(s) for s in rest)}</details></section>"""

    # ---- astroturf ----
    astro = data.get("astroturf", [])
    astro_html = ""
    if astro:
        rows = "".join(f"<li><b>{esc(a['channel'])}</b> · {esc(a['author'])}: {esc(a['text'][:180])}</li>"
                       for a in astro)
        astro_html = f"""<section><h2>🚫 Astroturf filtered <span class="count">{len(astro)}</span></h2>
<p class="lede">Same ask, verbatim, across more than one channel. That's a campaign, not demand. Excluded from every cluster above.</p>
<ul class="astro">{rows}</ul></section>"""

    # ---- scope table ----
    rows = "".join(
        f"""<tr class="{'own' if s.get('is_own_channel') else ''}">
        <td>{esc(s.get('channel'))}</td>
        <td><a href="{esc(s.get('url'))}" target="_blank">{esc(s.get('title'))}</a></td>
        <td class="n">{fmt(s.get('views'))}</td>
        <td class="n">{esc(s.get('comments'))}</td>
        <td class="n">{esc(s.get('signals'))}</td></tr>""" for s in stats)
    total_c = sum(s.get("comments") or 0 for s in stats)
    dropped = data.get("dropped", {})
    drop_line = " · ".join(f"{k.replace('_', ' ')}: {v}" for k, v in sorted(dropped.items()))

    doc = f"""<!doctype html><html><head><meta charset="utf-8">
<title>Comment Mining — {date.today().isoformat()}</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>⛏️</text></svg>">
<style>
:root{{--bg:#0f1115;--card:#181b22;--line:#272b35;--tx:#e6e8ee;--dim:#98a1b3;--acc:#f5c518}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--tx);font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,sans-serif}}
.wrap{{max-width:900px;margin:0 auto;padding:40px 20px 80px}}
h1{{font-size:30px;margin:0 0 6px;letter-spacing:-.02em}}
h2{{font-size:19px;margin:0 0 6px;letter-spacing:-.01em}}
.sub{{color:var(--dim);margin:0 0 28px}}
.headline{{background:linear-gradient(135deg,#1c2030,#181b22);border:1px solid var(--line);border-left:3px solid var(--acc);border-radius:10px;padding:18px 20px;margin:0 0 34px;font-size:16px}}
section{{margin:0 0 38px}}
.count{{background:var(--line);color:var(--dim);font-size:12px;padding:2px 8px;border-radius:20px;vertical-align:middle;margin-left:6px}}
.lede,.verdict{{color:var(--dim);margin:0 0 14px;font-size:14px}}
.idea{{background:#141821;border:1px solid var(--line);border-radius:8px;padding:10px 14px;margin:0 0 16px;font-size:14px}}
.idea-l{{color:var(--acc);font-weight:600;font-size:11px;letter-spacing:.08em;text-transform:uppercase;margin-right:10px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:0 0 10px}}
.card-top{{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;align-items:center;margin-bottom:8px}}
.who b{{font-weight:600}}
.meta-i{{color:var(--dim);font-size:12px;margin-left:10px}}
.own{{background:var(--acc);color:#000;font-size:10px;font-weight:700;padding:2px 6px;border-radius:4px;margin-left:8px;text-transform:uppercase}}
.tier{{color:#fff;font-size:10px;font-weight:700;padding:2px 7px;border-radius:4px;margin-left:4px;text-transform:uppercase;letter-spacing:.04em}}
.text{{white-space:pre-wrap;margin:0 0 12px}}
.card-bot{{display:flex;gap:8px;flex-wrap:wrap}}
.btn{{background:#20242e;border:1px solid var(--line);color:var(--dim);font-size:12px;padding:5px 10px;border-radius:6px;text-decoration:none;cursor:pointer;font-family:inherit}}
.btn:hover{{color:var(--tx);border-color:#3a4050}}
table{{width:100%;border-collapse:collapse;font-size:13px}}
th,td{{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line)}}
th{{color:var(--dim);font-weight:600;font-size:11px;text-transform:uppercase;letter-spacing:.06em}}
td.n{{text-align:right;font-variant-numeric:tabular-nums}}
tr.own td{{background:#1a1d16}}
a{{color:#7aa2f7}}
.astro li{{color:var(--dim);font-size:13px;margin-bottom:6px}}
details summary{{cursor:pointer;color:var(--dim);margin-bottom:12px}}
.foot{{color:var(--dim);font-size:12px;border-top:1px solid var(--line);padding-top:16px}}
</style></head><body><div class="wrap">
<h1>Comment Mining</h1>
<p class="sub">{date.today().isoformat()} · {len(stats)} videos · {total_c} comments read · {len(signals)} signals kept</p>
{f'<div class="headline">{esc(clusters.get("headline"))}</div>' if clusters.get("headline") else ""}
{rq_html}
{''.join(cl_html)}
{rest_html}
{astro_html}
<section><h2>Scope</h2><table>
<tr><th>Channel</th><th>Video</th><th>Views</th><th>Comments</th><th>Signals</th></tr>
{rows}</table></section>
<p class="foot">Filtered out — {esc(drop_line)}. Scraped with yt-dlp; no API key, no browser.</p>
</div>
<script>
function cp(b){{
  const t=b.dataset.copy||'';
  const done=()=>{{const o=b.textContent;b.textContent='\u2713 copied';setTimeout(()=>b.textContent=o,1200)}};
  const fallback=()=>{{const a=document.createElement('textarea');a.value=t;a.style.position='fixed';a.style.opacity=0;
    document.body.appendChild(a);a.select();try{{document.execCommand('copy');done()}}catch(e){{window.prompt('Copy:',t)}}
    document.body.removeChild(a)}};
  if(navigator.clipboard&&window.isSecureContext){{navigator.clipboard.writeText(t).then(done).catch(fallback)}}else{{fallback()}}
}}
</script></body></html>"""

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w") as f:
        f.write(doc)
    print(out_path)
    missing = [i for i in clusters.get("reply_queue", []) if i not in by_id]
    for c in clusters.get("clusters", []):
        missing += [i for i in c.get("signal_ids", []) if i not in by_id]
    if missing:
        print(f"!! {len(missing)} signal id(s) in clusters.json not found in signals.json", file=sys.stderr)
    if do_open:
        webbrowser.open(f"file://{os.path.abspath(out_path)}")


if __name__ == "__main__":
    main()
