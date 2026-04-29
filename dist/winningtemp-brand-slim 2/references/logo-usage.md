# Logo Usage

The Winningtemp logo consists of two elements that **always appear together** in the primary form: the **wordmark** ("Winningtemp") and the **symbol** (the geometric "star/diamond" mark).

All official logo files live in `assets/logos/` — sourced directly from the brand team. Use these instead of any older versions.

## Contents

- File organization in `assets/logos/`
- Approved colors (Deep Purple / White / Black)
- Variants and when to use each
- File format guide (PNG / EPS / SVG, RGB / CMYK / PMS)
- Clear space (safe area)
- Minimum sizes
- Backgrounds and contrast
- App symbol — restricted use
- Do's and don'ts
- Where to get higher-resolution / source files

---

## File organization in `assets/logos/`

```
assets/logos/
├── standard/                                          ← Use these for everyday digital work
│   ├── Winningtemp_RGB Deep purple (Without tagline).png
│   └── Winningtemp_RGB White (Without tagline) (1).png
└── variations/                                        ← Full library by purpose × color × format
    ├── Winningtemp Logo/                              ← Default: wordmark + symbol
    │   ├── Black/      → CMYK.eps · PMS.eps · RGB.eps · RGB.png
    │   ├── Deep purple/ → CMYK.eps · PMS.eps · RGB.eps · RGB.png
    │   └── White/      → CMYK.eps · RGB.eps · RGB.png
    ├── Winningtemp Logo (Without tagline)/            ← Same as above, no "SUCCEED TOGETHER" tagline
    │   ├── Black (Without tagline)/
    │   ├── Deep purple (Without tagline)/
    │   └── White (Without tagline)/
    ├── Winningtemp Logo (tagline)/                    ← Same as Logo/ — explicit tagline subfolder
    │   ├── Black (tagline)/
    │   ├── Deep purple (tagline)/
    │   └── White (tagline)/
    └── Winningtemp Symbol/                            ← Symbol on its own
        ├── App symbol (ONLY PRODUCT USE)/             ⚠ Restricted — see below
        ├── Black Symbol/
        ├── Deep purple Symbol/
        └── White Symbol/
```

### Quick file picker

| I need… | Use this file |
|---|---|
| Logo for a slide / web / doc (digital) | `standard/Winningtemp_RGB Deep purple (Without tagline).png` |
| Logo for white-on-purple slide | `standard/Winningtemp_RGB White (Without tagline) (1).png` |
| Logo for print (with tagline) | `variations/Winningtemp Logo/Deep purple/Winningtemp_CMYK Deep purple.eps` |
| Logo for spot-color print | the `PMS` EPS in the matching color folder |
| Symbol only (favicon, app icon, watermark) | `variations/Winningtemp Symbol/Deep purple Symbol/Winningtemp_Symbol RGB Deep purple Symbol.png` |
| Symbol for white-on-dark | `variations/Winningtemp Symbol/White Symbol/Winningtemp_Symbol RGB White Symbol.png` |

---

## Approved colors

The logo may **only** appear in three colors. No exceptions.

| Color | Hex | Internal name | When to use |
|---|---|---|---|
| **Deep Purple** | `#7F2696` | "Deep purple" | **Default.** Use on white, gray, or light-purple backgrounds. |
| **White** | `#FFFFFF` | "White" | On dark/purple backgrounds, dark photography. |
| **Black** | `#18181B` | "Black" | Secondary, use sparingly. Black-and-white print, monochrome contexts only. |

**Primary recommendation:** Use Deep Purple or White wherever possible. Black is technically allowed but reduces brand clarity if overused.

**Forbidden:** any other color, gradients, outline-only versions, drop shadows, glows, recolored variants.

---

## Variants and when to use each

### 1. Logo (wordmark + symbol + tagline) — DEFAULT for solo placements
Folder: `Winningtemp Logo/` (or `Winningtemp Logo (tagline)/` — same content)

The full logo with the "SUCCEED TOGETHER" tagline below the wordmark.

- **Use when:** the logo appears on its own with sufficient clear space (covers, print collateral, large-format material, branded swag).
- **Do not use:** on the website or in publishing/editorial content. The tagline is for brand marks in standalone contexts, not navigation/headers.

### 2. Logo without tagline — DEFAULT for general use
Folder: `Winningtemp Logo (Without tagline)/`

Same wordmark + symbol but no "SUCCEED TOGETHER" line.

- **Use when:** the logo sits inside layouts (slide headers, doc footers, web headers, signatures, embedded in content). This is the most common variant.

### 3. Symbol only (no wordmark)
Folder: `Winningtemp Symbol/Black Symbol/`, `Deep purple Symbol/`, `White Symbol/`

The standalone symbol mark.

