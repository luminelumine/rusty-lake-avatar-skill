# Canonical scene and prompt guide

Use this guide for every avatar request after inspecting the portrait.

## Three-turn opening interview

Ask these as three separate turns, not one combined questionnaire. Ask only the next unanswered question, then stop and wait. Every question must show the ten primary choices vertically as `1.` through `10.`, one option per line, followed by `11. 随机`. Tell the user that a bare number is a complete answer; for multi-select menus, accept forms such as `2, 5, 10`, `2 5 10`, or `2、5、10`. Use `11` as the only displayed numeric code for random selection; never display, suggest, or later reinterpret random as `0`. Keep free-form input available beneath the numbered list.

### Question 1 — game

```text
第 1 个问题：你希望从哪一部游戏里随机抽取场景作为构图骨架？回复一个序号即可。
1. Samsara Room
2. Cube Escape: Paradox
3. Cube Escape: Birthday
4. Cube Escape: Seasons
5. Cube Escape: The Lake
6. Rusty Lake Hotel
7. Rusty Lake: Roots
8. Rusty Lake Paradise
9. The White Door
10. Underground Blossom
11. 随机
其他：直接输入游戏名
```

The user chooses a game, not a generic location. Afterward, research that game and randomly select one visually distinctive, verified scene from it. If the user voluntarily names an exact room or chapter, use that as an override.

### Question 2 — cast

```text
第 2 个问题：你想和哪些角色合影？可以多选，直接回复序号，例如：2, 5, 10。
1. Dale Vandermeer
2. Laura Vanderboom
3. Mr. Owl
4. Mr. Crow
5. Harvey
6. Rose Vanderboom
7. Albert Vanderboom
8. William Vanderboom
9. Robert “Bob” Hill
10. Corrupted Soul（黑影人）
11. 随机
不需要角色：回复“无”
其他：直接输入名字
```

These ten are the default major-character menu, not an exhaustive canon list. Accept any other named character, including Mr. Rabbit, Mr. Deer, other Hotel guests, Vanderboom or Eilander family members, and ordinary animals. Interpret a casual `Dave` as likely `Dale Vandermeer`, but confirm only if context makes the intended character genuinely ambiguous.

### Question 3 — elements

```text
第 3 个问题：你希望画面里出现哪些锈湖元素？可以多选，直接回复序号，例如：1, 4, 9。
1. 黑方块
2. 白方块
3. 蓝方块
4. 落地钟
5. 花树或生命树
6. 月亮或血月
7. 锈湖湖面
8. 猫头鹰面具
9. 老式电话
10. 电梯或地铁列车
11. 随机
其他：直接输入
```

Accept multiple selections and free-form canonical props. For `11` / `随机`, choose only items compatible with the chosen game and scene. Every image must contain at least five distinct canonical cues as an unconditional default. Do not present this minimum as a selectable option and do not ask whether the user wants it. If the user's chosen elements, setting, wardrobe, cast, and props total fewer than five countable cues, automatically add the least intrusive compatible cues from the same scene until the total reaches five. For example, if the user selects only items `1, 2, 3`, add two compatible scene-native cues automatically. Recommend no more than three accompanying characters and three freestanding props, using the canonical setting and wardrobe to reach the minimum without clutter. If the user asks for no extras, explain that this skill still retains the minimum five scene-native cues.

## Scene selection

After all three questions are answered, apply this priority order:

1. Search only within the chosen game for the scene skeleton, unless the user explicitly permits cross-game scenery.
2. Randomly choose one verified, visually distinctive scene from that game; use an exact room/chapter if the user named one.
3. Fit the chosen cast and elements into that scene while preserving its recognizable architecture, landscape, furniture, and primary prop arrangement.
4. For categories marked `auto`, select compatible characters/elements only after the scene is fixed.
5. Build a five-item minimum checklist and add unobtrusive, scene-native cues until it is satisfied.

Search by exact game title plus a concrete scene term. Prefer these source classes:

1. Official Rusty Lake game pages, press kit, blog, walkthroughs, trailers, and official video frames.
2. Official store screenshots.
3. A clearly labeled gameplay screenshot or walkthrough frame from a reputable secondary source.

Useful official starting points include `rustylake.com`, `press.rustylake.com`, and the official Rusty Lake YouTube channel. Use image search when it is the fastest way to compare candidate scenes. Never use fan art or another generated image as the sole canonical reference.

Before generation, be able to fill in both fields:

- `Game`: exact title.
- `Scene anchor`: a short concrete description that distinguishes the location, such as the Hotel lobby, a named guest room, the Vanderboom family tree view, or a specific clock room.

Avoid a generic "Rusty Lake room" label. If the source does not establish a specific place, keep searching or ask the user for a reference.

## Approved element palette

