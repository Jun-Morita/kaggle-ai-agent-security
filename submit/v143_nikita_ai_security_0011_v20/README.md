# v143 Nikita AI Security 0011 v20

Post-refresh public Code transfer from `nikitagajbhiye30/ai-security-0011` version 20.

- Source public score: `89.280`
- Source script version: `340442178`
- Source path: `/tmp/kaggle-aas-nikita-v20/v020__scriptVersionId-340442178/source.ipynb`
- Strategy family: live validation-fill, single-post `SECRET_MARKER`, Harmony frame, replay-safe sizing
- Notable override: `REPLAY_SAFE_FRAC = 0.98`

Submit with:

```bash
set -a
. ./.env
set +a
UV_CACHE_DIR=/tmp/uv-cache uv run kaggle kernels push -p submit/v143_nikita_ai_security_0011_v20

UV_CACHE_DIR=/tmp/uv-cache uv run kaggle competitions submit \
  ai-agent-security-multi-step-tool-attacks \
  -k junichiromorita/ai-agent-security-v143-nikita-0011-v20 \
  -v 1 \
  -f submission.csv \
  -m "v143 nikita ai security 0011 v20"
```
