from pathlib import Path
import subprocess,json,time,sys,hashlib
R=Path(__file__).resolve().parent;stage=sys.argv[1];assert stage=='verify_dual'
if stage=='build_dual':
    paths=[R.parent/'compressed-249/direction.json',R.parent/'quotient-254/quotient.json']
    manifest={str(p.relative_to(R.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    with (R/'input-manifest.json').open('x') as f:json.dump(manifest,f)
t=time.monotonic()
with (R/(stage+'.log')).open('x') as f:
    try:
        p=subprocess.run([sys.executable,'-B',str(R/(stage+'.py'))],stdout=f,stderr=subprocess.STDOUT,timeout=181)
        result={'returncode':p.returncode,'watchdog_fired':False}
    except subprocess.TimeoutExpired:result={'returncode':None,'watchdog_fired':True}
result.update(stage=stage,seconds=time.monotonic()-t,arithmetic_cap_seconds=180,external_cap_seconds=181,bytes_before_report=sum(p.stat().st_size for p in R.rglob('*') if p.is_file()),byte_cap=134217728)
with (R/(stage+'-watchdog.json')).open('x') as f:json.dump(result,f)
print(json.dumps(result));sys.exit(0 if result['returncode']==0 and result['bytes_before_report']<=134217728 else 1)
