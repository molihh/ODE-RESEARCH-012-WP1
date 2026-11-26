"""Adapter used by Integration's run_integrated method_pack branch."""
from __future__ import annotations
import json
from pathlib import Path
from .runner import run_all

def run_method_pack(production_config, output):
    cfg=production_config['method_pack']
    base=Path(cfg['wp1_base']); asset=json.loads(Path(cfg['asset_path']).read_text()); identity=json.loads(Path(cfg['identity_path']).read_text())
    v03_asset=json.loads(Path(cfg['v03_asset_path']).read_text()) if cfg.get('v03_asset_path') else None
    v03_kb=Path(cfg['v03_kb']) if cfg.get('v03_kb') else None
    result=run_all(base=base,asset=asset,identity=identity,requested=cfg.get('methods'),output=output,v03_asset=v03_asset,v03_kb=v03_kb)
    result['run_id']=f"run_wp1_{Path(output).name}"
    result['status']='PASS' if result['validated']>=6 else 'PARTIAL'
    result['new_DeepSeek_requests']=0
    (Path(output)/'run-receipt.json').write_text(json.dumps({k:result[k] for k in ('run_id','status','validated','provider_calls','network_calls')},indent=2)+'\n')
    return result
