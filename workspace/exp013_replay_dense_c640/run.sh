#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
ATTACK_PATH="${1:-submit/v013_replay_dense_c640/attack.py}"
SDK_ROOT="${SDK_ROOT:-data/raw/ai-agent-security-multi-step-tool-attacks}"
BUDGET_S="${BUDGET_S:-60}"
AGENT="${AGENT:-deterministic}"
export UV_CACHE_DIR="${UV_CACHE_DIR:-/tmp/uv-cache}"

cd "$ROOT_DIR"

PYTHONPATH="$SDK_ROOT${PYTHONPATH:+:$PYTHONPATH}"   uv run python -m aicomp_sdk.cli.main validate redteam "$ATTACK_PATH"

PYTHONPATH="$SDK_ROOT${PYTHONPATH:+:$PYTHONPATH}"   uv run python -m aicomp_sdk.cli.main test redteam "$ATTACK_PATH"   --budget-s "$BUDGET_S" --agent "$AGENT"
