"""Independent complete replay. No producer imports or numpy arithmetic.

Frobenius is reconstructed in F31[T]/H; old products, action operators
and new products are proved by full polynomial divisibility in original H.
Both integral preimages are checked by explicit two-sided generator identities.
"""
from pathlib import Path
from fractions import Fraction
import hashlib, json, math, signal, sys, time

sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
NOTEBOOK=HERE.parents[2]
SOURCE=NOTEBOOK/'scripts/seven-torsion/nonmonic-order-283'
BEGAN=time.monotonic()
REPORT={'status':'INCOMPLETE','phase':'inputs','old_product_slots':0,
        'action_slots':0,'new_product_slots':0,'row_operations':0,'failures':[]}
UNIT=[[int(i==j) for j in range(48)] for i in range(48)]

def require(ok,name):
    if not ok:raise ValueError(name)

def read(name):return json.loads((HERE/name).read_text())
def rat(a):return [[Fraction(x) for x in r] for r in a]
def tr(a):return [list(row) for row in zip(*a)]

def product(a,b):
    out=[[0]*len(b[0]) for _ in a]
    for k in range(len(b)):
        for i in range(len(a)):
            x=a[i][k]
            if x:
                for j,y in enumerate(b[k]):
                    if y:out[i][j]+=x*y
    return out

def is_integer_matrix(a,rows,cols,label):
    require(len(a)==rows and all(len(r)==cols and all(type(x) is int for x in r) for r in a),label)

