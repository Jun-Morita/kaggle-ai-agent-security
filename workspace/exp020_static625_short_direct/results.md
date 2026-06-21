# exp020 Results

## 2026-06-19

Candidate:

```text
submit/v020_static625_short_direct/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v020_static625_short_direct/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v020_static625_short_direct/attack.py
./workspace/exp020_static625_short_direct/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 34.7s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260619_200304.json`
- Static `env=None` return count: `625`
- Static message shape: one message per candidate, exactly 72 chars per message
- Profile check: `RETURN_TARGET_CANDIDATES=625`, `HARD_MAX_CANDIDATES=640`, `MAX_USER_MESSAGE_CHARS=120`, one message per candidate
- Kaggle kernel: `junichiromorita/ai-agent-security-v020-static625-short-direct`
- Kaggle kernel version: `1`
- Kaggle submission ref: `53846429`
- Kaggle status: complete with blank public score as of 2026-06-20
- Kaggle public score: none

Notes:

- Direct static short-message port of `agi-ai-agent-security.ipynb`.
- Expected public score if all candidates replay as one EXFILTRATION finding: `56.250`.
- Hosted result produced no public score. Treat as no-score / evaluator timeout; this stale static interpretation of the public notebook did not transfer.
