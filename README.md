```md
# 💖 Heart Lottery Page Builder

English | [中文](#中文)

https://github.com/user-attachments/assets/bd3fa6a2-f645-41b8-99bf-4646eb58d76d

An open-source Codex/Claude Code skill and generator for creating **heart-shaped HTML gift draw pages** for birthdays, Women’s Day, Men’s Day, class events, and other celebrations. 🎁✨

---

## English

A cute and reusable skill project for building **heart-shaped gift draw pages** with a soft pink style, interactive card reveal, and a full-screen confetti celebration effect. 🎉💌

This repository includes:

- A ready-to-use demo page: `gift-draw-page-demo.html`
- A reusable skill toolkit for generating matching single-file HTML pages from your own options, gifts, and blessings

Good for:

- Women’s Day gift draws 🌸
- Birthday surprise pages 🎂
- Class event raffles 🎊
- Holiday interaction pages 🎈
- Any lightweight page where users pick an option and reveal a matching gift or message 💝

### ✨ Features

- Single-file HTML output
- Heart-shaped card layout
- Reveal modal for each card
- Full-screen confetti celebration on reveal
- Random draw support
- Reset support
- Used cards automatically fade and show status
- Generate pages from plain text or JSON
- Can be used as a Codex skill or Claude Code skill
- Fully open source

### 📁 Project Structure

```text
.
├─ README.md
├─ LICENSE
├─ demo_vedio.mp4
├─ showcase.png
├─ gift-draw-page-demo.html
└─ gift-draw-page/
   ├─ SKILL.md
   ├─ agents/
   │  └─ openai.yaml
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

### 🚀 Quick Start

#### 1. Use the demo page

Open:

```text
gift-draw-page-demo.html
```

This is the finished demo page and can be used directly or further customized.

#### 2. Generate a new page

The generator supports:

- JSON input
- Plain-text input

Example:

```bash
python gift-draw-page/scripts/generate_page.py \
  --config your-input.txt \
  --output your-page.html
```

PowerShell example:

```powershell
python .\gift-draw-page\scripts\generate_page.py `
  --config .\gift-draw-page\assets\example-input.txt `
  --output .\my-lottery.html
```

### 📝 Plain-Text Input

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

- `gift-draw-page/references/plaintext-format.md`
- `gift-draw-page/references/input-schema.md`

### 🧩 Use as a Codex Skill

Install `gift-draw-page` into:

```text
~/.codex/skills/gift-draw-page
```

Restart Codex after installation.

Then you can use prompts like:

```text
Use gift-draw-page to create a lottery page.

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

### 🤖 Use as a Claude Code Skill

Copy the `gift-draw-page` folder from this repository into:

```text
~/.claude/skills/gift-draw-page
```

Then restart Claude Code.

Inside Claude Code, you can invoke it with:

```text
/gift-draw-page
```

Or prompt it like this:

```text
/gift-draw-page Create a heart-shaped gift draw page.

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

This skill guides Claude Code to:

- Prefer the bundled `gift-draw-page/scripts/generate_page.py` generator
- Reuse the template and reference files already in the repository
- Make incremental edits when updating an existing page
- Preserve the single-file HTML output, heart layout, random draw, reset, used-card behavior, and the full-screen confetti celebration effect

### 🎀 Default Output Includes

- Soft pink event-page styling
- Heart-shaped option layout
- Centered reveal modal
- Full-screen confetti celebration effect
- Random pick button
- Used-card state
- Reset support
- Single-file output for easy sharing

### 📄 Open Source

This project is released under the MIT License.

You are free to use, modify, distribute, and adapt it for personal, school, or commercial use, as long as the license text is preserved.

---

## 中文

这是一个可爱又可复用的开源 **Codex / Claude Code skill + 页面生成器**，用来创建 **爱心形状礼物抽选页**。它带有柔和粉色风格、点击揭晓弹窗，以及全屏礼炮庆祝效果。🎀🎉

仓库包含两部分：

- 一个可以直接打开使用的演示页面：`gift-draw-page-demo.html`
- 一套可复用的 skill 生成资源，可根据你提供的选项、礼物和祝福语生成同风格的单文件 HTML 页面

适合场景：

