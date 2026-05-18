#!/usr/bin/env python3
import argparse
import json
import math
import re
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[4]
OUT_ROOT = ROOT / "carousel" / "outputs"

PALETTES = {
    "signal": {
        "bg": "#0F1115",
        "panel": "#F3F0E8",
        "ink": "#F4F0E8",
        "panel_ink": "#111318",
        "muted": "#A8ADB8",
        "accent": "#FFD34D",
        "accent2": "#55D6BE",
        "danger": "#FF6B5A",
    },
    "editorial": {
        "bg": "#F2EFE6",
        "panel": "#111318",
        "ink": "#111318",
        "panel_ink": "#F8F4EA",
        "muted": "#66645E",
        "accent": "#EF3E36",
        "accent2": "#1D7A8C",
        "danger": "#B3261E",
    },
    "mono": {
        "bg": "#FAFAF7",
        "panel": "#111111",
        "ink": "#111111",
        "panel_ink": "#FFFFFF",
        "muted": "#626262",
        "accent": "#111111",
        "accent2": "#D8FF3E",
        "danger": "#C9362D",
    },
}

FONT_CANDIDATES = [
    "/System/Library/Fonts/Helvetica.ttc",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/Library/Fonts/Arial.ttf",
]


def font(size, bold=False):
    for path in FONT_CANDIDATES:
        p = Path(path)
        if not p.exists():
            continue
        try:
            if p.suffix == ".ttc":
                return ImageFont.truetype(str(p), size=size, index=1 if bold else 0)
            return ImageFont.truetype(str(p), size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def slugify(text):
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return text[:80] or "carousel"


def fmt_size(fmt):
    if fmt == "1:1":
        return 1080, 1080
    return 1080, 1350


def text_box(draw, xy, text, font_obj, fill, max_width, line_gap=10, max_lines=None):
    words = str(text or "").split()
    if not words:
        return xy[1]
    lines = []
    current = []
    for word in words:
        test = " ".join(current + [word])
        if draw.textlength(test, font=font_obj) <= max_width or not current:
            current.append(word)
        else:
            lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip(".") + "..."
    x, y = xy
    for line in lines:
        draw.text((x, y), line, font=font_obj, fill=fill)
        bbox = draw.textbbox((x, y), line, font=font_obj)
        y += bbox[3] - bbox[1] + line_gap
    return y


def fit_font(draw, text, max_width, start_size, min_size, bold=True):
    size = start_size
    while size > min_size:
        f = font(size, bold=bold)
        wrapped = wrap_lines(draw, text, f, max_width)
        if len(wrapped) <= 4:
            return f
        size -= 4
    return font(min_size, bold=bold)


def wrap_lines(draw, text, font_obj, max_width):
    words = str(text or "").split()
    lines, current = [], []
    for word in words:
        test = " ".join(current + [word])
        if draw.textlength(test, font=font_obj) <= max_width or not current:
            current.append(word)
        else:
            lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines


def rounded_rect(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def add_texture(draw, W, H, palette):
    for i in range(0, W, 54):
        color = palette["accent2"] if (i // 54) % 2 == 0 else palette["accent"]
        draw.line((i, H - 170, i + 190, H), fill=color, width=2)


def draw_header(draw, W, palette, label, idx, total):
    small = font(28, bold=True)
    draw.text((70, 56), label.upper(), font=small, fill=palette["muted"])
    draw.text((W - 170, 56), f"{idx:02d}/{total:02d}", font=small, fill=palette["muted"])


def render_cover(draw, slide, W, H, palette, idx, total):
    draw.rectangle((0, 0, W, H), fill=palette["bg"])
    draw.rectangle((0, H - 260, W, H), fill=palette["accent"])
    draw.ellipse((W - 250, 150, W + 220, 620), fill=palette["accent2"])
    draw.rectangle((70, 70, 450, 130), fill=palette["panel"])
    draw.text((92, 86), slide.get("kicker", "CAROUSEL").upper(), font=font(26, True), fill=palette["panel_ink"])
    headline_font = fit_font(draw, slide.get("headline", ""), W - 220, 100, 68, True)
    y = text_box(draw, (70, 250), slide.get("headline", ""), headline_font, palette["ink"], W - 220, 14)
    text_box(draw, (76, y + 38), slide.get("subhead", ""), font(38), palette["muted"], W - 170, 12, max_lines=3)
    draw.text((70, H - 118), f"{idx:02d}/{total:02d}", font=font(38, True), fill=palette["panel_ink"])


def render_point(draw, slide, W, H, palette, idx, total):
    draw.rectangle((0, 0, W, H), fill=palette["bg"])
    draw_header(draw, W, palette, slide.get("eyebrow", "POINT"), idx, total)
    rounded_rect(draw, (70, 160, W - 70, 1170), 26, palette["panel"])
    draw.text((108, 205), str(slide.get("eyebrow", "01")).upper(), font=font(36, True), fill=palette["accent"])
    headline = fit_font(draw, slide.get("headline", ""), W - 220, 74, 52, True)
    y = text_box(draw, (108, 300), slide.get("headline", ""), headline, palette["panel_ink"], W - 220, 12, max_lines=4)
    draw.line((108, y + 36, W - 160, y + 36), fill=palette["accent"], width=7)
    text_box(draw, (108, y + 92), slide.get("body", ""), font(43), palette["panel_ink"], W - 220, 14, max_lines=6)
    add_texture(draw, W, H, palette)


def render_quote(draw, slide, W, H, palette, idx, total):
    draw.rectangle((0, 0, W, H), fill=palette["bg"])
    draw_header(draw, W, palette, "RECEIPT", idx, total)
    draw.text((70, 190), '"', font=font(180, True), fill=palette["accent"])
    text_box(draw, (120, 340), slide.get("quote", ""), font(64, True), palette["ink"], W - 190, 12, max_lines=6)
    if slide.get("attribution"):
        rounded_rect(draw, (120, 1010, W - 120, 1090), 18, palette["panel"])
        draw.text((148, 1032), "- " + slide["attribution"], font=font(30, True), fill=palette["panel_ink"])


def render_compare(draw, slide, W, H, palette, idx, total):
    draw.rectangle((0, 0, W, H), fill=palette["bg"])
    draw_header(draw, W, palette, "COMPARE", idx, total)
    text_box(draw, (70, 150), slide.get("headline", ""), font(66, True), palette["ink"], W - 140, 10, max_lines=3)
    mid = H // 2 + 40
    rounded_rect(draw, (70, 430, W - 70, mid - 30), 24, palette["panel"])
    rounded_rect(draw, (70, mid + 20, W - 70, H - 130), 24, palette["accent"])
    draw.text((110, 470), slide.get("left_label", "OLD WAY").upper(), font=font(30, True), fill=palette["accent"])
    text_box(draw, (110, 540), slide.get("left", ""), font(42, True), palette["panel_ink"], W - 220, 12, max_lines=4)
    draw.text((110, mid + 60), slide.get("right_label", "NEW WAY").upper(), font=font(30, True), fill=palette["bg"])
    text_box(draw, (110, mid + 130), slide.get("right", ""), font(42, True), palette["bg"], W - 220, 12, max_lines=4)


def render_steps(draw, slide, W, H, palette, idx, total):
    draw.rectangle((0, 0, W, H), fill=palette["bg"])
    draw_header(draw, W, palette, "PLAYBOOK", idx, total)
    y = text_box(draw, (70, 150), slide.get("headline", ""), font(66, True), palette["ink"], W - 140, 8, max_lines=3)
    for n, step in enumerate(slide.get("steps", [])[:5], 1):
        y += 32
        rounded_rect(draw, (70, y, 148, y + 78), 39, palette["accent"])
        draw.text((94, y + 17), str(n), font=font(34, True), fill=palette["bg"])
        text_box(draw, (178, y + 4), step, font(38, True), palette["ink"], W - 245, 8, max_lines=2)
        y += 105


def render_stat(draw, slide, W, H, palette, idx, total):
    draw.rectangle((0, 0, W, H), fill=palette["bg"])
    draw_header(draw, W, palette, slide.get("eyebrow", "STAT"), idx, total)
    draw.text((70, 240), slide.get("stat", ""), font=font(138, True), fill=palette["accent"])
    y = text_box(draw, (76, 430), slide.get("headline", ""), font(68, True), palette["ink"], W - 150, 8, max_lines=3)
    rounded_rect(draw, (70, y + 70, W - 70, y + 360), 26, palette["panel"])
    text_box(draw, (110, y + 110), slide.get("body", ""), font(42, True), palette["panel_ink"], W - 220, 12, max_lines=5)


def render_cta(draw, slide, W, H, palette, idx, total):
    draw.rectangle((0, 0, W, H), fill=palette["accent"])
    draw.rectangle((0, 0, W, 130), fill=palette["bg"])
    draw_header(draw, W, {**palette, "muted": palette["panel_ink"]}, "NEXT MOVE", idx, total)
    text_box(draw, (70, 250), slide.get("headline", ""), font(78, True), palette["bg"], W - 140, 12, max_lines=4)
    rounded_rect(draw, (70, 770, W - 70, 1100), 28, palette["bg"])
    text_box(draw, (112, 830), slide.get("body", ""), font(46, True), palette["ink"], W - 225, 14, max_lines=5)
    draw.text((70, H - 110), "@jasoncooperson", font=font(34, True), fill=palette["bg"])


RENDERERS = {
    "cover": render_cover,
    "point": render_point,
    "quote": render_quote,
    "compare": render_compare,
    "steps": render_steps,
    "stat": render_stat,
    "cta": render_cta,
}


def render_slide(slide, W, H, palette, idx, total):
    img = Image.new("RGB", (W, H), palette["bg"])
    draw = ImageDraw.Draw(img)
    renderer = RENDERERS.get(slide.get("type", "point"), render_point)
    renderer(draw, slide, W, H, palette, idx, total)
    return img


def make_contact_sheet(paths, out_path):
    thumbs = [Image.open(p).resize((216, 270)) for p in paths]
    cols = 5
    rows = math.ceil(len(thumbs) / cols)
    sheet = Image.new("RGB", (cols * 216, rows * 270), "#FFFFFF")
    for i, thumb in enumerate(thumbs):
        sheet.paste(thumb, ((i % cols) * 216, (i // cols) * 270))
    sheet.save(out_path)


def write_caption(manifest, out_dir):
    caption = manifest.get("caption", {})
    lines = []
    for key in ("hook", "body", "cta"):
        if caption.get(key):
            lines.append(caption[key].strip())
            lines.append("")
    lines.append("Sources:")
    for src in manifest.get("sources", []):
        title = src.get("title", "Source")
        url = src.get("url", "")
        date = src.get("date", "")
        note = src.get("note", "")
        lines.append(f"- {title} ({date}) {url} - {note}".strip())
    lines.append("")
    lines.append("Alt text:")
    lines.append(caption.get("alt_text", f"Instagram carousel about {manifest.get('topic', 'a creator economy topic')}."))
    lines.append("")
    lines.append("Posting notes:")
    lines.append(caption.get("posting_notes", "Post as 4:5 carousel. Use slide 1 as cover."))
    (out_dir / "caption.md").write_text("\n".join(lines).strip() + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest")
    args = parser.parse_args()

    manifest_path = Path(args.manifest)
    manifest = json.loads(manifest_path.read_text())
    slug = manifest.get("slug") or slugify(manifest.get("topic", "carousel"))
    W, H = fmt_size(manifest.get("format", "4:5"))
    palette = PALETTES.get(manifest.get("theme", "signal"), PALETTES["signal"])
    slides = manifest.get("slides", [])
    if not slides:
        raise SystemExit("Manifest has no slides")

    out_dir = OUT_ROOT / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for idx, slide in enumerate(slides, 1):
        img = render_slide(slide, W, H, palette, idx, len(slides))
        out = out_dir / f"slide-{idx:02d}.png"
        img.save(out)
        paths.append(out)
    make_contact_sheet(paths, out_dir / "contact-sheet.png")
    write_caption(manifest, out_dir)
    print(f"[carousel] wrote {len(paths)} slides to {out_dir}")


if __name__ == "__main__":
    main()
