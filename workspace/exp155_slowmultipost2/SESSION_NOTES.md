# exp155_slowmultipost2

## Context

Strategic reconsideration on 2026-08-19 to close the gap to public Silver
(top-5%, currently rank 94 at score `94.375` out of 1885 teams; we sit at
rank 534, score `88.245`). The gap is only `+6.13`, equivalent to roughly
68 more successful EXFILTRATION findings (raw needed ~1226, at 18 raw per
firing candidate). Decision: prioritize throughput levers over predicate
diversity for the next round.

## Hypothesis

`SLOW_MULTIPOST_N=2` makes the slow (gpt_oss/Harmony) classifier row's
candidates use `_forge_plan_msg`, which forges the reasoning model's
analysis channel to COMMIT to posting the marker to `N` enumerated
endpoints, firing `http.post` once per endpoint within the same candidate's
8-hop trace. If both posts fire, that candidate is worth roughly double the
severity-5 EXFILTRATION raw score for the same wall-clock fill cost -- a
genuine amortization win, not just more probing throughput.

The only prior submission of this knob above `N=1`,
`v107_canqiang_slow_multipost2` (`N=2`, 2026-07-24), regressed to `80.830`.
But that was on a different (canqiang) base and PRE-REFRESH:
`REPLAY_SAFE_FRAC=0.97`, and a replay timeout back then zeroed the entire
submission. Post-2026-08-05 (discussion `733058`), timeouts now preserve
partial score, softening the downside that likely made `v107` look worse
than the underlying technique deserved. The forge mechanism itself was
independently probe-verified (per the code's own comment) at `4.0` firing
posts/candidate at `N=4` on gpt_oss -- `N=2` here is a smaller, safer step.

## Change

Single-knob change from `submit/v148_replaysafe_postrefresh_push=88.245`:

```
SLOW_MULTIPOST_N = 1 -> 2
```

Everything else (`REPLAY_SAFE_FRAC=0.985`, `SPLIT_CLASSIFY_N=6`,
`PROBE_HOPS=0`, template-race classifier) unchanged.

## Expected Readout

- If `v155 > v148=88.245`: multipost density is a genuine post-refresh win;
  consider pushing `N` further (e.g. `3` or `4`, matching the probe-verified
  fire rate at `N=4`).
- If `v155 < v148`: the forge mechanism's fire-rate cost (each extra post is
  a full reasoning generation, ~3.6x replay cost for 4x posts at `N=4` per
  the code's own comment) outweighs the amortization gain in our hosted
  draw even post-refresh; retire multipost again.

## Validation

- `python3 -m py_compile submit/v155_slowmultipost2/attack.py`: passed.
- `diff` against `submit/v148_replaysafe_postrefresh_push/attack.py`:
  confirms single-knob change (`SLOW_MULTIPOST_N` line + comment only).
- Notebook cell 0 resynced from the edited `attack.py`.
- `kernel-metadata.json`: valid JSON; id/title updated to
  `ai-agent-security-v155-slowmultipost2`.
- `aicomp_sdk.cli.main validate redteam`: passed.
- `aicomp_sdk.cli.main test redteam --agent deterministic --budget-s 60`:
  completed, score `0.00` (expected smoke-test pattern).

## Submission

- 2026-08-19: pushed to Kaggle as
  `junichiromorita/ai-agent-security-v155-slowmultipost2`, submitted.

## Result (2026-08-20)

Public `81.365`. Regressed below `v148=88.245`. Combined with `v152`'s
similar collapse for a different compound-instruction shape, this is now
the second piece of evidence that asking the model to perform two actions
in one message reliably costs more fire-rate than the extra
severity/amortization gains it. Retired; keep `SLOW_MULTIPOST_N=1`. See
`exp156_confdeputy_compound/SESSION_NOTES.md` for the follow-up test of
whether this compound-instruction penalty applies even to a fully benign
second action (clean `email.send`, no dangerous content).
