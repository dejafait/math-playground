"""One aggregate external watchdog. Refuses retries and overwrites."""
from pathlib import Path
import json,os,signal,subprocess,sys,time
D=Path(__file__).resolve().parent
with (D/'run-start.json').open('x') as f:json.dump({'external_limit':181,'internal_limit':180,'byte_limit':134217728},f)
t=time.monotonic();report={'status':'STOP','timeout':False,'byte_cap':False}
with (D/'aggregate.log').open('x') as log:
    p=subprocess.Popen([sys.executable,'-B',str(D/'aggregate.py')],stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
    while p.poll() is None:
        elapsed=time.monotonic()-t
        size=sum(q.stat().st_size for q in D.iterdir() if q.is_file())
        if elapsed>=181 or size>134217728-16384:
            report['timeout']=elapsed>=181;report['byte_cap']=size>134217728-16384
            os.killpg(p.pid,signal.SIGKILL);p.wait();break
        time.sleep(.02)
    report['returncode']=p.returncode
report['seconds']=time.monotonic()-t
report.update(external_limit=181,internal_limit=180,byte_limit=134217728)
if not report['timeout'] and not report['byte_cap'] and p.returncode==0 and report['seconds']<=181:report['status']='PASS'
with (D/'watchdog.json').open('x') as f:json.dump(report,f)
size=sum(q.stat().st_size for q in D.iterdir() if q.is_file())
print(json.dumps({**report,'aggregate_bytes':size,'path':str(D)}))
sys.exit(0 if report['status']=='PASS' and size<=134217728 else 1)
