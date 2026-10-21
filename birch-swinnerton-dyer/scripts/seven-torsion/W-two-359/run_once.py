"""Single combined watchdog, exclusive execution, no retry."""
from pathlib import Path
import json, math, os, signal, subprocess, sys, time
D=Path(__file__).resolve().parent; START=time.monotonic(); CAP=134217728
def save(n,x):
    with (D/n).open('x') as f: json.dump(x,f,separators=(',',':')); f.write('\n')
def size():return sum(p.stat().st_size for p in D.rglob('*') if p.is_file())
save('run-start.json',{'required_seconds':180,'required_bytes':CAP,'prepared_sources':['run_once.py','stage.py'],'prewatchdog_mathematics':False,'all_prepared_bytes_included':True})
fail=[]
with (D/'worker.log').open('x') as log:
    child=subprocess.Popen([sys.executable,'-B',str(D/'stage.py')],stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
    while child.poll() is None:
        if time.monotonic()-START>=180 or size()>CAP-65536:
            fail.append('combined_time_or_byte_cap');os.killpg(child.pid,signal.SIGKILL);child.wait();break
        time.sleep(.01)
if child.returncode:fail.append('stage_exit_'+str(child.returncode))
if time.monotonic()-START>=180 or size()>CAP-16384:fail.append('final_bound')
save('watchdog.json',{'status':'STOP' if fail else 'PASS','failures':fail,'seconds_before_write':time.monotonic()-START,'bytes_before_write':size(),'required_seconds':180,'required_bytes':CAP})
sec=math.ceil(time.monotonic()-START)+1;byt=size()+4096;ok=sec<180 and byt<CAP
save('final-bound.json',{'status':'PASS' if not fail and ok else 'STOP','seconds_upper_bound':sec,'bytes_upper_bound':byt,'required_seconds':180,'required_bytes':CAP})
if time.monotonic()-START>sec or size()>byt or not ok:
    fail.append('inclusive_final_write_bound');save('late-bound-failure.json',{'failures':fail})
print(json.dumps({'status':'STOP' if fail else 'PASS','failures':fail,'seconds':time.monotonic()-START,'bytes':size(),'required_seconds':180,'required_bytes':CAP,'path':str(D)}))
sys.exit(1 if fail else 0)
