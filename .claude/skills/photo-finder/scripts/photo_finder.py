#!/usr/bin/env python3
"""
photo_finder.py — find the best lifestyle photos of one person in the macOS Photos library,
without Claude looking at photos one by one.

  find    osxphotos filter (person, stills, no screenshots/selfies/hidden, burst key frames)
          -> SigLIP embedding of each photo's local preview (cached by uuid)
          -> composite of Apple's own overall score + Aesthetic Predictor v2.5 + vibe
          -> near-duplicate collapse -> numbered 5x5 contact sheets of the top N
  export  full-res originals for the ranks Claude picked (iCloud download if needed),
          added to a Photos album, verified on disk

The Photos library is read through osxphotos only, read-only. Never touch Photos.sqlite.

Writes:  photos/cache/embeddings.npz              uuid -> normalized SigLIP embedding (reused every run)
         photos/runs/<stamp>/ranked.json           every candidate, ranked, with all scores
         photos/runs/<stamp>/sheets/sheet_NN.jpg   numbered contact sheets of the top N
         photos/runs/<stamp>/export/               originals, after `export`
"""
import argparse, datetime as dt, json, os, shutil, subprocess, sys
from pathlib import Path

import numpy as np

ROOT = Path(os.environ.get("CONTENT_OS_ROOT", Path(__file__).resolve().parents[4]))
OUT = ROOT / "photos"
CACHE = OUT / "cache" / "embeddings.npz"
SIGLIP = "google/siglip-so400m-patch14-384"
HEAD_URL = "https://github.com/discus0434/aesthetic-predictor-v2-5/raw/main/models/aesthetic_predictor_v2_5.pth"

# Vibe = mean similarity to LOOK minus mean similarity to NOT_LOOK. --look / --refs override LOOK.
LOOK = [
    "a high-end lifestyle photo of a well-dressed man",
    "a candid editorial photo of a stylish man in a beautiful city",
    "a man at an upscale restaurant or rooftop bar",
    "golden hour travel photography of a man",
    "a man in a luxury hotel, villa, or yacht",
    "a confident man photographed by a professional photographer",
]
NOT_LOOK = [
    "a blurry low quality snapshot",
    "a messy room",
    "a photo of a screen, document, or receipt",
    "a crowded group photo at a party",
    "an awkward unflattering photo of a man",
    "a dark grainy photo taken at night",
]
# Photos tags faces in saved graphics too (PFPs, YT thumbnails, AI generations, video stills).
# An image with no camera EXIF is dropped when it reads as a graphic more than a photo.
PHOTO = [
    "a candid photograph of a man taken with a phone camera",
    "a photo of a man outdoors",
    "a photo of a man at an event",
]
GRAPHIC = [
    "a profile picture headshot on a plain colored background",
    "a YouTube thumbnail with bold text and graphics",
    "a digital collage or graphic design",
    "a screenshot of a video call or editing software",
    "an AI generated image",
    "a still frame from a video of a man talking to the camera",
    "an Instagram post graphic with a text overlay",
]
WEIGHTS = {"apple": 0.25, "aesthetic": 0.35, "vibe": 0.40}
DUP_COS = 0.94  # embedding cosine above this = same moment; keep the higher-ranked one


def candidates(person, selfies, since):
    import osxphotos
    db = osxphotos.PhotosDB()
    if not person:  # default: whoever the library has the most photos of
        named = [p for p in db.person_info if p.name and p.name != "_UNKNOWN_"]
        if not named:
            sys.exit("No named people in Photos. Name yourself once in Photos > People, then rerun.")
        person = max(named, key=lambda p: len(p.photos)).name
    print(f"[find] person: {person}", file=sys.stderr)
    out = []
    for p in db.photos(persons=[person]):
        if p.ismovie or p.screenshot or p.hidden or p.intrash or not p.path_derivatives:
            continue
        if p.burst and not (p.burst_key or p.burst_selected):
            continue
        if p.selfie and not selfies:
            continue
        if since and p.date.date() < since:
            continue
        si = p.search_info
        out.append({
            "uuid": p.uuid, "date": p.date.isoformat(), "filename": p.original_filename,
            "preview": p.path_derivatives[0], "apple": p.score.overall if p.score else 0.0,
            "selfie": p.selfie, "camera": bool(p.exif_info and p.exif_info.camera_make), "labels": si.labels if si else [], "venues": si.venues if si else [],
            "city": si.city if si else "", "captured_by_me": bool(si and si.captured_by_me),
        })
    return person, out


def load_model():
    import torch
    from transformers import AutoProcessor, SiglipModel
    from aesthetic_predictor_v2_5 import AestheticPredictorV2_5Head
    dev = "mps" if torch.backends.mps.is_available() else "cpu"
    model = SiglipModel.from_pretrained(SIGLIP, torch_dtype=torch.float16 if dev == "mps" else torch.float32).to(dev).eval()
    proc = AutoProcessor.from_pretrained(SIGLIP)
    head = AestheticPredictorV2_5Head(model.config.vision_config)
    head.load_state_dict(torch.hub.load_state_dict_from_url(HEAD_URL, map_location="cpu"))
    return model, proc, head.eval(), dev


