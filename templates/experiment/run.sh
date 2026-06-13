#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

ATTACK_PATH="${1:-attack.py}"
SDK_ROOT="${SDK_ROOT:-../../data/raw/ai-agent-security-multi-step-tool-attacks}"

PYTHONPATH="$SDK_ROOT${PYTHONPATH:+:$PYTHONPATH}" \
  uv run python -m aicomp_sdk.cli.main validate redteam "$ATTACK_PATH"

PYTHONPATH="$SDK_ROOT${PYTHONPATH:+:$PYTHONPATH}" \
  uv run python -m aicomp_sdk.cli.main test redteam "$ATTACK_PATH" \
  --budget-s 60 --agent deterministic
