# exp015 Results

## 2026-06-17

Candidate:

```text
submit/v015_replay_dense_n800/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v015_replay_dense_n800/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v015_replay_dense_n800/attack.py
./workspace/exp015_replay_dense_n800/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 7.5s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260617_212655.json`
- Static `env=None` return count: `400`
- Profile check: `SEARCH_PROFILE=guide18_n800`, `RETURN_TARGET_CANDIDATES=800`, `MIN_RETURN_CANDIDATES=400`, `STATIC_FALLBACK_CANDIDATES=400`, `MAX_MSG_CHARS=400`
- Kaggle kernel: `junichiromorita/ai-agent-security-v015-replay-dense-n800`
- Kaggle kernel version: `1`
- Kaggle submission ref: `53775486`
- Kaggle status: `PENDING` as of 2026-06-17 21:28 JST
- Kaggle public score: pending

Notes:

- Safe backup while v014 is pending.
- If this no-scores, even the `400` floor plus raised target/static count is too much for hosted runtime.
