# exp025 Results

## 2026-06-20

Candidate:

```text
submit/v025_replay_dense_classic580/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v025_replay_dense_classic580/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v025_replay_dense_classic580/attack.py
./workspace/exp025_replay_dense_classic580/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 6.3s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260620_211940.json`
- Static `env=None` return count: `400`
- Profile check: `SEARCH_PROFILE=classic580`, `RETURN_TARGET_CANDIDATES=800`, `MIN_RETURN_CANDIDATES=580`, `STATIC_FALLBACK_CANDIDATES=400`, `MAX_MSG_CHARS=260`, `SAFE_TARGET_FACTOR=0.84`
- Kaggle kernel: `junichiromorita/ai-agent-security-v025-replay-dense-classic580`
- Kaggle kernel version: `1`
- Kaggle submission ref: `53881541`
- Kaggle status: `PENDING` as of 2026-06-20 21:21 JST
- Kaggle public score: pending

Notes:

- High-risk boundary probe after v020-v023 no-scored.
- Preserves v019's confirmed classic shape and changes only `MIN_RETURN_CANDIDATES` from `570` to `580`.
- Expected score if it completes at scale: `580 * 18 / 200 = 52.2`.
