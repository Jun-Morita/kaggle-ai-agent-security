# exp151_threearm_rsf985

## Hypothesis

Two independent post-refresh levers both beat `v140`/`v142=87.705` on
2026-08-17:

- `v147_v140_three_arm_race=87.930` (`+0.225`): three-arm classifier race
  between the plain template, verbose Harmony frame, and the short Dimong4
  v16 Harmony frame.
- `v148_replaysafe_postrefresh_push=88.245` (`+0.540`): `REPLAY_SAFE_FRAC`
  raised from `0.975` to `0.985`.

Since these are orthogonal changes (classifier routing vs. replay-safety
sizing), they may stack additively. This experiment combines them.

## Change

Single-knob change from `submit/v147_v140_three_arm_race`:

```
REPLAY_SAFE_FRAC = 0.975 -> 0.985
```

Everything else (the 2+2+2 three-arm classifier, `SPLIT_CLASSIFY_N=6`,
`PROBE_HOPS=0`, `SLOW_MULTIPOST_N=1`) unchanged.

## Expected Readout

- If `v151 > 88.245` (better than both `v147` and `v148` alone): the two
  levers stack additively; promote `v151` as the new baseline.
- If `v151` lands between `v147` and `v148` or below both: the levers
  interfere; keep `v148`'s simpler two-arm base as the baseline instead.

## Validation

- `python3 -m py_compile submit/v151_threearm_rsf985/attack.py`: passed.
- `diff` against `submit/v147_v140_three_arm_race/attack.py`: confirms
  single-knob change (`REPLAY_SAFE_FRAC` line + comment only).
- Notebook cell 0 resynced from the edited `attack.py`.
- `kernel-metadata.json`: valid JSON; id/title updated to
  `ai-agent-security-v151-threearm-rsf985`.
- `aicomp_sdk.cli.main validate redteam`: passed.
- `aicomp_sdk.cli.main test redteam --agent deterministic --budget-s 60`:
  completed, score `0.00` (expected smoke-test pattern).

## Submission

- 2026-08-18: pushed to Kaggle as
  `junichiromorita/ai-agent-security-v151-threearm-rsf985`, kernel completed
  (`KernelWorkerStatus.COMPLETE`), hosted `attack.py` verified to contain
  `REPLAY_SAFE_FRAC = 0.985`, submitted to the competition (submission
  description "v151 three-arm classifier x replay-safe-frac 0.985"). Public
  score pending as of end of day 2026-08-18.
