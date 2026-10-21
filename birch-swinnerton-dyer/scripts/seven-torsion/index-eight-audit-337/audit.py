"""Replay-only audit of fixed actual S; no production or correction."""
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
            need(type(cert['i']) is int and type(e['j']) is int
                 and all(type(x) is str for x in e['quotient']+e['remainder']),
                 'exact_original_division_types')
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

report={'status':'STOP','failures':[],'phase':'initial_inventory'}
try:
    OLD=S/'index-four-order-two-335'
    original=load(OLD/'canonical-input-hashes.json')
    need(len(original)==1020,'entire_1020_production_input_inventory')
    names=set(original)
    names.update(str(p.relative_to(ROOT)) for p in OLD.rglob('*') if p.is_file())
    names.update(['lemmas/L087-conductor389-index-four-order-not-2-maximal.md',
        'drafts/literature/2026-10-19-index-four-order-two-critical-audit.md',
        'scripts/seven-torsion/index-four-audit-327/audit.py'])
    before={p:digest(ROOT/p) for p in sorted(names)}
    need(all(before[p]==h for p,h in original.items()),'every_historical_inventory_input_unchanged')
    save('canonical-input-hashes.json',before)
    manifest={}
    fixed=['basis.json']+['product-%02d.json'%i for i in range(48)]
    core=['input-basis.json','frobenius.json','radical-lattice.json','action-kernel.json',
          'numerator-lattice.json','decision.json']+['action-%02d.json'%i for i in range(48)]
    sources={name:name for name in fixed+core+['input_verify.py','verify.py']}
    for prefix in ['division-','action-division-']:
        for i in range(48):sources['fixed-'+prefix+'%02d.json'%i]=prefix+'%02d.json'%i
    for name in ['input-report.json','input-validation.json','verification-report.json',
                 'producer-report.json','stage-report.json','watchdog.json','final-bound.json']:
        sources['reference-'+name]=name
    for dest,srcname in sources.items():
        src=OLD/srcname;raw=src.read_bytes()
        with (D/dest).open('xb') as f:f.write(raw)
        h=digest(D/dest);need(h==before[str(src.relative_to(ROOT))],'exact_fixed_copy_'+dest)
        manifest[dest]={'source':str(src.relative_to(ROOT)),'sha256':h}
    for name in fixed:
        for dn in ['index-four-table-329','preserved-table-replay-331','preserved-table-audit-333']:
            p=str((S/dn/name).relative_to(ROOT))
            need(manifest[name]['sha256']==before[p],'full_49_fixed_provenance_'+dn+'_'+name)
    save('copy-manifest.json',manifest)
    codes={p.name:digest(p) for p in D.glob('*.py')};save('code-hashes.json',codes)
    report['phase']='fresh_complete_input_replay'
    iv=run('input_verify.py','input-report.json')
    required={'product_slots':110592,'product_identities':2304,'remainder_coefficients':218880,
              'transport_entries':18432,'inverse_products':8,'division_certificates':2304,'identity_actions':96,'index':4}
    for k,v in required.items():need(iv[k]==v,'complete_input_count_'+k)
    got=load(D/'basis.json');V=got['scaled_polynomials'];H=got['H']
    need(len(H)==49 and H[-1]==343 and len(V)==48
         and all(len(row)==48 and all(type(x) is int for x in row) for row in V),'entire_actual_V_and_H')
    table=[load(D/('product-%02d.json'%i)) for i in range(48)]
    # Check the original persisted evidence separately, never replace it by replay output.
    original_product_divisions=divisions('fixed-division-',V,H,table)
    fresh_product_divisions=divisions('division-',V,H,table)
    J=load(D/'radical-lattice.json')['basis']
    original_action_divisions=divisions('fixed-action-division-',V,H,table,J)
    save('persisted-input-checks.json',{'status':'PASS','failures':[],
        'original_product_divisions':original_product_divisions,
        'original_action_divisions':original_action_divisions,'fresh_product_divisions':fresh_product_divisions,
        'all_actual_dividends_reconstructed':True,'fixed_inputs_checked_before_kernel_replay':True})
    report['phase']='fresh_complete_kernel_action_replay'
    v=run('verify.py','verification-report.json')
    vr={'input_product_slots':110592,'product_slots':110592,'product_identities':2304,
        'remainder_coefficients':218880,'action_slots':110592,'frobenius_slots':13824,
        'frobenius_iterates':6,'exponent':64,'prime':2,'frobenius_rank':1,'radical_dimension':47,
        'action_rank':45,'action_kernel_dimension':3,'index':8,'identity_actions':96,
        'transport_entries':18432,'inverse_products':8,'action_division_certificates':2304,'row_operations':1591}
    for k,x in vr.items():need(v[k]==x,'complete_fresh_verifier_count_'+k)
    need(v['decision']=='NOT_2_MAXIMAL','fresh_strict_decision')
    fresh_action_divisions=divisions('action-division-',V,H,table,J)
    report['phase']='independent_full_certificates'
    independent=run('independent.py','independent-report.json')
    for k,x in {'frobenius_rank':1,'action_rank':45,'index':8,'radical_kernel_dimension':47,
                'action_kernel_dimension':3,'independent_preimages':2,'action_entries':110592,
                'full_strict_action_entries':2304}.items():need(independent[k]==x,'independent_complete_'+k)
    need(independent['all_load_bearing_certificates_reread'] is True,'complete_persisted_supplement_rereads')
    # Reread the complete fresh reports and division summary, rather than inheriting reference PASS.
    need(load(D/'input-report.json')==iv and load(D/'verification-report.json')==v
         and load(D/'independent-report.json')==independent,'complete_fresh_report_round_trips')
    e=load(D/'persisted-input-checks.json')
    need(e['original_product_divisions']==e['original_action_divisions']==2304
         and e['all_actual_dividends_reconstructed'] is True,'persisted_original_division_summary')
    report['phase']='final_preservation'
    after={p:digest(ROOT/p) for p in before}
    copies_after={name:digest(D/name) for name in manifest}
    codes_after={p.name:digest(p) for p in D.glob('*.py')}
    need(before==after and codes==codes_after
         and copies_after=={k:v['sha256'] for k,v in manifest.items()},'every_original_copy_and_code_preserved')
    save('audit-preservation.json',{'equal':True,'before':before,'after':after,
        'fixed_before':{k:v['sha256'] for k,v in manifest.items()},'fixed_after':copies_after,
        'code_before':codes,'code_after':codes_after})
    report.update(status='PASS',phase='complete',original_files=len(before),fixed_copies=len(manifest),
        table_copies=49,code_files=len(codes),original_product_divisions=original_product_divisions,
        original_action_divisions=original_action_divisions,fresh_product_divisions=fresh_product_divisions,
        fresh_action_divisions=fresh_action_divisions,replay_counts=vr,
        frobenius_rank=1,action_rank=45,index=8,decision='NOT_2_MAXIMAL',
        independent_preimages=2,all_certificates_reread=True)
except Exception as e:
    report.update(status='STOP',failures=[type(e).__name__+': '+str(e)])
report.update(seconds=time.monotonic()-START,required_seconds=180,required_bytes=134217728)
save('audit-report.json',report);print(json.dumps(report))
sys.exit(0 if report['status']=='PASS' else 1)
