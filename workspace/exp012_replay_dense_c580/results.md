# exp012 Results

## 2026-06-16

Candidate:

```text
submit/v012_replay_dense_c580/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v012_replay_dense_c580/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v012_replay_dense_c580/attack.py
./workspace/exp012_replay_dense_c580/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 7.8s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260616_221105.json`
- Static `env=None` return count: `400`
- Profile check: `SEARCH_PROFILE=guide22_c580`, `RETURN_TARGET_CANDIDATES=800`, `MIN_RETURN_CANDIDATES=580`, `MAX_MSG_CHARS=260`, `SAFE_TARGET_FACTOR=0.88`
- Kaggle kernel: `junichiromorita/ai-agent-security-v012-replay-dense-c580`
- Kaggle kernel version: `1`
- Kaggle submission ref: `53744896`
- Kaggle status: `COMPLETE` with blank public score as of 2026-06-17 20:57 JST
- Kaggle public score: none; treat as no-score / timeout

Notes:

- This is the first attempt after v010 `36.000` and public `52.2` notebook analysis.
- Preserve `guide22_c580` settings; do not mix in semantic boost or private payload changes in this run.
- Hosted result indicates `MIN_RETURN_CANDIDATES=580` / guide22 shape is too aggressive for this account/runtime path, despite the public reference score.
