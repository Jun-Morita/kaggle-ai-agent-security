# exp007 Results

## 2026-06-14

Candidate:

```text
workspace/exp007_v008_parameterized/attack.py
```

Checks:

```bash
python3 -m py_compile workspace/exp007_v008_parameterized/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check workspace/exp007_v008_parameterized/attack.py scripts/measure_candidate_posts.py
./workspace/exp007_v008_parameterized/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 11.2s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260614_195624.json`
- Static return count: `96`
- Kaggle kernel: `junichiromorita/ai-agent-security-v008-timeout-safe-multipost` v1
- Kaggle submission ref: `53671096`
- Kaggle script version: pending
- Kaggle status: `PENDING` as of 2026-06-14 20:14 JST
- Kaggle public score: pending

Notes:

- v006 timeout changed the default `V008_PARAMS` from a 240-candidate midpoint to a 96-candidate timeout-safe multipost fallback.
- Submitted before v007 finished to measure a much smaller multipost runtime envelope.
