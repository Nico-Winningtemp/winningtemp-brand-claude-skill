# Fonts

The brand uses two typefaces, both bundled here. Source-of-truth specs live in `assets/typography.json` and the `references/typography.md` file in this skill.

## What's bundled

```
fonts/
├── Poppins/   18 .ttf files (all weights + italics) + OFL.txt license
└── Inter/     18 .otf files (all weights + italics)
```

Both are free for commercial use under the SIL Open Font License (OFL).

### Poppins weights included
Thin, ExtraLight, Light, Regular, Medium, SemiBold, Bold, ExtraBold, Black + matching italics.

**Brand-default weights:** Medium (500), SemiBold (600).

### Inter weights included
Thin (BETA), ExtraLight (BETA), Light (BETA), Regular, Medium, SemiBold, Bold, ExtraBold, Black + matching italics.

**Brand-default weights:** Regular (400), Medium (500), Bold (700) for emphasis.

## Installing the fonts on your machine

### macOS
1. Open `Finder` → navigate to `assets/fonts/Poppins/` (or `Inter/`).
2. Select all `.ttf` (or `.otf`) files.
3. Double-click any one → click **Install Font** in Font Book.
4. Repeat for the other family.

Or via terminal:
```bash
cp assets/fonts/Poppins/*.ttf ~/Library/Fonts/
cp assets/fonts/Inter/*.otf  ~/Library/Fonts/
```

### Windows
1. Select all `.ttf` / `.otf` files in `assets/fonts/Poppins/` and `assets/fonts/Inter/`.
2. Right-click → **Install for all users** (requires admin) or **Install** (current user only).

### Linux (Ubuntu/Debian)
```bash
mkdir -p ~/.local/share/fonts/Poppins ~/.local/share/fonts/Inter
cp assets/fonts/Poppins/*.ttf ~/.local/share/fonts/Poppins/
cp assets/fonts/Inter/*.otf   ~/.local/share/fonts/Inter/
fc-cache -fv
```

After installation, restart any open apps (PowerPoint, Word, browsers, design tools) so they pick up the new fonts.

## Using the fonts in different contexts

### PowerPoint / Word
Once installed system-wide, they appear in the font menu. Select **Poppins SemiBold** for H1, **Inter Regular** for body. The branded templates in `assets/templates/` already use these.

### Web (CSS)

**Option A — bundle locally:**
```css
@font-face {
  font-family: 'Poppins';
  src: url('/fonts/Poppins/Poppins-SemiBold.ttf') format('truetype');
  font-weight: 600;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter/Inter-Regular.otf') format('opentype');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
/* repeat for other weights */
```

**Option B — Google Fonts (recommended for web):**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Poppins:wght@500;600&display=swap" rel="stylesheet">
```

Lighter on bandwidth (CDN cached), guaranteed up-to-date.

### Python (matplotlib, PIL, etc.)
```python
from matplotlib import font_manager
font_manager.fontManager.addfont('assets/fonts/Poppins/Poppins-SemiBold.ttf')
font_manager.fontManager.addfont('assets/fonts/Inter/Inter-Regular.otf')
```

### python-pptx
Set `font.name = "Poppins"` / `"Inter"` on text runs. The font won't be embedded in the .pptx by default — install it on the viewer's machine, or have python-pptx embed it (more advanced).

## Why bundle the fonts at all?

1. **Generated PPTX/DOCX files render correctly** even on machines without internet (no Google Fonts fallback to Calibri).
2. **Designers/marketing teammates can install once** instead of hunting for the right Google Fonts page.
3. **Print pieces** going to a third-party printer can include the font files in the package.
4. **Offline development** — the fonts work even without a network.

## Why not bundle everything?

Other typefaces (Aptos, Calibri, Helvetica Neue) **are not** Winningtemp fonts. The skill bundles Poppins + Inter only. If a generated artifact opens on a machine without these:
- **Acceptable fallback:** Helvetica Neue → Arial (sans-serif).
- **Never acceptable:** Calibri, Aptos, Comic Sans, Times.

## License

Both fonts are licensed under the **SIL Open Font License** (OFL).
- `Poppins/OFL.txt` — full Poppins license
- Inter is also OFL-licensed (the .otf files don't include the license text bundled, but the license is published at https://github.com/rsms/inter/blob/master/LICENSE.txt)

Free for commercial use, redistribution, embedding, and modification (with restrictions on naming derivatives). Read the OFL if you plan to modify or redistribute.

## Updating the fonts

If Google releases new versions of Poppins or Inter:
1. Download the latest from [Google Fonts](https://fonts.google.com).
2. Replace the contents of `Poppins/` and `Inter/`, keeping the same filenames.
3. Test against the brand templates — sometimes new font versions change metrics slightly.
