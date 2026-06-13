from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd


def parse_columns(value: str | None) -> list[str] | None:
    if value is None:
        return None
    columns = [column.strip() for column in value.split(",") if column.strip()]
    return columns or None


def require_columns(columns: list[str], available: list[str], label: str) -> list[str]:
    missing = [column for column in columns if column not in available]
    if missing:
        joined = ", ".join(missing)
        raise ValueError(f"{label} not found in submission: {joined}")
    return columns


def validate_submission(
    submission_path: Path,
    sample_path: Path,
    id_columns: list[str] | None = None,
    prediction_columns: list[str] | None = None,
    min_value: float | None = None,
    max_value: float | None = None,
    require_numeric: bool = False,
    check_id_order: bool = True,
) -> list[str]:
    errors: list[str] = []

    sample = pd.read_csv(sample_path)
    submission = pd.read_csv(submission_path)

    sample_columns = list(sample.columns)
    submission_columns = list(submission.columns)

    if submission_columns != sample_columns:
        errors.append(
            "columns differ from sample submission: "
            f"expected={sample_columns}, actual={submission_columns}"
        )

    if len(submission) != len(sample):
        errors.append(f"row count differs: expected={len(sample)}, actual={len(submission)}")

    if not sample_columns:
        errors.append("sample submission has no columns")
        return errors

    id_columns = id_columns or [sample_columns[0]]
    try:
        require_columns(id_columns, submission_columns, "id_columns")
    except ValueError as exc:
        errors.append(str(exc))
        return errors

    if prediction_columns is None:
        prediction_columns = [column for column in sample_columns if column not in id_columns]
    try:
        require_columns(prediction_columns, submission_columns, "prediction_columns")
    except ValueError as exc:
        errors.append(str(exc))
        return errors

    duplicate_count = int(submission.duplicated(subset=id_columns).sum())
    if duplicate_count:
        errors.append(f"duplicated id rows: {duplicate_count}")

    if check_id_order and len(submission) == len(sample):
        expected_ids = sample[id_columns].astype("string").reset_index(drop=True)
        actual_ids = submission[id_columns].astype("string").reset_index(drop=True)
        if not actual_ids.equals(expected_ids):
            errors.append("id order differs from sample submission")

    missing = submission.isna().sum()
    missing = missing[missing > 0]
    if not missing.empty:
        details = ", ".join(f"{column}={count}" for column, count in missing.items())
        errors.append(f"missing values found: {details}")

    if prediction_columns and (require_numeric or min_value is not None or max_value is not None):
        predictions = submission[prediction_columns]
        numeric_predictions = predictions.apply(pd.to_numeric, errors="coerce")
        invalid_numeric = numeric_predictions.isna() & predictions.notna()
        if invalid_numeric.any().any():
            invalid_columns = list(invalid_numeric.any()[invalid_numeric.any()].index)
            errors.append(f"non-numeric prediction values found: {invalid_columns}")
        else:
            if min_value is not None:
                actual_min = float(numeric_predictions.min().min())
                if actual_min < min_value:
                    errors.append(
                        f"prediction min is below limit: min={actual_min}, limit={min_value}"
                    )
            if max_value is not None:
                actual_max = float(numeric_predictions.max().max())
                if actual_max > max_value:
                    errors.append(
                        f"prediction max is above limit: max={actual_max}, limit={max_value}"
                    )

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--submission", required=True, type=Path)
    parser.add_argument("--sample", required=True, type=Path)
    parser.add_argument("--id-columns", default=None)
    parser.add_argument("--prediction-columns", default=None)
    parser.add_argument("--min-value", type=float, default=None)
    parser.add_argument("--max-value", type=float, default=None)
    parser.add_argument("--require-numeric", action="store_true")
    parser.add_argument("--no-check-id-order", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate_submission(
        submission_path=args.submission,
        sample_path=args.sample,
        id_columns=parse_columns(args.id_columns),
        prediction_columns=parse_columns(args.prediction_columns),
        min_value=args.min_value,
        max_value=args.max_value,
        require_numeric=args.require_numeric,
        check_id_order=not args.no_check_id_order,
    )

    if errors:
        print("submission validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("submission validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
