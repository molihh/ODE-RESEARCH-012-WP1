# Production run_integrated Method-Pack Acceptance

Status: **PASS**

Integration entry: `ode_integration.production.integrated.run_integrated`

Added additive branch:

```python
if production_config.get("method_pack"):
    from .wp1_method_pack import run_method_pack
    return run_method_pack(production_config, output)
```

The branch reuses WP1 unified method chain; it does not change the existing D01/D06 path or public contract.

Executed:

```text
run_integrated(
  config_path=<existing config>,
  output=/Users/chj/Desktop/ode/WP1_RUN_INTEGRATED,
  production_config={"method_pack": {...}}
)
```

Result:

```text
selected: U04, U05, U06, A04, G06
validated: 5/5
status: PASS
provider_calls: 0
network_calls: 0
```

Per-method actual EV/replay/report all PASS. Evidence:

```text
evidence/production-run-integrated/result.json
evidence/production-run-integrated/trace.jsonl
evidence/production-run-integrated/run-receipt.json
evidence/production-run-integrated/<MID>/
```

The adapter files are preserved as:

```text
evidence/integrated.py.patchcopy
evidence/wp1_method_pack.py
```
