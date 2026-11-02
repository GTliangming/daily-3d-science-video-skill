#!/usr/bin/env python3
"""Validate the structural and timing contract of a 3D science-video shot plan.

Usage:
  python scripts/validate_shot_plan.py templates/3d-shot-plan-template.json
  python scripts/validate_shot_plan.py path/to/shot-plan.json --max-shot-seconds 15

This checks metadata and timing continuity. It cannot judge visual quality or scientific truth.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_CAMERA_FIELDS = (
    "shot_size",
    "viewpoint",
    "movement",
    "start_state",
    "end_state",
    "path",
    "speed_profile",
    "focus_target",
)


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def validate(data: dict[str, Any], max_seconds: float) -> list[str]:
    errors: list[str] = []
    project = data.get("project")
    shots = data.get("shots")

    if not isinstance(project, dict):
        fail("'project' must be an object", errors)
    if not isinstance(shots, list) or not shots:
        fail("'shots' must be a non-empty array", errors)
        return errors

    seen_ids: set[str] = set()
    previous_end: float | None = None

    for index, shot in enumerate(shots, start=1):
        label = f"shots[{index - 1}]"
        if not isinstance(shot, dict):
            fail(f"{label} must be an object", errors)
            continue

        shot_id = shot.get("id")
        if not isinstance(shot_id, str) or not shot_id.strip():
            fail(f"{label}.id must be a non-empty string", errors)
        elif shot_id in seen_ids:
            fail(f"duplicate shot id: {shot_id}", errors)
        else:
            seen_ids.add(shot_id)

        try:
            start = float(shot["start"])
            end = float(shot["end"])
            duration = float(shot["duration"])
        except (KeyError, TypeError, ValueError):
            fail(f"{label} must have numeric start, end and duration", errors)
            continue

        if start < 0:
            fail(f"{label}.start cannot be negative", errors)
        if end <= start:
            fail(f"{label}.end must be greater than start", errors)
        if duration <= 0:
            fail(f"{label}.duration must be greater than 0", errors)
        if duration > max_seconds:
            fail(
                f"{label} duration {duration:g}s exceeds limit {max_seconds:g}s",
                errors,
            )
        if abs((end - start) - duration) > 0.05:
            fail(
                f"{label} duration does not match end-start "
                f"({duration:g}s vs {end - start:g}s)",
                errors,
            )
        if previous_end is not None and abs(start - previous_end) > 0.05:
            relation = "gap" if start > previous_end else "overlap"
            fail(
                f"{label} has a timeline {relation}: starts at {start:g}s, "
                f"previous shot ended at {previous_end:g}s",
                errors,
            )
        previous_end = end

        camera = shot.get("camera")
        if not isinstance(camera, dict):
            fail(f"{label}.camera must be an object", errors)
        else:
            for field in REQUIRED_CAMERA_FIELDS:
                value = camera.get(field)
                if not isinstance(value, str) or not value.strip():
                    fail(f"{label}.camera.{field} is required", errors)

        if not isinstance(shot.get("purpose"), str) or not shot["purpose"].strip():
            fail(f"{label}.purpose is required", errors)
        if shot.get("implementation") not in {"blender", "ai_video", "hybrid", "live_action"}:
            fail(
                f"{label}.implementation must be blender, ai_video, hybrid, or live_action",
                errors,
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path, help="Path to shot-plan JSON")
    parser.add_argument("--max-shot-seconds", type=float, default=15.0)
    args = parser.parse_args()

    if args.max_shot_seconds <= 0:
        parser.error("--max-shot-seconds must be greater than 0")
    try:
        data = json.loads(args.plan.read_text(encoding="utf-8"))
    except OSError as exc:
        print(f"ERROR: cannot read {args.plan}: {exc}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}", file=sys.stderr)
        return 2

    if not isinstance(data, dict):
        print("ERROR: plan root must be a JSON object", file=sys.stderr)
        return 2

    errors = validate(data, args.max_shot_seconds)
    if errors:
        print("Shot plan validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    total = sum(float(shot["duration"]) for shot in data["shots"])
    print(
        f"OK: {len(data['shots'])} shots; total {total:.2f}s; "
        f"each shot <= {args.max_shot_seconds:g}s; timeline is contiguous."
    )
    print("Note: this validates structure/timing only, not visual quality or scientific accuracy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
