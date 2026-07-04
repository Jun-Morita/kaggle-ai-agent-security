# v055 G1 latency direct

Higher-risk transfer from public `attack-exfil-g1`.

- direct one-message `SECRET_MARKER` exfil prompt
- compact unique `.co` domains
- probes latency with `5` live interactions
- emits at least `300` candidates when hosted budget allows
- can expand up to `520` candidates when probe estimates capacity
- no burst, no multipost, no multi-turn compression

## Result

- Kernel: `junichiromorita/ai-agent-security-v055-g1-latency-direct`
- Kernel version: `1`
- Submission ref: `54234614`
- Status: `Submission Format Error` in Kaggle UI as of 2026-07-04
- Public score:
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 9.5s
- Static env-none return count: `300`
- Hash: `12e57e861a19`

## Interpretation

- Direct `attack-exfil-g1` style latency sizing did not transfer safely in this wrapper.
