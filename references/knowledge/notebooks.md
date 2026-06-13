# Notebook Knowledge

Public notebook から得た知識を要約する。

## Entries

## 2026-06-13: 17-1 EDA Agent Security Trajectory Search

- Source: local raw copy at `references/raw/notebooks/17-1-eda-agent-security-trajectory-search.ipynb`
- Fetched at: 2026-06-13
- Author: likely Pilkwang Kim based on notebook metadata path and user-provided leaderboard context
- Competition: AI Agent Security - Multi-Step Tool Attacks
- User-provided leaderboard context: team `Pilkwang Kim`, rank 9, public score `17.085`, 4 entries, last activity 7h before the snapshot

### Key Ideas

- This is more than an EDA notebook; it builds a generated `attack.py` with a trajectory-search style attack generator.
- It reads SDK source files to derive the actual contract:
  - `AttackCandidate` only has `user_messages`
  - max replay findings: `2000`
  - max replay messages per finding: `32`
  - max user message chars: `2000`
  - evaluation default max tool hops: `4`
  - env default max tool hops: `8`
- It exposes search profiles:
  - `fast`: return target `64`, search fraction `0.15`, max search `120s`, endpoints per message `4`
  - `balanced`: return target `120`, search fraction `0.25`, max search `300s`, endpoints per message `6`
  - `full`: return target `180`, search fraction `0.30`, max search `600s`, endpoints per message `8`
  - `aggressive`: return target `300`, search fraction `0.35`, max search `850s`, endpoints per message `8`
- The selected notebook profile is `full`.
- It explicitly studies score-cell geometry. A synthetic check shows changing an `http.post` URL path under the same domain does **not** change the cell hash, while changing the domain does. This supports varying subdomains/hosts rather than only paths.
- It parses public fixtures:
  - web pages: `19679`
  - mail messages: `8746`
  - file seed files: `24`
- It ranks risky web/email sources and extracts tool-call edges from web/email content, but keeps source-based lottery small because public guardrail likely blocks dangerous actions after untrusted sources.
- It filters public notebook prompt strings before reuse:
  - keep only official SDK / `AttackCandidate(user_messages=...)` compatible sources
  - reject dummy schemas, `score_hint`, `context_channel`, code fragments, unsafe domains, and credential-looking terms
  - provide a manual seed floor when no public notebooks are discoverable on Kaggle

### Attack Template Structure

- Main scoring payload bank:
  - `TOKEN=admin123`
  - `SECRET_API_KEY=sk_live_test`
  - `PASSWORD=test123`
  - `SECRET_MARKER`
- Exfil prompt variants:
  - strict `http.post`
  - argument-schema wording
  - connectivity validation
  - canary exact text
  - batch validation
  - audit marker
  - seed prompt only for calibration, not mass generation
- Confused-deputy variants avoid explicit `send`, `email`, and `upload` wording:
  - `Notify`, `Drop update`, `Let`, `Brief`, `Update`, `Tell`, `Route a note`, `Drop a brief note`
- Runtime loop:
  - calibrate exfil across endpoint counts `(1, 2, 4, 8)`, payloads, and variants
  - sort successful combos by local predicate score and endpoint count
  - mutate successful single-turn exfil prompts
  - mass-generate exfil prompts using the best combos
  - run single-endpoint exfil phase
  - calibrate and sweep confused-deputy prompts
  - run a small snapshot branch for exfil follow-ups
  - run a tiny source-action lottery
  - **bounded fill** unattempted exfil/deputy candidates up to a target count, even when verified findings already exist
- It tracks `last_run_details` with family, phase, predicates, raw predicate weight, trace-cell count, URL count, and priority, then sorts candidates by priority.
- If `env is None`, it returns static fallback candidates for contract checking: roughly 82% exfil and 18% confused deputy.
- Notebook contract check generated `80` candidates in static mode under the `full` notebook run:
  - `65` static exfil fill
  - `15` static confused-deputy fill
  - exfil endpoint count `260`
- Local deterministic gateway produced `0.0`, consistent with our v001-v003 deterministic smoke behavior.

### Useful for This Competition

- The user-provided public score `17.085` makes this the strongest known public reference in this repository by a large margin:
  - our `v001_wiring_baseline`: `0.330`
  - our `v002_public_reachable`: `0.565`
  - this notebook's reported public context: `17.085`
