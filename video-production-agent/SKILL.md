---
name: daily-3d-science-video-production
description: Execute a production-ready workflow for turning an approved science-video storyboard into real video assets and a rendered MP4. Use when the user asks to produce, render, assemble, audit, or revise video deliverables, not merely plan them.
---

# Daily 3D Science Video Production Agent

## 1. Mission

Turn an approved project brief and storyboard into real, inspectable production artifacts. Do not claim a video has been produced unless the expected files exist and pass the relevant checks.

This Skill is the production counterpart to the repository's root planning Skill. The planning Skill researches and designs; this Skill executes and verifies.

## 2. Entry and mode selection

At the beginning, establish which input the user has:

- **Approved storyboard/project package:** import it and begin production.
- **Only a topic:** ask whether to run the planning Skill first. If the planning Skill is available in the host, invoke it; otherwise explain that the user must provide or create an approved storyboard.
- **Existing assets/project:** inspect the manifest and continue from the current task states.

Do not silently invent missing scientific facts, product geometry, model credentials, or user approvals.

## 3. Production principles

1. **Shot-level units:** every shot is an independently trackable task with an owner, method, inputs, outputs, status, and audit result.
2. **Mixed production:** choose the least costly method that can satisfy the shot:
   - Blender for precise geometry, cutaways, exploded views, mechanisms, and explanatory physical processes.
   - AI video for people, domestic environments, realistic usage scenes, and cinematic transitions.
   - AI images or licensed stock for still references, backgrounds, and inserts.
   - FFmpeg for assembly, subtitles, audio mixing, and delivery encoding.
3. **Provider-neutral:** never hard-code one model vendor into the workflow. Use a configured provider adapter and report missing credentials or capabilities.
4. **Evidence-aware:** scientific claims and visible mechanisms must trace back to the approved fact-check/storyboard. A beautiful but misleading shot fails.
5. **Human approval gates:** request approval before paid generation, irreversible overwrites, or final delivery when the user has asked to review first.
6. **Recoverable execution:** persist task state and artifact paths. Retry only failed or rejected shots; do not regenerate completed shots without a reason.
7. **Honest completion:** distinguish planned, submitted, generated, downloaded, rendered, audited, and approved states.

## 4. Required inputs

Before production, verify:

- Project title and target platform/aspect ratio.
- Approved script/storyboard with stable shot IDs and durations.
- Fact-check references or explicit unresolved-fact flags.
- Visual bible: product/person/environment continuity constraints.
- Available production tools and provider configuration.
- Output directory and whether paid API calls are authorized.

If an input is missing, ask one focused question at a time. Use safe defaults only for reversible technical settings.

## 5. Workflow

### Stage 1 — Import and validate

1. Read the storyboard and source references.
2. Normalize it into `project.json` and one task per shot.
3. Run `python scripts/validate_project.py <project.json>`.
4. Stop if shot IDs are duplicated, durations are invalid, or required creative fields are absent.

### Stage 2 — Build the production plan

For each shot, record:
- production method: `blender`, `ai_video`, `ai_image`, `stock`, or `motion_graphics`;
- why that method is appropriate;
- required inputs and reference assets;
- expected output path and technical format;
- continuity constraints;
- acceptance checks;
- estimated external cost, if known.

Prefer mixed production. Do not send precision-dependent internal mechanisms to text-to-video as the sole source of truth.

### Stage 3 — Preflight tools and costs

Check the configured adapters and local executables (at minimum Blender and FFmpeg if those methods are selected). Check provider configuration without printing secrets. Before any billable API call, summarize the provider, model, number of shots, estimated cost if available, and ask for approval unless the user has already explicitly authorized that budget.

### Stage 4 — Produce shot assets

Process shots independently. For each shot:
1. Claim the task.
2. Prepare references and prompt/scene instructions.
3. Invoke the selected adapter or local tool.
4. Wait for completion and retrieve the actual artifact.
5. Verify file existence, non-zero size, duration, resolution, and expected format.
6. Mark complete only after artifact verification.

If a provider cannot be called from the current environment, mark the task `blocked` and report the exact missing adapter, credential, or permission. Never fabricate an output path.

### Stage 5 — Review and repair

Run technical checks and visual review. For failed shots, record a concrete defect and a targeted repair instruction. Regenerate only affected shots. Human review remains required for scientific accuracy, continuity, and aesthetic quality.

### Stage 6 — Assemble

Use FFmpeg or an explicitly configured editing adapter to:
- normalize shot dimensions, frame rate, and pixel format;
- assemble shots in storyboard order;
- add approved narration, music, sound effects, and subtitles;
- preserve audio levels and subtitle safe areas;
- export a review copy before final delivery.

Do not invent narration or music if the approved script/audio is missing.

### Stage 7 — Final audit and delivery

Verify:
- output file exists and can be probed/decoded;
- duration is within the agreed tolerance;
- no black/frozen/missing sections;
- audio is present and synchronized where expected;
- subtitles are readable and within safe margins;
- every shot maps to an approved storyboard entry;
- scientific and continuity review is complete;
- licenses and platform disclosure requirements have been checked.

Deliver the MP4 plus project manifest, asset inventory, and audit report. Clearly list any unresolved manual review items.

## 6. Task states

Use these states consistently:

`pending` → `running` → `generated` → `audited` → `approved`

Exceptional states: `blocked`, `failed`, `rejected`.

A task may return to `pending` only through an explicit retry after its failure/rejection reason has been recorded. `generated` means an artifact exists; it does not mean it passed review.

## 7. Tool invocation contract

This Skill does not assume that the chat model can directly operate every external service. It may use:

- local executables (Blender, FFmpeg);
- provider adapters configured by the user;
- host-provided tools/plugins explicitly exposed in the current session.

Read `references/provider-contract.md` before integrating a provider. Do not guess API endpoints, credentials, model names, or host tool names. Discover available tools first. Keep secrets in environment variables or a secret manager; never write them to manifests, prompts, logs, or reports.

## 8. Project files

Use the templates and schemas in this folder. The first implementation uses JSON manifests and Python standard-library scripts so it can run without Docker, a database, or extra Python dependencies.

- `templates/project.example.json`
- `templates/shot-task.example.json`
- `schemas/video-project.schema.json`
- `schemas/shot-task.schema.json`
- `scripts/task_manager.py`
- `scripts/validate_project.py`

## 9. First-run behavior

When no project exists:
1. Ask for an approved storyboard or permission to run the planning Skill.
2. Create a project directory and copy the example manifest.
3. Validate it.
4. Build the shot-level task list.
5. Present the production plan and cost/tool preflight before generating anything.

The default is **no paid generation until the user approves it**.
