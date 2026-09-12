# Rusty Lake Avatar Skill

[中文说明](#中文说明) · [English](#english)

A fan-made Codex skill that turns an attached portrait into one square avatar inspired by the visual language and universe of the Rusty Lake / Cube Escape games.

The skill does more than imitate a drawing style. It asks the user to choose a game, companion characters, and lore elements; verifies a real game scene; then builds a 1:1 portrait around that scene while keeping the subject human and recognizable.

> [!IMPORTANT]
> This is an unofficial fan project. It is not affiliated with, endorsed by, or sponsored by Rusty Lake. Rusty Lake, Cube Escape, and related characters and game assets belong to their respective owners. This repository contains no official game artwork.

## 中文说明

### 它能做什么

`rusty-lake-avatar` 会把用户上传的人像照片转绘成一张 1:1 的锈湖宇宙风格头像。它会：

- 保留人物最有辨识度的 3–5 个特征，但使用扁平、克制、略显疲惫的游戏人物造型；
- 先分三轮询问场景来源游戏、合影角色和环境元素；
- 每轮把 10 个主要选项按 `1–10` 逐行列出，单选可只回复一个数字，多选可回复 `2, 5, 10`；
- 从所选游戏中查找并重绘一个可验证的真实场景，而不是凭空编造背景；
- 为人物选择符合场景与性别呈现的游戏角色服装；
- 默认生成一张正方形头像，并保证至少出现 5 个可单独辨认的锈湖元素；
- 保持人物为人脸主体，动物头人、黑影人、Harvey 等只作为陪衬或彩蛋。
- 默认使用苍白的平面肤色、极小瞳孔或豆豆眼、带黑色内部线条的块面头发，以及无明显唇色的嘴巴。

### 要求

- 支持 Agent Skills 的 ChatGPT / Codex 环境；
- 可用的图片生成或图片编辑工具；
- 能访问网络，以便核对官方场景、角色、服装和道具；
- 一张你有权使用的清晰人像照片。

### 安装

推荐直接让 Codex 的系统技能安装器从 GitHub 安装：

```text
$skill-installer 请从 https://github.com/luminelumine/rusty-lake-avatar-skill/tree/main/rusty-lake-avatar 安装这个 skill
```

也可以手动安装到用户级技能目录：

```bash
git clone https://github.com/luminelumine/rusty-lake-avatar-skill.git
mkdir -p "$HOME/.agents/skills"
cp -R rusty-lake-avatar-skill/rusty-lake-avatar "$HOME/.agents/skills/"
```

Codex 通常会自动发现新技能；如果技能没有立刻出现，请重启 Codex。

### 使用方法

1. 在新任务中上传一张人像照片。
2. 调用技能：

   ```text
   $rusty-lake-avatar 请把我附上的照片做成头像
   ```

3. 技能会逐轮问三个问题：

   - 从哪一部 Rusty Lake / Cube Escape 游戏中抽取场景；
   - 想和哪些角色合影；
   - 希望出现哪些元素或道具。

   每个问题都会把 10 个主要选项按行编号。单选直接回复一个序号，多选回复多个序号即可。

4. 回答完三个问题后，技能会核对参考素材并生成一张 1:1 头像。

完整示例：

```text
用户：$rusty-lake-avatar 请用我上传的照片生成头像
技能：第 1 个问题：你希望从哪一部游戏里随机抽取场景作为构图骨架？
用户：3
技能：第 2 个问题：你想和哪些角色合影？
用户：5
技能：第 3 个问题：你希望画面里出现哪些锈湖元素？
用户：0
```

你也可以在回答中选择 `随机`，或直接输入菜单之外的游戏、角色和元素。

### 默认输出规则

- 每次生成 1 张 PNG；
- 1:1 正方形头像；
- 人脸是画面的明确主体，同时保留足够场景信息；
- 默认使用疲惫、低落、疏离的表情；
- 默认使用苍白平面脸；眼睛采用“大眼白配极小瞳孔”或“豆豆眼”之一；头发带清晰黑色纹理线；嘴唇接近肤色；
- 人物始终保留人类面孔；
- 至少 5 个可独立识别的锈湖宇宙元素；
- 不直接拼贴官方截图，只根据核实过的参考重新绘制。

## English

### What it does

`rusty-lake-avatar` turns a portrait into a square, strongly stylized avatar grounded in a verified Rusty Lake or Cube Escape scene. It preserves a few recognizable identity anchors, uses a canonical outfit, keeps the user's face human and dominant, and adds at least five distinct lore cues.

Before generation, it asks three questions in separate turns. Each menu prints ten primary choices as a vertical `1`–`10` list, so a user can answer with a number or a comma-separated set of numbers:

1. Which game should provide the scene skeleton?
2. Which characters should join the portrait?
3. Which environmental elements or props should appear?

### Requirements

- ChatGPT or Codex with Agent Skills support;
- access to an image-generation or image-editing tool;
- web access for verifying official scenes and designs;
- a clear portrait you have permission to use.

### Install

Ask the built-in skill installer to install this GitHub path:

```text
$skill-installer Install the skill from https://github.com/luminelumine/rusty-lake-avatar-skill/tree/main/rusty-lake-avatar
```

Or install it manually:

```bash
git clone https://github.com/luminelumine/rusty-lake-avatar-skill.git
mkdir -p "$HOME/.agents/skills"
cp -R rusty-lake-avatar-skill/rusty-lake-avatar "$HOME/.agents/skills/"
```

Codex normally detects newly installed skills automatically. Restart Codex if it does not appear.

### Use

Attach a portrait, then invoke:

```text
$rusty-lake-avatar Turn my attached portrait into an avatar
```

Answer the three setup questions. The skill then verifies a scene, wardrobe, characters, and props before producing exactly one square avatar.

The character face defaults to a pale flat plane rather than the portrait's photographic skin tone. Eyes use either large whites with tiny pupils or compact bean/dot marks; hair has visible black interior strand lines; lips stay pale and nearly colorless.

### Repository layout

```text
rusty-lake-avatar/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    └── scene-and-prompt-guide.md
```

## Privacy and responsible use

Portraits are processed by whichever image tool your Codex environment provides. Review that tool's data and retention policy before using sensitive images. Only upload portraits you own or have permission to transform. Do not use the skill to impersonate, harass, or deceive people.

## Development

Validate the skill with the `quick_validate.py` script bundled with Codex's `skill-creator` system skill:

```bash
python /path/to/skill-creator/scripts/quick_validate.py ./rusty-lake-avatar
```

The skill follows the open Agent Skills directory format: a required `SKILL.md`, plus optional references and UI metadata. See the [official OpenAI skill documentation](https://developers.openai.com/codex/skills).

## License

The original instructions and configuration in this repository are licensed under the [MIT License](LICENSE). This license does not grant rights to Rusty Lake trademarks, characters, game artwork, or other third-party intellectual property.
