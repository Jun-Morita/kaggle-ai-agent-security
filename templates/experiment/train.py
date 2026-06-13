from __future__ import annotations

import argparse
from pathlib import Path

import yaml

from kaggle_agent_template.repro import set_seed, write_run_metadata


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.yaml")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config_path = Path(args.config)

    with config_path.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    output_dir = Path(config.get("output", {}).get("dir", "results"))
    output_dir.mkdir(parents=True, exist_ok=True)

    seed = int(config.get("experiment", {}).get("seed", 42))
    set_seed(seed)
    metadata_path = write_run_metadata(output_dir=output_dir, config_path=config_path)

    print(f"Loaded config: {config_path}")
    print(f"Output dir: {output_dir}")
    print(f"Seed: {seed}")
    print(f"Run metadata: {metadata_path}")
    print("Edit train.py for this competition before running real experiments.")


if __name__ == "__main__":
    main()
