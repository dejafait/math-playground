"""Fresh reports only; original files and stopped producers are untouched."""
from pathlib import Path
import json, subprocess, sys, time
R=Path(__file__).resolve().parent
U=R.parent
stages=[('upstream',U/'verify_certificate.py'),
        ('actions',U/'scalar-actions-243/verify_actions.py'),
        ('direction',U/'compressed-249/verify_direction.py'),
        ('crosscheck',R/'crosscheck.py')]
records=[]
for name,script in stages:
    report=R/(name+'.json')
    assert not report.exists()
    cmd=[sys.executable,str(script)]
    if name!='crosscheck':cmd+=['--report',str(report)]
    start=time.monotonic()
    with (R/(name+'.log')).open('x') as log:
        try:
            p=subprocess.run(cmd,stdout=log,stderr=subprocess.STDOUT,timeout=181)
            rc=p.returncode; timed_out=False
        except subprocess.TimeoutExpired:
            rc=None; timed_out=True
    record={'stage':name,'returncode':rc,'watchdog_fired':timed_out,
            'seconds':time.monotonic()-start,'required_seconds':180,'watchdog_seconds':181,
            'report':str(report.relative_to(U))}
    records.append(record)
    with (R/'stages.json').open('w') as out:json.dump(records,out,indent=2)
    print(json.dumps(record),flush=True)
    if rc!=0 or record['seconds']>180:raise SystemExit(1)
