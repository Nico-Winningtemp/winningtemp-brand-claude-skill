---
name: winningtemp-brand
description: This skill should be used when creating any branded artifact for Winningtemp — including presentations, PDFs, ad creative, social posts, sales decks, blog graphics, internal documents, web copy, email signatures, or anything carrying the Winningtemp name. Triggers on requests mentioning "Winningtemp branding", "brand guidelines", "on-brand", "our colors", "our fonts", "our logo", "logo usage", "brand voice", "messaging", "visual identity", "brand values", "icons", or on any request to generate slides, PDFs, marketing materials, email signatures, or copy in this repo. Provides exact hex codes, Poppins/Inter typography rules (with bundled font files), official logo variants in RGB/CMYK/PMS, the full 95-icon library, the four brand values, ready-to-use PowerPoint and Word templates, and EN/SE/NO voice guidelines drawn from the official Visual identity document.
---

# Winningtemp Brand

This skill packages Winningtemp's official brand identity — including real logo files, fonts, icons, templates, and brand values — so any artifact you produce comes out on-brand by default.

**Source of truth:** `assets/Visual-identity-source.pptx` (snapshot, ~46 MB) and the live SharePoint master at `references/external-resources.md`. The repo copy is a snapshot; SharePoint wins ties.

## What's in this skill

```
winningtemp-brand/
├── SKILL.md                 (this file — load first)
├── references/
│   ├── colors.md            full palette, hex/RGB, when to use each
│   ├── typography.md        Poppins/Inter rules, sizes, hierarchy
│   ├── logo-usage.md        variants, formats (RGB/CMYK/PMS), do's and don'ts
│   ├── icons.md             95-icon library inventory and usage
│   ├── brand-values.md      4 values (Curious, Results Together, Passion, Responsibility)
│   ├── templates.md         PPTX / Word / email-signature usage
│   ├── deck-design.md       slide-layout patterns: white default, purple as exception
│   ├── graphic-elements.md  shapes, image masks, the symbol as graphic
│   ├── imagery-guidelines.md photography style and selection rules
│   ├── voice-and-tone.md    brand voice, EN/SE/NO localization
│   └── external-resources.md SharePoint URL, brand-team contacts
├── assets/
│   ├── Visual-identity-source.pptx   ~46 MB master document (source of truth)
│   ├── color-palette.json            machine-readable colors
│   ├── typography.json               machine-readable font specs
│   ├── logos/                        OFFICIAL logos
│   │   ├── standard/                 RGB PNG, deep purple + white (no tagline)
│   │   └── variations/               full library: with/without tagline × 3 colors × RGB/CMYK/PMS EPS + PNG
│   ├── fonts/
│   │   ├── Poppins/                  18 .ttf files (all weights + italics)
│   │   ├── Inter/                    18 .otf files (all weights + italics)
│   │   └── README.md                 install instructions
│   ├── icons/
│   │   ├── black/                    95 PNG icons
│   │   └── white/                    (placeholder for white set)
│   ├── values/                       4 brand-value PDFs + PNGs
│   └── templates/
│       ├── winningtemp-presentation-template.pptx       4.5 MB official deck template
│       ├── winningtemp-word-template.dotx               Word template
│       ├── winningtemp-word-template-with-footer.dotx   Word + footer
│       └── email-signature.docx                         Email signature
└── scripts/
    ├── extract_visual_identity.py    re-run when SharePoint version updates
    ├── apply_brand_palette.py        python-pptx helper library
    └── generate_branded_pptx.py      reusable branded deck builder (uses official template)
```

## How to use this skill

### When generating anything visual
1. **Always** load `references/colors.md` and `references/typography.md`.
2. **Use logos from `assets/logos/`** — for digital, default to `assets/logos/standard/Winningtemp_RGB Deep purple (Without tagline).png`. Full file picker in `references/logo-usage.md`.
3. **For PowerPoint:** open `assets/templates/winningtemp-presentation-template.pptx` as the base, or use `scripts/generate_branded_pptx.py`. Don't build from scratch.
4. **For Word docs:** use the matching `.dotx` template from `assets/templates/`.
5. **For icons:** use the official set in `assets/icons/black/`. See `references/icons.md` for the 95-icon inventory and substitution table.

### When writing copy
1. Load `references/voice-and-tone.md` and `references/brand-values.md` before drafting any customer-facing or branded text.
2. For Swedish (SE) or Norwegian (NO) content, the voice file has language-specific guidance. **Don't auto-translate** — get a native speaker for marketing copy.

### When the user is unsure or asks "where is X?"
Point to the SharePoint master in `references/external-resources.md` — that's the live document the brand team maintains.

## Critical brand facts (always loaded)

These are the highest-frequency rules. Full detail in references.

### Colors
- **Primary:** `#7F2696` Deep Purple — the most distinctive Winningtemp color.
- **Secondary backgrounds:** `#DDD3F2` Light Purple, `#F1F1F1` Gray.
- **Accent:** `#C0DAD8` Wave (mint-teal) — for highlights/icons only, never primary.
- **Text:** `#18181B` near-black on light, `#FFFFFF` white on dark/purple.
- **CTAs use only primary palette colors.** Never use secondary colors for CTAs.

### Typography
- **Headlines:** Poppins (Semibold for H1, Medium for H2)
- **Body:** Inter (Regular/Medium for body, Bold for emphasis only)
- **Sizing:** subheading = 50% of headline. Body = 10–14pt, never below 7pt.
- **Fallback:** Helvetica Neue → Arial. Never Calibri/Aptos.

