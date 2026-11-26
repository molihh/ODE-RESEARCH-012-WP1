from __future__ import annotations
from dataclasses import dataclass, field

@dataclass(frozen=True)
class MethodSpec:
    method_id: str
    name: str
    dimension: str
    task_type: str
    question: str
    expected_fields: tuple[str, ...]
    asset_type: str = "api"
    oracle_mode: str = "B"
    version: str = "1.0.0"

SPECS = {
    "U04": MethodSpec("U04","约束关系组合","understand","auto_d06",
        "列出该 API 基础声明的参数名、参数类型和参数数量，按声明顺序返回。",
        ("parameter_names","parameter_types","parameter_count")),
    "U05": MethodSpec("U05","多跳理解","understand","auto_d06",
        "同时给出该 API 的 official api_id 与所属 Target KB document_id。",
        ("api_id","document_id")),
    "U06": MethodSpec("U06","对比/差异理解","understand","auto_d06",
        "该文档同时描述了 base API 与 inplace API；给出两个 API 名。",
        ("base_api","inplace_api")),
    "A04": MethodSpec("A04","参数配置","apply","auto_d06",
        "给出调用该 API 时 workspace、workspaceSize、executor、stream 对应的参数名。",
        ("workspace","workspace_size","executor","stream")),
    "G06": MethodSpec("G06","来源与版本核验","ground_verify","auto_d06",
        "给出该 API 文档的官方 source_uri 与 source_version。",
        ("source_uri","source_version")),
}

KNOWN_ASSET_TYPES = {"D07": "engineering_evidence"}

def select(method_ids, asset_type="api"):
    selected=[]; excluded=[]
    for mid in method_ids:
        spec=SPECS.get(mid)
        if spec is None:
            reason = "ASSET_TYPE_MISMATCH" if KNOWN_ASSET_TYPES.get(mid) not in (None, asset_type) else "NOT_REGISTERED"
            excluded.append({"method_id":mid,"reason":reason}); continue
        if spec.asset_type != asset_type: excluded.append({"method_id":mid,"reason":"ASSET_TYPE_MISMATCH"}); continue
        selected.append(spec)
    return selected,excluded
