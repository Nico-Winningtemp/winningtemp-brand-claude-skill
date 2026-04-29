# External Resources

The skill bundles a snapshot of brand assets. **The live source of truth lives in SharePoint** — the brand team maintains those documents and may publish updates the skill doesn't yet reflect.

When in doubt, defer to the SharePoint version.

## Contents

- SharePoint master location
- When to refer the user to SharePoint
- How to refresh this skill from SharePoint
- Brand team contacts
- Font sources and licenses
- Photography library
- Other related internal resources

---

## SharePoint master — Visual identity

**The official Visual identity document:**

```
https://winningtemp.sharepoint.com/:p:/r/sites/MarketingInternal/_layouts/15/Doc.aspx?sourcedoc=%7BF580D805-4C59-48A8-874D-24D5DCD48E6F%7D&file=Visual%20identity.pptx&action=edit&mobileredirect=true
```

**Site:** Marketing Internal (Winningtemp tenant)
**File:** `Visual identity.pptx`

This is the canonical brand guideline document. **It is NOT bundled in this repo** — the .pptx may contain unreleased campaign material and customer photography, so it stays on SharePoint only.

To work with it locally:
1. Open the SharePoint URL above and download `Visual identity.pptx`.
2. Save it as `assets/Visual-identity-source.pptx` in your local clone (the path is gitignored — won't be committed).
3. Run `python3 scripts/extract_visual_identity.py assets/Visual-identity-source.pptx` to extract theme colors, fonts, and embedded media into your local cache.

### Always go to SharePoint when:
- The user asks for the latest version of guidelines
- A discrepancy is suspected between the skill and current brand direction
- New asset variants (logos, templates) are needed beyond what the skill has
- The user is on a non-developer device and just needs to view/share
- A sign-off process requires linking to the official doc

---

## When to refer the user to SharePoint

If a user asks something like:
- "Where's the brand guideline doc?" → SharePoint URL above.
- "Has anything changed recently?" → SharePoint URL — check the version date in the doc.
- "Do you have the source AI/InDesign files?" → SharePoint (those aren't bundled in the skill).
- "I need a co-branded logo with [partner]" → SharePoint + brand team contact (below).
- "Where's the brand book PDF?" → SharePoint (the latest export should be alongside the .pptx).

Format the answer as a clickable link (in markdown):
```
[Visual identity (SharePoint)](https://winningtemp.sharepoint.com/...)
```

---

## How to refresh this skill from SharePoint

When the brand team updates the SharePoint version, the local skill snapshot will drift. To re-sync:

1. **Download the latest `Visual identity.pptx`** from SharePoint.
2. **Replace** `assets/Visual-identity-source.pptx` with the new file.
3. **Re-run the extractor:**
   ```bash
   python3 .claude/skills/winningtemp-brand/scripts/extract_visual_identity.py \
       .claude/skills/winningtemp-brand/assets/Visual-identity-source.pptx
   ```
   This re-extracts theme colors, fonts, and embedded media into the skill's `assets/`.
4. **Diff the output:** check `.extracted/summary.json` against the previous run. Update the markdown references in `references/` if values changed.
5. **Update template files** (`assets/templates/*.pptx`, `*.dotx`) if the brand team released new versions — these aren't auto-extracted.
6. **Update logos** in `assets/logos/` if the brand team published new logo files.
7. **Bump the date** in this file so teammates know when the last sync happened.

Last sync: **2026-04-29**

---

## Brand team contacts

> ⚠ **Action required:** Fill these in. The skill needs concrete people / channels for routing requests. Until updated, route through the user's marketing manager.

| Type | Contact | Channel |
|---|---|---|
| Brand manager (general questions, asset requests) | _TBD_ | _TBD (Slack #brand?)_ |
| Design team lead | _TBD_ | _TBD_ |
| Marketing operations | _TBD_ | _TBD_ |
| Co-branding / partner logo approvals | _TBD_ | _TBD_ |
| Photography commissioning | _TBD_ | _TBD_ |

To update: edit this file and commit.

---

## Font sources and licenses

| Font | Source | License | Local copy |
|---|---|---|---|
| **Poppins** | [Google Fonts](https://fonts.google.com/specimen/Poppins) | SIL Open Font License (OFL) — see `assets/fonts/Poppins/OFL.txt` | `assets/fonts/Poppins/` (18 .ttf files) |
| **Inter** | [Google Fonts](https://fonts.google.com/specimen/Inter) | SIL Open Font License (OFL) | `assets/fonts/Inter/` (18 .otf files) |

Both fonts are free for commercial use under OFL. They can be redistributed as long as the license file is preserved (which is why `OFL.txt` is bundled with Poppins).

Installation instructions: `assets/fonts/README.md`.

---

## Photography library

| Source | Where | Notes |
|---|---|---|
| **Approved Winningtemp image bank** | _SharePoint folder TBD_ | Pre-cleared, on-brand. Use first. |
| **Customer photography (with consent)** | _Internal asset manager TBD_ | Consent records required. |
| **Branded shoot archives** | _SharePoint TBD_ | Campaign-specific. |
| **External stock (curated)** | Death to Stock, Unsplash+, Stocksy | See `references/imagery-guidelines.md` for selection rules. |

---

## Other related internal resources

| Resource | Where | Why it matters |
|---|---|---|
| Brand book (PDF export) | SharePoint, alongside `Visual identity.pptx` | Easier to share than the .pptx |
| Sales playbook | _TBD_ | Voice/messaging examples for sales contexts |
| Customer case studies | _Marketing site / SharePoint TBD_ | Real customer language to mirror |
| Legal: trademark / IP guidelines | _TBD_ | Required reading before co-branded work |
| Brand evolution archive (old logos, deprecated assets) | _TBD_ | Reference only — never use these versions |

---

## Asking the brand team for new things

When the skill / SharePoint don't cover what you need, the request flow is:

1. **Check `references/` and `assets/` first** — most needs are covered.
2. **Check SharePoint** — newer assets may exist there.
3. **Slack #brand** (or equivalent channel — to be confirmed in Contacts above) with:
   - What you're working on (1 sentence context)
   - What you need (specific asset / variant / approval)
   - When you need it (realistic deadline)
   - Whether it's customer-facing
4. **For approval-required work** (logo modifications, co-branding, motion logos, custom illustrations), allow 2–3 business days for sign-off.

---

## Reporting issues with this skill

If the skill is wrong (stale data, missing assets, contradicting current SharePoint), open an issue in the repo or message the maintainer of `.claude/skills/winningtemp-brand/`. Include:
- What you were trying to do
- What the skill said vs. what's actually current
- Link to the SharePoint version that's correct

This keeps the skill aligned with reality over time.
