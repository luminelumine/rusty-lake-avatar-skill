---
name: rusty-lake-avatar
description: Turn an attached portrait into one square, strongly stylized Rusty Lake group avatar using a verified game scene, canonical wardrobe, and user-selected characters or motifs while retaining only the person's most recognizable human traits. Use for personal-photo avatar requests, not generic gothic or surreal illustrations without a portrait.
---

# Rusty Lake Avatar

Create a polished, fan-made 1:1 avatar from the user's portrait. It must look like a character frame from a Rusty Lake game, not a realistic portrait with a themed background. The result must also use canonical world elements; visual style alone is not enough.

## Required input

- Require at least one portrait of the person. If none is attached or accessible, ask the user to attach one before generating.
- If several people appear and the intended subject is unclear, ask which person to use.
- Treat the portrait as the identity reference and edit target. Treat any supplied game screenshot as a scene reference, not as part of the person's identity.
- Inspect local image files with `view_image` before using them. Label the role of every image in the generation prompt.

## Opening choices

Before researching or generating, collect the setup through three separate questions in three turns. Ask only the next unanswered question and wait after each one:

1. Which Rusty Lake or Cube Escape game should supply the scene skeleton?
2. Which characters should pose with the user?
3. Which environmental elements or props should appear?

Use the exact menus in [references/scene-and-prompt-guide.md](references/scene-and-prompt-guide.md). In every menu, print choices `1` through `10` vertically, one choice per line, followed by `11. 随机`; never compress them into a slash-separated sentence. Tell the user they may reply with only the number, and accept comma- or punctuation-separated numbers for multi-select questions. Use `11` as the sole displayed numeric code for `随机` / `auto`; never display or suggest `0` as an alias. Accept free-form input for choices outside the menu. After the user chooses a game, randomly select one verified scene from that game unless they also name an exact scene. Do not silently answer any category the user did not answer or mark `auto`.

## Defaults

- Produce exactly one final image, not a contact sheet or set of alternatives.
- Use a square 1:1 canvas suitable for an avatar.
- Make the person's face the dominant focal point with a medium head-and-shoulders or bust crop matching the approved reference scale. Target the full head silhouette, including hair, at roughly 50–65% of canvas height and the visible facial oval at roughly 38–48%. Do not push the facial oval past 50% unless the user explicitly asks for a tighter close-up.
- Keep the person human and recognizable from a few signature traits. Never replace their head or face with an animal head.
- Use [assets/face-color-reference.png](assets/face-color-reference.png) as the fixed skin-plane color reference for every generated person. Its canonical unshadowed base color is median RGB `219, 197, 175` (`#DBC5AF`). Apply it consistently to every visible area of human skin—face, ears, neck, chest, arms, and hands—not only the face. State this exact value in the generation prompt; do not reinterpret it as generic ivory, white, pink, beige, or a color sampled from the portrait or scene. Allow only sparse hard-edged game-style shadows over this base. Preserve identity and ethnicity through facial geometry, hair, and other visible anchors rather than photographic pigmentation.
- Freely change pose and expression to fit the selected scene. Unless the user requests another mood or gaze direction, give the person the weary, emotionally drained expression used by many Rusty Lake characters while looking directly at the viewer.
- Replace the source clothing by default with a randomly selected, verified Rusty Lake character outfit that fits the scene and the subject's stated or apparent gender presentation. Use explicit user-provided gender information first. If the photo clearly presents as feminine, choose clothing worn by a female character; if it clearly presents as masculine, choose clothing worn by a male character. If presentation is unclear or nonbinary, use a verified gender-neutral outfit or ask instead of guessing. Respect an explicit outfit or cross-gender styling choice.
- Use one verified game setting and the characters/elements selected during the opening choice.
- Include at least five visually distinct, canonically verified Rusty Lake cues besides the user's identity. This minimum is an unconditional default, not a menu choice: if the user's selections provide fewer than five, automatically add compatible, scene-native cues until the total reaches five, without asking another question or mixing unrelated locations.
- Match the verified game's line economy as well as its layout. Keep foreground and background props simpler than the face: broad flat fills, one strong outer contour, and only a few functional interior lines. Do not add dense brick seams, grass hatching, wood grain, stone speckling, mountain texture, or other decorative micro-detail absent from the canonical screenshot.
- Keep adult, non-chibi neck and shoulder construction even though the avatar uses a large close crop.