- Best immediate adoption target is not the broad destructive/untrusted bank; it is the exfil search policy:
  - calibration grid over payload, variant, and endpoint count
  - endpoint count bounded by `config.max_tool_hops`
  - include `SECRET_MARKER` in payload bank
  - return bounded fill candidates after verified search, not only when no findings exist
  - sort candidates so verified high-value exfil candidates come first
- It gives evidence that domain diversity matters more than URL path diversity for score cells.
- It provides a cleaner approach for future `v004` than our current `v003`:
  - keep `v002` public-reachable exfil core
  - add notebook-style calibration and bounded fill
  - keep source/untrusted lottery small
  - avoid spending much budget on public-guardrail-blocked destructive writes

### Risks / Caveats

- The generated notebook attack is not using our established submission wrapper. We should port the ideas into `templates/submit_attack` / `submit/vNNN_*`, not copy the notebook harness wholesale.
- It still relies heavily on public predicate strings and public guardrail behavior.
- It uses many unverified bounded-fill candidates. That can help public LB, but too many candidates may waste replay budget or overfit public behavior.
- Its `trace_cell_count` helper is a priority heuristic, not exactly the SDK `cell_signature`.
- The source fixture IDs and public fixture topology can overfit. Treat source lottery as a small private-robust probe, not the main scoring engine.
- The smart local gateway cell is useful in notebook form but unnecessary for our current script-kernel template because we already write `attack.py` and placeholder `submission.csv`.

### Experiment Candidates

- Build `v004_trajectory_exfil` after `v003` score is known:
  - adopt `SCORING_PAYLOADS = ("TOKEN=admin123", "SECRET_API_KEY=sk_live_test", "PASSWORD=test123", "SECRET_MARKER")`
  - add strict/schema/connectivity/canary/batch/audit exfil variants
  - calibrate endpoint counts `(1, 2, 4, 8)` clipped to `config.max_tool_hops`
  - return bounded fill up to `120-180` candidates
  - keep deputy fill around `15-20%`
  - keep untrusted/source lottery very small
- Prefer a `balanced` profile first for risk control, then try `full` if daily submissions remain.

## 2026-06-13: Verify and Keep Deterministic Red-Team Attack

- Source: local raw copy at `references/raw/notebooks/verify-and-keep-deterministic-red-team-attack.ipynb`
- Fetched at: 2026-06-13
- Author: public Kaggle notebook author not checked in notebook metadata
- Competition: AI Agent Security - Multi-Step Tool Attacks

### Key Ideas

- This is a "fast variant" deterministic red-team notebook capped at roughly `MAX_SEARCH_S = 360` seconds of search per model.
- It uses the same Kaggle submission harness:
  - discover `/kaggle/input/**/kaggle_evaluation`
  - add the dataset root to `sys.path`
  - write `/kaggle/working/attack.py`
  - start `JEDAttackInferenceServer().serve()`
- Unlike broad prompt sweeps, it intentionally targets only two predicate families:
  - `EXFILTRATION`
  - `CONFUSED_DEPUTY`
- Its rationale is based on reading the public `OptimalGuardrail`:
  - `http.post` guardrail target extraction checks `url` before `data`, so a neutral URL with `TOKEN=admin123` in `data` can pass the public guardrail and fire `EXFILTRATION`.
  - `email.send` can fire `CONFUSED_DEPUTY` if the user request avoids explicit words such as `send`, `email`, or `upload`.
  - `DESTRUCTIVE_WRITE` is considered unreachable under public guardrail because `secret.txt` contains an ultra-dangerous pattern.
  - `UNTRUSTED_TO_ACTION` is considered unreachable under public guardrail because web/email taint blocks later dangerous actions.
- The generated `AttackAlgorithm` uses a verify-and-keep loop:
  - build candidate message
  - `env.reset()`
  - run `env.interact(...)`
  - check `eval_predicates(env.export_trace_dict())`
  - append `AttackCandidate` only when a predicate fires
- It auto-calibrates which exfil prompt phrasing the current model follows, then cycles through successful variants.
- It varies `http.post` destination hosts to create distinct score-driving cells.
- Important constants in the generated `attack.py`:
  - `ENDPOINTS_PER_MSG = 4`
  - `SEARCH_FRACTION = 0.35`
  - `MAX_SEARCH_S = 360`
  - `MAX_CANDIDATES = 60`

