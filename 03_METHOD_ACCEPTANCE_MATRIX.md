# WP1 Method Acceptance Matrix

| Method | Oracle | Binding | Actual EV | Replay | Report | Unified T1–T7 |
|---|---|---|---|---|---|---|
| U04 | VALID | PASS | pass | true | true | NOT_VERIFIED |
| U05 | VALID | PASS | pass | true | true | NOT_VERIFIED |
| U06 | VALID | PASS | pass | true | true | NOT_VERIFIED |
| A04 | VALID | PASS | pass | true | true | NOT_VERIFIED |
| G06 | VALID | PASS | pass | true | true | NOT_VERIFIED |

```text
METHOD_CHAIN_VALIDATED = 5
NEW_METHODS_E2E_VALIDATED = NOT_VERIFIED
```
Reason: "method chain" = Oracle + binding + actual new-evaluator + replay + report; it does not yet run through the unified T1–T7 `run_offline`/`run_integrated` method-selection path.
