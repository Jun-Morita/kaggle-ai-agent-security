# exp110_kaiwalya_classify6

## Hypothesis

The `v109` `SPLIT_CLASSIFY_N=4` latency cut was too aggressive and produced an incorrect-format/no-score result. A middle rung, `SPLIT_CLASSIFY_N=6`, may reclaim some classification overhead while staying closer to the scoring `v106` behavior.

## Implementation

- Submission dir: `submit/v110_kaiwalya_classify6`
- Source notebook: `references/raw/notebooks/kaiwalya-ai-agent-security-solution/v009__scriptVersionId-337445891/source.ipynb`
- Baseline: `v106_kaiwalya_solution_v9_exact`, public `88.110`
- Attack: live validation-fill / replay-safe single-hop `SECRET_MARKER`
- Change: `SPLIT_CLASSIFY_N=8 -> 6`

## Validation

- `python3 -m py_compile submit/v110_kaiwalya_classify6/attack.py`: passed
- `aicomp validate redteam submit/v110_kaiwalya_classify6/attack.py`: passed

## Result

- Kernel: `junichiromorita/ai-agent-security-v110-classify6` version 1
- Competition submission ref: `54975832`
- Status: pending as of 2026-07-25 21:54 JST
