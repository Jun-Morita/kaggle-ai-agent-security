# v078 Live Fill Result Signal

Controlled throughput experiment from `v077_another_approach_exact`.

## Strategy

- Preserve the `SECRET_MARKER` single-post live-fill strategy from v077.
- Preserve its prompt, `.co` unique-host sequence, `MARGIN_S=45.0`, untimed
  warm-up, and `FILL_BUDGET_FRAC=0.95`.
- Replace per-candidate trace export and tool-event scanning with the
  `EnvInteractionResult.successful_tool_calls` signal returned by
  `env.interact()`.

## Intended Measurement

The only intended behavior change is one fewer RemoteEnv round trip per live
candidate. Replay remains authoritative, so a public-score change measures
whether this reduced collection overhead returns more replayable candidates.

## Status

Submitted as Kaggle Kernel version 1.

- Kernel: `junichiromorita/ai-agent-security-v078-live-fill-result-signal`
- Submission ref: `54589058`
- Status: complete; public score `60.750`
- Python syntax, SDK validation, Ruff, Notebook preflight, and hosted-output
  hash verification: passed.
