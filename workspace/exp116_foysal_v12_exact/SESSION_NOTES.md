# exp116_foysal_v12_exact

## Hypothesis

Public Code `foysalemonshanto/ai-agent-security-v12` version 2 scored `89.190`, above our current repo best `v110=88.605`. Its attack is nearly identical to our proven high-80 single-post `SECRET_MARKER` live validation-fill family, with the key source-level difference from `v110` being `SPLIT_CLASSIFY_N=8` instead of `6`. An exact-style transfer may recover the public source's better hosted draw or safer latency classification.

## Implementation

- Submission dir: `submit/v116_foysal_v12_exact`
- Source notebook: `foysalemonshanto/ai-agent-security-v12` version 2, scriptVersionId `337777744`
- Public source score: `89.190`
- Attack family: single-post `SECRET_MARKER`, live keep-only-fired validation-fill, replay-safe sizing, latency split
- Local extracted attack SHA-256 prefix: `3867ef52aa19`

## Validation

- `python3 -m json.tool submit/v116_foysal_v12_exact/ai-agent-security-v12.ipynb`: passed
- `python3 -m py_compile submit/v116_foysal_v12_exact/attack.py`: passed
- `aicomp validate redteam submit/v116_foysal_v12_exact/attack.py`: passed

## Result

- Kernel: `junichiromorita/ai-agent-security-v116-foysal-v12` version 1
- Competition submission ref: `55056719`
- Status: pending as of 2026-07-28 22:54 JST

## Interpretation

Pending.
