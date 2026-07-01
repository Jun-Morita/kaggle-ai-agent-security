# exp055 G1 latency direct

## Hypothesis

The public `attack-exfil-g1` direct prompt plus latency-aware sizing may transfer
better than our fixed-count Omega variants after the evaluator update.

## Result

- Kaggle kernel: `junichiromorita/ai-agent-security-v055-g1-latency-direct`
- Submission ref: `54234614`
- Public LB: pending as of 2026-07-01
- Local deterministic score: `0.00`
- Local deterministic runtime: about 9.5s
- Static env-none return count: `300`
- Notes: py_compile, ruff, SDK validate, deterministic smoke, kernel push, and competition submit passed. Hash `12e57e861a19`.
