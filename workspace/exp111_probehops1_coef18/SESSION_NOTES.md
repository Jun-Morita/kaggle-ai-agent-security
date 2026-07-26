# exp111_probehops1_coef18

## Hypothesis

The current high-80s family is latency-bound. Probing each candidate at one tool hop can make the fill phase cheaper, while `REPLAY_COST_COEF=1.8` conservatively charges the kept candidates for the full replay cost. This may add enough fired candidates to close part of the Silver gap without changing payload, prompt, classification, or multipost behavior.

## Implementation

- Submission dir: `submit/v111_probehops1_coef18`
- Source notebook: `references/raw/notebooks/kaiwalya-ai-agent-security-solution/v009__scriptVersionId-337445891/source.ipynb`
- Baseline: `v106_kaiwalya_solution_v9_exact`, public `88.110`
- Attack: live validation-fill / replay-safe single-hop `SECRET_MARKER`
- Changes:
  - `PROBE_HOPS=0 -> 1`
  - `REPLAY_COST_COEF=1.0 -> 1.8`
- Kept unchanged:
  - `SPLIT_CLASSIFY_N=8`
  - `SLOW_MULTIPOST_N=1`
  - `REPLAY_SAFE_FRAC=0.97`

## Validation

- `python3 -m py_compile submit/v111_probehops1_coef18/attack.py`: passed
- `aicomp validate redteam submit/v111_probehops1_coef18/attack.py`: passed

## Result

- Kernel: `junichiromorita/ai-agent-security-v111-probehops1` version 1
- Competition submission ref: `54988002`
- Status: pending as of 2026-07-26 10:05 JST
