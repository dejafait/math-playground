"""Independent W replay in original H; imports no producer arithmetic."""
from pathlib import Path
from fractions import Fraction as F
import json,math,sys,time
sys.set_int_max_str_digits(0)
D=Path(__file__).resolve().parent; START=time.monotonic(); N=48
I=[[int(i==j) for j in range(N)] for i in range(N)]
def read(n):return json.loads((D/n).read_text())
def save(n,x):
    with (D/n).open('x') as f:json.dump(x,f,separators=(',',':'));f.write('\n')
def need(x,s):
    if not x:raise ArithmeticError(s)
def shape(a,n,m,ints=False):
    need(type(a) is list and len(a)==n and all(type(r) is list and len(r)==m for r in a),'full_shape')
    if ints:need(all(type(x) is int for r in a for x in r),'all_integer_types')
def rat(a):
    shape(a,N,N);need(all(type(x) in (str,int) for r in a for x in r),'no_floats')
    return [[F(x) for x in r] for r in a]
def mm(a,b):
    out=[[0]*len(b[0]) for _ in a]
    for k,row in enumerate(b):
        for j,x in enumerate(row):
            if x:
                for i in range(len(a)):
                    if a[i][k]:out[i][j]+=a[i][k]*x
    return out
report={'status':'STOP','failures':[],'product_slots':0,'product_identities':0,
    'remainder_coefficients':0,'rational_quotient_steps':0}
try:
    old=read('v-basis.json'); got=read('w-basis.json'); d=read('decision-351.json')
    need(d==read('decision-353.json'),'both_entire_fixed_decisions')
    independent=read('W-independent-multiplier.json')
    M=[[F(int(i==j),2 if j>=43 else 1) for j in range(N)] for i in range(N)]
    T=[[int(i==j)*(2 if j>=43 else 1) for j in range(N)] for i in range(N)]
    Q=[[2*x for x in r] for r in M]
    need(rat(d['M'])==M and d['inverse']==T and d['numerator']==Q
        and d['index']==d['determinant']==32 and d['kernel_dimension']==5
        and d['decision']=='NOT_2_MAXIMAL','entire_audited_W')
    need(rat(independent['basis'])==M and independent['numerator']==Q
        and independent['inclusion']==T and independent['determinant']==32
        and independent['index_orientation']=='[(I:I):V] = absolute determinant of V basis in (I:I)',
        'full_separately_audited_W')
    need(rat(got['basis_in_v'])==M and got['old_inclusion']==T
        and mm(M,T)==I and mm(T,M)==I,'both_multiplier_inclusion_inverses')
    transport_entries=2*N*N;inverse_products=2; matrices={}
    for f,r in [('basis_in_b','b_to_basis'),('basis_to_power','power_to_basis'),('to_L067','from_L067')]:
        left=rat(old[f]);right=rat(old[r]);expected=mm(left,M);back=mm(T,right)
        actual=rat(got[f]);actualback=rat(got[r])
        need(actual==expected and actualback==back,'every_transport_entry_'+f)
        need(mm(actual,actualback)==I and mm(actualback,actual)==I,'both_inverse_products_'+f)
        need(mm(actual,T)==left and mm(M,actualback)==right,'entire_old_lattice_'+f)
        matrices[f]=actual;matrices[r]=actualback
        transport_entries+=2*N*N;inverse_products+=2
    shape(T,N,N,True)
    need(all(T[i][j]==int(i==j)*(2 if i>=43 else 1) for i in range(N) for j in range(N)),
        'entire_diagonal_inclusion')
    index=math.prod(T[i][i] for i in range(N))
    need(index==got['index']==32 and got['rank']==48,'exact_index_thirty_two_orientation')
    identity=[sum(T[i][j]*old['identity'][j] for j in range(N)) for i in range(N)]
    need(all(type(x) is int for x in identity) and got['identity']==identity==d['identity_in_multiplier']
        and independent['identity']==old['identity'] and independent['identity_in_multiplier']==identity,'actual_integral_identity')
    one=[[int(i==0)] for i in range(N)]
    need(mm(matrices['basis_to_power'],[[x] for x in identity])==one,'unit_in_original_field')
    H=old['H'];shape([H],1,49,True)
    need(H[-1]==343 and math.gcd(*H)==1 and got['H']==H,'original_nonmonic_H')
    need(old['scale']==496 and old['original_scale']==31 and old['input_scale']==248
        and got['scale']==992 and got['input_scale']==496 and got['original_scale']==31
        and got['prior_scales']==[31,62,124,248,496] and got['enlargement_denominator']==2,'every_scale_retained')
    V=[]
    for j in range(N):
        column=[F(992*matrices['basis_to_power'][i][j]) for i in range(N)]
        need(all(x.denominator==1 for x in column),'exact_integral_original_H_representatives')
        V.append([int(x) for x in column])
    shape(got['scaled_polynomials'],N,N,True)
    need(V==got['scaled_polynomials'],'all_2304_scaled_coefficients')
    need(V==[[int(F(2*x,2 if j>=43 else 1)) for x in row]
             for j,row in enumerate(old['scaled_polynomials'])],'full_scale_transport')
    table=[];Hnz=[(k,x) for k,x in enumerate(H) if x]
    for i in range(N):
        row=read('w-product-%02d.json'%i);shape(row,N,N,True);divisions=[]
        for j,c in enumerate(row):
            poly=[0]*95
            for a,x in enumerate(V[i]):
                for b,y in enumerate(V[j]):
                    if x and y:poly[a+b]+=x*y
            for k,z in enumerate(c):
                if z:
                    for a,x in enumerate(V[k]):
                        if x:poly[a]-=992*z*x
            dividend=poly[:];qout=[0]*47
            for degree in range(94,47,-1):
                x=poly[degree]
                if not x:continue
                if type(x) is int:
                    q,r=divmod(x,343)
                    if r:q=F(x,343);report['rational_quotient_steps']+=1
                else:q=F(x,343);report['rational_quotient_steps']+=1
                qout[degree-48]=q
                for k,h in Hnz:poly[degree-48+k]-=q*h
            need(not any(poly),'full_original_H_remainder_'+str((i,j)))
            divisions.append({'j':j,'dividend':dividend,'quotient':[str(x) for x in qout],
                'remainder':[str(x) for x in poly]})
            report['product_slots']+=48;report['product_identities']+=1;report['remainder_coefficients']+=95
        save('w-division-%02d.json'%i,{'i':i,'products':divisions});table.append(row)
    for i in range(N):
        left=[sum(identity[j]*table[j][i][k] for j in range(N)) for k in range(N)]
        right=[sum(identity[j]*table[i][j][k] for j in range(N)) for k in range(N)]
        need(left==I[i] and right==I[i],'actual_both_identity_actions_'+str(i))
    report.update(status='PASS',transport_entries=transport_entries,inverse_products=inverse_products,
        identity_actions=96,index=index,division_certificates=2304,scale=992,basis_elements=48)
except Exception as e:report['failures']=[type(e).__name__+': '+str(e)]
report['seconds']=time.monotonic()-START
save('w-verification-report.json',report);print(json.dumps(report))
sys.exit(0 if report['status']=='PASS' else 1)
