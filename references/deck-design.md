# Deck Design

How to lay out a Winningtemp deck so it matches the brand convention. This is the rule set Claude / designers should follow when generating new presentations.

The official Visual identity .pptx is the reference. Every one of its 24 slides uses a **white background** — purple appears as headline color, accent shapes, and the logo, never as the slide canvas itself.

## Contents

- The default rule
- Background budget
- When to use purple as a background
- Slide patterns
- Layout conventions
- Common mistakes

---

## The default rule

> **Default to a WHITE background. Purple is the exception, not the rule.**

When generating a deck, the working assumption for every new slide is:
- Background = `#FFFFFF` White
- Headlines = `#7F2696` Deep Purple (Poppins SemiBold, large)
- Body = `#18181B` Black (Inter Regular)
- Accents = the brand palette per `references/colors.md`

You override the white default only for the specific slide types listed under "When to use purple as a background" below.

---

## Background budget

Across a typical deck, no more than **25%** of slides should use Deep Purple as the background. For a 16-slide deck that's roughly 4 slides max.

| Deck length | Max purple-bg slides |
|---|---|
| 5 slides | 1–2 |
| 10 slides | 2–3 |
| 15 slides | 3–4 |
| 20 slides | 4–5 |
| 30 slides | 6–7 |

If you find yourself building most slides on purple, stop and ask whether they actually need to be impact moments — or whether they're regular content slides that should be on white.

---

## When to use purple as a background

A purple background signals "this is an impact moment." Use it for:

| Slide role | Background |
|---|---|
| **Title / cover** | Deep Purple `#7F2696` (white text, white logo bottom-right) |
| **End / closing** | Deep Purple (white text, white logo) |
| **Major section dividers** (between Part 1 and Part 2, etc.) | Deep Purple OR Light Purple `#DDD3F2` |
| **Hero stat callout** (e.g. one big number that defines the deck) | Deep Purple, sparingly — pick the single most important moment |
| All other slides | **White (default)** |

For a typical sales / commercial / product deck:
- Slide 1: Title → Deep Purple ✓
- Slides 2 to N-1: Content → White ✓
- Slide N: Closing → Deep Purple ✓

That's 2 purple slides regardless of length. Add 1–2 more only if there's a genuine "this deserves a hero moment" content slide.

---

## Slide patterns

These are the structures the brand guideline uses across its 24 slides. Borrow these patterns.

### Section header (light)
```
+--------------------------------------------------+
|                                                  |
|   01.                       <-- big number, top-left, Deep Purple, Poppins
|                                                  |
|   Section title             <-- huge headline, Poppins SemiBold ~60pt, Black
|                                                  |
|   One-line description.     <-- Inter Regular, ~16pt, Black
|                                                  |
+--------------------------------------------------+
                                                White background
```

### Content slide (split layout)
```
+---------------------+----------------------------+
|                     |                            |
|  Topic title        |  [Rounded-rectangle        |
|  Poppins ~36pt      |   masked image, OR a       |
|                     |   simple key-detail block] |
|  Inter body...      |                            |
|  • bullet           |                            |
|  • bullet           |                            |
|                     |                            |
+---------------------+----------------------------+
                                                White background
```

### Title / cover (purple)
```
+--------------------------------------------------+
|                                                  |   Deep Purple background
|  Big headline (Poppins SemiBold, white)         |
|                                                  |
|  Subtitle / context (Inter, white)              |
|                                                  |
|                                                  |
|                                  [White logo]   |
+--------------------------------------------------+
```

### End / closing (purple)
```
+--------------------------------------------------+
|                                                  |   Deep Purple background
|              Questions?                          |
|                                                  |
|              Brief follow-up line                |
|                                                  |
+--------------------------------------------------+
```

### Hero callout (purple, sparingly)
```
+--------------------------------------------------+
|                                                  |   Deep Purple background
|            12%                                   |   (one slide per deck max)
|            of customers at ~100% churn risk      |
|                                                  |
+--------------------------------------------------+
```

---

## Layout conventions (brand-guideline style)

These apply on white-background slides:

1. **Headline first, big.** Poppins SemiBold at 36–60pt depending on slide density. Don't shrink the headline to fit more body — split the slide instead.

2. **Section number top-left.** "01.", "02." pattern in Deep Purple, Poppins Medium ~24pt. Marks position in deck.

3. **Generous margins.** Aim for 5–8% of the shorter side as outer padding. Don't go edge-to-edge.

4. **One idea per slide.** If you have 6 bullets, you probably have 2–3 slides worth of content.

5. **Body in Inter Regular at 14–18pt.** Bold for occasional emphasis only. Bullets get a bullet character + one line of breathing room each.

6. **Imagery in rounded-rectangle masks.** Corner radius ~5–8% of the shorter side. No drop shadows, no borders.

7. **The symbol as low-opacity watermark.** Optional — at 10–20% opacity in a corner of section-divider or impact slides. Never stamped large or at full opacity.

8. **Page numbers / "X / N" markers.** OK in small Inter Regular at the top-right or as part of the section-number block. Don't crowd them.

9. **No drop shadows or gradients.** Brand is flat. Cards have solid fills, period.

---

## Common mistakes

1. **Default-purple decks.** This is the most frequent failure. Putting purple on every slide is the *opposite* of the brand pattern. Default to white; reserve purple for impact.
2. **Wave on purple.** Already a strict rule (see `references/colors.md`) — but worth repeating. Wave never appears on Deep Purple backgrounds.
3. **Crowding the slide.** Tightly packed bullets, small headlines, narrow margins — feels rushed and breaks the brand's airy feel.
4. **Tiny headlines.** If a headline is the same size as the body, it isn't a headline.
5. **Sharp-corner image rectangles.** All masked imagery is rounded.
6. **Adding drop shadows or glow effects.** The brand is flat.
7. **Treating section dividers like content slides.** Section dividers should be mostly empty — number, title, breathing room. They're a pause, not more content.
8. **Logo at wrong size on purple covers.** White logo bottom-right, modest scale (~1.5–2 inches wide on a 13.33-inch deck). Not a watermark, not a headline.
