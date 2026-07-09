# v073 AI Agent V3 Margin445

Single-knob safety probe from `v071_ai_agent_v3_margin44`.

- Source baseline: `submit/v071_ai_agent_v3_margin44/`
- Code file: `ai-agent-v3-1-2-single-post-exfiltration.ipynb`
- GPU: disabled
- Internet: disabled

## Strategy

- Preserve the public v3.1.2 notebook execution form.
- Keep the successful `v071` single-post attack logic unchanged.
- Change only `MARGIN_S = 44.0` to `44.5`.
- Goal: test whether a tiny safety increase keeps the score near `v071=57.825` while reducing no-score risk.

## Validation

- Notebook JSON: valid
- Kernel metadata JSON: valid
- Local notebook execution: passed; generated `attack.py` and placeholder `submission.csv`
- SDK validate: passed
- Deterministic smoke: `0.00`, about `15.1s`
- Notebook hash: `048d91ff333d`
- Generated `attack.py` hash: `e3b480afd95b`

## Result

- Kernel: `junichiromorita/ai-agent-security-v073-ai-agent-v3-margin445`
- Kernel version: `1`
- Submission ref: `54492959`
- Status: complete with blank public score
- Public score:

## Interpretation

The `MARGIN_S=44.5` safety probe did not transfer. Keep `v071` as the active
best unless `v072` completes with a higher score.
