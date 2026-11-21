#!/usr/bin/env python3
"""Fixed quartic first-zero/curvature certificate; no floating quadrature."""
import decimal
from decimal import Decimal as D
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import platform

OUT = Path(__file__).with_suffix('.json')
PREC, N, CAP, MESH = 70, 2048, 8, 32
dn, up, near = [decimal.Context(prec=PREC, rounding=r,
                               Emin=-999999, Emax=999999)
                for r in (decimal.ROUND_FLOOR, decimal.ROUND_CEILING,
                          decimal.ROUND_HALF_EVEN)]
for c in (dn, up, near):
    for signal in c.traps:
        c.traps[signal] = signal not in (decimal.Inexact, decimal.Rounded)


def rat(q):
    q = F(q)
    return dn.divide(D(q.numerator), D(q.denominator)), up.divide(D(q.numerator), D(q.denominator))


def pack(a):
    return {'lower': str(a[0]), 'upper': str(a[1])}


def add(a, b):
    return dn.add(a[0], b[0]), up.add(a[1], b[1])


def neg(a):
    return a[1].copy_negate(), a[0].copy_negate()


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    return (min(dn.multiply(x, y) for x in a for y in b),
            max(up.multiply(x, y) for x in a for y in b))


def inflate(a, e):
    return dn.subtract(a[0], e), up.add(a[1], e)


def expq(q):
    a = rat(q)
    return dn.next_minus(near.exp(a[0])), up.next_plus(near.exp(a[1]))


def sc_step(z):
    # Taylor through degree25, |z|<=1/64; common order26 remainder.
    assert 0 <= z <= F(1, 64)
    s = sum(((-1)**j * z**(2*j+1) / factorial(2*j+1) for j in range(13)), F(0))
    c = sum(((-1)**j * z**(2*j) / factorial(2*j) for j in range(13)), F(0))
    e = rat(z**26 / factorial(26))[1]
    return inflate(rat(s), e), inflate(rat(c), e)


def polynomial_next(p):
    q = [0] * (len(p)+3)
    for i, a in enumerate(p):
        if i:
            q[i-1] += i*a
        q[i+1] -= 2*a
        q[i+3] -= 4*a
    return q


P = [[1]]
for j in range(4):
    P.append(polynomial_next(P[-1]))


def monomial_bound(m):
    # For t<=1 use1. For t>=1, t^m exp(-t^4-t^2)
    # <=t^(4k)exp(-t^4) <=(k/e)^k <=(k/2)^k.
    k = (m+3)//4
    return max(F(1), F(k, 2)**k) if k else F(1)


def polynomial_bound(p, shift=0):
    return sum((abs(a)*monomial_bound(i+shift) for i, a in enumerate(p)), F(0))


BK = [polynomial_bound(p) for p in P]
BTK = [polynomial_bound(p, 1) + (j*polynomial_bound(P[j-1]) if j else 0)
       for j, p in enumerate(P)]
# These bound |K^(j)| and |(t K)^(j)| on the complete real half-line.
D4 = sum(F(comb(4, j))*CAP**(4-j)*BK[j] for j in range(5))
D4t = sum(F(comb(4, j))*CAP**(4-j)*BTK[j] for j in range(5))
H = F(4, N)
errF = rat(F(4)*H**4*D4/180)[1]
errFp = rat(F(4)*H**4*D4t/180)[1]
errShift = rat(F(3)*H**4*D4/180)[1]
# V'(t)=4t^3+2t >=264 for t>=4; K(4)=exp(-272).
tailF = mul(expq(-272), rat(F(1, 264)))[1]
tailFp = mul(expq(-272), rat(F(4, 264)+F(1, 264**2)))[1]

nodes = []
for i in range(N+1):
    t = H*i
    nodes.append((t, expq(-t**4-t**2)))


def integrate(x, start=0, derivative=False, sine=False):
    assert 0 <= x <= CAP
    step_s, step_c = sc_step(x*H)
    s, c = rat(0), rat(1)
    acc = rat(0)
    for i in range(start, N+1):
        t, k = nodes[i]
        trig = s if sine else c
        term = mul(k, trig)
        if derivative:
            term = mul(term, rat(-t))
        w = 1 if i in (start, N) else (4 if (i-start) % 2 else 2)
        acc = add(acc, mul(rat(w), term))
        s, c = add(mul(s, step_c), mul(c, step_s)), sub(mul(c, step_c), mul(s, step_s))
    ans = mul(rat(H/3), acc)
    error = errFp if derivative else (errShift if start else errF)
    tail = tailFp if derivative else tailF
    return inflate(ans, up.add(error, tail))


