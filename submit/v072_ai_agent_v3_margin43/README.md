# v072 AI Agent V3 Margin43

Single-knob boundary probe from `v071_ai_agent_v3_margin44`.

- Source baseline: `submit/v071_ai_agent_v3_margin44/`
- Code file: `ai-agent-v3-1-2-single-post-exfiltration.ipynb`
- GPU: disabled
- Internet: disabled

## Strategy

- Preserve the public v3.1.2 notebook execution form.
- Keep the successful `v071` single-post attack logic unchanged.
- Change only `MARGIN_S = 44.0` to `43.0`.
- Goal: test whether the no-score boundary is between `42.0` and `43.0`, or whether `43.0` can return more validated candidates than `v071`.

## Validation

- Notebook JSON: valid
- Kernel metadata JSON: valid
- Local notebook execution: passed; generated `attack.py` and placeholder `submission.csv`
- SDK validate: passed
- Deterministic smoke: `0.00`, about `15.2s`
- Notebook hash: `32c64a455059`
- Generated `attack.py` hash: `1fea9394aa99`

## Result

- Kernel: `junichiromorita/ai-agent-security-v072-ai-agent-v3-margin43`
- Kernel version: `1`
- Submission ref: `54492957`
- Status: pending
- Public score: pending
