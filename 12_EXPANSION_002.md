# WP1 Expansion 002 — Six New Methods

## New methods

| Method | Asset family | Target KB | Actual EV | Negative case |
|---|---|---|---|---|
| G02 精确证据定位 | operator API | v02 | pass | fail |
| U07 边界与例外 | operator API | v02 | pass | fail |
| A06 兼容性决策 | operator API | v02 | pass | fail |
| D04 结构化过滤检索 | operator API | v02 | pass | fail |
| U10 跨来源一致性 | operator API | v02 | pass | fail |
| D07 符号存在性 | engineering evidence | v03 | pass | fail |

Existing baseline methods U04/U05/U06/A04/G06 remain PASS.

## Production entry

`run_integrated` method_pack:

```text
selected: 11
validated: 11
status: PASS
provider_calls: 0
network_calls: 0
```

Evidence: `evidence/production-run-integrated-11/result.json`, `trace.jsonl`, per-method directories.

Negative cases: `evidence/negative.json` — all six new methods fail on wrong answers, as required.

## Coverage

```text
NEW_METHODS_E2E_VALIDATED = 6
TOTAL_WP1_METHODS_VALIDATED = 11
VALIDATED_ASSET_FAMILIES = 2
```
