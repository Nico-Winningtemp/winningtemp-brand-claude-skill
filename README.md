# Winningtemp Brand — Claude Skill

A Claude Code / Claude.ai skill that packages Winningtemp's official brand identity — logos, fonts, colors, icons, templates, brand values, voice, and visual identity guidelines — so that any artifact Claude produces (slides, PDFs, ad copy, sales decks, blog drafts, email signatures) comes out on-brand by default.

**Source of truth:** the live `Visual identity.pptx` on Marketing Internal SharePoint. This repo is a snapshot of the *publishable* parts of that document. See [SKILL.md](SKILL.md) and [references/external-resources.md](references/external-resources.md) for the SharePoint URL.

> **What this repo deliberately does NOT contain:** the source `Visual identity.pptx` master file (it may include unreleased campaign material and customer photography). That stays on SharePoint. Designers needing it should download from SharePoint and place it at `assets/Visual-identity-source.pptx` locally — `scripts/extract_visual_identity.py` will then work as documented.

---

## Two flavors

| Flavor | Where | Size | Audience |
|---|---|---|---|
| **Full** | Repo root (`SKILL.md`, `references/`, `assets/`, `scripts/`) | ~95 MB | Engineers / designers using Claude Code locally |
| **Slim** | `dist/winningtemp-brand-slim.zip` | ~10 MB | Anyone uploading to Claude.ai |

The full version includes EPS/PMS print-ready logos, all bundled font binaries, and the original 46 MB Visual identity .pptx. The slim version drops those (pointing to SharePoint instead) so it fits inside Claude.ai's skill upload limits.

---

## Install for Claude Code (developers)

### Option A — User-level (available across all your projects)

```bash
# Clone next to your other repos
git clone <this-repo-url> ~/Documents/winningtemp-brand-claude-skill

# Symlink into your Claude Code skills directory
ln -s ~/Documents/winningtemp-brand-claude-skill ~/.claude/skills/winningtemp-brand
```

Verify it loaded by opening Claude Code and asking *"What are Winningtemp's brand colors?"* — Claude should pick up the skill and answer with `#7F2696` Deep Purple.

### Option B — Project-level (only loads when working in a specific repo)

Inside any project where you want the skill available:

```bash
mkdir -p .claude/skills
git submodule add <this-repo-url> .claude/skills/winningtemp-brand
```

Or copy the folder in if you don't want a submodule.

---

## Install for Claude.ai (everyone in the company, no terminal required)

1. Download `dist/winningtemp-brand-slim.zip` from this repo (use the **Code → Download ZIP** button on a single file in GitHub, or `git clone` the repo and grab it from `dist/`).
2. In Claude.ai, go to your profile → **Settings → Capabilities → Skills** (the path may vary slightly by plan).
3. Click **Upload skill** and select the slim zip.
4. If you're on a Team / Enterprise plan, your admin can publish the skill org-wide so every Winningtemp user sees it automatically.
5. Test by asking Claude *"What are Winningtemp's brand colors?"* in any chat — it should activate and answer specifically.

The slim version omits print-ready EPS files, the 46 MB Visual identity .pptx, and bundled font binaries. Designers needing those should fall back to the full repo or SharePoint.

---

## What the skill provides

- **Colors** — exact hex codes (Deep Purple `#7F2696`, Light Purple, Wave, Gray, etc.) with usage rules
- **Typography** — Poppins (headlines) + Inter (body) with weights, sizes, and hierarchy. Full font binaries included in the full version.
- **Logos** — primary + tagline + symbol-only variants in Deep Purple / White / Black, in RGB/CMYK/PMS/EPS/PNG (full) or RGB PNG only (slim). Includes the App Symbol with explicit "product UI only" warning.
- **Icons** — 97 official PNG icons, brand-styled, with a substitution table for common generic-icon requests
- **Brand values** — the four official values (We are Curious, We get Results Together, We show Passion, We take Responsibility) and how they shape copy and design
- **Templates** — official PowerPoint deck, two Word templates (with/without footer), branded email signature
- **Voice & tone** — what to say and what not to say, in English / Swedish / Norwegian
- **Imagery & graphic-element guidance** — photo style, rounded-rectangle masks, the symbol used as a watermark, etc.
- **Reusable Python helpers** — `apply_brand_palette.py` (color/font helpers for python-pptx) and `generate_branded_pptx.py` (one-call branded deck builder)

See [SKILL.md](SKILL.md) for the full overview.

---

## Building the slim version yourself

If the slim zip is stale or you want to rebuild after making changes:

```bash
python3 scripts/build_slim.py
# Output: dist/winningtemp-brand-slim/  (the unzipped slim skill)
#         dist/winningtemp-brand-slim.zip
```

The build script copies SKILL.md, all references, all scripts, and a curated subset of `assets/` (PNG logos only, JSON specs, icons, values, key templates, no fonts/EPS/Visual-identity master).

---

## Updating from SharePoint

When the brand team updates the live Visual identity document:

1. Download the new `Visual identity.pptx` from SharePoint (URL in [references/external-resources.md](references/external-resources.md)).
2. Replace `assets/Visual-identity-source.pptx` with the new file.
3. Re-run the extractor:
   ```bash
   python3 scripts/extract_visual_identity.py assets/Visual-identity-source.pptx
   ```
4. Diff `.extracted/summary.json` against the previous run; update markdown references in `references/` if anything changed (colors, fonts, logo specs).
5. Replace template/logo files in `assets/templates/` and `assets/logos/` if the brand team published new versions (these aren't auto-extracted).
6. Bump the date in `references/external-resources.md` so the team knows when the last sync happened.
7. Rebuild the slim version: `python3 scripts/build_slim.py`
8. Commit, push, tag a version (e.g., `v1.1.0`).

---

## Reporting issues / contributing

Found something wrong with the skill (stale data, missing assets, contradicting current SharePoint)? Open an issue or PR with:
- What you were trying to do
- What the skill said vs. what's actually current
- Link to the SharePoint version that's correct

Brand team contacts (for asset requests, logo modifications, sign-offs) are listed in [references/external-resources.md](references/external-resources.md).

---

## License

Internal Winningtemp tool. Brand assets (logos, photos, templates) are property of Winningtemp AB. Bundled fonts (Poppins, Inter) are licensed under the SIL Open Font License — see `assets/fonts/Poppins/OFL.txt`.

The skill scaffolding (SKILL.md, references, scripts) is intended for internal Winningtemp use.
