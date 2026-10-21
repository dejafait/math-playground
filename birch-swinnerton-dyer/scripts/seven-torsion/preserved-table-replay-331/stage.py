"""Copy fixed untrusted bytes, replay once, verify persisted evidence."""
from pathlib import Path
from fractions import Fraction
import hashlib, json, subprocess, sys, time
D=Path(__file__).resolve().parent; ROOT=D.parents[2]; SRC=D.parent
OLD=SRC/'index-four-table-329'; START=time.monotonic()
sys.set_int_max_str_digits(0)
def save(name,data):
    with (D/name).open('x') as f:json.dump(data,f,separators=(',',':'));f.write('\n')
def need(ok,label):
    if not ok: raise ArithmeticError(label)
def load(p):return json.loads(p.read_text())
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
report={'status':'INCOMPLETE','failures':[]}
try:
    # This is a new inventory; the historical step-329 inventory is immutable.
    canonical_names=list(load(OLD/'input-hashes.json'))
    canonical_names.append('drafts/literature/2026-10-18-preserved-index-four-table-replay.md')
    canonical={name:digest(ROOT/name) for name in sorted(set(canonical_names))}
    need(all(canonical[name]==h for name,h in load(OLD/'input-hashes.json').items()),'historical_canonical_inputs_unchanged')
    historical_paths=sorted(p for p in OLD.rglob('*') if p.is_file())
    historical_paths += [ROOT/'scripts/seven-torsion/index-four-table-stop-329/preservation.json',
                         ROOT/'ATTEMPTS/044-index-four-table-verifier-integer-zero.md',
                         ROOT/'drafts/2026-10-18-index-four-table-attempt.md']
    historical={str(p.relative_to(ROOT)):digest(p) for p in historical_paths}
    code={p.name:digest(p) for p in D.glob('*.py')}
    save('canonical-input-hashes.json',canonical)
    save('historical-source-hashes.json',historical)
    save('fresh-code-hashes.json',code)
    copies={}; manifest=[]
    for name in ['basis.json']+['product-%02d.json'%i for i in range(48)]:
        p=OLD/name; h=historical[str(p.relative_to(ROOT))]
        raw=p.read_bytes();need(hashlib.sha256(raw).hexdigest()==h,'source_before_copy_'+name)
        with (D/name).open('xb') as f:f.write(raw)
        need(digest(D/name)==h,'fixed_copy_'+name)
        copies[name]=h
        manifest.append({'source':str(p.relative_to(ROOT)),'copy':name,'sha256':h,
                         'classification':'preserved_untrusted_table_input'})
    save('copy-manifest.json',{'canonical_inventory':'canonical-input-hashes.json',
        'historical_inventory':'historical-source-hashes.json','fresh_code_inventory':'fresh-code-hashes.json',
        'fixed_inputs':manifest})
    with (D/'verify.log').open('x') as log:
        result=subprocess.run([sys.executable,'-B',str(D/'verify.py')],stdout=log,stderr=subprocess.STDOUT)
    need(result.returncode==0,'verify_exit_'+str(result.returncode))
    v=load(D/'verification-report.json')
    need(v['status']=='PASS' and not v['failures'],'verifier_PASS')
    for key,value in (('product_slots',110592),('product_identities',2304),('remainder_coefficients',218880),
                      ('transport_entries',18432),('inverse_products',8),('division_certificates',2304),
                      ('identity_actions',96),('index',4)):
        need(v[key]==value,'complete_'+key)
    H=load(D/'basis.json')['H']; persisted=0
    for i in range(48):
        certificate=load(D/('division-%02d.json'%i))
        need(certificate['i']==i and len(certificate['products'])==48,'full_division_row')
        for j,entry in enumerate(certificate['products']):
            q=list(map(Fraction,entry['quotient'])); rem=list(map(Fraction,entry['remainder']))
            need(entry['j']==j and len(q)==47 and len(rem)==95 and not any(rem),'complete_zero_remainder')
            dividend=entry['dividend']
            need(len(dividend)==95 and all(type(x) is int for x in dividend),'complete_integer_dividend')
            product=[0]*95
            for a,x in enumerate(q):
                if x:
                    for b,y in enumerate(H):
                        if y:product[a+b]+=x*y
            need(product==dividend,'persisted_H_quotient_'+str((i,j)))
            persisted+=1
    after={name:digest(ROOT/name) for name in canonical}
    hist_after={name:digest(ROOT/name) for name in historical}
    copies_after={name:digest(D/name) for name in copies}
    code_after={p.name:digest(p) for p in D.glob('*.py')}
    need(after==canonical,'canonical_final_preservation')
    need(hist_after==historical,'historical_final_preservation')
    need(copies_after==copies,'fixed_copy_final_preservation')
    need(code_after==code,'fresh_code_final_preservation')
    save('preservation-stage.json',{'canonical_before':canonical,'canonical_after':after,
        'historical_before':historical,'historical_after':hist_after,'fixed_before':copies,
        'fixed_after':copies_after,'code_before':code,'code_after':code_after,'equal':True})
    report.update(status='PASS',persisted_divisions=persisted,canonical_files=len(canonical),
        historical_files=len(historical),fixed_copies=len(copies),fresh_code_files=len(code),
        **{k:v[k] for k in ('product_slots','product_identities','remainder_coefficients',
                            'transport_entries','inverse_products','identity_actions','index')})
except Exception as e:report.update(status='STOP',failures=[type(e).__name__+': '+str(e)])
finally:
    report.update(seconds=time.monotonic()-START,required_seconds=180,required_bytes=134217728)
    save('stage-report.json',report);print(json.dumps(report))
sys.exit(0 if report['status']=='PASS' else 1)
