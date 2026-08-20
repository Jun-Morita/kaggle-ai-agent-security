# exp154_probehops1

## Context

Strategic reconsideration on 2026-08-19 to close the gap to public Silver
(top-5%, currently rank 94 at score `94.375` out of 1885 teams; we sit at
rank 534, score `88.245`). The gap is only `+6.13`, equivalent to roughly
68 more successful EXFILTRATION findings (raw needed ~1226, at 18 raw per
firing candidate). Decision: prioritize throughput levers over predicate
diversity for the next round, since the gap is small and throughput is the
repo's best-understood lever.

## Hypothesis

`PROBE_HOPS=1` (vs the current `0`, meaning "probe at the grader's max hop
cap, today 8") lets the live-fill loop skip the scoring-irrelevant wrap-up
generation during probing, for an estimated ~1.5-2x faster fill per the
code's own comment (validated 12/12 both models that a candidate fires
identically whether probed at 1 or 8 hops, since the exfil event is recorded
at hop-0). Faster fill -> more candidates probed within the time budget ->
more successful firing candidates -> higher raw score.

This exact knob was tried once before, `v111_probehops1_coef18`
(2026-07-26), and completed with a Kaggle "incorrect format" / no-score
result -- but that was PRE-REFRESH (`REPLAY_SAFE_FRAC=0.97`, and critically,
a replay timeout back then zeroed the ENTIRE submission). Post-2026-08-05
(discussion `733058`), a replay timeout now preserves the score accumulated
before it, so the downside of pushing throughput harder is much softer than
when `v111` failed under the old all-or-nothing regime.

## Change

Single-knob change from `submit/v148_replaysafe_postrefresh_push=88.245`:

```
PROBE_HOPS = 0 -> 1
REPLAY_COST_COEF = 1.0 -> 1.8
```

`REPLAY_COST_COEF` scales the under-counted 1-hop probe elapsed time back up
to the estimated hops=8 replay cost so `REPLAY_SAFE_SIZING` doesn't
under-charge and risk a replay-budget overrun; `1.8` is the same pairing
value used in `v111`. Everything else (`REPLAY_SAFE_FRAC=0.985`,
`SPLIT_CLASSIFY_N=6`, template-race classifier) unchanged.

## Expected Readout

- If `v154 > v148=88.245`: the 1-hop probe throughput gain is real under the
  post-refresh regime; consider it the new default and look for further
  throughput levers (e.g. combining with `v150`'s `REPLAY_SAFE_FRAC=0.99` if
  that also lands positive).
- If `v154 < v148`: the `PROBE_HOPS=1` / `REPLAY_COST_COEF=1.8` pairing is
  still unfavorable in this wrapper even post-refresh; retire this knob
  again and look elsewhere (e.g. `v155`'s multipost density, or predicate
  diversity).

## Validation

- `python3 -m py_compile submit/v154_probehops1/attack.py`: passed.
- `diff` against `submit/v148_replaysafe_postrefresh_push/attack.py`:
  confirms single-knob change (`PROBE_HOPS` + `REPLAY_COST_COEF` lines plus
  comment only).
- Notebook cell 0 resynced from the edited `attack.py`.
- `kernel-metadata.json`: valid JSON; id/title updated to
  `ai-agent-security-v154-probehops1`.
- `aicomp_sdk.cli.main validate redteam`: passed.
- `aicomp_sdk.cli.main test redteam --agent deterministic --budget-s 60`:
  completed, score `0.00` (expected smoke-test pattern).

## Submission

- 2026-08-19: pushed to Kaggle as
  `junichiromorita/ai-agent-security-v154-probehops1`, submitted.

## Result (2026-08-20)

Public `77.580`. Regressed below `v148=88.245`. The post-refresh
softened-timeout-penalty theory did not rescue this knob: the 1-hop probe's
fire prediction apparently diverges enough from the real hops=8 replay
outcome that `REPLAY_SAFE_SIZING`'s `REPLAY_COST_COEF=1.8` calibration
either over- or under-charges in practice, producing a worse net outcome
than the proven `PROBE_HOPS=0` baseline. Retired; keep `PROBE_HOPS=0`.
