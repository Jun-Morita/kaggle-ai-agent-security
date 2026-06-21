# exp028 replay-dense classic585

## Hypothesis

`v025_replay_dense_classic580` completed at public `52.200`, exactly matching `580 * 0.09`. The next low-risk boundary step is to preserve the successful `classic580` shape and raise only `MIN_RETURN_CANDIDATES` to `585`.

Expected public score if the hosted replay completes at scale: `52.650`.

## Changes from v025

- `SEARCH_PROFILE`: `classic580 -> classic585`
- profile key: `classic580 -> classic585`
- `MIN_RETURN_CANDIDATES`: `580 -> 585`

All other replay/search settings are unchanged.

## Local Checks

- `py_compile`: passed
- Ruff: passed
- SDK validate: passed
- deterministic smoke score: `0.00`
- deterministic smoke runtime: about 6.6s
- static `env=None` return count: `400`
- expected public score: `52.650`

## Submission

- Kernel slug: `junichiromorita/ai-agent-security-v028-replay-dense-classic585`
- Kernel version: `1`
- Submission ref: `53913061`
- Hosted status: `PENDING` as of 2026-06-21 21:28 JST
- Public LB: pending
