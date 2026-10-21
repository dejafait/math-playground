"""One execution per stage; enforce external time and combined byte bounds."""
from pathlib import Path
import subprocess,sys,time,json
R=Path(__file__).resolve().parent
stage=sys.argv[1];assert stage in ('build_norms','verify_norms')
if stage=='verify_norms':assert json.loads((R/'construction-report.json').read_text())['passed']
t=time.monotonic();reason=None
with (R/(stage+'.log')).open('x') as log:
    p=subprocess.Popen([sys.executable,'-B',str(R/(stage+'.py'))],stdout=log,stderr=subprocess.STDOUT)
    while p.poll() is None:
        if time.monotonic()-t>=181:reason='181-second external watchdog'
        if sum(x.stat().st_size for x in R.rglob('*') if x.is_file())>134217728:reason='combined 128-MiB cap'
        if reason:p.kill();p.wait();break
        time.sleep(.05)
size=sum(x.stat().st_size for x in R.rglob('*') if x.is_file())
result={'stage':stage,'returncode':p.returncode,'seconds':time.monotonic()-t,'external_seconds_cap':181,'stage_seconds_cap':180,'bytes_before_report':size,'required_bytes':134217728,'watchdog_fired':reason is not None,'failure':reason}
s=json.dumps(result)+'\n'
assert size+len(s.encode())<=134217728,'cap exceeded; do not write further'
with (R/(stage+'-watchdog.json')).open('x') as f:f.write(s)
print(s,end='');sys.exit(0 if p.returncode==0 and reason is None else 1)
