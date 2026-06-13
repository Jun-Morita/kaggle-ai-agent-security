#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

CONFIG_PATH="${1:-config.yaml}"

# Edit this command for each competition.
uv run python train.py --config "$CONFIG_PATH"
