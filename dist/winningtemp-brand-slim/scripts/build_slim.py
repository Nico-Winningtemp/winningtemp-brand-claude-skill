#!/usr/bin/env python3
"""
Build a slim version of the winningtemp-brand skill suitable for Claude.ai upload.

Strips out:
  - assets/Visual-identity-source.pptx (~46 MB master, available on SharePoint)
  - assets/fonts/ (~14 MB — both Poppins & Inter are on Google Fonts)
  - All .eps logo files (~25 MB — print-only formats)
  - .extracted/ (intermediate output of the extractor)

Keeps:
  - SKILL.md, references/ (the brain)
  - All scripts/ (Python helpers)
  - assets/color-palette.json, typography.json (machine-readable specs)
  - assets/logos/standard/ + variations/ PNG files (digital use)
  - assets/icons/ (full official set)
  - assets/values/ (value cards — both PDFs and PNGs)
  - assets/templates/ (PPTX, Word, email signature)

Outputs:
  dist/winningtemp-brand-slim/        (unzipped)
  dist/winningtemp-brand-slim.zip     (ready for Claude.ai upload)
"""

from __future__ import annotations

import argparse
import shutil
import sys
import urllib.parse
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
SLIM = DIST / "winningtemp-brand-slim"
ZIP_OUT = DIST / "winningtemp-brand-slim.zip"

# Default GitHub raw URL base for the public repo. Override with --github-base.
DEFAULT_GITHUB_BASE = "https://raw.githubusercontent.com/winningtemp/winningtemp-brand-claude-skill/main"

# Paths to copy verbatim
COPY_DIRS = ["references", "scripts"]
COPY_FILES = ["SKILL.md"]

# Asset paths to keep (relative to assets/)
KEEP_ASSET_FILES = [
    "color-palette.json",
    "typography.json",
]
KEEP_ASSET_DIRS_PNG_ONLY = [
    Path("logos") / "standard",
    Path("logos") / "variations",
]
KEEP_ASSET_DIRS = [
    Path("icons"),
    Path("values"),
    Path("templates"),
]


def copy_tree(src: Path, dst: Path):
    if not src.exists():
        return
    shutil.copytree(src, dst, dirs_exist_ok=True)


def copy_dir_filter(src: Path, dst: Path, allowed_suffixes: set[str]):
    """Mirror src → dst, copying only files whose suffix is in allowed_suffixes."""
    if not src.exists():
        return
    for item in src.rglob("*"):
        if item.is_file() and item.suffix.lower() in allowed_suffixes:
            rel = item.relative_to(src)
            target = dst / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, target)


def patch_skill_md_for_slim(slim_skill_md: Path):
    """Add a SLIM-NOTE banner at the top of SKILL.md so users know what's missing."""
    content = slim_skill_md.read_text()
    banner = """\

> **SLIM VARIANT.** This is the Claude.ai-upload version of the skill. The following are NOT bundled here (download from SharePoint or from the full repo at `winningtemp-brand-claude-skill` if you need them):
> - `assets/Visual-identity-source.pptx` — 46 MB master document (SharePoint URL in `references/external-resources.md`)
> - `assets/fonts/` — Poppins + Inter font binaries (free on Google Fonts; see `references/typography.md`)
> - `assets/logos/**/*.eps` — print-ready CMYK/PMS/EPS files (request from brand team for print runs)
>
> Everything you need for digital, slide, doc, ad, copy, and web work is included.
"""
    # Insert after the closing --- of frontmatter
    parts = content.split("---", 2)
    if len(parts) >= 3:
        new_content = "---" + parts[1] + "---" + banner + parts[2]
    else:
        new_content = banner + content
    slim_skill_md.write_text(new_content)


