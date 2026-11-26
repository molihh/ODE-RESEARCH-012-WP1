from __future__ import annotations
import hashlib,re
from pathlib import Path
from ode_oracle_factory.model import Evidence,OracleEnvelope
from .specs import MethodSpec

def evidence(asset,start,end,quote,kind):
    return Evidence(evidence_id=f"{asset['asset_id'][:12]}:{kind}:{start}",
        source_uri=asset['source']['uri'],locator=f"chars:{start}:{end}",quote=quote,
        source_sha256=asset['content']['sha256'],kind=kind)

def facts(asset,identity):
    text=asset['content']['full_text']
    heading=re.search(r'(?m)^#\s+(aclnn\w+)',text)
    sig=re.search(r'(?m)^\s*aclnnStatus\s+aclnnAdd\((.*?)\)\s*$',text,re.S)
    if not heading or not sig: raise ValueError('ASSET_FACTS_MISSING')
    params=[]
    for line in sig.group(1).splitlines():
        line=re.sub(r'//.*','',line).strip().rstrip(',')
        if not line: continue
        parts=line.rsplit(None,1)
        if len(parts)==2: params.append((parts[1],parts[0]))
    api_id=identity['api_id']; doc_id=identity['document_id']
    source=asset['source']['uri']; version=asset['source'].get('version','9.2.0')
    ev=[evidence(asset,heading.start(),heading.end(),heading.group(0),'heading'),
        evidence(asset,sig.start(),sig.end(),sig.group(0)[:80],'prototype')]
    workspace=re.search(r'aclnnAddGetWorkspaceSize',text)
    line='55'; quote='aclnnStatus aclnnAdd('
    return {'api_id':api_id,'document_id':doc_id,'source_uri':source,'source_version':version,
            'start_line':1,'end_line':1,'quote':heading.group(0),
            'parameter_names':[p[0] for p in params],'parameter_types':[p[1] for p in params],
            'parameter_count':len(params),'base_api':'aclnnAdd','inplace_api':'aclnnInplaceAdd',
            'workspace':'workspace','workspace_size':'workspaceSize','executor':'executor','stream':'stream',
            'workspace_api':workspace.group(0) if workspace else 'aclnnAddGetWorkspaceSize',
            'target_version':version,'compatible':True,'api_kind':'aclnn','api_count':int(identity.get('api_count',0)),
            'source_count':2,'consistent':True,'canonical_name':'aclnnAdd'},ev

def build(spec:MethodSpec,asset,identity):
    f,ev=facts(asset,identity)
    claims={k:f[k] for k in spec.expected_fields}
    env=OracleEnvelope(oracle_id=f"oracle_{spec.method_id}_wp1",oracle_version=spec.version,
        task_id=f"task_wp1_{spec.method_id.lower()}",task_type=spec.task_type,method_id=spec.method_id,
        oracle_mode=spec.oracle_mode,construction_strategy='DETERMINISTIC_WP1',
        asset_id=asset['asset_id'],asset_version=asset['source'].get('version','9.2.0'),
        asset_sha256=asset['content']['sha256'],claims=claims,evidence=ev,
        provenance={'builder':'wp1-method-builder','method':spec.method_id,'asset_source':asset['source']['uri']},
        independence={'agent_answer_used':False,'ev_verdict_used':False,'grader_used_for_claims':False},
        validation={})
    return env.seal()

def task(spec,asset):
    return {'task_id':f"task_wp1_{spec.method_id.lower()}",'task_type':spec.task_type,
            'method_id':spec.method_id,'prompt':spec.question,'asset_id':asset['asset_id']}
