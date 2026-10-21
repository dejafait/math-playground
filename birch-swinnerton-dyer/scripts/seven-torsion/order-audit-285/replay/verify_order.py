"""Independent exact replay: imports no producer or producer arithmetic.

Products are checked by integer polynomial divisibility of the claimed
identity, traces by composition of the complete multiplication matrices.
Every saved elimination step is reconstructed, including all exact divisions.
"""
from pathlib import Path
from fractions import Fraction
import hashlib, json, math, signal, sys, time

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
BEGAN = time.monotonic()
REPORT = {'status':'INCOMPLETE','phase':'input','product_slots':0,'trace_entries':0}

def require(condition, name):
    if not condition: raise ValueError(name)

def read(name): return json.loads((HERE/name).read_text())

def stop(*unused): raise TimeoutError('internal_180_second_cap')

def multiply_matrices(left,right):
    m,n,p = len(left),len(right),len(right[0])
    out = [[Fraction(0) for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for k in range(n):
            if left[i][k]:
                for j in range(p):
                    if right[k][j]: out[i][j] += left[i][k]*right[k][j]
    return out

def rational_matrix(a): return [list(map(Fraction,row)) for row in a]

def check_elimination(name,matrix):
    evidence = read(name+'.json')
    require(evidence['matrix']==matrix,name+'_complete_input')
    work = [row.copy() for row in matrix]
    n = len(work)
    require(len(evidence['steps'])==n-1,name+'_all_steps')
    sign, denominator, count = 1,1,0
    for k in range(n-1):
        row = k
        while row<n and work[row][k]==0: row += 1
        require(row<n,name+'_nonsingular')
        if row!=k:
            work[k],work[row] = work[row],work[k]
            sign = -sign
        pivot = work[k][k]
        step = evidence['steps'][k]
        require((step['k'],step['row'],step['pivot'],step['divisor'])==
                (k,row,pivot,denominator),name+'_pivot_'+str(k))
        column = [r[k] for r in work]
        # Column-major replay, with original column retained separately.
        for j in range(k+1,n):
            top = work[k][j]
            for i in range(k+1,n):
                numerator = work[i][j]*pivot-column[i]*top
                require(numerator%denominator==0,name+'_division_'+str(k))
                work[i][j] = numerator//denominator
                count += 1
        for i in range(k+1,n): work[i][k]=0
        sha = hashlib.sha256(json.dumps(work,separators=(',', ':')).encode()).hexdigest()
        require(sha==step['after_sha256'],name+'_full_stage_'+str(k))
        denominator = pivot
    value = sign*work[-1][-1]
    require(evidence['exact_divisions']==count and evidence['terminal']==work[-1][-1]
            and evidence['sign']==sign and evidence['determinant']==value,
            name+'_terminal_and_all_divisions')
    REPORT[name+'_divisions'] = count
    return value

def main():
    certpath = HERE.parent/'certificate.json'
    original = json.loads(certpath.read_text())
    certificate = read('basis.json')
    require(hashlib.sha256(certpath.read_bytes()).hexdigest()==certificate['source_sha256'],
            'audited_L067_exact_input_hash')
    H = certificate['H']
    require(len(H)==49 and all(type(v) is int for v in H) and H[-1]==343,
            'H_degree48_leading343')
    content = 0
    for v in H: content=math.gcd(content,v)
    require(content==1 and H==original['primitive_integer_factors'][0]
            and [Fraction(v,343) for v in H]==list(map(Fraction,original['h'])),
            'all49_coefficients_content_and_h')
    bases = certificate['basis']
    expected = [[1]+[0]*47]
    for i in range(1,48):
        expected.append([H[48-i+k] if k<=i else 0 for k in range(48)])
    require(bases==expected,'all48_cited_basis_elements')
    bp = certificate['basis_to_power']
    require(bp==[list(row) for row in zip(*expected)],'basis_to_power_all_entries')
    pb = rational_matrix(certificate['power_to_basis'])
    to_old = rational_matrix(certificate['basis_to_L067'])
    from_old = rational_matrix(certificate['L067_to_basis'])
    identity = [[int(i==j) for j in range(48)] for i in range(48)]
    for left,right,name in [(bp,pb,'power_forward_inverse'),(pb,bp,'power_inverse_forward'),
            (to_old,from_old,'old_forward_inverse'),(from_old,to_old,'old_inverse_forward')]:
        require(len(left)==len(right)==48 and all(len(r)==48 for r in left+right),name+'_shapes')
        require(multiply_matrices(left,right)==identity,name)
    oldM = rational_matrix(original['matrix'])
    oldN = rational_matrix(original['inverse'])
    require(multiply_matrices(oldM,bp)==to_old,'all_L067_forward_transports')
    require(multiply_matrices(pb,oldN)==from_old,'all_L067_reverse_transports')
    require(certificate['identity']==[1]+[0]*47,'identity_vector')
    REPORT['phase'] = 'product_identities'
    products=[]
    for i in range(48):
        row=read('product-%02d.json'%i)
        require(len(row)==48 and all(len(v)==48 for v in row),'product_shape_'+str(i))
        for j,vector in enumerate(row):
            require(all(type(v) is int for v in vector),'ring_integral_'+str((i,j)))
            difference=[0]*95
            # Claimed product minus its full basis expansion.
            for k in range(48):
                if bases[i][k]:
                    for l in range(48):
                        difference[k+l] += bases[i][k]*bases[j][l]
                if vector[k]:
                    for l in range(48): difference[l] -= vector[k]*bases[k][l]
            for degree in range(94,47,-1):
                require(difference[degree]%H[-1]==0,'product_exact_quotient')
                q=difference[degree]//H[-1]
                for k in range(49): difference[degree-48+k]-=q*H[k]
            require(not any(difference),'full_polynomial_product_identity_'+str((i,j)))
            REPORT['product_slots'] += 48
        products.append(row)
    require(products[0]==identity and all(products[i][0]==identity[i] for i in range(48)),
            'identity_both_sides')
    REPORT['phase']='trace_matrix_compositions'
    trace = read('trace.json')
    require(len(trace['traces'])==48 and len(trace['gram'])==48
            and all(len(r)==48 for r in trace['gram']),'trace_shapes')
    for i in range(48):
        require(trace['traces'][i]==sum(products[i][j][j] for j in range(48)),
                'trace_basis_'+str(i))
        for j in range(48):
            value=0
            for k in range(48):
                for l in range(48):
                    value += products[i][k][l]*products[j][l][k]
            require(value==trace['gram'][i][j],'trace_composition_'+str((i,j)))
            REPORT['trace_entries']+=1
    REPORT['phase']='trace_elimination'
    disc = check_elimination('trace-elimination',trace['gram'])
    require(disc!=0,'nonzero_trace_determinant')
    REPORT['phase']='resultant_elimination'
    # Independently place descending coefficients in the Sylvester matrix.
    s = [[0 for _ in range(95)] for _ in range(95)]
    for i in range(47):
        for k in range(49): s[i][i+k]=H[48-k]
    for i in range(48):
        for k in range(48): s[47+i][i+k]=(48-k)*H[48-k]
    resultant = check_elimination('resultant-elimination',s)
    require(resultant%343==0 and resultant//343==disc,
            'complete_trace_resultant_equality')
    d=read('discriminant.json')
    require(d=={'order_discriminant':disc,'resultant':resultant,
        'polynomial_discriminant':disc,'sign_exponent':1128,'leading_coefficient':343,
        'equal':True,'nonzero':True,'decimal_digits':len(str(abs(disc)))},
        'all_discriminant_fields')
    REPORT.update(status='PASS',phase='complete',basis_elements=48,
                  discriminants_agree=True,discriminant_decimal_digits=len(str(abs(disc))))

signal.signal(signal.SIGALRM,stop)
signal.setitimer(signal.ITIMER_REAL,180)
try: main()
except Exception as exc:
    REPORT.update(status='STOP',failure=type(exc).__name__+': '+str(exc))
finally:
    signal.setitimer(signal.ITIMER_REAL,0)
    REPORT.update(seconds=time.monotonic()-BEGAN,required_seconds=180,
                  required_product_slots=110592,required_trace_entries=2304)
    with (HERE/'verification-report.json').open('x') as f: json.dump(REPORT,f)
    print(json.dumps(REPORT))
sys.exit(0 if REPORT['status']=='PASS' else 1)
