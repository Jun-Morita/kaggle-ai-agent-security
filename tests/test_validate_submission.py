from __future__ import annotations

import pandas as pd

from scripts.validate_submission import validate_submission


def test_validate_submission_accepts_matching_file(tmp_path) -> None:
    sample_path = tmp_path / "sample_submission.csv"
    submission_path = tmp_path / "submission.csv"

    pd.DataFrame({"id": [1, 2], "target": [0.0, 0.0]}).to_csv(sample_path, index=False)
    pd.DataFrame({"id": [1, 2], "target": [0.2, 0.8]}).to_csv(submission_path, index=False)

    errors = validate_submission(submission_path, sample_path, id_columns=["id"])

    assert errors == []


def test_validate_submission_catches_id_order(tmp_path) -> None:
    sample_path = tmp_path / "sample_submission.csv"
    submission_path = tmp_path / "submission.csv"

    pd.DataFrame({"id": [1, 2], "target": [0.0, 0.0]}).to_csv(sample_path, index=False)
    pd.DataFrame({"id": [2, 1], "target": [0.8, 0.2]}).to_csv(submission_path, index=False)

    errors = validate_submission(submission_path, sample_path, id_columns=["id"])

    assert "id order differs from sample submission" in errors


def test_validate_submission_allows_string_predictions_by_default(tmp_path) -> None:
    sample_path = tmp_path / "sample_submission.csv"
    submission_path = tmp_path / "submission.csv"

    pd.DataFrame({"id": [1, 2], "label": ["cat", "cat"]}).to_csv(sample_path, index=False)
    pd.DataFrame({"id": [1, 2], "label": ["cat", "dog"]}).to_csv(submission_path, index=False)

    errors = validate_submission(submission_path, sample_path, id_columns=["id"])

    assert errors == []
