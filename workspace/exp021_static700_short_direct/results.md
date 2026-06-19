# exp021 Results

## 2026-06-19

Candidate:

```text
submit/v021_static700_short_direct/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v021_static700_short_direct/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v021_static700_short_direct/attack.py
./workspace/exp021_static700_short_direct/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 40.9s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260619_200938.json`
- Static `env=None` return count: `700`
- Static message shape: one message per candidate, exactly 72 chars per message
- Profile check: `RETURN_TARGET_CANDIDATES=700`, `HARD_MAX_CANDIDATES=720`, `MAX_USER_MESSAGE_CHARS=120`, one message per candidate
- Kaggle kernel: `junichiromorita/ai-agent-security-v021-static700-short-direct`
- Kaggle kernel version: `1`
- Kaggle submission ref: `53846620`
- Kaggle status: `PENDING` as of 2026-06-19 20:11 JST
- Kaggle public score: pending

Notes:

- High-upside static short-message extension of `v020`.
- Expected public score if all candidates replay as one EXFILTRATION finding: `63.000`.
