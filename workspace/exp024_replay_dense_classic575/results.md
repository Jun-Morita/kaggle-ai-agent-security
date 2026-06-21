# exp024 Results

## 2026-06-20

Candidate:

```text
submit/v024_replay_dense_classic575/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v024_replay_dense_classic575/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v024_replay_dense_classic575/attack.py
./workspace/exp024_replay_dense_classic575/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 6.5s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260620_210940.json`
- Static `env=None` return count: `400`
- Profile check: `SEARCH_PROFILE=classic575`, `RETURN_TARGET_CANDIDATES=800`, `MIN_RETURN_CANDIDATES=575`, `STATIC_FALLBACK_CANDIDATES=400`, `MAX_MSG_CHARS=260`, `SAFE_TARGET_FACTOR=0.84`
- Kaggle kernel: `junichiromorita/ai-agent-security-v024-replay-dense-classic575`
- Kaggle kernel version: `1`
- Kaggle submission ref: `53881304`
- Kaggle status: `PENDING` as of 2026-06-20 21:11 JST
- Kaggle public score: pending

Notes:

- Boundary probe after v020-v023 no-scored.
- Preserves v019's confirmed classic shape and changes only `MIN_RETURN_CANDIDATES` from `570` to `575`.
- Expected score if it completes at scale: `575 * 18 / 200 = 51.75`.
