# exp023 Results

## 2026-06-20

Candidate:

```text
submit/v023_web2post_short_240_push/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v023_web2post_short_240_push/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v023_web2post_short_240_push/attack.py
./workspace/exp023_web2post_short_240_push/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 26.7s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260620_084735.json`
- Static `env=None` return count: `240`
- Static total user messages: `720`
- Static message length min/mean/max: `32 / 38.0 / 41`
- Kaggle kernel: `junichiromorita/ai-agent-security-v023-web2post-short-240-push`
- Kaggle kernel version: `1`
- Kaggle submission ref: `53862892`
- Kaggle status: complete with blank public score as of 2026-06-20
- Kaggle public score: none

Notes:

- This is a higher-risk scale-up after correcting the stale public-notebook interpretation.
- It intentionally keeps the public V26 candidate generation shape and changes only the candidate count.
- The pulled public kernel output reports proxy validation `http.post` success `416/416`, source success `0/208`, proxy normalized score `35.36`, and public notebook score `56.25`.
- Submitted via `KaggleApi.competition_submit_code()` after the kernel completed.
- Hosted result produced no public score. Treat as no-score / evaluator timeout; the 720-message scale-up exceeded the usable hosted envelope or did not transfer.