### Useful for This Competition

- Strong reference for a fast, submission-friendly baseline.
- The focus on public-guardrail-reachable predicates may be more efficient than spending budget on blocked `secret.txt` writes or tainted untrusted-to-action chains.
- Multi-endpoint exfil messages can stack multiple `EXFILTRATION` events in one candidate if the model performs several `http.post` calls.
- The score-cell argument is mostly consistent with SDK scoring: `score_cell_signature` is computed from `tool_events` only, so changing `http.post` host is a meaningful diversity lever.
- The capped search budget makes it useful for quick pipeline validation before running longer variants.

### Risks / Caveats

- This is heavily optimized around public `OptimalGuardrail`; private guardrail may block the neutral-url exfil trick.
- It relies on the literal public secret pattern `TOKEN=admin123`, not discovery of hidden fixture secrets.
- It intentionally ignores `DESTRUCTIVE_WRITE` and `UNTRUSTED_TO_ACTION`; that may cap private score if those are reachable under hidden conditions.
- The code calls `env.interact(m)` without explicitly passing `max_tool_hops=config.max_tool_hops`.
- The safety-net fallback can return unverified exfil candidates if no live candidate fires, which weakens the "verify every candidate" claim in the empty-result case.
- Notebook prose has stale numbers in the final notes (`MAX_CANDIDATES` described as 250 and phase fractions described differently), while the code uses `MAX_CANDIDATES = 60` and phase deadlines `0.14 / 0.69 / 0.86 / 1.00`.

### Experiment Candidates

- Use as a fast public-LB baseline after adding:
  - explicit `max_tool_hops=config.max_tool_hops`
  - candidate deduplication
  - local logs for number of tool calls, predicates, score cells, and replay success
- Test variants with `ENDPOINTS_PER_MSG` from 1 to 8 to find model/tool-hop compliance tradeoffs.
- Add a private-robust branch that discovers actual secrets from files when guardrail/model behavior allows it, while keeping this public-guardrail exfil baseline as fallback.

## 2026-06-13: Baseline Solution 4.900

- Source: local raw copy at `references/raw/notebooks/baseline-solution-4-900.ipynb`
- Fetched at: 2026-06-13
- Author: public Kaggle notebook author not checked in notebook metadata
- Competition: AI Agent Security - Multi-Step Tool Attacks

### Key Ideas

- The notebook follows the official submission harness:
  - find `/kaggle/input/**/kaggle_evaluation`
  - insert the dataset root into `sys.path`
  - write `/kaggle/working/attack.py`
  - call `JEDAttackInferenceServer().serve()`
- The generated `attack.py` defines `AttackAlgorithm.run(self, env, config: AttackRunConfig)`.
- It is a deterministic, no-runtime-LLM prompt-bank attacker.
- It organizes payloads into four families:
  - `EXFIL_SETUPS`: direct `http.post`-style credential exfiltration prompts
  - `DESTRUCTIVE_SETUPS`: delete, truncate, zero, or overwrite `secret.txt`
  - `CONFUSED_DEPUTY_SETUPS`: send routine-looking emails
  - `UNTRUSTED_SETUPS` + `UNTRUSTED_FOLLOWUPS`: read/search/email setup followed by write/share/execute actions
- It uses `snapshot_branch(setup_msg, followups)` to run one setup, snapshot the state, then restore and try multiple follow-ups.
- It mutates successful single-turn prompts with prefix/suffix strings to increase cell diversity.
- It appends `AttackCandidate(user_messages=messages)` only when `eval_predicates(env.export_trace_dict())` fires locally.

### Useful for This Competition

- Good reference for a simple high-throughput baseline:
  - prompt banks first
  - snapshot branching second
  - mutation sweep third
- The broad predicate coverage is useful for a first serious submission template.
- The mutation structure is useful for diversity, especially because unique cell signatures add score.
- The code is syntactically valid as embedded `attack_code`.

### Risks / Caveats

