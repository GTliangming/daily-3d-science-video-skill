#!/usr/bin/env python3
"""Validate the production project manifest using only the Python standard library."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

METHODS = {"blender", "ai_video", "ai_image", "stock", "motion_graphics"}
STATUSES = {"pending", "running", "generated", "audited", "approved", "blocked", "failed", "rejected"}


def validate(data: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["project root must be a JSON object"]

    for key in ("schema_version", "project_id", "title", "target", "shots", "approvals", "output"):
        if key not in data:
            errors.append(f"missing required field: {key}")

    project_id = data.get("project_id")
    if not isinstance(project_id, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", project_id):
        errors.append("project_id must contain only letters, digits, dot, underscore, or hyphen")

    target = data.get("target")
    if not isinstance(target, dict):
        errors.append("target must be an object")
    else:
        for key in ("aspect_ratio", "width", "height", "fps"):
            if key not in target:
                errors.append(f"target.{key} is required")
        for key in ("width", "height"):
            if key in target and (not isinstance(target[key], int) or target[key] <= 0):
                errors.append(f"target.{key} must be a positive integer")
        if "fps" in target and (not isinstance(target["fps"], (int, float)) or target["fps"] <= 0):
            errors.append("target.fps must be positive")

    shots = data.get("shots")
    if not isinstance(shots, list):
        errors.append("shots must be an array")
        return errors

    seen: set[str] = set()
    for index, shot in enumerate(shots):
        prefix = f"shots[{index}]"
        if not isinstance(shot, dict):
            errors.append(f"{prefix} must be an object")
            continue
        shot_id = shot.get("shot_id")
        if not isinstance(shot_id, str) or not shot_id.strip():
            errors.append(f"{prefix}.shot_id is required")
        elif shot_id in seen:
            errors.append(f"duplicate shot_id: {shot_id}")
        else:
            seen.add(shot_id)
        duration = shot.get("duration_seconds")
        if not isinstance(duration, (int, float)) or duration <= 0:
            errors.append(f"{prefix}.duration_seconds must be positive")
        if not isinstance(shot.get("visual_description"), str) or not shot["visual_description"].strip():
            errors.append(f"{prefix}.visual_description is required")
        if shot.get("production_method") not in METHODS:
            errors.append(f"{prefix}.production_method must be one of {sorted(METHODS)}")
        if shot.get("status", "pending") not in STATUSES:
            errors.append(f"{prefix}.status is invalid")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python validate_project.py <project.json>")
        return 2
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read project JSON: {exc}")
        return 2

    errors = validate(data)
    if errors:
        print("Project validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Project valid: {data['project_id']} ({len(data['shots'])} shots)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
