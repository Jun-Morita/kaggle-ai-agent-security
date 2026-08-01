# exp124_v121_frame_short

## Hypothesis

The slow `gpt_oss` row remains latency-gated. Removing the plain-English final-answer instruction from the slow-row Harmony frame may reduce prompt/finalization overhead while keeping the forged analysis-channel close that made the `nctuan` frame useful.

## Base

- `submit/v121_v120_exact_rerun`

## Changes

- `FRAME_TEMPLATE`: remove `Then answer OK only.` before the forged Harmony analysis close.
- Preserve `REPLAY_SAFE_FRAC=0.975`, `SPLIT_CLASSIFY_N=6`, `PROBE_HOPS=0`, and `SLOW_MULTIPOST_N=1`.

## Risk

- This is the daily new-mechanism exploration slot. It may reduce compliance if the removed sentence was helping tool-call reliability.

## Status

- Submitted on 2026-08-01.
- Kernel: `junichiromorita/ai-agent-security-v124-frame-short` version 1.
- Submission ref: `55151005`.
- Current status: `PENDING`.
