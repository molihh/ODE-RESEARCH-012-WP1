# WP1 Baseline and Method Selection

Baseline: WP2-FINAL=PASS; code `649fe587…`; deterministic KB Gold accepted.
Target KB v02: API docs; v03: engineering symbols only.

Selected 5 methods (all offline-tested, actual v02 asset support):

- U04 约束关系组合 — parameter names/types/count.
- U05 多跳理解 — official api_id + document_id.
- U06 对比/差异 — base/inplace API names.
- A04 参数配置 — workspace/workspaceSize/executor/stream names.
- G06 来源与版本核验 — source_uri + version.

Excluded: D07 from v02 (engineering-only), D99 (not registered). Registry-only/offline-tested status alone was not counted as E2E.
