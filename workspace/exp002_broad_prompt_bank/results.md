# exp002 Results

## 2026-06-13

Candidate:

```text
submit/v003_broad_prompt_bank/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v003_broad_prompt_bank/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v003_broad_prompt_bank/attack.py
./workspace/exp002_broad_prompt_bank/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 20.4s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260613_142228.json`
- Kaggle kernel: `junichiromorita/ai-agent-security-v003-broad-prompt-bank` v1
- Kaggle submission ref: `53625867`
- Kaggle status: `PENDING` after repeated CLI checks
- Pending Kaggle public score

Notes:

- This is intentionally riskier than `v002`; it spends budget on broader predicate families.
- Compare against `v002_public_reachable` public score `0.565`.
