"""One complete replay, separate lattice check, full persisted divisions."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,subprocess,sys,time
sys.set_int_max_str_digits(0)
D=Path(__file__).resolve().parent; ROOT=D.parents[2]; S=D.parent
OLD=S/'index-four-table-329'; PREV=S/'preserved-table-replay-331'
def load(p):return json.loads(p.read_text())
def need(ok,label):
    if not ok:raise ArithmeticError(label)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):
    with (D/name).open('x') as f:json.dump(obj,f,separators=(',',':'));f.write('\n')
report={'status':'STOP','failures':[]}
try:
    names=set(load(PREV/'canonical-input-hashes.json'))
    names.update(str(p.relative_to(ROOT)) for parent in [OLD,PREV] for p in parent.rglob('*') if p.is_file())
    names.update(['lemmas/L086-conductor389-index-four-multiplier-order-table.md','drafts/literature/2026-10-18-preserved-index-four-table-critical-audit.md','ATTEMPTS/041-first-overorder-integral-power-witness-cap.md','ATTEMPTS/042-changed-order-audit-approval-repetition.md','ATTEMPTS/044-index-four-table-verifier-integer-zero.md'])
    before={p:digest(ROOT/p) for p in sorted(names)}
    need(all(before[p]==h for p,h in load(PREV/'canonical-input-hashes.json').items()),'unchanged_historical_canonical_inputs')
    need(digest(D/'verify.py')==before[str((PREV/'verify.py').relative_to(ROOT))]==load(PREV/'fresh-code-hashes.json')['verify.py'],'byte_unchanged_repaired_verifier')
    save('canonical-input-hashes.json',before)
    codes={p.name:digest(p) for p in D.glob('*.py')};save('code-hashes.json',codes)
    copies={}
    for name in ['basis.json']+['product-%02d.json'%i for i in range(48)]:
        raw=(OLD/name).read_bytes()
        with (D/name).open('xb') as f:f.write(raw)
        need(digest(D/name)==before[str((OLD/name).relative_to(ROOT))],'fixed_copy_'+name)
        need(digest(D/name)==before[str((PREV/name).relative_to(ROOT))],'same_step331_fixed_copy_'+name)
        copies[name]={'source':str((OLD/name).relative_to(ROOT)),'sha256':digest(D/name)}
    save('copy-manifest.json',copies)
    for script in ['verify.py','independent.py']:
        with (D/(script+'.log')).open('x') as log:
            rc=subprocess.run([sys.executable,'-B',str(D/script)],stdout=log,stderr=subprocess.STDOUT).returncode
        need(rc==0,'first_failure_'+script+'_exit_'+str(rc))
    v=load(D/'verification-report.json'); ind=load(D/'independent-report.json')
    required={'status':'PASS','failures':[],'product_slots':110592,'product_identities':2304,'remainder_coefficients':218880,'transport_entries':18432,'inverse_products':8,'division_certificates':2304,'identity_actions':96,'index':4}
    for k,x in required.items():need(v[k]==x,'replay_count_'+k)
    need(ind['status']=='PASS' and not ind['failures'] and ind['complete_certificate_reread'],'independent_complete')
    b=load(D/'basis.json'); H=b['H']; V=b['scaled_polynomials']; count=0
    for i in range(48):
        row=load(D/('product-%02d.json'%i)); cert=load(D/('division-%02d.json'%i))
        need(cert['i']==i and len(cert['products'])==48,'all_persisted_divisions')
        for j,e in enumerate(cert['products']):
            dividend=[0]*95
            for r,x in enumerate(V[i]):
                if x:
                    for s,y in enumerate(V[j]):
                        if y:dividend[r+s]+=x*y
            for k,z in enumerate(row[j]):
                if z:
                    for r,x in enumerate(V[k]):
                        if x:dividend[r]-=124*z*x
            q=list(map(F,e['quotient'])); rem=list(map(F,e['remainder']))
            need(e['j']==j and len(q)==47 and len(rem)==95 and not any(rem),'full_persisted_shapes_remainders')
            need(len(e['dividend'])==95 and all(type(x) is int for x in e['dividend']) and dividend==e['dividend'],'actual_product_dividend')
            product=rem[:]
            for r,x in enumerate(q):
                if x:
                    for s,y in enumerate(H):
                        if y:product[r+s]+=x*y
            need(product==dividend,'full_persisted_division_identity')
            count+=1
    need(count==2304,'complete_persisted_count')
    after={p:digest(ROOT/p) for p in before}
    copies_after={name:digest(D/name) for name in copies}
    codes_after={p.name:digest(p) for p in D.glob('*.py')}
    need(after==before and codes==codes_after and copies_after=={k:v['sha256'] for k,v in copies.items()},'final_full_preservation')
    save('audit-preservation.json',{'equal':True,'before':before,'after':after,'fixed_after':copies_after,'code_before':codes,'code_after':codes_after})
    report.update(status='PASS',original_files=len(before),fixed_copies=len(copies),code_files=len(codes),persisted_divisions=count,**{k:v[k] for k in required if k not in ['status','failures']},independent=ind)
except Exception as e:report['failures']=[type(e).__name__+': '+str(e)]
save('audit-report.json',report);print(json.dumps(report))
sys.exit(0 if report['status']=='PASS' else 1)
