"""One attempt per stage; fixed external watchdog and combined byte cap."""
import json,subprocess,sys,time
from pathlib import Path
D=Path(__file__).resolve().parent;s=sys.argv[1]
assert s in ('produce','verify')
p=D/(s+'-watchdog.json');assert not p.exists()
t=time.monotonic()
try:
 r=subprocess.run([sys.executable,'-B',str(D/(s+'.py'))],capture_output=True,text=True,timeout=181)
 report={'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'timeout':False}
except subprocess.TimeoutExpired as e:report={'timeout':True,'stdout':str(e.stdout),'stderr':str(e.stderr)}
report.update(seconds=time.monotonic()-t,external_limit=181,internal_limit=180,aggregate_bytes=sum(p.stat().st_size for p in D.iterdir() if p.is_file()),byte_limit=134217728)
with p.open('x') as f:json.dump(report,f)
print(json.dumps(report))
