"""Exact finite-field and local-factor evidence; ascending coefficients.

No package dependencies. Run from the active notebook. Complete evidence is
written before the compact summary. Further certification is documented in L039.
"""
from pathlib import Path
from itertools import product
import json

BASE = Path(__file__).resolve().parent


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a): c[i] += x
    for i, x in enumerate(b): c[i] += x
    return trim(c)


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] += x*y
    return trim(c)


def power(a, n):
    c = [1]
    for _ in range(n): c = mul(c, a)
    return c


def mod(a): return trim([x % 5 for x in a])


def divide(a, b):
    a = mod(a)
    q = [0]*max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        i = len(a)-len(b)
        t = a[-1]*pow(b[-1], -1, 5) % 5
        q[i] = t
        for j, x in enumerate(b): a[i+j] = (a[i+j]-t*x) % 5
        a = trim(a)
    return trim(q), a


def scale(a, t): return mod([t*x for x in a])


def xgcd(a, b):
    r0, r1 = mod(a), mod(b)
    u0, u1, v0, v1 = [1], [0], [0], [1]
    while r1 != [0]:
        q, r = divide(r0, r1)
        r0, r1 = r1, r
        u0, u1 = u1, mod(add(u0, scale(mul(q,u1), -1)))
        v0, v1 = v1, mod(add(v0, scale(mul(q,v1), -1)))
    c = pow(r0[-1], -1, 5)
    return scale(r0,c), scale(u0,c), scale(v0,c)


def powmod(a, n, modulus):
    r = [1]
    while n:
        if n % 2: r = divide(mul(r,a), modulus)[1]
        a = divide(mul(a,a), modulus)[1]
        n //= 2
    return r


def prime_divisors(n):
    return [q for q in range(2,n+1)
            if n % q == 0 and all(q % d for d in range(2,q))]


def irreducibility_certificate(g):
    n = len(g)-1
    x = [0,1]
    frobenius = [divide(x,g)[1]]
    for i in range(n): frobenius.append(powmod(frobenius[-1],5,g))
    witnesses = []
    for q in prime_divisors(n):
        i = n//q
        r = mod(add(frobenius[i], scale(x,-1)))
        gcd, u, v = xgcd(g,r)
        identity = mod(add(mul(u,g),mul(v,r)))
        assert gcd == [1] and identity == [1]
        witnesses.append({'prime_divisor':q, 'frobenius_index':i,
                          'remainder_minus_x':r, 'bezout_u':u,
                          'bezout_v':v, 'identity':identity})
    assert frobenius[-1] == frobenius[0]
    return {'degree':n, 'frobenius_remainders':frobenius,
            'proper_degree_tests':witnesses, 'final_remainder_minus_x':[0]}


def factor(a):
    """Trial monic divisors in increasing degree, exhaustive through n/2.

    When a divisor first succeeds it is irreducible: any proper monic divisor
    was already exhausted. Once degree d exceeds half the remaining degree,
    that remaining polynomial is irreducible. Multiplicities are retained.
    """
    left = mod(a)
    factors = []
    d = 1
    while 2*d <= len(left)-1:
        for coeff in product(range(5), repeat=d):
            b = list(coeff)+[1]
            count = 0
            while True:
                q, r = divide(left, b)
                if r != [0]: break
                left = q
                count += 1
            if count: factors.append({'coefficients': b, 'multiplicity': count})
        d += 1
    if len(left) > 1:
        factors.append({'coefficients': left, 'multiplicity': 1})
    check = [1]
    for f in factors: check = mul(check, power(f['coefficients'], f['multiplicity']))
    assert mod(check) == mod(a)
    return factors