- **Use when:** space is too tight for the wordmark (favicons, social profile pictures, app icons for non-product use, watermarks in print).
- The symbol must always appear in full — never cropped.

### 4. App symbol — ⚠ ONLY for the product
Folder: `Winningtemp Symbol/App symbol (ONLY PRODUCT USE)/`

This is a separate, distinct mark intended only for the Winningtemp product UI / product-related icons.

- **Use when:** building product UI mockups, app store listings, in-product designs.
- **Never use:** in marketing, sales, social, ad creative, or any non-product context. Use the regular Symbol files instead.

---

## File format guide

| Format | Use for | Color models available |
|---|---|---|
| **PNG (RGB)** | Web, slides, docs, social, email | RGB |
| **EPS (RGB)** | Print pieces handled in design software | RGB |
| **EPS (CMYK)** | Process-color print (4-color print runs) | CMYK |
| **EPS (PMS)** | Spot-color print (Pantone match — premium print, swag, signage) | PMS |
| **SVG** | Web (where vector scaling matters), favicons, design-tool import | RGB |

### Quick decision tree
- "I'm putting this in a slide / web page / doc / email" → use the **RGB PNG** from `standard/`.
- "I'm sending this to a designer/printer for a brochure/poster" → use the **CMYK EPS** from the matching `variations/` folder.
- "It's premium swag (T-shirts, signs, retractable banners) with a custom Pantone color" → use the **PMS EPS**.
- "I need crisp scaling at any size on a website" → use the **SVG** if available, or the largest PNG.

---

## Clear space (safe area)

Maintain minimum clear space around the logo equal to the **height of the symbol**. More is recommended.

```
        ┌─────────┐
        │         │   ← clear space (= symbol height)
   ┌────┴─────────┴────┐
   │                   │
   │   Winningtemp ✦   │  ← logo
   │                   │
   └────┬─────────┬────┘
        │         │   ← clear space (= symbol height)
        └─────────┘
```

No other elements (text, images, lines, other logos) may enter this zone.

---

## Minimum sizes

| Medium | Minimum width |
|---|---|
| **Print** | 50mm wide (full logo with wordmark + symbol) |
| **Web** | 200px wide (full logo) |
| Symbol-only | No formal min; use judgment for legibility (≥ 32px web is safe) |

### Size reference (from Visual identity slide 7)
- A5 page: 200px / 50mm
- A4 page: 260px / 70mm
- A3 page: 350px / 95mm

Below the minimum, the wordmark loses legibility. If your space is smaller, switch to the **symbol-only** variant.

---

## Backgrounds and contrast

The logo must always sit on a background with sufficient contrast.

### ✅ Allowed pairings

| Logo color | Background |
|---|---|
| Deep Purple | White, Gray (`#F1F1F1`), Light Purple (`#DDD3F2`), Pale Purple (`#F2E9F3`), Wave (`#C0DAD8`) |
| White | Deep Purple, Black, dark photography |
| Black | White, Light Gray (use sparingly) |

### ❌ Forbidden pairings
- Deep Purple logo on Deep Purple background (no contrast)
- White logo on Light Purple / Wave (insufficient contrast)
- Logo on busy photography without a contrast plate or scrim
- Logo on patterned/textured backgrounds without a clean container

If you must place the logo on a complex image, add a clean rectangular plate (white or purple) behind it, respecting clear space.

---

## Do's and don'ts

### ✅ Always:
- Use the original logo files from `assets/logos/`
- Use one of the three approved colors only
- Maintain minimum clear space and minimum size
- Place on a background with sufficient contrast
- Keep proportions intact (constrain when scaling)
- Use the right format for the medium (RGB PNG for digital, CMYK/PMS EPS for print)

### ❌ Never:
- Rotate or tilt the logo
- Stretch, compress, or distort
- Recolor (no gradients, outlines, or non-approved colors)
- Redraw or recreate from scratch
- Add effects: drop shadow, glow, bevel, emboss, 3D
- Crop the symbol or wordmark
- Place on busy/low-contrast backgrounds
- Combine with other logos directly (use clear space + a separator)
- Animate without brand-team approval
- Use old/superseded versions you may have lying around
- Use the **App symbol** outside of product UI

---

## Where to get higher-resolution / source files

The skill bundles RGB PNG + EPS variants. For:
- AI/InDesign source files
- Updated/revised logos (when the brand team releases changes)
- Co-branded variants (logo + customer/partner)
- Animation-ready or motion logos

→ See `references/external-resources.md` for the SharePoint master and brand-team contact.

---

## When unsure: ask the brand team

If you're tempted to:
- Recolor the logo
- Crop the symbol
- Combine with another mark
- Apply effects
- Use the App symbol outside the product
- Animate the logo

…stop and check with the brand team. Brand consistency depends on these requests being routed properly rather than improvised.
