# exp014 Results

## 2026-06-17

Candidate:

```text
submit/v014_replay_dense_classic500/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v014_replay_dense_classic500/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v014_replay_dense_classic500/attack.py
./workspace/exp014_replay_dense_classic500/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 6.6s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260617_211351.json`
- Static `env=None` return count: `400`
- Profile check: `SEARCH_PROFILE=guide20_classic500`, `RETURN_TARGET_CANDIDATES=800`, `MIN_RETURN_CANDIDATES=500`, `MAX_MSG_CHARS=260`, `SAFE_TARGET_FACTOR=0.78`
- Kaggle kernel: `junichiromorita/ai-agent-security-v014-replay-dense-classic500`
- Kaggle kernel version: `1`
- Kaggle submission ref: `53775306`
- Kaggle status: `PENDING` as of 2026-06-17 21:21 JST
- Kaggle public score: pending

Notes:

- This is the first post-guide22-timeout recovery attempt.
- The target public range is above v010 `36.000` but below the failed guide22 `580+` floor.
