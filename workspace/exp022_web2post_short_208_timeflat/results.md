# exp022 Results

## 2026-06-20

Candidate:

```text
submit/v022_web2post_short_208_timeflat/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v022_web2post_short_208_timeflat/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v022_web2post_short_208_timeflat/attack.py
./workspace/exp022_web2post_short_208_timeflat/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 21.8s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260620_081144.json`
- Static `env=None` return count: `208`
- Static total user messages: `624`
- Static message length min/mean/max: `32 / 38.0 / 41`
- Kaggle kernel: `junichiromorita/ai-agent-security-v022-web2post-short-208-timeflat`
- Kaggle kernel version: `1`
- Kaggle submission ref: `53862744`
- Kaggle status: complete with blank public score as of 2026-06-20
- Kaggle public score: none

Notes:

- This is the first attempt after correcting the stale public-notebook interpretation.
- It intentionally keeps the public V26 candidate generation shape and only wraps it in our existing script-kernel submission harness.
- The pulled public kernel output reports proxy validation `http.post` success `416/416`, source success `0/208`, proxy normalized score `35.36`, and public notebook score `56.25`.
- `uv run kaggle competitions submit ...` returned a generic `400`, but calling `KaggleApi.competition_submit_code()` directly with the same kernel/version succeeded and returned ref `53862744`.
- Hosted result produced no public score. Treat as no-score / evaluator timeout; the public V26 web2post notebook did not transfer through this script-kernel submission path.
