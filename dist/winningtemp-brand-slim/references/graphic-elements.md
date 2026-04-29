# Graphic Elements

Graphic elements are the supporting shapes and visual motifs that bring rhythm, structure, and personality to Winningtemp's design system. Used consistently, they strengthen recognition without overpowering core content.

The elements draw inspiration from **data, movement, growth, simplicity,** and the **human experience**.

## Contents

- The core shape language
- Image masking (rounded rectangle)
- Branded shape masks (the inner star / symbol)
- The Winningtemp symbol as a graphic element
- Layout principles (alignment, spacing, hierarchy)
- Common mistakes

---

## The core shape language

Three categories of shapes:
1. **Containers** — rounded rectangles that hold imagery or content blocks.
2. **Brand shapes** — the symbol's inner geometry (the diamond/star) used as expressive accents.
3. **Decorative motifs** — soft circles, curves, lines that suggest data and movement.

All shapes follow the same principles:
- Rounded, soft corners (no sharp 90° angles in decorative use)
- Single-color fills using the brand palette
- Generous white space around them
- Used **with clear purpose** — never just to fill space

---

## Image masking — rounded rectangle (DEFAULT)

The **rounded rectangle** is our primary container for masked imagery. It creates a clean, structured frame that works across formats and screen sizes.

### Specs
- **Corner radius:** generous, but not capsule. Aim for ~5–8% of the shorter side. Examples:
  - 600×400px image → 32px corner radius
  - 1200×800px image → 64px corner radius
  - A4 print image (170mm wide) → 12mm corner radius
- **Aspect ratios that work well:** 4:3, 16:9, 1:1, 4:5 (portrait social), 3:4 (print)
- **Border:** none by default. If a separator is needed, use a 1px Light Purple `#DDD3F2` line.
- **Drop shadow:** none. Flat by default.

### When to use
- Hero photos in slides and web pages
- Customer/team photos in case studies
- Product UI screenshots in marketing materials
- Any standalone photo that needs a contained frame

### Code reference (CSS)
```css
.wt-image {
  border-radius: 32px;        /* adjust to ~5-8% of shorter side */
  overflow: hidden;
  display: block;
}
```

### Code reference (python-pptx)
python-pptx doesn't expose corner radius for pictures directly. Workaround: place the picture inside an auto-shape (`MSO_SHAPE.ROUNDED_RECTANGLE`) configured as a picture fill. See `scripts/apply_brand_palette.py` for a helper.

---

## Branded shape masks (the inner star / symbol)

For more **expressive or campaign-driven applications**, mask imagery using:
- The **inner star** (the diamond geometry from inside our symbol)
- The **logo icon** itself (less common — heavier brand presence)

### When to use
- Campaign hero visuals (e.g., a recruiting campaign cover)
- Branded social posts where impact matters more than scannability
- Editorial-style spreads
- Annual report covers

### When NOT to use
- Standard slide imagery (rounded rectangle is the default)
- UI screenshots (clarity matters; the mask interferes)
- Customer photos in case studies (use rounded rectangle to be respectful and conventional)
- Repeated/grid layouts (looks busy)

### Application rule
**Sparingly.** Use these shape masks to create emphasis or a branded layer in the composition. A single hero shape mask per piece is usually right. More than one and the design starts to feel decorated rather than designed.

---

## The Winningtemp symbol as a graphic element

The symbol (the star/diamond mark) can be used **on its own** as a graphic element, beyond its role in the logo.

### Approved standalone uses
- **Watermark** in print or large-format material — at low opacity (10–20%) in Deep Purple, Light Purple, or Pale Purple
- **Background motif** — full-bleed at very large scale, partially cropped to the edge of the page (a classic graphic move; signals brand without being a logo)
- **Bullet point** — at small scale next to a list item
- **Section divider** — single instance between major content sections
- **Loading/empty state** in product UI

### Rules (from `references/logo-usage.md`)
- Only in approved primary colors (Deep Purple, White, Black, or low-opacity tints)
- Never rotated, cropped (other than full-bleed background), distorted, or recolored
- Never combined with other shapes to form a new mark

### Code reference
Use `assets/logos/variations/Winningtemp Symbol/Deep purple Symbol/Winningtemp_Symbol RGB Deep purple Symbol.png` (or the white/black equivalent).

---

## Layout principles

Three rules that apply to all graphic-element work:

### 1. Alignment
Everything aligns to a grid. For:
- **Slides:** 12-column grid with 24px gutters at 1920×1080
- **Web:** 12-column container with 24px or 32px gutters
- **Print:** start with the page's text grid; align graphic elements to that

### 2. Spacing
Generous white space is a brand signature. Avoid edge-to-edge density.
- Minimum margin from page/slide edge: 5% of the shorter side
- Between graphic blocks: 1.5–2× the body line-height
- Around the logo: see `references/logo-usage.md` (clear space rule)

### 3. Hierarchy without weight
Lead with **size and color**, not weight or borders. A large rounded-rectangle photo + a confident purple headline already creates hierarchy. You usually don't need lines, boxes, or background shading on top.

---

## Composition examples

### Slide cover
```
+--------------------------------------------------+
|  [Symbol watermark, low opacity, top-right]      |
|                                                  |
|   POPPINS SEMIBOLD 60PT                          |
|   Headline goes here                             |
|                                                  |
|   POPPINS MEDIUM 30PT                            |
|   Subheading                                     |
|                                                  |
|   [Logo bottom-left, small]                      |
+--------------------------------------------------+
```

### Content slide with image
```
+---------------------+----------------------------+
|                     |                            |
|   POPPINS SEMI 36   |   [Rounded-rectangle       |
|   Section title     |    masked image,           |
|                     |    aspect 4:3]             |
|   INTER 14          |                            |
|   Body paragraph... |                            |
|   - Bullet          |                            |
|   - Bullet          |                            |
|                     |                            |
+---------------------+----------------------------+
```

### Editorial / campaign spread
```
+--------------------------------------------------+
|              [Star-masked hero image,            |
|               full-bleed where appropriate]      |
|                                                  |
|   Big POPPINS SEMIBOLD headline overlaid         |
|   in Deep Purple or White (depending on bg)      |
+--------------------------------------------------+
```

---

## Common mistakes

1. **Using sharp 90° rectangles for image masks.** The brand always uses rounded corners. Sharp corners look like a mistake or non-branded asset.
2. **Overusing the star/symbol mask.** It's an emphasis tool. One per piece is usually right.
3. **Stacking graphic elements.** Don't put a star-masked photo inside a rounded rectangle inside a colored background block. Pick one container.
4. **Adding drop shadows or glows.** The brand is flat. Shadows date a design and feel bolt-on.
5. **Tiny corner radius.** A 4px radius on a large image looks like a default browser style. Use 5–8% of the shorter side.
6. **Symbol watermark at full opacity.** Watermarks should be 10–20% opacity. Higher and they read as a placement error.
7. **Using stock geometric patterns.** Skip the dot grids, isometric backgrounds, generic abstract waves. Stick to the brand's own shapes.
