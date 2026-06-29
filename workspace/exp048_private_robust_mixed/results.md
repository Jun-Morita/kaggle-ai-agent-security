# exp048 private robust mixed

## Hypothesis

Pure public `SECRET_MARKER` exfil is narrow. A mixed submission using naked
`sk_live_test`, a small encoded-marker tail, and confused-deputy probes may be
less brittle for private scoring even if public score is lower than `v043`.

## Result

- Kaggle kernel: `junichiromorita/ai-agent-security-v048-private-robust-mixed` v1
- Submission ref: `54111548`
- Public LB: `0.030` as of 2026-06-28
- Local deterministic score: `0.00`
- Local deterministic runtime: about 17.4s
- Static return count: `255`
- Notes: py_compile, ruff, SDK validate, and deterministic smoke passed.
- Interpretation: public score is essentially zero; naked `sk_live_test` and
  the small mixed tail are not useful for public scoring in this form.
