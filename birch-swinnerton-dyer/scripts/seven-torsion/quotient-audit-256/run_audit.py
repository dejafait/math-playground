"""Bounded stages; all reports fresh; no stopped construction is invoked."""
from pathlib import Path
import hashlib,json,subprocess,sys,time
R=Path(__file__).resolve().parent; U=R.parent
stages=[('upstream',U/'verify_certificate.py'),('actions',U/'scalar-actions-243/verify_actions.py'),('direction',U/'compressed-249/verify_direction.py'),('quotient',R/'replay_quotient.py'),('crosscheck',R/'crosscheck.py')]
records=[]
for name,script in stages:
    cmd=[sys.executable,'-B',str(script)]
    if name in ['upstream','actions','direction']:
        out=R/(name+'.json');assert not out.exists();cmd+=['--report',str(out)]
    start=time.monotonic()
    with (R/(name+'.log')).open('x') as log:
        try:
            p=subprocess.run(cmd,stdout=log,stderr=subprocess.STDOUT,timeout=181)
            rc=p.returncode; timeout=False
        except subprocess.TimeoutExpired:rc=None; timeout=True
    record={'stage':name,'returncode':rc,'watchdog_fired':timeout,'seconds':time.monotonic()-start,'required_seconds':180,'watchdog_seconds':181}
    records.append(record)
    with (R/'stages.json').open('w') as f:json.dump(records,f,indent=2)
    print(json.dumps(record),flush=True)
    if rc!=0 or record['seconds']>180:raise SystemExit(1)
m=json.loads((R/'original-manifest.json').read_text())
changed=[p for p,d in m.items() if not (U/p).is_file() or hashlib.sha256((U/p).read_bytes()).hexdigest()!=d]
size=sum(p.stat().st_size for p in R.rglob('*') if p.is_file())
result={'passed':not changed and size<134217728,'failures':changed,'original_files':len(m),'changed_or_missing':changed,'bytes_before_final_report':size,'required_byte_bound':134217728,'stages':records}
with (R/'audit-report.json').open('x') as f:json.dump(result,f,indent=2)
print(json.dumps({k:v for k,v in result.items() if k!='stages'}));assert result['passed']
