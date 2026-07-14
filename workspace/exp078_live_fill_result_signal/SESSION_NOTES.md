# exp078 Live Fill Result Signal

## Hypothesis

`v077` checks each live candidate by exporting and scanning the full trace.
The current public Pilkwang single-post implementation instead uses the
interaction result's `successful_tool_calls` field. Keeping the direct prompt,
URL scheme, margin, and live-fill deadline unchanged while removing trace export
may reduce per-candidate collection overhead and increase the returned,
replayable candidate count.

## Controlled Difference From v077

- Baseline: `workspace/exp077_another_approach_exact/attack.py`
- Preserved: `SECRET_MARKER`, direct single-post prompt, `.co` host scheme,
  `MARGIN_S=45.0`, warm-up, 0.95 fill fraction, latency reserve, and fallback.
- Changed: use `result.successful_tool_calls >= 1` from `env.interact()` rather
  than calling `env.export_trace_dict()` and scanning tool events.

## Risk

The result signal confirms a successful tool call but does not independently
confirm the tool name or payload. The fixed direct prompt makes `http.post` the
intended only successful tool action; replay remains authoritative.

## Validation Plan

- Run Python syntax and SDK structure validation.
- Run deterministic smoke to confirm the target SDK exposes the result signal.
- Compare the public live-validation runtime against v077 before considering a
  Kaggle submission.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v078-live-fill-result-signal` v1
- Submission ref: `54589058`
- Status: `PENDING`
- Hosted `attack.py` hash: `3d54b3f82efe`