def embed(paths, model, proc, dev, batch=16):
    import torch
    from PIL import Image, ImageOps
    vecs = []
    for i in range(0, len(paths), batch):
        ims = [ImageOps.exif_transpose(Image.open(p)).convert("RGB") for p in paths[i:i + batch]]
        px = proc(images=ims, return_tensors="pt")["pixel_values"].to(dev, model.dtype)
        with torch.no_grad():
            v = model.vision_model(pixel_values=px).pooler_output.float()
        vecs.append(torch.nn.functional.normalize(v, dim=-1).cpu().numpy())
        print(f"[find] embedded {min(i + batch, len(paths))}/{len(paths)}", file=sys.stderr)
    return np.concatenate(vecs).astype(np.float16)


def text_vecs(texts, model, proc, dev):
    import torch
    t = proc(text=texts, padding="max_length", return_tensors="pt").to(dev)
    with torch.no_grad():
        out = model.get_text_features(**t)
    out = (out if torch.is_tensor(out) else out.pooler_output).float()
    return torch.nn.functional.normalize(out, dim=-1).cpu().numpy()


def z(x):
    x = np.asarray(x, dtype=np.float64)
    return (x - x.mean()) / (x.std() or 1.0)


def contact_sheets(rows, dest, tile=256, grid=5):
    from PIL import Image, ImageDraw, ImageFont, ImageOps
    dest.mkdir(parents=True, exist_ok=True)
    font = ImageFont.load_default(size=30)
    per = grid * grid
    for s in range(0, len(rows), per):
        sheet = Image.new("RGB", (tile * grid, tile * grid), (20, 20, 20))
        draw = ImageDraw.Draw(sheet)
        for k, r in enumerate(rows[s:s + per]):
            im = ImageOps.exif_transpose(Image.open(r["preview"])).convert("RGB")
            im.thumbnail((tile - 6, tile - 6))
            x, y = (k % grid) * tile, (k // grid) * tile
            sheet.paste(im, (x + (tile - im.width) // 2, y + (tile - im.height) // 2))
            label = str(r["rank"])
            box = draw.textbbox((x + 6, y + 4), label, font=font)
            draw.rectangle((box[0] - 4, box[1] - 2, box[2] + 4, box[3] + 4), fill=(255, 214, 0))
            draw.text((x + 6, y + 4), label, fill=(0, 0, 0), font=font)
        sheet.save(dest / f"sheet_{s // per + 1:02d}.jpg", quality=88)


def cmd_find(a):
    since = dt.date.fromisoformat(a.since) if a.since else None
    person, rows = candidates(a.person, a.selfies, since)
    print(f"[find] {len(rows)} candidate stills", file=sys.stderr)
    if not rows:
        sys.exit("No candidates.")

    cache = dict(np.load(CACHE)) if CACHE.exists() else {}
    todo = [r for r in rows if r["uuid"] not in cache]
    model, proc, head, dev = load_model()
    if todo:
        print(f"[find] embedding {len(todo)} new photos ({len(rows) - len(todo)} cached) on {dev}", file=sys.stderr)
        for r, v in zip(todo, embed([r["preview"] for r in todo], model, proc, dev)):
            cache[r["uuid"]] = v
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        np.savez(CACHE, **cache)

    import torch
    E = np.stack([cache[r["uuid"]] for r in rows]).astype(np.float32)
    graphic = ((E @ text_vecs(GRAPHIC, model, proc, dev).T).max(1)
               > (E @ text_vecs(PHOTO, model, proc, dev).T).max(1) - 0.02)  # margin: PFPs score a near-tie
    keep = [i for i, r in enumerate(rows) if r["camera"] or not graphic[i]]
    print(f"[find] dropped {len(rows) - len(keep)} graphics (PFPs, thumbnails, stills)", file=sys.stderr)
    rows, E = [rows[i] for i in keep], E[keep]
    with torch.no_grad():
        aesthetic = head(torch.from_numpy(E)).squeeze(-1).numpy()
    if a.refs:
        refs = sorted(p for p in Path(a.refs).iterdir() if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"})
        pos = embed([str(p) for p in refs], model, proc, dev).astype(np.float32)
        pos = pos.mean(0, keepdims=True)
        pos /= np.linalg.norm(pos)
    else:
        pos = text_vecs(a.look or LOOK, model, proc, dev)
    neg = text_vecs(NOT_LOOK, model, proc, dev)
    vibe = (E @ pos.T).mean(1) - (E @ neg.T).mean(1)

    comp = (WEIGHTS["apple"] * z([r["apple"] for r in rows]) + WEIGHTS["aesthetic"] * z(aesthetic)
            + WEIGHTS["vibe"] * z(vibe))
    for r, ae, vb, c in zip(rows, aesthetic, vibe, comp):
        r.update(aesthetic=round(float(ae), 3), vibe=round(float(vb), 4), composite=round(float(c), 3))
    order = np.argsort(-comp)

    kept, kept_vecs, rank = [], [], 0
    for i in order:
        r = rows[i]
        sims = np.array(kept_vecs) @ E[i] if kept_vecs else np.array([0.0])
        if sims.max() > DUP_COS:
            r["dup_of"] = kept[int(sims.argmax())]["rank"]
            continue
        rank += 1
        r["rank"] = rank
        kept.append(r)
        kept_vecs.append(E[i])
    dups = [rows[i] for i in order if "dup_of" in rows[i]]

    run = OUT / "runs" / dt.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    run.mkdir(parents=True)
    (run / "ranked.json").write_text(json.dumps(
        {"person": person, "weights": WEIGHTS, "look": a.refs or (a.look or LOOK), "ranked": kept, "duplicates": dups},
        indent=1, default=str))
    contact_sheets(kept[:a.top], run / "sheets")
    print(f"[find] {len(kept)} unique ({len(dups)} near-dupes collapsed); top {min(a.top, len(kept))} on "
          f"{-(-min(a.top, len(kept)) // 25)} sheets", file=sys.stderr)
    print(run)


def cmd_export(a):
    run = Path(a.run)
    ranked = {r["rank"]: r for r in json.loads((run / "ranked.json").read_text())["ranked"]}
    ranks = [int(x) for x in a.ranks.replace(" ", "").split(",") if x]
    missing = [k for k in ranks if k not in ranked]
    if missing:
        sys.exit(f"Ranks not in this run: {missing}")
    dest = run / "export"
    dest.mkdir(exist_ok=True)
    osxphotos = Path(sys.executable).parent / "osxphotos"
    cmd = [str(osxphotos), "export", str(dest), "--download-missing", "--skip-original-if-edited", "--skip-live",
           "--convert-to-jpeg", "--jpeg-quality", "0.95", "--filename", "{created.strftime,%Y-%m-%d}_{original_name}",
           "--update"]
    if a.photokit:
        cmd.append("--use-photokit")
    if a.album:
        cmd += ["--add-exported-to-album", a.album, "--add-skipped-to-album", a.album]
    for k in ranks:
        cmd += ["--uuid", ranked[k]["uuid"]]
    # Photos launched by an AppleScript call hangs that call (macOS 27); launched by `open`, it answers.
    if subprocess.run(["pgrep", "-x", "Photos"], capture_output=True).returncode:
        subprocess.run(["open", "-g", "-a", "Photos"], check=True)
        import time; time.sleep(10)
    subprocess.run(cmd, check=True)

    # Verify on disk: every pick exported, at (near) its original size, not a preview.
    import osxphotos
    from PIL import Image
    db = osxphotos.PhotosDB()
    files = sorted(p for p in dest.iterdir() if p.is_file() and not p.name.startswith("."))
    bad = []
    for k in ranks:
        p = db.get_photo(ranked[k]["uuid"])
        hits = [f for f in files if Path(p.original_filename).stem in f.name]
        size = max(Image.open(hits[0]).size) if hits else 0
        if size < 0.9 * max(p.width, p.height):
            bad.append((k, p.original_filename, size, max(p.width, p.height)))
    print(f"[export] {len(files)} files in {dest}; {len(ranks) - len(bad)}/{len(ranks)} verified full-res", file=sys.stderr)
    if bad:
        print(f"[export] MISSING or undersized (rank, file, got, original): {bad}", file=sys.stderr)
    if a.downloads:
        dl = Path.home() / "Downloads" / f"{a.album} {run.name[:10]}"
        shutil.copytree(dest, dl, dirs_exist_ok=True, ignore=shutil.ignore_patterns(".*"))
        print(f"[export] copied to {dl}", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("find")
    f.add_argument("--person", help="Photos > People name (default: the most-photographed named person)")
    f.add_argument("--selfies", action="store_true", help="include front-camera selfies")
    f.add_argument("--since", help="YYYY-MM-DD: only photos taken on/after this date")
    f.add_argument("--top", type=int, default=200, help="how many go on contact sheets")
    f.add_argument("--look", action="append", help="describe the look you want (repeatable, replaces the defaults)")
    f.add_argument("--refs", help="folder of reference images of the look (overrides --look)")
    e = sub.add_parser("export")
    e.add_argument("run", help="photos/runs/<stamp> folder from `find`")
    e.add_argument("ranks", help="comma-separated ranks from the contact sheets")
    e.add_argument("--album", default="Lifestyle picks")
    e.add_argument("--photokit", action="store_true", help="download from iCloud via PhotoKit instead of AppleScript")
    e.add_argument("--downloads", action="store_true", help="also copy the export to ~/Downloads")
    a = ap.parse_args()
    {"find": cmd_find, "export": cmd_export}[a.cmd](a)


if __name__ == "__main__":
    main()
