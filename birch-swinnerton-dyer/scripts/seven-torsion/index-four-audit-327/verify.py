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
    require(sum(p.stat().st_size for p in HERE.iterdir() if p.is_file())+len(raw)+65536<=CAP,'artifact_cap')
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
    files=[SRC/'certificate.json']
    files += [ROOT/p for p in ['lemmas/L067-conductor389-full-seven-torsion-algebra.md', 'lemmas/L077-conductor389-nonmonic-starting-order.md', 'lemmas/L078-conductor389-first-31-overorder.md', 'lemmas/L080-conductor389-changed-order-not-2-maximal.md', 'lemmas/L084-conductor389-index-two-multiplier-order-table.md', 'drafts/literature/2026-10-18-index-two-order-prime-two-test.md']]
    for d in ('nonmonic-order-283','radical-overorder-295','radical-overorder-audit-297',
              'changed-order-two-303','changed-order-two-audit-305','index-two-table-321','index-two-table-audit-323'):
        files+=list(p for p in (SRC/d).iterdir() if p.is_file())
    return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(files)}
# Aliases for the independent kernel replay; no producer imports.
product=matrix
rat=rational
tr=transpose
file_hashes=inventory
def read(name): return load(HERE/name)
def is_integer_matrix(a,rows,cols,label):
    require(len(a)==rows and all(len(r)==cols and all(type(x) is int for x in r) for r in a),label)
def verify_elimination(cert,matrix,label):
    require(cert['matrix']==matrix,label+'_full_matrix')
    width=len(matrix[0]) if matrix else 48; height=len(matrix)
    a=[[x%2 for x in row] for row in matrix]
    for operation in cert['operations']:
        kind=operation[0]
        if kind=='swap':
            _,i,j=operation
            require(0<=i<height and 0<=j<height,label+'_invertible_swap')
            a[i],a[j]=a[j],a[i]
        elif kind=='scale':
            _,i,q=operation
            require(0<=i<height and 0<q<2,label+'_nonzero_scaling')
            for c in range(width):a[i][c]=(a[i][c]*q)%2
        elif kind=='add':
            _,i,j,q=operation
            require(0<=i<height and 0<=j<height and i!=j and 0<q<2,label+'_invertible_row_add')
            for c in range(width):a[i][c]=(a[i][c]+q*a[j][c])%2
        else:raise ValueError(label+'_unknown_row_operation')
        REPORT['row_operations']+=1
    require(a==cert['rref'],label+'_all_terminal_coefficients')
    piv=cert['pivots'];rank=len(piv)
    require(cert['rank']==rank and piv==sorted(set(piv)) and all(0<=c<width for c in piv),label+'_pivots')
    for i,c in enumerate(piv):
        require(not any(a[i][:c]) and a[i][c]==1,label+'_leading_one')
        require(all(a[j][c]==int(j==i) for j in range(height)),label+'_entire_pivot_column')
    require(all(not any(row) for row in a[rank:]),label+'_all_remaining_rows_zero')
    # These invertible operations plus the displayed RREF prove the full rank.
    kernels=[]
    for c in range(width):
        if c not in piv:
            v=[0]*width;v[c]=1
            for i,p in enumerate(piv):v[p]=(-a[i][c])%2
            kernels.append(v)
    require(kernels==cert['kernel'],label+'_complete_free_variable_kernel')
    for v in kernels:
        require(all(sum(x*y for x,y in zip(row,v))%2==0 for row in matrix),label+'_kernel_containment')
    return kernels,rank

def verify_lattice(name,kernel):
    cert=read(name+'.json')
    _,rank=verify_elimination(cert['kernel_reduction'],kernel,name+'_kernel_rref')
    require(rank==len(kernel),name+'_kernel_independent')
    rows=cert['kernel_reduction']['rref'][:rank]
    S=tr(rows+[[2*x for x in row] for row in UNIT])
    require(S==cert['S'],name+'_every_lift_and_2O_generator')
    J=cert['basis'];C=cert['C'];D=cert['D'];inverse=rat(cert['inverse'])
    is_integer_matrix(J,48,48,name+'_integer_basis')
    is_integer_matrix(C,48+rank,48,name+'_integer_forward_generators')
    is_integer_matrix(D,48,48+rank,name+'_integer_reverse_generators')
    require(product(S,C)==J and product(J,D)==S,name+'_two_sided_integral_generation')
    require(product(J,inverse)==UNIT and product(inverse,J)==UNIT,name+'_full_inverse_both_orders')
    require(cert['rank']==48,name+'_rank48')
    return J,inverse


