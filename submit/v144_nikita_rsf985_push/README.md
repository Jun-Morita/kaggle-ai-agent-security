# v144 Nikita RSF985 Push

High-risk boundary push from `v143_nikita_ai_security_0011_v20`.

## Strategy

- Base: close transfer of public `nikitagajbhiye30/ai-security-0011` v20.
- Keep the single-post `SECRET_MARKER` live validation-fill family.
- Keep `SPLIT_CLASSIFY_N = 8`, prompt text, frame template, payload, and notebook wrapper.
- Change only the final variant override:
  - `REPLAY_SAFE_FRAC = 0.98 -> 0.985`

## Rationale

`v143` is the safer exact transfer of a public `89.280` post-refresh notebook. This variant intentionally pushes the replay-safe boundary to see whether the same source can return more successful candidates without crossing the hosted replay/output envelope.

## Commands

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run kaggle kernels push -p submit/v144_nikita_rsf985_push

UV_CACHE_DIR=/tmp/uv-cache uv run kaggle competitions submit ai-agent-security-multi-step-tool-attacks \
  -k junichiromorita/ai-agent-security-v144-nikita-rsf985 \
  -v 1 \
  -f submission.csv \
  -m "v144 nikita rsf985 boundary push"
```
