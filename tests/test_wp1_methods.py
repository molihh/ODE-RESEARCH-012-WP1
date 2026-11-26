import json
from pathlib import Path
import pytest
from wp1_methods import SPECS, build, task, select

ROOT=Path('/Users/chj/Desktop/ode'); BASE=Path(__file__).parents[1]
ASSET=json.loads((ROOT/'ODE-PROD-004/AUTO_D01_SUITE/asset_input.json').read_text())
IDENTITY={'api_id':'e73eb03c3bc1f30f8ca079eaedf484caf318fc7bf2aa6408d9d398980a191e34','document_id':'531700089d39d2560a73db308b593d7ca8702deac97d56b74174828dc214d1f4'}

def test_five_specs():
    assert {'U04','U05','U06','A04','G06','G02','U07','A06','D04','U10','D07'} <= set(SPECS)

@pytest.mark.parametrize('mid',['U04','U05','U06','A04','G06'])
def test_oracle_valid_identity(mid):
    e=build(SPECS[mid],ASSET,IDENTITY)
    assert e.status=='VALID'; assert e.verify_hash(); assert e.oracle_mode=='B'
    assert e.claims; assert e.evidence
    if 'api_id' in e.claims: assert e.claims['api_id']!=e.asset_id

@pytest.mark.parametrize('mid',['U04','U05','U06','A04','G06'])
def test_evidence_run_results(mid):
    rows=json.loads((BASE/'evidence/results.json').read_text())
    r=next(x for x in rows if x['method_id']==mid)
    assert r['preflight']=='READY'; assert r['actual_ev_verdict']=='pass'
    assert r['local_verdict']=='PASS'; assert r['replay'] is True; assert r['report_identical'] is True
    assert r['provider_calls']==0

def test_auto_selector_trace():
    selected,excluded=select(['U04','U05','U06','A04','G06','D99'],asset_type='api')
    assert [s.method_id for s in selected]==['U04','U05','U06','A04','G06']
    assert excluded==[{'method_id':'D99','reason':'NOT_REGISTERED'}]

def test_wrong_asset_type_excluded():
    selected,excluded=select(['U04','D07'],asset_type='api')
    assert [s.method_id for s in selected]==['U04']; assert excluded[0]['method_id']=='D07'
