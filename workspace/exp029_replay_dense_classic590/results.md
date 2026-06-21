# exp029 replay-dense classic590

## Hypothesis

`v025_replay_dense_classic580` completed at public `52.200`, exactly matching `580 * 0.09`. This higher-risk companion to `v028` preserves the successful `classic580` shape and raises only `MIN_RETURN_CANDIDATES` to `590`.

Expected public score if the hosted replay completes at scale: `53.100`.

## Changes from v025

- `SEARCH_PROFILE`: `classic580 -> classic590`
- profile key: `classic580 -> classic590`
- `MIN_RETURN_CANDIDATES`: `580 -> 590`

All other replay/search settings are unchanged.

## Local Checks

- `py_compile`: passed
- Ruff: passed
- SDK validate: passed
- deterministic smoke score: `0.00`
- deterministic smoke runtime: about 6.4s
- static `env=None` return count: `400`
- expected public score: `53.100`

## Submission

- Kernel slug: `junichiromorita/ai-agent-security-v029-replay-dense-classic590`
- Kernel version: `1`
- Submission ref: `53913086`
- Hosted status: `PENDING` as of 2026-06-21 21:29 JST
- Public LB: pending
