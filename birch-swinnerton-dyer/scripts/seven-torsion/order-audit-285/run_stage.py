"""External aggregate watchdog; never retries or overwrites prior output."""
from pathlib import Path
import json, os, signal, subprocess, sys, time

R = Path(__file__).resolve().parent
assert not (R/'audit-report.json').exists() and not (R/'watchdog.json').exists()
start = time.monotonic()
with (R/'audit.log').open('x') as log:
    child = subprocess.Popen([sys.executable,'-B',str(R/'audit.py')],
        stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
    try:
        code=child.wait(timeout=181)
        fired=False
    except subprocess.TimeoutExpired:
        os.killpg(child.pid,signal.SIGKILL)
        code=child.wait()
        fired=True
report={'returncode':code,'watchdog_fired':fired,'seconds':time.monotonic()-start,
        'internal_cap':180,'external_cap':181,'required_bytes':134217728}
report['bytes_before_report']=sum(p.stat().st_size for p in R.rglob('*') if p.is_file())
with (R/'watchdog.json').open('x') as f: json.dump(report,f)
report['actual_bytes']=sum(p.stat().st_size for p in R.rglob('*') if p.is_file())
print(json.dumps(report))
sys.exit(0 if code==0 and not fired and report['actual_bytes']<=134217728 else 1)
