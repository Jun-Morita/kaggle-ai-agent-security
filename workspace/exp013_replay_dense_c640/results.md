# exp013 Results

## 2026-06-16

Candidate:

```text
submit/v013_replay_dense_c640/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v013_replay_dense_c640/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v013_replay_dense_c640/attack.py
./workspace/exp013_replay_dense_c640/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 8.5s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260616_222812.json`
- Static `env=None` return count: `400`
- Profile check: `SEARCH_PROFILE=guide22_c640`, `RETURN_TARGET_CANDIDATES=800`, `MIN_RETURN_CANDIDATES=640`, `MAX_MSG_CHARS=260`, `SAFE_TARGET_FACTOR=0.9`
- Kaggle kernel: `junichiromorita/ai-agent-security-v013-replay-dense-c640`
- Kaggle kernel version: `1`
- Kaggle submission ref: `53745360`
- Kaggle status: `COMPLETE` with blank public score as of 2026-06-17 20:57 JST
- Kaggle public score: none; treat as no-score / timeout

Notes:

- High-risk / high-return follow-up to v012.
- This is public-LB upside, not a private-robust hedge.
- Hosted result confirms the `guide22_c640` lower bound is also beyond the stable runtime envelope here.
