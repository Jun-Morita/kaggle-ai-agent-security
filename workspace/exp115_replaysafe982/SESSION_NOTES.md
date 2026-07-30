# exp115_replaysafe982

## Hypothesis

The public Silver gap is now large enough that a conservative rerun alone is unlikely to be sufficient. `REPLAY_SAFE_FRAC=0.982` is a higher-risk replay-envelope push designed to recover more returned fired candidates than `v114`, accepting a larger chance of blank / incorrect-format timeout.

## Implementation

- Submission dir: `submit/v115_replaysafe982`
- Baseline: `v110_kaiwalya_classify6`, public `88.605`
- Attack: same single-post `SECRET_MARKER` live validation-fill family
- Change: `REPLAY_SAFE_FRAC=0.97 -> 0.982`

## Validation

- `python3 -m json.tool submit/v115_replaysafe982/ai-agent-security-solution-v9.ipynb`: passed
- `python3 -m py_compile submit/v115_replaysafe982/attack.py`: passed
- `aicomp validate redteam submit/v115_replaysafe982/attack.py`: passed

## Result

- Kernel: `junichiromorita/ai-agent-security-v115-rsf982` version 1
- Competition submission ref: `55030555`
- Status: complete with Kaggle `incorrect format` error as of 2026-07-28
- Hosted output: `attack.py` and `submission.csv` present; hosted `attack.py` SHA-256 matched local (`36e5689cb396` prefix).

## Interpretation

`REPLAY_SAFE_FRAC=0.982` crossed the hosted evaluator envelope. Do not continue increasing replay-safe fraction on this branch without another compensating change such as safer classification or reduced replay pressure.
