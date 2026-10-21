"""Distinct exact audit: no producer/verifier imports; standard library only."""
from fractions import Fraction as Q
from pathlib import Path
from math import lcm
import hashlib, json, signal, time

R = Path(__file__).resolve().parent
U = R.parent
start = time.monotonic()
signal.alarm(180)
checks = []
def need(ok, label):
    if not ok:
        raise ValueError(label)
    checks.append(label)
def read(p):
    return json.loads(p.read_text())
def mat(a):
    return [[Q(v) for v in row] for row in a]
def shape(a, n, m):
    return len(a) == n and all(len(r) == m for r in a)
def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]
def scale(a):
    d = lcm(*(v.denominator for row in a for v in row))
    return [[int(d*v) for v in row] for row in a], d
def product(a, b):
    # Clear denominators before every complete integer matrix product.
    assert len(a[0]) == len(b)
    aa, da = scale(a)
    bb, db = scale(b)
    columns = list(zip(*bb))
    return [[Q(sum(x*y for x,y in zip(row,col)), da*db)
             for col in columns] for row in aa]
def determinant(a):
    # Pivoted fraction-free Bareiss elimination after global scaling.
    b, d = scale(a)
    n = len(b); sign = 1; previous = 1
    for k in range(n-1):
        pivot = next((i for i in range(k,n) if b[i][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            b[k], b[pivot] = b[pivot], b[k]; sign = -sign
        p = b[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator = b[i][j]*p-b[i][k]*b[k][j]
                quotient, remainder = divmod(numerator,previous)
                assert remainder == 0
                b[i][j] = quotient
            b[i][k] = 0
        previous = p
    return Q(sign*b[-1][-1], d**n)
def evaluate(p,t):
    r = Q(0)
    for v in reversed(p):
        r = r*t+v
    return r

up = read(U/'certificate.json')
act = read(U/'scalar-actions-243/actions.json')
c = read(U/'compressed-249/direction.json')
f = list(map(Q,up['f']))
def reduce(p):
    r = list(p)
    while len(r)>24:
        v = r.pop()
        for i in range(24):
            r[len(r)-24+i] -= v*f[i]
    return r+[Q(0)]*(24-len(r))
def mul(a,b):
    r = [Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            r[i+j] += x*y
    return reduce(r)
def add(*ps):
    return [sum(p[i] for p in ps) for i in range(24)]
one = [Q(1)]+[Q(0)]*23
xs = [reduce(list(map(Q,act['maps'][str(i)]['X'][0]))) for i in (1,2,3)]
z = add(*xs)
need(z == reduce(list(map(Q,c['z']))), 'geometric_sum')
h = list(map(Q,c['h']))
need(h == list(map(Q,[-47414394214612992,2465179874131968,
    -63037439668224,1268096643072,-17283248640,69890688,
    -254016,0,1])), 'printed_polynomial_all_coefficients')
powers = [one]
for j in range(8):
    powers.append(mul(powers[-1],z))
need(all(reduce(list(map(Q,v))) == powers[j] for j,v in enumerate(c['powers']))
     and len(c['powers'])==9, 'all_saved_powers')
need(add(*[[v*x for x in p] for v,p in zip(h,powers)]) == [0]*24,
     'full_h_identity')
M = mat(c['mixed_matrix']); N = mat(c['mixed_inverse'])
need(shape(M,24,24) and shape(N,24,24), 'mixed_shapes')
columns = [reduce([Q(0)]*k+powers[j]) for k in range(3) for j in range(8)]
need(M == list(map(list,zip(*columns))), 'mixed_columns')
need(product(M,N)==eye(24) and product(N,M)==eye(24), 'mixed_inverse_both_orders')
q = [list(map(Q,p)) for p in c['cubic']]
need(len(q)==4 and q[-1]==[1] and all(len(p)<=8 for p in q[:3]),
     'all_cubic_degrees_and_monicity')
x3 = [[Q(i==3)] for i in range(24)]
v = product(N,x3)
need(all(q[k][j]==-v[8*k+j][0] for k in range(3) for j in range(8)),
     'cubic_is_complete_mixed_X3_coordinate')
def at_z(p):
    return add(*[[v*x for x in powers[j]] for j,v in enumerate(p)])
# Independent geometric relative characteristic polynomial: all three roots,
# retaining every coefficient, rather than just substitution U=X.
orbit_coeffs = [[-v for v in mul(mul(xs[0],xs[1]),xs[2])],
    add(mul(xs[0],xs[1]),mul(xs[0],xs[2]),mul(xs[1],xs[2])),
    [-v for v in z], one]
need([at_z(p) for p in q]==orbit_coeffs, 'full_three_root_orbit_cubic')

# Multiplication by z in C has characteristic polynomial h^3. Both sides
# have degree 24, so 25 exact rational evaluations certify the identity.
Z = list(map(list,zip(*[reduce([Q(0)]*j+z) for j in range(24)])))
rows=[]
for t in range(-12,13):
    actual=determinant([[Q(t*(i==j))-Z[i][j] for j in range(24)] for i in range(24)])
    required=evaluate(h,Q(t))**3
    need(actual==required, 'characteristic_evaluation_'+str(t))
    rows.append({'t':t,'determinant':str(actual),'h_cubed':str(required)})

EB,KB,RB,ET,KT,RT = [mat(c[k]) for k in ('E_B','K_B','R_B','E_T','K_T','R_T')]
for name,a,n,m in [('EB',EB,48,8),('KB',KB,8,48),('RB',RB,48,48),
                    ('ET',ET,48,8),('KT',KT,8,48),('RT',RT,48,48)]:
    need(shape(a,n,m),'shape_'+name)
need(EB==[row[:8] for row in M]+[[Q(0)]*8 for _ in range(24)],'whole_B_inclusion')
for model,E,K,P in [('B',EB,KB,RB),('T',ET,KT,RT)]:
    actions=[mat(act['maps'][str(a)][model+'_action']) for a in range(1,7)]
    need(all(shape(a,48,48) for a in actions),'all_six_action_shapes_'+model)
    mean=[[sum(a[i][j] for a in actions)/6 for j in range(48)] for i in range(48)]
    need(mean==P,'six_action_mean_'+model)
    need(product(E,K)==P and product(K,E)==eye(8),'both_image_products_'+model)
    need(product(P,P)==P and sum(P[i][i] for i in range(48))==8,
         'idempotence_trace_rank8_'+model)
    for a,A in enumerate(actions,1):
        need(product(A,E)==E,'fixed_all_columns_'+model+'_'+str(a))
oldM,oldN=mat(up['matrix']),mat(up['inverse'])
need(product(oldM,ET)==EB and product(oldN,EB)==ET,'both_inclusion_transports')
need(product(KB,oldM)==KT and product(KT,oldN)==KB,'both_retraction_transports')
need(product(product(oldN,RB),oldM)==RT,'projection_transport')

def mod_h(p):
    r=list(p)
    while len(r)>8:
        v=r.pop()
        for i in range(8):r[len(r)-8+i]-=v*h[i]
    return r+[Q(0)]*(8-len(r))
for i in range(8):
    for j in range(8):
        need(mul(powers[i],powers[j])==at_z(mod_h([Q(0)]*(i+j)+[Q(1)])),
             'product_'+str(i)+'_'+str(j))
report={'passed':True,'checks':checks,'failures':[],
        'characteristic_evaluations':rows,'actual_evaluations':25,'required_evaluations':25,
        'actual_fixed_rank':8,'required_fixed_rank':8,
        'mixed_rank':24,'required_mixed_rank':24,'direction_products':64,
        'seconds':time.monotonic()-start,'limit_seconds':180,
        'input_hashes':{str(p.relative_to(U)):hashlib.sha256(p.read_bytes()).hexdigest()
                       for p in [U/'certificate.json',U/'scalar-actions-243/actions.json',U/'compressed-249/direction.json']}}
with (R/'crosscheck.json').open('x') as out:json.dump(report,out,indent=2)
signal.alarm(0)
print(json.dumps({k:v for k,v in report.items() if k not in ('checks','characteristic_evaluations','input_hashes')}))
