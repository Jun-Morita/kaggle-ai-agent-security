# exp018 Results

## 2026-06-18

Candidate:

```text
submit/v018_replay_dense_classic560/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v018_replay_dense_classic560/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v018_replay_dense_classic560/attack.py
./workspace/exp018_replay_dense_classic560/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 6.6s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260618_211310.json`
- Static `env=None` return count: `400`
- Profile check: `SEARCH_PROFILE=classic560`, `RETURN_TARGET_CANDIDATES=800`, `MIN_RETURN_CANDIDATES=560`, `STATIC_FALLBACK_CANDIDATES=400`, `MAX_MSG_CHARS=260`, `SAFE_TARGET_FACTOR=0.82`
- Kaggle kernel: `junichiromorita/ai-agent-security-v018-replay-dense-classic560`
- Kaggle kernel version: `1`
- Kaggle submission ref: `53808088`
- Kaggle status: `PENDING` as of 2026-06-18 21:31 JST
- Kaggle public score: pending

Notes:

- Main public-upside attempt after v017.
- If it completes near `50.4`, the next safe step may be `classic570`.
