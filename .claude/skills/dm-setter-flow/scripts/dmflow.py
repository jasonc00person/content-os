#!/usr/bin/env python3
"""DM Setter comment-keyword automations for a short form.

  list                       every comment automation (LIVE / OFF / DRAFT, keyword, post)
  create SPEC.json [--from ID]   duplicate the newest promo as a DRAFT and rewrite it from the spec
  show ID                    read an automation's draft (or live graph) back
  test ID                    a 3-digit code: DM it to the account to run the draft on yourself
  arm ID                     publish on Next Post or Reel, right before the reel goes up

Writes go through DM Setter's own admin routes; graphs are checked with its own src/graph.ts validator.
Reads go through wrangler D1. Every call needs network (Bash with the sandbox off).
"""
import argparse
import base64
import json
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

# The project folder was renamed dm-setter -> fewchat on 2026-11-23 (the Worker and D1 database are still "dm-setter").
PROJECT = next((p for p in (Path.home() / "Projects" / n for n in ("fewchat", "dm-setter")) if p.is_dir()), Path.home() / "Projects" / "fewchat")
URL = "https://fewchat.jason-80a.workers.dev"  # renamed from dm-setter.jason-80a.workers.dev on 2026-11-23; the old host only redirects
DB = "dm-setter"
NEXT_POST = "next"  # DM Setter's Next Post or Reel post id (src/comments.ts NEXT_POST)
SPEC_KEYS = ("keyword", "name", "tag", "card", "links")


def die(msg):
    sys.exit(f"[dmflow] {msg}")


def password():
    for line in (PROJECT / ".env").read_text().splitlines():
        if line.startswith("ADMIN_PASSWORD="):
            return line.split("=", 1)[1].strip()
    die(f"no ADMIN_PASSWORD in {PROJECT}/.env")


def q(v):
    return "NULL" if v is None else "'" + str(v).replace("'", "''") + "'"


def d1(sql):
    r = subprocess.run(["npx", "wrangler", "d1", "execute", DB, "--remote", "--json", "--command", sql],
                       cwd=PROJECT, capture_output=True, text=True)
    if r.returncode:
        die(f"wrangler d1 failed:\n{r.stderr or r.stdout}")
    return [s["results"] for s in json.loads(r.stdout)]


def row(tid):
    rows = d1(f"SELECT id, name, source, keyword, media_id, enabled, published_at, deleted_at, public_reply, draft FROM triggers WHERE id = {int(tid)}")[0]
    if not rows:
        die(f"no automation #{tid}")
    return rows[0]


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def admin(path, body=None):
    """POST to a console route. JSON in, JSON out; a redirect (form-style routes) counts as done."""
    data = json.dumps(body if body is not None else {}).encode()
    req = urllib.request.Request(URL + path, data=data, method="POST", headers={
        "Authorization": "Basic " + base64.b64encode(f"admin:{password()}".encode()).decode(),
        "Content-Type": "application/json", "Accept": "application/json",
        "User-Agent": "dmflow/1 (content-os)"})  # Cloudflare 1010-blocks Python-urllib's default UA
    try:
        with urllib.request.build_opener(_NoRedirect).open(req, timeout=30) as r:
            text = r.read().decode()
    except urllib.error.HTTPError as e:
        if 300 <= e.code < 400:
            loc = e.headers.get("Location") or ""
            if loc.startswith("http") and not loc.startswith(URL):  # the app moved: nothing was written
                die(f"{path} redirected to another host ({loc}); update URL in dmflow.py")
            return {"ok": True}
        text = e.read().decode()
        try:
            out = json.loads(text)
        except ValueError:
            out = None
        if isinstance(out, dict) and "problems" in out:  # publish's validation refusal
            return out
        die(f"{path} -> {e.code}: {text[:300]}")
    return json.loads(text) if text.strip().startswith("{") else {"ok": True}


def checked(graph):
    """The app's own sanitize + validate, so a draft that saves here will also publish."""
    js = ("import { readFileSync } from 'node:fs'; const { sanitize, validate } = await import('./src/graph.ts');"
          "const g = JSON.parse(readFileSync(0, 'utf8')); const s = sanitize(g, g.trigger);"
          "console.log(JSON.stringify({ graph: s, problems: validate(s) }));")
    r = subprocess.run(["node", "--input-type=module", "-e", js], cwd=PROJECT, input=json.dumps(graph),
                       capture_output=True, text=True)
    if r.returncode:
        die(f"validator failed:\n{r.stderr}")
    out = json.loads(r.stdout.strip().splitlines()[-1])
    return out["graph"], out["problems"]


