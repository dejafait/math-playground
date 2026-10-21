"""One 180-second aggregate allowance, not renewed between stages."""
from pathlib import Path
import hashlib,json,subprocess,sys,time
D=Path(__file__).resolve().parent
start=time.monotonic();report={'status':'STOP','stages':[],'failures':[]}
try:
    for stage in ('produce','verify'):
        remaining=180-(time.monotonic()-start)
        if remaining<=0:raise TimeoutError('aggregate_internal_180_second_cap')
        with (D/(stage+'.log')).open('x') as log:
            result=subprocess.run([sys.executable,'-B',str(D/(stage+'.py'))],stdout=log,stderr=subprocess.STDOUT,timeout=remaining)
        report['stages'].append({'stage':stage,'returncode':result.returncode,'aggregate_elapsed':time.monotonic()-start})
        if result.returncode:raise ArithmeticError(stage+'_failed_no_retry')
        if sum(p.stat().st_size for p in D.iterdir() if p.is_file())+32768>134217728:raise OverflowError('aggregate_byte_cap')
    report['status']='PASS'
except Exception as e:report['failures']=[type(e).__name__+': '+str(e)]
finally:
    ip=D/'input-hashes.json'
    if ip.exists():
        before=json.loads(ip.read_text());root=D.parents[2]
        after={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in before}
        with (D/'preservation-aggregate.json').open('x') as f:json.dump({'before':before,'after':after,'equal':before==after},f)
        if before!=after:report['status']='STOP';report['failures'].append('original_input_changed')
    report.update(seconds=time.monotonic()-start,internal_limit=180,byte_limit=134217728)
    with (D/'aggregate-report.json').open('x') as f:json.dump(report,f)
    print(json.dumps(report))
sys.exit(0 if report['status']=='PASS' and report['seconds']<=180 else 1)
