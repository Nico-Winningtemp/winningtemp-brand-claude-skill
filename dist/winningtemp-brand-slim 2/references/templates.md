# Templates

Official Winningtemp templates for presentations, documents, and email signatures. Use these as the **starting point** for any branded artifact rather than building from scratch.

All templates live in `assets/templates/`.

## Inventory

| File | Format | Purpose |
|---|---|---|
| `winningtemp-presentation-template.pptx` | PowerPoint (.pptx) | Master deck template (4.5 MB). Includes branded title slide, content layouts, end-card, fonts pre-set to Poppins/Inter. |
| `winningtemp-word-template.dotx` | Word template (.dotx) | Standard Word doc template (no footer). For internal docs, briefs, plans. |
| `winningtemp-word-template-with-footer.dotx` | Word template (.dotx) | Same as above + branded footer. For external-facing docs (proposals, customer-facing reports). |
| `email-signature.docx` | Word doc (.docx) | Branded email signature template. Open, replace your details, copy into your mail client. |

---

## Presentation template (`winningtemp-presentation-template.pptx`)

### When to use
- Sales decks
- Internal all-hands / quarterly reviews
- Customer presentations
- Webinar slides
- Conference talks
- Any new deck where you'd otherwise start with a blank file

### How to use it
**Manually (in PowerPoint/Keynote):**
1. Open the template.
2. Save As → your new deck name.
3. Use the built-in slide layouts (title, content, section break, end-card).
4. Don't replace the master colors or fonts — they're pre-configured to brand spec.

**Programmatically (Python):**
```python
from pptx import Presentation

template = Presentation(".claude/skills/winningtemp-brand/assets/templates/winningtemp-presentation-template.pptx")
# Modify slides, add content, save:
template.save("my-deck.pptx")
```

The reusable script `scripts/generate_branded_pptx.py` opens this template by default — use it instead of writing PPTX-building code from scratch.

### What NOT to do
- Don't replace the title slide background with a custom photo.
- Don't change theme colors in the master (the brand colors are baked in).
- Don't switch fonts to Calibri/Aptos/Arial in the master.
- Don't add a custom footer with your name/title — that's a doc-template thing, not a deck thing.

---

## Word templates (`winningtemp-word-template.dotx`, `*-with-footer.dotx`)

### Which one to pick

| Use case | Template |
|---|---|
| Internal brief, planning doc, retrospective | `winningtemp-word-template.dotx` |
| External proposal, contract addendum, customer report | `winningtemp-word-template-with-footer.dotx` |
| Long-form whitepaper / research report | Either (footer version preferred for shareable PDFs) |

### How to use
1. Open the `.dotx` — Word will create a new untitled document based on the template (it won't overwrite the template).
2. Write content. Use the built-in styles (Heading 1 / 2 / 3 / Body) — they're pre-set to Poppins/Inter and brand colors.
3. Save As `.docx` (not `.dotx`).

### Style mapping (what's pre-set in the templates)

| Word style | Font | Size | Color |
|---|---|---|---|
| Title | Poppins Semibold | 28–32pt | Deep Purple `#7F2696` |
| Heading 1 | Poppins Semibold | 18pt | Deep Purple `#7F2696` |
| Heading 2 | Poppins Medium | 14pt | Black `#18181B` |
| Heading 3 | Poppins Medium | 12pt | Black `#18181B` |
| Body | Inter Regular | 11pt | Black `#18181B` |
| Caption | Inter Regular | 9pt | Black 70% |

If you find these styles missing or off, the template may be stale — re-download from SharePoint (see `references/external-resources.md`).

---

## Email signature (`email-signature.docx`)

### How to install (Outlook / Apple Mail / Gmail)

**Outlook (Mac/Windows):**
1. Open `email-signature.docx` in Word.
2. Replace placeholder fields: name, title, phone, etc. **Do not** alter the layout, colors, fonts, or logo placement.
3. Select the entire signature block → Copy.
4. Outlook → Preferences → Signatures → New → paste.
5. Set as default for new mail and replies.

**Apple Mail:**
1. Open the signature in Word, copy.
2. Mail → Settings → Signatures → New → paste.
3. Uncheck "Always match my default font" so the Poppins/Inter formatting holds.

**Gmail:**
1. Word's rich-text won't paste cleanly into Gmail. Either:
   - Use the official HTML signature from the brand team (request via `references/external-resources.md`), OR
   - Render the signature to an image (PNG) and paste as an image, with the email + phone as plain text below for accessibility.

### What's in the signature
- Your name
- Your title
- Phone number
- Email
- Winningtemp logo (Deep Purple, small)
- Optional: company URL or campaign link

### What to NEVER add
- Inspirational quotes
- Personal pronouns (unless the company adopts a pronouns policy and provides updated templates — until then, follow the template as-is)
- Background images
- Emoji (in branded signatures)
- "Sent from my iPhone" — strip this
- Customer logos (use only Winningtemp's)

---

## Updating templates

When the brand team releases updated templates:
1. Replace the file(s) in `assets/templates/` with the new version, keeping the same filename.
2. Re-test `scripts/generate_branded_pptx.py` against the new PPTX template — slide master changes can break programmatic generation.
3. Note the update in `references/external-resources.md` with the date.

The SharePoint location for the master templates is documented in `references/external-resources.md`.

---

## Common mistakes

1. **Starting from a blank file.** If a template exists, use it. The brand colors, fonts, and master layouts are already correct — re-creating them by hand introduces drift.
2. **Replacing master colors / fonts.** The templates are calibrated. Modifying the master breaks every slide/page based on it.
3. **Saving as `.dotx` after edits.** Save as `.docx` for documents (`.dotx` is the template format — overwriting it modifies the template itself).
4. **Pasting the email signature into Gmail without converting.** Gmail strips formatting. Use HTML or image.
5. **Ignoring the footer template** for external docs. Customer-facing PDFs without a footer feel undone.
