# v116_foysal_v12_exact

Exact-style transfer of public Code `foysalemonshanto/ai-agent-security-v12` version 2, public score `89.190`.

## Rationale

- Current repo best is `v110_kaiwalya_classify6`, public `88.605`.
- Recent replay-safe fraction pushes underperformed or failed:
  - `v114` (`REPLAY_SAFE_FRAC=0.978`) scored `87.975`.
  - `v115` (`REPLAY_SAFE_FRAC=0.982`) produced Kaggle `incorrect format`.
- Foysal v12 version 2 is the strongest newly found public source above our best and stays in the same proven single-post `SECRET_MARKER` live validation-fill family.

## Source

- Kaggle Code: `foysalemonshanto/ai-agent-security-v12`
- Version: `2`
- Script version id: `337777744`
- Public LB: `89.190`

## Expected Behavior

The notebook writes `/kaggle/working/attack.py` and then runs the competition `JEDAttackInferenceServer`. On commit runs it writes a placeholder `submission.csv`; on competition rerun the gateway writes the real scored `submission.csv`.
