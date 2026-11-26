import json
from pathlib import Path
from wp1_methods.runner import run_all

def test_unified_five_methods(tmp_path):
    root=Path('/Users/chj/Desktop/ode'); base=Path('/Users/chj/Desktop/ode/ODE-RESEARCH-012/IMPLEMENTATION/WP1-DSH')
    asset=json.loads((root/'ODE-PROD-004/AUTO_D01_SUITE/asset_input.json').read_text())
    identity={'api_id':'e73eb03c3bc1f30f8ca079eaedf484caf318fc7bf2aa6408d9d398980a191e34','document_id':'531700089d39d2560a73db308b593d7ca8702deac97d56b74174828dc214d1f4'}
    r=run_all(base=base,asset=asset,identity=identity)
    assert r['selected']==['U04','U05','U06','A04','G06']
    assert r['validated']==5
    assert r['provider_calls']==0
    assert all(x['status']=='PASS' for x in r['records'])
