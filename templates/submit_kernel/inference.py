"""Kaggle script kernel source template."""

from pathlib import Path

import pandas as pd

OUTPUT_PATH = Path("submission.csv")


def main() -> None:
    # Replace this with competition-specific inference.
    submission = pd.DataFrame()

    assert not submission.empty, "submission is empty"
    submission.to_csv(OUTPUT_PATH, index=False)
    print(f"saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
