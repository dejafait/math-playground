"""A single invocation of each stage; no retry/resumption/overwrite."""
from pathlib import Path
import json, subprocess, sys, time
D=Path(__file__).resolve().parent
s=sys.argv[1]
assert s in ('produce','verify')
p=D/(s+'-watchdog.json')
assert not p.exists()
if s=='verify':
    assert json.loads((D/'producer-report.json').read_text())['status']=='PASS'
    assert json.loads((D/'produce-watchdog.json').read_text())['returncode']==0
t=time.monotonic()
try:
    r=subprocess.run([sys.executable,'-B',str(D/(s+'.py'))],capture_output=True,text=True,timeout=181)
    report={'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'timeout':False}
except subprocess.TimeoutExpired as e:
    report={'timeout':True,'stdout':str(e.stdout),'stderr':str(e.stderr)}
report.update(seconds=time.monotonic()-t,external_limit=181,internal_limit=180,
    aggregate_bytes=sum(q.stat().st_size for q in D.iterdir() if q.is_file()),byte_limit=134217728)
with p.open('x') as f:json.dump(report,f)
print(json.dumps(report))
sys.exit(0 if not report['timeout'] and report.get('returncode')==0 and report['aggregate_bytes']<=134217728 else 1)
