"""One total external watchdog; no child receives a renewed audit budget."""
from pathlib import Path
import subprocess,sys,time,json
R=Path(__file__).resolve().parent;CAP=134217728
t=time.monotonic();reason=None
with (R/'audit.log').open('x') as log:
    p=subprocess.Popen([sys.executable,'-B',str(R/'audit.py')],stdout=log,stderr=subprocess.STDOUT)
    while p.poll() is None:
        if time.monotonic()-t>=181:reason='181-second external watchdog'
        if sum(x.stat().st_size for x in R.rglob('*') if x.is_file())>CAP:reason='whole-directory byte cap'
        if reason:p.kill();p.wait();break
        time.sleep(.05)
result={'returncode':p.returncode,'seconds':time.monotonic()-t,'external_seconds_cap':181,'internal_seconds_cap':180,'bytes_before_report':sum(x.stat().st_size for x in R.rglob('*') if x.is_file()),'required_bytes':CAP,'watchdog_fired':reason is not None,'failure':reason}
s=json.dumps(result)+'\n'
assert result['bytes_before_report']+len(s.encode())<=CAP
with (R/'watchdog.json').open('x') as f:f.write(s)
print(s,end='');sys.exit(0 if p.returncode==0 and reason is None else 1)
