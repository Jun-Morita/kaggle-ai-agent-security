# exp030 replay-dense classic600

## Hypothesis

`v029_replay_dense_classic590` completed at public `53.100`, exactly matching `590 * 0.09`. This follow-up preserves the successful `classic590` shape and raises only `MIN_RETURN_CANDIDATES` to `600`.

Expected public score if the hosted replay completes at scale: `54.000`.

## Changes from v029

- `SEARCH_PROFILE`: `classic590 -> classic600`
- profile key: `classic590 -> classic600`
- `MIN_RETURN_CANDIDATES`: `590 -> 600`

All other replay/search settings are unchanged.

## Local Checks

- `py_compile`: passed
- Ruff: passed
- SDK validate: passed
- deterministic smoke score: `0.00`
- deterministic smoke runtime: about 6.6s
- static `env=None` return count: `400`
- expected public score: `54.000`

## Submission

- Kernel slug: `junichiromorita/ai-agent-security-v030-replay-dense-classic600`
- Kernel version: `1`
- Submission ref: `53946466`
- Hosted status: `PENDING` as of 2026-06-22 21:50 JST
- Public LB: pending
