"""Single combined table construction/replay, complete persisted-division check."""
from pathlib import Path
from fractions import Fraction
import hashlib, json, subprocess, sys, time
D=Path(__file__).resolve().parent; ROOT=D.parents[2]
sys.set_int_max_str_digits(0)
START=time.monotonic()
def save(name,data):
    with (D/name).open('x') as f: json.dump(data,f,separators=(',',':')); f.write('\n')
def need(ok,label):
    if not ok: raise ArithmeticError(label)
def load(name): return json.loads((D/name).read_text())
report={'status':'INCOMPLETE','failures':[]}
try:
    code={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in D.glob('*.py')}
    save('code-hashes.json',code)
    for name in ('produce','verify'):
        with (D/(name+'.log')).open('x') as log:
            child=subprocess.run([sys.executable,'-B',str(D/(name+'.py'))],stdout=log,stderr=subprocess.STDOUT)
        need(child.returncode==0,name+'_exit_'+str(child.returncode))
        r=load('producer-report.json' if name=='produce' else 'verification-report.json')
        need(r['status']=='PASS' and not r['failures'],name+'_report')
        need(r['product_slots']==110592 and r['identity_actions']==96 and r['index']==4,name+'_complete_counts')
    v=load('verification-report.json')
    for key,value in (('product_identities',2304),('remainder_coefficients',218880),
                      ('transport_entries',18432),('inverse_products',8),('division_certificates',2304)):
        need(v[key]==value,'verifier_complete_'+key)
    basis=load('basis.json'); H=basis['H']; persisted=0
    for i in range(48):
        certificate=load('division-%02d.json'%i)
        need(certificate['i']==i and len(certificate['products'])==48,'full_division_row')
        for j,entry in enumerate(certificate['products']):
            q=list(map(Fraction,entry['quotient'])); rem=list(map(Fraction,entry['remainder']))
            need(entry['j']==j and len(q)==47 and len(rem)==95 and not any(rem),'all_persisted_zero_remainders')
            dividend=entry['dividend']; need(len(dividend)==95 and all(type(x) is int for x in dividend),'complete_dividend')
            product=[0]*95
            for a,x in enumerate(q):
                if x:
                    for b,y in enumerate(H):
                        if y: product[a+b]+=x*y
            need(product==dividend,'persisted_full_H_quotient_'+str((i,j)))
            persisted+=1
    before=load('input-hashes.json')
    after={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in before}
    need(before==after,'every_original_final_hash')
    need(code=={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in D.glob('*.py')},'all_new_code_preserved')
    save('preservation-stage.json',{'before':before,'after':after,'equal':True,'new_code_equal':True})
    report.update(status='PASS',index=4,product_slots=v['product_slots'],
                  product_identities=v['product_identities'],remainder_coefficients=v['remainder_coefficients'],
                  persisted_divisions=persisted,original_files=len(before),identity_actions=96,
                  transport_entries=v['transport_entries'],inverse_products=v['inverse_products'])
except Exception as e:
    report.update(status='STOP',failures=[type(e).__name__+': '+str(e)])
finally:
    report.update(seconds=time.monotonic()-START,required_seconds=180,required_bytes=134217728)
    save('stage-report.json',report); print(json.dumps(report))
sys.exit(0 if report['status']=='PASS' else 1)
