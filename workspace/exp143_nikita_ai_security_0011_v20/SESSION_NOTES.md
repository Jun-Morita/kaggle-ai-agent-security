# exp143_nikita_ai_security_0011_v20

## Hypothesis

Post-refresh public Code `nikitagajbhiye30/ai-security-0011` version 20 scored `89.280`, above the current repo post-refresh best `v140=87.705`. A close notebook-form transfer may recover some of that throughput.

## Source

- Kernel: `nikitagajbhiye30/ai-security-0011`
- Version: `20`
- Script version: `340442178`
- Public LB: `89.280`
- Downloaded source: `/tmp/kaggle-aas-nikita-v20/v020__scriptVersionId-340442178/source.ipynb`

## Implementation

- Copied source notebook to `submit/v143_nikita_ai_security_0011_v20/ai-security-0011-v20.ipynb`.
- Extracted embedded `attack_code` to `submit/v143_nikita_ai_security_0011_v20/attack.py` for local validation.
- Added private Kaggle kernel metadata with competition source and T4 machine shape.

## Notes

- The source uses the familiar single-post `SECRET_MARKER` live validation-fill branch.
- The source has `SPLIT_CLASSIFY_N = 8`, `REPLAY_SAFE_SIZING = True`, and a final variant override `REPLAY_SAFE_FRAC = 0.98`.
- This is a trial branch, not the current final candidate unless it beats `v140`.
