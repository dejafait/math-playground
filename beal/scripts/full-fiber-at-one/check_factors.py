"""Exact finite-field and local-factor evidence; ascending coefficients.

No package dependencies. Run from the active notebook. Complete evidence is
written before the compact summary. Further certification is documented in L038.
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


m = [-380,-774,-1062,-456,258,468,104,-126,-6,6,-6,0,1]
source = json.loads(Path('scripts/five-isogeny-modular-norm/norm-certificate.json').read_text())
F1 = source['polynomials_ascending']['F_at_1']
certificate = {'inputs': {'m': m, 'F1': F1}, 'residue_factorizations': {},
               'irreducibility_certificates': {}, 'coprimality_certificates': {},
               'decision': 'NONISOMORPHIC', 'failures': []}
for label, a in [('A',m), ('B1',F1)]:
    ff = factor(a)
    certificate['residue_factorizations'][label] = ff
    assert sum((len(f['coefficients'])-1)*f['multiplicity'] for f in ff) == 12
    assert all(f['multiplicity'] == 1 for f in ff)
    certificate['irreducibility_certificates'][label] = [
        irreducibility_certificate(f['coefficients']) for f in ff]
    left, right = [f['coefficients'] for f in ff]
    gcd, u, v = xgcd(left,right)
    identity = mod(add(mul(u,left),mul(v,right)))
    assert gcd == [1] and identity == [1]
    certificate['coprimality_certificates'][label] = {
        'bezout_u':u, 'bezout_v':v, 'identity':identity}
certificate['complete_factor_degrees'] = {
    label: sorted(len(f['coefficients'])-1 for f in ff)
    for label,ff in certificate['residue_factorizations'].items()}
assert certificate['complete_factor_degrees'] == {'A':[1,11], 'B1':[6,6]}
certificate['lifting_bounds'] = {
    'criterion':'monic integral polynomial with pairwise coprime residue blocks',
    'resultant_valuation_actual':{'A':0,'B1':0},
    'resultant_valuation_required':0,
    'approximate_precision_cutoff':None}
path = BASE/'factor-certificate.json'
path.write_text(json.dumps(certificate, indent=2)+'\n')
for label, ff in certificate['residue_factorizations'].items():
    print(label, 'mod 5 factors:', ff, 'dimension actual=12 required=12')
print('Certified complete degrees:',certificate['complete_factor_degrees'])
print('Coprime Hensel: resultant valuations actual=0 required=0; no precision cutoff')
print('Decision:', certificate['decision'], 'failures:', certificate['failures'])
print('Certificate:', path.relative_to(Path.cwd()))
