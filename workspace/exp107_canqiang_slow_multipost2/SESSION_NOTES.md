# exp107_canqiang_slow_multipost2

## Hypothesis

Discussion suggests optimized GPT-OSS continuation can improve score per replay second. The `v102` source already contains a Harmony forged multi-post path guarded by latency classification. Setting `SLOW_MULTIPOST_N=2` tests whether the slow row can gain density without over-running replay.

## Implementation

- Submission dir: `submit/v107_canqiang_slow_multipost2`
- Source: `submit/v102_canqiang_ea_b_exact`
- Single change: `SLOW_MULTIPOST_N=1 -> 2`

## Validation

- `python3 -m py_compile submit/v107_canqiang_slow_multipost2/attack.py`: passed
- `aicomp validate redteam submit/v107_canqiang_slow_multipost2/attack.py`: passed

## Result

- Kernel: `junichiromorita/ai-agent-security-v107-slow-mp2` version 1
- Competition submission ref: `54951801`
- Status: pending as of 2026-07-24 22:10 JST
