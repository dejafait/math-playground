"""I/O and fixed stage limits only; no mathematical helpers."""
from pathlib import Path
from fractions import Fraction
import hashlib,json,signal,time
R=Path(__file__).resolve().parent
U=R.parent
CAP=134217728
def enc(v):
    if isinstance(v,Fraction):return str(v)
    if isinstance(v,(list,tuple)):return [enc(x) for x in v]
    if isinstance(v,dict):return {str(k):enc(x) for k,x in v.items()}
    return v
def read(p):return json.loads(p.read_text())
def save(name,value):
    s=json.dumps(enc(value),separators=(',',':'))+'\n'
    assert sum(p.stat().st_size for p in R.rglob('*') if p.is_file())+len(s.encode())<=CAP,'combined byte cap'
    with (R/name).open('x') as f:f.write(s)
def alarm(*_):raise TimeoutError('fixed 180-second stage cap')
def start():
    signal.signal(signal.SIGALRM,alarm);signal.alarm(180)
    return time.monotonic()
def finish(name,result,t):
    signal.alarm(0)
    inv=read(R/'originals.json')
    changed=[p for p,h in inv.items() if not (U/p).is_file() or hashlib.sha256((U/p).read_bytes()).hexdigest()!=h]
    result.update(seconds=time.monotonic()-t,required_seconds=180,preserved_files=len(inv),changed_or_missing=changed)
    if result['seconds']>180:result['passed']=False;result['failures'].append('180-second stage bound exceeded')
    if changed:result['passed']=False;result['failures'].append('original bytes changed')
    save(name+'-report.json',result)
    print(json.dumps({k:v for k,v in result.items() if k!='checks'}),flush=True)

