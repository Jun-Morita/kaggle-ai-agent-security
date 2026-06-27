# exp047 encoded marker N160

## Hypothesis

The post-update evaluator recognizes reversible encodings for secret
exfiltration. A low-count single-hop probe can test whether encoded
`SECRET_MARKER` scores without using literal `SECRET_MARKER`.

## Result

- Kaggle kernel: `junichiromorita/ai-agent-security-v047-encoded-marker-n160` v1
- Submission ref: `54111527`
- Public LB: pending as of 2026-06-27
- Local deterministic score: `0.00`
- Local deterministic runtime: about 11.6s
- Static return count: `160`
- Notes: py_compile, ruff, SDK validate, and deterministic smoke passed.
