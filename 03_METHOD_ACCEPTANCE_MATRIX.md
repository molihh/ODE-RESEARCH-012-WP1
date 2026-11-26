# WP1 Method Acceptance Matrix

| Method | Oracle | Binding | Actual EV | Replay | Report | Unified WP1 Runner |
|---|---|---|---|---|---|---|
| U04 | VALID | PASS | pass | true | true | PASS |
| U05 | VALID | PASS | pass | true | true | PASS |
| U06 | VALID | PASS | pass | true | true | PASS |
| A04 | VALID | PASS | pass | true | true | PASS |
| G06 | VALID | PASS | pass | true | true | PASS |

```text
METHOD_CHAIN_VALIDATED = 5
NEW_METHODS_E2E_VALIDATED = 5
```
The unified WP1 method-chain runner executes selector -> Oracle -> binding -> TE/EV -> trace -> replay/report. It is not the production `run_integrated`; that distinction is retained in limitations.
