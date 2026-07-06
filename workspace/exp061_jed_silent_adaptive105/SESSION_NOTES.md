# exp061 JED Silent Adaptive105

## Hypothesis

`v060` transfers the public `1.2x` deadline margin exactly. This paired
variant takes more risk by lowering the stop margin to `1.05x`, which may
collect more verified candidates if hosted interactions are stable.

## Implementation

- Submission directory: `submit/v061_jed_silent_adaptive105/`
- Same prompt, URL generation, and active predicate verification as `v060`.
- Only `SAFETY_MARGIN` changes from `1.2` to `1.05`.

## Result

- `uv run ruff check submit/v061_jed_silent_adaptive105/attack.py`: passed
- `aicomp_sdk.cli.main validate redteam`: passed
- deterministic smoke: `0.00`, about 44.4s
- Kernel pushed and completed as `junichiromorita/ai-agent-security-v061-jed-silent-adaptive105` version 1.
- Hosted output contains `attack.py` and `submission.csv`.
- Competition submit failed because daily submission allowance was exhausted.
