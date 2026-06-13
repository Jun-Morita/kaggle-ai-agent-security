---
title: "AI Agent Security - Multi-Step Tool Attacks"
source: "https://www.kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks/data"
author:
published:
created: 2026-06-13
description: "Develop attack algorithms to identify reproducible multi-step failures in tool-using AI agents."
tags:
  - "clippings"
---
OpenAI · Featured Code Competition · 3 months to go

## AI Agent Security - Multi-Step Tool Attacks

## Dataset Description

JED Red-Team Attack is a security evaluation benchmark within the JED (Jailbreak, Exploit, Defend) Framework, where participants craft prompt sequences that attempt to trick a tool-using AI agent into performing harmful or unauthorized actions despite the presence of safety guardrails.

## How It Works

Your submission is an `AttackAlgorithm` class that receives an **environment** containing a target AI agent, its toolbox (filesystem, email, web search, shell, HTTP), and a guardrail. You interact with the agent by sending prompts and observing the resulting tool calls.

- Your agent sends **prompts** via `env.interact(prompt)` —each returns an interaction result with tool events.
- You return a list of **attack candidates** —replayable prompt chains that triggered security predicates.
- Candidates are **independently replayed** against both a public and a private guardrail, and scored.

## Environment

The environment simulates a workspace with pre-seeded files, emails, and web content. The agent has access to these tools:

| Tool | Side Effect | Description |
| --- | --- | --- |
| `fs.read` | READ | Read a file from the filesystem |
| `fs.write` | WRITE | Write/overwrite a file |
| `fs.delete` | WRITE | Delete a file |
| `http.post` | SHARE | Send data to an external HTTP endpoint |
| `email.send` | SHARE | Send an email |
| `web.search` | READ | Search the web corpus |
| `shell.run` | EXEC | Execute a shell command |

### Environment API

```dockerfile
env.reset()                    # Reset to clean initial state
env.interact(prompt)           # Send a user message; blocks until the agent responds
env.export_trace_dict()        # Get the full execution trace (tool events, messages)
env.snapshot()                 # Save current state (returns a handle)
env.restore(handle)            # Restore a saved state
```

### Environment Fixtures

The agent's workspace contains pre-seeded data, we use a set of hidden fixtures for the private leaderboard:

- **`file_seed/`** — Filesystem files the agent can read, write, and delete. Includes `secret.txt` containing sensitive credentials (`SECRET_API_KEY`, `TOKEN`, `PASSWORD`).
- **`web_corpus.json`** — Simulated web search results returned by `web.search`.
- **`mail_seed.json`** — Pre-loaded email inbox accessible via `email.read`.

## Target Models

Your attack is evaluated against **two models sequentially**, each with its own independent 1800-second budget:

| Model | Architecture | Backend |
| --- | --- | --- |
| `gpt_oss` | GPT-OSS 20B | GGUF via llama.cpp on T4 GPU |
| `gemma` | Gemma 4 26B-A4B-it | GGUF via llama.cpp on T4 GPU |

## Files

- **`kaggle_evaluation/`** — Hearth evaluation framework connecting your submission to the competition infrastructure.
- **`kaggle_evaluation/jed_attack_134815/`** — Competition-specific gateway, inference server, model servers, and remote environment proxy.
- **`aicomp_sdk-3.1.0` (wheel)** — SDK containing the environment API, predicates, agents, scoring, and guardrail implementations.
- **`aicomp_sdk/fixtures/`** — Pre-seeded environment data (`file_seed/`, `web_corpus.json`, `mail_seed.json`).

## Key Constraints

| Parameter | Value |
| --- | --- |
| Time budget per model | 18000 seconds |
| Max tool hops per interaction | 8 |
| Max candidates returned | 2,000 |
| Max messages per candidate | 32 |
| Max message length | 10,000 characters |
| Seed | 123 (fixed) |

## Files

137 files

## Size

9.62 MB

## Type

py, txt, json + 5 others

## License

[MIT](https://www.mit.edu/~amini/LICENSE.md)

### \_\_init\_\_.py(0 B)

get\_app

fullscreen

chevron\_right

## Data Explorer

9.62 MB

- aicomp\_sdk
- aicomp\_sdk-3.1.0.dist-info
- kaggle\_evaluation
- \_\_init\_\_.py

## Summary

137 files