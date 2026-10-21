"""Independent full polynomial replay. No producer imports or table transport."""
from pathlib import Path
from fractions import Fraction
import hashlib, json, math, sys, time
sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[2]; SRC=ROOT/'scripts/seven-torsion'
BEGAN=time.monotonic(); CAP=134217728
UNIT=[[int(i==j) for j in range(48)] for i in range(48)]
REPORT={'status':'INCOMPLETE','phase':'inputs','product_slots':0,'product_identities':0,
        'remainder_coefficients':0,'rational_quotient_steps':0,'failures':[]}
def require(ok,label):
    if not ok: raise ValueError(label)
def load(p): return json.loads(p.read_text())
def save(name,data):
    raw=(json.dumps(data,separators=(',',':'))+'\n').encode()
    require(sum(p.stat().st_size for p in HERE.rglob('*') if p.is_file())+len(raw)+65536<=CAP,'artifact_cap')
    with (HERE/name).open('xb') as f: f.write(raw)
def rational(a): return [[Fraction(x) for x in r] for r in a]
def transpose(a): return [list(r) for r in zip(*a)]
def matrix(a,b):
    out=[[0]*len(b[0]) for _ in a]
    for k,row in enumerate(b):
        for i in range(len(a)):
            if a[i][k]:
                for j,y in enumerate(row):
                    if y: out[i][j]+=a[i][k]*y
    return out
def shape(a,n,m,integer=False):
    require(len(a)==n and all(len(r)==m for r in a),'complete_matrix_shape')
    if integer: require(all(type(x) is int for r in a for x in r),'integer_slots')
def inventory():
    expected=load(HERE/'canonical-input-hashes.json')
    return {name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in expected}

