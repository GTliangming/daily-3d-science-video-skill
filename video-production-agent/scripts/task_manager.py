#!/usr/bin/env python3
"""Small JSON task-state manager; no database or third-party dependency required."""
from __future__ import annotations

import argparse
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ACTIVE = {"running"}
RETRYABLE = {"failed", "rejected", "blocked"}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_atomic(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def find_shot(project: dict, shot_id: str) -> dict:
    for shot in project.get("shots", []):
        if shot.get("shot_id") == shot_id:
            return shot
    raise SystemExit(f"Unknown shot_id: {shot_id}")


def cmd_status(args: argparse.Namespace) -> int:
    project = load(args.project)
    counts: dict[str, int] = {}
    for shot in project.get("shots", []):
        status = shot.get("status", "pending")
        counts[status] = counts.get(status, 0) + 1
    print(json.dumps({"project_id": project.get("project_id"), "total": len(project.get("shots", [])), "counts": counts}, ensure_ascii=False, indent=2))
    return 0


def cmd_claim(args: argparse.Namespace) -> int:
    project = load(args.project)
    shot = find_shot(project, args.shot_id)
    if shot.get("status", "pending") != "pending":
        raise SystemExit(f"Cannot claim shot in state {shot.get('status')!r}; expected 'pending'")
    shot["status"] = "running"
    shot["claimed_by"] = args.worker
    shot["updated_at"] = now()
    shot.setdefault("attempts", []).append({"attempt": len(shot["attempts"]) + 1, "started_at": now(), "worker": args.worker})
    save_atomic(args.project, project)
    print(f"Claimed {args.shot_id}")
    return 0


def cmd_complete(args: argparse.Namespace) -> int:
    project = load(args.project)
    shot = find_shot(project, args.shot_id)
    if shot.get("status") != "running":
        raise SystemExit(f"Cannot complete shot in state {shot.get('status')!r}; expected 'running'")
    artifact = Path(args.artifact)
    if not artifact.is_file() or artifact.stat().st_size == 0:
        raise SystemExit(f"Artifact does not exist or is empty: {artifact}")
    shot["status"] = "generated"
    shot["selected_artifact"] = str(artifact)
    shot["updated_at"] = now()
    attempts = shot.setdefault("attempts", [])
    if attempts:
        attempts[-1]["finished_at"] = now()
        attempts[-1]["artifact"] = str(artifact)
        attempts[-1]["notes"] = args.notes or ""
    save_atomic(args.project, project)
    print(f"Marked {args.shot_id} generated: {artifact}")
    return 0


def cmd_fail(args: argparse.Namespace) -> int:
    project = load(args.project)
    shot = find_shot(project, args.shot_id)
    if shot.get("status") != "running":
        raise SystemExit(f"Cannot fail shot in state {shot.get('status')!r}; expected 'running'")
    shot["status"] = "failed"
    shot["updated_at"] = now()
    attempts = shot.setdefault("attempts", [])
    if attempts:
        attempts[-1]["finished_at"] = now()
        attempts[-1]["error"] = args.reason
    save_atomic(args.project, project)
    print(f"Marked {args.shot_id} failed")
    return 0


def cmd_retry(args: argparse.Namespace) -> int:
    project = load(args.project)
    shot = find_shot(project, args.shot_id)
    if shot.get("status") not in RETRYABLE:
        raise SystemExit(f"Cannot retry shot in state {shot.get('status')!r}; expected one of {sorted(RETRYABLE)}")
    shot["status"] = "pending"
    shot["updated_at"] = now()
    shot["retry_reason"] = args.reason
    save_atomic(args.project, project)
    print(f"Reset {args.shot_id} to pending")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("status",):
        command = sub.add_parser(name)
        command.add_argument("project", type=Path)
        command.set_defaults(func=cmd_status)
    claim = sub.add_parser("claim")
    claim.add_argument("project", type=Path)
    claim.add_argument("shot_id")
    claim.add_argument("--worker", default="agent")
    claim.set_defaults(func=cmd_claim)
    complete = sub.add_parser("complete")
    complete.add_argument("project", type=Path)
    complete.add_argument("shot_id")
    complete.add_argument("--artifact", required=True)
    complete.add_argument("--notes", default="")
    complete.set_defaults(func=cmd_complete)
    fail = sub.add_parser("fail")
    fail.add_argument("project", type=Path)
    fail.add_argument("shot_id")
    fail.add_argument("--reason", required=True)
    fail.set_defaults(func=cmd_fail)
    retry = sub.add_parser("retry")
    retry.add_argument("project", type=Path)
    retry.add_argument("shot_id")
    retry.add_argument("--reason", required=True)
    retry.set_defaults(func=cmd_retry)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
