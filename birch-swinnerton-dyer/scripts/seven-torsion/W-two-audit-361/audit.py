"""Replay-only L092 audit. No producer, historical wrapper or modular test executes."""
from pathlib import Path
import hashlib,json,sys,textwrap,time,re
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

    fixed359=S/'W-two-359'
    previous359=read(fixed359/'audit-input-hashes.json')
    need(len(previous359)==7363,'entire_7363_step359_inventory')
    audit_names.update(previous359)
    audit_names.update(str(p.relative_to(ROOT)) for p in fixed359.rglob('*') if p.is_file())
    audit_names.update([
        'lemmas/L093-conductor389-index-thirty-two-order-not-2-maximal.md',
        'drafts/literature/2026-10-20-W-two-critical-audit.md',
        'drafts/2026-10-20-W-two-critical-audit-attempt.md',
        'history/359-2026-10-20-W-two-index64.md',
        'history/360-2026-10-20-W-two-audit-scope.md',
        'scripts/seven-torsion/V-two-audit-353/independent.py'])
    audit_before={n:digest(ROOT/n) for n in sorted(audit_names)}
    prepared={p.name:digest(p) for p in D.iterdir() if p.suffix in ('.py','.txt')}
    save('audit-input-hashes.json',audit_before);save('prepared-source-hashes.json',prepared)


    note359='drafts/2026-10-20-W-two-attempt.md'
    a359='99c1e1ceea80f471d2b1ca1a1c8dbd8d8ab86a70070e05241e9df91a04d96beb'
    b359='3f0b22531c79a9e28e3c128e1cf2cc399b30fa5404fc5b26c7f1a40790c5f765'
    hist359='history/359-2026-10-20-W-two-index64.md'
    h359='5741a0f3a78cdddfa05f9945f2e6ed3ef2a748bbb6e8d5badb8592fe8f5ecf92'
    raw359=(ROOT/note359).read_bytes(); marker359=b'\n## Completed execution\n'
    need(previous359[note359]==a359 and audit_before[note359]==b359
        and audit_before[hist359]==h359 and a359 in (ROOT/hist359).read_text()
        and b359 in (ROOT/hist359).read_text() and raw359.count(marker359)==1
        and hashlib.sha256(raw359.split(marker359)[0]).hexdigest()==a359,
        'exact_step359_append_bound_to_old_inventory_and_history')
    need(all(audit_before[n]==h for n,h in previous359.items() if n!=note359),
        'all_other_step359_originals')
    mf359=read(fixed359/'complete-copy-manifest.json')
    need(len(mf359)==322,'all_322_step359_copy_bindings')
    for n,e in mf359.items():
        need(audit_before[e['source']]==e['sha256']
            ==audit_before[str((fixed359/n).relative_to(ROOT))],'entire_fixed359_copy_'+n)
    cd359=read(fixed359/'code-hashes.json');need(len(cd359)==17,'all_17_step359_sources')
    need(all(digest(fixed359/n)==h for n,h in cd359.items()),'all_fixed359_source_hashes')
    save('post359-transition.json',{'path':note359,'prior':a359,'current':b359,
        'history':hist359,'history_sha256':h359,'all_other_inputs_unchanged':True,
        'no_pathname_exemptions':True})
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

    wanchor="    for c in original357['systems'].values(): reread(c)\n"
    need(wmain.count(wanchor)==1,'unique_step359_W_solve_insertion')
    wmain=wmain.replace(wanchor,wanchor+
        "    original359=load(S/'W-two-359/W-exact-lattice-certificate.json')\n"+
        "    need(original359==persisted,'entire_original359_W_certificate')\n"+
        "    for c in original359['systems'].values(): reread(c)\n")
    vanchor="    for c in prod['systems'].values(): reread(c)\n"
    need(wmain.count(vanchor)==1,'unique_all_V_solve_copies_insertion')
    wmain=wmain.replace(vanchor,vanchor+
        "    for folder in ['W-table-audit-357','W-two-359']:\n"+
        "        vc=load(S/folder/'exact-lattice-certificate.json')\n"+
        "        need(vc==fresh,'entire_original_V_copy_'+folder)\n"+
        "        for c in vc['systems'].values(): reread(c)\n")
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

    report['phase']='complete_step359_input_dividends'
    fixed359_count=sum([divisions('division-',sb,st,folder=fixed359),
        divisions('u-division-',ub,ut,folder=fixed359),
        divisions('v-division-',vb,vt,folder=fixed359),
        divisions('w-division-',wb,wt,folder=fixed359)])
    need(fixed359_count==9216,'all_9216_step359_input_divisions')
    # Exact bindings of the entire 322 fixed files to this fresh replay.
    for n,e in mf359.items():
        need((D/n).is_file() and digest(D/n)==e['sha256'],'original_fixed_fresh_'+n)
    core359=['test-input-basis.json','test-frobenius.json','test-radical-lattice.json',
        'test-action-kernel.json','test-numerator-lattice.json','test-decision.json']
    core359+=['test-action-%02d.json'%i for i in range(48)]
    for n in core359+['W_verify.py']:copy(n,fixed359/n)
    WJ=read(D/'test-radical-lattice.json')['basis']
    original_actions=divisions('test-action-division-',wb,wt,WJ,
        folder=fixed359,action_prefix='test-')
    need(original_actions==2304,'every_original_W_actual_action_dividend')
    # Adapt only the already assessed independent full rank/preimage instance.
    ind=(S/'V-two-audit-353/independent.py').read_text()
    ind=ind.replace("OLD = D.parent/'index-sixteen-order-two-351'",
        "OLD = D.parent/'W-two-359'")
    ind=ind.replace('v-product-','w-product-')
    ind=re.sub(r'\b43\b','42',ind)
    ind=re.sub(r'\b32\b','64',ind)
    ind=re.sub(r'\b496\b','992',ind)
    ind=ind.replace('[2]*42+[1]*5','[2]*42+[1]*6')
    ind=ind.replace('action_kernel_dimension=5','action_kernel_dimension=6')
    ind=ind.replace('action_left_inverse_entries=99072','action_left_inverse_entries=96768')
    ind=ind.replace('selected_inverse_entries=1849','selected_inverse_entries=1764')
    ind=ind.replace('[(I:I):V] = absolute determinant of V basis in (I:I)',
        '[(I:I):W] = absolute determinant of W basis in (I:I)')
    oldread="def read(path):\n    return json.loads(path.read_text())"
    newread=("def read(path):\n    if path.parent==D and (path.name in "+repr(
        ['frobenius.json','radical-lattice.json','numerator-lattice.json',
        'action-kernel.json','decision.json','input-basis.json'])+
        " or __import__('re').fullmatch(r'action-[0-9]{2}\\.json',path.name)):\n"+
        "        path=path.with_name('test-'+path.name)\n"+
        "    return json.loads(path.read_text())")
    need(ind.count(oldread)==1,'unique_independent_storage_redirection')
    ind=ind.replace(oldread,newread)
    compile(ind,str(D/'independent.py'),'exec')
    with (D/'independent.py').open('x') as f:f.write(ind)
    code={p.name:digest(p) for p in D.iterdir() if p.suffix in ('.py','.txt')}
    save('code-hashes.json',code);save('audit-complete-copy-manifest.json',manifest)
    report['phase']='full_fixed_W_modular_replay'
    verifier=run('W_verify.py','test-verification-report.json')
    for k,x in {'input_product_slots':110592,'action_slots':110592,
        'frobenius_slots':13824,'frobenius_iterates':6,'exponent':64,'prime':2,
        'action_division_certificates':2304,'frobenius_rank':1,
        'action_rank':42,'index':64,'action_kernel_dimension':6}.items():
        need(verifier[k]==x,'complete_W_replay_'+k)
    for name in ['test-producer-report.json','test-verification-report.json']:
        prior_report=read(fixed359/name)
        need(prior_report['status']=='PASS' and not prior_report['failures'],'fixed_report_'+name)
        for key in ['decision','index','frobenius_rank','radical_dimension',
            'action_rank','action_kernel_dimension']:
            need(prior_report[key]==verifier[key],'whole_fixed_fresh_result_'+key)
    action_count=divisions('test-action-division-',wb,wt,WJ,action_prefix='test-')
    need(action_count==2304,'all_fresh_W_actual_action_dividends')
    report['phase']='independent_complete_W_rank_kernel_and_global_preimages'
    supplement=run('independent.py','independent-report.json')
    for k,x in {'frobenius_rank':1,'action_rank':42,'index':64,
        'radical_kernel_dimension':47,'action_kernel_dimension':6,
        'independent_preimages':2,'action_entries':110592,
        'action_factorization_entries':110592,'action_left_inverse_entries':96768,
        'full_strict_action_entries':2304,'all_load_bearing_certificates_reread':True}.items():
        need(supplement[k]==x,'entire_independent_supplement_'+k)
    for n in core359:
        need(read(D/n)==read(fixed359/n),'final_entire_fixed_W_certificate_'+n)
    for n,obj in [('independent-report.json',supplement),
        ('test-verification-report.json',verifier)]:
        need(read(D/n)==obj,'final_audit_report_reread_'+n)
    need(read(D/'audit-complete-copy-manifest.json')==manifest,'final_complete_copy_manifest')
    report.update(W_decision=verifier['decision'],W_multiplier_index=verifier['index'],
        W_frobenius_rank=verifier['frobenius_rank'],W_action_rank=verifier['action_rank'],
        W_action_kernel_dimension=verifier['action_kernel_dimension'],
        fixed357_divisions=fixed357_count,fixed359_input_divisions=fixed359_count,
        fixed359_action_divisions=original_actions,fresh_W_action_divisions=action_count,
        full_independent_supplement=supplement,all_original_V_and_W_systems_replayed=True)
    report['phase']='final_preservation'
    audit_after={n:digest(ROOT/n) for n in audit_before}
    copies={n:digest(D/n) for n in manifest};code_after={n:digest(D/n) for n in code}
    need(audit_before==audit_after and code==code_after and all(code[n]==h for n,h in prepared.items())
        and copies=={n:e['sha256'] for n,e in manifest.items()},'entire_preservation')
    preservation={'equal':True,'before':audit_before,'after':audit_after,'code_before':code,'code_after':code_after,
        'fixed_before':{n:e['sha256'] for n,e in manifest.items()},'fixed_after':copies}
    save('preservation-audit.json',preservation)
    for n,obj in [('audit-input-hashes.json',audit_before),('preservation-audit.json',preservation),
        ('code-hashes.json',code),('audit-complete-copy-manifest.json',manifest)]:need(read(D/n)==obj,'entire_final_inventory_'+n)
    report.update(status='PASS',phase='complete',products_per_table=2304,product_slots_per_table=110592,index=32,scale=992,
        original_divisions=27648+fixed351+fixed353+fixed355,fresh_divisions=fresh_s+fresh_u+fresh_v+fresh_w,
        original_files=len(audit_before),fixed_copies=len(manifest),source_files=len(code),direct_W_systems=6,
        original_349_351_353_355_solves_replayed=True)
except Exception as exc:
    report.update(status='STOP',failures=[type(exc).__name__+': '+str(exc)])
report.update(seconds=time.monotonic()-BEGAN,required_seconds=180,required_bytes=134217728)
save('audit-report.json',report);print(json.dumps(report));sys.exit(0 if report['status']=='PASS' else 1)
