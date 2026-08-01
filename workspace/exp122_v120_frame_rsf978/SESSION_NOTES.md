# exp122_v120_frame_rsf978

## Hypothesis

The `v120` nctuan frame succeeded at `REPLAY_SAFE_FRAC=0.975`. A small increase to `0.978` may add enough candidates to approach the silver boundary while keeping replay/runtime risk moderate.

## Base

- `submit/v120_v110_nctuan_frame_rsf975`

## Changes

- `REPLAY_SAFE_FRAC: 0.975 -> 0.978`
- Same frame, classify count, probe hops, and multipost setting as `v120`.

## Status

- Submitted on 2026-07-31.
- Kernel: `junichiromorita/ai-agent-security-v122-frame-rsf978` version 1.
- Submission ref: `55132440`.
- Current status: complete.
- Public LB: `91.170`.
- Result note: improved over `v120=89.640`, but slightly below exact-rerun `v121=91.260`. `REPLAY_SAFE_FRAC=0.978` is viable with the `v120` frame, but the exact rerun is the better current final candidate.
