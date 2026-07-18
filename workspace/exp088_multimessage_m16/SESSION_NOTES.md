# exp088 Multi-message M16

## Hypothesis

The current single-message replay-safe family appears to plateau around the
low-to-mid 60s. Public Code from 2026-07-16 suggests the next higher-scoring
direction is multi-message amortization: one candidate contains multiple short
single-post messages, so replay pays the fresh-environment overhead once for
many scored `http.post` events.

## Source

- Public Code: `tensorliu/jed-attack-improved-nb`
- Pulled: 2026-07-16
- Extracted source hash: `aa36e405229e`
- Saved raw notebook:
  `references/raw/notebooks/jed-attack-improved-nb-20260716.ipynb`

## Implementation

Close source transfer of the M=16 multi-message variant:

- `_M = 16`
- `_FILL_FRAC = 0.65`
- `_MARGIN_S = 90.0`
- `_SLOWEST0 = 90.0`
- short `SECRET_MARKER` single-post messages chained inside each candidate
- row routing between bare and routine wording based on measured per-message
  latency

## Expected Outcome

High-risk / high-return. If replay amortizes per-candidate overhead as described
in the public notebook, this can break the single-message public-score plateau.
If long candidate chains are replay-costlier than expected or private replay
times out, it can no-score.

`M=16` is chosen over `M=32` as the first repo test because previous multi-turn
experiments showed chain length can cause evaluator instability.

## Validation

- `python3 -m py_compile`: passed.
- SDK validate: passed.
- Deterministic smoke: completed in about `7.0s`, score `0.00`.
- Notebook embedded source hash matched `workspace/exp088_multimessage_m16/attack.py`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v088-mm16-safe65` version 1
- Competition submission ref: `54761992`
- Status: complete as of 2026-07-17
- Public score: `3.990`
- Result: failed as a score-up path. The M16 multi-message amortization idea did
  not transfer in this form; it likely replayed too slowly or caused much lower
  per-message compliance than the single-message baseline. Avoid this exact
  branch unless a new public notebook demonstrates a reproducible fix.
