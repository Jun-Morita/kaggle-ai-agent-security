# exp090 Raw Weighted Push99

## Hypothesis

`v087` showed that aggressive replay-safe single-message fill is the active
score path. The `pilkwang` / `liubaby` public source is a distinct `0.99`
variant that selects templates by measured raw-per-second rather than only
boolean fire rate and latency.

## Source

- Public Code: `liubabyvstone/ai-security-pilkwang-v3`
- Same source hash observed in `pilkwang/ai-agent-v3-1-2-single-post-exfiltration`
- Pulled: 2026-07-17
- Extracted source hash: `e13fc4b9ea5b`
- Saved raw notebook:
  `references/raw/notebooks/ai-security-pilkwang-v3-20260717.ipynb`

## Implementation

Close source transfer of the raw-weighted `REPLAY_SAFE=0.99` variant:

- `REPLAY_SAFE = 0.99`
- `PROBE_REPS = 5`
- `MIN_FIRE_RATE = 0.2`
- larger template bank including `call_syntax`, `inj_empty`, and `inj_done`
- counts EXFIL events and selects by raw-per-second

## Expected Outcome

This is an independent high-upside branch from `v089`. If the model reliably
fires one of the extra templates faster, it can improve public score. The
larger template bank and raw-weighted selection also make it riskier than the
clean R1-011 transfer.

## Validation

- `python3 -m py_compile`: passed.
- SDK validate: passed.
- Deterministic smoke: passed with score `0.00`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v090-raw-weighted-push99` version 1
- Competition submission ref: `54781620`
- Status: complete with blank public score as of 2026-07-18
- Diagnosis: likely replay failure. Compared with the public 84.87 five-template
  notebook, the raw-weighted branch uses a larger template bank and raw-per-second
  selection, which likely increased variance or over-returned candidates.
