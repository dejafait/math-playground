"""Replay-only L092 audit. No producer, historical wrapper or modular test executes."""
from pathlib import Path
import hashlib,json,sys,textwrap,time,re
sys.set_int_max_str_digits(0)
D=Path(__file__).resolve().parent; S=D.parent; ROOT=D.parents[2]; BEGAN=time.monotonic()
FIX=S/'index-thirty-two-table-355'
def change(t,a,b):
    if t.count(a)!=1:raise ValueError("unique_adaptation_"+a[:80])
    return t.replace(a,b)
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

    fixed361=S/'W-two-audit-361'
    previous361=read(fixed361/'audit-input-hashes.json')
    need(len(previous361)==8040,'entire_8040_step361_inventory')
    audit_names.update(previous361)
    audit_names.update(str(p.relative_to(ROOT)) for p in fixed361.rglob('*') if p.is_file())
    audit_names.update(['drafts/literature/2026-10-20-index-sixty-four-multiplier-table.md',
        'drafts/2026-10-20-index-sixty-four-table-attempt.md',
        'history/361-2026-10-20-W-two-critical-audit.md',
        'history/362-2026-10-20-index64-table-scope.md'])

    fixed363=S/'index-sixty-four-table-363'
    previous363=read(fixed363/'audit-input-hashes.json')
    need(len(previous363)==8721,'all_8721_step363_originals')
    audit_names.update(previous363)
    audit_names.update(str(p.relative_to(ROOT)) for p in fixed363.rglob('*') if p.is_file())
    audit_names.update(['lemmas/L094-conductor389-index-sixty-four-multiplier-order-table.md',
        'drafts/literature/2026-10-20-index-sixty-four-table-critical-audit.md',
        'drafts/2026-10-20-index-sixty-four-table-critical-audit-attempt.md',
        'history/363-2026-10-20-index64-table.md','history/364-2026-10-20-index64-table-audit-scope.md'])
    audit_before={n:digest(ROOT/n) for n in sorted(audit_names)}
    prepared={p.name:digest(p) for p in D.iterdir() if p.suffix in ('.py','.txt')}
    save('audit-input-hashes.json',audit_before);save('prepared-source-hashes.json',prepared)




    note363='drafts/2026-10-20-index-sixty-four-table-attempt.md'
    a363='206adc232e71da52b5191e7f619869c31a04ea0b80359b2e3c31b8ec6839a1af'
    b363='89a6dfbe3cd544897ed837c6605535464653cf5b1a5bc121e2726abd42dfee40'
    hist363='history/363-2026-10-20-index64-table.md'
    raw363=(ROOT/note363).read_bytes();marker363=b'\n## Completed execution\n'
    need(previous363[note363]==a363 and audit_before[note363]==b363
        and raw363.count(marker363)==1 and hashlib.sha256(raw363.split(marker363)[0]).hexdigest()==a363
        and a363 in (ROOT/hist363).read_text() and b363 in (ROOT/hist363).read_text(),
        'exact_post363_append_bound_to_old_inventory_and_history')
    need(all(audit_before[n]==h for n,h in previous363.items() if n!=note363),'every_other_step363_original')
    mf363=read(fixed363/'table-complete-copy-manifest.json')
    need(len(mf363)==383,'all_383_step363_copy_bindings')
    for n,e in mf363.items():
        need(audit_before[e['source']]==e['sha256']==audit_before[str((fixed363/n).relative_to(ROOT))],
            'whole_step363_copy_binding_'+n)
    cd363=read(fixed363/'code-hashes.json');need(len(cd363)==20,'all_twenty_step363_sources')
    need(all(digest(fixed363/n)==h for n,h in cd363.items()),'all_step363_executed_source_hashes')
    save('post363-transition.json',{'path':note363,'prior':a363,'current':b363,
        'history':hist363,'history_sha256':audit_before[hist363],
        'all_other_originals_unchanged':True,'no_pathname_exemptions':True})
    post361={
        'lemmas/L093-conductor389-index-thirty-two-order-not-2-maximal.md':
        ('a23cf1537577dbb1bfbfd85efb8b5f4c1c7d9865a3d1763dd00cf8f9d24a4344','06775693da9f08d6a43b3aced0f97fc8b84ca68eda4d6f77799c58e84ca976b5'),
        'drafts/2026-10-20-W-two-critical-audit-attempt.md':
        ('a1772ff757b2cf9133778b96236aab4248c3c157baf780d16da7e71412a95367','f981d3e7c19c11161c5503046328e7dff1ad82f48bcc63dc9442b05a03d63a5b')}
    hist361='history/361-2026-10-20-W-two-critical-audit.md'
    h361='5f01bba525a8e7b0aa262c51ef00565ce2637fce631c6e45431c77f682da01f2'
    need(audit_before[hist361]==h361,'exact_history361_hash')
    history361=(ROOT/hist361).read_text()
    for n,(a,b) in post361.items():
        need(previous361[n]==a and audit_before[n]==b and a in history361 and b in history361,
            'exact_post361_bound_to_inventory_and_history_'+n)
    note361='drafts/2026-10-20-W-two-critical-audit-attempt.md'
    raw361=(ROOT/note361).read_bytes(); marker361=b'\n## Completed execution\n'
    need(raw361.count(marker361)==1 and hashlib.sha256(raw361.split(marker361)[0]).hexdigest()==post361[note361][0],
        'exact_step361_note_append')
    need(all(audit_before[n]==h for n,h in previous361.items() if n not in post361),'every_other_step361_original')
    mf361=read(fixed361/'audit-complete-copy-manifest.json')
    need(len(mf361)==377,'all_377_step361_copy_bindings')
    for n,e in mf361.items():
        need(audit_before[e['source']]==e['sha256']==audit_before[str((fixed361/n).relative_to(ROOT))],
            'whole_step361_copy_binding_'+n)
    cd361=read(fixed361/'code-hashes.json');need(len(cd361)==17,'all_17_step361_sources')
    need(all(digest(fixed361/n)==h for n,h in cd361.items()),'every_step361_source_hash')
    save('post361-transition.json',{'exact_changes':post361,'history':hist361,'history_sha256':h361,
        'every_other_original_unchanged':True,'no_pathname_exemptions':True})
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

    wa="    for c in original359['systems'].values(): reread(c)\n"
    need(wmain.count(wa)==1,'unique_step361_W_copy_comparison')
    wmain=wmain.replace(wa,wa+
        "    original361=load(S/'W-two-audit-361/W-exact-lattice-certificate.json')\n"+
        "    need(original361==persisted,'entire_original361_W_certificate')\n"+
        "    for c in original361['systems'].values(): reread(c)\n")
    wmain=wmain.replace("['W-table-audit-357','W-two-359']", "['W-table-audit-357','W-two-359','W-two-audit-361']")

    wa363="    for c in original361['systems'].values(): reread(c)\n"
    need(wmain.count(wa363)==1,'unique_W363_solve_insertion')
    wmain=wmain.replace(wa363,wa363+
        "    original363=load(S/'index-sixty-four-table-363/W-exact-lattice-certificate.json')\n"+
        "    need(original363==persisted,'entire_original363_W_certificate')\n"+
        "    for c in original363['systems'].values(): reread(c)\n")
    wmain=wmain.replace("['W-table-audit-357','W-two-359','W-two-audit-361']",
        "['W-table-audit-357','W-two-359','W-two-audit-361','index-sixty-four-table-363']")
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

    report['phase']='fixed_W_eliminations_and_actual_actions'
    fixed_replay=run('W_verify.py','test-verification-report.json')
    need(fixed_replay['index']==64 and fixed_replay['action_rank']==42
        and fixed_replay['action_division_certificates']==2304,'complete_fixed_W_elimination_replay')
    fresh_actions=divisions('test-action-division-',wb,wt,WJ,action_prefix='test-')
    fixed361_inputs=sum([divisions('division-',sb,st,folder=fixed361),
        divisions('u-division-',ub,ut,folder=fixed361),divisions('v-division-',vb,vt,folder=fixed361),
        divisions('w-division-',wb,wt,folder=fixed361)])
    fixed361_actions=divisions('test-action-division-',wb,wt,WJ,folder=fixed361,action_prefix='test-')
    need(fixed361_inputs==9216 and fixed361_actions==fresh_actions==2304,'all_step361_and_fresh_actual_dividends')
    for n in core359:
        need(read(fixed361/n)==read(fixed359/n)==read(D/n),'whole_fixed359_361_fresh_'+n)
    report['phase']='fixed_independent_ranks_kernels_and_global_preimages'
    # Use binary-product definitions only: no rank search, elimination,
    # kernel discovery, inverse construction or new preimage production.
    defs=(fixed361/'independent.py').read_text().split('def preimage(',1)[0]
    ns={'__file__':str(D/'fixed_independent.py')}
    with (D/'fixed_independent.py').open('x') as f:f.write(defs)
    exec(compile(defs,str(D/'fixed_independent.py'),'exec'),ns)
    bm=ns['bm'];bits=ns['bits']
    def binary_shape(a,h,w):
        need(type(a) is list and len(a)==h and all(type(r) is list and len(r)==w for r in a),'full_binary_shape')
        for row in a:bits(row)
    def fixed_rank(label,A,r,kernel):
        c=read(fixed361/(label+'-full-rank.json'));height=len(A)
        shapes={'matrix':(height,48),'columns':(height,r),'factor':(r,48),'left_inverse':(r,height),
            'kernel':(48,48-r),'kernel_projection':(48-r,48),'kernel_rows':(48-r,48),'selected_inverse':(r,r)}
        for key,(h,w) in shapes.items():binary_shape(c[key],h,w)
        C,B,L,K,P=map(c.get,['columns','factor','left_inverse','kernel','kernel_projection'])
        RI=[[int(i==j) for j in range(r)] for i in range(r)]
        KI=[[int(i==j) for j in range(48-r)] for i in range(48-r)]
        need(c['matrix']==A and C==[row[:r] for row in A] and bm(C,B)==A and bm(L,C)==RI,
            'full_fixed_rank_factorization_'+label)
        need(B==I[:r] and c['rank']==r and bm(A,K)==[[0]*(48-r) for _ in A] and bm(P,K)==KI
            and K==tr(c['kernel_rows']) and c['kernel_rows']==I[r:]==kernel,'entire_fixed_kernel_'+label)
        rows=c['selected_rows'];inv=c['selected_inverse']
        need(len(rows)==r and len(set(rows))==r and all(type(x) is int and 0<=x<height for x in rows),
            'fixed_selected_rows_'+label)
        selected=[C[i] for i in rows]
        need(bm(selected,inv)==RI and bm(inv,selected)==RI,'both_fixed_selected_inverse_products_'+label)
    fc=read(D/'test-frobenius.json')
    first=tr([[x%2 for x in wt[i][i]] for i in range(48)]);terminal=first
    for k in range(6):
        if k:terminal=bm(first,terminal)
        need(terminal==fc['iterates'][k],'all_fixed_independent_frobenius_iterates')
    fixed_rank('frobenius',terminal,1,fc['elimination']['kernel'])
    actions=[read(D/('test-action-%02d.json'%i)) for i in range(48)]
    stack=[[actions[i][k][j]%2 for i in range(48)] for j in range(48) for k in range(48)]
    ak=read(D/'test-action-kernel.json')
    need(ak['matrix']==stack,'entire_actual_action_stack')
    fixed_rank('action',stack,42,ak['kernel'])
    def fixed_preimage(label,kernel):
        e=read(fixed361/(label+'-independent-preimage.json'));c=read(D/('test-'+label+'-lattice.json'))
        G=tr(kernel+[[2*x for x in row] for row in I]);L=e['basis'];LI=rat(e['inverse'])
        U=e['G_to_basis'];V=e['basis_to_G'];width=48+len(kernel)
        for a,h,w in [(G,48,width),(L,48,48),(U,width,48),(V,48,width)]:shape(a,h,w)
        need(e['kernel_rows']==kernel and e['generators']==c['S']==G and L==c['basis']
            and mm(G,U)==L and mm(L,V)==G and mm(L,LI)==I and mm(LI,L)==I,'whole_fixed_preimage_'+label)
        f=rat(e['saved_basis_in_displayed']);b=rat(e['displayed_basis_in_saved'])
        need(all(F(x).denominator==1 for a in (f,b) for row in a for x in row)
            and mm(L,f)==c['basis'] and mm(c['basis'],b)==L and mm(f,b)==I and mm(b,f)==I,
            'both_integral_fixed_preimage_comparisons_'+label)
        return e
    radical=fixed_preimage('radical',I[1:]);numerator=fixed_preimage('numerator',I[42:])
    need(radical['basis']==WJ,'entire_actual_W_radical_binding')
    for i,A in enumerate(actions):
        shape(A,48,48)
        need(mm(WJ,A)==mm(tr(wt[i]),WJ),'all_saved_full_radical_actions')
    # Distinct filenames protect the input V-to-W interface and its sources.
    for dest,path in [('decision-359.json',fixed359/'test-decision.json'),
        ('decision-361.json',fixed361/'test-decision.json'),
        ('Z-numerator-359.json',fixed359/'test-numerator-lattice.json'),
        ('Z-numerator-361.json',fixed361/'test-numerator-lattice.json'),
        ('Z-independent-multiplier.json',fixed361/'independent-multiplier.json'),
        ('Z-independent-preimage.json',fixed361/'numerator-independent-preimage.json')]:copy(dest,path)
    interface=(fixed361/'successor-interface-body.txt').read_text()
    interface=interface.replace('W-', 'Z-').replace('decision-351.json','decision-359.json').replace('decision-353.json','decision-361.json')
    interface=interface.replace('numerator-351.json','numerator-359.json').replace('numerator-353.json','numerator-361.json')
    interface=interface.replace('>=43','>=42').replace('I[43:]','I[42:]').replace('53','54').replace('==32','==64').replace('==5','==6')
    interface=interface.replace('[(I:I):V] = absolute determinant of V basis in (I:I)',
        '[(I:I):W] = absolute determinant of W basis in (I:I)').replace("vb['identity']","wb['identity']")
    with (D/'new-successor-interface-body.txt').open('x') as f:f.write(interface)
    exec(compile(interface,str(D/'new-successor-interface-body.txt'),'exec'),globals())
    dc=read(D/'decision-359.json');im=read(D/'Z-independent-multiplier.json')
    witness=dc['strict_witness'];strict=im['strict_action']
    shape(strict,48,48)
    need(im['strict_numerator']==I[42] and im['strict_denominator']==2 and witness['column']==42
        and witness['numerator']==I[42] and witness['radical_action']==strict
        and [[2*x for x in row] for row in strict]==actions[42],'full_actual_strict_action_interface')
    # All 377 step-361 fixed bindings agree; generated audit-only artifacts
    # remain read in place, with their original hashes and full equations.
    for n,e in mf361.items():
        if (D/n).is_file():need(digest(D/n)==e['sha256'],'fixed361_fresh_binding_'+n)
    save('new-successor-input-validation.json',{'status':'PASS','failures':[],
        'half_columns':[42,43,44,45,46,47],'index':64,'global_preimages':2,
        'full_fixed_rank_factorizations':2,'all_original_eliminations_replayed':True,
        'all_original_V_and_direct_W_solves_replayed':True,'all_before_production':True,
        'fixed_input_divisions':64512+fixed359_count+fixed361_inputs,
        'fixed_W_action_divisions':original_actions+fixed361_actions,'fresh_W_action_divisions':fresh_actions})

    report['phase']='all_fixed363_actual_dividends_and_copies'
    for n,e in mf363.items():
        need((D/n).is_file() and digest(D/n)==e['sha256'],'every_step363_fresh_copy_binding_'+n)
    fixed363_inputs=sum([divisions('division-',sb,st,folder=fixed363),
        divisions('u-division-',ub,ut,folder=fixed363),divisions('v-division-',vb,vt,folder=fixed363),
        divisions('w-division-',wb,wt,folder=fixed363)])
    fixed363_actions=divisions('test-action-division-',wb,wt,WJ,folder=fixed363,action_prefix='test-')
    need(fixed363_inputs==9216 and fixed363_actions==2304,'all_step363_input_and_action_dividends')
    for n in ['z-basis.json','verify_z.py']+['z-product-%02d.json'%i for i in range(48)]:copy(n,fixed363/n)
    zb=read(D/'z-basis.json');zt=[read(D/('z-product-%02d.json'%i)) for i in range(48)]
    fixed_z=divisions('z-division-',zb,zt,folder=fixed363)
    report['phase']='full_Z_original_H_replay'
    zr=run('verify_z.py','z-verification-report.json')
    for k,x in counts.items():need(zr[k]==x,'full_Z_'+k)
    need(zr['index']==64 and zr['scale']==1984,'actual_Z_index_scale')
    fresh_z=divisions('z-division-',zb,zt)
    report['phase']='independent_direct_Z_six_systems'
    zi=run('Z_reconstruct.py','Z-solve-report.json')
    need(zi['elimination_systems']==6 and zi['inverse_products']==8 and zi['index']==64 and zi['scale']==1984
        and zi['solved_identity_actions']==192 and zi['both_integral_Z_containments']
        and zi['all_scales_derived_from_full_denominator_lcm'],'complete_direct_Z_report')
    save('audit-dividend-report.json',{'status':'PASS','failures':[],
        'fixed_input_divisions':82944+fixed363_inputs,'fixed_W_action_divisions':4608+fixed363_actions,
        'fixed_Z_divisions':fixed_z,'fresh_input_divisions':fresh_s+fresh_u+fresh_v+fresh_w,
        'fresh_W_action_divisions':fresh_actions,'fresh_Z_divisions':fresh_z,
        'all_actual_dividends_checked':True,'all_original_V_and_W_solves_replayed':True})
    for bn,tn,b,t in [('basis.json','product-',sb,st),('u-basis.json','u-product-',ub,ut),
        ('v-basis.json','v-product-',vb,vt),('w-basis.json','w-product-',wb,wt),('z-basis.json','z-product-',zb,zt)]:
        need(read(D/bn)==b and all(read(D/(tn+'%02d.json'%i))==t[i] for i in range(48)),'final_whole_table_'+bn)
    for n,obj in [('z-verification-report.json',zr),('Z-solve-report.json',zi),
        ('test-verification-report.json',fixed_replay)]:need(read(D/n)==obj,'full_final_report_'+n)
    code={p.name:digest(p) for p in D.iterdir() if p.suffix in ('.py','.txt')}
    save('code-hashes.json',code);save('audit-complete-copy-manifest.json',manifest)
    report['phase']='final_preservation'
    audit_after={n:digest(ROOT/n) for n in audit_before}
    copies={n:digest(D/n) for n in manifest};code_after={n:digest(D/n) for n in code}
    need(audit_before==audit_after and code==code_after and all(code[n]==h for n,h in prepared.items())
        and copies=={n:e['sha256'] for n,e in manifest.items()},'whole_preservation')
    preservation={'equal':True,'before':audit_before,'after':audit_after,'code_before':code,'code_after':code_after,
        'fixed_before':{n:e['sha256'] for n,e in manifest.items()},'fixed_after':copies}
    save('preservation-audit.json',preservation)
    for n,obj in [('audit-input-hashes.json',audit_before),('preservation-audit.json',preservation),
        ('code-hashes.json',code),('audit-complete-copy-manifest.json',manifest)]:
        need(read(D/n)==obj,'entire_final_inventory_'+n)
    for n in ['new-successor-input-validation.json','audit-dividend-report.json']:
        r=read(D/n);need(r['status']=='PASS' and not r['failures'],'full_final_evidence_'+n)
    report.update(status='PASS',phase='complete',products=2304,product_slots=110592,index=64,scale=1984,
        original_files=len(audit_before),fixed_copies=len(manifest),source_files=len(code),
        fixed_input_divisions=82944+fixed363_inputs,fixed_W_action_divisions=4608+fixed363_actions,
        fixed_Z_divisions=fixed_z,fresh_input_divisions=fresh_s+fresh_u+fresh_v+fresh_w,
        fresh_W_action_divisions=fresh_actions,fresh_Z_divisions=fresh_z,
        direct_Z_systems=6,all_actual_dividends_checked=True,all_original_V_and_W_systems_replayed=True)
except Exception as exc:
    report.update(status='STOP',failures=[type(exc).__name__+': '+str(exc)])
report.update(seconds=time.monotonic()-BEGAN,required_seconds=180,required_bytes=134217728)
save('stage-report.json',report);print(json.dumps(report));sys.exit(0 if report['status']=='PASS' else 1)