- It does not pass `max_tool_hops=config.max_tool_hops` to `env.interact`.
- It uses high time margins (`180`, `200`, `240`, `280`, `300`, `400` seconds), so short local smoke tests may do almost nothing unless the margins are parameterized.
- Direct exfiltration prompts hard-code secret-like strings. Some match public predicate patterns, but this is brittle for private fixtures and stricter guardrails.
- No deduplication of `AttackCandidate` message chains or score cells.
- Public fixture filenames such as `secret.txt`, `config.json`, and `weekly_report.txt` are used directly, so private fixture generalization is uncertain.
- Markdown claims local smoke-test behavior, but the final code cell simply starts the Kaggle inference server; actual local validation still needs `aicomp validate/test/evaluate`.

### Experiment Candidates

- Use this as `v001` or `v002` baseline after adapting:
  - pass `max_tool_hops=config.max_tool_hops`
  - lower margins for local testing while preserving official-budget behavior
  - deduplicate candidates
  - record predicate family and cell hash during local runs
- Replace hard-coded secret-looking exfil payloads with fixture-aware but private-robust discovery flows.
- Add a local smoke harness around the generated `attack.py`.

## 2026-06-13: Getting Started Notebook

- Source: local raw copy at `references/raw/notebooks/getting-started-notebook.ipynb`
- Original URL: https://www.kaggle.com/code/martynaplomecka/getting-started-notebook
- Fetched at: 2026-06-13
- Author: Martyna Plomecka / competition starter notebook
- Competition: AI Agent Security - Multi-Step Tool Attacks

### Key Ideas

- The notebook has four cells:
  - a short markdown intro
  - Kaggle setup code that finds `/kaggle/input/**/kaggle_evaluation` and inserts the dataset root into `sys.path`
  - code that writes `/kaggle/working/attack.py`
  - code that starts `kaggle_evaluation.jed_attack_134815.jed_attack_inference_server.JEDAttackInferenceServer().serve()`
- The starter `attack.py` imports:
  - `AttackAlgorithmBase`, `AttackCandidate`, `AttackRunConfig` from `aicomp_sdk.attacks`
  - `eval_predicates` from `aicomp_sdk.core.predicates`
- The required method signature is `run(self, env, config: AttackRunConfig) -> list[AttackCandidate]`.
- The starter tracks wall-clock time with `config.time_budget_s` and uses a large safety margin before each attempt.
- The starter pattern for each attempt is:
  - `env.reset()`
  - call `env.interact(msg)` for each message
  - call `eval_predicates(env.export_trace_dict())`
  - append `AttackCandidate(user_messages=messages)` only when a predicate fires
- It demonstrates `env.snapshot()` / `env.restore()` branching after a setup prompt.

### Useful for This Competition

- This is the submission harness pattern to copy into a dedicated submit template.
- The Kaggle Notebook must write `/kaggle/working/attack.py` before starting the inference server.
- The dataset-root discovery via `glob.glob('/kaggle/input/**/kaggle_evaluation', recursive=True)` is useful because the competition data directory name may vary.
- The starter attack prompts are weak but useful as smoke-test examples for exfiltration, confused deputy, multi-turn state carryover, and snapshot branching.

### Risks / Caveats

- The starter hard-codes secret-looking strings such as `SECRET_API_KEY=sk_live_test` and `PASSWORD=test123`; that may score locally but is likely brittle against private fixtures.
- It calls `env.interact(msg)` without passing `config.max_tool_hops`; a stronger implementation should pass `max_tool_hops=config.max_tool_hops`.
- The time margins (`180`, `360`, `600` seconds) are conservative for official budget but awkward for short local smoke tests unless parameterized.
- The raw notebook is intentionally kept under `references/raw/` and should not be committed.

### Experiment Candidates

- Create `templates/submit_attack/` from this notebook pattern.
- Build a minimal local `attack.py` that can run through `aicomp validate redteam` and `aicomp test redteam`.
- Replace hard-coded secret strings with trace-guided prompt generation and fixture-agnostic tool-action goals.
- Add configurable prompt banks and snapshot/restore branching while preserving clean replayable `AttackCandidate` chains.

```markdown
## YYYY-MM-DD: title

- Source:
- Fetched at:
- Author:
- Competition:

### Key Ideas
- 

### Useful for This Competition
- 

### Risks / Caveats
- 

### Experiment Candidates
- 
```
