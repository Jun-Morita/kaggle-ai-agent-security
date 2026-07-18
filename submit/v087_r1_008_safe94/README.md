# v087 R1-008 Safe94

Prepared follow-up to `v085`.

## Strategy

- Move from `v085` `REPLAY_SAFE=0.90` to `0.94`.
- Use the current public `R1-008` template bank:
  `plain`, `bare`, `bare_ok`, `call_syntax`, `inj_close`,
  `inj_commentary`.
- Keep replay-cost-capped candidate sizing.

## Source

- Experiment: `workspace/exp087_r1_008_safe94/`
- Public reference: `yusuketogashi/ai-agent-sec-another-approach`
- Raw notebook:
  `references/raw/notebooks/ai-agent-sec-another-approach-20260716.ipynb`

## Status

Complete.

- SDK validate: passed.
- Deterministic smoke: passed with score `0.00`.
- Notebook embedded source hash: matches experiment `attack.py`.
- Kernel: `junichiromorita/ai-agent-security-v087-r1-008-safe94` version 1
- Competition submission ref: `54761706`
- Public score: `76.950` as of 2026-07-17
- Status: current confirmed best; improved over `v085=63.495` by `+13.455`
