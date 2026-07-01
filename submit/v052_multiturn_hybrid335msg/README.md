# v052 Multiturn hybrid335msg

Static adoption from public `multi-turn-exfiltration-with-adaptive-burst`.

- no adaptive probing
- no burst mode
- `155` single-message exfil candidates
- `60` three-message exfil candidates
- total candidates: `215`
- total tool-intent messages: `335`
- theoretical public if all messages replay as findings: `335 * 18 / 200 = 30.150`

## Result

- Kernel: `junichiromorita/ai-agent-security-v052-multiturn-hybrid335msg`
- Kernel version: `1`
- Submission ref: `54212725`
- Status: complete with blank public score as of 2026-07-01
- Public score:
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 15.8s
- Static return count: `215`
- Static user-message count: `335`

## Interpretation

- Treat as no-score / replay timeout.
- `335` user messages in this static multi-turn shape exceed the current practical replay envelope.
