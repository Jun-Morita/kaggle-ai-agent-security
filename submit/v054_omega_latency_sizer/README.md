# v054 Omega latency sizer

Low-risk adaptive follow-up to `v043`.

- uses the `v043` Omega `SECRET_MARKER` phrase bank
- probes single-hop latency with `5` live interactions
- returns at least `330` exfil candidates when hosted budget allows
- can expand up to `360` exfil candidates when the probe estimates capacity
- keeps the `v043` five confused-deputy tail only when staying at the `330` floor
- no burst, no multipost, no multi-turn compression

## Result

- Kernel: `junichiromorita/ai-agent-security-v054-omega-latency-sizer`
- Kernel version: `1`
- Submission ref: `54234607`
- Status: pending as of 2026-07-01
- Public score:
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 9.5s
- Static env-none return count: `335`
- Hash: `e9a7a52d939d`
