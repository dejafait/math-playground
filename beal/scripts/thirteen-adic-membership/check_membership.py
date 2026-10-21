"""Exact finite-field certificates for one bounded thirteen-adic witness test.

No p-adic approximations. Canonical lifting arguments are documented separately.
"""
import ast
import json
from pathlib import Path

P = 13
ROOT = Path(__file__).resolve().parents[2]

def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a): c[i] += x
    for i, x in enumerate(b): c[i] += x
    return trim([x % P for x in c])

def scale(a, t): return trim([x*t % P for x in a])

def mul(a, b):
    c = [0] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] += x*y
    return trim([x % P for x in c])

def divide(a, b):
    a = scale(a, 1)
    q = [0] * max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        i = len(a)-len(b)
        t = a[-1]*pow(b[-1], -1, P) % P
        q[i] = t
        for j, x in enumerate(b): a[i+j] = (a[i+j]-t*x) % P
        a = trim(a)
    return trim(q), a

def gcd(a, b):
    while b != [0]: a, b = b, divide(a,b)[1]
    return scale(a, pow(a[-1], -1, P))

def power(a, n, m=None):
    out = [1]
    while n:
        if n & 1:
            out = mul(out, a)
            if m: out = divide(out,m)[1]
        a = mul(a,a)
        if m: a = divide(a,m)[1]
        n //= 2
    return out

def derivative(a): return scale([i*a[i] for i in range(1,len(a))],1)

