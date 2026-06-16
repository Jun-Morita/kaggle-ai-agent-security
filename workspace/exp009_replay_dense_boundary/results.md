# exp009 Results

## 2026-06-15

Candidate:

```text
submit/v010_replay_dense_boundary/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v010_replay_dense_boundary/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v010_replay_dense_boundary/attack.py
./workspace/exp009_replay_dense_boundary/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 5.5s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260615_211217.json`
- Static `env=None` return count: `300`
- Kaggle kernel: `junichiromorita/ai-agent-security-v010-replay-dense-boundary` v1
- Kaggle submission ref: `53710139`
- Kaggle script version: pending
- Kaggle status: `COMPLETE` as of 2026-06-16
- Kaggle public score: `36.000`

Notes:

- Compare against `v005_trajectory_exfil_aggressive` public score `27.150`.
- Compare against public `Replay-Dense Exfiltration Boundary Search` notebook score `36`.
- This is a replay-hop reduction experiment, not another multi-endpoint mass-shift run.
- Static profile check: `SEARCH_PROFILE=guide16_single_600`, `RETURN_TARGET_CANDIDATES=600`, `MIN_RETURN_CANDIDATES=400`, `DEFAULT_MAX_HOPS=1`, `ENDPOINTS_PER_MSG=1`.
- Kernel push succeeded as version `1`; competition submit succeeded after waiting for the kernel status to become `COMPLETE`.
- This matches the public `Replay-Dense Exfiltration Boundary Search` notebook score and is the current best submission.
