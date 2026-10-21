"""Independent watchdog; child stages also arm their own 180-second timer."""
from pathlib import Path
import hashlib,json,subprocess,sys,time
R=Path(__file__).resolve().parent
stage=sys.argv[1]
t=time.monotonic()
with (R/(stage+'.log')).open('x') as log:
    try:
        p=subprocess.run([sys.executable,str(R/(stage+'.py'))],stdout=log,
                         stderr=subprocess.STDOUT,timeout=181)
        result={'returncode':p.returncode,'watchdog_fired':False}
    except subprocess.TimeoutExpired:
        result={'returncode':None,'watchdog_fired':True}
result.update(seconds=time.monotonic()-t,child_limit=180,watchdog_limit=181,
              stage=stage,certificate_bytes=sum(p.stat().st_size for p in R.rglob('*') if p.is_file()),
              byte_cap=128*1024*1024)
(R/(stage+'-watchdog.json')).write_text(json.dumps(result)+'\n')
print(json.dumps(result))

