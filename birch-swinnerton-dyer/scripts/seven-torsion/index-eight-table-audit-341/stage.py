"""Inclusive setup, full S input validation, one U production/replay, preservation."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,subprocess,sys,time
sys.set_int_max_str_digits(0)
D=Path(__file__).resolve().parent; ROOT=D.parents[2]; S=D.parent; START=time.monotonic()
def read(p):return json.loads(p.read_text())
def need(x,s):
    if not x:raise ArithmeticError(s)
def save(n,x):
    with (D/n).open('x') as f:json.dump(x,f,separators=(',',':'));f.write('\n')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(name,report):
    with (D/(name+'.log')).open('x') as log:
        rc=subprocess.run([sys.executable,'-B',str(D/name)],stdout=log,stderr=subprocess.STDOUT).returncode
    need(rc==0,'first_failure_'+name+'_exit_'+str(rc))
    result=read(D/report);need(result['status']=='PASS' and not result['failures'],'full_'+report)
    return result
def divisions(prefix,basis,products):
    V=basis['scaled_polynomials'];H=basis['H'];scale=basis['scale'];count=0
    for i in range(48):
        cert=read(D/(prefix+'%02d.json'%i))
        need(type(cert['i']) is int and cert['i']==i and len(cert['products'])==48,'full_division_row')
        for j,e in enumerate(cert['products']):
            need(type(e['j']) is int and e['j']==j and len(e['dividend'])==95
                and all(type(x) is int for x in e['dividend']) and len(e['quotient'])==47
                and len(e['remainder'])==95 and all(type(x) is str for x in e['quotient']+e['remainder']),
                'complete_exact_division_types')
            actual=[0]*95
            # Independently expand from the actual basis and product row, not saved dividend labels.
            for a in range(48):
                for b in range(48):
                    if V[i][a] and V[j][b]:actual[a+b]+=V[i][a]*V[j][b]
            for k,c in enumerate(products[i][j]):
                if c:
                    for a,x in enumerate(V[k]):
                        if x:actual[a]-=scale*c*x
            need(actual==e['dividend'],'all_actual_dividend_positions_'+str((prefix,i,j)))
            q=list(map(F,e['quotient']));rem=list(map(F,e['remainder']))
            need(not any(rem),'all_remainder_positions_zero')
            reconstructed=rem[:]
            for a,x in enumerate(q):
                if x:
                    for b,h in enumerate(H):
                        if h:reconstructed[a+b]+=x*h
            need(actual==reconstructed,'whole_persisted_H_division_'+str((prefix,i,j)));count+=1
    need(count==2304,'all_persisted_divisions');return count
report={'status':'STOP','failures':[],'phase':'setup'}
try:
    prior=S/'index-eight-table-339'
    prior_hashes=read(prior/'canonical-input-hashes.json'); names=set(prior_hashes)
    names.update(str(p.relative_to(ROOT)) for p in prior.rglob('*') if p.is_file())
    names.update(['lemmas/L088-conductor389-index-eight-multiplier-order-table.md',
        'drafts/literature/2026-10-19-index-eight-table-critical-audit.md',
        'history/339-2026-10-19-index-eight-multiplier-table.md',
        'history/340-2026-10-19-index-eight-table-audit-scope.md',
        'scripts/seven-torsion/preserved-table-audit-333/independent.py',
        'ATTEMPTS/041-first-overorder-integral-power-witness-cap.md',
        'ATTEMPTS/042-changed-order-audit-approval-repetition.md',
        'ATTEMPTS/044-index-four-table-verifier-integer-zero.md'])
    before={n:digest(ROOT/n) for n in sorted(names)}
    need(all(before[n]==h for n,h in prior_hashes.items()),'all_step339_canonical_inputs_unchanged')
    transition=read(prior/'inventory-transition.json')
    lname='lemmas/L087-conductor389-index-four-order-not-2-maximal.md'
    prevhashes=read(S/'index-eight-audit-337/canonical-input-hashes.json')
    need(transition['only_permitted_post337_document_change']==lname
         and transition['prior']==prevhashes[lname] and transition['current']==before[lname],
         'retain_only_explicit_historical_L087_transition')
    need(all(before[n]==h for n,h in prevhashes.items() if n!=lname),'all_other_step337_inputs_unchanged')
    save('canonical-input-hashes.json',before)
    manifest={}
    def copy(dest,src):
        raw=src.read_bytes(); expected=before[str(src.relative_to(ROOT))]
        need(hashlib.sha256(raw).hexdigest()==expected,'source_before_copy_'+dest)
        with (D/dest).open('xb') as f:f.write(raw)
        need(digest(D/dest)==expected,'full_copy_'+dest)
        manifest[dest]={'source':str(src.relative_to(ROOT)),'sha256':expected}
    for name in ['basis.json']+['product-%02d.json'%i for i in range(48)]:
        copy(name,prior/name)
        for dn in ['index-four-table-329','preserved-table-replay-331','preserved-table-audit-333',
                   'index-four-order-two-335','index-eight-audit-337']:
            need(digest(S/dn/name)==manifest[name]['sha256'],'all_fixed_S_provenance_'+dn+'_'+name)
    for name in ['u-basis.json']+['u-product-%02d.json'%i for i in range(48)]:copy(name,prior/name)
    for i in range(48):
        name='division-%02d.json'%i
        copy('fixed-original-S-'+name,prior/('fixed-'+name))
        for path in [S/'index-four-order-two-335'/name,S/'index-eight-audit-337'/('fixed-'+name)]:
            need(digest(path)==manifest['fixed-original-S-'+name]['sha256'],'original_S_division_provenance')
        copy('fixed-replayed-S-'+name,prior/name)
        copy('fixed-U-'+name,prior/('u-'+name))
    for name in ['decision-335.json','decision-337.json','fixed-independent-multiplier.json',
                 'fixed-numerator-lattice.json','input_verify.py','verify_u.py']:copy(name,prior/name)
    for name in ['stage-report.json','input-report.json','u-verification-report.json',
                 'producer-report.json','watchdog.json','final-bound.json']:copy('reference-'+name,prior/name)
    save('copy-manifest.json',manifest)
    code={p.name:digest(p) for p in D.glob('*.py')};save('code-hashes.json',code)
    report['phase']='complete_fresh_S_replay'
    iv=run('input_verify.py','input-report.json')
    for k,x in {'product_slots':110592,'product_identities':2304,'remainder_coefficients':218880,
        'transport_entries':18432,'inverse_products':8,'division_certificates':2304,
        'identity_actions':96,'index':4}.items():need(iv[k]==x,'complete_S_'+k)
    basis=read(D/'basis.json'); table=[read(D/('product-%02d.json'%i)) for i in range(48)]
    counts={}
    for prefix in ['fixed-original-S-division-','fixed-replayed-S-division-','division-']:
        counts[prefix]=divisions(prefix,basis,table)
    report['phase']='complete_fresh_U_replay'
    uv=run('verify_u.py','u-verification-report.json')
    for k,x in {'product_slots':110592,'product_identities':2304,'remainder_coefficients':218880,
        'transport_entries':18432,'inverse_products':8,'division_certificates':2304,
        'identity_actions':96,'index':8,'scale':248,'basis_elements':48}.items():need(uv[k]==x,'complete_U_'+k)
    ub=read(D/'u-basis.json'); ut=[read(D/('u-product-%02d.json'%i)) for i in range(48)]
    for prefix in ['fixed-U-division-','u-division-']:counts[prefix]=divisions(prefix,ub,ut)
    report['phase']='independent_full_exact_solves'
    ind=run('independent.py','independent-report.json')
    for k,x in {'elimination_systems':6,'transport_entries':13824,'inclusion_entries':4608,
        'scaled_slots':9216,'index':8,'identity_entries':96,'solved_identity_actions':192,
        'complete_certificate_reread':True}.items():need(ind[k]==x,'independent_'+k)
    need(read(D/'input-report.json')==iv and read(D/'u-verification-report.json')==uv
         and read(D/'independent-report.json')==ind,'all_full_report_rereads')
    need(read(D/'basis.json')==basis and read(D/'u-basis.json')==ub
         and all(read(D/('product-%02d.json'%i))==table[i]
                 and read(D/('u-product-%02d.json'%i))==ut[i] for i in range(48)),
         'all_fixed_basis_table_rereads')
    report['phase']='final_preservation'
    after={n:digest(ROOT/n) for n in before};copies={n:digest(D/n) for n in manifest}
    code_after={p.name:digest(p) for p in D.glob('*.py')}
    need(before==after and code==code_after and copies=={n:x['sha256'] for n,x in manifest.items()},
         'all_original_copy_code_preservation')
    preservation={'equal':True,'before':before,'after':after,'code_before':code,'code_after':code_after,
                  'fixed_before':{n:x['sha256'] for n,x in manifest.items()},'fixed_after':copies}
    save('audit-preservation.json',preservation)
    need(read(D/'audit-preservation.json')==preservation and read(D/'copy-manifest.json')==manifest
         and read(D/'canonical-input-hashes.json')==before and read(D/'code-hashes.json')==code,
         'complete_preservation_roundtrips')
    report.update(status='PASS',phase='complete',original_files=len(before),fixed_copies=len(manifest),
         code_files=len(code),actual_divisions=counts,original_actual_divisions=6912,
         fresh_actual_divisions=4608,S_product_slots=110592,U_product_slots=110592,
         S_product_identities=2304,U_product_identities=2304,independent=ind,
         historical_inventory_transition=transition,all_actual_dividends_checked=True)
except Exception as e:report.update(status='STOP',failures=[type(e).__name__+': '+str(e)])
report.update(seconds=time.monotonic()-START,required_seconds=180,required_bytes=134217728)
save('audit-report.json',report);need(read(D/'audit-report.json')==report,'full_final_report_reread')
print(json.dumps(report));sys.exit(0 if report['status']=='PASS' else 1)
