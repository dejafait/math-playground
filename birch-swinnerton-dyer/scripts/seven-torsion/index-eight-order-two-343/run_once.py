"""One external watchdog, including all setup and final writing."""
from pathlib import Path
import json,math,os,signal,subprocess,sys,time
D=Path(__file__).resolve().parent;START=time.monotonic();CAP=134217728
def save(n,x):
    with (D/n).open('x') as f:json.dump(x,f,separators=(',',':'));f.write('\n')
def size():return sum(p.stat().st_size for p in D.rglob('*') if p.is_file())
if len(sys.argv)>1:
    for name in ['prepare.py','stage.py']:
        with (D/(name+'.log')).open('x') as log:
            rc=subprocess.run([sys.executable,'-B',str(D/name)],stdout=log,stderr=subprocess.STDOUT).returncode
        if rc:sys.exit(rc)
    sys.exit(0)
save('run-start.json',{'required_seconds':180,'required_bytes':CAP,
    'prewatchdog_setup_files':['run_once.py','prepare.py','stage.py'],
    'prewatchdog_mathematical_checks':False,'all_setup_bytes_included':True})
fail=[]
with (D/'worker.log').open('x') as log:
    child=subprocess.Popen([sys.executable,'-B',str(Path(__file__).resolve()),'worker'],stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
    while child.poll() is None:
        if time.monotonic()-START>=180 or size()>CAP-65536:
            fail.append('combined_time_or_byte_cap');os.killpg(child.pid,signal.SIGKILL);child.wait();break
        time.sleep(.01)
if child.returncode:fail.append('stage_exit_'+str(child.returncode))
if time.monotonic()-START>=180 or size()>CAP-16384:fail.append('final_bound')
save('watchdog.json',{'status':'STOP' if fail else 'PASS','failures':fail,
    'seconds_before_write':time.monotonic()-START,'bytes_before_write':size(),
    'required_seconds':180,'required_bytes':CAP})
upper_seconds=math.ceil(time.monotonic()-START)+1;upper_bytes=size()+4096
bound_ok=upper_seconds<180 and upper_bytes<CAP
save('final-bound.json',{'status':'PASS' if not fail and bound_ok else 'STOP',
    'seconds_upper_bound':upper_seconds,'bytes_upper_bound':upper_bytes,
    'required_seconds':180,'required_bytes':CAP})
if time.monotonic()-START>upper_seconds or size()>upper_bytes or not bound_ok:
    fail.append('inclusive_final_write_bound');save('late-bound-failure.json',{'failures':fail})
print(json.dumps({'status':'STOP' if fail else 'PASS','failures':fail,'seconds':time.monotonic()-START,
    'bytes':size(),'required_seconds':180,'required_bytes':CAP,'path':str(D)}))
sys.exit(1 if fail else 0)
