# Icons

Winningtemp's official icon library lives in `assets/icons/black/`. There are **95 icons** in the official set, in a clean, friendly, rounded style consistent with the rest of the brand.

When generating slides, docs, or web content that needs an icon, use these instead of pulling from generic icon libraries (Lucide, FontAwesome, Material, etc.) — those will look off-brand.

## Contents

- File location and naming
- Style and characteristics
- Color rules (when to use black vs white)
- Categories (full inventory)
- Common substitutions for off-brand icon names
- Sizing guidance
- How to use in PPTX / web / docs

---

## File location and naming

```
assets/icons/
├── black/    ← 95 PNG icons (default — for use on light backgrounds)
└── white/    ← White variants (currently empty — recolor from black if needed)
```

**Naming:** human-readable English, mostly lowercase or Title Case, separated by spaces. Some have hyphens (`magnifying-glass-zoom-in.png`). When picking by name, treat case and separators loosely.

**Format:** PNG with transparent background. No SVG variants in this skill (request from brand team if vector needed).

---

## Style and characteristics

- Clean lines, soft rounded forms
- Friendly and modern character matching the brand voice
- Designed to scale well across formats (digital + print)
- Single-color (black) — recolorable in design tools or via image filters
- Consistent stroke weight across the set

These icons are designed to feel **functional first, decorative second**. They support clarity, accessibility, and consistency across all touchpoints.

---

## Color rules

- **On light backgrounds** (white, gray, light purple): use the **black** icon as-is.
- **On dark/purple backgrounds**: use a **white** version. Since the white folder is empty, recolor the black icon at use-time:
  - In Keynote / PowerPoint: use the "Recolor" picture effect → set to white
  - In Figma / Sketch: import + apply white fill
  - In CSS: use `filter: invert(1)` on the black PNG, or convert to SVG and color via `fill`
- **Never** recolor icons to non-brand colors (no rainbow palettes, no orange/teal/coral). If you want to color-code an icon, use Deep Purple `#7F2696` only.

---

## Categories (full inventory)

### Communication & feedback (16)
- Announcement, bell, Mail, New mail, paper plane
- Conversation conflict, Conversation happy, Conversation urgent, Two way conversation
- Listening, Phone, Phone calling, Phone notice
- praise, Whistle, quotation-mark

### People & teams (10)
- One person standing, Two persons standing, Three persons standing, one person, two persons, Group
- Person with tie, Person with bow tie, Profile picture
- collaboration

### Status & emotion (12)
- Smiling, Happy face, Love, Broken heart, Dissatisfied
- Thumbs up, Thumbs down
- Check, Cross, False
- Star 2, Star 2-1

### Data & analytics (12)
- Line graph, Statistics, Computer statistics, Insight
- Trend up, Trend up 2, Trend down
- Progress ring, eNPS, wave-temperature
- Refresh analytics, overview

### Tools & UI (15)
- Eye, Eye off
- Lightning, Power, Settings
- Pen, Writing, Document, Checklist, List, Text
- Image, video, presentation
- Lock

### Notifications & alerts (8)
- Notice, +100 notice, Urgent notice
- Flag 1, Flag 2, Flag 3
- Internet, Internet error

### Time & planning (5)
- clock, Calendar, Calendar error
- News, follow-ups

### Actions & navigation (10)
- Plus, Trash, check out
- Arrow up, Arrow down
- Refresh analytics, magnifying-glass-zoom-in, magnifying-glass-zoom-out
- Condense, Union

### Business & strategy (7)
- Money, work, organisation, organization-tree, training, commitment, shield

### Devices (3)
- Computer screen, Phone, paper-clip

### Decorative / shapes (3)
- Polygon 12 (Stroke), Star 2, Star 2-1

---

## Common substitutions

When you (or a user) ask for a generic icon name, map to the closest official one:

| If the request is for… | Use this Winningtemp icon |
|---|---|
| "lightbulb" / "idea" | `Insight.png` or `Lightning.png` |
| "graph" / "chart" / "trend" | `Line graph.png`, `Trend up.png`, `Statistics.png` |
| "settings" / "gear" | `Settings.png` |
| "heart" / "favorite" | `Love.png` |
| "warning" / "alert" | `Urgent notice.png`, `Notice.png`, or `Flag 3.png` |
| "thumbs up" / "approve" | `Thumbs up.png` |
| "user" / "person" | `Profile picture.png`, `one person.png`, or `Person with tie.png` (corporate context) |
| "team" / "group" | `Group.png`, `collaboration.png`, `two persons.png`, `Three persons standing.png` |
| "calendar" / "schedule" | `Calendar.png` |
| "email" / "envelope" | `Mail.png` or `New mail.png` |
| "phone" / "call" | `Phone.png` or `Phone calling.png` |
| "search" / "magnifier" | `magnifying-glass-zoom-in.png` |
| "document" / "file" | `Document.png` or `paper-clip.png` |
| "checkbox" / "tick" | `Check.png` |
| "cross" / "delete" / "X" | `Cross.png` or `Trash.png` |
| "trophy" / "win" / "achievement" | `Star 2.png` (closest available) |
| "growth" / "up arrow" | `Arrow up.png` or `Trend up.png` |
| "decline" / "down arrow" | `Arrow down.png` or `Trend down.png` |
| "lock" / "secure" / "privacy" | `Lock.png` or `shield.png` |
| "speak" / "speech bubble" | `Conversation happy.png` |
| "video call" / "meeting" | `video.png` or `presentation.png` |

---

## Sizing guidance

| Use case | Recommended size |
|---|---|
| Inline UI/web button | 16–24px |
| Standalone web/list icon | 32–48px |
| Slide bullet icon | 32–40px (PPT) |
| Hero / feature illustration | 64–128px |
| Print collateral / icon-led layout | 12–24mm depending on density |

Maintain proportional scaling. Keep at least 8px padding around the icon when placed in a button or container.

---

## How to use in PPTX (python-pptx)

```python
from pptx.util import Inches
from pathlib import Path

ICON_DIR = Path(".claude/skills/winningtemp-brand/assets/icons/black")
slide.shapes.add_picture(str(ICON_DIR / "Insight.png"), Inches(0.5), Inches(1.0), width=Inches(0.4))
```

To color-fill a black PNG icon in PPTX, set the picture's "Recolor" effect manually after generation, or pre-process the PNG with PIL:

```python
from PIL import Image
img = Image.open("Insight.png").convert("RGBA")
data = img.getdata()
new = [(127, 38, 150, p[3]) if p[3] > 0 else p for p in data]   # color → Deep Purple
img.putdata(new)
img.save("Insight-purple.png")
```

## How to use in HTML / CSS

```html
<img src=".claude/skills/winningtemp-brand/assets/icons/black/Insight.png"
     alt="Insight" class="wt-icon">
```

```css
.wt-icon { width: 24px; height: 24px; }
.wt-icon--white { filter: invert(1); }                 /* on dark backgrounds */
.wt-icon--purple {
  /* For an exact purple recolor, prefer SVG. As a quick fix: */
  filter: brightness(0) saturate(100%)
          invert(15%) sepia(99%) saturate(2647%) hue-rotate(283deg)
          brightness(85%) contrast(112%);
}
```

---

## When the icon you need isn't here

1. First check the substitution table above — there's often a close match.
2. If still no match: fall back to a clean generic icon library (Lucide preferred for similar style), but **recolor it to black `#18181B` and apply the same stroke weight** so it doesn't visually clash.
3. Long-term: request the brand team add the icon to the official library. Note it in `references/external-resources.md` for follow-up.
