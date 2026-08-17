# exp148_replaysafe_postrefresh_push

## Hypothesis

The current post-refresh best `v140=87.705` (== `submit/v128_template_race`,
unchanged) still uses `REPLAY_SAFE_FRAC = 0.975`, the same conservative value
chosen pre-refresh specifically to avoid the old failure mode where a replay
timeout during Phase-2 scoring zeroed the ENTIRE submission score. Discussion
`733058` (2026-08-05, "[IMPORTANT] Upcoming Evaluation Updates and Leaderboard
Refresh", organizer MartynaPlomecka) states:

> Partial scores preserved during replay timeouts: Public and private replays
> will now preserve the score accumulated before a timeout instead of
> returning 0.0.

No post-refresh submission (v137-v147) has changed `REPLAY_SAFE_FRAC` on the
current best base to test whether the safety margin can now be relaxed. The
only post-refresh frac variant tried was `v141` (rerun of `v122`, which used
`REPLAY_SAFE_FRAC=0.978` AND a different base frame -- the nctuan frame, not
the `v128` template-race frame), which scored a confounded `75.960`, well
below `v140/v142=87.705`. That result cannot isolate the frac effect from the
frame effect.

Pre-refresh, this same frac knob was tested multiple times on frame-matched
bases and was NOT monotonic:
- `v120/v121` (rsf975): `89.640` / `91.260`
- `v122` (rsf978, same nctuan frame): `91.170` (below `v121` exact rerun)
- `v126` (rsf976, v123 frame): `87.840` (below `v123=91.890`)
- `v127` (rsf978 recheck, v123 frame): `84.060` (below `v123`, "high variance")

All of that evidence assumes a timeout wipes the whole score. Under the new
partial-score-preserving replay, a higher frac (fill closer to the wall) has a
softer downside than it used to, so the old boundary evidence may no longer
generalize.

## Change

Single-knob change from `submit/v128_template_race` (the exact source of the
current best `v140`/`v142=87.705`):

```
REPLAY_SAFE_FRAC = 0.975 -> 0.985
```

Everything else (frame, `SPLIT_CLASSIFY_N=6`, `PROBE_HOPS=0`,
`SLOW_MULTIPOST_N=1`, template-race classifier) is unchanged.

## Expected Readout

- If `v148 >= v140=87.705`: the safety fraction should move up as the new
  post-refresh default; try a further push (e.g. 0.99) next.
- If `v148 < v140`: the frac boundary itself, not just the old all-or-nothing
  timeout penalty, is still the limiting factor; keep `0.975` and look
  elsewhere for gains.

## Validation

- `python3 -m py_compile submit/v148_replaysafe_postrefresh_push/attack.py`: passed.
- `diff` against `submit/v128_template_race/attack.py`: confirms single-knob
  change (`REPLAY_SAFE_FRAC` line + explanatory comment only).
- Notebook JSON regenerated: cell 0 source resynced from the edited
  `attack.py` (`%%writefile /kaggle/working/attack.py` + full source).
- `kernel-metadata.json`: valid JSON; `id`/`title` updated to
  `ai-agent-security-v148-rsf-postrefresh-push`.
- `aicomp_sdk.cli.main validate redteam`: passed.
- `aicomp_sdk.cli.main test redteam --agent deterministic --budget-s 60`:
  completed in 76.1s, score `0.00` (expected -- the deterministic agent does
  not exercise the live-fill path meaningfully; matches prior experiments'
  smoke-test pattern).

## Submission

- 2026-08-17: pushed to Kaggle as
  `junichiromorita/ai-agent-security-v148-rsf-postrefresh-push`, submitted to
  the competition. See `submit/SUBMISSIONS.md` for the ref and result.
