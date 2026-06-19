# exp022 Web2post short 208 timeflat

Goal: reproduce the current public high-score notebook's actual `V26` attack shape after discovering that the local raw `agi-ai-agent-security.ipynb` copy was stale.

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
- generated `attack.py` uses `source_two_post`, not static 625 direct POST;
- each candidate has `web.search` followed by two short POST messages;
- public output validation summary has 416/416 successful `http.post` proxy messages and 0/208 successful source messages;
- public score `56.25` is therefore from replay-dense multi-message candidate chains, not from the stale static625 plan.

Active submission copy:

```text
submit/v022_web2post_short_208_timeflat/
```

Expected public score if it transfers: near or above `56.25`.
