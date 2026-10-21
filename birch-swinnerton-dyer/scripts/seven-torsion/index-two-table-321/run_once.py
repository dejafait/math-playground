"""Two single stages, each at most 180 seconds. No overwrite or retry."""
from pathlib import Path
import json, os, signal, subprocess, sys, time
D=Path(__file__).resolve().parent; CAP=134217728
def save(name,x):
    with (D/name).open('x') as f: json.dump(x,f,separators=(',',':')); f.write('\n')
save('run-start.json',{'stage_limit_seconds':180,'artifact_limit_bytes':CAP})
stages=[]
for program in ('produce','verify'):
    start=time.monotonic(); report={'stage':program,'status':'STOP','timeout':False,'byte_cap':False}
    with (D/(program+'.log')).open('x') as log:
        p=subprocess.Popen([sys.executable,'-B',str(D/(program+'.py'))],stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
        while p.poll() is None:
            seconds=time.monotonic()-start
            size=sum(f.stat().st_size for f in D.iterdir() if f.is_file())
            if seconds>=180 or size>CAP-65536:
                report['timeout']=seconds>=180; report['byte_cap']=size>CAP-65536
                os.killpg(p.pid,signal.SIGKILL); p.wait(); break
            time.sleep(.02)
    report.update(seconds=time.monotonic()-start,returncode=p.returncode,required_seconds=180)
    if p.returncode==0 and not report['timeout'] and not report['byte_cap'] and report['seconds']<=180:
        report['status']='PASS'
    save(program+'-watchdog.json',report); stages.append(report)
    print(json.dumps(report),flush=True)
    if report['status']!='PASS': break
size=sum(f.stat().st_size for f in D.iterdir() if f.is_file())
status='PASS' if len(stages)==2 and all(x['status']=='PASS' for x in stages) and size+16384<=CAP else 'STOP'
result={'status':status,'stages':stages,'artifact_bytes_before_report':size,'required_bytes':CAP,
        'path':str(D),'failures':[] if status=='PASS' else ['single_stage_or_artifact_limit_failure']}
save('aggregate-report.json',result)
print(json.dumps(result),flush=True)
sys.exit(0 if status=='PASS' else 1)
