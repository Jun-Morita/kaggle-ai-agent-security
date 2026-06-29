# exp049 URAD fallback static400

## Hypothesis

The public `Agent-Security Attack Submission` notebook scored `37.675`.
Its full adaptive burst path is risky, but its fallback prompt may have better
public model compliance than our Omega phrase bank. A static 400-candidate port
tests that prompt family without adaptive probing or multi-hop replay cost.

## Result

- Kaggle kernel: `junichiromorita/ai-agent-security-v049-urad-fallback-static400` v1
- Submission ref: `54122297`
- Public LB: none; complete with blank public score as of 2026-06-29
- Local deterministic score: `0.00`
- Local deterministic runtime: about 21.9s
- Static return count: `400`
- Notes: py_compile, ruff, SDK validate, and deterministic smoke passed.
- Interpretation: no-score / replay timeout; `400` URAD fallback-style static
  candidates exceeded the current wrapper envelope.
