# v053 Multiturn conservative250msg

Lower-risk companion to `v052`.

- no adaptive probing
- no burst mode
- `100` single-message exfil candidates
- `50` three-message exfil candidates
- total candidates: `150`
- total tool-intent messages: `250`
- theoretical public if all messages replay as findings: `250 * 18 / 200 = 22.500`

## Result

- Kernel: `junichiromorita/ai-agent-security-v053-mt250`
- Kernel version: `1`
- Submission ref: `54212740`
- Status: complete as of 2026-07-01
- Public score: `21.500`
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 11.3s
- Static return count: `150`
- Static user-message count: `250`

## Interpretation

- Static multi-turn chains can score, but this did not beat `v043=30.170`.
- The result is below the theoretical `22.500`, so not every user message appears to replay as a scored finding.
