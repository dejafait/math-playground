"""Full diagonal lattice transport; no polynomial verifier is imported."""
from pathlib import Path
from fractions import Fraction as F
import json,sys,time
sys.set_int_max_str_digits(0)
D=Path(__file__).resolve().parent; START=time.monotonic(); N=48
def read(n):return json.loads((D/n).read_text())
def save(n,x):
    with (D/n).open('x') as f:json.dump(x,f,separators=(',',':'));f.write('\n')
def need(x,s):
    if not x:raise ArithmeticError(s)
def strs(a):return [[str(x) for x in r] for r in a]
report={'status':'STOP','failures':[],'product_slots':0}
try:
    old=read('basis.json'); d=read('decision-335.json')
    a=[1]*45+[2]*3
    mult=[[F(int(i==j),a[j]) for j in range(N)] for i in range(N)]
    inc=[[int(i==j)*a[j] for j in range(N)] for i in range(N)]
    need([[F(x) for x in r] for r in d['M']]==mult and d['inverse']==inc,'full_fixed_lattice')
    basis={'H':old['H'],'scale':248,'original_scale':31,'prior_scales':[31,62,124],
        'input_scale':124,'enlargement_denominator':2,'rank':48,'index':8,
        'basis_in_s':strs(mult),'old_inclusion':inc}
    for f,r in [('basis_in_b','b_to_basis'),('basis_to_power','power_to_basis'),('to_L067','from_L067')]:
        basis[f]=strs([[F(x)/a[j] for j,x in enumerate(row)] for row in old[f]])
        basis[r]=strs([[a[i]*F(x) for x in row] for i,row in enumerate(old[r])])
    power=[[F(x) for x in row] for row in basis['basis_to_power']]
    scaled=[[248*power[i][j] for i in range(N)] for j in range(N)]
    need(all(x.denominator==1 for row in scaled for x in row),'all_scale_248_integral')
    basis['scaled_polynomials']=[[int(x) for x in row] for row in scaled]
    basis['identity']=[a[i]*old['identity'][i] for i in range(N)]
    need(basis['identity']==d['identity_in_multiplier'],'actual_identity')
    save('u-basis.json',basis)
    for i in range(N):
        source=read('product-%02d.json'%i); row=[]
        need(len(source)==N and all(len(c)==N and all(type(x) is int for x in c) for c in source),'full_input_shape')
        for j,c in enumerate(source):
            v=[]
            for k,x in enumerate(c):
                q,r=divmod(x*a[k],a[i]*a[j])
                need(r==0,'nonintegral_product_'+str((i,j,k)));v.append(q)
                report['product_slots']+=1
            row.append(v)
        save('u-product-%02d.json'%i,row)
    report.update(status='PASS',basis_elements=48,products=2304,index=8,scale=248)
except Exception as e:report['failures']=[type(e).__name__+': '+str(e)]
report['seconds']=time.monotonic()-START
save('producer-report.json',report);print(json.dumps(report))
sys.exit(0 if report['status']=='PASS' else 1)
