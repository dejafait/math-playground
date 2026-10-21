"""Prepare and execute one replay-only audit inside the external watchdog."""
from pathlib import Path
import textwrap
D=Path(__file__).resolve().parent
S=D.parent
def change(t,a,b):
    if t.count(a)!=1: raise ValueError('unique_adaptation_'+a[:100])
    return t.replace(a,b)

# No historical stage/wrapper or producer executes.
src=(S/'index-sixty-four-table-363/execution.py').read_text()
boundary="    report['phase']='successor_table_source_adaptation'\n"
if src.count(boundary)!=1: raise ValueError('unique_replay_boundary')
src=src.split(boundary)[0]
src=change(src,'    audit_before={n:digest(ROOT/n) for n in sorted(audit_names)}',"""
    fixed363=S/'index-sixty-four-table-363'
    previous363=read(fixed363/'audit-input-hashes.json')
    need(len(previous363)==8721,'all_8721_step363_originals')
    audit_names.update(previous363)
    audit_names.update(str(p.relative_to(ROOT)) for p in fixed363.rglob('*') if p.is_file())
    audit_names.update(['lemmas/L094-conductor389-index-sixty-four-multiplier-order-table.md',
        'drafts/literature/2026-10-20-index-sixty-four-table-critical-audit.md',
        'drafts/2026-10-20-index-sixty-four-table-critical-audit-attempt.md',
        'history/363-2026-10-20-index64-table.md','history/364-2026-10-20-index64-table-audit-scope.md'])
    audit_before={n:digest(ROOT/n) for n in sorted(audit_names)}""")
src=change(src,'    post361={',"""
    note363='drafts/2026-10-20-index-sixty-four-table-attempt.md'
    a363='206adc232e71da52b5191e7f619869c31a04ea0b80359b2e3c31b8ec6839a1af'
    b363='89a6dfbe3cd544897ed837c6605535464653cf5b1a5bc121e2726abd42dfee40'
    hist363='history/363-2026-10-20-index64-table.md'
    raw363=(ROOT/note363).read_bytes();marker363=b'\\n## Completed execution\\n'
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
    post361={""")
# All original direct W and V certificates remain checked, including 363.
src=change(src,"    with (D/'w_main.txt').open('x') as f:f.write(wmain)",r"""
    wa363="    for c in original361['systems'].values(): reread(c)\n"
    need(wmain.count(wa363)==1,'unique_W363_solve_insertion')
    wmain=wmain.replace(wa363,wa363+
        "    original363=load(S/'index-sixty-four-table-363/W-exact-lattice-certificate.json')\n"+
        "    need(original363==persisted,'entire_original363_W_certificate')\n"+
        "    for c in original363['systems'].values(): reread(c)\n")
    wmain=wmain.replace("['W-table-audit-357','W-two-359','W-two-audit-361']",
        "['W-table-audit-357','W-two-359','W-two-audit-361','index-sixty-four-table-363']")
    with (D/'w_main.txt').open('x') as f:f.write(wmain)""")

# Six independent direct systems: the prefix reconstructs canonical H/b/m/n/s/u/v/w.
zprefix=(S/'index-sixty-four-table-363/W_reconstruct.py').read_text().split(
    '    # All six system inputs above/below are canonical definitions, not saved inverses.\n')[0]
