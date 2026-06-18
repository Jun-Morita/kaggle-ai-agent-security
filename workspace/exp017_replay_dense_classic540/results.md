# exp017 Results

## 2026-06-18

Candidate:

```text
submit/v017_replay_dense_classic540/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v017_replay_dense_classic540/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v017_replay_dense_classic540/attack.py
./workspace/exp017_replay_dense_classic540/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 7.4s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260618_062939.json`
- Static `env=None` return count: `400`
- Profile check: `SEARCH_PROFILE=guide20_classic540`, `RETURN_TARGET_CANDIDATES=800`, `MIN_RETURN_CANDIDATES=540`, `STATIC_FALLBACK_CANDIDATES=400`, `MAX_MSG_CHARS=260`, `SAFE_TARGET_FACTOR=0.8`
- Kaggle kernel: `junichiromorita/ai-agent-security-v017-replay-dense-classic540`
- Kaggle kernel version: `1`
- Kaggle submission ref: `53788043`
- Kaggle status: `COMPLETE` as of 2026-06-18 21:02 JST
- Kaggle public score: `48.600`

Notes:

- Controlled follow-up to v014/v016.
- If this completes near `48.6`, the 540 floor is viable.
- If it no-scores, the safe boundary likely lies below 540.
- Result confirms the 540 floor is viable and becomes the new repo best.