## Canonical scene gate

Before writing the image prompt, read [references/scene-and-prompt-guide.md](references/scene-and-prompt-guide.md).

Verify that the backdrop, selected characters, requested props, and chosen outfit exist in a released Rusty Lake or Cube Escape game. Search for an official screenshot, press-kit image, official walkthrough/trailer frame, or other reliable visual reference. Prefer official Rusty Lake sources; do not treat fan art, AI images, or moodboards as proof of canonical design.

Record the game title, scene cue, wardrobe source, character/prop references, and a checklist of at least five distinct canonical cues internally before generation. Reconstruct the verified setting in the new illustration; do not paste or reuse screenshot pixels. Do not combine architecture from several unrelated rooms or invent a new location and call it canonical.

Every user-selected named character or animal needs its own verified appearance reference. A scene screenshot containing a different person or animal does not verify the selected character and must not be used as a substitute. When Harvey is selected, always include [assets/harvey-reference.png](assets/harvey-reference.png) as the dedicated appearance reference and describe him as a green parrot with an olive-green head and torso, darker green wings and long tail, a large hooked charcoal beak, and a white eye ring. Never describe or render Harvey as the small brown passerine seen at the barred window in `The White Door`.

If a credible scene reference cannot be found after a focused search, do not invent the background. Ask the user for a game/room choice or a screenshot.

## Stylization, identity, and composition

Prioritize the Rusty Lake character design over photographic fidelity. Preserve only 3–5 strongest identity anchors visible in the portrait, such as:

- face silhouette or one distinctive facial proportion;
- hairstyle, hairline, or facial hair;
- characteristic eye, brow, nose, or mouth shape;
- glasses, jewelry, freckles, scars, or another signature detail;
- approximate age.

Do not preserve realistic skin tone or texture, detailed lighting, the exact expression, the exact pose, or the original clothes. Use the fixed `#DBC5AF` base face plane from `assets/face-color-reference.png`, spare black outlines, simplified features, and rigid illustrated anatomy like the supplied game-character references. The unshadowed face fill must remain stable across scenes and people. Default to large white almond/round eyes with small round pupils about 1.5–2 times the diameter of the franchise's classic tiny-dot pupils; keep the pupils clearly smaller than the eye whites. Very small bean/dot eyes under short lid lines remain an option only when the user explicitly requests them. Never use realistic iris rendering, pupils that dominate the eye, wet highlights, or glossy photographic eyes. Divide the hair into solid locks and add clearly visible black contour and interior strand lines that follow those locks. Keep the closed mouth pale gray or nearly the same color as the face, defined mostly by a thin line; do not use red or saturated pink lip fill. Default to heavy upper eyelids, slightly raised inner brows, direct eye contact with the viewer, a flat or downturned mouth, a long still face, lowered shoulders, and restrained body language. The mood should feel tired, lonely, and quietly defeated rather than cute, glamorous, cheerful, or theatrically tearful.

Compose for avatar readability rather than full-body staging. Use the approved medium-close scale: the whole head silhouette is prominent, while the visible facial oval stays around 38–48% of the square's height so surrounding lore remains legible. Show enough neck, shoulders, and upper chest to preserve adult anatomy; the crop must not become chibi, bobblehead, doll-like, a floating head, or an extreme beauty close-up. Keep supporting cast and lore props smaller and behind or beside the face.

Selected black shadow figures, animal-headed figures, Harvey, and the dog may pose beside or behind the person as group-photo participants. Keep them as separate characters: they must not replace the user's head, obscure the user's signature traits, or merge into the user.

## Generate

