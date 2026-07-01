# exp050 Omega URAD hybrid335

## Hypothesis

`v043` succeeded with total return count `335`, while `v046` no-scored at pure
`340`. A hybrid that stays at total `335` but replaces 30 Omega candidates with
the public URAD fallback prompt may preserve runtime safety while improving
model compliance or cell diversity.

## Result

- Kaggle kernel: `junichiromorita/ai-agent-security-v050-omega-urad-hybrid335` v1
- Submission ref: `54170993`
- Public LB: none; complete with blank public score as of 2026-07-01
- Local deterministic score: `0.00`
- Local deterministic runtime: about 22.4s
- Static return count: `335`
- Notes: py_compile, ruff, SDK validate, deterministic smoke, and kernel push passed. Initial submit attempt on 2026-06-28 failed because the daily allowance was exhausted; submitted successfully after reset.
- Interpretation: no-score / replay timeout. Replacing 30 Omega candidates with
  URAD fallback prompts did not preserve `v043` behavior.