def add_slim_fonts_readme(slim_root: Path):
    """The slim version omits assets/fonts/, but keep a small README pointing to Google Fonts."""
    fonts_dir = slim_root / "assets" / "fonts"
    fonts_dir.mkdir(parents=True, exist_ok=True)
    (fonts_dir / "README.md").write_text(
        "# Fonts (slim variant)\n\n"
        "Font binaries are not bundled in the slim skill (they're ~14 MB and free on Google Fonts).\n\n"
        "- **Poppins** — https://fonts.google.com/specimen/Poppins\n"
        "- **Inter**   — https://fonts.google.com/specimen/Inter\n\n"
        "Install them on your machine, or use the web `<link>` from `references/typography.md` for "
        "browser-based work. The full skill repo includes the .ttf/.otf binaries if you need them "
        "for offline / print work.\n"
    )


def write_heavy_assets_reference(slim_root: Path, github_base: str):
    """Generate references/heavy-assets.md listing GitHub raw URLs for files not in the slim bundle."""
    heavy_paths = []

    # Heavy assets in the FULL repo (paths relative to repo root)
    full_eps_logos = sorted((ROOT / "assets" / "logos" / "variations").rglob("*.eps"))
    full_fonts_poppins = sorted((ROOT / "assets" / "fonts" / "Poppins").glob("*.ttf"))
    full_fonts_inter = sorted((ROOT / "assets" / "fonts" / "Inter").glob("*.otf"))
    poppins_license = ROOT / "assets" / "fonts" / "Poppins" / "OFL.txt"

    for f in full_eps_logos:
        heavy_paths.append(("Print logo (EPS)", f.relative_to(ROOT)))
    for f in full_fonts_poppins:
        heavy_paths.append(("Poppins font", f.relative_to(ROOT)))
    for f in full_fonts_inter:
        heavy_paths.append(("Inter font", f.relative_to(ROOT)))
    if poppins_license.exists():
        heavy_paths.append(("Poppins OFL license", poppins_license.relative_to(ROOT)))

    def to_url(rel: Path) -> str:
        encoded = "/".join(urllib.parse.quote(p) for p in rel.parts)
        return f"{github_base}/{encoded}"

    lines = [
        "# Heavy Assets (Hosted Externally)\n\n",
        "The slim variant of this skill omits ~40 MB of binary assets that aren't useful to ",
        "Claude.ai's text/code context (print-only EPS files and bundled font binaries). They ",
        "remain available via the public GitHub repo's raw URLs — Claude can fetch them with ",
        "WebFetch when needed, or return the URL for the human to download.\n\n",
        "**Public repo:** the URLs below resolve only if the repo has been made public.\n\n",
        "## Visual identity master document\n\n",
        "The 46 MB `Visual identity.pptx` source is **NOT hosted publicly**. ",
        "See `references/external-resources.md` for the SharePoint URL.\n\n",
        "## Print-ready logo files (EPS)\n\n",
        "EPS files in CMYK / PMS / RGB color models for designers and print vendors:\n\n",
    ]
    for label, rel in heavy_paths:
        if rel.suffix.lower() == ".eps":
            lines.append(f"- [{rel.name}]({to_url(rel)})\n")

    lines.extend([
        "\n## Fonts (Poppins + Inter binaries)\n\n",
        "Both fonts are SIL Open Font License — bundled here for convenience. ",
        "For most uses, prefer the Google Fonts CSS link in `references/typography.md` instead.\n\n",
        "### Poppins\n\n",
    ])
    for label, rel in heavy_paths:
        if "Poppins" in str(rel) and rel.suffix.lower() == ".ttf":
            lines.append(f"- [{rel.name}]({to_url(rel)})\n")
    lines.extend([
        "\n[OFL license (Poppins)](" + to_url(poppins_license.relative_to(ROOT)) + ")\n",
        "\n### Inter\n\n",
    ])
    for label, rel in heavy_paths:
        if "Inter" in str(rel) and rel.suffix.lower() == ".otf":
            lines.append(f"- [{rel.name}]({to_url(rel)})\n")
    lines.extend([
        "\n---\n\n",
        f"_URLs generated against: `{github_base}`. Update via `python3 scripts/build_slim.py --github-base <url>` if the repo moves._\n",
    ])

    refs_dir = slim_root / "references"
    refs_dir.mkdir(parents=True, exist_ok=True)
    (refs_dir / "heavy-assets.md").write_text("".join(lines))


