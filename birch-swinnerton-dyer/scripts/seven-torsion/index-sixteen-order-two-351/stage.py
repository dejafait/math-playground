"""One entire actual-V test, with complete fixed input replay before production."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, subprocess, sys, time, textwrap
sys.set_int_max_str_digits(0)
D=Path(__file__).resolve().parent; ROOT=D.parents[2]; S=D.parent; START=time.monotonic()
def save(n,x):
    with (D/n).open('x') as f: json.dump(x,f,separators=(',',':')); f.write('\n')
report={'status':'STOP','failures':[],'phase':'source_helpers'}
try:
    prior=S/'index-sixteen-table-audit-349'; table_source=S/'index-sixteen-table-347'
    source=(table_source/'stage.py').read_text()
    helpers=source.split('def prepare_sources():')[0]
    # Definitions only, never a historical stage, producer or preparation function.
    need_marker="def divisions(prefix,basis,table,radical=None):"
    if helpers.count(need_marker)!=1: raise ValueError('exact_division_helper_boundary')
    helpers=helpers.replace(need_marker,"def divisions(prefix,basis,table,radical=None,folder=None,action_prefix='old-U-'):\n    folder=D if folder is None else folder")
    helpers=helpers.replace("cert=read(D/(prefix+'%02d.json'%i))", "cert=read(folder/(prefix+'%02d.json'%i))")
    helpers=helpers.replace("A=read(D/('action-%02d.json'%i))", "A=read(D/(action_prefix+'action-%02d.json'%i))")
    exec(compile(helpers,str(table_source/'stage.py')+':definitions','exec'),globals())
    report['phase']='initial_inventory_and_exact_transitions'
    previous=read(prior/'canonical-input-hashes.json'); need(len(previous)==4001,'entire_step349_inventory')
    names=set(previous)
    for folder in [prior,table_source,S/'index-eight-order-two-343']:
        names.update(str(p.relative_to(ROOT)) for p in folder.rglob('*') if p.is_file())
    names.update(['drafts/literature/2026-10-19-index-sixteen-order-prime-two-test.md',
        'drafts/2026-10-19-index-sixteen-order-two-attempt.md',
        'history/349-2026-10-19-index-sixteen-table-critical-audit.md',
        'history/350-2026-10-19-index-sixteen-order-two-scope.md'])
    before={n:digest(ROOT/n) for n in sorted(names)}
    post349={
        'lemmas/L090-conductor389-index-sixteen-multiplier-order-table.md':
        ('f08ad5b4a84ce9c76600d5b5b8dcf718bd47e862a6a55b9925ebaa4f017303b4','c17c34aca9c0ab8499175282bbedbbc1884485ac5990576e6936fa56a908fa0c'),
        'drafts/2026-10-19-index-sixteen-table-critical-audit-attempt.md':
        ('ba47e6b004a15828a122be9e104529edf1663219b98d82ecc905972f1105209e','c622a5ff24fa3800eae5e81a7e08d6b1acecdffb2b389425186f614853e84dba')}
    for n,(a,b) in post349.items():
        need(previous[n]==a and before[n]==b,'exact_post349_document_transition_'+n)
    need(all(before[n]==h for n,h in previous.items() if n not in post349),'all_other_step349_inputs_unchanged')
    step349transition=read(prior/'inventory-transition.json')
    note='drafts/2026-10-19-index-sixteen-table-attempt.md'
    raw=(ROOT/note).read_bytes(); marker=b'\n## Completed execution\n'
    need(raw.count(marker)==1,'one_step347_document_append')
    oldhash='d0917f59ac51e1bd824dc732f96b50bbbe4b5e84eb099a28e22b0da1f7e4cd79'
    newhash='ba7345d0f3cf539defa7231456dbedbcebd5f9d73bbfb1f61159dbf60fb970a5'
    step347inventory=read(table_source/'canonical-input-hashes.json')
    need(hashlib.sha256(raw.split(marker)[0]).hexdigest()==oldhash
        and step347inventory[note]==oldhash and before[note]==newhash
        and step349transition['only_new_document_change']==note
        and step349transition['prior']==oldhash and step349transition['current']==newhash,
        'complete_retained_step347_document_transition')
    retained=step349transition['retained_step347_transition']
    transitions=[(retained,'only_permitted_post345_document_change','U-two-audit-345'),
        (retained['retained_step345_transition']['retained_step343_transition'],
         'only_permitted_post341_document_change','index-eight-table-audit-341'),
        (retained['retained_step345_transition']['retained_step343_transition']['retained_post337_transition'],
         'only_permitted_post337_document_change','index-eight-audit-337')]
    changed=set(post349)|{note}
    for t,key,folder in transitions:
        n=t[key]; historical=read(S/folder/'canonical-input-hashes.json')
        need(t['prior']==historical[n] and t['current']==before[n],'exact_retained_transition_'+folder)
        changed.add(n)
    for folder in [table_source,S/'U-two-audit-345',S/'index-eight-table-audit-341',S/'index-eight-audit-337']:
        historical=read(folder/'canonical-input-hashes.json')
        need(all(before[n]==h for n,h in historical.items() if n not in changed),
             'every_other_historical_input_'+folder.name)
    transition={'exact_post349':{n:{'prior':a,'current':b} for n,(a,b) in post349.items()},
        'retained_step349_transition':step349transition,'no_pathname_exemptions':True}
    save('canonical-input-hashes.json',before); save('inventory-transition.json',transition)
    for folder,count in [(S/'index-eight-order-two-343',248),(S/'U-two-audit-345',447),
                          (table_source,449),(prior,643)]:
        m=read(folder/'copy-manifest.json'); need(len(m)==count,'entire_manifest_'+folder.name)
        for n,e in m.items():
            need(before[e['source']]==e['sha256']==before[str((folder/n).relative_to(ROOT))],
                 'all_manifest_source_bindings_'+folder.name+'_'+n)
    for folder,count in [(table_source,6),(prior,7)]:
        codes=read(folder/'code-hashes.json'); need(len(codes)==count,'all_executed_sources_'+folder.name)
        need(all(digest(folder/n)==h for n,h in codes.items()),'every_executed_source_hash_'+folder.name)
    manifest={}
    def copy(dest,src):
        key=str(src.relative_to(ROOT)); raw=src.read_bytes()
        need(hashlib.sha256(raw).hexdigest()==before[key],'source_before_copy_'+dest)
        with (D/dest).open('xb') as f: f.write(raw)
        need(digest(D/dest)==before[key],'full_copy_'+dest)
        manifest[dest]={'source':key,'sha256':before[key]}
    for n in read(prior/'copy-manifest.json'):
        dest='old-U-'+n if n in ['radical-lattice.json','numerator-lattice.json','decision.json'] or n.startswith('action-') else n
        copy(dest,prior/n)
    sfiles=['basis.json']+['product-%02d.json'%i for i in range(48)]
    ufiles=['u-basis.json']+['u-product-%02d.json'%i for i in range(48)]
    vfiles=['v-basis.json']+['v-product-%02d.json'%i for i in range(48)]
    for name in sfiles:
        for dn in ['index-four-table-329','preserved-table-replay-331','preserved-table-audit-333',
            'index-four-order-two-335','index-eight-audit-337','index-eight-table-339','index-eight-table-audit-341']:
            need(digest(S/dn/name)==manifest[name]['sha256'],'entire_S_provenance_'+dn+'_'+name)
    for name in ufiles:
        for dn in ['index-eight-table-339','index-eight-table-audit-341','index-eight-order-two-343','U-two-audit-345']:
            need(digest(S/dn/name)==manifest[name]['sha256'],'entire_U_provenance_'+dn+'_'+name)
    for name in vfiles:
        need(digest(table_source/name)==manifest[name]['sha256'],'all_49_V_files_347_349_'+name)
    save('copy-manifest.json',manifest)
    def adapt(t,a,b):
        need(a in t,'exact_source_adaptation_'+a[:70]); return t.replace(a,b)
    # Fresh known-algorithm specialization; no old mathematical executable runs.
    p=(S/'index-eight-order-two-343/produce.py').read_text()
    for a,b in [('L088 U','L090 V'),('u-basis.json','v-basis.json'),('u-product-','v-product-'),
        ('248','496'),('61504','246016'),("nb['input_scale']==124","nb['input_scale']==248"),
        ("nb['prior_scales']==[31,62,124]","nb['prior_scales']==[31,62,124,248]"),
        ("nb['index']==8","nb['index']==16"),('integral_U','integral_V'),('scaled_U','scaled_V'),
        ('U_basis','V_basis'),('actual_scale_496_U','actual_scale_496_V'),('U_two_coordinate','V_two_coordinate')]: p=adapt(p,a,b)
    v=(S/'index-eight-order-two-343/verify.py').read_text()
    for a,b in [('u-basis.json','v-basis.json'),('u-product-','v-product-'),
        ('u-verification-report.json','v-verification-report.json'),('248','496'),
        ("validation['index']==8","validation['index']==16")]: v=adapt(v,a,b)
    ind=(prior/'independent.py').read_text()
    anchor="    for c in reread_cert['systems'].values(): reread(c)\n"
    ind=adapt(ind,anchor,anchor+"    original349=load(S/'index-sixteen-table-audit-349/exact-lattice-certificate.json')\n    need(original349==reread_cert,'entire_original349_exact_certificate_agrees')\n    for c in original349['systems'].values(): reread(c)\n")
    for name,body in [('produce.py',p),('verify.py',v),('independent.py',ind)]:
        compile(body,str(D/name),'exec')
        with (D/name).open('x') as f: f.write(body)
    code={p.name:digest(p) for p in D.glob('*.py')}; save('code-hashes.json',code)
    report['phase']='complete_S_U_V_inputs_and_original_dividends'
    counts={'product_slots':110592,'product_identities':2304,'remainder_coefficients':218880,
        'transport_entries':18432,'inverse_products':8,'division_certificates':2304,'identity_actions':96}
    iv=run('input_verify.py','input-report.json')
    for k,x in counts.items(): need(iv[k]==x,'full_S_'+k)
    need(iv['index']==4,'S_index')
    sb=read(D/'basis.json'); st=[read(D/('product-%02d.json'%i)) for i in range(48)]
    prefixes=['fixed-S-original-division-','fixed-S-fresh-division-','division-',
        'fixed-U-division-','u-division-','action-division-']
    checked={p:divisions('original343-'+p,sb,st) for p in prefixes[:3]}
    original347s=divisions('original347-division-',sb,st); fresh_s=divisions('division-',sb,st)
    uv=run('verify_u.py','u-verification-report.json')
    for k,x in counts.items(): need(uv[k]==x,'full_U_'+k)
    need(uv['index']==8 and uv['scale']==248 and uv['basis_elements']==48,'U_scale_index')
    ub=read(D/'u-basis.json'); ut=[read(D/('u-product-%02d.json'%i)) for i in range(48)]
    for p in prefixes[3:5]: checked[p]=divisions('original343-'+p,ub,ut)
    original347u=divisions('original347-u-division-',ub,ut); fresh_u=divisions('u-division-',ub,ut)
    oldJ=read(D/'old-U-radical-lattice.json')['basis']
    checked['action-division-']=divisions('original343-action-division-',ub,ut,oldJ)
    need(sum(checked.values())==13824 and set(checked)==set(prefixes),'all_six_original343_sets')
    report['phase']='full_audited_V_lattice_interfaces'
    block=source.split("    report['phase']='full_audited_V_lattice_interfaces'\n",1)[1]
    block=block.split("    report['phase']='one_V_table_production'",1)[0]
    # Names expected by the inspected full comparison block.
    fresh_s=fresh_s; fresh_u=fresh_u
    exec(compile(textwrap.dedent(block),str(table_source/'stage.py')+':full_lattice_interfaces','exec'),globals())
    vr=run('verify_v.py','v-verification-report.json')
    for k,x in counts.items(): need(vr[k]==x,'full_V_'+k)
    need(vr['index']==16 and vr['scale']==496 and vr['basis_elements']==48,'V_scale_index')
    vb=read(D/'v-basis.json'); vt=[read(D/('v-product-%02d.json'%i)) for i in range(48)]
    original347v=divisions('original347-v-division-',vb,vt); fresh_v=divisions('v-division-',vb,vt)
    # Also read the original step-349 fresh divisions in place. They are inventoried
    # and preserved, and their actual dividends cannot be replaced by fresh evidence.
    original349fresh=sum([divisions('division-',sb,st,folder=prior),
        divisions('u-division-',ub,ut,folder=prior),divisions('v-division-',vb,vt,folder=prior)])
    need(sum(checked.values())+original347s+original347u+original347v+original349fresh==27648,
         'all_27648_original349_divisions')
    report['phase']='all_six_complete_step349_solves'
    independent=run('independent.py','independent-report.json')
    for k,x in {'elimination_systems':6,'transport_entries':13824,'inclusion_entries':4608,
        'scaled_slots':11520,'index':16,'identity_entries':96,'solved_identity_actions':192,
        'complete_certificate_reread':True,'both_integral_V_containments':True}.items(): need(independent[k]==x,'independent_'+k)
    complete_inputs={'status':'PASS','failures':[],'all_before_modular_production':True,
        'complete_S':iv,'complete_U':uv,'complete_V':vr,'full_lattice_interfaces':evidence,
        'original349_divisions':27648,'fresh_S_U_V_divisions':fresh_s+fresh_u+fresh_v,
        'six_complete_original349_solves_checked':True,'independent':independent}
    save('complete-input-validation.json',complete_inputs)
    report['phase']='one_actual_V_radical_multiplier_test'
    producer=run('produce.py','producer-report.json')
    verifier=run('verify.py','verification-report.json')
    for r,label in [(producer,'producer'),(verifier,'independent')]:
        for k,x in {'input_product_slots':110592,'action_slots':110592,'frobenius_slots':13824,
            'frobenius_iterates':6,'exponent':64,'prime':2}.items(): need(r[k]==x,label+'_complete_'+k)
    for k in ['decision','index','frobenius_rank','radical_dimension','action_rank','action_kernel_dimension']:
        need(producer[k]==verifier[k],'independent_actual_V_result_'+k)
    need(verifier['action_division_certificates']==2304,'every_V_action_division_persisted')
    actions=divisions('action-division-',vb,vt,read(D/'radical-lattice.json')['basis'],action_prefix='')
    final=read(D/'decision.json')
    need(final['decision']==verifier['decision'] and final['index']==verifier['index'],'full_final_verdict')
    for name,obj in [('input-report.json',iv),('u-verification-report.json',uv),
        ('v-verification-report.json',vr),('independent-report.json',independent),
        ('input-validation.json',evidence),('complete-input-validation.json',complete_inputs),
        ('producer-report.json',producer),('verification-report.json',verifier)]:
        need(read(D/name)==obj,'all_report_rereads_'+name)
    for bn,tn,b,t in [('basis.json','product-',sb,st),('u-basis.json','u-product-',ub,ut),('v-basis.json','v-product-',vb,vt)]:
        need(read(D/bn)==b and all(read(D/(tn+'%02d.json'%i))==t[i] for i in range(48)),'all_table_rereads_'+bn)
    report['phase']='final_preservation'
    after={n:digest(ROOT/n) for n in before}; copies={n:digest(D/n) for n in manifest}
    code_after={n:digest(D/n) for n in code}
    need(before==after and code==code_after and copies=={n:e['sha256'] for n,e in manifest.items()},'complete_preservation')
    preservation={'equal':True,'before':before,'after':after,'code_before':code,'code_after':code_after,
        'fixed_before':{n:e['sha256'] for n,e in manifest.items()},'fixed_after':copies}
    save('preservation-stage.json',preservation)
    for name,obj in [('preservation-stage.json',preservation),('copy-manifest.json',manifest),
        ('canonical-input-hashes.json',before),('code-hashes.json',code),('inventory-transition.json',transition)]:
        need(read(D/name)==obj,'all_inventory_rereads_'+name)
    report.update(status='PASS',phase='complete',decision=final['decision'],index=final['index'],scale=496,
        frobenius_rank=verifier['frobenius_rank'],radical_dimension=verifier['radical_dimension'],
        action_rank=verifier['action_rank'],action_kernel_dimension=verifier['action_kernel_dimension'],
        original349_divisions=27648,fresh_input_divisions=fresh_s+fresh_u+fresh_v,
        V_action_divisions=actions,all_actual_dividends_checked=True,
        product_slots_per_table=110592,action_slots=110592,frobenius_slots=13824,
        original_files=len(before),fixed_copies=len(manifest),source_files=len(code),
        six_original349_solves_checked=True,row_operations=verifier['row_operations'])
except Exception as e:
    report.update(status='STOP',failures=[type(e).__name__+': '+str(e)])
report.update(seconds=time.monotonic()-START,required_seconds=180,required_bytes=134217728)
save('stage-report.json',report); print(json.dumps(report)); sys.exit(0 if report['status']=='PASS' else 1)
