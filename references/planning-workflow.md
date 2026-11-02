# Planning workflow, routing and quality gates

This reference defines how the main Skill moves through a project. It borrows the router pattern (detect → classify → load minimal modules → compose), staged evidence-first planning, and explicit review gates. It is written for science-video planning, not for executing media production.

## 1. Router: identify the user's actual request

Classify the current turn into one primary task. Do not load every specialist module by default.

| User request | Primary work | Load when needed |
|---|---|---|
| “I want to make a video” | Entry and brief | None |
| Topic, angle, title, audience | Research/creative treatment | content strategy; fact checking |
| Explain how something works | Science research and explanation | fact checking; animation-motion if physical process planning is needed |
| Write or revise narration | Script | content strategy; fact checking |
| Design storyboard / shots | Beat → coverage → shot design | shot-design-v2; camera; scene; animation as needed |
| Establish visual style / references | Visual Bible and reference map | lighting-materials; scene-composition; reference-image consistency |
| Prepare model prompts | Model translation | generic translation or H3 adapter only |
| Review an existing plan | Quality audit | only the references related to failed checks |

Routing rules:
- The main Skill owns the project state, science truth, user approvals and final integration.
- Specialist modules are additive expertise, not alternative workflows.
- Load the smallest useful set. A shot involving an internal mechanism may need fact-checking + animation planning + camera; it does not automatically need asset modeling and lighting.
- Re-route only when the user's task changes materially.
- If a named specialist file is missing, do not claim it was loaded. Continue with the main rules.

## 2. Brief: capture the minimum viable creative brief

Resolve only details that materially change the plan:
- topic / product / phenomenon and whether a specific model is being depicted
- audience and intended takeaway
- platform and aspect ratio
- target total duration
- desired visual style and realism
- available references or tools, if execution feasibility depends on them

Use known context where available. Ask one question at a time. If the user says “you decide”, recommend defaults and label them as assumptions.

Deliverable: a short brief with confirmed choices, assumptions and open questions.

Gate 1 — brief:
- Is the subject and intended audience clear?
- Is the central question specific enough to research?
- Is the target duration known or explicitly assumed?
- Are exact-product claims distinguished from typical schematic claims?

## 3. Research: evidence before storytelling

Build a question list before searching. For each important claim, record:
- claim in plain language
- evidence/source and publication/updated date when available
- what the source actually supports
- scope and caveats (model/version/material/operating conditions)
- confidence: verified / model-dependent / inference / unresolved
- planned visual consequence

Prefer primary sources: standards and regulators, manufacturer technical documentation, patents, peer-reviewed papers and reputable scientific institutions. Secondary explainers can help discover terms but should not be the sole support for a critical mechanical or safety claim.

Do not over-research trivia. Research only facts that affect the explanation, visuals, safety, or likely audience misconception.

Deliverable: fact sheet + source list + unresolved questions.

Gate 2 — science:
- Does every central claim have support?
- Are contradictory sources or product variants acknowledged?
- Are visual simplifications marked as explanatory?
- Can the mechanism be explained without a false causal shortcut?

If a key fact remains unresolved, either research further, remove the claim, or label it as an assumption. Never quietly turn uncertainty into certainty.

## 4. Treatment: one central idea and a visual argument

Before writing the full narration, define:
- one-sentence promise: what the viewer will understand
- hook: the question, contradiction or everyday observation that earns attention
- narrative progression: how each section changes the viewer's understanding
- visual argument: what images demonstrate the principle rather than merely decorate it
- ending: what the viewer should remember

A visual metaphor is optional. Use it only when it clarifies the mechanism; never let an attractive metaphor replace evidence or the real subject.

Deliverable: 2–3 genuinely different treatments, then one recommended direction. Do not present cosmetic rewrites as distinct concepts.

Gate 3 — treatment:
- Is the central promise narrow and accurate?
- Does each section add a new piece of understanding?
- Does the proposed visual approach actually help explain the topic?
- Is the hook interesting without exaggerating?

## 5. Script: narration and evidence mapping

Write Mandarin narration in natural spoken language unless another language is requested. Default voice is calm, clear and exploratory; light humor is acceptable if it does not distort the science.

For each paragraph/line, map:
- time estimate
- narration text
- knowledge point / claim ID
- evidence source
- visual evidence needed
- optional on-screen label or post-production subtitle

The narration should not describe a visual that the storyboard cannot reasonably show. The storyboard should not introduce a scientific claim absent from the research sheet.

Estimate spoken duration using realistic Mandarin delivery, then revise to the requested total length. Do not force a fixed script template if the topic needs a different structure.

Deliverable: approved narration + claim-to-script map + timing estimate.

Gate 4 — script:
- Does the script answer the central question?
- Is each factual sentence traceable to evidence or marked as uncertain?
- Does spoken duration fit the requested length?
- Are voiceover, character dialogue and on-screen text separate?

## 6. Visual Bible: lock the visual system

Create a concise shared visual system before designing many reference images or prompts:
- subject identity, proportions and immutable features
- geometry and component relationships backed by sources
- material and surface behavior
- environment, props and spatial orientation
- lighting direction, quality, contrast and color temperature
- palette and color semantics
- lens / framing / depth-of-field language
- aspect ratio and safe areas
- permitted simplifications and prohibited errors

Use the same visual bible across the storyboard and prompt pack. Do not repeat long generic “cinematic 8K” adjectives; specify visible properties and constraints.

