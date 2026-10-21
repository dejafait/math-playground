"""All arithmetic in one capped stage; no restart on first mismatch."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,shutil,signal,subprocess,sys,time
import group_law
R=Path(__file__).resolve().parent;U=R.parent
start=time.monotonic();report={'passed':False,'phase':'fresh replay','failures':[],'required_seconds':180,'required_bytes':134217728}
def timeout(*_):raise TimeoutError('single audit stage: 180 seconds')
signal.signal(signal.SIGALRM,timeout);signal.alarm(180)
def save(name,obj):
    data=json.dumps(obj,separators=(',',':'))+'\n'
    size=sum(p.stat().st_size for p in R.rglob('*') if p.is_file())
    if size+len(data.encode())>134217728:raise ValueError('128 MiB evidence cap')
    with (R/name).open('x') as f:f.write(data)
def invoke(path):
    remain=180-(time.monotonic()-start)
    if remain<=0:raise TimeoutError('no audit time remaining')
    with (path/'replay.log').open('x') as log:
        child=subprocess.Popen([sys.executable,'-B',str(path/'verify_dual.py')],stdout=log,stderr=subprocess.STDOUT)
        try:rc=child.wait(timeout=remain)
        finally:
            if child.poll() is None:child.kill();child.wait()
    return rc,json.loads((path/'replay-report.json').read_text())
try:
    rc,replay=invoke(R/'replay')
    if rc or not replay['passed'] or replay['failures']:raise ValueError('fresh replay failed: '+str(replay['failures']))
    report['fresh_replay_seconds']=replay['seconds']
    report['phase']='complete evidence comparison'
    names=['dual.json','normalization.json','reconstruction.json','series.json','basic-identities.json','dual_after_quotient.json','quotient_after_dual.json','dual_after_quotient-recurrence.json','quotient_after_dual-recurrence.json','algebra.json','rejections.json']
    evidence={}
    for name in names:
        fresh=json.loads((R/'replay'/name).read_text());old=json.loads((U/'dual-263'/name).read_text())
        if fresh!=old:raise ValueError('complete evidence mismatch '+name)
        evidence[name]={'complete_recursive_equality':True,'sha256':hashlib.sha256((R/'replay'/name).read_bytes()).hexdigest()}
    save('complete-evidence.json',{'passed':True,'files':evidence,'all_replay_checks':replay['checks'],'failures':[]})
    report['phase']='distinct group-law chain'
    report['group_law']=group_law.run(R)
    report['phase']='fresh malformed-evidence checks'
    rejected=[]
    for label in ['normalization','sign','late-series']:
        folder=R/('reject-'+label);folder.mkdir()
        for name in ['dual.json','normalization.json','reconstruction.json','series.json','input-manifest.json','original-manifest.json','verify_dual.py']:
            shutil.copyfile(R/'replay'/name,folder/name)
        filename='series.json' if label=='late-series' else 'dual.json'
        bad=json.loads((folder/filename).read_text())
        if label=='normalization':bad['x_divisor']=7
        elif label=='sign':bad['normalized_M']=[[str(-F(v)) for v in row] for row in bad['normalized_M']]
        else:bad['T'][-1][0]=str(F(bad['T'][-1][0])+1)
        (folder/filename).write_text(json.dumps(bad,separators=(',',':'))+'\n')
        rc,rr=invoke(folder)
        expected={'normalization':'actual_dual_normalization','sign':'actual_dual_differential_seven','late-series':'complete_Newton_prefix_26'}[label]
        if rc!=1 or rr['passed'] or rr['failures']!=['ValueError: '+expected]:raise ValueError('unintended rejection '+label+': '+str(rr['failures']))
        rejected.append({'case':label,'failed_check':expected,'completed_checks':rr['checks'],'phase':rr['phase'],
                         'qualification':'preliminary condition only' if label!='late-series' else 'after both full composition orders; final Newton prefix mismatch; reciprocal, ODE and algebra checks not reached'})
    save('fresh-rejections.json',rejected)
    report['passed']=True;report['phase']='complete'
except Exception as e:
    report['failures']=[type(e).__name__+': '+str(e)]
finally:
    signal.alarm(0)
    manifest=json.loads((R/'original-manifest.json').read_text())
    changed=[p for p,d in manifest.items() if not (U/p).is_file() or hashlib.sha256((U/p).read_bytes()).hexdigest()!=d]
    save('preservation.json',{'original_files':len(manifest),'changed_or_missing':changed,'passed':not changed})
    if changed:report['passed']=False;report['failures'].append('original evidence changed')
    report.update(seconds=time.monotonic()-start,original_files=len(manifest),changed_or_missing=changed,bytes_before_report=sum(p.stat().st_size for p in R.rglob('*') if p.is_file()))
    if report['seconds']>180 or report['bytes_before_report']>134217728:
        report['passed']=False;report['failures'].append('resource bound exceeded')
    save('audit-report.json',report)
print(json.dumps(report));sys.exit(0 if report['passed'] else 1)
