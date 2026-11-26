# Publication — Plan 2

## Independent repos

```text
WP1: https://github.com/molihh/ODE-RESEARCH-012-WP1
     main = f5a6a00c1560771facafed5e6a06ba4d53cd191b（发布时）
WP2: https://github.com/molihh/ODE-RESEARCH-012-WP2
     main = 7d2fec7652ccab77df4c216e6f3c76c191973688
```

WP1 `pyproject.toml` 锁定 WP2 版本；WP2 包包含 `ode_oracle_factory` 与 `wp2_runtime`。

## Integration

```text
PR #87
merge commit: 8e0a3d57d173e7b79aeffa1de0eba73c323a91c7
```

只增加：

```text
src/ode_integration/production/wp1_method_pack.py
src/ode_integration/production/integrated.py  (method_pack branch)
requirements-wp1.txt  (pinned WP1/WP2 refs)
```

没有把 WP1/WP2 源码复制进 Integration，符合方案 2。

## Real Provider

```text
G02 final retry = FAIL
REAL_EV_PASS = 10/11
```

方案 2 仍按 Owner 指令执行；没有把 G02 失败写成 PASS。