def make_zip(src_dir: Path, zip_path: Path):
    """Zip src_dir's *contents* (not the wrapping folder) so SKILL.md ends up at the zip root —
    which is what Claude.ai expects."""
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for item in src_dir.rglob("*"):
            if item.is_file():
                z.write(item, arcname=item.relative_to(src_dir))


def human_size(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--github-base", default=DEFAULT_GITHUB_BASE,
                        help=f"GitHub raw URL base for heavy-assets.md generation (default: {DEFAULT_GITHUB_BASE})")
    global args
    args = parser.parse_args()

    if SLIM.exists():
        shutil.rmtree(SLIM)
    SLIM.mkdir(parents=True, exist_ok=True)

    print(f"Building slim skill in {SLIM}...")

    # 1. SKILL.md
    for fname in COPY_FILES:
        shutil.copy2(ROOT / fname, SLIM / fname)
    print(f"  ✓ Copied SKILL.md")

    # 2. Top-level dirs (references, scripts)
    for d in COPY_DIRS:
        copy_tree(ROOT / d, SLIM / d)
        n_files = sum(1 for _ in (SLIM / d).rglob("*") if _.is_file())
        print(f"  ✓ Copied {d}/ ({n_files} files)")

    # 3. Selected asset files
    slim_assets = SLIM / "assets"
    slim_assets.mkdir(parents=True, exist_ok=True)
    for f in KEEP_ASSET_FILES:
        src = ROOT / "assets" / f
        if src.exists():
            shutil.copy2(src, slim_assets / f)
    print(f"  ✓ Copied {len(KEEP_ASSET_FILES)} asset spec files")

    # 4. Selected asset dirs (full)
    for rel in KEEP_ASSET_DIRS:
        copy_tree(ROOT / "assets" / rel, slim_assets / rel)
        n_files = sum(1 for _ in (slim_assets / rel).rglob("*") if _.is_file())
        print(f"  ✓ Copied assets/{rel}/ ({n_files} files)")

    # 5. Logos: PNG-only filter
    for rel in KEEP_ASSET_DIRS_PNG_ONLY:
        copy_dir_filter(ROOT / "assets" / rel, slim_assets / rel,
                        allowed_suffixes={".png", ".svg"})
        n_files = sum(1 for _ in (slim_assets / rel).rglob("*") if _.is_file())
        print(f"  ✓ Copied assets/{rel}/ — PNG/SVG only ({n_files} files)")

    # 6. Fonts placeholder README
    add_slim_fonts_readme(SLIM)
    print(f"  ✓ Added assets/fonts/README.md (links to Google Fonts)")

    # 7. Heavy-assets reference (GitHub raw URLs for files not bundled in slim)
    write_heavy_assets_reference(SLIM, args.github_base)
    print(f"  ✓ Added references/heavy-assets.md (GitHub URLs base: {args.github_base})")

    # 8. Patch SKILL.md with slim banner
    patch_skill_md_for_slim(SLIM / "SKILL.md")
    print(f"  ✓ Added SLIM banner to SKILL.md")

    # 9. Zip it
    make_zip(SLIM, ZIP_OUT)
    slim_size = sum(f.stat().st_size for f in SLIM.rglob("*") if f.is_file())
    zip_size = ZIP_OUT.stat().st_size
    print()
    print(f"✓ Slim skill built")
    print(f"  Unzipped: {SLIM}  ({human_size(slim_size)})")
    print(f"  Zipped:   {ZIP_OUT}  ({human_size(zip_size)})")
    print()
    print(f"Upload {ZIP_OUT.name} to Claude.ai → Settings → Capabilities → Skills.")


if __name__ == "__main__":
    main()
