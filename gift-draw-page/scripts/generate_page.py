from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


DEFAULTS = {
    "eyebrow": "GIRLS' DAY SPECIAL",
    "title": "女生节心愿礼物抽选",
    "subtitle": "给你们准备了一点女生节的小惊喜。选一句最像自己的小心思，看看今天落到你手里的，会是哪一份可爱礼物。",
    "tip": "轻轻点开一张小卡片，开奖属于你的女生节惊喜。",
    "footer": "愿今天的快乐不止女生节限定，愿你们被偏爱、被惦记，也一直闪闪发光。",
    "random_button_label": "帮我随机选一个",
    "reset_button_label": "刷新重置",
    "modal_badge": "Girls' Day Lucky Draw",
    "modal_title": "礼物揭晓",
    "gift_label": "Gift",
}

PRESET_ROWS = {
    8: [2, 3, 2, 1],
    9: [2, 3, 3, 1],
    10: [2, 4, 3, 1],
    11: [2, 4, 4, 1],
    12: [2, 4, 4, 2],
    13: [2, 5, 4, 2],
    14: [2, 5, 4, 2, 1],
    15: [3, 5, 4, 2, 1],
    16: [3, 5, 4, 3, 1],
    17: [4, 5, 4, 3, 1],
    18: [4, 5, 4, 3, 2],
    19: [4, 5, 4, 3, 2, 1],
    20: [4, 5, 5, 3, 2, 1],
}

ROW_X = {
    1: [50],
    2: [38, 62],
    3: [31, 50, 69],
    4: [22, 40, 60, 78],
    5: [14, 32, 50, 68, 86],
    6: [10, 26, 42, 58, 74, 90],
}

ROW_Y = {
    4: [18, 42, 66, 84],
    5: [15, 39, 56, 72, 86],
    6: [15, 30, 46, 62, 76, 88],
}

TEXT_KEY_MAP = {
    "英文标签": "eyebrow",
    "eyebrow": "eyebrow",
    "标题": "title",
    "title": "title",
    "副标题": "subtitle",
    "subtitle": "subtitle",
    "提示": "tip",
    "tip": "tip",
    "底部文案": "footer",
    "footer": "footer",
    "随机按钮": "random_button_label",
    "random_button_label": "random_button_label",
    "重置按钮": "reset_button_label",
    "reset_button_label": "reset_button_label",
    "弹窗标签": "modal_badge",
    "modal_badge": "modal_badge",
    "弹窗标题": "modal_title",
    "modal_title": "modal_title",
    "礼物标签": "gift_label",
    "gift_label": "gift_label",
}

