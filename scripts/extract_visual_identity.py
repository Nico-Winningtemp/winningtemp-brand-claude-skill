#!/usr/bin/env python3
"""
Extract Winningtemp brand assets from Visual identity.pptx.

Pulls theme colors, fonts, and embedded media (logos, icons, images) out of the
PowerPoint file (which is a ZIP under the hood) and into the skill's assets/
directory. Also dumps a structured summary the markdown reference files draw from.

Re-run this whenever the SharePoint version of Visual identity.pptx is updated:

    python3 scripts/extract_visual_identity.py /path/to/Visual\\ identity.pptx
"""

import json
import re
import shutil
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
ASSETS_DIR = SKILL_DIR / "assets"
LOGOS_DIR = ASSETS_DIR / "logos" / "extracted-from-pptx"   # never write into the curated logos/ root
TEMPLATES_DIR = ASSETS_DIR / "templates"
EXTRACT_DIR = SKILL_DIR / ".extracted"


def extract_pptx(pptx_path: Path) -> Path:
    if EXTRACT_DIR.exists():
        shutil.rmtree(EXTRACT_DIR)
    EXTRACT_DIR.mkdir(parents=True)
    with zipfile.ZipFile(pptx_path) as z:
        z.extractall(EXTRACT_DIR)
    return EXTRACT_DIR


def parse_theme(extract_root: Path) -> dict:
    theme_files = sorted(extract_root.glob("ppt/theme/theme*.xml"))
    if not theme_files:
        return {"colors": {}, "fonts": {}}
    tree = ET.parse(theme_files[0])
    root = tree.getroot()

    colors: dict[str, str] = {}
    clr_scheme = root.find(".//a:clrScheme", NS)
    if clr_scheme is not None:
        for child in clr_scheme:
            tag = child.tag.split("}", 1)[1]
            srgb = child.find("a:srgbClr", NS)
            sys_clr = child.find("a:sysClr", NS)
            if srgb is not None:
                colors[tag] = "#" + srgb.attrib["val"].upper()
            elif sys_clr is not None:
                last = sys_clr.attrib.get("lastClr")
                if last:
                    colors[tag] = "#" + last.upper()

    fonts: dict[str, dict] = {"major": {}, "minor": {}}
    font_scheme = root.find(".//a:fontScheme", NS)
    if font_scheme is not None:
        for kind in ("major", "minor"):
            node = font_scheme.find(f"a:{kind}Font", NS)
            if node is not None:
                latin = node.find("a:latin", NS)
                if latin is not None:
                    fonts[kind]["latin"] = latin.attrib.get("typeface", "")
                ea = node.find("a:ea", NS)
                if ea is not None:
                    fonts[kind]["ea"] = ea.attrib.get("typeface", "")
                cs = node.find("a:cs", NS)
                if cs is not None:
                    fonts[kind]["cs"] = cs.attrib.get("typeface", "")

    return {"colors": colors, "fonts": fonts}


def collect_media(extract_root: Path) -> list[dict]:
    media_dir = extract_root / "ppt" / "media"
    if not media_dir.exists():
        return []

    LOGOS_DIR.mkdir(parents=True, exist_ok=True)
    items = []
    for src in sorted(media_dir.iterdir()):
        if not src.is_file():
            continue
        size = src.stat().st_size
        ext = src.suffix.lower()
        items.append({"name": src.name, "size_bytes": size, "ext": ext, "path": str(src)})
    return items


def copy_likely_logos(media_items: list[dict]) -> list[dict]:
    """Copy SVG/EMF/transparent-PNG candidates that read like logos to assets/logos/."""
    LOGOS_DIR.mkdir(parents=True, exist_ok=True)
    copied = []
    for item in media_items:
        ext = item["ext"]
        if ext in {".svg", ".emf", ".wmf"}:
            dest = LOGOS_DIR / item["name"]
            shutil.copy2(item["path"], dest)
            copied.append({"name": item["name"], "ext": ext, "size_bytes": item["size_bytes"]})
        elif ext in {".png"} and item["size_bytes"] < 200_000:
            dest = LOGOS_DIR / item["name"]
            shutil.copy2(item["path"], dest)
            copied.append({"name": item["name"], "ext": ext, "size_bytes": item["size_bytes"]})
    return copied


def collect_slide_text(extract_root: Path) -> list[dict]:
    slides_dir = extract_root / "ppt" / "slides"
    if not slides_dir.exists():
        return []
    out = []
    for slide_path in sorted(slides_dir.glob("slide*.xml"), key=lambda p: int(re.search(r"\d+", p.stem).group())):
        try:
            tree = ET.parse(slide_path)
        except ET.ParseError:
            continue
        texts = [t.text for t in tree.iter("{http://schemas.openxmlformats.org/drawingml/2006/main}t") if t.text]
        out.append({
            "slide": slide_path.name,
            "text_blocks": texts,
        })
    return out


def main():
    if len(sys.argv) < 2:
        default = Path("/Users/nicholasmuradov/Documents/Winningtemp-hubspot/Visual identity.pptx")
        if default.exists():
            pptx_path = default
            print(f"No path provided; defaulting to: {pptx_path}")
        else:
            sys.exit("Usage: extract_visual_identity.py <path-to-Visual-identity.pptx>")
    else:
        pptx_path = Path(sys.argv[1]).expanduser()

    if not pptx_path.exists():
        sys.exit(f"PPTX not found: {pptx_path}")

    print(f"Extracting {pptx_path.name} ({pptx_path.stat().st_size / 1024 / 1024:.1f} MB)...")
    extract_root = extract_pptx(pptx_path)

    print("Parsing theme (colors, fonts)...")
    theme = parse_theme(extract_root)

    print("Collecting media...")
    media = collect_media(extract_root)
    logos = copy_likely_logos(media)

    print("Collecting slide text (sample)...")
    slides = collect_slide_text(extract_root)

    summary = {
        "source": str(pptx_path),
        "theme_colors": theme["colors"],
        "theme_fonts": theme["fonts"],
        "media_count": len(media),
        "media_extensions": sorted({m["ext"] for m in media}),
        "logos_copied": logos,
        "slide_count": len(slides),
        "slide_text_sample": slides[:80],
    }

    summary_path = SKILL_DIR / ".extracted" / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
    print(f"\n✓ Summary written to {summary_path}")
    print(f"✓ {len(logos)} logo candidates copied to {LOGOS_DIR}")
    print(f"\nTheme colors:")
    for name, hex_val in theme["colors"].items():
        print(f"  {name:10s} = {hex_val}")
    print(f"\nTheme fonts:")
    for kind, info in theme["fonts"].items():
        print(f"  {kind:6s} = {info}")
    print(f"\nMedia extensions found: {summary['media_extensions']}")
    print(f"Total media items: {summary['media_count']}")
    print(f"Total slides: {summary['slide_count']}")


if __name__ == "__main__":
    main()
