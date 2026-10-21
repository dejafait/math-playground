"""Single externally bounded audit stage; never retries or overwrites."""
from pathlib import Path
import json, os, signal, subprocess, sys, time
D=Path(__file__).resolve().parent
CAP=134217728
def save(name,data):
    with (D/name).open('x') as f: json.dump(data,f,separators=(',',':')); f.write('\n')
save('run-start.json',{'required_seconds':180,'required_bytes':CAP})
start=time.monotonic()
failure=[]
with (D/'audit.log').open('x') as log:
    child=subprocess.Popen([sys.executable,'-B',str(D/'audit.py')],stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
    while child.poll() is None:
        size=sum(p.stat().st_size for p in D.iterdir() if p.is_file())
        if time.monotonic()-start>=180 or size>CAP-65536:
            failure.append('time_or_byte_cap'); os.killpg(child.pid,signal.SIGKILL); child.wait(); break
        time.sleep(.02)
if child.returncode: failure.append('audit_exit_'+str(child.returncode))
size=sum(p.stat().st_size for p in D.iterdir() if p.is_file())
report={'status':'STOP' if failure else 'PASS','returncode':child.returncode,
        'seconds':time.monotonic()-start,'required_seconds':180,
        'bytes_before_watchdog':size,'required_bytes':CAP,'failures':failure}
if report['seconds']>=180 or size+16384>=CAP:
    report['status']='STOP'; failure.append('final_bound')
save('watchdog.json',report)
elapsed=time.monotonic()-start
finalsize=sum(p.stat().st_size for p in D.iterdir() if p.is_file())
if elapsed>=180 or finalsize>=CAP:
    save('late-bound-failure.json',{'seconds':elapsed,'bytes':finalsize})
    sys.exit(1)
print(json.dumps({**report,'seconds_through_watchdog_write':elapsed,'final_bytes':finalsize,'path':str(D)}))
sys.exit(0 if report['status']=='PASS' else 1)
