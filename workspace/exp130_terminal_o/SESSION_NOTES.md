# exp130_terminal_o

## Hypothesis

The current best family is gated by gpt_oss throughput. `v124` showed that
removing the terminal instruction from the Harmony frame is unsafe, but discussion
evidence still points to shorter wrap-up generations as the main remaining lever.
Changing `OK` to a one-letter terminal `O` keeps the terminal instruction present
while making the requested final answer shorter.

## Base and Change

- Base: `submit/v123_v121_exact_rerun`
- Only change: `Then answer OK only.` -> `Then answer O only.` in both the plain
  and Harmony frame templates.
- Preserve `REPLAY_SAFE_FRAC=0.975`, `SPLIT_CLASSIFY_N=6`, `PROBE_HOPS=0`,
  `SLOW_MULTIPOST_N=1`, payload, host generation, and replay sizing.

## Validation

- `python3 -m py_compile`: passed.
- Notebook JSON is valid and emits the identical `attack.py`.
- SDK `validate redteam`: passed.
- Deterministic 60-second smoke: completed; expected score `0.00`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v130-terminal-o` version 1.
- Competition submission ref: `55211414`.
- Status: complete.
- Public LB: `89.910` as of 2026-08-05.
- Result: better than recent failed variants, but below `v123=91.890` and below
  the current public Silver boundary.
- Attack SHA-256: `e38d3c0b36`.
