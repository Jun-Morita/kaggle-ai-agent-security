from __future__ import annotations

import argparse
import importlib.util
import json
import statistics
from collections import Counter
from pathlib import Path
from typing import Any

from aicomp_sdk.agents import build_agent
from aicomp_sdk.core.env.sandbox import SandboxEnv
from aicomp_sdk.guardrails.optimal import Guardrail


def load_attack(path: Path) -> Any:
    spec = importlib.util.spec_from_file_location("attack_under_probe", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load attack module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def ok_http_post_count(trace: dict[str, Any]) -> int:
    return sum(
        1
        for event in trace.get("tool_events", []) or []
        if event.get("ok") is True and event.get("name") == "http.post"
    )


def summarize_counts(counts: list[int]) -> dict[str, Any]:
    if not counts:
        return {
            "n": 0,
            "min": 0,
            "max": 0,
            "mean": 0.0,
            "median": 0.0,
            "with_any_post": 0,
            "distribution": {},
        }
    return {
        "n": len(counts),
        "min": min(counts),
        "max": max(counts),
        "mean": statistics.fmean(counts),
        "median": statistics.median(counts),
        "with_any_post": sum(1 for count in counts if count > 0),
        "distribution": dict(sorted(Counter(counts).items())),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Replay static AttackCandidates and count successful http.post tool calls."
    )
    parser.add_argument("attack", type=Path)
    parser.add_argument("--limit", type=int, default=32)
    parser.add_argument("--max-tool-hops", type=int, default=4)
    parser.add_argument(
        "--fixtures-dir",
        type=Path,
        default=Path("data/raw/ai-agent-security-multi-step-tool-attacks/aicomp_sdk/fixtures"),
    )
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    module = load_attack(args.attack)
    candidates = module.AttackAlgorithm().run(None, None)
    selected = candidates[: max(0, args.limit)]

    env = SandboxEnv(
        seed=123,
        fixtures_dir=args.fixtures_dir,
        agent=build_agent("deterministic"),
        guardrail=Guardrail(),
        max_tool_hops=args.max_tool_hops,
    )

    rows: list[dict[str, Any]] = []
    for idx, candidate in enumerate(selected):
        env.reset()
        for message in candidate.user_messages:
            env.interact(message, max_tool_hops=args.max_tool_hops)
        trace = env.export_trace_dict()
        tool_events = trace.get("tool_events", []) or []
        rows.append(
            {
                "index": idx,
                "messages": len(candidate.user_messages),
                "http_post_ok_count": ok_http_post_count(trace),
                "tool_event_count": len(tool_events),
                "tool_names": [event.get("name") for event in tool_events],
                "first_message": candidate.user_messages[0][:240],
            }
        )

    counts = [int(row["http_post_ok_count"]) for row in rows]
    report = {
        "attack": str(args.attack),
        "candidate_source": "AttackAlgorithm().run(None, None)",
        "candidate_count_available": len(candidates),
        "candidate_count_replayed": len(selected),
        "max_tool_hops": args.max_tool_hops,
        "summary": summarize_counts(counts),
        "rows": rows,
    }

    text = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
