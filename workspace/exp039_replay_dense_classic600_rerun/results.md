# exp039 Replay Dense classic600 Rerun

## Hypothesis

The current best `v030_replay_dense_classic600` may or may not still score under
the 2026-06-25 evaluator update. A direct rerun gives the cleanest control.

## Source

- `submit/v030_replay_dense_classic600/attack.py`

## Design

- Copy the v030 `attack.py` without changing candidate generation.
- Submit under a new Kaggle kernel slug.
- Compare public score with original `v030 = 54.000`.

## Result

- Kaggle kernel: `junichiromorita/ai-agent-security-v039-classic600-rerun`
- Kaggle kernel version: `1`
- Submission ref: `54042220`
- Kaggle status: `COMPLETE` as of 2026-06-25
- Public LB: `0.540`
- Local deterministic score: `0.00`
- Local deterministic runtime: about 6.3s
- Static return count: `400`
- Notes: `attack.py` sha256 matches `v030` exactly:
  `d1e1d6be26508b7ff03aabfc1a596b51ee41fc98870ae7b30cd89ced3e150091`.
  py_compile, ruff, SDK validate, and deterministic smoke passed.
- The exact rerun collapsed from original `v030=54.000` to `0.540`, matching
  the failed `v034/v035` boundary probes. The old classic family should no
  longer be treated as post-update reliable.
