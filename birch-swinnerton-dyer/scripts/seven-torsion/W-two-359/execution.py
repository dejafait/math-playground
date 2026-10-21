"""Replay-only L092 audit. No producer, historical wrapper or modular test executes."""
from pathlib import Path
import hashlib,json,sys,textwrap,time
sys.set_int_max_str_digits(0)
D=Path(__file__).resolve().parent; S=D.parent; ROOT=D.parents[2]; BEGAN=time.monotonic()
FIX=S/'index-thirty-two-table-355'
def read(p):return json.loads(p.read_text())
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def need(x,s):
    if not x:raise ArithmeticError(s)
def save(n,x):
    with (D/n).open('x') as f:json.dump(x,f,separators=(',',':'));f.write('\n')
report={'status':'STOP','phase':'initial_inventory','failures':[]}
try:
    original355=read(FIX/'canonical-input-hashes.json');need(len(original355)==6245,'all_6245_original_inputs')
    audit_names=set(original355)
    audit_names.update(str(p.relative_to(ROOT)) for p in FIX.rglob('*') if p.is_file())
    audit_names.update(['lemmas/L092-conductor389-index-thirty-two-multiplier-order-table.md',
        'drafts/literature/2026-10-20-index-thirty-two-table-critical-audit.md',
        'drafts/2026-10-20-index-thirty-two-table-critical-audit-attempt.md',
        'history/355-2026-10-20-index-thirty-two-table.md'])

    fixed357=S/'W-table-audit-357'
    previous357=read(fixed357/'audit-input-hashes.json')
    need(len(previous357)==6801,'entire_6801_step357_inventory')
    audit_names.update(previous357)
    audit_names.update(str(p.relative_to(ROOT)) for p in fixed357.rglob('*') if p.is_file())
    audit_names.update(['drafts/literature/2026-10-20-index-thirty-two-order-prime-two-test.md',
        'drafts/2026-10-20-W-two-attempt.md','history/357-2026-10-20-index-thirty-two-table-critical-audit.md',
        'history/358-2026-10-20-W-two-source-scope.md'])
    audit_before={n:digest(ROOT/n) for n in sorted(audit_names)}
    prepared={p.name:digest(p) for p in D.iterdir() if p.suffix in ('.py','.txt')}
    save('audit-input-hashes.json',audit_before);save('prepared-source-hashes.json',prepared)

    post357={
        'lemmas/L092-conductor389-index-thirty-two-multiplier-order-table.md':
        ('4be8ae3f18f2545688ca8ecc0839521c68e6810f8c6bb79f3455a2b7a79c1f85','193730fc345fc756aa50cd308ec557157fcae213500ddb93c5809920123be73a'),
        'drafts/2026-10-20-index-thirty-two-table-critical-audit-attempt.md':
        ('a4b2cfd0c575ee5b97ad9516e28c4ed220cdd7579598050ff275121e923fa0cc','d0acc4a9b1b3e5cdaed5ab8678d816d965535e162392d5ac306cc847bbf2b433')}
    for n,(a,b) in post357.items():need(previous357[n]==a and audit_before[n]==b,'exact_post357_'+n)
    need(all(audit_before[n]==h for n,h in previous357.items() if n not in post357),'all_other_step357_originals')
    note357='drafts/2026-10-20-index-thirty-two-table-critical-audit-attempt.md'
    raw357=(ROOT/note357).read_bytes();mark357=b'\n## Completed execution\n'
    need(raw357.count(mark357)==1 and hashlib.sha256(raw357.split(mark357)[0]).hexdigest()==post357[note357][0], 'exact_step357_note_append')
    mf357=read(fixed357/'complete-copy-manifest.json');need(len(mf357)==322,'all_322_step357_copies')
    for n,e in mf357.items():need(audit_before[e['source']]==e['sha256']==audit_before[str((fixed357/n).relative_to(ROOT))],'whole_step357_copy_binding_'+n)
    cd357=read(fixed357/'code-hashes.json');need(len(cd357)==14,'all_14_step357_sources')
    need(all(digest(fixed357/n)==h for n,h in cd357.items()),'all_step357_executed_source_hashes')
    save('post357-transition.json',{'exact_changes':post357,'all_other_inputs_unchanged':True,'no_pathname_exemptions':True})
    # Fresh direct W reconstruction also replays every original step-357 system.
    wmain=(fixed357/'w_main.txt').read_text()
    anchor="    for c in persisted['systems'].values(): reread(c)\n"
    need(wmain.count(anchor)==1,'unique_W_original_solve_insertion')
    wmain=wmain.replace(anchor,anchor+"    original357=load(S/'W-table-audit-357/W-exact-lattice-certificate.json')\n    need(original357==persisted,'entire_original357_W_certificate')\n    for c in original357['systems'].values(): reread(c)\n")
    with (D/'w_main.txt').open('x') as f:f.write(wmain)
    note='drafts/2026-10-20-index-thirty-two-table-attempt.md'
    oldhash='f2dbb381fe775ccfbdb1df7c863c863759a9d3a987d7f127ff6bd85635b5a14c'
    newhash='65bd626d8d1f5cc4eef75da9d778056131654ebe3c46247e199edd59a6c1af92'
    raw=(ROOT/note).read_bytes();marker=b'\n## Completed execution\n'
    need(original355[note]==oldhash and audit_before[note]==newhash and raw.count(marker)==1
        and hashlib.sha256(raw.split(marker)[0]).hexdigest()==oldhash,'exact_step355_document_append')
    need(all(audit_before[n]==h for n,h in original355.items() if n!=note),'all_other_step355_originals')
    manifest355=read(FIX/'complete-copy-manifest.json');need(len(manifest355)==272,'all_272_copies')
    for n,e in manifest355.items():
        need(audit_before[e['source']]==e['sha256']==audit_before[str((FIX/n).relative_to(ROOT))],'original355_copy_binding_'+n)
    code355=read(FIX/'code-hashes.json');need(len(code355)==12,'all_twelve_step355_sources')
    need(all(digest(FIX/n)==h for n,h in code355.items()),'all_step355_source_hashes')
    save('post355-transition.json',{'path':note,'prior':oldhash,'current':newhash,'no_pathname_exemptions':True})
    report['phase']='complete_fixed_input_replay'
    # This complete saved body only replays S/U/V, divisions and six V systems.
    body=(FIX/'input-replay-body.txt').read_text()
    anchor='before={n:digest(ROOT/n) for n in sorted(names)}'
    need(body.count(anchor)==1,'unique_encompassing_inventory_adaptation')
    body=body.replace(anchor,'names.update(audit_names)\n'+anchor)
    with (D/'input-replay-body.txt').open('x') as f:f.write(body)
    exec(compile(body,str(D/'input-replay-body.txt'),'exec'),globals())
    # This bounded slice checks all step-353 divisions and both full preimages.
    stage=(FIX/'stage.py').read_text()
    block=between(stage,"    report['phase']='fixed_step353_divisions_and_multiplier_interfaces'\n",
        "    report['phase']='table_source_specialization'\n")
    block=textwrap.dedent(block)
    with (D/'fixed-W-interface-body.txt').open('x') as f:f.write(block)
    exec(compile(block,str(D/'fixed-W-interface-body.txt'),'exec'),globals())
    report['phase']='full_fixed_W_table_and_divisions'
    for n in ['w-basis.json','verify_w.py']+['w-product-%02d.json'%i for i in range(48)]:copy(n,FIX/n)
    wb=read(D/'w-basis.json');wt=[read(D/('w-product-%02d.json'%i)) for i in range(48)]
    # Bind copied files to the encompassing inventory, as well as source bytes.
    for n,e in manifest.items():need(audit_before[e['source']]==e['sha256'],'encompassing_copy_binding_'+n)
    wr=run('verify_w.py','w-verification-report.json')
    for k,x in counts.items():need(wr[k]==x,'all_W_'+k)
    need(wr['index']==32 and wr['scale']==992,'W_scale_index')
    fixed355=sum([divisions('division-',sb,st,folder=FIX),divisions('u-division-',ub,ut,folder=FIX),
        divisions('v-division-',vb,vt,folder=FIX),divisions('w-division-',wb,wt,folder=FIX)])
    fresh_w=divisions('w-division-',wb,wt)
    need(fixed355==9216 and fresh_w==2304,'all_fixed355_and_fresh_W_divisions')
    report['phase']='direct_complete_W_reconstruction'
    # Only the general exact elimination definitions are reused; no stored
    # transport/inverse or producer helper supplies an independent solve input.
    definitions=(FIX/'solve_replay.py').read_text().split('def main():\n',1)[0]
    wsource=definitions+(D/'w_main.txt').read_text()
    compile(wsource,str(D/'W_reconstruct.py'),'exec')
    with (D/'W_reconstruct.py').open('x') as f:f.write(wsource)
    code={p.name:digest(p) for p in D.iterdir() if p.suffix in ('.py','.txt')}
    save('input-audit-code-hashes.json',code);save('complete-copy-manifest.json',manifest)
    wi=run('W_reconstruct.py','W-solve-report.json')
    need(wi['elimination_systems']==6 and wi['index']==32 and wi['scale']==992
        and wi['solved_identity_actions']==192 and wi['both_integral_W_containments']
        and wi['whole_step355_V_solves_replayed'],'complete_independent_W_solve_report')
    evidence={'status':'PASS','failures':[],'original349_divisions':27648,'original351_divisions':fixed351,
        'original353_divisions':fixed353,'original355_divisions':fixed355,'fresh_divisions':fresh_s+fresh_u+fresh_v+fresh_w,
        'all_actual_dividends_checked':True,'original_six_solves_349_351_353_355_replayed':True,'W_direct_solve_systems':6}
    save('persisted-input-checks.json',evidence)
    for bn,tn,b,t in [('basis.json','product-',sb,st),('u-basis.json','u-product-',ub,ut),
        ('v-basis.json','v-product-',vb,vt),('w-basis.json','w-product-',wb,wt)]:
        need(read(D/bn)==b and all(read(D/(tn+'%02d.json'%i))==t[i] for i in range(48)),'full_final_table_'+bn)
    for n,obj in [('w-verification-report.json',wr),('W-solve-report.json',wi),('input-report.json',iv),
        ('u-verification-report.json',uv),('v-verification-report.json',vr),('solve-report.json',independent),
        ('persisted-input-checks.json',evidence)]:need(read(D/n)==obj,'full_final_report_'+n)

    report['phase']='all_fixed357_actual_divisions'
    fixed357_count=sum([divisions('division-',sb,st,folder=fixed357),
        divisions('u-division-',ub,ut,folder=fixed357),divisions('v-division-',vb,vt,folder=fixed357),
        divisions('w-division-',wb,wt,folder=fixed357)])
    need(fixed357_count==9216,'all_9216_fixed357_actual_dividends')
    report['phase']='new_W_modular_source_specialization'
    p=(S/'index-sixteen-order-two-351/produce.py').read_text()
    p=p.replace('496','992').replace('246016','984064')
    p=p.replace("nb['input_scale']==248","nb['input_scale']==496")
    p=p.replace("nb['prior_scales']==[31,62,124,248]","nb['prior_scales']==[31,62,124,248,496]")
    p=p.replace("nb['index']==16","nb['index']==32")
    p=p.replace('v-basis.json','w-basis.json').replace('v-product-','w-product-')
    v=(S/'index-sixteen-order-two-351/verify.py').read_text()
    v=v.replace('496','992').replace("validation['index']==16","validation['index']==32")
    v=v.replace('v-basis.json','w-basis.json').replace('v-product-','w-product-').replace('v-verification-report.json','w-verification-report.json')
    for name in ['input-basis.json','frobenius.json','radical-lattice','numerator-lattice','action-',
        'action-kernel.json','decision.json','preservation-producer.json','preservation-verifier.json',
        'input-hashes.json','producer-report.json','verification-report.json']:
        p=p.replace("'"+name,"'test-"+name);v=v.replace("'"+name,"'test-"+name)
    for name,t in [('W_produce.py',p),('W_verify.py',v)]:
        compile(t,str(D/name),'exec')
        with (D/name).open('x') as f:f.write(t)
    code={p.name:digest(p) for p in D.iterdir() if p.suffix in ('.py','.txt')}
    save('code-hashes.json',code)
    report['phase']='one_actual_W_radical_action_multiplier_test'
    producer=run('W_produce.py','test-producer-report.json')
    verifier=run('W_verify.py','test-verification-report.json')
    for r,label in [(producer,'producer'),(verifier,'independent')]:
        for k,x in {'input_product_slots':110592,'action_slots':110592,'frobenius_slots':13824,
            'frobenius_iterates':6,'exponent':64,'prime':2}.items():need(r[k]==x,label+'_complete_'+k)
    for k in ['decision','index','frobenius_rank','radical_dimension','action_rank','action_kernel_dimension']:
        need(producer[k]==verifier[k],'independent_actual_W_result_'+k)
    need(verifier['action_division_certificates']==2304,'all_W_action_divisions_persisted')
    WJ=read(D/'test-radical-lattice.json')['basis']
    action_count=divisions('test-action-division-',wb,wt,WJ,action_prefix='test-')
    need(action_count==2304,'all_W_action_actual_dividends_reread')
    for n,o in [('test-producer-report.json',producer),('test-verification-report.json',verifier),
        ('test-decision.json',read(D/'test-decision.json'))]:need(read(D/n)==o,'final_new_result_reread_'+n)
    report.update(W_decision=verifier['decision'],W_multiplier_index=verifier['index'],
        W_frobenius_rank=verifier['frobenius_rank'],W_radical_dimension=verifier['radical_dimension'],
        W_action_rank=verifier['action_rank'],W_action_kernel_dimension=verifier['action_kernel_dimension'],
        new_W_action_divisions=action_count,fixed357_divisions=fixed357_count)
    report['phase']='final_preservation'
    audit_after={n:digest(ROOT/n) for n in audit_before}
    copies={n:digest(D/n) for n in manifest};code_after={n:digest(D/n) for n in code}
    need(audit_before==audit_after and code==code_after and all(code[n]==h for n,h in prepared.items())
        and copies=={n:e['sha256'] for n,e in manifest.items()},'entire_preservation')
    preservation={'equal':True,'before':audit_before,'after':audit_after,'code_before':code,'code_after':code_after,
        'fixed_before':{n:e['sha256'] for n,e in manifest.items()},'fixed_after':copies}
    save('preservation-audit.json',preservation)
    for n,obj in [('audit-input-hashes.json',audit_before),('preservation-audit.json',preservation),
        ('code-hashes.json',code),('complete-copy-manifest.json',manifest)]:need(read(D/n)==obj,'entire_final_inventory_'+n)
    report.update(status='PASS',phase='complete',products_per_table=2304,product_slots_per_table=110592,index=32,scale=992,
        original_divisions=27648+fixed351+fixed353+fixed355,fresh_divisions=fresh_s+fresh_u+fresh_v+fresh_w,
        original_files=len(audit_before),fixed_copies=len(manifest),source_files=len(code),direct_W_systems=6,
        original_349_351_353_355_solves_replayed=True)
except Exception as exc:
    report.update(status='STOP',failures=[type(exc).__name__+': '+str(exc)])
report.update(seconds=time.monotonic()-BEGAN,required_seconds=180,required_bytes=134217728)
save('audit-report.json',report);print(json.dumps(report));sys.exit(0 if report['status']=='PASS' else 1)
