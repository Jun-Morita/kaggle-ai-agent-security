# exp191_generation_order_cpu

## Hypothesis

The updated evaluator preserves score accumulated before replay timeout, and
discussion 736246 reports that only the returned prefix may be replayed. Keep
all `v169` attack generation behavior, but return validated candidates in their
generation order rather than sorting them by observed latency.

