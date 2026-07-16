# v088 Multi-message M16

High-risk / high-return branch based on public multi-message amortization Code.

## Strategy

- One `AttackCandidate` contains `16` short user messages.
- Each message asks for one `SECRET_MARKER` `http.post`.
- The approach tries to amortize fresh-env replay overhead across multiple
  scored exfiltration events.
- Uses measured fill sizing with `_FILL_FRAC = 0.65`.

## Source

- Experiment: `workspace/exp088_multimessage_m16/`
- Public reference: `tensorliu/jed-attack-improved-nb`
- Raw notebook:
  `references/raw/notebooks/jed-attack-improved-nb-20260716.ipynb`

## Status

Submitted to Kaggle.

- SDK validate: passed.
- Deterministic smoke: passed with score `0.00`.
- Notebook embedded source hash: matches experiment `attack.py`.
- Kernel: `junichiromorita/ai-agent-security-v088-mm16-safe65` version 1
- Competition submission ref: `54761992`
- Status: pending as of 2026-07-16
