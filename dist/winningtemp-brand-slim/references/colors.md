# Colors

The Winningtemp palette has three layers: **primary** (the core identity), **secondary** (accents and warnings), and **support** (text colors).

Machine-readable spec: `assets/color-palette.json`.

## Contents

- Primary palette
- Secondary palette
- Support (text) colors
- When to use each color
- CTA rules
- Background pairings
- Accessibility notes
- Common mistakes

---

## Primary palette

These are the visual backbone of the brand. They are used **mainly as background colors** to create structure, contrast, and a recognizable look. They can occasionally appear in display text or design elements for emphasis, but **never** in body copy.

| Color | Hex | RGB | Role |
|---|---|---|---|
| **Dark Purple** | `#7F2696` | 127, 38, 150 | Primary brand color. Hero backgrounds, primary CTAs, default logo color, key headlines, brand impact moments. The most distinctive Winningtemp color. |
| **Light Purple** | `#DDD3F2` | 221, 211, 242 | Soft section backgrounds, content cards, subtle highlights. Pairs well with purple text. |
| **Gray** | `#F1F1F1` | 241, 241, 241 | Neutral background. Large flat areas, content separation, low-emphasis sections. |

## Secondary palette

These extend and support the primary palette. They add flexibility, depth, and clearer hierarchy. **Use sparingly** — they support the primaries; they do not replace them.

| Color | Hex | RGB | Role |
|---|---|---|---|
| **Pale Purple** | `#F2E9F3` | 242, 233, 243 | Very light wash. Subtle dividers, table-row banding, hover states. |
| **Wave** | `#C0DAD8` | 192, 218, 216 | Mint-teal freshness accent. Highlights, icons, secondary callouts, growth/positive data points. **Reserve for accent — never primary.** |
| **Warning Red** | `#D64545` | 214, 69, 69 | Error states, regression indicators, declining metrics, alerts. **Never decorative.** Confirm exact hex against latest Visual identity if precise match is required. |

## Support (text) colors

| Color | Hex | RGB | Role |
|---|---|---|---|
| **Black** | `#18181B` | 24, 24, 27 | Primary body text on light backgrounds. Default body color. Logo black variant. |
| **White** | `#FFFFFF` | 255, 255, 255 | Primary body text on dark/purple backgrounds. Logo white variant. Card backgrounds on purple sections. |

---

## When to use each color

### Use Dark Purple (`#7F2696`) for:
- The primary CTA on every page/slide
- The default logo color
- Hero backgrounds (with white text)
- Key statistics or single highlighted numbers in display formats
- Section dividers in long documents
- Chart "primary series" color

### Use Light Purple (`#DDD3F2`) for:
- Subtle section backgrounds (with black text)
- Cards/tiles on neutral backgrounds
- Quote blocks, testimonial highlights
- Soft section transitions between major content blocks

### Use Gray (`#F1F1F1`) for:
- Page-level neutral backgrounds
- Inactive/disabled UI states
- Large empty layout areas

### Use Wave (`#C0DAD8`) for:
- Positive trend indicators (e.g., growth arrows, positive deltas)
- Secondary chart series (alongside purple)
- Decorative icons and small accents
- Data visualization "good" / "above target" states

### Use Pale Purple (`#F2E9F3`) for:
- Alternating table row backgrounds
- Hover/focus states on interactive elements
- Very subtle background washes that need to feel branded but not loud

### Use Warning Red (`#D64545`) for:
- Error messages
- "Below target" / declining metrics in dashboards
- Critical alerts only — never for emphasis or decoration

---

## CTA rules

CTAs (buttons, links, calls to action) **must** use only primary palette colors:

✅ Allowed CTA fills: `#7F2696` (Purple), `#FFFFFF` (White), `#18181B` (Black)
✅ Allowed CTA borders: same as fills, plus `#F1F1F1` for ghost CTAs
❌ Forbidden CTA colors: `#DDD3F2`, `#F2E9F3`, `#C0DAD8`, `#D64545`

**Why:** Secondary colors don't have enough contrast or brand recognizability to act as primary action signals. They're support colors.

### CTA examples

| Context | Background | Button fill | Button text |
|---|---|---|---|
| White section | `#FFFFFF` | `#7F2696` | `#FFFFFF` |
| Purple hero | `#7F2696` | `#FFFFFF` | `#7F2696` (or `#18181B`) |
| Light purple section | `#DDD3F2` | `#7F2696` | `#FFFFFF` |
| Dark/black section | `#18181B` | `#7F2696` | `#FFFFFF` |

---

## Background pairings

What text color goes on what background:

| Background | Body text | Headlines | Notes |
|---|---|---|---|
| `#FFFFFF` White | `#18181B` Black | `#18181B` or `#7F2696` | Most common for documents, web. |
| `#F1F1F1` Gray | `#18181B` Black | `#18181B` or `#7F2696` | Same rules as white. |
| `#DDD3F2` Light Purple | `#18181B` Black | `#18181B` or `#7F2696` | Don't put white text here — too low contrast. |
| `#F2E9F3` Pale Purple | `#18181B` Black | `#18181B` | Use for subtle backgrounds; treat like a tinted white. |
| `#7F2696` Dark Purple | `#FFFFFF` White | `#FFFFFF` | Hero / impact backgrounds. Never put black body text here. |
| `#C0DAD8` Wave | `#18181B` Black | `#18181B` or `#7F2696` | Wave is light enough for black text. |
| `#18181B` Black | `#FFFFFF` White | `#FFFFFF` | Rare; use sparingly. |

---

## Accessibility notes

- `#7F2696` Purple on White: contrast ratio ~7.5:1 — passes WCAG AA + AAA for normal text.
- `#7F2696` Purple on `#DDD3F2` Light Purple: contrast ratio ~5.8:1 — passes AA.
- White on Purple `#7F2696`: contrast ratio ~7.5:1 — passes AAA.
- `#18181B` on `#F1F1F1` Gray: ~17:1 — easily passes AAA.
- **Do not** put white text on Light Purple `#DDD3F2` or Wave `#C0DAD8` — fails accessibility.

When generating any digital artifact, verify contrast for any new color combinations.

---

## Common mistakes

1. **Using teal/coral instead of purple.** This skill exists partly because the March 2026 LinkedIn report did this. Wave (`#C0DAD8`) is mint-teal, but it is a *secondary accent*, not a primary background. There is no coral in the brand palette.
2. **Using Light Purple as a CTA color.** It's a background color — too low-contrast for a button.
3. **Putting body text in purple.** Purple is for headlines, backgrounds, CTAs. Body is always black or white.
4. **Adding "almost on-brand" colors** (like a slightly different purple). Use the exact hex codes — drift breaks brand recognition.
5. **Treating Warning Red as decoration.** It signals errors only. Don't use it to emphasize a positive metric.
6. **Skipping contrast checks** when overlaying text on photos or gradients.

---

## Quick reference

```
PRIMARY:   #7F2696 (Purple)  #DDD3F2 (Light Purple)  #F1F1F1 (Gray)
SECONDARY: #F2E9F3 (Pale)    #C0DAD8 (Wave)          #D64545 (Warning)
TEXT:      #18181B (Black)   #FFFFFF (White)
```
