# Production Pipeline

## 1. End-to-end flow

`approved storyboard → project manifest → shot tasks → preflight → asset generation → shot audit → repair → assembly → final audit → delivery`

The pipeline is a directed workflow, not a single prompt. Each stage consumes explicit artifacts and writes a result that can be inspected or resumed.

## 2. Stage contracts

| Stage | Input | Output | Must stop when |
|---|---|---|---|
| Import | approved script/storyboard | project.json + shot tasks | shot IDs or durations are ambiguous |
| Plan | project + visual bible | production plan | method cannot meet accuracy/quality |
| Preflight | plan + local/provider config | preflight report | tool unavailable, credentials absent, cost unapproved |
| Generate | one shot task | source asset + metadata | provider error or invalid output |
| Audit | asset + acceptance checks | audit result | artifact missing or critical defect |
| Repair | failed audit + defect notes | replacement asset | repair would contradict source facts |
| Assemble | approved shot assets + audio | review.mp4 | required assets/audio missing |
| Final audit | review.mp4 + project | final report | decode, duration, audio, subtitle, or review failure |
| Deliver | audited outputs | MP4 + manifest + report | unresolved critical issue |

## 3. Shot-level execution

A shot is the smallest independently retryable production unit. Keep a stable `shot_id` across retries. Each attempt should record:
- attempt number and timestamp;
- selected provider/model or local tool version;
- prompt or scene script version;
- input reference paths;
- output path and checksum;
- technical validation result;
- human review status and defect notes.

Do not overwrite a previously approved artifact. Write each attempt to a versioned path, then update the selected artifact only after review.

## 4. Production method selection

Use this decision order:

1. Does the shot explain an exact internal structure, component relationship, or physical mechanism? Use Blender or a verified diagram/animation.
2. Does it primarily show people, environment, product use, or cinematic action? Use AI video or licensed footage.
3. Is it a still reference or background? Use AI image or licensed still.
4. Is it typography, labels, arrows, charts, or simple explanatory overlays? Use deterministic motion graphics/FFmpeg.
5. If no available method can meet the acceptance criteria, mark it blocked and ask for a decision.

## 5. Checkpoints

- **P0 Input approval:** storyboard and facts are approved.
- **P1 Plan approval:** method, assets, provider/model, and cost are approved.
- **P2 Shot review:** representative or high-risk shots are reviewed before batch generation.
- **P3 Rough-cut review:** sequence, narration, and pacing are reviewed.
- **P4 Final approval:** final audit and human review complete.

A user may explicitly waive a checkpoint. Record that waiver in the project manifest.
