from __future__ import annotations

import math

import numpy as np

from kaggle_agent_template.metrics import binary_log_loss, mae, rmse


def test_rmse_uses_hand_checked_case() -> None:
    y_true = np.array([1.0, 2.0, 3.0])
    y_pred = np.array([1.0, 4.0, 3.0])

    assert rmse(y_true, y_pred) == math.sqrt(4.0 / 3.0)


def test_mae_uses_hand_checked_case() -> None:
    y_true = np.array([1.0, 2.0, 3.0])
    y_pred = np.array([2.0, 2.0, 5.0])

    assert mae(y_true, y_pred) == 1.0


def test_binary_log_loss_uses_hand_checked_case() -> None:
    y_true = np.array([1.0, 0.0])
    y_pred = np.array([0.8, 0.25])
    expected = -0.5 * (math.log(0.8) + math.log(0.75))

    assert binary_log_loss(y_true, y_pred) == expected
