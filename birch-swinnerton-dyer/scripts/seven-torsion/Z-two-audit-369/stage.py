"""One replay-only audit; adaptations occur under the encompassing watchdog."""
from pathlib import Path
D=Path(__file__).resolve().parent; S=D.parent
def change(t,a,b):
    if t.count(a)!=1: raise ValueError('unique_adaptation_'+a[:100])
    return t.replace(a,b)
def write(n,t):
    compile(t,str(D/n),'exec')
    with (D/n).open('x') as f:f.write(t)

src=(S/'Z-two-367/execution.py').read_text()
# Retain only the inspected replay, removing the entire production block.
start="    report['phase']='new_Z_source_specialization'\n"
end="    code={p.name:digest(p) for p in D.iterdir() if p.suffix in ('.py','.txt')}\n    save('code-hashes.json',code);save('audit-complete-copy-manifest.json',manifest)"
if src.count(start)!=1 or src.count(end)!=1:raise ValueError('unique_production_exclusion')
a,b=src.split(start); discarded,c=b.split(end)
src=a+'''    report['phase']='fixed367_full_dividends_and_Z_replay'
    for n,e in mf367.items():
        need((D/n).is_file() and digest(D/n)==e['sha256'],'all_fixed367_copy_bindings_'+n)
    fixed367_inputs=sum([divisions('division-',sb,st,folder=fixed367),
        divisions('u-division-',ub,ut,folder=fixed367),
        divisions('v-division-',vb,vt,folder=fixed367),
        divisions('w-division-',wb,wt,folder=fixed367)])
    fixed367_w=divisions('test-action-division-',wb,wt,WJ,folder=fixed367,action_prefix='test-')
    fixed367_z=divisions('z-division-',zb,zt,folder=fixed367)
    need(fixed367_inputs==9216 and fixed367_w==fixed367_z==2304,'all_fixed367_input_divisions')
    need(read(fixed367/'ztest-input-validation.json')==read(D/'ztest-input-validation.json'),
        'whole_fixed367_input_validation')
    coreZ=['ztest-'+n+'.json' for n in ['input-basis','frobenius','radical-lattice',
        'action-kernel','numerator-lattice','decision']]
    coreZ+=['ztest-action-%02d.json'%i for i in range(48)]
    for n in coreZ+['Z_verify.py']:copy(n,fixed367/n)
    ZJ=read(D/'ztest-radical-lattice.json')['basis']
    fixed367_actions=divisions('ztest-action-division-',zb,zt,ZJ,folder=fixed367,action_prefix='ztest-')
    need(fixed367_actions==2304,'all_original_Z_actual_dividends')
    verifier=run('Z_verify.py','ztest-verification-report.json')
    for k,x in {'input_product_slots':110592,'action_slots':110592,'frobenius_slots':13824,
        'frobenius_iterates':6,'exponent':64,'prime':2,'frobenius_rank':1,
        'radical_dimension':47,'action_rank':41,'action_kernel_dimension':7,'index':128,
        'action_division_certificates':2304,'decision':'NOT_2_MAXIMAL'}.items():
        need(verifier[k]==x,'actual_Z_replay_'+k)
    fresh_Z_actions=divisions('ztest-action-division-',zb,zt,ZJ,action_prefix='ztest-')
    need(fresh_Z_actions==2304,'all_fresh_Z_actual_dividends')
    oldver=read(fixed367/'ztest-verification-report.json')
    need({k:v for k,v in oldver.items() if k not in ('seconds','original_files')}==
        {k:v for k,v in verifier.items() if k not in ('seconds','original_files')},
        'entire_original_Z_verifier_arithmetic_report')
    report['phase']='independent_actual_Z_ranks_and_global_preimages'
    supplement=run('independent.py','independent-report.json')
    need(supplement['action_rank']==41 and supplement['index']==128
        and supplement['independent_preimages']==2,'independent_full_Z_result')
    save('Z-audit-obligations.json',{'status':'PASS','failures':[],
        'original_division_identities':131328,'fresh_division_identities':16128,
        'total_division_identities':147456,'original_step367_input_divisions':fixed367_inputs+fixed367_w+fixed367_z,
        'original_Z_action_divisions':fixed367_actions,'fresh_Z_action_divisions':fresh_Z_actions,
        'full_rank_factorizations':2,'global_preimages':2,'rank':41,'index':128,
        'all_original_V_W_Z_systems_replayed':True,'producer_executed':False})
    report.update(Z_decision=verifier['decision'],Z_multiplier_index=128,Z_frobenius_rank=1,
        Z_action_rank=41,Z_action_kernel_dimension=7,original_division_identities=131328,
        fresh_division_identities=16128,independent_full_preimages=2)
'''+end+c
src=change(src,'    audit_before={n:digest(ROOT/n) for n in sorted(audit_names)}', '''
    fixed367=S/'Z-two-367'
    previous367=read(fixed367/'audit-input-hashes.json')
    need(len(previous367)==10298,'all_10298_step367_originals')
    audit_names.update(previous367)
    audit_names.update(str(p.relative_to(ROOT)) for p in fixed367.rglob('*') if p.is_file())
    audit_names.update(['lemmas/L095-conductor389-index-sixty-four-order-not-2-maximal.md',
        'drafts/literature/2026-10-20-Z-two-critical-audit.md',
        'drafts/2026-10-20-Z-two-critical-audit-attempt.md',
        'history/367-2026-10-20-Z-two-index128.md',
        'history/368-2026-10-20-Z-two-audit-source-comparison.md'])
    audit_before={n:digest(ROOT/n) for n in sorted(audit_names)}
    note367='drafts/2026-10-20-Z-two-attempt.md'
    old367='8a3458ba941d026487d80403993abb2aec38cdef09813c239256ca6498574252'
    new367='08035b536945bf1a945aea7ab807566e02a4a12932b4a5da7dc4c36256fdf308'
    hist367='history/367-2026-10-20-Z-two-index128.md'
    raw367=(ROOT/note367).read_bytes(); mark367=b'\\n## Completed execution\\n'
    need(previous367[note367]==old367 and audit_before[note367]==new367
        and raw367.count(mark367)==1 and hashlib.sha256(raw367.split(mark367)[0]).hexdigest()==old367
        and audit_before[hist367]=='67906a0b2407bc8bf8122aede10fd8dd48fed6f6bde477531623948d2f17a224'
        and old367 in (ROOT/hist367).read_text() and new367 in (ROOT/hist367).read_text(),
        'exact_post367_unique_append_bound_to_inventory_history')
    need(all(audit_before[n]==h for n,h in previous367.items() if n!=note367),'all_other_step367_originals')
    mf367=read(fixed367/'audit-complete-copy-manifest.json')
    need(len(mf367)==433,'all_433_step367_copy_bindings')
    for n,e in mf367.items():
        need(audit_before[e['source']]==e['sha256']==audit_before[str((fixed367/n).relative_to(ROOT))],
            'original_fixed367_binding_'+n)
    cd367=read(fixed367/'code-hashes.json');need(len(cd367)==22,'all_22_step367_sources')
    need(all(digest(fixed367/n)==h for n,h in cd367.items()),'all_step367_source_hashes')
    save('post367-transition.json',{'path':note367,'prior':old367,'current':new367,
        'history':hist367,'history_sha256':audit_before[hist367],'all_other_originals_unchanged':True})
''')
# Extend direct solve replay through every step-367 copy.
src=change(src,"    with (D/'w_main.txt').open('x') as f:f.write(wmain)",'''
    anchor367="    for c in original365['systems'].values(): reread(c)\\n"
    wmain=change(wmain,anchor367,anchor367+
        "    original367=load(S/'Z-two-367/W-exact-lattice-certificate.json')\\n"+
        "    need(original367==persisted,'entire_original367_W_certificate')\\n"+
        "    for c in original367['systems'].values(): reread(c)\\n")
    wmain=change(wmain,"['W-table-audit-357','W-two-359','W-two-audit-361','index-sixty-four-table-363','Z-table-audit-365']",
        "['W-table-audit-357','W-two-359','W-two-audit-361','index-sixty-four-table-363','Z-table-audit-365','Z-two-367']")
    with (D/'w_main.txt').open('x') as f:f.write(wmain)
''')
z=(S/'Z-two-367/Z_reconstruct.py').read_text()
z=change(z,"    for c in original365['systems'].values():reread(c)",
    "    for c in original365['systems'].values():reread(c)\n"+
    "    original367=load(S/'Z-two-367/Z-exact-lattice-certificate.json')\n"+
    "    need(original367==persisted,'entire_original367_Z_certificate')\n"+
    "    for c in original367['systems'].values():reread(c)")