def walk(g):
    """The promo shape: When... -> card (tap button) -> tag action -> links, and nothing after the links."""
    nodes = {n["id"]: n for n in g["nodes"]}

    def nxt(nid, port="next"):
        return next((nodes[e["to"]] for e in g["edges"] if e["from"] == nid and e["port"] == port), None)

    card = nxt("trigger")
    btn = card and next((b for bub in card["data"].get("bubbles", []) for b in bub["buttons"] if "url" not in b), None)
    tag = btn and nxt(card["id"], btn["id"])
    links = tag and nxt(tag["id"])
    shape = [n and n["kind"] for n in (card, tag, links)]
    if shape != ["message", "action", "message"]:
        die(f"template isn't the promo shape (card, tag, links); found {shape}. Pick another with --from.")
    return card, tag, links


def drop_after(g, node):
    """Remove every step that hangs off `node` (an old template's pause + follow-up question). Returns how many went."""
    gone, todo = set(), [e["to"] for e in g["edges"] if e["from"] == node["id"]]
    while todo:
        nid = todo.pop()
        if nid in gone:
            continue
        gone.add(nid)
        todo += [e["to"] for e in g["edges"] if e["from"] == nid]
    g["nodes"] = [n for n in g["nodes"] if n["id"] not in gone]
    g["edges"] = [e for e in g["edges"] if e["from"] not in gone and e["to"] not in gone]
    return len(gone)


def where(media_id):
    return "next Post or Reel" if media_id == NEXT_POST else media_id or "any post"


def text_of(node):
    return "\n\n".join(b["text"] for b in node["data"]["bubbles"])


def report(r):
    g = json.loads(r["draft"]) if r["draft"] else None
    status = "LIVE" if r["enabled"] else "OFF" if r["published_at"] else "DRAFT"
    print(f"#{r['id']} {status}  {r['name']}")
    print(f"  keyword {r['keyword']}  post {where(r['media_id'])}")
    if not g:
        print("  (no unpublished draft: the live graph is what runs)")
        return
    t = g["trigger"]
    print(f"  draft trigger: {t['source']} · keyword {t['keyword']} · post {where(t['media_id'])}")
    card, tag, links = walk(g)
    btn = next(b for b in card["data"]["bubbles"][0]["buttons"] if "url" not in b)
    print(f"\n[card] button \"{btn['title']}\"\n{text_of(card)}")
    print(f"\n[tag] {', '.join(a['value'] for a in tag['data']['actions'] if a['type'] == 'add_tag')}")
    print(f"\n[links]\n{text_of(links)}")
    after = sum(1 for e in g["edges"] if e["from"] == links["id"])
    print("\n[end] the links are the last message" if not after else f"\n[!] {after} step(s) still hang off the links message")
    print(f"\n[public replies] {' | '.join((t['public_reply'] or '').splitlines())}")
    print(f"\neditor: {URL}/admin/flows/{r['id']}")


def cmd_list(_):
    rows = d1("SELECT id, name, keyword, media_id, enabled, published_at FROM triggers "
              "WHERE id > 0 AND deleted_at IS NULL AND source = 'comment' ORDER BY id")[0]
    for r in rows:
        status = "LIVE" if r["enabled"] else "OFF" if r["published_at"] else "DRAFT"
        print(f"#{r['id']:<4} {status:<6} {r['keyword']:<12} {where(r['media_id']):<20} {r['name']}")


