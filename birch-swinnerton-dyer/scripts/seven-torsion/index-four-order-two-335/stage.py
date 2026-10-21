"""One actual-S test: input validation, production, independent full replay."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,subprocess,sys,time
sys.set_int_max_str_digits(0)
D=Path(__file__).resolve().parent; ROOT=D.parents[2]; S=D.parent
START=time.monotonic()
def load(p):return json.loads(p.read_text())
def need(ok,label):
    if not ok:raise ArithmeticError(label)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):
    with (D/name).open('x') as f:json.dump(obj,f,separators=(',',':'));f.write('\n')
def transpose(a):return [list(r) for r in zip(*a)]
def mul(a,b):
    cols=list(zip(*b))
    return [[sum(x*y for x,y in zip(r,c) if x and y) for c in cols] for r in a]
def run(name,reportname):
    with (D/(name+'.log')).open('x') as log:
        rc=subprocess.run([sys.executable,'-B',str(D/name)],stdout=log,stderr=subprocess.STDOUT).returncode
    need(rc==0,'first_failure_'+name+'_exit_'+str(rc))
    report=load(D/reportname)
    need(report['status']=='PASS' and not report['failures'],'complete_'+reportname)
    return report

def divisions(prefix,V,H,table,radical=None):
    count=0
    if radical is not None:
        J=radical;W=transpose(mul(transpose(V),J))
    for i in range(48):
        cert=load(D/(prefix+'%02d.json'%i))
        need(cert['i']==i and len(cert['products'])==48,'complete_persisted_division_row')
        if radical is not None:
            A=load(D/('action-%02d.json'%i)); JA=mul(J,A)
            need(JA==mul(transpose(table[i]),J),'persisted_action_coordinate_identity')
            expansion=transpose(mul(transpose(V),JA))
        for j,e in enumerate(cert['products']):
            dividend=[0]*95;right=V[j] if radical is None else W[j]
            for r,x in enumerate(V[i]):
                if x:
                    for s,y in enumerate(right):
                        if y:dividend[r+s]+=x*y
            if radical is None:
                for k,z in enumerate(table[i][j]):
                    if z:
                        for r,x in enumerate(V[k]):
                            if x:dividend[r]-=124*z*x
            else:
                for r,x in enumerate(expansion[j]):dividend[r]-=124*x
            q=list(map(F,e['quotient'])); rem=list(map(F,e['remainder']))
            need(e['j']==j and len(q)==47 and len(rem)==95 and not any(rem),'full_persisted_shapes_and_zero_remainders')
            need(len(e['dividend'])==95 and all(type(x) is int for x in e['dividend'])
                 and dividend==e['dividend'],'every_actual_dividend_coefficient')
            product=rem[:]
            for r,x in enumerate(q):
                if x:
                    for s,y in enumerate(H):
                        if y:product[r+s]+=x*y
            need(product==dividend,'complete_persisted_original_H_division')
            count+=1
    need(count==2304,'complete_persisted_division_count')
    return count

report={'status':'STOP','failures':[]}
try:
    names=set(load(S/'preserved-table-audit-333/canonical-input-hashes.json'))
    for dn in ['index-two-order-two-325','index-four-table-329','preserved-table-replay-331','preserved-table-audit-333']:
        names.update(str(p.relative_to(ROOT)) for p in (S/dn).rglob('*') if p.is_file())
    names.update(['lemmas/L086-conductor389-index-four-multiplier-order-table.md',
                  'drafts/literature/2026-10-19-index-four-order-prime-two-test.md',
                  'history/329-2026-10-18-index-four-table-verifier-stop.md',
                  'history/331-2026-10-18-preserved-index-four-table-replay.md',
                  'history/333-2026-10-19-preserved-index-four-table-critical-audit.md',
                  'ATTEMPTS/041-first-overorder-integral-power-witness-cap.md',
                  'ATTEMPTS/042-changed-order-audit-approval-repetition.md',
                  'ATTEMPTS/044-index-four-table-verifier-integer-zero.md'])
    before={p:digest(ROOT/p) for p in sorted(names)}
    save('canonical-input-hashes.json',before)
    codes={p.name:digest(p) for p in D.glob('*.py')};save('code-hashes.json',codes)
    copies={}
    for name in ['basis.json']+['product-%02d.json'%i for i in range(48)]:
        src=S/'index-four-table-329'/name;raw=src.read_bytes()
        with (D/name).open('xb') as f:f.write(raw)
        h=digest(D/name)
        for dn in ['index-four-table-329','preserved-table-replay-331','preserved-table-audit-333']:
            need(h==before[str((S/dn/name).relative_to(ROOT))],'fixed_full_table_copy_'+dn+'_'+name)
        copies[name]={'source':str(src.relative_to(ROOT)),'sha256':h}
    save('copy-manifest.json',copies)
    iv=run('input_verify.py','input-report.json')
    required={'product_slots':110592,'product_identities':2304,'remainder_coefficients':218880,
              'transport_entries':18432,'inverse_products':8,'division_certificates':2304,'identity_actions':96,'index':4}
    for k,v in required.items():need(iv[k]==v,'input_full_count_'+k)
    got=load(D/'basis.json');V=got['scaled_polynomials'];H=got['H']
    table=[load(D/('product-%02d.json'%i)) for i in range(48)]
    persisted_inputs=divisions('division-',V,H,table)
    save('input-validation.json',{'status':'PASS','failures':[],'all_before_modular_production':True,
        'persisted_actual_divisions':persisted_inputs,**required})
    p=run('produce.py','producer-report.json')
    v=run('verify.py','verification-report.json')
    for r,label in [(p,'producer'),(v,'independent')]:
        for k,x in {'input_product_slots':110592,'action_slots':110592,'frobenius_slots':13824,
                    'frobenius_iterates':6,'exponent':64,'prime':2}.items():need(r[k]==x,label+'_complete_'+k)
    for k in ['decision','index','frobenius_rank','radical_dimension','action_rank','action_kernel_dimension']:
        need(p[k]==v[k],'independent_full_result_'+k)
    need(v['action_division_certificates']==2304,'complete_action_division_certificates')
    persisted_actions=divisions('action-division-',V,H,table,load(D/'radical-lattice.json')['basis'])
    dc=load(D/'decision.json')
    need(dc['decision']==v['decision'] and dc['index']==v['index'],'complete_final_verdict_agreement')
    after={p:digest(ROOT/p) for p in before}
    copies_after={name:digest(D/name) for name in copies}
    codes_after={p.name:digest(p) for p in D.glob('*.py')}
    need(before==after and codes==codes_after and copies_after=={k:v['sha256'] for k,v in copies.items()},'every_original_fixed_copy_and_code_preserved')
    save('preservation-stage.json',{'equal':True,'before':before,'after':after,
         'fixed_before':{k:v['sha256'] for k,v in copies.items()},'fixed_after':copies_after,
         'code_before':codes,'code_after':codes_after})
    report.update(status='PASS',decision=dc['decision'],index=dc['index'],
        frobenius_rank=v['frobenius_rank'],radical_dimension=v['radical_dimension'],
        action_rank=v['action_rank'],action_kernel_dimension=v['action_kernel_dimension'],
        input_product_slots=110592,action_slots=110592,frobenius_slots=13824,
        row_operations=v['row_operations'],persisted_input_divisions=persisted_inputs,
        persisted_action_divisions=persisted_actions,original_files=len(before),fixed_copies=len(copies),code_files=len(codes))
except Exception as e:
    report.update(status='STOP',failures=[type(e).__name__+': '+str(e)])
report.update(seconds=time.monotonic()-START,required_seconds=180,required_bytes=134217728)
save('stage-report.json',report);print(json.dumps(report))
sys.exit(0 if report['status']=='PASS' else 1)