Deliverable: Visual Bible + unresolved visual assumptions.

Gate 5 — visual system:
- Is the look coherent across shots?
- Are true material colors distinguished from explanatory color coding?
- Are structural details evidence-backed?
- Can the chosen visual language remain legible at the target aspect ratio?

## 7. Storyboard: Beat → coverage → Shot

### 7.1 Start with Beats

For each Beat record:
- what the audience does not yet understand
- what they must understand at the end
- narration passage and approximate time
- visible evidence that can teach it
- relevant claim IDs

### 7.2 Build coverage before counting shots

Consider only the coverage types that serve the Beat:
- establish whole object / environment
- show structure and relative positions
- isolate a critical detail
- demonstrate action, flow or state change
- compare states or outcomes
- reconnect the detail to the whole system

A Beat may need one shot or several. Do not divide narration into 15-second chunks mechanically.

### 7.3 Define each shot

Each shot is one continuous view and must contain:
- Shot ID, Beat ID, timeline in/out, duration
- unique visual purpose and audience takeaway
- subject, main action/state change, environment
- shot size, angle, composition, focus
- camera: static by default, or one motivated primary move
- start/end visual state
- narration line and subtitle/label plan
- science claim IDs and geometry constraints
- previous/next continuity
- required references
- execution class A/B/C and reason

Hard duration rule: every editorial shot is >0 and ≤15 seconds. Fifteen seconds is a maximum, not a target. If a shot requires a hard cut, new scale, new subject, new space or a different viewpoint, split it into separate shots. Never hide several shots inside a “sub-shot” row.

### 7.4 Camera rule

For every moving camera, answer:
- what new information does this movement reveal?
- is the camera moving, or is the subject rotating/moving?
- what are the start and end compositions?
- what is the direction, approximate amplitude and speed?
- what must remain still?

Orbit is exceptional, not default. Use it only when seeing multiple sides or spatial relationships is genuinely necessary. If the same information can be shown with a static view or a cut, prefer that.

Deliverables:
A. Beat table
B. Shot table
C. shot continuity matrix
D. execution feasibility table

Gate 6 — storyboard:
- Does each shot have a distinct teaching purpose?
- Does each cut add new information?
- Are repeated views justified?
- Is the main mechanism actually visible?
- Are all shots ≤15s and the full timeline continuous?
- Are precision-sensitive shots assigned to a suitable route?
- Are camera movements motivated?

## 8. Reference plan: assign roles, don't generate images

Each reference asset receives:
- stable ID and proposed filename
- type (subject / geometry / style / composition / first-last keyframe / video / audio)
- source or planned source
- primary responsibility
- what it must constrain
- what it must not constrain
- shots that use it

A reference image can have multiple roles only when those roles are explicitly separated. A geometry reference does not prove the geometry is correct; science sources do. A style reference is not automatically a first frame. An image used as a true first/last frame must be identified as such.

Deliverable: reference asset manifest + shot-to-reference matrix. No image files are created by this Skill.

Gate 7 — references:
- Is every asset role explicit?
- Are there conflicting references?
- Does every precision-sensitive shot have a trustworthy geometry source?
- Are actual keyframes distinguished from identity/style references?

## 9. Model prompt adapter

Only after the storyboard and visual bible are confirmed:
1. Identify the exact model and workflow variant.
2. Check actual supported inputs, duration, resolution, reference count, audio and keyframe controls from the user's workflow documentation.
3. Translate one approved shot at a time.
4. Keep each prompt self-contained; repeat necessary identity/geometry/continuity constraints.
5. State unsupported or unverified requirements as limitations, not instructions disguised as guarantees.

The model adapter may simplify execution, but cannot change the scientific claim, invent a physical mechanism or merge separate editorial shots.

For MiniMax H3, read `references/h3-prompt-planning.md`. Follow official mode-specific prompt structure and use the user's actual ComfyUI/API node schema when it differs from the official guide.

Gate 8 — prompt preflight:
- mode matches the supplied inputs
- references have stable labels and correct roles
- timing is within the workflow limit
- shots and cuts are represented correctly
- voiceover is not assigned to a visible character
- diegetic sound, ambient sound and non-diegetic music are separated
- Chinese subtitles and complex labels are planned for post by default
- prompt asks only for behavior the model may plausibly perform

## 10. Final review: viewer test and factual test

Review the plan from two perspectives.

**Science editor**
- Is every central statement supported?
- Are model-specific variants and uncertainty visible?
- Do visuals preserve the real causal relationships?

**Viewer / director**
- Can the audience understand what each shot is teaching?
- Does the sequence vary subject, scale, angle and information purpose?
- Does the opening create a real question?
- Does the ending resolve the question?
- Is the pace appropriate, not merely fast?

A complete table is not evidence of a good film. If a sequence feels repetitive, abstract, visually empty or too difficult for the selected method, return to the relevant stage and redesign only the affected part.

## 11. Standard delivery structure

For a full planning package, use this order:
1. Project brief and assumptions
2. Creative treatment
3. Research / fact sheet and sources
4. Approved narration and claim map
5. Visual Bible
6. Beat table
7. Shot table
8. Continuity matrix
9. Reference asset manifest and mapping
10. Per-shot prompt pack (only if requested)
11. Risks, unresolved questions and final checklist

For a single-stage request, deliver only the relevant section.