write('Z_reconstruct.py',z)

ind=(S/'V-two-audit-353/independent.py').read_text()
ind=ind.replace("v-product-","z-product-")
ind=ind.replace("D/(label+'-lattice.json')","D/('ztest-'+label+'-lattice.json')")
for n in ['frobenius','action-kernel','decision','input-basis']:
    ind=ind.replace("D/'"+n+".json'","D/'ztest-"+n+".json'")
ind=ind.replace("D/('action-%02d.json'%i)","D/('ztest-action-%02d.json'%i)")
ind=ind.replace('43','41').replace('[1]*5','[1]*7').replace('==32','==128')
ind=ind.replace('index=32','index=128').replace('action_kernel_dimension=5','action_kernel_dimension=7')
ind=ind.replace('496*int','1984*int').replace('[(I:I):V]','[(I:I):Z]')
ind=ind.replace('of V basis','of Z basis').replace('thirty_two','one_hundred_twenty_eight')
ind=ind.replace('action_left_inverse_entries=99072','action_left_inverse_entries=94464')
ind=ind.replace('selected_inverse_entries=1849','selected_inverse_entries=1681')
ind=change(ind,"    for _ in range(5):terminal=bm(first,terminal)\n    fc=read(D/'ztest-frobenius.json')",
    "    fc=read(D/'ztest-frobenius.json')\n"+
    "    for k in range(6):\n"+
    "        if k:terminal=bm(first,terminal)\n"+
    "        need(terminal==fc['iterates'][k],'each_independent_frobenius_iterate')\n")
write('independent.py',ind)
write('execution.py',src)
exec(compile(src,str(D/'execution.py'),'exec'),globals())