def main():
    before=inventory(); require(before==load(HERE/'canonical-input-hashes.json'),'exact_original_inputs')
    original=load(SRC/'certificate.json'); b=load(SRC/'nonmonic-order-283/basis.json')
    old=load(SRC/'radical-overorder-295/basis.json'); d=load(SRC/'changed-order-two-303/decision.json')
    got=load(HERE/'basis.json'); H=b['H']
    shape([H],1,49,True)
    require(H[-1]==343 and math.gcd(*H)==1 and H==original['primitive_integer_factors'][0]
            and [Fraction(x,343) for x in H]==list(map(Fraction,original['h'])),'full_original_H')
    bp=[[0]*48 for _ in range(48)]; bp[0][0]=1
    for j in range(1,48):
        for i in range(j+1): bp[i][j]=H[48-j+i]
    require(b['basis']==transpose(bp) and b['basis_to_power']==bp,'every_original_basis_coefficient')
    pb=rational(b['power_to_basis']); shape(pb,48,48)
    require(matrix(bp,pb)==UNIT and matrix(pb,bp)==UNIT,'original_both_power_inverses')
    lmat=rational(original['matrix']); linv=rational(original['inverse'])
    shape(lmat,48,48); shape(linv,48,48)
    require(matrix(lmat,linv)==UNIT and matrix(linv,lmat)==UNIT,'L067_both_inverse_products')
    bt=matrix(lmat,bp); bf=matrix(pb,linv)
    require(rational(b['basis_to_L067'])==bt and rational(b['L067_to_basis'])==bf,'original_L067_transports')
    # Reconstruct L078 independently from its explicit canonical full basis.
    even=[1,20,25,8,10,28,4,5,14,2,18,7,1,9,19,16,20,25,8,10,28,4,5,14]
    odd=[1,9,19,16,20,25,8,10,28,4,5,14,2,18,7,1,9,19,16,20,25,8,10,28]
    M=[[Fraction(x) for x in row] for row in UNIT]
    for i in range(48):
        M[i][0]=Fraction(even[i//2] if i%2==0 else 0,31)
        M[i][1]=Fraction(odd[i//2] if i%2 else 0,31)
    C=rational(old['inverse']); shape(C,48,48)
    require(M==rational(old['M']) and [[31*x for x in r] for r in M]==old['numerator']
            and matrix(M,C)==UNIT and matrix(C,M)==UNIT,'canonical_entire_L078_basis')
    require(matrix(bt,M)==rational(old['to_L067']) and matrix(C,bf)==rational(old['from_L067']),'L078_all_transports')
    oldZ=[[Fraction(int(i==j),2 if j==47 else 1) for j in range(48)] for i in range(48)]
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
    Z=[[Fraction(int(i==j),2 if j>=46 else 1) for j in range(48)] for i in range(48)]
    T=[[int(i==j)*(2 if j>=46 else 1) for j in range(48)] for i in range(48)]
    require(rational(d['M'])==Z and d['numerator']==[[2*x for x in row] for row in Z]
            and d['inverse']==T and d['index']==4 and d['determinant']==4
            and d['decision']=='NOT_2_MAXIMAL','audited_L085_entire_multiplier')
    B=matrix(M,Z); BI=matrix(T,C)
    powers=matrix(bp,B); back=matrix(BI,pb)
    coords=matrix(lmat,powers); coords_back=matrix(back,linv)
    pairs=[('basis_in_b','b_to_basis',B,BI),('basis_to_power','power_to_basis',powers,back),
           ('to_L067','from_L067',coords,coords_back)]
    for forward,reverse,a,z in pairs:
        af=rational(got[forward]); az=rational(got[reverse]); shape(af,48,48); shape(az,48,48)
        require(af==a and az==z,'every_transport_entry_'+forward)
        require(matrix(af,az)==UNIT and matrix(az,af)==UNIT,'both_inverse_products_'+forward)
    shape(T,48,48,True)
    require(rational(got['basis_in_n'])==Z and got['old_inclusion']==T
            and matrix(Z,T)==UNIT and matrix(T,Z)==UNIT and matrix(B,T)==M,'full_integral_old_inclusion')
    # Full diagonal checks certify determinant, not a saved index label.
    require(all(T[i][j]==(int(i==j)*(2 if i>=46 else 1)) for i in range(48) for j in range(48)),'all_determinant_entries')
    index=math.prod(T[i][i] for i in range(48))
    require(index==got['index']==4 and got['rank']==48,'exact_index_four')
    identity=[BI[i][0] for i in range(48)]
    require(all(Fraction(x).denominator==1 for x in identity),'integral_actual_identity')
    identity=list(map(int,identity))
    require(got['identity']==identity==d['identity_in_multiplier']
            and prior['identity']==[C[i][0] for i in range(48)]
            and matrix(powers,transpose([identity]))==transpose([UNIT[0]]),'actual_identity_in_original_field')
    # M now describes n; retain its scale 62 and the original m-scale 31.
    nscaled=transpose(matrix(bp,[[62*x for x in row] for row in M]))
    require(all(Fraction(x).denominator==1 for row in nscaled for x in row),'input_scaled_polynomials_integer')
    require(nscaled==prior['scaled_polynomials'],'every_input_scale_62_coefficient')
    W=[[Fraction(x,1 if i==47 else 2) for x in row] for i,row in enumerate(nscaled)]
    require(all(Fraction(x).denominator==1 for row in W for x in row),'original_scale_31_retained')
    V=[[int(x)*(1 if i==47 else 2 if i==46 else 4) for x in row] for i,row in enumerate(W)]
    require(got['H']==H and got['scale']==124 and got['original_scale']==31
            and got['input_scale']==62 and got['enlargement_denominator']==2
            and got['scaled_polynomials']==V
            and transpose(matrix(powers,[[124*x for x in row] for row in UNIT]))==V,'all_scaled_polynomial_slots')
    REPORT['phase']='all_original_H_product_remainders'; table=[]
    Hnz=[(i,x) for i,x in enumerate(H) if x]
    for i in range(48):
        row=load(HERE/('product-%02d.json'%i)); shape(row,48,48,True)
        divisions=[]
        for j,c in enumerate(row):
            # Independent convolution and expansion. All 48 coefficients of c are used.
            poly=[0]*95
            for a,x in enumerate(V[i]):
                if x:
                    for b,y in enumerate(V[j]):
                        if y: poly[a+b]+=x*y
            for k,z in enumerate(c):
                if z:
                    for a,x in enumerate(V[k]):
                        if x: poly[a]-=124*z*x
            # General rational division, with an exact-integer fast path checked
            # at each step; nondivisibility is handled, never assumed impossible.
            dividend=poly[:]; quotient=[0]*47
            for degree in range(94,47,-1):
                x=poly[degree]
                if not x: continue
                if type(x) is int:
                    q,r=divmod(x,343)
                    if r:
                        q=Fraction(x,343); REPORT['rational_quotient_steps']+=1
                else:
                    q=Fraction(x,343); REPORT['rational_quotient_steps']+=1
                quotient[degree-48]=q
                for a,h in Hnz: poly[degree-48+a]-=q*h
            require(not any(poly),'full_product_remainder_'+str((i,j)))
            divisions.append({'j':j,'dividend':dividend,'quotient':[str(x) for x in quotient],
                              'remainder':[str(x) for x in poly]})
            REPORT['product_slots']+=48; REPORT['product_identities']+=1
            REPORT['remainder_coefficients']+=95
        save('division-%02d.json'%i,{'i':i,'products':divisions})
        table.append(row)
    for i in range(48):
        left=[0]*48; right=[0]*48
        for j,z in enumerate(identity):
            for k in range(48):
                left[k]+=z*table[j][i][k]; right[k]+=z*table[i][j][k]
        require(left==UNIT[i] and right==UNIT[i],'both_actual_identity_actions_'+str(i))
    after=inventory(); require(after==before,'every_original_preserved')
    save('preservation-input.json',{'equal':True,'original_files':len(before),'after':after})
    REPORT.update(status='PASS',phase='complete',basis_elements=48,transport_entries=18432,division_certificates=2304,
                  inverse_products=8,identity_actions=96,index=index,original_files=len(before))
try: main()
except Exception as e: REPORT.update(status='STOP',failure=type(e).__name__+': '+str(e),failures=[str(e)])
finally:
    REPORT.update(seconds=time.monotonic()-BEGAN,required_product_slots=110592,
                  required_product_identities=2304,stage_limit_seconds=180,artifact_limit_bytes=CAP)
    save('input-report.json',REPORT); print(json.dumps(REPORT))
sys.exit(0 if REPORT['status']=='PASS' else 1)
