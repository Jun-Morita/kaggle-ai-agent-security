# exp063 JED Silent Notebook With CSV

## Hypothesis

`v060` transferred the attack logic into our standard script-kernel wrapper and
ended as a no-score / `Submission Format Error` class result. The public
notebook may rely on the notebook-kernel execution form, where the cell writes
`/kaggle/working/attack.py` and starts `JEDAttackInferenceServer` directly.

`v062` preserved the notebook form exactly but could not be submitted because
the output did not include the API-named `submission.csv`. This variant adds
only a placeholder `submission.csv` output while leaving attack generation
logic unchanged.

## Implementation

- Submission directory: `submit/v063_jed_silent_notebook_with_csv/`
- Notebook source:
  `submit/v063_jed_silent_notebook_with_csv/jed-silent-notebook-with-csv.ipynb`
- `kernel-metadata.json` uses `kernel_type = notebook` and `code_file` set to
  the copied `.ipynb`.
- GPU and internet disabled for competition compatibility.
- Adds placeholder `/kaggle/working/submission.csv` for submit API compatibility.

## Result

- Kernel pushed and completed as
  `junichiromorita/ai-agent-security-v063-jed-silent-nb-csv` version 1.
- Hosted output contains `attack.py` and `submission.csv`.
- Submitted as ref `54348480`; completed at public `52.430` as of
  2026-07-06.
- This is the current confirmed post-update best. Notebook-form reproduction
  fixed the transfer failure seen in the script-kernel `v060`.
