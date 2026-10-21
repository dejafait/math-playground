"""No retries: external watchdog and total new-evidence bound."""
from pathlib import Path
import subprocess,sys,time,json,hashlib
R=Path(__file__).resolve().parent;U=R.parent
name=sys.argv[1];assert name in ['build_incidence','verify_incidence']
if name=='build_incidence':
    manifest={str(p.relative_to(U)):hashlib.sha256(p.read_bytes()).hexdigest() for p in U.rglob('*') if p.is_file() and R not in p.parents and '__pycache__' not in p.parts}
    with (R/'originals.json').open('x') as f:json.dump(manifest,f,separators=(',',':'))
t=time.monotonic()
with (R/(name+'.log')).open('x') as f:
    try:
        p=subprocess.run([sys.executable,'-B',str(R/(name+'.py'))],stdout=f,stderr=subprocess.STDOUT,timeout=181)
        result={'returncode':p.returncode,'watchdog_fired':False}
    except subprocess.TimeoutExpired:result={'returncode':None,'watchdog_fired':True}
result.update(stage=name,seconds=time.monotonic()-t,required_seconds=180,external_seconds_cap=181,bytes_before_report=sum(p.stat().st_size for p in R.rglob('*') if p.is_file()),required_bytes=134217728)
with (R/(name+'-watchdog.json')).open('x') as f:json.dump(result,f)
print(json.dumps(result));sys.exit(0 if result['returncode']==0 and result['bytes_before_report']<=134217728 else 1)