def split_equal(f, d):
    if len(f)-1 == d: return [f]
    # Deterministic candidate enumeration; every split is verified by division.
    for seed in range(1, P**(len(f)-1)):
        n, candidate = seed, []
        while n:
            candidate.append(n % P); n //= P
        g = gcd(f, candidate)
        if len(g) in (1,len(f)):
            g = gcd(f, add(power(candidate,(P**d-1)//2,f),[-1]))
        if 1 < len(g) < len(f):
            q, r = divide(f,g)
            assert r == [0]
            return split_equal(g,d) + split_equal(q,d)
    raise RuntimeError('No equal-degree split found')

def factor(f):
    f = scale(f,pow(f[-1],-1,P))
    assert gcd(f,derivative(f)) == [1], 'Repeated residue factors require refinement'
    rem, out, d = f, [], 1
    while len(rem)-1 >= 2*d:
        block = gcd(rem,add(power([0,1],P**d,rem),[0,-1]))
        if len(block)>1:
            out.extend(split_equal(block,d))
            rem, residue = divide(rem,block)
            assert residue == [0]
        d += 1
    if len(rem)>1: out.append(rem)
    out.sort(key=lambda q:(len(q),q))
    prod=[1]
    for q in out: prod=mul(prod,q)
    assert prod==f
    return out

def irreducibility(f):
    n=len(f)-1
    xs=[divide([0,1],f)[1]]
    for _ in range(n): xs.append(power(xs[-1],P,f))
    witnesses=[]
    for q in range(2,n+1):
        if n%q==0 and all(q%i for i in range(2,q)):
            r=add(xs[n//q],[0,-1]); g=gcd(f,r)
            assert g==[1]
            witnesses.append({'prime':q,'remainder_minus_x':r,'gcd':g})
    assert xs[-1]==xs[0]
    return {'factor':f,'degree':n,'frobenius_remainders':xs,'gcd_tests':witnesses}

def inv(a,m):
    # Only called in a field; the irreducibility certificate is retained.
    assert divide(a,m)[1]!=[0]
    return power(a,P**(len(m)-1)-2,m)

def evalpoly(a,x,m):
    r=[0]
    for c in reversed(a): r=divide(add(mul(r,x),[c]),m)[1]
    return r

def valuation(n):
    if n == 0: return None
    v=0
    while n%P==0: n//=P; v+=1
    return v

source=ROOT/'scripts/five-isogeny-modular-norm/check_norm.py'
data={}
for node in ast.parse(source.read_text()).body:
    if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name):
        name=node.targets[0].id
        if name in {'a','b1','b2','h','jcoef'}:
            data[name]=ast.literal_eval(node.value)
a=scale(data['a'],1); b=mul(data['b1'],data['b2'])
h=scale(data['h'],1); J=scale(data['jcoef'],1); d=power([-16,1],11)
K=[-380,-774,-1062,-456,258,468,104,-126,-6,6,-6,0,1]
kf=factor(K)
kc=[irreducibility(f) for f in kf]
cubes=sorted({a**3%P for a in range(1,P)})
fourths=sorted({b**4%P for b in range(1,P)})
unit_witnesses={}
for aa in range(1,P):
    for bb in range(1,P):
        cc=next((c for c in range(1,P) if (aa**3+bb**4-c**11)%P==0),None)
        if cc is not None:
            s=1728*aa**3*pow(cc**11,-1,P)%P
            unit_witnesses.setdefault(s,[aa,bb,cc])
fibers=[]
for s,witness in sorted(unit_witnesses.items()):
    F=add(add(power(h,3),scale(J,s)),scale(d,-s*s))
    factors=factor(F)
    certs=[irreducibility(f) for f in factors]
    points=[]
    for f in factors:
        x=divide([0,1],f)[1]
        br=evalpoly(b,x,f)
        if br==[0]:
            points.append({'factor':f,'reconstruction':'BLOCKED: zero b'})
            continue
        y=divide(mul(add(scale(evalpoly(d,x,f),s),scale(evalpoly(a,x,f),-1)),inv(br,f)),f)[1]
        curve=divide(add(add(mul(y,y),y),scale(evalpoly([-20,-10,-1,1],x,f),-1)),f)[1]
        fv=divide(add(mul(add(x,[-4]),y),evalpoly([-55,30,-4],x,f)),f)[1]
        assert curve==[0]
        points.append({'factor':f,'x':x,'y':y,'curve_residual':curve,'f_value':fv,
                       'fifth_power_trivial': (fv!=[0] and power(fv,(P**(len(f)-1)-1)//5,f)==[1]) if (P**(len(f)-1)-1)%5==0 else fv!=[0]})
    fibers.append({'scalar_residue':s,'primitive_unit_residues':witness,'polynomial':F,
                   'factors':certs,'degrees':[len(f)-1 for f in factors],'points':points})
Fbranch=add(add(power(h,3),scale(J,1728)),scale(d,-1728**2))
G=gcd(Fbranch,derivative(Fbranch))
assert mul(G,G)==Fbranch
gc=irreducibility(G)
x=divide([0,1],G)[1]
br=evalpoly(b,x,G)
yr=divide(mul(add(scale(evalpoly(d,x,G),1728),scale(evalpoly(a,x,G),-1)),inv(br,G)),G)[1]
fr=divide(add(mul(add(x,[-4]),yr),evalpoly([-55,30,-4],x,G)),G)[1]
assert fr!=[0]
wr=power(fr,pow(5,-1,P**6-1),G)
target=next(f for f in fibers if f['scalar_residue']==3)
M=target['factors'][0]['factor']; fv=target['points'][0]['f_value']
N=(P**12-1)//5
assert N%5 and power(fv,N,M)==[1]
wv=power(fv,pow(5,-1,N),M)
primitive={'b':2,'a_cubed':[16,575],'c_eleventh':[9216,575],
           'a_start':1,'c_start':10,
           'a_polynomial_value':[559,575],
           'c_polynomial_value':[575*10**11-9216,575],
           'a_value_valuation':valuation(559),
           'c_value_valuation':valuation(575*10**11-9216),
           'a_derivative_residue':3,'c_derivative_residue':11*pow(10,10,P)%P}
checks={
    'K_complete_irreducible_degree12':len(kf)==1 and len(kf[0])==13,
    'canonical_branch_square_degree6':len(G)==7 and mul(G,G)==Fbranch,
    'canonical_reconstruction_b_unit':gcd(b,G)==[1],
    'canonical_reconstruction_d_unit':gcd(d,G)==[1],
    'canonical_curve_residual':divide(add(add(mul(yr,yr),yr),scale(evalpoly([-20,-10,-1,1],x,G),-1)),G)[1]==[0],
    'canonical_fifth_root_identity':power(wr,5,G)==fr,
    'target_complete_irreducible_degree12':target['degrees']==[12],
    'target_b_unit':gcd(b,M)==[1],
    'target_d_unit':gcd(d,M)==[1],
    'target_curve_residual':target['points'][0]['curve_residual']==[0],
    'target_fifth_root_identity':power(wv,5,M)==fv,
    'a_strict_hensel':primitive['a_value_valuation']>0 and primitive['a_derivative_residue']!=0,
    'c_strict_hensel':primitive['c_value_valuation']>0 and primitive['c_derivative_residue']!=0,
    'shared_power_sum':16+16*575==9216,
    'scalar_exactly_three':1728*16==3*9216,
    'both_curves_good_reduction':(-11**5)%P!=0 and (-11)%P!=0,
}
cert={'prime':P,'K_polynomial_mod13':scale(K,1),'K_factors':kc,'K_degrees':[len(f)-1 for f in kf],
      'unit_cubes':cubes,'unit_fourths':fourths,'primitive_regular_residue_fibers':fibers,
      'canonical_branch':{'polynomial':Fbranch,'square_factor':gc,'b_gcd':gcd(b,G),'d_gcd':gcd(d,G),
                          'y_residue':yr,'f_residue':fr,'fifth_root_residue':wr,'fifth_root_check':power(wr,5,G)},
      'target_scalar_three':{'polynomial':M,'b_gcd':gcd(b,M),'d_gcd':gcd(d,M),
                             'f_residue':fv,'fifth_root_residue':wv,'fifth_root_check':power(wv,5,M),
                             'residue_order':P**12-1,'order_over_five':N,
                             'fifth_root_exponent':pow(5,-1,N)},
      'primitive_power_witness':primitive,'checks':checks,
      'required_full_degree':12,'failures':[n for n,v in checks.items() if not v],
      'qualification':'Factor lifting, entire-fiber reconstruction and class comparison require the canonical mathematical proof; no integer solution or full local image is claimed.'}
out=Path(__file__).resolve().with_name('membership-certificate.json')
out.write_text(json.dumps(cert,indent=2)+'\n')
print('Checks passed:',sum(checks.values()),'/',len(checks))
print('Full K and scalar-three degrees actual=12 required=12; canonical branch degree actual=6 squared required=12.')
print('Exact residue fifth-root identities: canonical=True target=True; Hensel valuations actual=',primitive['a_value_valuation'],primitive['c_value_valuation'],'required>0.')
print('Failures:',cert['failures'],'certificate:',out.relative_to(ROOT))
if cert['failures']: raise SystemExit(1)
