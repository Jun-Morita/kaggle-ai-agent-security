# v091 JED 5 Templates Exact099

Exact transfer of the public high-score five-template `REPLAY_SAFE=0.99`
attack.

## Strategy

- Use the public 84.870 `attack_code` exactly.
- Keep the narrow five-template bank.
- Preserve all-latency median fill sizing.
- Use our standard notebook wrapper for `attack.py` and placeholder
  `submission.csv` output.

## Source

- Experiment: `workspace/exp091_jed_5tpl_exact099/`
- Public reference: `assiaben/jed-attack-5-templates-aggressive-replay-0-99`
- Raw notebook:
  `references/raw/notebooks/jed-attack-5-templates-aggressive-replay-0-99.ipynb`
- Source hash: `97a839b8755`

## Status

Submitted to Kaggle.

- `python3 -m py_compile`: passed.
- SDK validate: passed.
- Deterministic smoke: passed with score `0.00`.
- Kernel: `junichiromorita/ai-agent-security-v091-jed-5tpl-exact099`
- Competition submission ref: `54794170`
- Public score: `73.935` as of 2026-07-18
- Status: complete; below `v087=76.950` and `v092=81.540`
