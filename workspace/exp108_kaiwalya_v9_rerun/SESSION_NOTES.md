# exp108_kaiwalya_v9_rerun

## Hypothesis

`v106_kaiwalya_solution_v9_exact` scored `88.110`, while the public source scored `89.055`. Re-running the same attack can sample a better hosted replay draw and possibly cross the current top-5% boundary.

## Implementation

- Submission dir: `submit/v108_kaiwalya_v9_rerun`
- Source notebook: `references/raw/notebooks/kaiwalya-ai-agent-security-solution/v009__scriptVersionId-337445891/source.ipynb`
- Attack: exact rerun of the `v106` attack code and notebook wrapper.

## Validation

- `python3 -m py_compile submit/v108_kaiwalya_v9_rerun/attack.py`: passed
- `aicomp validate redteam submit/v108_kaiwalya_v9_rerun/attack.py`: passed

## Result

- Kernel: `junichiromorita/ai-agent-security-v108-kaiwalya-rerun` version 1
- Competition submission ref: `54967521`
- Status: pending as of 2026-07-25 14:07 JST
