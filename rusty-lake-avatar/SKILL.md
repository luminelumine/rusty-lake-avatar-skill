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

Use the exact menus in [references/scene-and-prompt-guide.md](references/scene-and-prompt-guide.md). Each question must allow `随机` / `auto` and free-form input. After the user chooses a game, randomly select one verified scene from that game unless they also name an exact scene. Do not silently answer any category the user did not answer or mark `auto`.

## Defaults

- Produce exactly one final image, not a contact sheet or set of alternatives.
- Use a square 1:1 canvas suitable for an avatar.
- Make the person's face the dominant focal point with a medium head-and-shoulders or bust crop matching the approved reference scale. Target the full head silhouette, including hair, at roughly 50–65% of canvas height and the visible facial oval at roughly 38–48%. Do not push the facial oval past 50% unless the user explicitly asks for a tighter close-up.
- Keep the person human and recognizable from a few signature traits. Never replace their head or face with an animal head.
- Freely change pose and expression to fit the selected scene. Unless the user requests another mood, give the person the weary, downcast, emotionally drained expression used by many Rusty Lake characters.
- Replace the source clothing by default with a randomly selected, verified Rusty Lake character outfit that fits the scene and the subject's stated or apparent gender presentation. Use explicit user-provided gender information first. If the photo clearly presents as feminine, choose clothing worn by a female character; if it clearly presents as masculine, choose clothing worn by a male character. If presentation is unclear or nonbinary, use a verified gender-neutral outfit or ask instead of guessing. Respect an explicit outfit or cross-gender styling choice.
- Use one verified game setting and the characters/elements selected during the opening choice.
- Include at least five visually distinct, canonically verified Rusty Lake cues besides the user's identity. If the user's selections provide fewer than five, automatically add scene-compatible cues without mixing unrelated locations.
- Keep adult, non-chibi neck and shoulder construction even though the avatar uses a large close crop.

## Canonical scene gate

Before writing the image prompt, read [references/scene-and-prompt-guide.md](references/scene-and-prompt-guide.md).

Verify that the backdrop, selected characters, requested props, and chosen outfit exist in a released Rusty Lake or Cube Escape game. Search for an official screenshot, press-kit image, official walkthrough/trailer frame, or other reliable visual reference. Prefer official Rusty Lake sources; do not treat fan art, AI images, or moodboards as proof of canonical design.

Record the game title, scene cue, wardrobe source, character/prop references, and a checklist of at least five distinct canonical cues internally before generation. Reconstruct the verified setting in the new illustration; do not paste or reuse screenshot pixels. Do not combine architecture from several unrelated rooms or invent a new location and call it canonical.

If a credible scene reference cannot be found after a focused search, do not invent the background. Ask the user for a game/room choice or a screenshot.

## Stylization, identity, and composition

Prioritize the Rusty Lake character design over photographic fidelity. Preserve only 3–5 strongest identity anchors visible in the portrait, such as:

- face silhouette or one distinctive facial proportion;
- hairstyle, hairline, or facial hair;
- characteristic eye, brow, nose, or mouth shape;
- glasses, jewelry, freckles, scars, or another signature detail;
- approximate age and skin-tone relationship.

Do not preserve realistic skin, detailed lighting, the exact expression, the exact pose, or the original clothes. Use flat pale face shapes, spare black outlines, simplified features, and rigid illustrated anatomy like the supplied game-character references. Default to heavy upper eyelids, slightly raised inner brows, a distant or lowered gaze, a flat or downturned mouth, a long still face, lowered shoulders, and restrained body language. The mood should feel tired, lonely, and quietly defeated rather than cute, glamorous, cheerful, or theatrically tearful.

Compose for avatar readability rather than full-body staging. Use the approved medium-close scale: the whole head silhouette is prominent, while the visible facial oval stays around 38–48% of the square's height so surrounding lore remains legible. Show enough neck, shoulders, and upper chest to preserve adult anatomy; the crop must not become chibi, bobblehead, doll-like, a floating head, or an extreme beauty close-up. Keep supporting cast and lore props smaller and behind or beside the face.

Selected black shadow figures, animal-headed figures, Harvey, and the dog may pose beside or behind the person as group-photo participants. Keep them as separate characters: they must not replace the user's head, obscure the user's signature traits, or merge into the user.

## Generate

Use the built-in image generation tool by default. This is a strong style transfer with loose identity preservation. Include the user's portrait and, when available, verified scene, character, and outfit screenshots as clearly labeled references according to the image tool's input conventions.

Build a concise structured prompt from the template in the scene guide. State the 3–5 identity anchors and the canonical scene anchor explicitly. Ask for a square composition and one image. Do not request text, logos, interface chrome, or watermarks.

Make one generation call by default. If inspection shows a critical failure—photorealistic facial modeling, cheerful/glamorous expression, an extreme close-up with the visible facial oval over half the canvas height, a face too small to remain the focal point, fewer than five distinct canonical cues, chibi anatomy, non-square output, all identity anchors lost, gender-incongruent canonical clothing without a user request, original clothing retained without a user request, an animal head replacing the user, an invented/mixed background, or omitted user-selected content—make at most one focused corrective edit and deliver only the best final image.

## Validate and report

Before finishing, verify:

- the output is square and only one final image is presented;
- the subject looks like a flat, simplified Rusty Lake game character rather than a realistic painted portrait;
- 3–5 signature traits still connect the human subject to the attached person;
- the unobstructed face is the dominant focal point at the approved medium-close scale: full head silhouette about 50–65% and visible facial oval about 38–48% of canvas height;
- the default expression is visibly weary and downcast, with restrained body language, unless the user chose another mood;
- the close crop retains adult neck-and-shoulder anatomy without chibi or bobblehead distortion;
- expression and pose fit the scene, regardless of whether they match the photo;
- clothing comes from a verified Rusty Lake character and matches the subject's stated or apparent gender presentation unless the user requested otherwise;
- the selected setting is identifiable from the verified reference rather than merely matching a color palette;
- every user-selected character and element is present and visually distinct;
- at least five distinct canonical Rusty Lake cues are clearly visible and can be named individually;
- there is no accidental text, logo, watermark, collage seam, or extra face.

Render the result inline. Briefly name the game and scene used, identify the borrowed character outfit, list the included universe elements, and link the sources used to verify them when web research was needed. State that the scene and designs were redrawn from references rather than directly composited.