def resultant(p, q):
    """Sylvester determinant via exact Bareiss elimination, with row swaps."""
    m, n = len(p)-1, len(q)-1
    size = m+n
    rows = []
    for i in range(n):
        rows.append([0]*i+list(reversed(p))+[0]*(n-i-1))
    for i in range(m):
        rows.append([0]*i+list(reversed(q))+[0]*(m-i-1))
    previous, sign = 1, 1
    for k in range(size-1):
        if not rows[k][k]:
            swap = next((i for i in range(k+1, size) if rows[i][k]), None)
            if swap is None:
                return 0
            rows[k], rows[swap] = rows[swap], rows[k]
            sign = -sign
        pivot = rows[k][k]
        for i in range(k+1, size):
            for l in range(k+1, size):
                num = pivot*rows[i][l]-rows[i][k]*rows[k][l]
                quotient, rem = divmod(num, previous)
                if rem:
                    raise ArithmeticError("inexact Bareiss division")
                rows[i][l] = quotient
            rows[i][k] = 0
        previous = pivot
    return sign*rows[-1][-1]


a = [-39176677684144739,108160113602504237,74593328129816300,
     420015065507429,-14545268641576841,-1895608370650736,
     576036867160006,82165362766027,2536749758583,19162005343,
     21559874,743]
b1 = [-707351591,271927184,65058492,1304157,4518,1]
b2 = [-37315543,-37789861,-3406817,3626752,192189,1]
b = mul(b1, b2)
g = [-20,-10,-1,1]
d = power([-16,1],11)
h = [9789217,4971236,1333262,-52820,1]
jcoef = [-104748564078368391,199736619430410535,159480622275659333,
         6839041777752481,-29669709666741936,-4074814667347831,
         1134855511654843,164063633585170,5072626276355,38323813979,
         43119747,1486]
F2 = add(add(power(h,3), [2*x for x in jcoef]), [-4*x for x in d])
assert add([2*x for x in a], [-x for x in b]) == jcoef
assert add(add(mul(a,a), [-x for x in mul(a,b)]), [-x for x in mul(mul(b,b),g)]) == [-x for x in mul(d,power(h,3))]
F2prime = [i*F2[i] for i in range(1,len(F2))]
def ev(p,x):
    r=0
    for c in reversed(p): r=r*x+c
    return r
coordinate = {'F2_at_16': ev(F2,16), 'resultant_F2_b':resultant(F2,b),
              'resultant_F2_derivative':resultant(F2,F2prime),
              'elimination_identity_verified': True}
assert all(coordinate[k] != 0 for k in ['F2_at_16','resultant_F2_b','resultant_F2_derivative'])
ff = factor(F2)
cert = {'inputs':{'F2':F2,'a':a,'b':b,'d':d,'h':h,'J':jcoef},
        'coordinate':coordinate,'residue_factors':ff,'irreducibility':[],
        'coprimality':[], 'failures':[]}
assert all(f['multiplicity']==1 for f in ff)
for f in ff: cert['irreducibility'].append(irreducibility_certificate(f['coefficients']))
for i in range(len(ff)):
    for j in range(i+1,len(ff)):
        l,r=ff[i]['coefficients'],ff[j]['coefficients']
        gcd,u,v=xgcd(l,r)
        ident=mod(add(mul(u,l),mul(v,r)))
        assert gcd==ident==[1]
        cert['coprimality'].append({'indices':[i,j],'u':u,'v':v,'identity':ident})
degrees=sorted(len(f['coefficients'])-1 for f in ff)
assert sum(degrees)==12
cert['complete_degrees']={'A_reused_L038':[1,11],'B2':degrees}
cert['decision']='NONISOMORPHIC' if degrees != [1,11] else 'ISOMORPHIC_UNRAMIFIED'
cert['bounds']={'dimension_actual':sum(degrees),'dimension_required':12,
                'pairwise_resultant_valuation_actual':0,'pairwise_resultant_valuation_required':0,
                'precision_cutoff':None}
path=BASE/'factor-certificate.json'
path.write_text(json.dumps(cert,indent=2)+'\n')
print('Coordinate completeness: all three exact nonzero checks passed')
print('B2 residue factors:',ff)
print('Complete degrees:',cert['complete_degrees'],'dimension actual=12 required=12')
print('Coprime Hensel: resultant valuation actual=0 required=0; no precision cutoff')
print('Decision:',cert['decision'],'failures:',cert['failures'])
print('Certificate:',path.relative_to(Path.cwd()))
