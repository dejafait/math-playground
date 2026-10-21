"""Prepare the fixed code before the one mathematical execution; no arithmetic run."""
from pathlib import Path
base=Path(__file__).resolve().parent.parent; out=Path(__file__).resolve().parent
def change(s,a,b):
    if s.count(a)!=1: raise ValueError((a[:70],s.count(a)))
    return s.replace(a,b)
extra="""    paths += [R/'lemmas'/name for name in (
        'L067-conductor389-full-seven-torsion-algebra.md','L077-conductor389-nonmonic-starting-order.md',
        'L078-conductor389-first-31-overorder.md','L080-conductor389-changed-order-not-2-maximal.md',
        'L084-conductor389-index-two-multiplier-order-table.md','L085-conductor389-index-two-order-not-2-maximal.md')]
    paths.append(R/'drafts/literature/2026-10-18-index-four-multiplier-table.md')
"""
p=(base/'index-two-table-321/produce.py').read_text()
p=change(p,"'changed-order-two-303','changed-order-two-audit-305'):","'changed-order-two-303','changed-order-two-audit-305',\n                 'index-two-table-321','index-two-table-audit-323',\n                 'index-two-order-two-325','index-four-audit-327'):")
p=change(p,"    return {str(p.relative_to(R)):",extra+"    return {str(p.relative_to(R)):")
p=change(p,"    Q=[[int(i==j)*(1 if i==47 else 2) for j in range(N)] for i in range(N)]", """    oldZ=[[F(int(i==j),2 if i==47 else 1) for j in range(N)] for i in range(N)]
    oldT=[[int(i==j)*(2 if i==47 else 1) for j in range(N)] for i in range(N)]
    need(rat(decision['M'])==oldZ and decision['inverse']==oldT
         and decision['numerator']==[[2*x for x in row] for row in oldZ]
         and decision['index']==2 and decision['decision']=='NOT_2_MAXIMAL','L080_input_identification')
    M=mm(M,oldZ); C=mm(oldT,C)
    prior=read(S/'index-two-table-321/basis.json')
    for f,r,a,z in (('basis_in_b','b_to_basis',M,C),
                   ('basis_to_power','power_to_basis',mm(bp,M),mm(C,pb)),
                   ('to_L067','from_L067',mm(to,M),mm(C,fr))):
        need(rat(prior[f])==a and rat(prior[r])==z and mm(a,z)==U and mm(z,a)==U,'entire_L084_'+f)
    need(prior['identity']==[C[i][0] for i in range(N)] and prior['scale']==62,'L084_identity_scale')
    decision=read(S/'index-two-order-two-325/decision.json')
    need(decision==read(S/'index-four-audit-327/decision.json'),'audited_L085_decision_content')
    Q=[[int(i==j)*(1 if i>=46 else 2) for j in range(N)] for i in range(N)]""")
p=change(p,"\n    T=[[int(i==j)*(2 if i==47 else 1)","\n    T=[[int(i==j)*(2 if i>=46 else 1)")
p=change(p,"and decision['index']==2 and decision['decision']=='NOT_2_MAXIMAL','entire_L080_lattice')", "and decision['index']==4 and decision['determinant']==4\n         and decision['decision']=='NOT_2_MAXIMAL','entire_L085_lattice')")
p=change(p,"scaled=[[62*power[i][j]", "scaled=[[124*power[i][j]")
p=change(p,"'scale':62,'original_scale':31,'enlargement_denominator':2", "'scale':124,'original_scale':31,'input_scale':62,'enlargement_denominator':2")
p=change(p,"'basis_in_m':strs(mult),'old_inclusion':T,'index':2", "'basis_in_n':strs(mult),'old_inclusion':T,'index':4")
p=change(p,"S/'radical-overorder-295'/('product-%02d.json'%i)", "S/'index-two-table-321'/('product-%02d.json'%i)")
p=change(p,"denominator=(2 if i==47 else 1)*(2 if j==47 else 1)", "denominator=(2 if i>=46 else 1)*(2 if j>=46 else 1)")
p=change(p,"divmod(x*(2 if k==47 else 1),denominator)", "divmod(x*(2 if k>=46 else 1),denominator)")
p=change(p,"inverse_pairs=3,identity_actions=96,index=2", "inverse_pairs=4,identity_actions=96,index=4")
v=(base/'index-two-table-321/verify.py').read_text()
v=change(v,"'changed-order-two-303','changed-order-two-audit-305'):","'changed-order-two-303','changed-order-two-audit-305',\n              'index-two-table-321','index-two-table-audit-323',\n              'index-two-order-two-325','index-four-audit-327'):")
v=change(v,"    return {str(p.relative_to(ROOT)):",extra.replace('paths','files').replace("R/","ROOT/")+"    return {str(p.relative_to(ROOT)):")
v=change(v,"    Z=[[Fraction(int(i==j),2 if j==47 else 1) for j in range(48)] for i in range(48)]", """    oldZ=[[Fraction(int(i==j),2 if j==47 else 1) for j in range(48)] for i in range(48)]
    oldT=[[int(i==j)*(2 if j==47 else 1) for j in range(48)] for i in range(48)]
    require(rational(d['M'])==oldZ and d['inverse']==oldT and d['index']==2
            and d['numerator']==[[2*x for x in r] for r in oldZ]
            and d['determinant']==2 and d['decision']=='NOT_2_MAXIMAL','canonical_L080')
    M=matrix(M,oldZ); C=matrix(oldT,C)
    prior=load(SRC/'index-two-table-321/basis.json')
    for f,r,a,z in (('basis_in_b','b_to_basis',M,C),
                   ('basis_to_power','power_to_basis',matrix(bp,M),matrix(C,pb)),
                   ('to_L067','from_L067',matrix(bt,M),matrix(C,bf))):
        require(rational(prior[f])==a and rational(prior[r])==z
                and matrix(a,z)==UNIT and matrix(z,a)==UNIT,'all_L084_'+f)
    require(prior['scale']==62 and prior['original_scale']==31
            and prior['identity']==[C[i][0] for i in range(48)],'L084_scale_identity')
    d=load(SRC/'index-two-order-two-325/decision.json')
    require(d==load(SRC/'index-four-audit-327/decision.json'),'actual_audited_L085_input')
    Z=[[Fraction(int(i==j),2 if j>=46 else 1) for j in range(48)] for i in range(48)]""")
