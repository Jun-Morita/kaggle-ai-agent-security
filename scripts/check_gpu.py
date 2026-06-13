from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys


def run_command(command: list[str]) -> tuple[int, str]:
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    output = (result.stdout or result.stderr).strip()
    return result.returncode, output


def print_section(title: str) -> None:
    print(f"\n[{title}]")


def check_nvidia_smi() -> bool:
    print_section("nvidia-smi")
    if shutil.which("nvidia-smi") is None:
        print("not found")
        print("NVIDIA GPU may be unavailable, or the driver is not visible in this environment.")
        return False

    command = [
        "nvidia-smi",
        "--query-gpu=name,memory.total,driver_version",
        "--format=csv,noheader",
    ]
    returncode, output = run_command(command)
    if returncode != 0:
        print(output)
        return False

    print(output)
    return True


def check_torch() -> bool:
    print_section("torch")
    if importlib.util.find_spec("torch") is None:
        print("not installed")
        return False

    import torch

    print(f"version: {torch.__version__}")
    print(f"cuda available: {torch.cuda.is_available()}")

    if not torch.cuda.is_available():
        return False

    print(f"cuda version: {torch.version.cuda}")
    print(f"device count: {torch.cuda.device_count()}")
    for index in range(torch.cuda.device_count()):
        print(f"device {index}: {torch.cuda.get_device_name(index)}")

    return True


def main() -> None:
    print_section("python")
    print(sys.version.replace("\n", " "))
    print(f"executable: {sys.executable}")

    nvidia_visible = check_nvidia_smi()
    torch_gpu = check_torch()

    print_section("summary")
    if torch_gpu:
        print("GPU is available from PyTorch. Prefer GPU-enabled training when it fits the task.")
    elif nvidia_visible:
        print("NVIDIA GPU is visible, but PyTorch GPU is not ready.")
        print("Install the GPU-enabled ML library needed for this competition.")
        print("Then rerun this check.")
    else:
        print("No NVIDIA GPU was detected from this environment.")
        print("Use CPU locally, or run GPU experiments on Kaggle / cloud / another machine.")


if __name__ == "__main__":
    main()
