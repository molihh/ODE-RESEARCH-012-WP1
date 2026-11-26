"""One-shot real DeepSeek solver for WP1. No retries, raw I/O persisted."""
from __future__ import annotations
import json, os, time
from pathlib import Path
import httpx

def _key():
    key=os.environ.get('DEEPSEEK_API_KEY')
    if key: return key
    import yaml
    data=yaml.safe_load(Path('/Users/chj/Desktop/ode/native/credentials/.credentials.yaml').read_text())
    rec=data['records']['deepseek-account-platform/default']
    return rec['payload']['token']

def prompt(spec, asset, *, source_uri, extra_context=None):
    text=asset['content']['full_text']
    numbered='\n'.join(f'[L{i+1}] {line}' for i,line in enumerate(text.splitlines()))
    return (f"Asset source_uri: {source_uri}\nAsset version: {asset.get('source',{}).get('version','')}\n"
            f"Question: {spec.question}\n"
            f"Required JSON keys: {', '.join(spec.expected_fields)}.\n"
            + (f"Retrieved context: {extra_context}\n" if extra_context else "")
            + "Use only the frozen asset/retrieved context. Return ONLY one JSON object, no markdown.\n"
            f"ASSET:\n{numbered}")

def solve(spec, asset, out_dir, extra_context=None):
    key=_key(); out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
    body={'model':'deepseek-flash','temperature':0,'max_tokens':4096,
          'messages':[{'role':'system','content':'Answer from the frozen CANN asset. Return strict JSON only.'},
                      {'role':'user','content':prompt(spec,asset,source_uri=asset['source']['uri'],extra_context=extra_context)}]}
    raw=json.dumps(body,ensure_ascii=False,sort_keys=True).encode()
    (out/'request.bin').write_bytes(raw)
    started=time.time()
    with httpx.Client(timeout=60,trust_env=False) as c:
        r=c.post('https://api.deepseek.com/chat/completions',headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'},content=raw)
    (out/'response.bin').write_bytes(r.content)
    try: resp=r.json()
    except Exception: resp={}
    content=''
    try: content=resp['choices'][0]['message']['content']
    except Exception: pass
    (out/'raw-output.txt').write_text(content)
    meta={'http_status':r.status_code,'model':resp.get('model'),'usage':resp.get('usage',{}),
          'request_sha256':__import__('hashlib').sha256(raw).hexdigest(),
          'response_sha256':__import__('hashlib').sha256(r.content).hexdigest(),
          'elapsed_seconds':round(time.time()-started,3),'request_id':r.headers.get('x-request-id')}
    (out/'meta.json').write_text(json.dumps(meta,indent=2)+'\n')
    if r.status_code!=200: raise RuntimeError(f'PROVIDER_HTTP_{r.status_code}')
    # strict JSON extraction
    s=content.strip()
    if s.startswith('```'):
        s=s.split('\n',1)[1].rsplit('```',1)[0].strip()
    try: return json.loads(s), meta
    except Exception:
        return {'_raw':content}, meta
