# exp132_frame_ok_period

## Hypothesis

`v130` showed that changing the terminal phrase can still score, but changing
both plain and frame templates was too broad. This variant changes only the
slow-row Harmony `FRAME_TEMPLATE` and preserves the requested `OK` answer while
dropping `only`, aiming to reduce gpt_oss wrap-up tokens with minimal blast
radius.

## Base and Change

- Base: `submit/v123_v121_exact_rerun`
- Only change: `FRAME_TEMPLATE` terminal wording:
  `Then answer OK only.` -> `Then answer OK.`
- Preserve plain `TEMPLATE`, `REPLAY_SAFE_FRAC=0.975`, `SPLIT_CLASSIFY_N=6`,
  `PROBE_HOPS=0`, `SLOW_MULTIPOST_N=1`, payload, host generation, and replay
  sizing.

## Validation

- `python3 -m py_compile`: passed.
- Notebook JSON is valid and emits the identical `attack.py`.
- SDK `validate redteam`: passed.
- Deterministic 60-second smoke: completed; expected score `0.00`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v132-frame-ok-period` version 1.
- Status: preparing.
- Attack SHA-256: `403432e388`.
