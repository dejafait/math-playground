"""Exactly one combined production/replay stage, with final complete checks."""
from pathlib import Path
import hashlib, json, subprocess, sys, time
D=Path(__file__).resolve().parent
ROOT=D.parents[2]
START=time.monotonic()
def save(name,data):
    with (D/name).open('x') as f:
        json.dump(data,f,separators=(',',':'));f.write('\n')
def need(ok,label):
    if not ok:raise ArithmeticError(label)
def load(name):return json.loads((D/name).read_text())
report={'status':'INCOMPLETE','failures':[]}
try:
    for name in ('produce','verify'):
        with (D/(name+'.log')).open('x') as log:
            child=subprocess.run([sys.executable,'-B',str(D/(name+'.py'))],stdout=log,stderr=subprocess.STDOUT)
        need(child.returncode==0,name+'_exit_'+str(child.returncode))
        r=load('producer-report.json' if name=='produce' else 'verification-report.json')
        need(r['status']=='PASS' and not r['failures'],name+'_report')
        for actual,required in (('input_product_slots',110592),('action_slots',110592),('frobenius_slots',13824)):
            need(r[actual]==required,name+'_complete_'+actual)
    p=load('producer-report.json');v=load('verification-report.json');decision=load('decision.json')
    for key in ('decision','index','frobenius_rank','radical_dimension','action_rank','action_kernel_dimension'):
        need(p[key]==v[key],'independent_verdict_'+key)
    need(p['decision']==decision['decision'] and p['index']==decision['index'],'final_verdict')
    before=load('input-hashes.json')
    after={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in before}
    need(before==after,'every_original_final_hash')
    save('preservation-stage.json',{'before':before,'after':after,'equal':True})
    report.update(status='PASS',decision=decision['decision'],index=decision['index'],
                  frobenius_rank=p['frobenius_rank'],action_rank=p['action_rank'],
                  original_files=len(before),input_product_slots=v['input_product_slots'],
                  action_slots=v['action_slots'],frobenius_slots=v['frobenius_slots'])
except Exception as e:
    report.update(status='STOP',failures=[type(e).__name__+': '+str(e)])
finally:
    report.update(seconds=time.monotonic()-START,required_seconds=180,required_bytes=134217728)
    save('stage-report.json',report)
    print(json.dumps(report))
sys.exit(0 if report['status']=='PASS' else 1)
