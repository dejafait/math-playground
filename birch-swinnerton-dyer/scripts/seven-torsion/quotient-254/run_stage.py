"""External watchdog and directory byte-bound enforcement for each declared stage."""
from pathlib import Path
import hashlib,json,subprocess,sys,time
R=Path(__file__).resolve().parent
stage=sys.argv[1];assert stage in ['build_quotient','verify_quotient']
t=time.monotonic()
if stage=='build_quotient':
    manifest={str(p.relative_to(R.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in R.parent.rglob('*') if p.is_file() and R not in p.parents and '__pycache__' not in p.parts}
    with (R/'production-input-manifest.json').open('x') as f:f.write(json.dumps(manifest,separators=(',',':'))+'\n')
with (R/(stage+'.log')).open('x') as f:
    try:
        p=subprocess.run([sys.executable,str(R/(stage+'.py'))],stdout=f,stderr=subprocess.STDOUT,timeout=181)
        result={'returncode':p.returncode,'watchdog_fired':False}
    except subprocess.TimeoutExpired:result={'returncode':None,'watchdog_fired':True}
result.update(stage=stage,seconds=time.monotonic()-t,child_seconds_cap=180,external_seconds_cap=181,
              bytes_before_report=sum(p.stat().st_size for p in R.rglob('*') if p.is_file()),byte_cap=134217728)
with (R/(stage+'-watchdog.json')).open('x') as f:f.write(json.dumps(result)+'\n')
print(json.dumps(result));sys.exit(0 if result['returncode']==0 and result['bytes_before_report']<=result['byte_cap'] else 1)