SECTION_ALIASES = {
    "[options]": "options",
    "options:": "options",
    "options：": "options",
    "选项:": "options",
    "选项：": "options",
    "[gifts]": "gifts",
    "gifts:": "gifts",
    "gifts：": "gifts",
    "礼物:": "gifts",
    "礼物：": "gifts",
    "[blessings]": "blessings",
    "blessings:": "blessings",
    "blessings：": "blessings",
    "祝福:": "blessings",
    "祝福：": "blessings",
    "[entries]": "entries",
    "entries:": "entries",
    "entries：": "entries",
    "条目:": "entries",
    "条目：": "entries",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a heart-shaped lottery HTML page.")
    parser.add_argument("--config", required=True, help="Path to JSON or plain-text config.")
    parser.add_argument("--output", required=True, help="Path to output HTML file.")
    parser.add_argument(
        "--template",
        default=str(Path(__file__).resolve().parents[1] / "assets" / "page-template.html"),
        help="Path to HTML template.",
    )
    return parser.parse_args()


def strip_number_prefix(text: str) -> str:
    return re.sub(r"^\s*\d+\s*[\.\、\)\]）-]*\s*", "", text).strip()


def split_entry_line(line: str) -> list[str]:
    body = strip_number_prefix(line)
    for separator in (" | ", "｜", " => ", " -> ", " —— ", " — ", " ->", " =>"):
        if separator in body:
            parts = [part.strip() for part in body.split(separator) if part.strip()]
            if len(parts) >= 2:
                return parts
    return [body]


def infer_blessing(option: str, gift: str) -> str:
    return f"愿这份{gift}替你收下今天的小惊喜，也愿关于“{option}”的小心思都被温柔回应。"


def parse_text_config(text: str) -> dict:
    config = dict(DEFAULTS)
    options: list[str] = []
    gifts: list[str] = []
    blessings: list[str] = []
    entries: list[dict] = []
    section: str | None = None

    for raw_line in text.replace("\ufeff", "").splitlines():
        line = raw_line.strip()
        if not line:
            continue

        section_name = SECTION_ALIASES.get(line.lower()) or SECTION_ALIASES.get(line)
        if section_name:
            section = section_name
            continue

        key_match = re.match(r"^(.*?)[：:]\s*(.+)$", line)
        if key_match:
            left = key_match.group(1).strip()
            right = key_match.group(2).strip()
            normalized_key = TEXT_KEY_MAP.get(left) or TEXT_KEY_MAP.get(left.lower())
            if normalized_key:
                config[normalized_key] = right
                section = None
                continue

        if section == "entries":
            parts = split_entry_line(line)
            if len(parts) == 2:
                option, gift = parts
                blessing = infer_blessing(option, gift)
            elif len(parts) >= 3:
                option, gift, blessing = parts[:3]
            else:
                raise ValueError(f"Cannot parse entry line: {line}")
            entries.append({"option": option, "gift": gift, "blessing": blessing})
            continue

        if section == "options":
            options.append(strip_number_prefix(line))
            continue

        if section == "gifts":
            gifts.append(strip_number_prefix(line))
            continue

        if section == "blessings":
            blessings.append(strip_number_prefix(line))
            continue

        parts = split_entry_line(line)
        if len(parts) >= 2:
            option = parts[0]
            gift = parts[1]
            blessing = parts[2] if len(parts) >= 3 else infer_blessing(option, gift)
            entries.append({"option": option, "gift": gift, "blessing": blessing})

    if not entries and options and gifts:
        if len(options) != len(gifts):
            raise ValueError("Options and gifts counts do not match.")
        if blessings and len(blessings) != len(options):
            raise ValueError("Blessings count must match options count when provided.")
        for index, option in enumerate(options):
            gift = gifts[index]
            blessing = blessings[index] if blessings else infer_blessing(option, gift)
            entries.append({"option": option, "gift": gift, "blessing": blessing})

    config["entries"] = entries
    return config


def load_config(path: Path) -> dict:
    raw_text = path.read_text(encoding="utf-8")
    stripped = raw_text.lstrip()
    if path.suffix.lower() == ".json" or stripped.startswith("{"):
        data = json.loads(raw_text)
    else:
        data = parse_text_config(raw_text)

    merged = {**DEFAULTS, **data}
    entries = merged.get("entries")
    if not isinstance(entries, list) or not entries:
        raise ValueError("`entries` must be a non-empty array.")

    for index, entry in enumerate(entries, start=1):
        if not isinstance(entry, dict):
            raise ValueError(f"Entry {index} must be an object.")
        for key in ("option", "gift", "blessing"):
            value = entry.get(key, "")
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"Entry {index} is missing a non-empty `{key}`.")
            entry[key] = value.strip()
    return merged


def build_rows(count: int) -> list[int]:
    if count in PRESET_ROWS:
        return PRESET_ROWS[count]

    if count < 8:
        rows = [2, max(count - 3, 1), 1]
    else:
        rows = [4, 5, 4, 3, 2, 1]
        total = sum(rows)
        while total > count:
            for i in range(len(rows) - 2, -1, -1):
                if rows[i] > 1 and total > count:
                    rows[i] -= 1
                    total -= 1
        while total < count:
            for i in range(1, len(rows)):
                if total < count:
                    rows[i] += 1
                    total += 1
    return [row for row in rows if row > 0]


