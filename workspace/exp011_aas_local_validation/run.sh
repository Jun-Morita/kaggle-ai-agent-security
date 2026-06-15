#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
export UV_CACHE_DIR="${UV_CACHE_DIR:-/tmp/uv-cache}"

cd "$ROOT_DIR"

uv run python scripts/build_aas_local_validation_kernel.py \
  --attack submit/v010_replay_dense_boundary/attack.py \
  --output-dir workspace/exp011_aas_local_validation/generated/v010 \
  --kernel-id junichiromorita/aas-local-validation-v010-replay-dense-boundary \
  --title "AAS local validation v010 replay dense boundary"

uv run python scripts/build_aas_local_validation_kernel.py \
  --attack submit/v011_single_breadth_500/attack.py \
  --output-dir workspace/exp011_aas_local_validation/generated/v011 \
  --kernel-id junichiromorita/aas-local-validation-v011-single-breadth-500 \
  --title "AAS local validation v011 single breadth 500"

echo "Generated validation kernels under workspace/exp011_aas_local_validation/generated/"
