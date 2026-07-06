# exp062 JED Silent Notebook Exact

## Hypothesis

`v060` transferred the attack logic into our standard script-kernel wrapper and
ended as a no-score / `Submission Format Error` class result. The public
notebook may rely on the notebook-kernel execution form, where the cell writes
`/kaggle/working/attack.py` and starts `JEDAttackInferenceServer` directly.

## Implementation

- Submission directory: `submit/v062_jed_silent_notebook_exact/`
- Copied raw notebook:
  `references/raw/notebooks/jed-attack-silent-no-output-30pct-faster.ipynb`
- `kernel-metadata.json` uses `kernel_type = notebook` and `code_file` set to
  the copied `.ipynb`.
- GPU and internet disabled for competition compatibility.

## Result

- Kernel pushed and completed as
  `junichiromorita/ai-agent-security-v062-jed-silent-notebook-exact` version 1.
- Hosted output contained `attack.py` but not `submission.csv`.
- Competition submit failed with `Did not find provided Notebook Output File`
  when using `-f submission.csv`.
