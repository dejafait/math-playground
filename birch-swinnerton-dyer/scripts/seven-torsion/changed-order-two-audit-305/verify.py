"""Independent integer replay, no producer imports and no numpy.

The full table and actions are verified by polynomial divisibility in
original H. Frobenius uses exact Python integer multiplication in that
verified table, keeping the original scale 31 distinct from prime 2.
"""
from pathlib import Path
from fractions import Fraction
import hashlib, json, math, sys, time
sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
NOTEBOOK=HERE.parents[2]
SOURCE=NOTEBOOK/'scripts/seven-torsion/nonmonic-order-283'
PREV=NOTEBOOK/'scripts/seven-torsion/radical-overorder-295'
BEGAN=time.monotonic()
REPORT={'status':'INCOMPLETE','phase':'inputs','input_product_slots':0,'action_slots':0,'row_operations':0,'failures':[]}
UNIT=[[int(i==j) for j in range(48)] for i in range(48)]
def save(name,data):
    raw=(json.dumps(data,separators=(',',':'))+'\n').encode()
    require(sum(p.stat().st_size for p in HERE.iterdir() if p.is_file())+len(raw)+65536<=134217728,'byte_cap')
    with (HERE/name).open('xb') as f:f.write(raw)
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
    for directory in (SOURCE,PREV,NOTEBOOK/'scripts/seven-torsion/radical-overorder-audit-297', NOTEBOOK/'scripts/seven-torsion/enlarged-order-test-299', NOTEBOOK/'scripts/seven-torsion/enlarged-order-audit-301'):
        files.extend(p for p in directory.iterdir() if p.is_file())
    return {str(p.relative_to(NOTEBOOK)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(files)}

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
    before=file_hashes();require(before==read('input-hashes.json'),'unchanged_audited_inputs')
    base=json.loads((SOURCE/'basis.json').read_text())
    original=json.loads((NOTEBOOK/'scripts/seven-torsion/certificate.json').read_text())
    nb=json.loads((PREV/'basis.json').read_text());ib=read('input-basis.json')
    H=base['H']
    require(len(H)==49 and all(type(x) is int for x in H) and H[-1]==343
        and H==original['primitive_integer_factors'][0] and math.gcd(*H)==1
        and list(map(Fraction,original['h']))==[Fraction(x,343) for x in H],'original_H_343h')
    bases=[[1]+[0]*47]+[[H[48-i+k] if k<=i else 0 for k in range(48)] for i in range(1,48)]
    require(bases==base['basis'] and tr(bases)==base['basis_to_power'],'all_original_basis_polynomials')
    pb=rat(base['power_to_basis']);to=rat(base['basis_to_L067']);fr=rat(base['L067_to_basis'])
    require(product(tr(bases),pb)==UNIT and product(pb,tr(bases))==UNIT,'both_original_power_inverses')
    require(product(rat(original['matrix']),tr(bases))==to
        and product(pb,rat(original['inverse']))==fr,'full_original_transports')
    M=rat(nb['M']);C=nb['inverse'];Q=nb['numerator']
    is_integer_matrix(C,48,48,'old_inclusion_integer');is_integer_matrix(Q,48,48,'input_numerator_integer')
    require(product(M,C)==UNIT and product(C,M)==UNIT
        and [[31*x for x in r] for r in M]==Q,'changed_inverse_both')
    identity=nb['identity_coordinates']
    require(identity==[C[i][0] for i in range(48)]
        and product(M,tr([identity]))==tr([UNIT[0]]),'actual_changed_identity')
    nto=rat(nb['to_L067']);nfr=rat(nb['from_L067'])
    require(product(to,M)==nto and product(C,fr)==nfr
        and product(nto,nfr)==UNIT and product(nfr,nto)==UNIT,'complete_changed_transports_and_both_inverses')
    polys=tr(product(tr(bases),Q))
    require(ib['H']==H and rat(ib['M'])==M and ib['inverse']==C and ib['scaled_polynomials']==polys
        and rat(ib['to_L067'])==nto and rat(ib['from_L067'])==nfr
        and ib['identity']==identity and ib['scale']==31,'every_input_basis_coefficient')
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
        require(not any(a),label+'_entire_zero_remainder')
    def compare(a,b,expansion,label):
        d=convolution(a,b)
        for k,x in enumerate(expansion):d[k]-=x
        divisible(d,label)
    table=[];REPORT['phase']='complete_input_table_polynomial_checks'
    for i in range(48):
        row=json.loads((PREV/('product-%02d.json'%i)).read_text())
        is_integer_matrix(row,48,48,'changed_table_full_integer_shape')
        for j,v in enumerate(row):
            expansion=[31*sum(v[k]*polys[k][l] for k in range(48) if v[k] and polys[k][l]) for l in range(48)]
            compare(polys[i],polys[j],expansion,'input_product_'+str((i,j)))
            REPORT['input_product_slots']+=48
        table.append(row)
    for i in range(48):
        require([sum(identity[j]*table[j][i][k] for j in range(48)) for k in range(48)]==UNIT[i],'left_identity')
        require([sum(identity[j]*table[i][j][k] for j in range(48)) for k in range(48)]==UNIT[i],'right_identity')
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
    # Each column of Wpolys represents 31 times the actual radical element.
    Wpolys=tr(product(tr(polys),J))
    actions=[];REPORT['phase']='all_integral_radical_actions_in_original_H'
    for i in range(48):
        A=read('action-%02d.json'%i);is_integer_matrix(A,48,48,'action_full_integer_shape')
        JA=product(J,A)
        expansion=tr(product(tr(polys),JA))
        for j in range(48):
            compare(polys[i],Wpolys[j],[31*x for x in expansion[j]],'action_'+str((i,j)))
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
    require(file_hashes()==before,'all_original_input_bytes_preserved')
    save('preservation-verifier.json',{'before':before,'after':file_hashes(),'equal':True})
    REPORT.update(status='PASS',phase='complete',decision=dc['decision'],index=index,original_files=len(before))

try:main()
except Exception as e:REPORT.update(status='STOP',failure=type(e).__name__+': '+str(e),failures=[type(e).__name__+': '+str(e)])
finally:
    REPORT.update(seconds=time.monotonic()-BEGAN,required_input_product_slots=110592,required_action_slots=110592)
    save('verification-report.json',REPORT);print(json.dumps(REPORT))
sys.exit(0 if REPORT['status']=='PASS' else 1)
