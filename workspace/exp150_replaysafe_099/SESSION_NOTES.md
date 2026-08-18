# exp150_replaysafe_099

## Hypothesis

`v148_replaysafe_postrefresh_push` (single-knob `REPLAY_SAFE_FRAC=0.975 -> 0.985`
on the `v140`/`v142` base) scored `88.245`, the new confirmed post-refresh
best (`+0.540` over `v140`/`v142=87.705`). This confirms the 2026-08-05
evaluator change (discussion `733058`, partial score preserved on replay
timeout) softens the downside of a higher safety fraction. This experiment
pushes the same knob one rung further: `0.985 -> 0.99`.

## Change

Single-knob change from `submit/v148_replaysafe_postrefresh_push`:

```
REPLAY_SAFE_FRAC = 0.985 -> 0.99
```

Everything else unchanged.

## Expected Readout

- If `v150 > v148=88.245`: the gain continues; consider a further rung
  (e.g. `0.995`) next.
- If `v150 < v148`: `0.985` is the local optimum for this frame; stop
  pushing this knob and look elsewhere (e.g. combining with `v147`'s
  three-arm classifier, see `exp151`).

## Validation

- `python3 -m py_compile submit/v150_replaysafe_099/attack.py`: passed.
- `diff` against `submit/v148_replaysafe_postrefresh_push/attack.py`:
  confirms single-knob change (`REPLAY_SAFE_FRAC` line + comment only).
- Notebook cell 0 resynced from the edited `attack.py`.
- `kernel-metadata.json`: valid JSON; id/title updated to
  `ai-agent-security-v150-rsf-099`.
- `aicomp_sdk.cli.main validate redteam`: passed.
- `aicomp_sdk.cli.main test redteam --agent deterministic --budget-s 60`:
  completed, score `0.00` (expected smoke-test pattern).

## Submission

- 2026-08-18: pushed to Kaggle as `junichiromorita/ai-agent-security-v150-rsf-099`.
  The GPU worker queue was congested (only 2 concurrent GPU kernel sessions
  allowed account-wide); after ~50 minutes still `KernelWorkerStatus.QUEUED`,
  the polling wait was cancelled by user request, and the kernel itself
  transitioned to `KernelWorkerStatus.CANCEL_ACKNOWLEDGED`. **Not submitted
  to the competition** -- the kernel never reached `COMPLETE`, so no
  `submission.csv` was ever produced or uploaded. Re-push and retry on a
  future session when the GPU queue is less congested.
