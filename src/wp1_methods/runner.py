"""Unified WP1 method-chain runner: selector -> Oracle -> binding -> TE/EV -> trace -> replay/report."""
from __future__ import annotations
import json, shutil
from pathlib import Path
from .specs import SPECS, select
from .builder import build, task
from wp2_runtime import run_once, replay, rebuild_report
from wp2_runtime.ev_adapter import trace, evaluate_with_ev
from evaluator.suite import Suite
from evaluator.preflight import validate_suite
from ode_oracle_factory.model import sha

def run_all(*, base, asset, identity, requested=None):
    base=Path(base); requested=requested or list(SPECS)
    selected, excluded = select(requested, asset_type='api')
    out=base/'unified'; shutil.rmtree(out,ignore_errors=True); out.mkdir(parents=True)
    records=[]; trace_events=[]
    for spec in selected:
        mid=spec.method_id; suite=base/'evidence'/f'suite-{mid}'
        pre=validate_suite(suite)
        if pre['status']!='READY':
            records.append({'method_id':mid,'status':'BLOCKED','reason':'PREFLIGHT_BLOCKED'}); continue
        env=build(spec,asset,identity); flat=task(spec,asset)
        run_dir=out/mid; rec=run_once(run_dir=run_dir,envelope=env,task=flat,asset=asset,answer=env.claims,
            output_schema_sha256='c'*64,grader_config={'type':'structured_match','version':'0.1','required_fields':list(spec.expected_fields)})
        rep=replay(run_dir); reb=rebuild_report(run_dir)
        m=json.loads((suite/'suite_manifest.json').read_text()); mh=Suite(suite).manifest_hash
        evdir=run_dir/'ev'; tr=trace(env,env.claims,None,run_id=f'wp1-{mid.lower()}',task_id=flat['task_id'],
            suite_id=m['suite_id'],asset_sha=asset['content']['sha256'],manifest_sha=mh)
        (run_dir/'traces.jsonl').write_text(json.dumps(tr)+'\n')
        evrows,summ=evaluate_with_ev(suite,run_dir/'traces.jsonl',evdir)
        event={'method_id':mid,'stage':'ALL','oracle_hash':env.content_hash,'binding':rec['binding_sha256'],
               'actual_ev':evrows[0]['verdict'],'replay':rep['verdict_identical'],'report':reb['byte_identical'],
               'provider_calls':rep['provider_calls'],'status':'PASS' if evrows[0]['verdict']=='pass' and rep['verdict_identical'] and reb['byte_identical'] else 'FAIL'}
        trace_events.append({'seq':len(trace_events)+1,'method_id':mid,'action':'method_chain_completed','status':event['status'],'oracle_hash':env.content_hash})
        records.append(event)
    result={'schema_version':'wp1.unified-method-chain/1','selected':[s.method_id for s in selected],
            'excluded':excluded,'records':records,'trace':trace_events,
            'validated':sum(1 for r in records if r.get('status')=='PASS'),
            'provider_calls':sum(r.get('provider_calls',0) for r in records),
            'network_calls':0}
    (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    (out/'trace.jsonl').write_text('\n'.join(json.dumps(e) for e in trace_events)+'\n')
    return result