def file_hashes():
    files=[NOTEBOOK/'scripts/seven-torsion/certificate.json']
    for directory in (SOURCE,NOTEBOOK/'scripts/residual-prime-289'):
        files.extend(p for p in directory.iterdir() if p.is_file())
    return {str(p.relative_to(NOTEBOOK)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(files)}

def verify_elimination(cert,matrix,label):
    require(cert['matrix']==matrix,label+'_full_matrix')
    width=len(matrix[0]);height=len(matrix)
    a=[[x%31 for x in row] for row in matrix]
    for operation in cert['operations']:
        kind=operation[0]
        if kind=='swap':
            _,i,j=operation
            require(0<=i<height and 0<=j<height,label+'_invertible_swap')
            a[i],a[j]=a[j],a[i]
        elif kind=='scale':
            _,i,q=operation
            require(0<=i<height and 0<q<31,label+'_nonzero_scaling')
            for c in range(width):a[i][c]=(a[i][c]*q)%31
        elif kind=='add':
            _,i,j,q=operation
            require(0<=i<height and 0<=j<height and i!=j and 0<q<31,label+'_invertible_row_add')
            for c in range(width):a[i][c]=(a[i][c]+q*a[j][c])%31
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
            for i,p in enumerate(piv):v[p]=(-a[i][c])%31
            kernels.append(v)
    require(kernels==cert['kernel'],label+'_complete_free_variable_kernel')
    for v in kernels:
        require(all(sum(x*y for x,y in zip(row,v))%31==0 for row in matrix),label+'_kernel_containment')
    return kernels,rank

def verify_lattice(name,kernel):
    cert=read(name+'.json')
    _,rank=verify_elimination(cert['kernel_reduction'],kernel,name+'_kernel_rref')
    require(rank==len(kernel),name+'_kernel_independent')
    rows=cert['kernel_reduction']['rref'][:rank]
    S=tr(rows+[[31*x for x in row] for row in UNIT])
    require(S==cert['S'],name+'_every_lift_and_31O_generator')
    J=cert['basis'];C=cert['C'];D=cert['D'];inverse=rat(cert['inverse'])
    is_integer_matrix(J,48,48,name+'_integer_basis')
    is_integer_matrix(C,48+rank,48,name+'_integer_forward_generators')
    is_integer_matrix(D,48,48+rank,name+'_integer_reverse_generators')
    require(product(S,C)==J and product(J,D)==S,name+'_two_sided_integral_generation')
    require(product(J,inverse)==UNIT and product(inverse,J)==UNIT,name+'_full_inverse_both_orders')
    require(cert['rank']==48,name+'_rank48')
    return J,inverse

def main():
    before=file_hashes()
    require(before==read('input-hashes.json'),'all_original_inputs_match_producer')
    base=json.loads((SOURCE/'basis.json').read_text())
    original=json.loads((NOTEBOOK/'scripts/seven-torsion/certificate.json').read_text())
    H=base['H']
    require(len(H)==49 and all(type(x) is int for x in H) and H[-1]==343,'original_H_shape')
    require(H==original['primitive_integer_factors'][0]
        and list(map(Fraction,original['h']))==[Fraction(x,343) for x in H]
        and math.gcd(*H)==1,'primitive_original_H_equals_343h')
    require(base['source_sha256']==before['scripts/seven-torsion/certificate.json'],'audited_L067_hash')
    bases=[[1]+[0]*47]
    for degree in range(1,48):
        bases.append([H[48-degree+k] if k<=degree else 0 for k in range(48)])
    require(bases==base['basis'] and tr(bases)==base['basis_to_power'],'all_original_basis_polynomials')
    power_to=rat(base['power_to_basis']);oldto=rat(base['basis_to_L067']);oldfrom=rat(base['L067_to_basis'])
    require(product(tr(bases),power_to)==UNIT and product(power_to,tr(bases))==UNIT,'original_power_inverses_both')
    require(product(oldto,oldfrom)==UNIT and product(oldfrom,oldto)==UNIT,'original_coordinate_inverses_both')
    require(product(rat(original['matrix']),tr(bases))==oldto
        and product(power_to,rat(original['inverse']))==oldfrom,'original_full_coordinate_transports')
    require(base['identity']==UNIT[0],'original_identity')
    ded=json.loads((NOTEBOOK/'scripts/residual-prime-289/dedekind.json').read_text())
    source=read('source.json')
    require(ded['G']==source['G']==[24,0,1] and source['prime']==31 and source['H']==H,'fixed_source_prime_gcd_H')
    U=source['U']
    require(len(U)==47 and source['degree_U']==46 and U[-1]==2,'full_degree46_U')
    GU=[0]*49
    for k,x in enumerate(U):GU[k]+=24*x;GU[k+2]+=x
    require(all((x-y)%31==0 for x,y in zip(GU,H)),'all49_GU_reduction_coefficients')

    def convolution(a,b):
        terms=[0]*95
        for j,y in enumerate(b):
            if y:
                for i,x in enumerate(a):
                    if x:terms[i+j]+=x*y
        return terms
    def divisible(poly,label):
        a=list(poly)
        for k in range(len(a)-1,47,-1):
            require(a[k]%343==0,label+'_exact_integer_quotient')
            z=a[k]//343
            if z:
                for j in range(49):a[k-48+j]-=z*H[j]
        require(not any(a),label+'_all_remainder_coefficients_zero')
    def compare_product(a,b,expansion,label):
        d=convolution(a,b)
        for k,x in enumerate(expansion):d[k]-=x
        divisible(d,label)
    REPORT['phase']='old_products'
    for i in range(48):
        row=json.loads((SOURCE/('product-%02d.json'%i)).read_text())
        is_integer_matrix(row,48,48,'old_product_integer_shape')
        for j,v in enumerate(row):
            expansion=[sum(v[k]*bases[k][l] for k in range(48) if v[k] and bases[k][l]) for l in range(48)]
            compare_product(bases[i],bases[j],expansion,'old_product_'+str((i,j)))
            REPORT['old_product_slots']+=48
        if i==0:require(row==UNIT,'old_left_identity')
        require(row[0]==UNIT[i],'old_right_identity')

    REPORT['phase']='independent_polynomial_frobenius'
    hmod=[x%31 for x in H];lead_inverse=pow(hmod[-1],-1,31)
    def mod_product(a,b):
        c=[0]*95
        for j in range(48):
            if b[j]:
                for i in range(48):c[i+j]+=a[i]*b[j]
        for d in range(94,47,-1):
            q=(c[d]*lead_inverse)%31
            if q:
                for k in range(49):c[d-48+k]-=q*hmod[k]
        return [x%31 for x in c[:48]]
    def mod_power(a,e):
        # Fixed left-to-right binary powering, unlike the table producer.
        v=[1]+[0]*47
        for digit in bin(e)[2:]:
            v=mod_product(v,v)
            if digit=='1':v=mod_product(v,a)
        return v
    pbinv=[[int(x.numerator%31)*pow(x.denominator%31,-1,31)%31 for x in row] for row in power_to]
    def as_old(v):return [sum(x*y for x,y in zip(row,v))%31 for row in pbinv]
    first_columns=[];second_columns=[]
    for b in bases:
        v=mod_power([x%31 for x in b],31)
        first_columns.append(as_old(v))
        second_columns.append(as_old(mod_power(v,31)))
    first,second=tr(first_columns),tr(second_columns)
    fc=read('frobenius.json')
    require(fc['first']==first and fc['second']==second,'all_frobenius_and_second_iterate_coefficients')
    require(fc['iterate']==2 and fc['dimension']==48 and fc['exponent']==961 and 961>48,'frobenius_full_radical_threshold')
    kernels,rank=verify_elimination(fc['elimination'],second,'frobenius')
    require(rank==46 and len(kernels)==2,'full_frobenius_rank46_kernel2')
    REPORT.update(frobenius_rank=rank,radical_dimension=len(kernels))
    J,Jinv=verify_lattice('radical-lattice',kernels)
    Jpolys=tr(product(tr(bases),J))

    REPORT['phase']='all_integral_action_operators'
    actions=[]
    for i in range(48):
        A=read('action-%02d.json'%i)
        is_integer_matrix(A,48,48,'action_integer_shape')
        # Every column of J A is independently checked as an equality in K.
        expanded_polys=tr(product(tr(bases),product(J,A)))
        for j in range(48):
            compare_product(bases[i],Jpolys[j],expanded_polys[j],'full_action_'+str((i,j)))
            REPORT['action_slots']+=48
        actions.append(A)
    stack=[]
    for j in range(48):
        for k in range(48):stack.append([a[k][j]%31 for a in actions])
    kernels,rank=verify_elimination(read('action-kernel.json'),stack,'full_I_mod31I_action')
    require(rank==46 and len(kernels)==2,'full_action_rank46_kernel2')
    REPORT.update(action_rank=rank,action_kernel_dimension=len(kernels))
    Q,Qinv=verify_lattice('numerator-lattice',kernels)

    REPORT['phase']='new_basis_index_and_transports'
    nb=read('basis.json');M=rat(nb['M']);C=nb['inverse']
    is_integer_matrix(C,48,48,'full_integral_old_order_inclusion')
    require(nb['numerator']==Q and [[31*x for x in row] for row in M]==Q,'full_31M_numerator')
    require(product(M,C)==UNIT and product(C,M)==UNIT,'new_full_inverse_both_orders')
    require([[31*x for x in row] for row in Qinv]==C,'numerator_inverse_matching')
    require(all(C[i][j]==0 for i in range(48) for j in range(i+1,48)),'full_triangular_inclusion_matrix')
    determinant=1
    for i in range(48):determinant*=C[i][i]
    require(abs(determinant)==nb['index']==961 and nb['inclusion_determinant']==determinant,'exact_full_triangular_determinant_index961')
    require(nb['identity_coordinates']==[C[i][0] for i in range(48)] and nb['rank']==48,'identity_and_old_basis_membership')
    nto=rat(nb['to_L067']);nfr=rat(nb['from_L067'])
    require(product(oldto,M)==nto and product(C,oldfrom)==nfr,'both_complete_new_L067_transports')
    require(product(nto,nfr)==UNIT and product(nfr,nto)==UNIT,'new_L067_both_inverse_identities')
    REPORT.update(index=abs(determinant),rank=48)

    REPORT['phase']='every_new_product_polynomial_identity'
    polynomials=tr(product(tr(bases),Q))
    for i in range(48):
        row=read('product-%02d.json'%i)
        is_integer_matrix(row,48,48,'new_product_integral_shape')
        for j,c in enumerate(row):
            # (V_i/31)(V_j/31)=sum c_k V_k/31 iff
            # V_i V_j -31 sum c_k V_k is zero modulo H.
            expansion=[31*sum(c[k]*polynomials[k][l] for k in range(48) if c[k] and polynomials[k][l]) for l in range(48)]
            compare_product(polynomials[i],polynomials[j],expansion,'new_product_'+str((i,j)))
            REPORT['new_product_slots']+=48
    require(file_hashes()==before,'all_original_files_unchanged_after_complete_replay')
    report_path=HERE/'preservation-verifier.json'
    with report_path.open('x') as f:json.dump({'before':before,'after':file_hashes(),'equal':True},f)
    REPORT.update(status='PASS',phase='complete',original_files=len(before),
        source_identification='entire radical and entire action on I/31I, both exact integral preimages; imported equality')

def stop(*unused):raise TimeoutError('internal_180_second_cap')
signal.signal(signal.SIGALRM,stop);signal.setitimer(signal.ITIMER_REAL,180)
try:main()
except Exception as e:REPORT.update(status='STOP',failure=type(e).__name__+': '+str(e),failures=[type(e).__name__+': '+str(e)])
finally:
    signal.setitimer(signal.ITIMER_REAL,0)
    REPORT.update(seconds=time.monotonic()-BEGAN,required_seconds=180,required_old_product_slots=110592,
        required_action_slots=110592,required_new_product_slots=110592,required_index=961)
    raw=(json.dumps(REPORT,separators=(',',':'))+'\n').encode()
    with (HERE/'verification-report.json').open('xb') as f:f.write(raw)
    size=sum(p.stat().st_size for p in HERE.iterdir() if p.is_file())
    REPORT['aggregate_bytes']=size;REPORT['byte_limit']=134217728
    print(json.dumps(REPORT))
sys.exit(0 if REPORT['status']=='PASS' and size<=134217728 else 1)
