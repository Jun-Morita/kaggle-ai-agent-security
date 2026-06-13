from __future__ import annotations

import argparse
import csv
import hashlib
import subprocess
from datetime import UTC, datetime
from pathlib import Path

FIELDS = [
    "timestamp",
    "version",
    "source_experiment",
    "fold_version",
    "cv",
    "public_lb",
    "private_lb",
    "file",
    "config_hash",
    "git_sha",
    "references",
    "note",
]


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()[:12]


def git_sha() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return ""
    return result.stdout.strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    parser.add_argument("--source-experiment", required=True)
    parser.add_argument("--fold-version", default="")
    parser.add_argument("--cv", default="")
    parser.add_argument("--public-lb", default="")
    parser.add_argument("--private-lb", default="")
    parser.add_argument("--file", default="")
    parser.add_argument("--config", type=Path, default=None)
    parser.add_argument("--references", default="")
    parser.add_argument("--note", default="")
    parser.add_argument("--log", type=Path, default=Path("submit/submissions.csv"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.log.parent.mkdir(parents=True, exist_ok=True)

    row = {
        "timestamp": datetime.now(UTC).isoformat(timespec="seconds"),
        "version": args.version,
        "source_experiment": args.source_experiment,
        "fold_version": args.fold_version,
        "cv": args.cv,
        "public_lb": args.public_lb,
        "private_lb": args.private_lb,
        "file": args.file,
        "config_hash": file_sha256(args.config) if args.config else "",
        "git_sha": git_sha(),
        "references": args.references,
        "note": args.note,
    }

    write_header = not args.log.exists()
    with args.log.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if write_header:
            writer.writeheader()
        writer.writerow(row)

    print(f"recorded submission: {args.log}")


if __name__ == "__main__":
    main()
