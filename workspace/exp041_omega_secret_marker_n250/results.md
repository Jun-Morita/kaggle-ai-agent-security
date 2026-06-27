# exp041 Omega SECRET_MARKER N250

## Hypothesis

The post-update replay boundary is between `N=100` and `N=400`. Public Omega
N250 demonstrates a `SECRET_MARKER` phrase-diverse attack that scores `22.825`,
so a close port should recover a usable post-update public score.

## Source

- `references/raw/notebooks/omega-attack-v9-0-secret-marker-n250.ipynb`

## Design

- Preserve Omega candidate count and phrase allocation.
- Use the repo's stable script-kernel wrapper.
- Do not scale count or change payload in the first port.

## Result

- Kaggle kernel: `junichiromorita/ai-agent-security-v041-omega-marker250`
- Kaggle kernel version: `1`
- Submission ref: `54075682`
- Kaggle status: `COMPLETE` as of 2026-06-27
- Public LB: `22.545`
- Local deterministic score: `0.00`
- Local deterministic runtime: about 14.4s
- Static return count: `255`
- Notes: py_compile, ruff, SDK validate, and deterministic smoke passed.
  Submitted to Kaggle as version 1.
- Score is close to the `250 * 18 / 200 = 22.5` exfil baseline and below the
  public reference `22.825`.