zbody=r'''
    import math
    z=[[x/(2 if j>=42 else 1) for j,x in enumerate(row)] for row in w]
    cert={}
    cert['power']=solve(z,[I[i]+w[i]+[F(i==0)] for i in range(N)])
    x=cert['power']['solution'];inv=[r[:48] for r in x];inc=[r[48:96] for r in x];unit=[r[96] for r in x]
    cert['old_power']=solve(w,[I[i]+[F(i==0)] for i in range(N)])
    oldinv=[r[:48] for r in cert['old_power']['solution']]
    oldunit=[r[48] for r in cert['old_power']['solution']]
    cert['inclusion']=solve(inc,I);invinc=cert['inclusion']['solution']
    cert['b_coordinates']=solve(b,z);B=cert['b_coordinates']['solution']
    cert['b_inverse']=solve(B,I)
    original=load(S/'certificate.json');p=rat(original['matrix']);pz=mul(p,z)
    need(h==original['primitive_integer_factors'][0]
        and [F(x,343) for x in h]==list(map(F,original['h'])),'whole_original_polynomial')
    cert['two_coordinates']=solve(pz,I)
    got=load(D/'z-basis.json');old=load(D/'w-basis.json')
    dec=load(D/'decision-359.json');aud=load(D/'Z-independent-multiplier.json')
    need(dec==load(D/'decision-361.json'),'whole_original_audited_decision')
    for f,r,mat,back in [('basis_to_power','power_to_basis',z,inv),
        ('basis_in_b','b_to_basis',B,cert['b_inverse']['solution']),
        ('to_L067','from_L067',pz,cert['two_coordinates']['solution'])]:
        need(mat==rat(got[f]) and back==rat(got[r]),'all_Z_transports_'+f)
        need(mul(mat,back)==I and mul(back,mat)==I,'both_Z_inverses_'+f)
    need(w==rat(old['basis_to_power']) and oldinv==rat(old['power_to_basis'])
        and mul(w,oldinv)==I and mul(oldinv,w)==I and oldunit==old['identity']==aud['identity'],
        'direct_W_inverse_and_unit')
    need(all(x.denominator==1 for row in inc for x in row),'integral_W_inclusion')
    need(inc==rat(got['old_inclusion'])==rat(dec['inverse'])==rat(aud['inclusion']),'whole_inclusion')
    need(invinc==rat(got['basis_in_w'])==rat(dec['M'])==rat(aud['basis']),'whole_multiplier')
    q=[[2*x for x in row] for row in invinc]
    need(q==dec['numerator']==aud['numerator']==load(D/'Z-numerator-359.json')['basis']
        ==load(D/'Z-numerator-361.json')['basis']==load(D/'Z-independent-preimage.json')['basis'],
        'whole_numerator')
    need(mul(z,inc)==w and mul(w,invinc)==z and mul(inc,invinc)==I and mul(invinc,inc)==I,
        'both_lattice_equations')
    audited=mul(w,rat(aud['basis']))
    forward=mul(inv,audited);reverse=mul(rat(aud['inclusion']),mul(oldinv,z))
    need(all(x.denominator==1 for mat in (forward,reverse) for row in mat for x in row)
        and mul(z,forward)==audited and mul(audited,reverse)==z
        and mul(forward,reverse)==I and mul(reverse,forward)==I,'both_integral_Z_containments')
    need(abs(cert['inclusion']['determinant'])==64==got['index']==dec['index']==aud['determinant'],'index_64')
    need(aud['index_orientation']=='[(I:I):W] = absolute determinant of W basis in (I:I)','orientation')
    need(cert['old_power']['determinant']/cert['power']['determinant']==cert['inclusion']['determinant'],
        'determinant_ratio')
    need(unit==list(map(F,got['identity']))==list(map(F,dec['identity_in_multiplier']))
        ==list(map(F,aud['identity_in_multiplier'])) and all(x.denominator==1 for x in unit)
        and mul(z,[[x] for x in unit])==[[F(i==0)] for i in range(N)],'actual_constant_one')
    scaled={}
    for label,scale,mat in [('m',31,m),('n',62,n),('s',124,s),('u',248,u),('v',496,v),('w',992,w),('z',1984,z)]:
        need(math.lcm(*(x.denominator for row in mat for x in row))==scale,'entire_denominator_lcm_'+label)
        scaled[label]=[[scale*mat[r][j] for r in range(N)] for j in range(N)]
        need(all(x.denominator==1 for row in scaled[label] for x in row),'scaled_integrality_'+label)
    mb=load(S/'radical-overorder-295/basis.json');nb=load(S/'index-two-table-321/basis.json')
    sb=load(D/'basis.json');ub=load(D/'u-basis.json');vb=load(D/'v-basis.json')
    need(a==rat(mb['M']) and scaled['m']==list(map(list,zip(*mul(b,rat(mb['numerator']))))),'original_m_coordinates')
    for label,obj in [('n',nb),('s',sb),('u',ub),('v',vb),('w',old),('z',got)]:
        need(scaled[label]==obj['scaled_polynomials'],'all_scaled_slots_'+label)
        need(obj['original_scale']==31 and obj['enlargement_denominator']==2,'scale_origin_'+label)
    need(nb['scale']==sb['input_scale']==62 and sb['scale']==ub['input_scale']==124
        and ub['scale']==vb['input_scale']==248 and vb['scale']==old['input_scale']==496
        and old['scale']==got['input_scale']==992 and got['scale']==1984
        and ub['prior_scales']==[31,62,124] and vb['prior_scales']==[31,62,124,248]
        and old['prior_scales']==[31,62,124,248,496] and got['prior_scales']==[31,62,124,248,496,992],
        'complete_scale_metadata')
    complete={'systems':cert,'reconstructed':{'b':b,'a':a,'m':m,'n':n,'s':s,'u':u,'v':v,'w':w,'z':z,
        'L067_map':p,'two_coordinates':pz},'scaled':scaled,'identity':unit,'old_identity':oldunit,
        'inclusion':inc,'inverse_inclusion':invinc,'audited_Z':audited,
        'forward_integral_comparison':forward,'reverse_integral_comparison':reverse}
    save('Z-exact-lattice-certificate.json',complete)
    persisted=load(D/'Z-exact-lattice-certificate.json')
    need(persisted==json.loads(json.dumps(complete,default=str)),'entire_Z_certificate_roundtrip')
    for c in persisted['systems'].values():reread(c)
    for prefix,un in [('w-',oldunit),('z-',unit)]:
        table=[load(D/(prefix+'product-%02d.json'%i)) for i in range(N)]
        for i in range(N):
            need([sum(un[j]*table[j][i][k] for j in range(N)) for k in range(N)]==I[i]
                and [sum(un[j]*table[i][j][k] for j in range(N)) for k in range(N)]==I[i],
                'all_direct_unit_actions_'+prefix+str(i))
    save('Z-solve-report.json',{'status':'PASS','failures':[],'elimination_systems':6,
        'transport_entries':13824,'inclusion_entries':4608,'inverse_products':8,'scaled_slots':16128,
        'index':64,'scale':1984,'solved_identity_actions':192,'both_integral_Z_containments':True,
        'complete_certificate_reread':True,'all_scales_derived_from_full_denominator_lcm':True})
if __name__=='__main__':main()
'''
zsource=zprefix+zbody
compile(zsource,str(D/'Z_reconstruct.py'),'exec')
with (D/'Z_reconstruct.py').open('x') as f:f.write(zsource)
src+=r'''
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
'''
compile(src,str(D/'execution.py'),'exec')
with (D/'execution.py').open('x') as f:f.write(src)
exec(compile(src,str(D/'execution.py'),'exec'),globals())