Choose only elements that remain coherent with the verified scene.

| Role | Available elements | Use rule |
|---|---|---|
| Background anchors | the lake, Rusty Lake Hotel, a grandfather clock, the flowering tree, the moon | Use only when the chosen screenshot establishes the setting or prop. Preserve the recognizable layout and main silhouettes. |
| Supporting figures | a black shadow figure / Corrupted Soul; Mr. Crow; Mr. Owl; Mr. Rabbit; Mr. Deer | Keep canonical silhouettes, clothing cues, and proportions. Place in the middle or far background as a quiet witness or cameo. |
| Supporting animals | the long-lived dog; Harvey the parrot | Use as a small companion or Easter egg. Do not make the animal compete with the face. |

### Minimum-five counting rule

Count at least five concrete, separately visible canonical cues besides the user's identity. Eligible cues are:

- one verified location/background anchor;
- one recognizable canonical outfit;
- each selected canonical character or animal;
- each distinct canonical prop or motif.

Do not count the art style, color palette, generic floral texture, mood, lighting, or repeated copies of one object as separate cues. Before generation, list the five or more items internally. If the user's requested cast and props do not reach five, add the least intrusive compatible cues from the same game and scene. Prefer a balanced set such as one location, one outfit, one companion, and two or three props.

Include all requested elements, but do not import a famous character or prop if it clashes with the chosen scene. Meet the five-item minimum with compact peripheral staging rather than turning the avatar into a crowded lore collage.

The background must remain one real game location. Because the output is an avatar, crop that location tightly behind the face and retain only its strongest identifying architecture, furniture, palette, and props. Compatible characters may be newly staged as small companions or cameos, but they must not compete with the face.

Match the source screenshot's economy of line. Simplify close scenery into broad flat shapes with one outer contour and only the structural lines needed to identify it. Do not embellish masonry with dense brick-by-brick texture, fill grass with hatching, add repeated wood grain, stipple stone, or over-render distant mountains. Environmental detail must remain sparser than the subject's facial and hair linework.

## Canonical wardrobe

Replace the source clothes unless the user asks to keep them. Randomly choose one recognizable outfit worn by a verified Rusty Lake or Cube Escape character and compatible with the scene's period, mood, and the subject's stated or apparent gender presentation.

Use this priority order:

1. Follow gender or clothing preferences explicitly stated by the user.
2. If the portrait clearly presents as feminine, choose clothing worn by a female character; if it clearly presents as masculine, choose clothing worn by a male character.
3. If the presentation is ambiguous, mixed, or nonbinary, use a verified gender-neutral outfit or ask a short question instead of assigning a gender.

Treat visual presentation only as a wardrobe-selection cue, not as a claim about the person's gender identity. Do not put a feminine-presenting subject in a male character's outfit or a masculine-presenting subject in a female character's outfit unless the user explicitly requests cross-gender styling. The wearer may be animal-headed in canon; transfer only the clothing, never the animal head.

Verify the outfit from a screenshot before prompting. Preserve its key silhouette, collar, layers, major colors, and one or two defining details. Avoid mixing pieces from several characters or inventing generic Victorian clothing and calling it canonical. If no compatible outfit can be verified, ask the user to choose a character whose clothes should be used.

## Visual treatment

Translate the portrait into the franchise's restrained 2D point-and-click character language. The character-model look is a hard requirement:

- flat color fills bounded by visible, slightly irregular black outlines;
- the fixed low-saturation neutral-to-slightly-pink light-ivory face plane shown in [../assets/face-color-reference.png](../assets/face-color-reference.png), with almost no modeled volume and chosen independently of the source portrait's skin tone; never allow the face to shift toward yellow, beige, ochre, or tan;
- default to large white almond/round eyes with small round pupils about 1.5–2 times the diameter of the classic tiny-dot pupils, while keeping the pupils clearly smaller than the eye whites; use small bean/dot eyes beneath short horizontal lid marks only when the user explicitly requests them; keep the iris minimal or absent and never paint realistic glossy eyes;
- sparse lashes, short graphic brows, and a narrow simplified nose;
- a closed, thin-line mouth in pale gray, ivory, or near-skin color; no lipstick effect, red fill, saturated pink, wet highlight, or realistic lip volume;
- hair grouped into a few solid locks with a strong black outer contour and clearly visible black interior strand/groove lines following the direction of each lock;
- at most a few hard-edged shadow or blush shapes—no soft airbrushed gradients;
- stiff, front-facing or minimally angled anatomy with simplified neck, shoulders, hands, and clothing folds;
- muted brown, ochre, olive, cream, gray, and black palette derived from the selected screenshot;
- frontal or minimally angled staging, slightly rigid poses, sparse theatrical lighting, and unsettling stillness;
- lightly aged paper, painted-wall, wood, or fabric texture where present in the reference;
- subdued macabre tension rather than gore, comedy, glossy fantasy art, or cinematic photorealism.

