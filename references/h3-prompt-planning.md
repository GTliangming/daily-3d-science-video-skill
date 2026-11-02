# MiniMax H3 prompt planning adapter

> Planning adapter only. It converts an approved, model-independent shot plan into text for the user's external H3 workflow. It never calls an API, submits a job, downloads a result or executes media production.

## 1. Source of truth and version discipline

The official MiniMax `h3-prompt-writing` Skill defines the mode-specific prompt structure. Use its current reference files as the authority for exact field names, label syntax, timing notation and section order. This document summarizes the planning implications; do not treat it as a replacement for the official guide.

If the user supplies a ComfyUI node, AutoDL wrapper or API schema, use that exact version for parameter names and supported controls. Do not mix fields from different interfaces. Mark unknown capabilities as unverified.

## 2. Choose the mode from the actual inputs

| Mode | Required input / role | Planning responsibility |
|---|---|---|
| T2VA | Text only | Build a complete audiovisual timeline |
| I2VA | Actual first-frame image | Anchor the opening composition, then describe forward development |
| FL2VA | First and last frame images | Describe one continuous, plausible path between them |
| L2VA | Actual last-frame image | Infer a plausible preceding state and converge to the ending frame |
| Ref2VA | Multiple references with distinct roles | Define subjects, concrete frame anchors, source video and audio references |

Do not choose I2VA just because the user has an image. An image may be a subject identity, geometry, style or composition reference rather than a first frame. If the intended role is unclear, ask one focused question.

For FL2VA, prefer a continuous shot unless the user explicitly requires multiple shots. The last frame must be reached by the final shot. For L2VA, the supplied image belongs to the ending, not automatically to the opening.

## 3. Separate director design from H3 translation

The approved Beat and Shot plan remains authoritative. H3 translation may:
- express the same shot with the official H3 fields
- clarify the reference-to-shot alignment
- describe observable motion and sound
- identify a shot as unsuitable for one generation and recommend splitting or precision 3D

It may not:
- change the scientific explanation to fit a model
- merge editorial shots that require a cut
- promise exact geometry, physical simulation or precise cuts without evidence
- invent dialogue or assign voiceover to a visible character

## 4. Reference roles and labels

For each reference, identify its role before writing a prompt:

| Role | What it constrains | Not automatically |
|---|---|---|
| Subject identity | silhouette, appearance, proportions, color, material | first frame or motion |
| Geometry / structure | part count, relative position, connections | style or camera |
| Style / material | rendering language, surface response, lighting | scientific truth |
| Composition / storyboard | framing, subject placement, spatial layout | actual keyframe |
| First / last / keyframe | a concrete time-aligned frame | general identity reference |
| Reference video | source edit, continuation or temporal structure | a reusable subject by itself |
| Reference audio | voice, music, sound or beat characteristics | visual content |

In Ref2VA, use the official six-section order:
1. `subject_definitions`
2. `summary`
3. `retention_analysis`
4. `detailed_description`
5. `overall_soundscape`
6. `non_diegetic_music`

Keep labels stable across every section. Distinguish reusable visible subjects (`<Subject N>`) from concrete frame anchors (`<Picture N>`), source videos (`<Video N>`) and audio references (`<Audio N>`). Do not create a standalone picture label when an image only supplies a subject's appearance; cite it in that subject definition instead.

## 5. Base-mode prompt structure

For T2VA / I2VA / FL2VA / L2VA, follow the official guide's exact first-line alignment instruction for the selected mode. Then use the three core fields in this order:

- `integrated_multimodal_description`: visible events, subjects, actions, shots, camera, speakers/dialogue and synchronized diegetic audio along the timeline.
- `overall_soundscape`: ambient sound, physical action sounds and non-verbal human sounds across the full video.
- `non_diegetic_music`: audience-only background music.

Do not invent alternate field names or rearrange the sections.

### Shot description

Each shot should state concrete, observable details:
- visual style and initial composition
- subject appearance, position and environment
- one primary action or state change
- shot size, angle and camera behavior
- lighting and material cues
- cut or continuous transition where appropriate
- diegetic sound only when it belongs to the scene

For later shots, follow the official shot numbering and cut-time syntax. Do not add hard cuts inside one generated clip unless the user explicitly wants that and the workflow has been validated for it. If the edit requires several independent shots, provide separate prompts/clips for each.

### Camera movement

Describe camera movement as a movement type plus meaningful amplitude and speed. Use static shot when no movement adds information. State whether the camera or the subject moves. Do not append a pile of generic camera adjectives.

## 6. Voiceover and sound for science explainers

Default project narration is third-person Mandarin off-screen voiceover:
- explicitly identify it as an off-screen voiceover / narration
- do not give the visible character matching mouth movement
- keep the exact approved Mandarin narration as its own script artifact
- only place speech in H3's spoken-content syntax if the selected mode/workflow is intended to generate it reliably

Keep four sound roles separate:
1. narration / voiceover
2. diegetic sound (motor, switch, airflow, impact)
3. ambient soundscape
4. non-diegetic music

Do not repeat dialogue or diegetic music in the ambient soundscape. If the user wants a silent model output, plan voiceover, SFX and music as post-production.

## 7. Chinese on-screen text

Complex Chinese subtitles, labels, measurements and diagrams should be post-produced by default. Prompt for clean negative space and avoid model-generated pseudo-text. If a short visible Chinese sign is essential, preserve its exact wording and flag generation uncertainty.

## 8. Per-shot prompt template

Use this as a planning worksheet, then translate it into the official mode format:

- Shot ID / final timeline / duration:
- H3 mode and why:
- Reference IDs and roles:
- Visual style and starting composition:
- Subject identity and geometry locks:
- Single visual task:
- Main action / state change:
- Shot size / angle / focus:
- Camera movement (static or one motivated move):
- Start state → end state:
- Environment / lighting / materials:
- Diegetic sound:
- Voiceover treatment:
- Continuity constraints:
- Negative constraints:
- Post-production items:
- Feasibility and known limitations:

## 9. Preflight

- [ ] Mode matches the actual input assets and intended reference roles.
- [ ] Official first-line alignment instruction and field order are correct.
- [ ] Reference labels are stable and used consistently.
- [ ] Every shot describes visible and audible events, not only abstract mood.
- [ ] One primary action and one coherent camera behavior per shot.
- [ ] Shot timing matches the approved storyboard and H3 workflow limit.
- [ ] Required cuts are represented as separate shots/clips where needed.
- [ ] Voiceover is off-screen; character dialogue is only present when requested.
- [ ] Ambient sound, diegetic sound and non-diegetic music are separated.
- [ ] Complex Chinese text is assigned to post-production by default.
- [ ] Unsupported model behavior is labeled unverified, not promised.
