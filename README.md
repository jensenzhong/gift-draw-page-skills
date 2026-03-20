# Heart Lottery Page Builder

中文 | [English](#english)

## 中文

一个用于生成“爱心形状抽奖页”的开源小项目。

这个仓库包含两部分：

- 一个已经做好的女生节抽奖成品页
- 一个可复用的 Codex skill，可以根据你提供的选项、礼物和祝福语，自动生成同风格的单文件 HTML 页面

适合场景：

- 女生节抽礼物
- 生日惊喜抽奖
- 班级活动抽奖
- 节日互动页
- 任何“选一项，然后揭晓对应礼物或祝福”的轻量活动页面

### 功能特点

- 单文件 HTML，打开即用
- 爱心形状布局
- 点击卡片弹出开奖卡片
- 支持随机抽取
- 支持刷新重置
- 已抽过卡片自动变淡并显示状态
- 支持通过文本清单或 JSON 自动生成新页面
- 完全开源

### 项目结构

```text
.
├─ README.md
├─ LICENSE
├─ 女生节心愿礼物抽选.html
└─ heart-lottery-page-builder/
   ├─ SKILL.md
   ├─ agents/
   ├─ assets/
   │  ├─ example-config.json
   │  ├─ example-input.txt
   │  ├─ example-output.html
   │  ├─ example-from-text.html
   │  └─ page-template.html
   ├─ references/
   │  ├─ input-schema.md
   │  └─ plaintext-format.md
   └─ scripts/
      └─ generate_page.py
```

### 快速开始

#### 1. 直接使用现成页面

打开：

```text
女生节心愿礼物抽选.html
```

这是当前已经做好的成品页，可以直接展示。

#### 2. 通过生成器创建新页面

生成器支持两种输入方式：

- JSON
- 纯文本清单

示例命令：

```bash
python heart-lottery-page-builder/scripts/generate_page.py \
  --config your-input.txt \
  --output your-page.html
```

Windows PowerShell 示例：

```powershell
python .\heart-lottery-page-builder\scripts\generate_page.py `
  --config .\heart-lottery-page-builder\assets\example-input.txt `
  --output .\my-lottery.html
```

### 纯文本输入格式

如果你不想写 JSON，可以直接写成下面这种格式：

```text
标题：女生节心愿礼物抽选
副标题：给你们准备了一点女生节的小惊喜。选一句最像自己的小心思，看看今天落到你手里的，会是哪一份可爱礼物。

选项：
1. 喜欢开盲盒
2. 老是忘记喝水
3. 想要最真挚的祝福

礼物：
1. 猫猫情绪盲盒
2. 口服液水杯
3. 牛逼陶瓷杯
```

如果没有提供祝福语，生成器会自动补默认祝福。

你也可以写成更快的一行式：

```text
标题：女生节心愿礼物抽选

条目：
1. 喜欢开盲盒 | 猫猫情绪盲盒 | 愿你的惊喜感永远在线，拆开的每一天都有小确幸。
2. 老是忘记喝水 | 口服液水杯
3. 想要最真挚的祝福 | 牛逼陶瓷杯
```

更完整的格式说明见：

- `heart-lottery-page-builder/references/plaintext-format.md`
- `heart-lottery-page-builder/references/input-schema.md`

### 作为 Codex Skill 使用

如果你想把它作为 Codex skill 使用，把 `heart-lottery-page-builder` 安装到：

```text
~/.codex/skills/heart-lottery-page-builder
```

安装后重启 Codex。

然后就可以直接这样使用：

```text
用 heart-lottery-page-builder 帮我生成一个抽奖页。

标题：女生节心愿礼物抽选

选项：
1. 喜欢开盲盒
2. 老是忘记喝水
3. 想要最真挚的祝福

礼物：
1. 猫猫情绪盲盒
2. 口服液水杯
3. 牛逼陶瓷杯
```

### 输出页面默认包含

- 柔和粉色活动页风格
- 爱心形状选项布局
- 居中开奖弹窗
- 随机抽取按钮
- 已抽过状态
- 重置功能
- 单文件输出，方便直接分享

### 开源说明

本项目以 MIT License 开源。

你可以自由使用、修改、分发和二次创作，包括个人项目、班级活动和商业用途，但请保留原始许可证文本。

---

## English

An open-source project for building heart-shaped lottery pages.

This repository includes:

- A ready-to-use Girls' Day lottery page
- A reusable Codex skill that can generate a page with the same style from your own options, gifts, and blessings

Good for:

- Girls' Day gift draws
- Birthday surprise pages
- Class event raffles
- Holiday interaction pages
- Any lightweight activity page where users pick one item and reveal a matching gift or message

### Features

- Single-file HTML output
- Heart-shaped card layout
- Reveal modal for each card
- Random draw support
- Reset support
- Used cards automatically fade and show status
- Generate pages from plain text lists or JSON
- Fully open source

### Project Structure

```text
.
├─ README.md
├─ LICENSE
├─ 女生节心愿礼物抽选.html
└─ heart-lottery-page-builder/
   ├─ SKILL.md
   ├─ agents/
   ├─ assets/
   │  ├─ example-config.json
   │  ├─ example-input.txt
   │  ├─ example-output.html
   │  ├─ example-from-text.html
   │  └─ page-template.html
   ├─ references/
   │  ├─ input-schema.md
   │  └─ plaintext-format.md
   └─ scripts/
      └─ generate_page.py
```

### Quick Start

#### 1. Use the ready-made page

Open:

```text
女生节心愿礼物抽选.html
```

This is the finished demo page and can be used directly.

#### 2. Generate a new page

The generator supports:

- JSON input
- Plain-text input

Example:

```bash
python heart-lottery-page-builder/scripts/generate_page.py \
  --config your-input.txt \
  --output your-page.html
```

PowerShell example:

```powershell
python .\heart-lottery-page-builder\scripts\generate_page.py `
  --config .\heart-lottery-page-builder\assets\example-input.txt `
  --output .\my-lottery.html
```

### Plain-Text Input

If you do not want to write JSON, use a format like this:

```text
Title: Girls' Day Gift Draw
Subtitle: I prepared a little surprise for you. Pick the line that feels most like you and see which gift lands in your hands today.

Options:
1. Loves opening blind boxes
2. Always forgets to drink water
3. Wants the most sincere blessing

Gifts:
1. Cat mood blind box
2. Water cup
3. Ceramic mug
```

If blessings are omitted, the generator will create default blessings automatically.

You can also use one-line entries:

```text
Title: Girls' Day Gift Draw

Entries:
1. Loves opening blind boxes | Cat mood blind box | Hope every unboxing brings a fresh little surprise.
2. Always forgets to drink water | Water cup
3. Wants the most sincere blessing | Ceramic mug
```

More details:

- `heart-lottery-page-builder/references/plaintext-format.md`
- `heart-lottery-page-builder/references/input-schema.md`

### Use as a Codex Skill

Install `heart-lottery-page-builder` into:

```text
~/.codex/skills/heart-lottery-page-builder
```

Restart Codex after installation.

Then you can use prompts like:

```text
Use heart-lottery-page-builder to create a lottery page.

Title: Girls' Day Gift Draw

Options:
1. Loves opening blind boxes
2. Always forgets to drink water
3. Wants the most sincere blessing

Gifts:
1. Cat mood blind box
2. Water cup
3. Ceramic mug
```

### Default Output Includes

- Soft pink event-page styling
- Heart-shaped option layout
- Centered reveal modal
- Random pick button
- Used-card state
- Reset support
- Single-file output for easy sharing

### Open Source

This project is released under the MIT License.

You are free to use, modify, distribute, and adapt it for personal, school, or commercial use, as long as the license text is preserved.
