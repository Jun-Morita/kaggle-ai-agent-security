# exp131_frame_say_ok

## Hypothesis

The active `v123` family is still the best scoring branch, but public Silver
cushion is shrinking. The next useful work is a tightly scoped slow-row latency
test. Replacing only the Harmony `FRAME_TEMPLATE` terminal phrase from
`Then answer OK only.` to `Then say OK only.` may shorten gpt_oss finalization
without touching the plain classification probes or gemma-oriented path.

## Base and Change

- Base: `submit/v123_v121_exact_rerun`
- Only change: `FRAME_TEMPLATE` terminal wording:
  `Then answer OK only.` -> `Then say OK only.`
- Preserve plain `TEMPLATE`, `REPLAY_SAFE_FRAC=0.975`, `SPLIT_CLASSIFY_N=6`,
  `PROBE_HOPS=0`, `SLOW_MULTIPOST_N=1`, payload, host generation, and replay
  sizing.

## Validation

- `python3 -m py_compile`: passed.
- Notebook JSON is valid and emits the identical `attack.py`.
- SDK `validate redteam`: passed.
- Deterministic 60-second smoke: completed; expected score `0.00`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v131-frame-say-ok` version 1.
- Status: preparing.
- Attack SHA-256: `55ffdb66fe`.
