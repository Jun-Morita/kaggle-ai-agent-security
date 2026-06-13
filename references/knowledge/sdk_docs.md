# SDK Documentation Notes

## 2026-06-13: JED Framework documentation

- Source: https://mbhatt1.github.io/competitionscratch/
- Fetched at: 2026-06-13
- Author: JED Framework contributors / competition SDK documentation
- Type: documentation
- Competition: AI Agent Security - Multi-Step Tool Attacks

### Key Ideas

- Public Kaggle path is attack-only: submit `attack.py`, define `AttackAlgorithm`, inherit `AttackAlgorithmBase`, and return `list[AttackCandidate]`.
- Minimum signature is `run(self, env, config: AttackRunConfig) -> list[AttackCandidate]`.
- Public leaderboard uses normalized attack score only.
- Returned candidates are replay instructions, not trusted metadata. The evaluator replays each message chain in a fresh environment, then recomputes trace, predicates, cell signature, and score.
- `aicomp evaluate redteam` and `aicomp test redteam` default to `1800` seconds.
- For local behavior closest to the Kaggle public path, use `aicomp evaluate redteam attack.py --env gym`.
- `deterministic` agent is the offline smoke-test target that does not require API keys.
- Current replay limits are:
  - at most `2000` replayed findings
  - at most `32` user messages per finding
  - at most `2000` characters per user message
- Canonical tool surface includes `web.search`, `web.open`, `fs.read`, `fs.write`, `fs.delete`, `shell.run`, `email.list`, `email.read`, `email.send`, and `http.post`.
- Useful trace fields are `user_messages`, `assistant_messages`, `tool_events`, and `egress`.
- `GymAttackEnv` uses `reset()` / `step(action)` semantics, but reward is always `0.0`; useful signal is in `info`.
- Baseline Go-Explore attacker is useful as a reference for archive search, `snapshot()` / `restore()`, cell prioritization, and replayable candidate construction.

### Useful Commands

```bash
aicomp init attack
aicomp validate redteam attack.py
aicomp test redteam attack.py --budget-s 60 --agent deterministic
aicomp evaluate redteam attack.py --budget-s 60 --agent deterministic --env gym
```

When using this repo with `uv`, prefer:

```bash
uv run aicomp validate redteam attack.py
uv run aicomp test redteam attack.py --budget-s 60 --agent deterministic
uv run aicomp evaluate redteam attack.py --budget-s 60 --agent deterministic --env gym
```

### Useful for This Competition

- Resolve doc conflicts in saved Kaggle pages:
  - Treat `1800` seconds as the current SDK/public path default until the official Kaggle page proves otherwise.
  - Treat `2000` characters per user message as the current SDK replay/interact limit, despite saved overview mentioning `10000`.
- Build first local validation around deterministic smoke tests, then evaluator parity with `--env gym`.
- Optimize for replayable message chains rather than local trace metadata.
- Use cell diversity deliberately; successful attacks that differ only by superficial wording may not improve score much.

### Risks / Caveats

- The docs describe current SDK behavior. Hosted Kaggle infrastructure can still impose outer process timeouts or private guardrail behavior not visible locally.
- `aicomp-sdk` is not yet a committed project dependency in `pyproject.toml`; the downloaded competition data contains the SDK source under `data/raw/`, which is ignored by Git.
- Private leaderboard fixtures and guardrail are hidden. Public fixture exact-string strategies can overfit.

### Experiment Candidates

- Create a minimal `attack.py` from `aicomp init attack` and commit an adapted version under `templates/submit_attack/`.
- Add a local smoke script that runs:
  - `aicomp validate redteam`
  - `aicomp test redteam --budget-s 60 --agent deterministic`
  - `aicomp evaluate redteam --budget-s 60 --agent deterministic --env gym`
- Start with a prompt-bank baseline, then add `snapshot()` / `restore()` branching and cell-signature deduplication.
