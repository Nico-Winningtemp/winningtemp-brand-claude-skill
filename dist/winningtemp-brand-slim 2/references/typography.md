# Typography

Two typefaces, both Google Fonts: **Poppins** for headlines, **Inter** for body text.

Machine-readable spec: `assets/typography.json`. Font installation: `assets/fonts/README.md`.

## Contents

- The two typefaces
- Hierarchy (H1 → body)
- Size ratios
- Recommended sizes
- Weights and when to use them
- Color rules
- Fallback stack
- CSS / python-pptx snippets
- Common mistakes

---

## The two typefaces

### Poppins (headlines)
A modern, geometric sans-serif with a friendly, clean look. Open shapes and high x-height keep it readable even at small sizes. Wide weight range. The style feels clear, confident, and aligned with our brand personality.

- **Use for:** headlines, subheadlines, emphasis, short supporting lines
- **Default weights:** Semibold (600) for H1, Medium (500) for H2
- **Other weights:** allowed in expressive/creative contexts (campaign graphics, posters)

### Inter (body text)
A clean, modern sans-serif designed for digital readability. Balanced proportions, simple shapes, excellent at small sizes. Pairs naturally with Poppins.

- **Use for:** all body copy, paragraphs, reports, internal documents, tables, captions, UI labels
- **Default weights:** Regular (400) or Medium (500) for body, Bold (700) for *occasional* emphasis only

---

## Hierarchy

```
H1 (Display / Hero)        Poppins Semibold        100pt example
  H2 (Subheading)          Poppins Medium          50pt   (= H1 × 0.5)
    H3 (Section)           Poppins Medium          ~32pt
      Body                 Inter Regular           10–14pt
        Caption / Footer   Inter Regular           min 7pt
```

The hierarchy is built on a **2:1 ratio** rule, anchored at the H1 size.

---

## Size ratios (the rules)

These are direct rules from the brand guideline:

1. **Subheading = 50% of headline.** If H1 is 100pt, H2 is 50pt. If H1 is 48pt, H2 is 24pt.
2. **Body in Poppins (when used for emphasis) = 50% of subheading.** Otherwise, use Inter at 10–14pt.
3. **Minimum size: 7pt.** Never go smaller — even for legal/footnote text.

### Example: A4 sales one-pager
- H1: 32pt Poppins Semibold
- H2: 16pt Poppins Medium
- Body: 11pt Inter Regular
- Caption: 8pt Inter Regular

### Example: 16:9 slide deck (KPI slide)
- Big number: 64pt Poppins Semibold (acts as H1)
- Label below: 14pt Inter Regular
- Section title: 28pt Poppins Medium
- Body bullets: 14pt Inter Regular

### Example: Presentation hero slide
- Title: 80pt Poppins Semibold
- Subtitle: 40pt Poppins Medium
- Date / context line: 18pt Inter Regular

---

## Recommended sizes by medium

| Medium | Body size | Headline size | Notes |
|---|---|---|---|
| Web (desktop) | 16px (≈12pt) | 48–72px H1 | Use rem units |
| Web (mobile) | 16px | 32–48px H1 | Don't shrink body below 16px |
| Print A4 docs | 10–11pt | 24–32pt H1 | Inter Regular for paragraphs |
| Print A3 posters | 12–14pt | 60+ pt H1 | Larger H1s for distance reading |
| 16:9 slide deck | 14–18pt | 32–80pt H1 | Body 14pt min; titles depend on slide density |
| Social posts (1080×1080) | 24–32pt | 60–96pt H1 | Designed for thumb scrolling |
| Internal docs | 11pt | 14–18pt H1 | Closer ratios for dense info |

---

## Weights

### Poppins weights
| Weight | Numeric | When to use |
|---|---|---|
| Light (300) | 300 | Avoid in branded output — too thin to feel confident |
| Regular (400) | 400 | Avoid for headlines — use Medium or Semibold |
| Medium (500) | 500 | **H2, subheads, decks subtitles** |
| Semibold (600) | 600 | **H1, hero titles, key emphasis** |
| Bold (700) | 700 | Reserved for very expressive/campaign use |
| ExtraBold (800) | 800 | Avoid — too heavy for our personality |

### Inter weights
| Weight | Numeric | When to use |
|---|---|---|
| Regular (400) | 400 | **Default body copy** |
| Medium (500) | 500 | Slightly stronger body, table headers, UI labels |
| Semibold (600) | 600 | Inline subheads inside body sections |
| Bold (700) | 700 | **Occasional emphasis only** — single words/phrases inside body |

---

## Color rules

- **Body text** is always `#18181B` (Black) on light or `#FFFFFF` (White) on dark.
- **Headlines** can be Black, White, or `#7F2696` (Dark Purple).
- **Wave** (`#C0DAD8`) and other secondary colors may appear in *display headlines* in expressive formats only — never body.
- See `references/colors.md` for the full color rules.

---

## Fallback stack

When Poppins/Inter aren't installed (e.g., generated PPTX opened on a machine without them):

```
Headlines: Poppins, "Helvetica Neue", Arial, sans-serif
Body:      Inter,   "Helvetica Neue", Arial, sans-serif
```

**Never fall back to:**
- Calibri (Microsoft default — feels generic, not on-brand)
- Aptos (the .pptx theme falls back to this — also not the brand)
- Times / Georgia / serif faces (wrong typographic personality)
- Comic Sans, Papyrus (obvious)

If neither Poppins nor Helvetica Neue is available, Arial is acceptable. Arial reads as neutral, not anti-brand.

---

## Code snippets

### CSS

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Poppins:wght@500;600&display=swap');

:root {
  --font-headings: 'Poppins', 'Helvetica Neue', Arial, sans-serif;
  --font-body:     'Inter',   'Helvetica Neue', Arial, sans-serif;
}

h1 { font-family: var(--font-headings); font-weight: 600; }
h2 { font-family: var(--font-headings); font-weight: 500; }
body, p { font-family: var(--font-body); font-weight: 400; }
strong  { font-weight: 700; }
```

### python-pptx

```python
from pptx.util import Pt

# Headline
heading_run.font.name = "Poppins"
heading_run.font.bold = True   # Semibold approximated via bold flag
heading_run.font.size = Pt(48)

# Body
body_run.font.name = "Inter"
body_run.font.size = Pt(14)
```

For full helpers, see `scripts/apply_brand_palette.py`.

---

## Common mistakes

1. **Using Calibri or Aptos.** PowerPoint defaults to these on Windows machines without the brand fonts installed. Always set the font explicitly to Poppins/Inter. If you're shipping a .pptx to someone without the fonts, accept the Helvetica Neue/Arial fallback — never Calibri.
2. **Mixing Poppins into body copy.** Body is Inter. Poppins in body is reserved for short emphatic supporting lines, sized at 50% of the surrounding subheading.
3. **Going below 7pt.** Even legal/footnote text stays at 7pt minimum.
4. **Using Light or ExtraBold weights.** Light feels timid; ExtraBold feels shouty. Stick to Regular/Medium/Semibold/Bold per the table above.
5. **Italics everywhere.** Both faces support italic, but use it sparingly — for citations, foreign words, named works. Not for general emphasis (use Bold instead).
6. **Mixing more than two type sizes per slide/section.** Stick to the hierarchy. If you need a third "size," it's usually a missing weight, not a missing size.
