# exp037 k1-short static640 safety

## Hypothesis

`v036_k1_short_static644_working_diary` is an exact transfer at the reported replay wall `N=644`. This follow-up keeps the same notebook execution path but lowers `COUNT` to `640` as a safety backup.

Expected public score if hosted replay completes at scale:

```text
640 * 18 / 200 = 57.60
```

## Changes from v036

- `PROFILE`: `v023_k1_short_static_644 -> v037_k1_short_static_640`
- `COUNT`: `644 -> 640`
- `BASE_HOSTED_SCORE`: `57.96 -> 57.60`

Prompt, URL pattern, payload, and notebook execution path are unchanged.

## Local Checks

- notebook `attack_code` exact match: passed
- `py_compile`: passed
- SDK validate: passed
- deterministic smoke score: `0.00`
- deterministic smoke runtime: about 35.4s
- static return count: `640`
- Ruff: skipped to preserve source shape

## Submission

- Kernel slug: `junichiromorita/ai-agent-security-v037-k1-static640`
- Kernel version: `1`
- Submission ref: `54022607`
- Hosted status: `COMPLETE` as of 2026-06-25
- Public LB: none

## Hosted Pre-submit Output

- Kaggle kernel status: `COMPLETE`
- Output files: `attack.py`, `submission.csv`
- Hosted/local `attack.py` hash: matched

## Result Notes

- Completed with blank public score / no-score.
- Treat as failed transfer despite the lower `COUNT=640` safety setting.
