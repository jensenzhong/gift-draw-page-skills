---
name: heart-lottery-page-builder
description: Build a single-file HTML heart-shaped gift lottery page from user-provided options, gifts, and blessings. Use when Codex needs to generate or update a romantic event draw page such as Girls' Day, birthday, class surprise, holiday raffle, or themed gift selection page with clickable cards, random draw, reset, used-state fading, and a reveal modal.
---

# Heart Lottery Page Builder

Build the page from structured content, not from scratch.

## Workflow

1. Normalize the user's request into either a JSON config or a plain-text list file.
2. Prefer plain text when the user sends a quick list of options and gifts.
3. If blessings are missing, let the generator create default blessings or write stronger custom blessings before generation.
4. Save the input as `.json` or `.txt`.
5. Run `python scripts/generate_page.py --config <config-file> --output <output.html>`.
5. Open the generated HTML and make only minimal visual touch-ups if the user asks for fine positioning changes.

## Input Contract

Use either:
- the JSON schema in [references/input-schema.md](references/input-schema.md)
- the plain-text format in [references/plaintext-format.md](references/plaintext-format.md)

Required field:
- `entries`: array of objects with `option`, `gift`, and `blessing`

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
- Keep the heart layout, reveal modal, random draw, reset, and used-card state.
- Prefer not to rewrite layout CSS unless the user explicitly wants a different look.
- For 8 to 20 entries, use the generated layout directly.
- For counts outside that range, generate anyway and then inspect the page for spacing issues.

## Resources

- Template: [assets/page-template.html](assets/page-template.html)
- Example config: [assets/example-config.json](assets/example-config.json)
- Example plain text: [assets/example-input.txt](assets/example-input.txt)
- Generator: [scripts/generate_page.py](scripts/generate_page.py)
- Schema reference: [references/input-schema.md](references/input-schema.md)
- Plain-text reference: [references/plaintext-format.md](references/plaintext-format.md)
