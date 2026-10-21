"""One capped fixed-field producer. All old artifacts are read-only."""
from pathlib import Path
from fractions import Fraction as Q
from math import gcd
from functools import reduce
import hashlib, json, signal, sys, time

sys.set_int_max_str_digits(0)
R = Path(__file__).resolve().parent
SOURCE = R.parent / 'certificate.json'
START = time.monotonic()
STATE = {'status': 'INCOMPLETE', 'phase': 'input', 'product_slots': 0}
CAP = 134217728

def need(ok, label):
    if not ok: raise ArithmeticError(label)

def write(name, value):
    data = (json.dumps(value, separators=(',', ':'))+'\n').encode()
    need(sum(p.stat().st_size for p in R.iterdir() if p.is_file())+len(data)<=CAP,
         'output_cap')
    with (R/name).open('xb') as f: f.write(data)

def alarm(*args): raise TimeoutError('internal_180_second_cap')

def matrix_digest(a):
    return hashlib.sha256(json.dumps(a,separators=(',', ':')).encode()).hexdigest()

def determinant(matrix, name):
    a = [row[:] for row in matrix]
    prev, sign, count = 1, 1, 0
    steps = []
    for k in range(len(a)-1):
        r = next((i for i in range(k,len(a)) if a[i][k]), None)
        need(r is not None, name+'_singular')
        if r != k: a[k],a[r],sign = a[r],a[k],-sign
        pivot = a[k][k]
        for i in range(k+1,len(a)):
            u = a[i][k]
            for j in range(k+1,len(a)):
                value, rem = divmod(pivot*a[i][j]-u*a[k][j], prev)
                need(rem==0, name+'_nonexact_division')
                a[i][j] = value
                count += 1
            a[i][k] = 0
        steps.append({'k':k,'row':r,'pivot':pivot,'divisor':prev,
                      'after_sha256':matrix_digest(a)})
        prev = pivot
    value = sign*a[-1][-1]
    write(name+'.json',{'matrix':matrix,'steps':steps,'terminal':a[-1][-1],
                        'sign':sign,'determinant':value,'exact_divisions':count})
    return value

def matmul(a,b):
    cols = list(zip(*b))
    return [[sum((x*y for x,y in zip(row,col) if x and y),Q(0))
             for col in cols] for row in a]

def rational_strings(a): return [[str(v) for v in row] for row in a]

def main():
    c = json.loads(SOURCE.read_text())
    h = list(map(Q,c['h']))
    H = c['primitive_integer_factors'][0]
    n = 48
    need(len(h)==len(H)==49 and h[-1]==1 and H[-1]==343,'degree_leading')
    need(all(Q(z)==343*v for z,v in zip(H,h)),'H_equals_343h_all49')
    need(reduce(gcd,H)==1,'primitive_content')
    a = H[-1]
    basis = [[0]*n for _ in range(n)]
    basis[0][0] = 1
    for i in range(1,n):
        for k in range(i+1): basis[i][k] = H[n-i+k]

    def coords(p):
        p = list(map(Q,p))
        out = [Q(0)]*n
        for i in range(n-1,0,-1):
            q = p[i]/a
            out[i] = q
            for k in range(i+1): p[k] -= q*basis[i][k]
        out[0] = p[0]
        return out

    bp = [list(row) for row in zip(*basis)]
    invcols = [coords([int(k==j) for k in range(n)]) for j in range(n)]
    pb = [list(row) for row in zip(*invcols)]
    I = [[Q(int(i==j)) for j in range(n)] for i in range(n)]
    need(matmul(bp,pb)==I and matmul(pb,bp)==I,'power_inverse_both')
    oldM = [[Q(v) for v in row] for row in c['matrix']]
    oldN = [[Q(v) for v in row] for row in c['inverse']]
    to_old = matmul(oldM,bp)
    from_old = matmul(pb,oldN)
    need(matmul(to_old,from_old)==I and matmul(from_old,to_old)==I,
         'L067_transports_inverse_both')
    write('basis.json', {'H':H,'basis':basis,'basis_to_power':bp,
        'power_to_basis':rational_strings(pb),
        'basis_to_L067':rational_strings(to_old),
        'L067_to_basis':rational_strings(from_old),
        'identity':[1]+[0]*47,
        'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest()})
    STATE['phase'] = 'products'
    table = []
    for i in range(n):
        row = []
        for j in range(n):
            p = [0]*95
            for k,x in enumerate(basis[i]):
                if x:
                    for l,y in enumerate(basis[j]):
                        if y: p[k+l] += x*y
            for k in range(94,47,-1):
                q,rem = divmod(p[k],a)
                need(rem==0,'integer_polynomial_reduction')
                if q:
                    for l,z in enumerate(H): p[k-48+l] -= q*z
            # Exact triangular conversion, including all zero slots.
            out = [0]*n
            for k in range(47,0,-1):
                q,rem = divmod(p[k],a)
                need(rem==0,'ring_closure_coefficient')
                out[k] = q
                if q:
                    for l in range(k+1): p[l] -= q*basis[k][l]
            out[0] = p[0]
            row.append(out)
            STATE['product_slots'] += 48
        table.append(row)
        write('product-%02d.json'%i,row)
    traces = [sum(table[i][j][j] for j in range(n)) for i in range(n)]
    gram = [[sum(x*y for x,y in zip(table[i][j],traces)) for j in range(n)]
            for i in range(n)]
    write('trace.json',{'traces':traces,'gram':gram,'entries':2304})
    STATE['phase'] = 'trace_determinant'
    d = determinant(gram,'trace-elimination')
    need(d!=0,'nonzero_order_discriminant')
    STATE['phase'] = 'polynomial_resultant'
    derivative = [k*H[k] for k in range(1,49)]
    desc,ddesc = H[::-1],derivative[::-1]
    sylvester = [[0]*k+desc+[0]*(46-k) for k in range(47)]
    sylvester += [[0]*k+ddesc+[0]*(47-k) for k in range(48)]
    res = determinant(sylvester,'resultant-elimination')
    pd,rem = divmod(res,a)  # (-1)^(48*47/2) = +1
    need(rem==0 and pd==d,'trace_resultant_discriminant_agreement')
    write('discriminant.json',{'order_discriminant':d,'resultant':res,
        'polynomial_discriminant':pd,'sign_exponent':1128,
        'leading_coefficient':a,'equal':True,'nonzero':d!=0,
        'decimal_digits':len(str(abs(d)))})
    STATE.update(status='PASS',phase='complete',basis_elements=48,
                 trace_entries=2304,discriminants_agree=True)

signal.signal(signal.SIGALRM,alarm)
signal.setitimer(signal.ITIMER_REAL,180)
try:
    main()
except Exception as exc:
    STATE.update(status='STOP',failure=type(exc).__name__+': '+str(exc))
finally:
    signal.setitimer(signal.ITIMER_REAL,0)
    STATE.update(seconds=time.monotonic()-START,required_seconds=180,
                 required_product_slots=110592,required_trace_entries=2304)
    write('producer-report.json',STATE)
    print(json.dumps(STATE))
sys.exit(0 if STATE['status']=='PASS' else 1)
