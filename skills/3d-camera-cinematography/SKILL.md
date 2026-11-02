---
name: 3d-camera-cinematography
description: >
  Design and execute cinematic 3D shots for realistic science explainer videos.
  Use when planning camera framing, lens, composition, camera movement, Blender camera rigs,
  shot continuity, product reveals, cutaways, macro shots, exploded views, or translating
  a storyboard into Blender and AI video generation instructions.
---

# 3D Camera Cinematography

## Mission

Turn an approved storyboard shot into a camera plan that is narratively motivated, spatially
coherent, technically executable, and suitable for a realistic cinematic 3D science video.

This is a video/film cinematography skill, not a gameplay camera controller. It owns shot design,
camera placement, lens choice, composition, movement, transitions, and camera-related review.
It does not invent scientific facts, redesign the approved story, model every asset, or call a
video-model API.

## Activation and inputs

Activate when the user asks for 3D shot design, camera work, camera movement, framing, lens,
cinematic composition, Blender camera execution, shot continuity, or conversion of storyboard
shots into production-ready camera instructions.

Before designing, reuse known project decisions. Read only the references needed:
- Camera language and shot selection: `references/camera-language.md`
- Blender scene/camera execution: `references/blender-execution.md`
- AI video prompt translation: `references/video-model-translation.md`
- Reusable output structure: `../../templates/3d-shot-execution-card.md`

Required input, if available:
- approved storyboard shot and its narration/purpose
- subject/product reference and approved visual bible
- aspect ratio and target platform
- shot duration (never over 15 seconds)
- preceding/following shots
- implementation target: Blender, AI video, or hybrid

If an essential input is missing, ask one concise question. Otherwise make explicit, reversible
assumptions and continue. Do not ask the user to repeat decisions already present in the project.

## Non-negotiable constraints

1. **One shot is at most 15 seconds.** A camera move or continuous take longer than 15 seconds
   must be split into separately numbered shots. Never hide multiple shots inside one row.
2. Every shot must have one primary visual purpose and one dominant subject/action.
3. Camera movement must reveal, explain, compare, or emotionally emphasize something. No
   gratuitous orbiting, zooming, or movement for decoration.
4. Preserve scientific truth. Camera angles, cutaways, scale changes, transparent materials,
   color coding, and visual effects must not imply false geometry or physical behavior.
5. Preserve continuity: subject identity, dimensions, part placement, axis/orientation, screen
   direction, light direction, lens language, and motion state must agree across adjacent shots.
6. Distinguish a real camera move from a subject move. State which one moves and which remains
   fixed.
7. Specify a start state and an end state. "Slow cinematic push-in" alone is not executable.
8. Design for the delivery aspect ratio. For vertical 9:16, protect the central subject and keep
   critical labels/action inside platform-safe regions; do not simply crop a 16:9 composition.
9. Never claim a Blender scene, render, or video exists unless it was actually created and checked.
10. Do not hard-code a specific video-generation provider, API, credential, or endpoint. Provider
    integration is configured by the user outside this Skill.

## Workflow

### Step 1 — Interpret the shot

Extract:
- shot ID and exact start/end timecode
- duration in seconds
- narrative function: establish / reveal / explain / compare / emphasize / transition / resolve
- scientific information the viewer must understand
- subject, action, environment, and relevant reference evidence
- continuity dependencies on previous and next shots

If the shot has multiple independent narrative beats, propose a split before camera design.

### Step 2 — Choose framing and camera geometry

Decide and justify:
- shot size: extreme wide, wide, full, medium, close-up, extreme close-up, macro, detail
- viewpoint: eye-level, high, low, top-down, three-quarter, profile, over-shoulder, orthographic
- camera-to-subject distance and subject placement
- lens focal length (state full-frame equivalent when communicating a photographic lens)
- perspective/depth-of-field intent
- focus target and focus behavior
- foreground, middle-ground, background and negative space
- subtitle/graphic safe area

Do not treat focal length as a substitute for camera distance. Explain perspective through both
camera position and focal length when it matters.

