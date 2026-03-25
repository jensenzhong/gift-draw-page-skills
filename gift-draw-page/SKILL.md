---
name: gift-draw-page
description: Build or update a single-file HTML heart-shaped gift lottery page from user-provided options, gifts, and blessings. Use when Codex needs to create or modify a romantic or celebratory interactive page such as Girls' Day, birthdays, class surprises, holiday raffles, confession pages, or themed gift selection pages with clickable cards, random draw, reset, used-card state, a reveal modal, and a full-screen confetti celebration effect.
---

# Heart Lottery Page Builder

Build from structured content and bundled resources. Do not rewrite the page from scratch unless the user explicitly asks for a different visual system.

## Workflow

1. Normalize the user's request into either a UTF-8 JSON config or a UTF-8 plain-text list file.
2. Prefer plain text when the user sends a quick list of options and gifts.
3. If the user is updating an existing page, preserve the current file and change data or template incrementally instead of rebuilding the page.
4. If blessings are missing, let the generator create defaults or write stronger custom blessings before generation.
5. Save the input as `.json` or `.txt` in the working directory and choose a concise kebab-case English output filename unless the user specifies one.
6. Run `python scripts/generate_page.py --config <config-file> --output <output.html>`.
7. Open the generated HTML and make only minimal visual touch-ups unless the user asks for a broader redesign.
8. After changing the skill, generator, or template, verify by running the generator with one bundled example input.

## Input Contract

Use either:
- the JSON schema in [references/input-schema.md](references/input-schema.md)
- the plain-text format in [references/plaintext-format.md](references/plaintext-format.md)

Required field:
- `entries`: array of objects with `option`, `gift`, and `blessing`

When the user gives separate option and gift lists, verify that their counts match before generation. Do not silently invent or drop items.

Useful optional fields:
- `eyebrow`
- `title`
- `subtitle`
- `tip`
- `footer`
- `random_button_label`
- `reset_button_label`
- `modal_badge`
- `modal_title`
- `gift_label`

If the user provides plain text, you can pass it directly to the generator without converting it to JSON first.

## Generation Rules

- Keep output as a single self-contained HTML file.
- Preserve the soft pink activity-page aesthetic from the bundled template.
- Keep the heart layout, reveal modal, random draw, reset, used-card state, and full-screen confetti celebration effect.
- Prefer data changes over template rewrites.
- Prefer not to rewrite layout CSS unless the user explicitly wants a different look.
- For 8 to 20 entries, use the generated layout directly.
- For counts outside that range, generate anyway and then inspect the page for spacing issues.
- If the user wants a new theme, copy and adapt the bundled template instead of rebuilding the interaction logic from zero.

## Resources

- Template: [assets/page-template.html](assets/page-template.html)
- Example config: [assets/example-config.json](assets/example-config.json)
- Example plain text: [assets/example-input.txt](assets/example-input.txt)
- Example generated from JSON: [assets/example-output.html](assets/example-output.html)
- Example generated from text: [assets/example-from-text.html](assets/example-from-text.html)
- Generator: [scripts/generate_page.py](scripts/generate_page.py)
- Schema reference: [references/input-schema.md](references/input-schema.md)
- Plain-text reference: [references/plaintext-format.md](references/plaintext-format.md)
