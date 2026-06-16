# exp010 Results

## 2026-06-15

Candidate:

```text
submit/v011_single_breadth_500/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v011_single_breadth_500/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v011_single_breadth_500/attack.py
./workspace/exp010_single_breadth_500/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 13.1s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260615_214700.json`
- Static `env=None` return count: `500`
- Kaggle kernel: `junichiromorita/ai-agent-security-v011-single-breadth-500` v1
- Kaggle submission ref: `53711101`
- Kaggle script version: pending
- Kaggle status: `COMPLETE` as of 2026-06-16
- Kaggle public score: `32.370`

Notes:

- Compare against pending `v010_replay_dense_boundary`.
- Compare against public `Replay-Dense Exfiltration Boundary Search` score `36`.
- This is the high-risk single-hop breadth profile: theoretical public score is `500 * 18 / 200 = 45`.
- Static profile check: `SEARCH_PROFILE=single_breadth_500`, `RETURN_TARGET_CANDIDATES=500`, `MIN_RETURN_CANDIDATES=360`, `DEFAULT_MAX_HOPS=1`, `ENDPOINTS_PER_MSG=1`, `MAX_SEARCH_S=240.0`.
- Kernel push succeeded as version `1`; competition submit succeeded after waiting for the kernel status to become `COMPLETE`.
- Result is below v010 `36.000`; simply increasing breadth to 500 did not improve public LB.
