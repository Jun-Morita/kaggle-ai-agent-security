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
- Current status: `PENDING`.
