# exp035 replay-dense classic605

## Hypothesis

`v030_replay_dense_classic600` completed at public `54.000`. `v034_replay_dense_classic610` is pending as the aggressive follow-up.

This experiment is a lower-risk insurance submission between them: preserve the successful classic runtime envelope and raise only `MIN_RETURN_CANDIDATES` from `600` to `605`.

Expected public score if hosted replay completes at scale: `54.450`.

## Changes from v030

- `SEARCH_PROFILE`: `classic600 -> classic605`
- profile key: `classic600 -> classic605`
- `MIN_RETURN_CANDIDATES`: `600 -> 605`

All other replay/search settings are unchanged.

## Local Checks

- `py_compile`: passed
- Ruff: passed
- SDK validate: passed
- deterministic smoke score: `0.00`
- deterministic smoke runtime: about 6.3s
- static `env=None` return count: `400`

## Submission

- Kernel slug: `junichiromorita/ai-agent-security-v035-replay-dense-classic605`
- Kernel version: `1`
- Submission ref: `53990711`
- Hosted status: `COMPLETE` as of 2026-06-25
- Public LB: `0.540`

## Result Notes

- Expected score was `54.450`, but hosted public LB was only `0.540`.
- `v035` output contained both `attack.py` and `submission.csv`; local and hosted `attack.py` hashes matched.
- Diff from successful `v030` is limited to `SEARCH_PROFILE` / profile key and `MIN_RETURN_CANDIDATES 600 -> 605`.
- Treat this as a failed boundary probe, not as a missing-output submission-format issue.
