# exp003 Results

## 2026-06-13

Candidate:

```text
submit/v004_trajectory_exfil/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v004_trajectory_exfil/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v004_trajectory_exfil/attack.py
./workspace/exp003_trajectory_exfil/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 17.8s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260613_210800.json`
- Kaggle kernel: `junichiromorita/ai-agent-security-v004-trajectory-exfil` v1
- Kaggle submission ref: `53637051`
- Kaggle script version: `326886459`
- Kaggle status: `SUCCEEDED`
- Kaggle public score: `16.230`

Notes:

- Compare against `v003_broad_prompt_bank` public score `0.630`.
- Public reference target is the rank-9 notebook context: `17.085`.
- Result is slightly below that reference but confirms trajectory-search / bounded-fill is the first high-impact family in this repo.
