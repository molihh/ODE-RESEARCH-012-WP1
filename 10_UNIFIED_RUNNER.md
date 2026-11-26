# WP1 Unified Method-Chain Runner

Implemented: `src/wp1_methods/runner.py`

```text
Auto Selector
  -> per-method OracleEnvelope
  -> EvaluationBinding freeze/verify
  -> TE public payload
  -> actual new-evaluator
  -> Artifact/Trace persistence
  -> Replay
  -> Report Rebuild
```

Single run result:

```text
selected: U04, U05, U06, A04, G06
validated: 5/5
provider_calls: 0
network_calls: 0
```

Per-method:

| Method | Oracle hash | Binding | Actual EV | Replay | Report | Status |
|---|---|---|---|---|---|---|
| U04 | 0668d404… | 51b3454a… | pass | true | true | PASS |
| U05 | f65d1993… | cfa43002… | pass | true | true | PASS |
| U06 | c526cc58… | 4073e89d… | pass | true | true | PASS |
| A04 | ba538a4d… | 28b98c27… | pass | true | true | PASS |
| G06 | 483a9577… | 2e583968… | pass | true | true | PASS |

Artifacts: `evidence/unified/result.json`, `evidence/unified/trace.jsonl`, per-method `evidence/unified/<MID>/`.
