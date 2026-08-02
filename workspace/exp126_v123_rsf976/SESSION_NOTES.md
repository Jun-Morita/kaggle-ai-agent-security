# exp126_v123_rsf976

## Hypothesis

`v123` gives a strong Silver cushion at `REPLAY_SAFE_FRAC=0.975`, and `v122` showed that `0.978` can still score above `91` with the same frame. A smaller `0.976` boundary test may add candidates without destabilizing the replay envelope.

## Base

- `submit/v123_v121_exact_rerun`

## Changes

- `REPLAY_SAFE_FRAC: 0.975 -> 0.976`
- Preserve `FRAME_TEMPLATE`, `SPLIT_CLASSIFY_N=6`, `PROBE_HOPS=0`, and `SLOW_MULTIPOST_N=1`.

## Status

- Submitted on 2026-08-02.
- Kernel: `junichiromorita/ai-agent-security-v126-rsf976` version 1.
- Submission ref: `55167162`.
- Current status: complete.
- Public LB: `87.840` as of 2026-08-02.
- Result: underperformed `v123=91.890`, `v122=91.170`, and `v121=91.260`; `REPLAY_SAFE_FRAC=0.976` is not a useful follow-up in this hosted draw.
