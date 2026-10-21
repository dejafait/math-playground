"""Single approved table construction; all adaptation occurs under watchdog."""
from pathlib import Path
D=Path(__file__).resolve().parent;S=D.parent

def change(t,a,b):
    if t.count(a)!=1:raise ValueError('unique_adaptation_'+a[:90])
    return t.replace(a,b)
def write(n,t):
    compile(t,str(D/n),'exec')
    with (D/n).open('x') as f:f.write(t)

fixed=S/'Z-two-audit-369'
src=(fixed/'execution.py').read_text()
extra='''
    fixed369=S/'Z-two-audit-369'
    previous369=read(fixed369/'audit-input-hashes.json')
    need(len(previous369)==11201,'all_11201_step369_originals')
    audit_names.update(previous369)
    audit_names.update(str(p.relative_to(ROOT)) for p in fixed369.rglob('*') if p.is_file())
    audit_names.update(['drafts/literature/2026-10-20-index-128-multiplier-table.md',
        'drafts/2026-10-20-index-128-table-attempt.md',
        'history/369-2026-10-20-Z-two-critical-audit.md',
        'history/370-2026-10-20-index-128-table-source-review.md'])
    audit_before={n:digest(ROOT/n) for n in sorted(audit_names)}
    transitions369={
      'lemmas/L095-conductor389-index-sixty-four-order-not-2-maximal.md':
      ('14dc7b33b8b4a3b09c74c691a7ca061d7987cc82481f0938cd7f3db64f271e69','41804c86ec67883bf39cb356053ae0979592258a08de0dedf93258b09cb389c4'),
      'drafts/2026-10-20-Z-two-critical-audit-attempt.md':
      ('c7e33fcd3523124b7e508e03b2b0b28700a1c55776f67376ad1ccd531062d25a','9f3ea09617e9acf5dbfc54b1f82c8bbcea6f4ec91db0b2b48e44de537a2a73c9')}
    hist369='history/369-2026-10-20-Z-two-critical-audit.md'
    need(audit_before[hist369]=='c5a64f0e2c9b448bb56474b858bbca6c929cb5b59449271707b9a7616b727118','exact_history369')
    for n,(a,b) in transitions369.items():
        need(previous369[n]==a and audit_before[n]==b and a in (ROOT/hist369).read_text()
            and b in (ROOT/hist369).read_text(),'exact_post369_transition_'+n)
    note369='drafts/2026-10-20-Z-two-critical-audit-attempt.md'
    raw369=(ROOT/note369).read_bytes();mark369=b'\\n## Completed execution\\n'
    need(raw369.count(mark369)==1 and hashlib.sha256(raw369.split(mark369)[0][:-1]).hexdigest()==transitions369[note369][0],
        'exact_post369_note_prefix_excluding_separator')
    need(all(audit_before[n]==h for n,h in previous369.items() if n not in transitions369),'all_other_step369_originals')
    mf369=read(fixed369/'audit-complete-copy-manifest.json');need(len(mf369)==488,'all_488_step369_copies')
    for n,e in mf369.items():
        need(audit_before[e['source']]==e['sha256']==audit_before[str((fixed369/n).relative_to(ROOT))],
            'whole_fixed369_binding_'+n)
    cd369=read(fixed369/'code-hashes.json');need(len(cd369)==22,'all_22_step369_sources')
    need(all(digest(fixed369/n)==h for n,h in cd369.items()),'all_step369_source_hashes')
    save('post369-transition.json',{'exact_changes':transitions369,'history':hist369,
        'history_sha256':audit_before[hist369],'every_other_original_unchanged':True})
'''
src=change(src,'    audit_before={n:digest(ROOT/n) for n in sorted(audit_names)}',extra)
# Extend both direct-system comparisons to the original step-369 copies.
src=change(src,"    with (D/'w_main.txt').open('x') as f:f.write(wmain)",'''
    wa369="    for c in original367['systems'].values(): reread(c)\\n"
    wmain=change(wmain,wa369,wa369+
        "    original369=load(S/'Z-two-audit-369/W-exact-lattice-certificate.json')\\n"+
        "    need(original369==persisted,'entire_original369_W_certificate')\\n"+
        "    for c in original369['systems'].values(): reread(c)\\n")
    wmain=change(wmain,"'Z-two-367']","'Z-two-367','Z-two-audit-369']")
    with (D/'w_main.txt').open('x') as f:f.write(wmain)
''')
z=(fixed/'Z_reconstruct.py').read_text()
z=change(z,"    for c in original367['systems'].values():reread(c)",
    "    for c in original367['systems'].values():reread(c)\n"+
    "    original369=load(S/'Z-two-audit-369/Z-exact-lattice-certificate.json')\n"+
    "    need(original369==persisted,'entire_original369_Z_certificate')\n"+
    "    for c in original369['systems'].values():reread(c)")