def cmd_create(a):
    spec = json.loads(Path(a.spec).read_text())
    missing = [k for k in SPEC_KEYS if not str(spec.get(k, "")).strip()]
    if missing:
        die(f"spec is missing {missing}")
    for k in ("card", "links", "name"):
        if "—" in spec[k]:
            die(f"spec.{k} has an em dash; it ships under Jason's name")
        if "PLACEHOLDER" in spec[k] or "<<" in spec[k]:
            die(f"spec.{k} still has a placeholder")

    if a.src:
        tpl = row(a.src)
    else:
        rows = d1("SELECT id FROM triggers WHERE id > 0 AND deleted_at IS NULL AND source = 'comment' AND enabled = 1 ORDER BY id DESC LIMIT 1")[0]
        if not rows:
            die("no live comment automation to copy")
        tpl = row(rows[0]["id"])
    print(f"[dmflow] copying #{tpl['id']} {tpl['name']}")

    before = d1("SELECT MAX(id) AS m FROM triggers")[0][0]["m"]
    admin(f"/admin/automations/{tpl['id']}/duplicate")
    after = d1("SELECT MAX(id) AS m FROM triggers")[0][0]["m"]
    if after <= before:
        die("duplicate didn't create a new automation")
    new = row(after)
    if new["enabled"] or new["published_at"] or not new["draft"]:
        die(f"#{after} isn't a fresh draft copy; stopping without touching it")

    g = json.loads(new["draft"])
    g["trigger"]["keyword"] = spec["keyword"]
    g["trigger"]["media_id"] = NEXT_POST  # waits from `arm` on; a draft never locks
    if spec.get("public_reply"):
        g["trigger"]["public_reply"] = spec["public_reply"]
    card, tag, links = walk(g)
    drop_after(g, links)  # no follow-up question: the automation ends on the links (Jason, 2026-11-23)
    card["data"]["bubbles"][0]["text"] = spec["card"]
    card["data"]["bubbles"] = card["data"]["bubbles"][:1]
    acts = tag["data"]["actions"]
    tags = [x for x in acts if x["type"] == "add_tag"]
    if tags:
        tags[0]["value"] = spec["tag"]
    else:
        acts.insert(0, {"type": "add_tag", "value": spec["tag"]})
    links["data"] = {"bubbles": [{"text": spec["links"], "buttons": []}], "quick_replies": []}

    clean, problems = checked(g)
    if problems:
        die(f"draft wouldn't publish: {problems}")
    kept = walk(clean)
    for mine, theirs in ((card, kept[0]), (links, kept[2])):
        if text_of(mine) != text_of(theirs):
            die(f"the validator clipped a message (Instagram limits): {text_of(mine)[:60]}...")

    if not admin(f"/admin/flows/{after}/draft", {"graph": clean}).get("ok"):
        die("draft save failed")
    admin(f"/admin/flows/{after}/rename", {"name": spec["name"]})
    # duplicate copied the template's keyword + post onto the row; the list reads them, the runtime ignores a draft
    d1(f"UPDATE triggers SET keyword = {q(spec['keyword'])}, media_id = {q(NEXT_POST)} "
       f"WHERE id = {after} AND enabled = 0 AND published_at IS NULL")

    r = row(after)
    g2 = json.loads(r["draft"])
    c2, t2, l2 = walk(g2)
    if (r["name"], g2["trigger"]["keyword"], g2["trigger"]["media_id"], r["enabled"]) != (spec["name"], spec["keyword"], NEXT_POST, 0) \
            or text_of(c2) != spec["card"] or text_of(l2) != spec["links"] or any(e["from"] == l2["id"] for e in g2["edges"]):
        die(f"read-back doesn't match the spec; check #{after} in the editor")
    print("[dmflow] saved as a DRAFT (not live, sends nothing)\n")
    report(r)


def cmd_show(a):
    report(row(a.id))


def cmd_test(a):
    out = admin(f"/admin/flows/{a.id}/test")
    if not out.get("code"):
        die(f"no test code: {out}")
    print(f"DM {out['code']} to @{out.get('handle') or 'the account'} within 15 minutes, from any account, "
          f"to run #{a.id}'s draft on yourself (the card arrives as a plain DM in a test).")


def cmd_arm(a):
    """Publish on Next Post or Reel: LIVE from now, locks onto the first post or reel published after this."""
    r = row(a.id)
    if r["deleted_at"]:
        die(f"#{a.id} is in Trash")
    if r["enabled"] and not r["draft"]:
        print("[dmflow] already live")
        report(r)
        return
    g = json.loads(r["draft"]) if r["draft"] else None
    if not g:
        die(f"#{a.id} has no draft to publish")
    kw = g["trigger"]["keyword"]

    # Any-post automations answering the same word would DM this reel's commenters twice.
    others = d1("SELECT id, name, keyword FROM triggers WHERE enabled = 1 AND deleted_at IS NULL AND source = 'comment' "
                f"AND id <> {int(a.id)} AND media_id IS NULL")[0]
    mine = {k.strip().lower() for k in kw.split(",")}
    clash = [o for o in others if mine & {k.strip().lower() for k in o["keyword"].split(",")} or o["keyword"].strip() == "*"]
    if clash:
        die("an any-post automation already answers this word: " + ", ".join(f"#{o['id']} {o['name']}" for o in clash))

    g["trigger"]["media_id"] = NEXT_POST
    clean, problems = checked(g)
    if problems:
        die(f"won't publish: {problems}")
    out = admin(f"/admin/flows/{a.id}/publish", {"graph": clean})
    if not out.get("ok"):
        die(f"publish refused: {out}")  # "already waiting for the next post" = another one is armed
    r = row(a.id)
    if not (r["enabled"] and r["media_id"] == NEXT_POST and r["keyword"] == kw and r["published_at"]):
        die(f"publish said ok but the row reads enabled={r['enabled']} post={r['media_id']} keyword={r['keyword']}")
    print("[dmflow] LIVE, waiting for the next post or reel (nothing else may go up on Instagram before this reel)")
    report(r)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list").set_defaults(fn=cmd_list)
    c = sub.add_parser("create")
    c.add_argument("spec")
    c.add_argument("--from", dest="src", type=int)
    c.set_defaults(fn=cmd_create)
    for name, fn in (("show", cmd_show), ("test", cmd_test)):
        s = sub.add_parser(name)
        s.add_argument("id", type=int)
        s.set_defaults(fn=fn)
    arm = sub.add_parser("arm")
    arm.add_argument("id", type=int)
    arm.set_defaults(fn=cmd_arm)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
