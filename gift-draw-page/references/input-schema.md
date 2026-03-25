# Input Schema

Create a UTF-8 JSON file with this shape:

```json
{
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
  "entries": [
    {
      "option": "休闲时刻喜欢打打麻将",
      "gift": "麻将魔方",
      "blessing": "愿你手气和脑力都在线，课业生活都能一把胡。"
    }
  ]
}
```

## Rules

- `entries` is required.
- Each entry must include non-empty `option`, `gift`, and `blessing`.
- Keep `entries` between 8 and 20 for the cleanest default heart layout.
- If the user gives only options and gifts, write blessings before running the generator.
- Omitted optional fields fall back to the template defaults.

For quick copy-paste input, prefer the plain-text format in [plaintext-format.md](plaintext-format.md).