Derive environment color and lighting from the chosen screenshot instead of applying one universal palette to every game, but keep the subject's face fixed to the reference ivory even when the portrait or environment has a different color cast. Preserve ethnicity through proportions, facial geometry, and hair rather than realistic skin color. Explicitly reject yellow or beige facial grading, realistic skin texture, pores, subsurface glow, glossy photographic eyes, large iris/pupil rendering, detailed eyelashes, saturated lips, smooth digital-painting gradients, cinematic depth of field, and portrait-photography lighting.

## Default expression and posture

Unless the user asks for a different emotion, use the drained, melancholy character acting seen in the supplied ensemble reference:

- heavy, lowered upper eyelids and small restrained pupils about 1.5–2 times the classic tiny-dot diameter;
- inner ends of the brows subtly raised, with the outer ends level or slightly lowered;
- gaze directed straight at the viewer by default, while the heavy lids and brows preserve the drained mood;
- mouth closed, pale, and flat or gently downturned, never smiling and never filled red or saturated pink;
- face held still, with minimal cheek animation and no beauty-pose tension;
- neck slightly forward, shoulders lowered, arms resting or hanging with little energy;
- emotional register: exhausted, lonely, resigned, and numb—not crying, screaming, comic, sulky-cute, or glamorous.

If a supplied portrait smiles, do not preserve the smile by default. Expression is not an identity anchor.

## Avatar framing lock

- Use a medium head-and-shoulders or bust crop by default. The face must be the unmistakable subject, not one figure inside a room illustration, while enough background remains to show the required lore cues.
- Match the approved reference scale: target the full head silhouette, including hair, at roughly 50–65% of canvas height and the visible facial oval from chin to hairline/brow region at roughly 38–48%.
- Do not enlarge the visible facial oval beyond 50% of canvas height unless the user explicitly requests an extreme close-up.
- Keep both eyes, nose, mouth, face outline, and signature hair cues unobstructed and legible at small icon size.
- Preserve adult neck width, shoulder slope, and upper-chest scale. The close crop may be large, but it must not look chibi, bobbleheaded, doll-like, mascot-like, or like a floating head.
- Crop the verified scene around the bust while preserving enough compact, unmistakable anchors to reach the five-cue minimum. Keep supporting characters and props small, peripheral, and visually subordinate.

## Identity anchors

Choose 3–5 visually strongest anchors from the photograph. Prefer features that survive simplification:

- face silhouette or one unusual proportion;
- hairstyle, fringe, hairline, or facial hair;
- a characteristic eye/brow, nose, or mouth shape;
- glasses, jewelry, freckles, scars, or another signature marker;
- approximate age.

Do not attempt a feature-by-feature likeness. Expression, gaze, pose, hand position, clothes, and skin tone may all change. Stylize aggressively by flattening planes, exaggerating the chosen anchors slightly, and discarding minor photographic detail. Preserve ethnicity through recognizable geometry and hair rather than photographic skin pigmentation; keep approximate age, and never turn the human head into an animal mask.

If the source portrait is low quality, preserve only traits that are actually visible. Do not invent distinctive facial features.

## Prompt template

Use only the lines that help the current request:

