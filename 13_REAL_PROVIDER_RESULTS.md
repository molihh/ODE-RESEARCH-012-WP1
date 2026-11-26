# Real Provider Results — deepseek-flash

## Quota

```text
HTTP attempts: 12
  1 x 401 invalid handoff token (no model response)
  11 x valid requests
Automatic retries: 0
```

## Results

| Method | HTTP | Returned model | Actual EV |
|---|---|---|---|
| U04 | 200 | deepseek-flash | FAIL（empty content） |
| U05 | 200 | deepseek-flash | PASS |
| U06 | 200 | deepseek-flash | PASS |
| A04 | 200 | deepseek-flash | PASS |
| G06 | 200 | deepseek-flash | PASS |
| G02 | 200 | deepseek-flash | FAIL（empty content） |
| U07 | 200 | deepseek-flash | FAIL（返回两个 API 名） |
| A06 | 200 | deepseek-flash | FAIL（empty content） |
| D04 | 200 | deepseek-flash | PASS |
| U10 | 200 | deepseek-flash | FAIL（canonical 含 Inplace） |
| D07 | 200 | deepseek-flash | PASS |

```text
REAL_EV_PASS = 6 / 11
```

## Failure detail

- U04/G02/A06: `content` empty at `max_tokens=256`; answer persisted as `_raw: ""`.
- U07: `aclnnAddGetWorkspaceSize / aclnlnInplaceAddGetWorkspaceSize` instead of one value.
- U10: `aclnnAdd&aclnnInplaceAdd` instead of canonical `aclnnAdd`.

## Status

```text
WP1_OFFLINE_METHOD_CHAIN = PASS
WP1_REAL_PROVIDER        = PARTIAL
```

No retry was made. A new authorization is required for additional real calls.

## Follow-up retries

```text
U04: 2048 tokens -> PASS
G02: 2048 tokens -> FAIL（JSON truncated; no complete quote/line fields）
```

Final real result:

```text
REAL_EV_PASS = 10 / 11
FAILED = G02（最终输出选择声明行 45–51，Gold 为 heading line 1）
```

Total HTTP attempts across all real phases: 21（1×401 + 20×valid）.

No further retry was made.
