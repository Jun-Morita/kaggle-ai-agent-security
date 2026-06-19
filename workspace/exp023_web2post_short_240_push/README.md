# exp023 Web2post short 240 push

Goal: push the current public high-score notebook's actual `V26` attack shape beyond 208 candidates by scaling to 240 candidates while preserving the same three-message chain.

Sources:

```text
Kaggle kernel metadata/output:
boristown/agi-ai-agent-security

Pulled files:
/tmp/agi_kernel_pull/
/tmp/agi_kernel_output/
```

Key finding:

- pulled public kernel metadata reports `NOTEBOOK_VERSION = "V26"`;
- generated public `attack.py` uses `source_two_post`, not static 625 direct POST;
- each candidate has `web.search` followed by two short POST messages;
- public output validation summary has 416/416 successful `http.post` proxy messages and 0/208 successful source messages;
- public score `56.25` is therefore from replay-dense multi-message candidate chains, not from the stale static625 plan.
- this version scales `208 -> 240` candidates, raising total user messages `624 -> 720` and theoretical normalized score `68.64 -> 79.2`.

Active submission copy:

```text
submit/v023_web2post_short_240_push/
```

Expected public score if it transfers at similar efficiency: above `60`.
