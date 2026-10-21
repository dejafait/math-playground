"""One-shot 181-second external watchdog for each approved stage."""
import json, subprocess, sys, time
from pathlib import Path
R=Path(__file__).resolve().parent
stage=sys.argv[1]
assert stage in ('produce','verify')
assert not (R/(stage+'-watchdog.json')).exists()
start=time.monotonic()
try:
    result=subprocess.run([sys.executable,'-B',str(R/(stage+'.py'))],capture_output=True,text=True,timeout=181)
    report={'returncode':result.returncode,'stdout':result.stdout,'stderr':result.stderr,'timeout':False}
except subprocess.TimeoutExpired:
    report={'timeout':True}
report.update(seconds=time.monotonic()-start,external_limit=181,internal_limit=180,
              aggregate_bytes=sum(p.stat().st_size for p in R.rglob('*') if p.is_file()),byte_limit=67108864)
with (R/(stage+'-watchdog.json')).open('x') as f: json.dump(report,f)
print(json.dumps(report))
