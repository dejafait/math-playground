"""One fixed V audit. Historical stages are read, never executed."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,re,subprocess,sys,textwrap,time
sys.set_int_max_str_digits(0)
D=Path(__file__).resolve().parent; ROOT=D.parents[2]; S=D.parent; START=time.monotonic()
def read(p): return json.loads(p.read_text())
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def need(x,label):
    if not x: raise ArithmeticError(label)
def save(n,x):
    with (D/n).open('x') as f: json.dump(x,f,separators=(',',':')); f.write('\n')
def between(t,a,b):
    need(t.count(a)==1 and t.count(b)==1,'unique_source_boundaries')
    return t.split(a,1)[1].split(b,1)[0]
def replace(t,a,b):
    need(a in t,'source_adaptation_'+a[:70]); return t.replace(a,b)
report={'status':'STOP','phase':'initial_inventory','failures':[]}
try:
    OLD=S/'index-sixteen-order-two-351'; prior=S/'index-sixteen-table-audit-349'
    table_source=S/'index-sixteen-table-347'
    previous351=read(OLD/'canonical-input-hashes.json')
    need(len(previous351)==4817,'entire_4817_input_inventory')
    names=set(previous351)
    for folder in [OLD,prior,table_source]:
        names.update(str(p.relative_to(ROOT)) for p in folder.rglob('*') if p.is_file())
    names.update(['lemmas/L091-conductor389-index-sixteen-order-not-2-maximal.md',
        'drafts/literature/2026-10-19-index-sixteen-order-two-critical-audit.md',
        'drafts/2026-10-20-V-two-critical-audit-attempt.md',
        'scripts/seven-torsion/U-two-audit-345/independent.py',
        'scripts/seven-torsion/U-two-audit-345/run_once.py',
        'drafts/literature/2026-10-17-prime-local-overorder-quotient.md',
        'history/351-2026-10-19-index-sixteen-order-two-verdict.md'])
    before={n:digest(ROOT/n) for n in sorted(names)}
    step351_note='drafts/2026-10-19-index-sixteen-order-two-attempt.md'
    step351_prior='5d598e211e687adf8c65d3f69679f4a6c65548af454cc69c89f879f19d6342b9'
    step351_current='c5a6a333d57ff2c6eb561a9066e357dc3d22a6ec11f058e6777b59e6ef3a8e35'
    raw=(ROOT/step351_note).read_bytes(); marker=b'\n## Completed execution\n'
    need(raw.count(marker)==1 and hashlib.sha256(raw.split(marker)[0]).hexdigest()==step351_prior
         and previous351[step351_note]==step351_prior and before[step351_note]==step351_current,'exact_step351_document_append')
    need(all(before[n]==h for n,h in previous351.items() if n!=step351_note),'every_other_step351_input_unchanged')
    save('canonical-input-hashes.json',before)
    # Inspected definitions only. Storage redirection retains all arithmetic.
    source=(table_source/'stage.py').read_text()
    helpers=source.split('def prepare_sources():',1)[0]
    helpers=replace(helpers,'def divisions(prefix,basis,table,radical=None):',
        "def divisions(prefix,basis,table,radical=None,folder=None,action_prefix='old-U-'):\n    folder=(OLD if prefix.startswith(('original343-','original347-')) else D) if folder is None else folder")
    helpers=replace(helpers,"cert=read(D/(prefix+'%02d.json'%i))","cert=read(folder/(prefix+'%02d.json'%i))")
    helpers=replace(helpers,"A=read(D/('action-%02d.json'%i))","A=read(D/(action_prefix+'action-%02d.json'%i))")
    with (D/'replay-definitions.py').open('x') as f: f.write(helpers)
    exec(compile(helpers,str(D/'replay-definitions.py'),'exec'),globals())
    stage351=(OLD/'stage.py').read_text()
    previous=read(prior/'canonical-input-hashes.json')
    need(len(previous)==4001,'entire_step349_inventory')
    # Recheck the exact historical transition cases, not pathname exemptions.
    transition_block='    post349='+between(stage351,'    post349=',"    save('canonical-input-hashes.json',before)")
    exec(compile(textwrap.dedent(transition_block),'fixed-historical-transitions','exec'),globals())
    need(transition==read(OLD/'inventory-transition.json'),'entire_original351_transition_record')
    transition={'retained_step351_transition':transition,'only_new_document_change':step351_note,
                'prior':step351_prior,'current':step351_current,'no_pathname_exemptions':True}
    save('inventory-transition.json',transition)
    for folder,count in [(S/'index-eight-order-two-343',248),(S/'U-two-audit-345',447),
                         (table_source,449),(prior,643),(OLD,643)]:
        m=read(folder/'copy-manifest.json'); need(len(m)==count,'full_manifest_'+folder.name)
        for n,e in m.items():
            need(before[e['source']]==e['sha256']==before[str((folder/n).relative_to(ROOT))],
                 'every_original_copy_binding_'+folder.name+'_'+n)
    for folder,count in [(table_source,6),(prior,7),(OLD,8)]:
        codes=read(folder/'code-hashes.json'); need(len(codes)==count,'source_count_'+folder.name)
        need(all(digest(folder/n)==h for n,h in codes.items()),'all_executed_source_hashes_'+folder.name)
    manifest={}; in_place={}
    def copy(dest,src):
        key=str(src.relative_to(ROOT)); raw=src.read_bytes()
        need(hashlib.sha256(raw).hexdigest()==before[key],'before_copy_'+dest)
        with (D/dest).open('xb') as f: f.write(raw)
        need(digest(D/dest)==before[key],'exact_copy_'+dest)
        manifest[dest]={'source':key,'sha256':before[key]}
    for n in read(OLD/'copy-manifest.json'):
        if 'division-' in n:
            in_place[n]={'source':str((OLD/n).relative_to(ROOT)),'sha256':digest(OLD/n)}
        else: copy(n,OLD/n)
    core=['input-basis.json','frobenius.json','radical-lattice.json','action-kernel.json',
          'numerator-lattice.json','decision.json']+['action-%02d.json'%i for i in range(48)]
    for n in core+['verify.py']: copy(n,OLD/n)
    sfiles=['basis.json']+['product-%02d.json'%i for i in range(48)]
    ufiles=['u-basis.json']+['u-product-%02d.json'%i for i in range(48)]
    vfiles=['v-basis.json']+['v-product-%02d.json'%i for i in range(48)]
    for files,dirs in [(sfiles,['index-four-table-329','preserved-table-replay-331','preserved-table-audit-333',
          'index-four-order-two-335','index-eight-audit-337','index-eight-table-339','index-eight-table-audit-341']),
          (ufiles,['index-eight-table-339','index-eight-table-audit-341','index-eight-order-two-343','U-two-audit-345']),
          (vfiles,['index-sixteen-table-347','index-sixteen-table-audit-349'])]:
        for n in files:
            for dn in dirs: need(digest(S/dn/n)==manifest[n]['sha256'],'all_fixed_provenance_'+dn+'_'+n)
    save('copy-manifest.json',manifest); save('in-place-manifest.json',in_place)
    # Six-system replay is unchanged except fresh report filename and additionally
    # checking all of the original step-351 certificate, including its six solves.
    solve=(OLD/'independent.py').read_text()
    solve=replace(solve,'independent-report.json','solve-report.json')
    anchor="    for c in original349['systems'].values(): reread(c)\n"
    solve=replace(solve,anchor,anchor+
        "    original351=load(S/'index-sixteen-order-two-351/exact-lattice-certificate.json')\n"
        "    need(original351==reread_cert,'entire_original351_exact_certificate_agrees')\n"
        "    for c in original351['systems'].values(): reread(c)\n")
    # Ready independent factorization, kernel and integral-preimage mechanism.
    ind=(S/'U-two-audit-345/independent.py').read_text()
    ind=replace(ind,"OLD = D.parent/'index-eight-order-two-343'","OLD = D.parent/'index-sixteen-order-two-351'")
    common,main=ind.split('def main():',1)
    main=replace(main,'u-product-','v-product-')
    main=re.sub(r'\b44\b','43',main)
    main=replace(main,'[2]*43+[1]*4','[2]*43+[1]*5')
    main=replace(main,'==16','==32'); main=replace(main,'index=16','index=32')
    main=replace(main,'action_kernel_dimension=4','action_kernel_dimension=5')
    main=replace(main,'248*int(i==0)','496*int(i==0)')
    main=replace(main,'[V:U] = absolute determinant of U basis in V','[(I:I):V] = absolute determinant of V basis in (I:I)')
    main=replace(main,'independent_index_sixteen','independent_index_thirty_two')
    main=replace(main,'action_left_inverse_entries=101376,selected_inverse_entries=1936',
                      'action_left_inverse_entries=99072,selected_inverse_entries=1849')
    ind=common+'def main():'+main
    for n,body in [('solve_replay.py',solve),('independent.py',ind)]:
        compile(body,str(D/n),'exec')
        with (D/n).open('x') as f: f.write(body)
    code={p.name:digest(p) for p in D.glob('*.py')}; save('code-hashes.json',code)
    # This inspected block contains input verifiers/division replay only. Its
    # internal extraction executes the already read full V lattice comparison.
    block=between(stage351,"    report['phase']='complete_S_U_V_inputs_and_original_dividends'\n",
                           "    report['phase']='one_actual_V_radical_multiplier_test'\n")
    block=replace(block,"run('independent.py','independent-report.json')","run('solve_replay.py','solve-report.json')")
    report['phase']='complete_S_U_V_inputs_original_divisions_and_six_solves'
    exec(compile(textwrap.dedent(block),'fixed-input-replay-only','exec'),globals())
    report['phase']='all_step351_fixed_divisions'
    fixed351=sum([divisions('division-',sb,st,folder=OLD),
        divisions('u-division-',ub,ut,folder=OLD),divisions('v-division-',vb,vt,folder=OLD)])
    J=read(D/'radical-lattice.json')['basis']
    fixed351+=divisions('action-division-',vb,vt,J,folder=OLD,action_prefix='')
    need(fixed351==9216,'all_step351_fresh_and_action_divisions')
    report['phase']='complete_fixed_V_verdict_replay'
    verifier=run('verify.py','verification-report.json')
    expected={'input_product_slots':110592,'action_slots':110592,'frobenius_slots':13824,
        'frobenius_iterates':6,'exponent':64,'prime':2,'frobenius_rank':1,'radical_dimension':47,
        'action_rank':43,'action_kernel_dimension':5,'index':32,'action_division_certificates':2304,
        'row_operations':1452}
    for k,x in expected.items(): need(verifier[k]==x,'full_verdict_'+k)
    need(verifier['decision']=='NOT_2_MAXIMAL','fixed_strict_verdict')
    fresh_action=divisions('action-division-',vb,vt,J,action_prefix='')
    report['phase']='independent_full_rank_kernel_and_global_lattice'
    rankproof=run('independent.py','independent-report.json')
    for k,x in {'frobenius_rank':1,'action_rank':43,'index':32,'radical_kernel_dimension':47,
        'action_kernel_dimension':5,'independent_preimages':2,'action_entries':110592,
        'full_strict_action_entries':2304,'action_left_inverse_entries':99072,
        'selected_inverse_entries':1849,'all_load_bearing_certificates_reread':True}.items():
        need(rankproof[k]==x,'full_independent_'+k)
    for n,obj in [('input-report.json',iv),('u-verification-report.json',uv),('v-verification-report.json',vr),
        ('solve-report.json',independent),('independent-report.json',rankproof),('verification-report.json',verifier),
        ('input-validation.json',evidence),('complete-input-validation.json',complete_inputs)]:
        need(read(D/n)==obj,'entire_report_reread_'+n)
    for bn,tn,basis,table in [('basis.json','product-',sb,st),('u-basis.json','u-product-',ub,ut),
                            ('v-basis.json','v-product-',vb,vt)]:
        need(read(D/bn)==basis and all(read(D/(tn+'%02d.json'%i))==table[i] for i in range(48)),
             'whole_table_reread_'+bn)
    checks={'status':'PASS','failures':[],'original349_divisions':27648,'original351_divisions':fixed351,
        'fresh_divisions':fresh_s+fresh_u+fresh_v+fresh_action,'all_actual_dividends_checked':True,
        'six_original349_and_original351_solves_replayed':True,'old_U_and_actual_V_actions_separated':True}
    save('persisted-input-checks.json',checks); need(read(D/'persisted-input-checks.json')==checks,'all_checks_reread')
    report['phase']='final_preservation'
    after={n:digest(ROOT/n) for n in before}; copies={n:digest(D/n) for n in manifest}
    code_after={n:digest(D/n) for n in code}
    need(before==after and code==code_after and copies=={n:e['sha256'] for n,e in manifest.items()},
         'all_original_copy_source_preservation')
    preservation={'equal':True,'before':before,'after':after,'code_before':code,'code_after':code_after,
                  'fixed_before':{n:e['sha256'] for n,e in manifest.items()},'fixed_after':copies}
    save('audit-preservation.json',preservation)
    for n,obj in [('audit-preservation.json',preservation),('copy-manifest.json',manifest),
        ('canonical-input-hashes.json',before),('code-hashes.json',code),('inventory-transition.json',transition),
        ('in-place-manifest.json',in_place)]: need(read(D/n)==obj,'entire_final_reread_'+n)
    report.update(status='PASS',phase='complete',decision='NOT_2_MAXIMAL',scale=496,index=32,
        frobenius_rank=1,action_rank=43,radical_kernel_dimension=47,action_kernel_dimension=5,
        original_divisions=36864,fresh_divisions=9216,original_files=len(before),fixed_copies=len(manifest),
        in_place_files=len(in_place),source_files=len(code),independent_preimages=2,
        all_load_bearing_certificates_reread=True,six_original349_and_original351_solves_replayed=True)
except Exception as exc:
    report.update(status='STOP',failures=[type(exc).__name__+': '+str(exc)])
report.update(seconds=time.monotonic()-START,required_seconds=180,required_bytes=134217728)
save('audit-report.json',report); print(json.dumps(report)); sys.exit(0 if report['status']=='PASS' else 1)
