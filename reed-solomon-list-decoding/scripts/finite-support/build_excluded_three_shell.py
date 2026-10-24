from pathlib import Path
B=Path('scripts/finite-support')

def replace(s,old,new):
    assert old in s, old[:100]
    return s.replace(old,new)

s=(B/'fixed_product_three_shell.py').read_text()
s=replace(s,'included-anchor five/six/seven','excluded-anchor five/six/seven')
s=replace(s,"OUT = B/'fixed-product-three-shell.json'","OUT = B/'fixed-product-excluded-three-shell.json'")
s=replace(s,"'l117-critical-audit.json', 'fixed-product-three-shell-frozen-input.json']","'l117-critical-audit.json', 'fixed-product-three-shell-frozen-input.json',\n             'fixed-product-three-shell.json','fixed-product-three-shell-verification.json','l118-critical-audit.json']")
s=replace(s,"'L117-fixed-product-excluded-five-six-psd.md']]","'L117-fixed-product-excluded-five-six-psd.md',\n        'L118-fixed-product-included-five-six-seven-psd.md']]")
s=replace(s,"('l117-critical-audit.json','critical_audit_l117.py')]:","('l117-critical-audit.json','critical_audit_l117.py'),\n                      ('l118-critical-audit.json','critical_audit_l118.py')]:")
s=replace(s,'    pairs=[(l,m)', '''    anchor=[]
    for l,m in [(0,0)]+[(l,m) for k in (5,6,7) for l,m in [(0,k),(k,0)]]:
        y=c[max(l,m)]
        v=c[l+m]-y
        ck('zero_anchor_'+str((l,m)),v==0)
        anchor.append(dict(layers=[l,m],orbit=[l,m,0,0],h=l+m,
                           pair=enc(c[l+m]),y=enc(y),affine=enc(v),
                           D=g[m] if l==0 else 1))
    pairs=[(l,m)''')
s=replace(s,'                value=((c[l],c[l])', '                y=((c[l],c[l])')
s=replace(s,'                D=choose(l,t)', '''                value=(c[h]-y[1],c[h]-y[0])
                ck('affine_nonnegative_'+str((l,m,t,s)),value[0]>=0)
                if h==0: ck('Boolean_diagonal_'+str(l),value==(1-c[l],)*2)
                D=choose(l,t)''')
s=replace(s,'h=h,D=D,interval=ei(value)', 'h=h,D=D,pair=enc(c[h]),y_interval=ei(y),interval=ei(value)')
s=replace(s,"old=json.loads((B/'fixed-product-coupled.json').read_text())", "old=json.loads((B/'fixed-product-excluded.json').read_text())\n    included=json.loads((B/'fixed-product-three-shell.json').read_text())")
s=replace(s,'            blocks={}; corrections={}', '            blocks={}; corrections={}; pairsums={}; ys={}')
s=replace(s,'''                    corr=c[l]*c[m]*g[l]*g[m] if aa==bb==0 else F(0)
                    blocks[l,m]=add(v,(-corr,-corr)); corrections[l,m]=corr''','''                    pair=sum(beta(68,l,m,aa,t)*beta(956,l,m,bb,s)*c[l+m-t-s]
                             for t,s in entries[l,m])
                    blocks[l,m]=v; corrections[l,m]=F(0); pairsums[l,m]=pair
                    ys[l,m]=(pair-v[1],pair-v[0])
                    corr=c[l]*c[m]*g[l]*g[m] if aa==bb==0 else F(0)
                    raw=tuple(F(*e)+corr for e in included['modes'][8*aa+bb]['blocks'][str(l)+str(m)])
                    ck('recover_included_y_'+str((aa,bb,l,m)),ys[l,m]==raw)''')
s=s.replace('every_L116_block_', 'every_L117_block_').replace('L116_old_', 'L117_old_')
s=replace(s,"q['normalized']==prev['five_normalized']", "q['normalized']==ei(scale(tuple(F(*e) for e in prev['five_normalized']),1/c[5]))")
s=replace(s,"q['normalized']==prev['remainder_normalized']", "q['normalized']==ei(scale(tuple(F(*e) for e in prev['remainder_normalized']),1/c[6]))")
s=replace(s,"                anchor_correction=", "                pair_blocks={str(l)+str(m):enc(v) for (l,m),v in pairsums.items()},\n                y_blocks={str(l)+str(m):ei(v) for (l,m),v in ys.items()},\n                anchor_correction=")
s=replace(s,"'THREE_SHELL_PASSES'", "'EXCLUDED_THREE_SHELL_PASSES'")
s=replace(s,'        entries=records,modes=modes,summary=', '        anchor_cases=anchor,entries=records,modes=modes,summary=')
s=replace(s,"    print('Verdict:'", "    print('Zero anchor cases: 7/7; no included-anchor subtraction')\n    print('Verdict:'")
(B/'fixed_product_excluded_three_shell.py').write_text(s)

s=(B/'verify_fixed_product_three_shell.py').read_text()
s=replace(s,"SOURCE=B/'fixed-product-three-shell.json'", "SOURCE=B/'fixed-product-excluded-three-shell.json'")
s=replace(s,"OUT=B/'fixed-product-three-shell-verification.json'", "OUT=B/'fixed-product-excluded-three-shell-verification.json'")
s=replace(s,"sha(B/'fixed_product_three_shell.py')", "sha(B/'fixed_product_excluded_three_shell.py')")
s=replace(s,"('l117-critical-audit.json','critical_audit_l117.py')]:", "('l117-critical-audit.json','critical_audit_l117.py'),\n                      ('l118-critical-audit.json','critical_audit_l118.py')]:")
s=replace(s,"                values.append(value)\n                presentation.append", """                values.append(value)
                affine=(c[h]-value[1],c[h]-value[0])
                ck('each_presentation_affine',affine[0]>=0 and
                   (h!=0 or affine==(1-c[i],)*2) and
                   (h not in range(1,5) or affine==(F(0),F(0))),[l,m,t,s,order])
                presentation.append""")
