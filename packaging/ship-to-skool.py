#!/usr/bin/env python3
"""Ship the built client zip to the Skool classroom lesson and stamp the lesson's UPDATED date.

    ./packaging/package-for-client.sh          # build first
    python3 packaging/ship-to-skool.py         # upload + swap the resource + bump the date + record the version
    python3 packaging/ship-to-skool.py --dry-run

The zip is small (about 1 MB), so it lives on the lesson as a Skool file resource. There's no
download Worker like video-editor's (that zip is over Skool's 100 MB attachment cap). The upload
works the way Skool's own classroom editor does it:
POST /files -> PUT the bytes to the signed writeUrl -> PUT /courses/<lesson> with the new file_id.
The Skool client is imported from ~/Projects/skool (never copied here).
"""
import argparse, datetime, hashlib, json, os, sys, time, urllib.request, zipfile

sys.path.insert(0, os.path.expanduser("~/Projects/skool/scripts"))
import skool_auth  # noqa: E402

GROUP_ID = "60b974683cfe436b88dd33221b5b4173"   # AI Leverage Lab (api2 wants the hex id)
COURSE_ID = "5dbb7476749e4c1a826d8dc74691257e"  # "Content OS" course (GET works on the root only)
LESSON_ID = "ea30cf2281ee47aeb79246ccd3130453"  # lesson "Claude Content OS"
ZIP_NAME = "content-os-client.zip"
HERE = os.path.dirname(os.path.abspath(__file__))
BACKUP_DIR = os.path.expanduser("~/Projects/skool/notes")


def find(node, cid):
    if node["course"]["id"] == cid:
        return node["course"]
    for ch in node.get("children") or []:
        hit = find(ch, cid)
        if hit:
            return hit
    return None


def stamp():
    # Whole hour only: Skool turns any "00:00" in lesson copy into a video-seek link.
    now = datetime.datetime.now()
    hour = now.strftime("%I").lstrip("0") + (" am" if now.hour < 12 else " pm")
    return now.strftime("%a %b ") + str(now.day) + ", " + hour


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("zip", nargs="?", default=os.path.join(HERE, "dist", ZIP_NAME))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if not os.path.isfile(a.zip):
        sys.exit(f"no zip at {a.zip}: run ./packaging/package-for-client.sh first")
    size = os.path.getsize(a.zip)
    with zipfile.ZipFile(a.zip) as z:
        version = z.read("content-os/VERSION").decode().strip()

    s = skool_auth.session()
    tree = s.get(f"/courses/{COURSE_ID}")
    lesson = find(tree, LESSON_ID)
    if not lesson:
        sys.exit(f"lesson {LESSON_ID} not found under course {COURSE_ID}")
    meta = lesson["metadata"]
    resources = json.loads(meta.get("resources") or "[]")
    idx = [i for i, r in enumerate(resources) if r.get("file_name") == ZIP_NAME]
    if len(idx) != 1:
        sys.exit(f"expected exactly one {ZIP_NAME} resource on the lesson, found {len(idx)}: {resources}")

    desc = json.loads(meta["desc"][len("[v2]"):])
    date_node = desc[0]["content"][1] if desc and len(desc[0].get("content", [])) > 1 else None
    if not (desc[0]["content"][0].get("text", "").startswith("UPDATED") and date_node):
        sys.exit("lesson description no longer opens with 'UPDATED: <date>'; fix it by hand first")
    old_date, new_date = date_node["text"], stamp()

    print(f"lesson:   {meta['title']}")
    print(f"zip:      {a.zip} ({size / 1e6:.1f} MB, version {version})")
    print(f"resource: {resources[idx[0]]['title']} (file {resources[idx[0]].get('file_id')})")
    print(f"date:     {old_date} -> {new_date}")
    if a.dry_run:
        print("dry run: nothing uploaded or changed")
        return

    os.makedirs(BACKUP_DIR, exist_ok=True)
    backup = os.path.join(BACKUP_DIR, f"skool-content-os-course-backup-{datetime.date.today()}.json")
    json.dump(tree, open(backup, "w"), indent=1)

    created = s.post("/files", {
        "file_name": ZIP_NAME, "content_type": "application/zip", "content_length": size,
        "content_disposition": f"attachment; filename={ZIP_NAME}", "ref": "",
        "owner_id": GROUP_ID, "privacy": 1, "large_thumbnail": False,
    })
    file_id = created["file"]["id"]
    blob = open(a.zip, "rb").read()
    req = urllib.request.Request(created["write_url"], method="PUT", data=blob,
                                 headers={"content-type": created.get("content_type") or "application/zip",
                                          "x-amz-acl": created.get("acl") or "private"})
    with urllib.request.urlopen(req, timeout=300) as r:
        if r.status >= 300:
            sys.exit(f"S3 upload failed: HTTP {r.status}")

    for _ in range(60):  # Skool post-processes the object after the PUT
        if s.get("/files", ids=file_id)["files"][0]["metadata"].get("postprocessed_at"):
            break
        time.sleep(2)
    else:
        sys.exit(f"file {file_id} never finished processing; lesson NOT changed")
    # Proof the bytes landed: download it back through Skool and compare hashes.
    url = s.post(f"/files/{file_id}/download-url", {})
    url = url.get("url") if isinstance(url, dict) else str(url).strip().strip('"')
    with urllib.request.urlopen(url, timeout=120) as r:
        back = r.read()
    if hashlib.sha256(back).digest() != hashlib.sha256(blob).digest():
        sys.exit(f"downloaded file {file_id} doesn't match the local zip; lesson NOT changed")

    resources[idx[0]]["file_id"] = file_id
    date_node["text"] = new_date
    s.put(f"/courses/{LESSON_ID}", {
        "desc": "[v2]" + json.dumps(desc, ensure_ascii=False, separators=(",", ":")),
        "resources": [{k: r[k] for k in ("title", "file_id", "link") if r.get(k)} for r in resources],
        "update_resources": True,
    })

    after = find(s.get(f"/courses/{COURSE_ID}"), LESSON_ID)["metadata"]
    got = [r for r in json.loads(after.get("resources") or "[]") if r.get("file_name") == ZIP_NAME]
    ok = (len(got) == 1 and got[0].get("file_id") == file_id and new_date in after["desc"]
          and after["title"] == meta["title"] and after.get("video_link") == meta.get("video_link"))
    print(f"backup:   {backup}")
    print(f"uploaded: file {file_id} ({size} bytes)")
    print("verified: resource points at the new file, date bumped, title + video untouched" if ok
          else "VERIFY FAILED: re-read the lesson by hand")
    if ok:  # the version that just shipped joins the update history the next build starts from (update.py)
        with zipfile.ZipFile(a.zip) as z:
            for name in ("shipped-blobs.json", "shipped-history.pack"):
                with open(os.path.join(HERE, name), "wb") as fh:
                    fh.write(z.read("content-os/." + name))
        print(f"recorded: {version} in packaging/shipped-blobs.json + shipped-history.pack")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