### Logo
- Three approved colors only: **Deep Purple, White, or Black.**
- Formats: RGB PNG (digital), CMYK EPS (process print), PMS EPS (spot print), some SVG.
- The wordmark + symbol always appear together in the primary form.
- Minimum size: 50mm wide print / 200px wide web.
- Clear space: minimum equal to symbol height.
- Never rotate, tilt, stretch, distort, recolor, redraw, or place on busy backgrounds.
- The **App symbol** (in `Winningtemp Symbol/App symbol (ONLY PRODUCT USE)/`) is **only for product UI** — never marketing.

### Brand values (the lens for all copy)
1. We are Curious
2. We get Results Together
3. We show Passion
4. We take Responsibility

See `references/brand-values.md` for what each means and how it shows up in writing/design.

### Voice
- Honest, modern, warm, inclusive. Never aggressive, hypey, or jargon-heavy.
- Lead with the human/business problem, not the feature.
- Bilingual: Swedish and Norwegian get equal weight in Nordic markets.

## Gotchas (real failures to avoid)

1. **Don't use teal/coral palettes.** The March 2026 LinkedIn Ads report used a generic dark-teal/coral theme. The brand is purple-led; Wave (`#C0DAD8`) is *secondary accent only*; there is no coral in the brand at all.
2. **Don't put Wave on Dark Purple backgrounds.** STRICT RULE. Wave (`#C0DAD8`) does NOT pair with Deep Purple (`#7F2696`) — not as cards, not as accent bars, not as dividers, not as chart series. On purple slides, use **White** for high-contrast cards or **Light Purple `#DDD3F2`** for soft cards. Wave is reserved for differentiating boxes on *light* layouts, growth arrows on charts, and small accents — used sparingly. (See `references/colors.md` for the full rule.)
3. **Don't default to dark-purple slide backgrounds.** STRICT RULE. The brand convention is **white-by-default, purple for impact only**. Reserve Deep Purple backgrounds for: title slide, end slide, optional section dividers, and at most one "hero stat" callout. Budget: max ~25% of slides on purple. The remaining 75%+ are white with purple headlines and accents. The Visual identity master document is 100% white-background. (See `references/deck-design.md` for slide patterns and the budget table.)
3. **Don't use Calibri or Aptos.** The .pptx theme falls back to Aptos because Microsoft ships it; it's **not** the brand. Always set Poppins/Inter explicitly. Fonts are bundled at `assets/fonts/`.
3. **Don't put body copy in purple.** Purple is for headlines, backgrounds, CTAs. Body is **always** black on light or white on dark.
4. **Don't use secondary colors in CTAs.** Light Purple, Wave, Pale Purple are support. CTAs use Purple/White/Black only.
5. **Don't recolor the logo.** Only Deep Purple, White, or Black. Even "close to purple" is wrong.
6. **Don't crop, rotate, or recolor the symbol.** Use only the official files. Place on contrasting backgrounds.
7. **Don't use the App symbol outside the product.** That's a separate, restricted mark. Use the regular Symbol files for marketing/social.
8. **Don't build PowerPoint decks from scratch.** Open `assets/templates/winningtemp-presentation-template.pptx` as the base — it has the colors, fonts, and master layouts already correct.
9. **Don't auto-translate marketing copy.** Use a native speaker for SE/NO. Direct translation produces stilted prose.
10. **Don't use generic icon libraries** (Lucide, FontAwesome, Material) when the official set in `assets/icons/black/` has 95 brand-styled options. See `references/icons.md` for substitutions.

## Workflow: building a branded artifact

Copy this checklist:

```
- [ ] Format confirmed (PPTX / Word / PDF / image / web)
- [ ] Started from official template if one exists (assets/templates/)
- [ ] Loaded references/colors.md and references/typography.md
- [ ] Used #7F2696 as primary (not teal/coral/blue)
- [ ] Headlines in Poppins, body in Inter (never Calibri/Aptos)
- [ ] Logo: correct variant + correct format + correct color, sized ≥ minimum, with clear space
- [ ] Icons from assets/icons/black/ (not from external libraries)
- [ ] CTAs use primary palette only
- [ ] Body copy is black-on-light or white-on-dark
- [ ] If multi-language, native speaker reviewed (SE/NO never auto-translated)
- [ ] No stretching/rotating/recoloring of logo or icons
- [ ] App symbol used ONLY in product contexts
```

## Workflow: writing branded copy

```
- [ ] Loaded references/voice-and-tone.md AND references/brand-values.md
- [ ] Audience identified (CHRO / HRBP / manager / employee / executive / IT)
- [ ] Language confirmed (EN / SE / NO)
- [ ] Lead with the human/business problem, not feature names
- [ ] At least one of the 4 values shows up naturally in the writing
- [ ] Avoided buzzwords: synergy, leverage, robust, best-in-class, scalable
- [ ] Avoided hype: revolutionary, game-changing, transformative
- [ ] Used active voice, short sentences, concrete examples
- [ ] CTAs are specific (not "Learn more")
- [ ] If SE: used "du" not "Ni"; decimal comma; lowercase day/month names
- [ ] If NO: Bokmål by default; correct æ/ø/å
- [ ] Reads like a person who cares wrote it
```

## When to ask the user

- The user requests a color or font that isn't in the palette/spec — confirm before deviating.
- The user wants logo modifications (recolor, crop, animate) — these need brand-team sign-off; route to `references/external-resources.md`.
- The artifact will be customer-facing and you don't have access to current product/feature naming — verify rather than guess.
- The user wants to use the App symbol outside the product — confirm and warn.

## Distribution to teammates

This skill lives in the repo at `.claude/skills/winningtemp-brand/` and travels via git. To make it available across all your projects:

```bash
ln -s "$(pwd)/.claude/skills/winningtemp-brand" ~/.claude/skills/winningtemp-brand
```

Or copy it into `~/.claude/skills/` for an independent install.
