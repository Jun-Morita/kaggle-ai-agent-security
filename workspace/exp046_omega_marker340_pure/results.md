# exp046 Omega marker340 pure

## Hypothesis

`v043` showed that `330` Omega-style `SECRET_MARKER` exfil candidates plus
`5` deputy probes can score, while `v044` showed that `350` exfil plus `5`
deputy probes no-scores. Removing the deputy tail may allow `340` pure exfil
candidates to stay inside the current replay boundary.

## Result

- Kaggle kernel: `junichiromorita/ai-agent-security-v046-omega-marker340-pure` v1
- Submission ref: `54103865`
- Public LB: none; complete with blank public score as of 2026-06-27
- Local deterministic score: `0.00`
- Local deterministic runtime: about 22.4s
- Static return count: `340`
- Notes: py_compile, ruff, SDK validate, and deterministic smoke passed.
- Interpretation: no-score / replay timeout. Current viable Omega boundary is
  below pure `N=340`; `v043` remains the best post-update submission.