def main():
    before=inventory(); require(before==load(HERE/'input-hashes.json'),'exact_original_inputs')
    original=load(SRC/'certificate.json'); b=load(SRC/'nonmonic-order-283/basis.json')
    old=load(SRC/'radical-overorder-295/basis.json'); d=load(SRC/'changed-order-two-303/decision.json')
    got=load(SRC/'index-two-table-321/basis.json'); H=b['H']
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
    Z=[[Fraction(int(i==j),2 if j==47 else 1) for j in range(48)] for i in range(48)]
    T=[[int(i==j)*(2 if j==47 else 1) for j in range(48)] for i in range(48)]
    require(rational(d['M'])==Z and d['numerator']==[[2*x for x in row] for row in Z]
            and d['inverse']==T and d['index']==2 and d['determinant']==2
            and d['decision']=='NOT_2_MAXIMAL','audited_L080_entire_multiplier')
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
    require(rational(got['basis_in_m'])==Z and got['old_inclusion']==T
            and matrix(Z,T)==UNIT and matrix(T,Z)==UNIT and matrix(B,T)==M,'full_integral_old_inclusion')
    # Full diagonal checks certify determinant, not a saved index label.
    require(all(T[i][j]==(int(i==j)*(2 if i==47 else 1)) for i in range(48) for j in range(48)),'all_determinant_entries')
    index=math.prod(T[i][i] for i in range(48))
    require(index==got['index']==2 and got['rank']==48,'exact_index_two')
    identity=[BI[i][0] for i in range(48)]
    require(all(x.denominator==1 for x in identity),'integral_actual_identity')
    identity=list(map(int,identity))
    require(got['identity']==identity==d['identity_in_multiplier']
            and old['identity_coordinates']==[C[i][0] for i in range(48)]
            and matrix(powers,transpose([identity]))==transpose([UNIT[0]]),'actual_identity_in_original_field')
    # Original scale 31 is retained: W_i=31m_i and V_i=62n_i.
    W=transpose(matrix(bp,[[31*x for x in row] for row in M]))
    V=[[int(x)*(1 if i==47 else 2) for x in row] for i,row in enumerate(W)]
    require(all(x.denominator==1 for row in W for x in row),'old_scaled_polynomials_integer')
    require(got['H']==H and got['scale']==62 and got['original_scale']==31
            and got['enlargement_denominator']==2 and got['scaled_polynomials']==V
            and transpose(matrix(powers,[[62*x for x in row] for row in UNIT]))==V,'all_scaled_polynomial_slots')
    REPORT['phase']='all_original_H_product_remainders'; table=[]
    Hnz=[(i,x) for i,x in enumerate(H) if x]
    for i in range(48):
        row=load(SRC/'index-two-table-321'/('product-%02d.json'%i)); shape(row,48,48,True)
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
                        if x: poly[a]-=62*z*x
            # General rational division, with an exact-integer fast path checked
            # at each step; nondivisibility is handled, never assumed impossible.
            for degree in range(94,47,-1):
                x=poly[degree]
                if not x: continue
                if type(x) is int:
                    q,r=divmod(x,343)
                    if r:
                        q=Fraction(x,343); REPORT['rational_quotient_steps']+=1
                else:
                    q=x/343; REPORT['rational_quotient_steps']+=1
                for a,h in Hnz: poly[degree-48+a]-=q*h
            require(not any(poly),'full_product_remainder_'+str((i,j)))
            REPORT['product_slots']+=48; REPORT['product_identities']+=1
            REPORT['remainder_coefficients']+=95
        table.append(row)
    for i in range(48):
        left=[0]*48; right=[0]*48
        for j,z in enumerate(identity):
            for k in range(48):
                left[k]+=z*table[j][i][k]; right[k]+=z*table[i][j][k]
        require(left==UNIT[i] and right==UNIT[i],'both_actual_identity_actions_'+str(i))
    ib=read('input-basis.json'); polys=V
    require(ib['H']==H and rat(ib['M'])==B and rat(ib['inverse'])==BI
        and ib['scaled_polynomials']==V and rat(ib['to_L067'])==coords
        and rat(ib['from_L067'])==coords_back and ib['identity']==identity
        and ib['scale']==62,'every_new_input_basis_slot')
    REPORT['input_product_slots']=REPORT['product_slots']
    REPORT['action_slots']=0; REPORT['row_operations']=0
    def compare(a,b,expansion,label):
        p=[0]*95
        for j,y in enumerate(b):
            if y:
                for i,x in enumerate(a):
                    if x:p[i+j]+=x*y
        for i,x in enumerate(expansion):p[i]-=x
        for k in range(94,47,-1):
            x=p[k]
            if not x:continue
            if type(x) is int:
                q,r=divmod(x,343)
                if r:q=Fraction(x,343)
            else:q=x/343
            for j,h in Hnz:p[k-48+j]-=q*h
        require(not any(p),label+'_entire_original_H_remainder')
    REPORT['phase']='independent_exact_table_frobenius'
    residues=[[[x%2 for x in v] for v in row] for row in table]
    # Exact Python integers and independent repeated squaring in the full table.
    def mul(a,b):
        out=[0]*48
        for j,y in enumerate(b):
            if y:
                for i,x in enumerate(a):
                    if x:
                        xy=x*y
                        for k,z in enumerate(residues[i][j]):
                            if z:out[k]+=xy*z
        return [v%2 for v in out]
    cols=UNIT;iterates=[]
    for step in range(6):
        cols=[mul(col,col) for col in cols]
        current=tr(cols)
        if iterates:
            require([[x%2 for x in r] for r in product(iterates[0],iterates[-1])]==current,
                    'every_composition_vs_independent_square_'+str(step+1))
        iterates.append(current)
    fc=read('frobenius.json')
    require(fc['iterates']==iterates,'all_six_complete_frobenius_matrices')
    require(fc['iterate']==6 and fc['dimension']==48 and fc['exponent']==64
            and fc['prime']==2 and 64>48,'radical_exponent_threshold')
    kernels,rank=verify_elimination(fc['elimination'],iterates[-1],'frobenius')
    REPORT.update(frobenius_rank=rank,radical_dimension=len(kernels),frobenius_iterates=6,frobenius_slots=13824,required_frobenius_slots=13824,exponent=64,prime=2)
    J,Jinv=verify_lattice('radical-lattice',kernels)
    # Each column of Wpolys represents 62 times the actual radical element.
    Wpolys=tr(product(tr(polys),J))
    actions=[];REPORT['phase']='all_integral_radical_actions_in_original_H'
    for i in range(48):
        A=read('action-%02d.json'%i);is_integer_matrix(A,48,48,'action_full_integer_shape')
        JA=product(J,A)
        expansion=tr(product(tr(polys),JA))
        for j in range(48):
            compare(polys[i],Wpolys[j],[62*x for x in expansion[j]],'action_'+str((i,j)))
            # Also check J A=L_i J in the already verified integral order.
        require(JA==product(tr(table[i]),J),'all_integral_action_basis_change_slots')
        REPORT['action_slots']+=2304;actions.append(A)
    stack=[[actions[i][k][j]%2 for i in range(48)] for j in range(48) for k in range(48)]
    kernels,rank=verify_elimination(read('action-kernel.json'),stack,'entire_I_mod2I_action')
    REPORT.update(action_rank=rank,action_kernel_dimension=len(kernels))
    Q,Qinv=verify_lattice('numerator-lattice',kernels)
    dc=read('decision.json');mult=rat(dc['M']);T=dc['inverse']
    is_integer_matrix(T,48,48,'integral_inclusion_into_multiplier')
    require(dc['numerator']==Q and [[2*x for x in r] for r in mult]==Q
        and [[2*x for x in r] for r in Qinv]==T,'all_multiplier_basis_and_inverse_coefficients')
    require(product(mult,T)==UNIT and product(T,mult)==UNIT,'multiplier_both_inverse_products')
    require(all(T[i][j]==0 for i in range(48) for j in range(i+1,48)),'every_upper_triangular_zero')
    diag=[T[i][i] for i in range(48)];det=1
    for x in diag:det*=x
    index=abs(det)
    require(dc['determinant_diagonal']==diag and dc['determinant']==det
        and dc['index']==index==2**len(kernels) and dc['kernel_dimension']==len(kernels),'full_exact_determinant_index_kernel_dimension')
    im=[sum(T[i][j]*identity[j] for j in range(48)) for i in range(48)]
    require(dc['identity_in_multiplier']==im and product(mult,tr([im]))==tr([identity]),'identity_and_all_old_basis_inclusion')
    if index==1:
        E=dc['equality_forward'];is_integer_matrix(E,48,48,'equality_forward_integer')
        require(dc['equality_reverse']==T and product([[2*x for x in r] for r in UNIT],E)==Q
            and product(Q,T)==[[2*x for x in r] for r in UNIT],'complete_both_N_equals_2R_containments')
        require(dc['strict_witness'] is None and dc['decision']=='2_MAXIMAL','equality_stopping_decision')
    else:
        w=dc['strict_witness'];v=w['numerator'];col=w['column'];B=w['radical_action']
        require(0<=col<48 and v==[Q[i][col] for i in range(48)] and any(x%2 for x in v),'strict_nonintegral_old_coordinate')
        is_integer_matrix(B,48,48,'strict_witness_integral_radical_action')
        for k in range(48):
            for j in range(48):
                require(sum(v[i]*actions[i][k][j] for i in range(48))==2*B[k][j],'strict_witness_every_radical_product')
        require(dc['equality_forward'] is None and dc['decision']=='NOT_2_MAXIMAL','strict_stopping_decision')
    after=inventory(); require(after==before,'every_original_preserved')
    save('preservation-verifier.json',{'equal':True,'original_files':len(before),'after':after})
    REPORT.update(status='PASS',phase='complete',decision=dc['decision'],index=index,
                  basis_elements=48,transport_entries=13824,inverse_products=6,
                  identity_actions=96,original_files=len(before),required_input_product_slots=110592,
                  required_action_slots=110592)

try: main()
except Exception as e: REPORT.update(status='STOP',failure=type(e).__name__+': '+str(e),failures=[str(e)])
finally:
    REPORT.update(seconds=time.monotonic()-BEGAN,required_product_slots=110592,
                  required_product_identities=2304,stage_limit_seconds=180,artifact_limit_bytes=CAP)
    save('verification-report.json',REPORT); print(json.dumps(REPORT))
sys.exit(0 if REPORT['status']=='PASS' else 1)
