"""Setup templates prepared before watchdog; all bytes counted and disclosed."""
from pathlib import Path
import hashlib,json,math,os,signal,subprocess,sys,time
D=Path(__file__).resolve().parent; CAP=134217728; START=time.monotonic()
def size():return sum(p.stat().st_size for p in D.rglob('*') if p.is_file())
def save(name,obj):
    with (D/name).open('x') as f:json.dump(obj,f,separators=(',',':'));f.write('\n')
if len(sys.argv)>1:
    for src,name in [(D/'stage-template.py','stage.py'),(D/'independent-template.py','independent.py'),(D.parent/'preserved-table-replay-331/verify.py','verify.py')]:
        with (D/name).open('xb') as f:f.write(src.read_bytes())
    with (D/'stage.log').open('x') as log:
        sys.exit(subprocess.run([sys.executable,'-B',str(D/'stage.py')],stdout=log,stderr=subprocess.STDOUT).returncode)
save('run-start.json',{'required_seconds':180,'required_bytes':CAP,'prewatchdog_setup_files':['run_once.py','stage-template.py','independent-template.py'],'prewatchdog_mathematical_checks':False})
fail=[]
with (D/'worker.log').open('x') as log:
    child=subprocess.Popen([sys.executable,'-B',str(Path(__file__).resolve()),'worker'],stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
    while child.poll() is None:
        if time.monotonic()-START>=180 or size()>CAP-65536:
            fail.append('combined_time_or_byte_cap');os.killpg(child.pid,signal.SIGKILL);child.wait();break
        time.sleep(.01)
if child.returncode:fail.append('stage_exit_'+str(child.returncode))
if time.monotonic()-START>=180 or size()>CAP-16384:fail.append('final_bound')
save('watchdog.json',{'status':'STOP' if fail else 'PASS','failures':fail,'seconds_before_write':time.monotonic()-START,'bytes_before_write':size(),'required_seconds':180,'required_bytes':CAP})
elapsed=time.monotonic()-START; total=size()
upper_seconds=math.ceil(elapsed)+1; upper_bytes=total+4096
save('final-bound.json',{'status':'STOP' if fail or upper_seconds>=180 or upper_bytes>=CAP else 'PASS','seconds_upper_bound':upper_seconds,'bytes_upper_bound':upper_bytes,'required_seconds':180,'required_bytes':CAP})
if time.monotonic()-START>upper_seconds or size()>upper_bytes or upper_seconds>=180 or upper_bytes>=CAP:
    fail.append('inclusive_final_write_bound');save('late-bound-failure.json',{'failures':fail})
print(json.dumps({'status':'STOP' if fail else 'PASS','failures':fail,'seconds':time.monotonic()-START,'bytes':size(),'required_seconds':180,'required_bytes':CAP,'path':str(D)}))
sys.exit(1 if fail else 0)