def build_positions(count: int) -> list[dict[str, float]]:
    rows = build_rows(count)
    y_values = ROW_Y.get(len(rows))
    if y_values is None:
        start = 16
        step = (86 - start) / max(len(rows) - 1, 1)
        y_values = [round(start + step * i, 1) for i in range(len(rows))]

    positions: list[dict[str, float]] = []
    for row_count, y in zip(rows, y_values):
        x_values = ROW_X.get(row_count)
        if x_values is None:
            step = 72 / max(row_count - 1, 1)
            x_values = [round(14 + step * i, 1) for i in range(row_count)]
        for x in x_values:
            positions.append({"x": x, "y": y})

    return positions[:count]


def replace_once(pattern: str, repl: str, text: str) -> str:
    updated, count = re.subn(pattern, repl, text, count=1, flags=re.S)
    if count != 1:
        raise ValueError(f"Failed to replace pattern: {pattern}")
    return updated


def js_literal(value) -> str:
    return json.dumps(value, ensure_ascii=False, indent=6)


def build_html(template_text: str, config: dict) -> str:
    entries = config["entries"]
    positions = build_positions(len(entries))

    html = template_text
    html = replace_once(r"<title>.*?</title>", f"<title>{config['title']}</title>", html)
    html = replace_once(
        r'<div class="eyebrow">.*?</div>',
        f'<div class="eyebrow">{config["eyebrow"]}</div>',
        html,
    )
    html = replace_once(r"<h1>.*?</h1>", f"<h1>{config['title']}</h1>", html)
    html = replace_once(
        r'<p class="subtitle">\s*.*?\s*</p>',
        f'      <p class="subtitle">\n        {config["subtitle"]}\n      </p>',
        html,
    )
    html = replace_once(
        r'<div class="tip">.*?</div>',
        f'      <div class="tip">{config["tip"]}</div>',
        html,
    )
    html = replace_once(
        r'<button class="ghost-btn" id="randomPick" type="button">.*?</button>',
        f'      <button class="ghost-btn" id="randomPick" type="button">{config["random_button_label"]}</button>',
        html,
    )
    html = replace_once(
        r'<button class="ghost-btn secondary" id="resetPage" type="button">.*?</button>',
        f'      <button class="ghost-btn secondary" id="resetPage" type="button">{config["reset_button_label"]}</button>',
        html,
    )
    html = replace_once(
        r'<section class="footer-note">\s*.*?\s*</section>',
        f'    <section class="footer-note">\n      {config["footer"]}\n    </section>',
        html,
    )
    html = replace_once(
        r'<div class="modal-badge">.*?</div>',
        f'      <div class="modal-badge">{config["modal_badge"]}</div>',
        html,
    )
    html = replace_once(
        r'<h2 class="modal-title" id="modalTitle">.*?</h2>',
        f'      <h2 class="modal-title" id="modalTitle">{config["modal_title"]}</h2>',
        html,
    )
    html = replace_once(
        r'<div class="gift-label">.*?</div>',
        f'        <div class="gift-label">{config["gift_label"]}</div>',
        html,
    )
    html = replace_once(
        r"const entries = \[.*?\n    \];",
        "const entries = " + js_literal(entries) + ";",
        html,
    )
    html = replace_once(
        r"const positions = \[.*?\n    \];",
        "const positions = " + js_literal(positions) + ";",
        html,
    )
    return html


def main() -> None:
    args = parse_args()
    config_path = Path(args.config).resolve()
    output_path = Path(args.output).resolve()
    template_path = Path(args.template).resolve()

    config = load_config(config_path)
    template_text = template_path.read_text(encoding="utf-8")
    html = build_html(template_text, config)
    output_path.write_text(html, encoding="utf-8")
    print(f"Generated: {output_path}")


if __name__ == "__main__":
    main()