s=replace(s,'opposite_pair=enc(c[h]),union_interval=pack(value)', 'opposite_pair=enc(c[h]),union_interval=pack(value),affine_interval=pack(affine)')
s=replace(s,'''            expected=dict(layers=[l,m],intersections=[t,s],h=l+m-t-s,D=D0,interval=pack(values[0]))''', '''            h=l+m-t-s
            affine=(c[h]-values[0][1],c[h]-values[0][0])
            expected=dict(layers=[l,m],intersections=[t,s],h=h,D=D0,pair=enc(c[h]),
                          y_interval=pack(values[0]),interval=pack(affine))''')
s=replace(s,'entry[l,m,t,s]=values[0]', 'entry[l,m,t,s]=affine')
s=replace(s,"old=json.loads((B/'fixed-product-coupled.json').read_text())", "old=json.loads((B/'fixed-product-excluded.json').read_text())\n    included=json.loads((B/'fixed-product-three-shell.json').read_text())")
start=s.index('    anchor=[]\n')
end=s.index('    modes=[];',start)
a=(B/'verify_fixed_product_excluded.py').read_text()
astart=a.index('    anchor=[]\n')
aend=a.index('\n    # Actual complete sets',astart)
anchor=a[astart:aend].replace('[(0,0),(0,5),(5,0),(0,6),(6,0)]', '[(0,0)]+[(l,m) for k in (5,6,7) for l,m in [(0,k),(k,0)]]').replace('len(anchor)==5','len(anchor)==7')
s=s[:start]+anchor+'\n'+s[end:]
s=replace(s,'    trace_anchor={l:F(0) for l in (5,6,7)}\n', '')
s=replace(s,'        blocks={}; corrections={}; poly={}', '        blocks={}; corrections={}; poly={}; pairsums={}; ys={}')
s=replace(s,'; diag=0\n', '; diag=0; pair=F(0)\n')
s=replace(s,'                if h>=5: coeff[h]+=w', '                pair+=w*c[h]\n                if h>=5: coeff[h]-=w')
s=replace(s,'(diag*c[l],)*2)', '(pair-diag*c[l],)*2)')
s=replace(s,'''            correction=c[l]*c[m]*g[l]*g[m] if aa==bb==0 else F(0)
            blocks[l,m]=plus(v,(-correction,-correction)); corrections[l,m]=correction
            poly[l,m]=dict(constant=enc(diag*c[l]),coefficients=coeff)''', '''            blocks[l,m]=v; corrections[l,m]=F(0); pairsums[l,m]=pair
            ys[l,m]=(pair-v[1],pair-v[0])
            correction=c[l]*c[m]*g[l]*g[m] if aa==bb==0 else F(0)
            raw=tuple(F(*e)+correction for e in included['modes'][8*aa+bb]['blocks'][str(l)+str(m)])
            ck('recover_complete_included_y',ys[l,m]==raw,[aa,bb,l,m])
            poly[l,m]=dict(constant=enc(pair-diag*c[l]),coefficients=coeff)''')
s=replace(s,'''                trace_diagonal[l]+=F(multiplicity*diag,D[l])*c[l]
                trace_anchor[l]+=F(multiplicity,D[l])*correction''', '''                trace_diagonal[l]+=F(multiplicity,D[l])*(pair-diag*c[l])''')
s=replace(s,"p['normalized']==previous['five_normalized' if p['layer']==5 else 'remainder_normalized']", "p['normalized']==pack(times(tuple(F(*e) for e in previous['five_normalized' if p['layer']==5 else 'remainder_normalized']),1/c[p['layer']]))")
s=s.replace('L116', 'L117')
s=replace(s,'            anchor_correction=', '            pair_blocks={str(l)+str(m):enc(v) for (l,m),v in pairsums.items()},\n            y_blocks={str(l)+str(m):pack(v) for (l,m),v in ys.items()},\n            anchor_correction=')
start=s.index('        if aa==bb==0:\n')
end=s.index('        # A second PSD certificate:',start)
s=s[:start]+"        ck('no_anchor_subtraction',not any(corrections.values()),[aa,bb])\n"+s[end:]
s=replace(s,'trace_diagonal[l]==g[l]*c[l] and trace_anchor[l]==g[l]*c[l]**2', 'trace_diagonal[l]==g[l]*(1-c[l])')
s=replace(s,"'THREE_SHELL_PASSES'", "'EXCLUDED_THREE_SHELL_PASSES'")
s=replace(s,"        trace_anchor={str(l):enc(v) for l,v in trace_anchor.items()},\n", '')
s=replace(s,'and entire L117 restriction recovered.', 'and entire L117 restriction recovered; zero anchor 7/7.')
# A straddle/negative result must be recorded, not converted to verification failure.
s=replace(s,"    ck('all_positive_pivots_and_minors',", "    if signs['positive']==64:\n        ck('all_positive_pivots_and_minors',")
(B/'verify_fixed_product_excluded_three_shell.py').write_text(s)