certificate = {
    'status': 'RUNNING', 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'runtime': {'python': platform.python_version(), 'libmpdec': decimal.__libmpdec_version__,
                'precision': PREC},
    'contracts': ['correct integer/Fraction arithmetic', 'directed Decimal basic operations',
                  'correctly rounded HALF_EVEN exp and outward neighbor steps'],
    'setup': {'kernel': 'exp(-u^4-u^2)', 'u': 1, 'cap': CAP, 'mesh': '1/32',
              'panels': N, 'finite_interval': '[0,4]', 'shift_interval': '[1,4]',
              'bisections_max': 10, 'trig_degree': 25, 'trig_remainder_order': 26},
    'bounds': {'K_derivative_polynomials': P, 'BK': list(map(str, BK)),
               'BtK': list(map(str, BTK)), 'D4': str(D4), 'D4t': str(D4t),
               'simpson_F': str(errF), 'simpson_Fprime': str(errFp),
               'simpson_shift': str(errShift), 'tail_F': str(tailF), 'tail_Fprime': str(tailFp),
               'Fsecond_abs': '1', 'shift_frequency_Lipschitz': '1/2'},
    'census': [], 'bisection': [], 'failures': [],
}


def save():
    OUT.write_text(json.dumps(certificate, indent=2)+'\n')


def require(test, message):
    if not test:
        certificate['failures'].append(message)
        certificate['status'] = 'FAILED_SETUP'
        save()
        raise RuntimeError(message)


save()
values = []
for i in range(CAP*MESH+1):
    x = F(i, MESH)
    val = integrate(x)
    values.append(val)
    if i == 0:
        require(val[0] > 0, 'F(0) positivity failed')
        continue
    cell = {'left': str(x-F(1, MESH)), 'right': str(x),
            'F_left': pack(values[-2]), 'F_right': pack(val)}
    interpolation_lower = dn.subtract(min(values[-2][0], val[0]), rat(F(1, 8*MESH**2))[1])
    cell['interpolation_lower'] = str(interpolation_lower)
    if val[1] < 0 or interpolation_lower <= 0:
        center = x-F(1, 2*MESH)
        fp = integrate(center, derivative=True, sine=True)
        upper = up.add(fp[1], rat(F(1, 2*MESH))[1])
        cell['Fprime_midpoint'] = pack(fp)
        cell['Fprime_cell_upper'] = str(upper)
        require(upper < 0, 'No rigorous monotonicity for cell '+str(i))
        if val[1] < 0:
            require(values[-2][0] > 0, 'left crossing endpoint not strictly positive')
            cell['result'] = 'UNIQUE_FIRST_ZERO_CELL'
            certificate['census'].append(cell)
            lo, hi = x-F(1, MESH), x
            break
        require(val[0] > 0, 'ambiguous mesh sign')
        cell['result'] = 'POSITIVE_BY_DECREASE'
    else:
        require(val[0] > 0, 'ambiguous mesh sign')
        cell['result'] = 'POSITIVE_BY_INTERPOLATION'
    certificate['census'].append(cell)
    if i % 32 == 0:
        save()
else:
    require(False, 'no first-zero bracket within cap8')

for j in range(10):
    mid = (lo+hi)/2
    val = integrate(mid)
    record = {'point': str(mid), 'F': pack(val)}
    if val[0] > 0:
        lo = mid
        record['sign'] = 'positive'
    elif val[1] < 0:
        hi = mid
        record['sign'] = 'negative'
    else:
        record['sign'] = 'unresolved_stop'
        certificate['bisection'].append(record)
        break
    certificate['bisection'].append(record)

center = (lo+hi)/2
radius = (hi-lo)/2
aa = inflate(integrate(center, start=N//4, sine=True), rat(radius/2)[1])
bb = inflate(integrate(center, start=N//4), rat(radius/2)[1])
xx = (rat(lo)[0], rat(hi)[1])
xx2 = mul(xx, xx)
g = mul(xx, aa)
gp = neg(mul(xx2, bb))
gpp = mul(xx2, sub(expq(-2), g))
delta = sub(mul(g, gpp), mul(gp, gp))
certificate['root'] = {'lower': str(lo), 'upper': str(hi), 'center': str(center),
                       'radius': str(radius), 'F_lower': pack(integrate(lo)),
                       'F_upper': pack(integrate(hi)), 'simple': True}
certificate['curvature'] = {'A_sine': pack(aa), 'B_cosine': pack(bb),
                             'G': pack(g), 'Gprime': pack(gp), 'Gsecond': pack(gpp),
                             'Delta': pack(delta), 'required_for_refutation': 'Delta.lower>0'}
require(g[0] > 0, 'numerical G lower bound failed')
certificate['status'] = ('POSITIVE_CURVATURE' if delta[0] > 0 else
                         'NONPOSITIVE_CURVATURE' if delta[1] <= 0 else 'INCONCLUSIVE_CURVATURE')
save()
print('status:', certificate['status'])
print('first zero:', lo, hi, '; required: (0,8), all preceding cells positive')
print('Delta:', delta, '; refutation requires lower>0')
print('Simpson errors F/Fprime/shift:', errF, errFp, errShift)
print('failures:', certificate['failures'])
print('certificate:', OUT)
