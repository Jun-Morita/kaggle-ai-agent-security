# ruff: noqa: E402, I001

from __future__ import annotations
import glob
import sys
from pathlib import Path

sys.argv = [sys.argv[0]]

for candidate in glob.glob("/kaggle/input/**/kaggle_evaluation", recursive=True):
    dataset_root = str(Path(candidate).parent)
    if dataset_root not in sys.path:
        sys.path.insert(0, dataset_root)
    print(f"Dataset root: {dataset_root}")
    break

source_attack = Path(__file__).with_name("attack.py")
working_dir = Path("/kaggle/working")
if not working_dir.exists():
    working_dir = Path.cwd()
target_attack = working_dir / "attack.py"
target_attack.write_text(source_attack.read_text(encoding="utf-8"), encoding="utf-8")
print(f"attack.py written: {target_attack}")

import kaggle_evaluation.jed_attack_134815.jed_attack_inference_server as server

server.JEDAttackInferenceServer().serve()