Use the built-in image generation tool by default. This is a strong style transfer with loose identity preservation. Include the user's portrait and, when available, verified scene, character, and outfit screenshots as clearly labeled references according to the image tool's input conventions.

Build a concise structured prompt from the template in the scene guide. State the 3–5 identity anchors and the canonical scene anchor explicitly. Ask for a square composition and one image. Do not request text, logos, interface chrome, or watermarks.

Make one generation call by default. If inspection shows a critical failure—photorealistic facial modeling, source-matched natural skin tone or a yellow/beige/ochre/tan face instead of the fixed reference ivory, realistic or glossy eyes, pupils that remain at the old tiny-dot scale or dominate the eye, gaze that does not meet the viewer by default, hair without visible black interior lines, saturated red/pink lips, cheerful/glamorous expression, an extreme close-up with the visible facial oval over half the canvas height, a face too small to remain the focal point, fewer than five distinct canonical cues, chibi anatomy, non-square output, all identity anchors lost, gender-incongruent canonical clothing without a user request, original clothing retained without a user request, an animal head replacing the user, an invented/mixed background, foreground or background linework substantially denser than the verified screenshot, or omitted user-selected content—make at most one focused corrective edit and deliver only the best final image.

## Validate and report

Before finishing, verify visually and run the numeric skin-color gate from [scripts/validate_face_color.py](scripts/validate_face_color.py). Select at least two clean, unshadowed rectangles per generated human, including one face sample and one sample from another visible skin area when available; avoid eyes, hair, outlines, clothing, mouth, and shadow shapes. The command must exit successfully with the default maximum per-channel tolerance of 6 before delivery. If it fails, use the single allowed corrective image edit and check again. If the corrective edit still misses only the color invariant, run [scripts/normalize_skin_color.py](scripts/normalize_skin_color.py) once on explicit human-skin regions, then rerun the numeric gate. This deterministic fallback may change color only: do not use it to repair composition, identity, anatomy, or character errors. If the normalized result still fails or affects non-skin content, do not deliver the image as valid.

Before finishing, verify:

- the output is square and only one final image is presented;
- the subject looks like a flat, simplified Rusty Lake game character rather than a realistic painted portrait;
- 3–5 signature traits still connect the human subject to the attached person;
- every generated human has all visible unshadowed skin planes matching `#DBC5AF` from `assets/face-color-reference.png`, and the numeric validator passes for every sampled rectangle;
- the eyes default to large whites with small round pupils about 1.5–2 times the classic tiny-dot diameter, with no glossy realism or eye-dominating pupils; bean/dot eyes appear only when requested;
- the hair contains visible black contour and interior strand lines, and the mouth remains pale and low-saturation without red or pink lip fill;
- the unobstructed face is the dominant focal point at the approved medium-close scale: full head silhouette about 50–65% and visible facial oval about 38–48% of canvas height;
- the default expression is visibly weary and emotionally drained, with direct eye contact and restrained body language, unless the user chose another mood or gaze direction;
- the close crop retains adult neck-and-shoulder anatomy without chibi or bobblehead distortion;
- expression and pose fit the scene, regardless of whether they match the photo;
- clothing comes from a verified Rusty Lake character and matches the subject's stated or apparent gender presentation unless the user requested otherwise;
- the selected setting is identifiable from the verified reference rather than merely matching a color palette;
- close scene elements use broad flat fills and sparse functional lines; their brick, grass, wood, stone, and mountain detail is no denser than the verified screenshot and remains visually subordinate to the face;
- every user-selected character and element is present, visually distinct, and matches its own verified appearance reference; Harvey must read unmistakably as the bundled green parrot, never as a generic brown bird;
- at least five distinct canonical Rusty Lake cues are clearly visible and can be named individually;
- there is no accidental text, logo, watermark, collage seam, or extra face.

Render the result inline. Briefly name the game and scene used, identify the borrowed character outfit, list the included universe elements, and link the sources used to verify them when web research was needed. State that the scene and designs were redrawn from references rather than directly composited.
