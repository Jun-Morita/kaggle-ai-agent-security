# exp019 Results

## 2026-06-18

Candidate:

```text
submit/v019_replay_dense_classic570/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v019_replay_dense_classic570/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v019_replay_dense_classic570/attack.py
./workspace/exp019_replay_dense_classic570/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 6.7s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260618_211310.json`
- Static `env=None` return count: `400`
- Profile check: `SEARCH_PROFILE=classic570`, `RETURN_TARGET_CANDIDATES=800`, `MIN_RETURN_CANDIDATES=570`, `STATIC_FALLBACK_CANDIDATES=400`, `MAX_MSG_CHARS=260`, `SAFE_TARGET_FACTOR=0.84`
- Kaggle kernel: `junichiromorita/ai-agent-security-v019-replay-dense-classic570`
- Kaggle kernel version: `1`
- Kaggle submission ref: `53808128`
- Kaggle status: `PENDING` as of 2026-06-18 21:31 JST
- Kaggle public score: pending

Notes:

- High-upside boundary probe after v017.
- This is close to the failed guide22 `580+` range and may no-score.
