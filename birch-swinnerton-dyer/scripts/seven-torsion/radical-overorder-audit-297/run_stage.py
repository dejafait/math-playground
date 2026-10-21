"""Single aggregate external watchdog; refuses a second invocation."""
from pathlib import Path
import json, subprocess, sys, time
D=Path(__file__).resolve().parent
with (D/'invoked.json').open('x') as f:
    json.dump({'one_attempt':True,'internal_limit':180,'external_limit':181,'byte_limit':134217728},f)
t=time.monotonic()
try:
    p=subprocess.run([sys.executable,'-B',str(D/'audit.py')],capture_output=True,text=True,timeout=181)
    report={'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'timeout':False}
except subprocess.TimeoutExpired as e:
    report={'timeout':True,'stdout':str(e.stdout),'stderr':str(e.stderr)}
report.update(seconds=time.monotonic()-t,external_limit=181,internal_limit=180,
              aggregate_bytes=sum(p.stat().st_size for p in D.iterdir() if p.is_file()),byte_limit=134217728)
with (D/'watchdog.json').open('x') as f:json.dump(report,f)
print(json.dumps(report))
sys.exit(0 if not report['timeout'] and report.get('returncode')==0 and report['aggregate_bytes']<=134217728 else 1)
