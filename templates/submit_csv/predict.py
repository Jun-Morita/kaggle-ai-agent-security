from pathlib import Path

import pandas as pd


def main() -> None:
    output_path = Path("submission.csv")

    # Replace this with competition-specific inference.
    submission = pd.DataFrame()

    if submission.empty:
        raise RuntimeError("submission is empty. Implement inference before running submit.")

    submission.to_csv(output_path, index=False)
    print(f"saved: {output_path}")


if __name__ == "__main__":
    main()