- 女生节礼物抽选 🌷
- 生日惊喜抽奖 🎂
- 班级活动抽奖 🎊
- 节日互动页 🎈
- 任何“选一个选项，再揭晓对应礼物或祝福”的轻量活动页面 💌

### ✨ 功能特点

- 单文件 HTML，打开即用
- 爱心形状选项布局
- 点击卡片弹出礼物揭晓弹窗
- 礼物揭晓时带全屏礼炮庆祝效果
- 支持随机抽取
- 支持刷新重置
- 已抽过的卡片自动变淡并显示状态
- 支持从纯文本或 JSON 自动生成新页面
- 可作为 Codex skill 或 Claude Code skill 使用
- 完全开源

### 📁 项目结构

```text
.
├─ README.md
├─ LICENSE
├─ demo_vedio.mp4
├─ showcase.png
├─ gift-draw-page-demo.html
└─ gift-draw-page/
   ├─ SKILL.md
   ├─ agents/
   │  └─ openai.yaml
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

### 🚀 快速开始

#### 1. 直接使用演示页面

打开：

```text
gift-draw-page-demo.html
```

这是当前已经做好的演示页，可以直接展示或继续修改。

#### 2. 通过生成器创建新页面

生成器支持两种输入方式：

- JSON
- 纯文本

示例命令：

```bash
python gift-draw-page/scripts/generate_page.py \
  --config your-input.txt \
  --output your-page.html
```

Windows PowerShell 示例：

```powershell
python .\gift-draw-page\scripts\generate_page.py `
  --config .\gift-draw-page\assets\example-input.txt `
  --output .\my-lottery.html
```

### 📝 纯文本输入格式

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
2. 水杯
3. 陶瓷杯
```

如果没有提供祝福语，生成器会自动补默认祝福。

你也可以写成一行一个条目的形式：

```text
标题：女生节心愿礼物抽选

条目：
1. 喜欢开盲盒 | 猫猫情绪盲盒 | 愿你拆开的每一次惊喜，都带来一点亮晶晶的小幸运。
2. 老是忘记喝水 | 水杯
3. 想要最真挚的祝福 | 陶瓷杯
```

更完整的格式说明见：

- `gift-draw-page/references/plaintext-format.md`
- `gift-draw-page/references/input-schema.md`

### 🧩 作为 Codex Skill 使用

把 `gift-draw-page` 安装到：

```text
~/.codex/skills/gift-draw-page
```

安装后重启 Codex。

然后可以直接这样使用：

```text
使用 gift-draw-page 帮我生成一个抽选页面。

标题：女生节心愿礼物抽选

选项：
1. 喜欢开盲盒
2. 老是忘记喝水
3. 想要最真挚的祝福

礼物：
1. 猫猫情绪盲盒
2. 水杯
3. 陶瓷杯
```

### 🤖 作为 Claude Code Skill 使用

把仓库中的 `gift-draw-page` 文件夹复制到：

```text
~/.claude/skills/gift-draw-page
```

然后重启 Claude Code。

在 Claude Code 中可以直接输入：

```text
/gift-draw-page
```

或者直接这样描述需求：

```text
/gift-draw-page 帮我生成一个爱心形状礼物抽选页。

标题：女生节心愿礼物抽选

选项：
1. 喜欢开盲盒
2. 老是忘记喝水
3. 想要最真挚的祝福

礼物：
1. 猫猫情绪盲盒
2. 水杯
3. 陶瓷杯
```

这个 skill 会引导 Claude Code：

- 优先复用 `gift-draw-page/scripts/generate_page.py`
- 优先使用仓库内已有模板和参考格式
- 修改现有页面时做增量调整，而不是整页重写
- 保持单文件 HTML、爱心布局、随机抽取、重置、已抽状态，以及全屏礼炮庆祝效果

### 🎀 默认输出包含

- 柔和粉色活动页风格
- 爱心形状选项布局
- 居中礼物揭晓弹窗
- 全屏礼炮庆祝效果
- 随机抽取按钮
- 已抽状态
- 重置功能
- 单文件输出，便于直接分享

### 📄 开源说明

本项目基于 MIT License 开源。

你可以自由使用、修改、分发和二次创作，包括个人项目、班级活动和商业用途，但请保留原始许可证文本。
```
