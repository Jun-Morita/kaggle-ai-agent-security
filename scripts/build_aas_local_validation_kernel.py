#!/usr/bin/env python3
"""Build a Kaggle notebook kernel for AAS public local validation.

The source notebook is the public AAS local validation notebook. This script
embeds a chosen attack.py into that notebook and writes a pushable Kaggle
kernel directory with the model sources and competition source configured.
"""

from __future__ import annotations

import argparse
import base64
import json
import textwrap
from pathlib import Path
from typing import Any

DEFAULT_NOTEBOOK = Path(
    "references/raw/notebooks/aas-local-validation/aas-local-validation.ipynb"
)
DEFAULT_METADATA = Path(
    "references/raw/notebooks/aas-local-validation/kernel-metadata.json"
)
NOTEBOOK_NAME = "aas-local-validation.ipynb"


def _source_text(source: Any) -> str:
    if isinstance(source, list):
        return "".join(source)
    if isinstance(source, str):
        return source
    raise TypeError(f"Unsupported notebook source type: {type(source)!r}")


def _source_lines(text: str) -> list[str]:
    return text.splitlines(keepends=True)


def _embedded_attack_cell(attack_path: Path, attack_bytes: bytes) -> list[str]:
    encoded = base64.b64encode(attack_bytes).decode("ascii")
    wrapped = textwrap.wrap(encoded, width=88)
    lines = [
        "import base64\n",
        "\n",
        f"ATTACK_SOURCE = {attack_path.as_posix()!r}\n",
        "ATTACK_CODE_B64 = (\n",
    ]
    lines.extend(f"    {chunk!r}\n" for chunk in wrapped)
    lines.extend(
        [
            ")\n",
            "ATTACK_PATH.write_text(\n",
            "    base64.b64decode(ATTACK_CODE_B64).decode('utf-8')\n",
            ")\n",
            "print(\n",
            "    f'Embedded {ATTACK_SOURCE} -> {ATTACK_PATH} '\n",
            "    f'({ATTACK_PATH.stat().st_size} bytes)'\n",
            ")\n",
        ]
    )
    return lines


def _replace_attack_cell(notebook: dict[str, Any], attack_path: Path, attack_bytes: bytes) -> None:
    replacement = _embedded_attack_cell(attack_path, attack_bytes)

    for cell in notebook.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        text = _source_text(cell.get("source", ""))
        if "getting-started-notebook/attack.py" in text and "ATTACK_PATH" in text:
            cell["source"] = replacement
            cell["outputs"] = []
            cell["execution_count"] = None
            return

    raise ValueError("Could not find the starter attack copy cell to replace")


def _annotate_notebook(notebook: dict[str, Any], attack_path: Path) -> None:
    note = (
        "# Generated AAS public validation notebook\n\n"
        f"- Embedded attack source: `{attack_path.as_posix()}`\n"
        "- Purpose: evaluate the attack against public gpt_oss and gemma GGUF models.\n"
        "- Caveat: this validates public guardrail behavior only; private guardrail can differ.\n"
    )
    notebook.setdefault("cells", []).insert(
        0,
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": _source_lines(note),
        },
    )


def _build_metadata(
    source_metadata: dict[str, Any],
    kernel_id: str,
    title: str,
    notebook_name: str,
) -> dict[str, Any]:
    return {
        "id": kernel_id,
        "title": title,
        "code_file": notebook_name,
        "language": "python",
        "kernel_type": "notebook",
        "is_private": True,
        "enable_gpu": True,
        "enable_tpu": False,
        "enable_internet": True,
        "dataset_sources": [],
        "competition_sources": source_metadata.get(
            "competition_sources", ["ai-agent-security-multi-step-tool-attacks"]
        ),
        "model_sources": source_metadata.get("model_sources", []),
        "kernel_sources": [],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Embed attack.py into the AAS local validation notebook."
    )
    parser.add_argument("--attack", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--kernel-id", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--source-notebook", default=DEFAULT_NOTEBOOK, type=Path)
    parser.add_argument("--source-metadata", default=DEFAULT_METADATA, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    attack_path = args.attack
    if not attack_path.exists():
        raise FileNotFoundError(attack_path)
    if not args.source_notebook.exists():
        raise FileNotFoundError(args.source_notebook)
    if not args.source_metadata.exists():
        raise FileNotFoundError(args.source_metadata)

    notebook = json.loads(args.source_notebook.read_text(encoding="utf-8"))
    source_metadata = json.loads(args.source_metadata.read_text(encoding="utf-8"))
    attack_bytes = attack_path.read_bytes()

    _replace_attack_cell(notebook, attack_path, attack_bytes)
    _annotate_notebook(notebook, attack_path)

    metadata = _build_metadata(
        source_metadata=source_metadata,
        kernel_id=args.kernel_id,
        title=args.title,
        notebook_name=NOTEBOOK_NAME,
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    notebook_path = args.output_dir / NOTEBOOK_NAME
    metadata_path = args.output_dir / "kernel-metadata.json"
    manifest_path = args.output_dir / "validation-target.json"

    notebook_path.write_text(
        json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )
    metadata_path.write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    manifest_path.write_text(
        json.dumps(
            {
                "attack": attack_path.as_posix(),
                "kernel_id": args.kernel_id,
                "title": args.title,
                "source_notebook": args.source_notebook.as_posix(),
                "source_metadata": args.source_metadata.as_posix(),
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"Wrote {notebook_path}")
    print(f"Wrote {metadata_path}")
    print(f"Wrote {manifest_path}")


if __name__ == "__main__":
    main()
