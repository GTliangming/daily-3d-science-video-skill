# Quality Control

## 1. Three independent audit layers

### A. Scientific and editorial audit

Human or qualified editorial review must verify:
- each factual statement maps to a source or is labeled uncertain;
- visible structures and process order match the approved references;
- diagrams are labeled as schematic when not product-specific;
- narration and visuals describe the same event;
- no generated detail is presented as verified fact without evidence.

Automated checks can enforce that references and review fields exist; they cannot prove scientific truth.

### B. Shot-level visual and audio audit

For every shot, inspect:
- correct subject, product appearance, and scene;
- continuity with the visual bible and neighboring shots;
- no major deformation, flicker, text gibberish, or unintended objects;
- framing and subtitle-safe area;
- expected duration and aspect ratio;
- audio presence, clipping, and synchronization when applicable.

### C. Final-file technical audit

Use FFprobe/FFmpeg where available to check:
- container and codec are readable;
- video stream exists;
- duration and frame rate are within tolerance;
- resolution and aspect ratio match the project;
- audio stream exists when required;
- full decode succeeds;
- black/frozen intervals are flagged for review;
- subtitle file parses and stays within safe margins.

## 2. Audit severity

- `critical`: scientific contradiction, missing/corrupt shot, wrong product/mechanism, unsafe misinformation.
- `major`: obvious continuity break, unreadable subtitle, severe visual artifact, missing narration/audio.
- `minor`: small timing, color, or polish issue.

Critical defects block delivery. Major defects require repair or an explicit user waiver. Minor defects may be accepted and recorded.

## 3. Avoid metric gaming

Counts such as animation events, transitions, or motion are diagnostic signals, not quality targets. Do not add meaningless movement to satisfy a numeric threshold. Evaluate whether the image communicates the intended information.

## 4. Audit report format

Each finding should include:
- severity;
- shot/time range;
- observed issue;
- expected behavior;
- evidence (frame, timestamp, probe output, or reviewer note);
- recommended repair;
- disposition: open, fixed, accepted, or waived.

## 5. Human review remains mandatory

Automated checks can detect structural and technical defects. They cannot reliably judge whether an explanation is scientifically faithful, emotionally effective, or aesthetically good. Final delivery requires human approval unless the user explicitly defines a different review policy.
