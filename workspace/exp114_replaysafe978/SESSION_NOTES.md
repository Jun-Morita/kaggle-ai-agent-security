# exp114_replaysafe978

## Hypothesis

`v110=88.605` is about eleven clean single-post findings short of the 2026-07-27 top-5% boundary (`89.595`). Classification reduction beyond `6` underperformed, and probe-hop changes failed. A small replay-safe fraction increase may return enough additional validated candidates while staying below the evaluator-envelope failure boundary.

## Implementation

- Submission dir: `submit/v114_replaysafe978`
- Baseline: `v110_kaiwalya_classify6`, public `88.605`
- Attack: same single-post `SECRET_MARKER` live validation-fill family
- Change: `REPLAY_SAFE_FRAC=0.97 -> 0.978`

## Validation

- `python3 -m json.tool submit/v114_replaysafe978/ai-agent-security-solution-v9.ipynb`: passed
- `python3 -m py_compile submit/v114_replaysafe978/attack.py`: passed
- `aicomp validate redteam submit/v114_replaysafe978/attack.py`: passed

## Result

- Kernel: `junichiromorita/ai-agent-security-v114-rsf978` version 1
- Competition submission ref: `55030557`
- Status: complete as of 2026-07-28
- Public LB: `87.975`
- Hosted output: `attack.py` and `submission.csv` present; hosted `attack.py` SHA-256 matched local (`d4f44adc35b2` prefix).

## Interpretation

The replay-safe fraction increase completed, but scored below `v110=88.605`. Treat `REPLAY_SAFE_FRAC=0.978` as negative evidence for this `SPLIT_CLASSIFY_N=6` branch; the extra pressure likely reduces the effective replay-safe set or increases hosted variance without enough upside.
