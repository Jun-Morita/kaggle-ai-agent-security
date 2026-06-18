# exp016 Results

## 2026-06-18

Candidate:

```text
submit/v016_replay_dense_classic520/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v016_replay_dense_classic520/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v016_replay_dense_classic520/attack.py
./workspace/exp016_replay_dense_classic520/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 7.4s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260618_062240.json`
- Static `env=None` return count: `400`
- Profile check: `SEARCH_PROFILE=guide20_classic520`, `RETURN_TARGET_CANDIDATES=800`, `MIN_RETURN_CANDIDATES=520`, `STATIC_FALLBACK_CANDIDATES=400`, `MAX_MSG_CHARS=260`, `SAFE_TARGET_FACTOR=0.78`
- Kaggle kernel: `junichiromorita/ai-agent-security-v016-replay-dense-classic520`
- Kaggle kernel version: `1`
- Kaggle submission ref: `53787950`
- Kaggle status: `COMPLETE` with blank public score as of 2026-06-18 21:02 JST
- Kaggle public score: none; treat as no-score / evaluator timeout

Notes:

- Controlled follow-up to v014.
- If it completes around `46.8`, the next step is likely `guide20_classic540`.
- If it no-scores, v014's 500 floor is near the stable boundary.
- Because v017 with `MIN_RETURN_CANDIDATES=540` succeeded, this no-score is not a clean count-boundary signal.