v=change(v,"\n    T=[[int(i==j)*(2 if j==47 else 1)","\n    T=[[int(i==j)*(2 if j>=46 else 1)")
v=change(v,"and d['inverse']==T and d['index']==2 and d['determinant']==2", "and d['inverse']==T and d['index']==4 and d['determinant']==4")
v=change(v,"'audited_L080_entire_multiplier'", "'audited_L085_entire_multiplier'")
v=change(v,"got['basis_in_m']", "got['basis_in_n']")
v=change(v,"(int(i==j)*(2 if i==47 else 1))", "(int(i==j)*(2 if i>=46 else 1))")
v=change(v,"index==got['index']==2", "index==got['index']==4")
v=change(v,"'exact_index_two'", "'exact_index_four'")
v=change(v,"and old['identity_coordinates']==[C[i][0] for i in range(48)]", "and prior['identity']==[C[i][0] for i in range(48)]")
v=change(v,"""    # Original scale 31 is retained: W_i=31m_i and V_i=62n_i.
    W=transpose(matrix(bp,[[31*x for x in row] for row in M]))
    V=[[int(x)*(1 if i==47 else 2) for x in row] for i,row in enumerate(W)]
    require(all(x.denominator==1 for row in W for x in row),'old_scaled_polynomials_integer')
    require(got['H']==H and got['scale']==62 and got['original_scale']==31
            and got['enlargement_denominator']==2 and got['scaled_polynomials']==V
            and transpose(matrix(powers,[[62*x for x in row] for row in UNIT]))==V,'all_scaled_polynomial_slots')""", """    # M now describes n; retain its scale 62 and the original m-scale 31.
    nscaled=transpose(matrix(bp,[[62*x for x in row] for row in M]))
    require(all(x.denominator==1 for row in nscaled for x in row),'input_scaled_polynomials_integer')
    require(nscaled==prior['scaled_polynomials'],'every_input_scale_62_coefficient')
    W=[[x/(1 if i==47 else 2) for x in row] for i,row in enumerate(nscaled)]
    require(all(x.denominator==1 for row in W for x in row),'original_scale_31_retained')
    V=[[int(x)*(1 if i==47 else 2 if i==46 else 4) for x in row] for i,row in enumerate(W)]
    require(got['H']==H and got['scale']==124 and got['original_scale']==31
            and got['input_scale']==62 and got['enlargement_denominator']==2
            and got['scaled_polynomials']==V
            and transpose(matrix(powers,[[124*x for x in row] for row in UNIT]))==V,'all_scaled_polynomial_slots')""")
v=change(v,"        for j,c in enumerate(row):", "        divisions=[]\n        for j,c in enumerate(row):")
v=change(v,"poly[a]-=62*z*x", "poly[a]-=124*z*x")
v=change(v,"            for degree in range(94,47,-1):", "            dividend=poly[:]; quotient=[0]*47\n            for degree in range(94,47,-1):")
v=change(v,"                for a,h in Hnz: poly[degree-48+a]-=q*h", "                quotient[degree-48]=q\n                for a,h in Hnz: poly[degree-48+a]-=q*h")
v=change(v,"            REPORT['product_slots']+=48;", "            divisions.append({'j':j,'dividend':dividend,'quotient':[str(x) for x in quotient],\n                              'remainder':[str(x) for x in poly]})\n            REPORT['product_slots']+=48;")
v=change(v,"        table.append(row)", "        save('division-%02d.json'%i,{'i':i,'products':divisions})\n        table.append(row)")
v=change(v,"transport_entries=13824,\n                  inverse_products=6", "transport_entries=18432,division_certificates=2304,\n                  inverse_products=8")
for name,s in (('produce.py',p),('verify.py',v),('run_once.py',(base/'index-two-order-two-325/run_once.py').read_text())):
    compile(s,str(out/name),'exec')
    with (out/name).open('x') as f: f.write(s)
print('Prepared producer/verifier/watchdog code; no mathematical execution.')