```text
Use case: style-transfer
Asset type: personal square avatar
Primary request: redraw the person in Image 1 as a strongly simplified Rusty Lake game character posing with the selected cast
Input images: Image 1 is the loose identity/edit target; later images, if present, are verified references for scene, cast, and wardrobe
Canonical source: <exact game title> — <scene anchor>
Scene/backdrop: faithfully redraw the recognizable layout, architecture, major furniture/landscape silhouettes, palette, and lighting of the verified scene; match its sparse line density with broad flat shapes, strong outer contours, and only essential structural interior lines; do not paste source pixels or add decorative micro-texture absent from the screenshot
Subject: one human character derived from Image 1; keep only <3–5 signature anchors>; expression and pose may change
Wardrobe: replace source clothes with <verified canonical character outfit and defining details>
Group cast: <user-selected characters, arranged beside or behind the subject without merging>
Environmental elements: <user-selected canonical props or motifs>
Canonical cue checklist: <name at least five separately visible items: location, wardrobe, cast, and props>
Style/medium: hard-flat 2D Rusty Lake character art, irregular black contours, minimally shaded face matching the fixed low-saturation neutral-pink light ivory in Image <face-color reference>; never yellow, beige, ochre, or tan; default to large white eyes with small round pupils about 1.5–2 times the classic tiny-dot diameter and still clearly smaller than the eye whites; use bean/dot eyes only if explicitly requested; narrow schematic nose; pale near-skin thin-line mouth; solid hair locks with visible black interior strand lines; rigid illustrated anatomy; lightly aged texture
Expression/posture: heavy lowered upper lids, small restrained pupils, subtly raised inner brows, direct eye contact with the viewer, pale flat or downturned closed mouth, long still face, lowered shoulders, restrained tired pose; exhausted and resigned, not smiling or theatrically sad
Composition/framing: 1:1 square avatar, medium head-and-shoulders or bust crop matching the approved reference; full head silhouette 50–65% of canvas height; visible facial oval 38–48% and never above 50% unless requested; retain adult neck and shoulder anatomy; compact peripheral cast and props
Identity anchors: retain only <specific face silhouette, hair, feature, accessory, or mark>; do not reproduce photographic detail
Constraints: user remains fully human; face matches the fixed reference ivory instead of the portrait or scene color cast; eyes follow one approved construction; hair has black internal linework; mouth has no saturated color; canonical background remains one location and no more line-dense than its verified screenshot; include every user-selected item and at least five separately visible canonical cues; no direct screenshot collage
Avoid: extreme close-up with visible facial oval over half the canvas height, face too small to dominate, fewer than five canonical cues, cheerful or glamorous expression, smile, gaze turned away from the viewer unless requested, pupils left at the old tiny-dot scale, realistic irises, glossy eyes, pupils large enough to dominate the eye whites, yellow/beige/ochre/tan face, colored lipstick, red or saturated pink lips, hair rendered as an unlined solid mass, dense brick seams, grass hatching, repeated wood grain, stone stippling, over-rendered mountains, chibi or bobblehead anatomy, floating head, semi-realistic or realistic face, soft skin shading, pores, detailed eyelashes, airbrushed gradients, photographic lighting, gender-incongruent wardrobe without user request, invented room, mixed locations, animal head on user, face obstruction, generic gothic fantasy, glossy rendering, gore, text, logo, watermark, unrequested people
Output: exactly one final image
```

Name concrete visual facts from the verified screenshot in `Scene/backdrop`; do not rely on the game title alone. Name exactly which few traits survive in `Identity anchors`; do not ask for full facial fidelity. Describe the borrowed outfit concretely rather than saying only "Rusty Lake clothes."

## Corrective pass

If a correction is necessary, change only the failed invariant. Examples:

- Identity drift: restate only the chosen 3–5 signature anchors; keep scene, wardrobe, and framing unchanged.
- Too realistic: demand flat pale facial shapes, sparse line features, solid-shape hair, rigid anatomy, and no gradients or photographic skin; keep the chosen anchors unchanged.
- Face-style drift: restore the fixed low-saturation neutral-pink light-ivory face plane from `assets/face-color-reference.png`, use large white eyes with small round pupils about 1.5–2 times the classic tiny-dot diameter, direct the gaze at the viewer, add black interior hair lines, and remove red/pink lip color; keep identity anchors, scene, wardrobe, and framing unchanged.
- Face-color drift: match the face plane to `assets/face-color-reference.png`, remove yellow/beige/ochre/tan cast and scene-color spill, and keep every other visual unchanged.
- Not melancholy enough: lower the upper eyelids without lowering the gaze, subtly raise the inner brows, keep direct eye contact, close and flatten/downturn the mouth, lower the shoulders, and remove any smile or beauty pose; keep identity anchors unchanged.
- Face too small: tighten to the approved medium-close scale—full head silhouette 50–65% and visible facial oval 38–48% of canvas height—while keeping expression, identity anchors, wardrobe, and scene cues.
- Face too large: pull back until the visible facial oval is 38–48% of canvas height, keeping the same expression, identity anchors, wardrobe, and scene cues.
- Fewer than five canonical cues: add only the missing number of compact, scene-native cues and keep the portrait scale and face unobstructed.
- Close crop looks chibi: keep the face large but restore adult neck width, shoulder slope, and upper-chest scale; remove doll-like or bobblehead distortion.
- Wrong-gender wardrobe: change only the clothing to a verified outfit worn by a character matching the subject's stated or apparent gender presentation; keep face, expression, crop, scene, and cast unchanged.
- Background drift: restate the verified room layout and landmark props; keep the subject unchanged.
- Over-detailed scenery: simplify only the environment into broad fills, outer contours, and essential structural lines matching the source screenshot; remove decorative brick, grass, wood, stone, and mountain micro-texture while keeping layout, props, subject, and canonical cues unchanged.
- Overcrowding: simplify or shrink the least important extras while retaining at least five countable canonical cues; favor the verified location, outfit, selected cast, and the clearest props.
- Animal-head error: restore the user's original human face and move the animal-headed figure into the background.

Do not use a corrective pass merely to explore another aesthetic option; the default deliverable is one image, not a variant set.