write('Z_reconstruct.py',z)
write('independent.py',(fixed/'independent.py').read_text())
addition='''
    report['phase']='entire_step369_evidence_and_seven_column_interface'
    count369=sum(divisions(p,b,t,folder=fixed369) for p,b,t in [
        ('division-',sb,st),('u-division-',ub,ut),('v-division-',vb,vt),
        ('w-division-',wb,wt),('z-division-',zb,zt)])
    count369+=divisions('test-action-division-',wb,wt,WJ,folder=fixed369,action_prefix='test-')
    count369+=divisions('ztest-action-division-',zb,zt,ZJ,folder=fixed369,action_prefix='ztest-')
    need(count369==16128,'all_16128_step369_fresh_actual_dividends')
    for n in ['frobenius-full-rank.json','action-full-rank.json','radical-independent-preimage.json',
        'numerator-independent-preimage.json','independent-multiplier.json']:
        need(read(D/n)==read(fixed369/n),'whole_original369_independent_certificate_'+n)
    for n in coreZ:need(read(D/n)==read(fixed369/n),'whole_original369_Z_interface_'+n)
    for dest,path in [('decision-367.json',fixed367/'ztest-decision.json'),
        ('decision-369.json',fixed369/'ztest-decision.json'),
        ('AA-numerator-367.json',fixed367/'ztest-numerator-lattice.json'),
        ('AA-numerator-369.json',fixed369/'ztest-numerator-lattice.json'),
        ('AA-independent-multiplier.json',fixed369/'independent-multiplier.json'),
        ('AA-independent-preimage.json',fixed369/'numerator-independent-preimage.json')]:copy(dest,path)
    interface=(fixed369/'successor-interface-body.txt').read_text()
    interface=interface.replace('W-','AA-').replace('decision-351.json','decision-367.json').replace('decision-353.json','decision-369.json')
    interface=interface.replace('numerator-351.json','numerator-367.json').replace('numerator-353.json','numerator-369.json')
    interface=interface.replace('>=43','>=41').replace('I[43:]','I[41:]').replace('53','55').replace('==32','==128').replace('==5','==7')
    interface=interface.replace('[(I:I):V] = absolute determinant of V basis in (I:I)',
        '[(I:I):Z] = absolute determinant of Z basis in (I:I)').replace("vb['identity']","zb['identity']")
    with (D/'AA-interface-body.txt').open('x') as f:f.write(interface)
    exec(compile(interface,str(D/'AA-interface-body.txt'),'exec'),globals())
    save('AA-input-validation.json',{'status':'PASS','failures':[],
        'half_columns':list(range(41,48)),'index':128,'original_input_divisions':147456,
        'step369_divisions':count369,'full_global_preimages':2,'all_before_production':True})
    report['phase']='successor_table_source_adaptation'
    p=(S/'index-sixty-four-table-363/produce_z.py').read_text()
    p=p.replace("old=read('w-basis.json'); d=read('decision-359.json')","old=read('z-basis.json'); d=read('decision-367.json')")
    p=p.replace('[1]*42+[2]*6','[1]*41+[2]*7').replace("'basis_in_w'","'basis_in_z'")
    p=p.replace("source=read('w-product-","source=read('z-product-").replace("save('z-","save('aa-")
    p=p.replace("'scale':1984","'scale':3968").replace("'input_scale':992","'input_scale':1984")
    p=p.replace("'prior_scales':[31,62,124,248,496,992]","'prior_scales':[31,62,124,248,496,992,1984]")
    p=p.replace("'index':64","'index':128").replace('1984*power','3968*power').replace('scale_1984','scale_3968')
    p=p.replace('index=64,scale=1984','index=128,scale=3968').replace('producer-report.json','aa-producer-report.json')
    v=(S/'index-sixty-four-table-363/verify_z.py').read_text()
    v=v.replace("old=read('w-basis.json'); got=read('z-basis.json')","old=read('z-basis.json'); got=read('aa-basis.json')")
    v=v.replace('decision-359.json','decision-367.json').replace('decision-361.json','decision-369.json')
    v=v.replace('Z-independent-multiplier.json','AA-independent-multiplier.json').replace('>=42','>=41').replace('==64','==128')
    v=v.replace("d['kernel_dimension']==6","d['kernel_dimension']==7").replace("got['basis_in_w']","got['basis_in_z']")
    v=v.replace('[(I:I):W] = absolute determinant of W basis in (I:I)','[(I:I):Z] = absolute determinant of Z basis in (I:I)')
    v=change(v,"old['scale']==992 and old['original_scale']==31 and old['input_scale']==496\\n        and got['scale']==1984 and got['input_scale']==992",
        "old['scale']==1984 and old['original_scale']==31 and old['input_scale']==992\\n        and got['scale']==3968 and got['input_scale']==1984")
    v=v.replace("got['prior_scales']==[31,62,124,248,496,992]","got['prior_scales']==[31,62,124,248,496,992,1984]")
    v=v.replace('==1984,\'reconstructed_actual_scale','==3968,\'reconstructed_actual_scale')
    v=v.replace('F(1984*','F(3968*').replace('poly[a]-=1984*z*x','poly[a]-=3968*z*x')
    v=v.replace("read('z-product-","read('aa-product-").replace("save('z-division-","save('aa-division-")
    v=v.replace('scale=1984','scale=3968').replace('z-verification-report.json','aa-verification-report.json')
    for n,t in [('produce_aa.py',p),('verify_aa.py',v)]:
        compile(t,str(D/n),'exec')
        with (D/n).open('x') as f:f.write(t)
    report['phase']='one_full_index128_table_production'
    ap=run('produce_aa.py','aa-producer-report.json')
    need(ap['products']==2304 and ap['product_slots']==110592 and ap['index']==128 and ap['scale']==3968,'full_AA_production')
    report['phase']='independent_AA_original_H_replay'
    av=run('verify_aa.py','aa-verification-report.json')
    need(av['product_slots']==110592 and av['product_identities']==2304 and av['inverse_products']==8
        and av['transport_entries']==18432 and av['identity_actions']==96 and av['index']==128
        and av['scale']==3968,'full_AA_independent_replay')
    ab=read(D/'aa-basis.json');at=[read(D/('aa-product-%02d.json'%i)) for i in range(48)]
    ad=divisions('aa-division-',ab,at);need(ad==2304,'all_actual_AA_dividends_reread')
    save('AA-complete-table-report.json',{'status':'PASS','failures':[],
        'products':2304,'integer_slots':110592,'new_divisions':ad,'original_input_divisions':147456,
        'scale':3968,'index':128,'half_columns':list(range(41,48))})
    for n,obj in [('aa-basis.json',ab),('aa-producer-report.json',ap),('aa-verification-report.json',av)]:
        need(read(D/n)==obj,'whole_final_AA_evidence_'+n)
    need(all(read(D/('aa-product-%02d.json'%i))==at[i] for i in range(48)),'all_final_AA_products')
'''
anchor="    code={p.name:digest(p) for p in D.iterdir() if p.suffix in ('.py','.txt')}\n"
src=change(src,anchor,addition+anchor)
src=change(src,"report.update(status='PASS',phase='complete',products=2304,product_slots=110592,index=64,scale=1984,",
    "report.update(status='PASS',phase='complete',products=2304,product_slots=110592,index=128,scale=3968,")
write('execution.py',src)
exec(compile(src,str(D/'execution.py'),'exec'),globals())