### Step 3 — Design movement

Choose only the movement needed:
- locked-off / tripod
- dolly or push-in / pull-out
- pan / tilt
- truck / lateral slide
- orbit / arc
- crane / pedestal / vertical rise
- tracking / follow
- rack focus
- subject rotation on a turntable
- controlled handheld only when the story calls for it

For every moving shot specify:
- start and end camera position (or relative offsets)
- start and end aim/target
- path shape and direction
- speed profile (ease-in, constant, ease-out, hold)
- movement duration and any hold
- what remains stationary
- how the movement reveals the intended information

Prefer smooth, physically plausible paths. Avoid sudden acceleration, unexplained axis changes,
camera passing through geometry, and focus hunting.

### Step 4 — Compose the frame

Describe:
- subject position and scale in frame
- headroom / lead room / look room where relevant
- visual hierarchy and focal point
- foreground framing and background separation
- depth layers and parallax
- negative space for subtitles and labels
- what must not be cropped, occluded, or confused

For science explanations, prioritize the visibility of the relevant part or process over decorative
symmetry. Keep labels readable and avoid placing arrows over the mechanism they explain.

### Step 5 — Plan lighting and visual readability

Camera design and lighting must work together. State:
- key/fill/rim or motivated practical-light direction
- contrast and exposure intent
- whether reflections obscure the subject
- whether depth of field hides important scientific detail
- whether transparent/cutaway parts remain legible

Use the shared project visual bible; do not invent a new look for each shot.

### Step 6 — Translate into an execution route

Select one:
- **Blender 3D**: precise geometry, internal mechanisms, cutaways, exploded views, controlled
  camera animation, repeatable framing.
- **AI video**: people, environments, lifestyle scenes, atmospheric transitions, or shots where
  exact internal geometry is not the point.
- **Hybrid**: render precise 3D subject/action and combine with AI/live-action environment or
  post-production graphics.

For Blender, follow `references/blender-execution.md`.
For AI video, follow `references/video-model-translation.md`.
Do not force every shot through Blender if an AI video shot is more efficient and sufficiently
accurate.

### Step 7 — Check continuity and scientific meaning

Compare the shot with adjacent shots:
- screen direction and axis
- subject scale and orientation
- product silhouette, color, materials and part locations
- camera height, lens family and movement direction
- lighting direction and color temperature
- motion phase at the cut
- narration-to-visual timing

For a cutaway, exploded view, macro scale, or invisible physical process, explicitly label the
image as a visualization when a viewer could mistake it for literal footage.

### Step 8 — Review and revise

Review a low-cost preview or storyboard frame before final rendering/generation. Evaluate:
- Is the intended information understood at a glance?
- Is the subject readable at final delivery size?
- Does movement improve understanding?
- Is the move smooth and physically plausible?
- Does the shot fit its duration?
- Is the previous/next cut coherent?
- Does the image accidentally assert an unsupported scientific claim?

Fix the highest-impact issue first. Change one major variable per revision pass where practical.

## Required output

Use the full execution card in `../../templates/3d-shot-execution-card.md`. At minimum return:

1. Shot purpose and viewer takeaway
2. Duration and timecode (≤15s)
3. Shot size, viewpoint, lens, camera distance
4. Composition and subject placement
5. Camera start/end state and movement path
6. Focus / depth-of-field behavior
7. Lighting and material readability
8. Blender execution steps OR AI video prompt OR hybrid plan
9. Continuity constraints and negative constraints
10. Preview/acceptance checklist

When several shots are requested, output one card per shot and then a continuity table.

## Boundaries and related skills

- Existing planning Skill owns topic, science research, script and storyboard approval.
- This Skill owns cinematic 3D shot/camera design and its execution translation.
- Visual production reference owns global look, asset workflow and tool division.
- The user-configured production environment owns actual model APIs and credentials.
- Post-production workflow owns final edit, sound, captions and delivery QC.

Do not silently change an approved narration, scientific statement, visual style, or storyboard.
If camera design exposes a story/science problem, flag it and propose a minimal correction for approval.
