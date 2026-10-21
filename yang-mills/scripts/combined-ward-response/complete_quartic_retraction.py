"""Exact finite gauge-jet/tilt checks; not a mesh asymptotic computation."""

from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

DEG = 4
ZQ = (F(0),) * 4
IQ = (F(1), F(0), F(0), F(0))


def add(*vs):
    return tuple(map(sum, zip(*vs)))


def scale(a, v):
    return tuple(a * x for x in v)


def bracket(v, w):
    return (v[2]*w[1]-v[1]*w[2], v[0]*w[2]-v[2]*w[0],
            v[1]*w[0]-v[0]*w[1])


def qm(q, r):
    s, v, t, w = q[0], q[1:], r[0], r[1:]
    return (s*t-sum(a*b for a, b in zip(v, w))/4,
            *add(scale(s, w), scale(t, v), scale(F(1, 2), bracket(v, w))))


def pm(p, q):
    return [add(*(qm(p[j], q[n-j]) for j in range(n+1)))
            for n in range(DEG+1)]


def unit():
    return [IQ] + [ZQ]*DEG


def exp_series(vs):
    x = [ZQ] + [(F(0), *v) for v in vs]
    x += [ZQ] * (DEG+1-len(x))
    out, power = unit(), unit()
    for k in range(1, DEG+1):
        power = pm(power, x)
        out = [add(a, scale(F(1, factorial(k)), b))
               for a, b in zip(out, power)]
    return out


def log_series(u):
    v = [add(u[0], scale(-1, IQ)), *u[1:]]
    out, power = [ZQ]*(DEG+1), unit()
    for k in range(1, DEG+1):
        power = pm(power, v)
        out = [add(a, scale(F((-1)**(k+1), k), b))
               for a, b in zip(out, power)]
    return out


def bch3(p, y, q):
    return add(
        scale(F(1, 12), bracket(p, bracket(p, y))),
        scale(F(1, 12), bracket(y, bracket(y, p))),
        scale(F(1, 4), bracket(bracket(p, y), q)),
        scale(F(1, 12), bracket(add(p, y), bracket(add(p, y), q))),
        scale(F(1, 12), bracket(q, bracket(q, add(p, y)))))


def probe(rows, degree):
    product = unit()
    for row in rows:
        product = pm(product, exp_series([row]))
    return -product[degree][0]  # 1 - Tr(loop)/2 at positive degree


records = []
load_bearing = [False]*3
for k in range(1, 9):
    potentials = [tuple(F(((k+2*i+3*j)*(i+j+1)) % 9-4, j+1)
                        for j in range(3)) for i in range(4)]
    ys = [tuple(F(((2*k+i+2*j)*(i+2)) % 11-5, i+1)
                for j in range(3)) for i in range(4)]
    zs, bs, cs = [], [], []
    for i in range(4):
        p, y, q = scale(-1, potentials[i]), ys[i], potentials[(i+1) % 4]
        z = add(p, y, q)
        b = scale(F(1, 2), add(bracket(p, y), bracket(p, q), bracket(y, q)))
        c = bch3(p, y, q)
        transformed = pm(pm(exp_series([p]), exp_series([y])), exp_series([q]))
        logarithm = log_series(transformed)
        assert logarithm[1] == (F(0), *z)
        assert logarithm[2] == (F(0), *b)
        assert logarithm[3] == (F(0), *c)
        zs.append(z)
        bs.append(b)
        cs.append(c)
    d3b = (probe([add(z, b) for z, b in zip(zs, bs)], 3)
           -probe([add(z, scale(-1, b)) for z, b in zip(zs, bs)], 3))/2-probe(bs, 3)
    b2 = probe(bs, 2)
    zc2 = probe([add(z, c) for z, c in zip(zs, cs)], 2)-probe(zs, 2)-probe(cs, 2)
    lhs, base = probe(ys, 4), probe(zs, 4)
    rhs = base+d3b+b2+zc2
    assert lhs == rhs
    for j, v in enumerate((d3b, b2, zc2)):
        load_bearing[j] |= bool(v)
    records.append(dict(case=k, lhs=str(lhs), full_coordinate_quartic=str(base),
                        cubic_derivative=str(d3b), quadratic_b=str(b2),
                        cubic_log=str(zc2), defect=str(lhs-rhs)))
assert all(load_bearing)

# Independent Gaussian moments: z=(X,X+2Y) is correlated; the second
# fixture is singular. Compute moments directly in independent X,Y.
def pa(*polys):
    result = {}
    for p in polys:
        for key, v in p.items():
            result[key] = result.get(key, F(0))+v
    return {key: v for key, v in result.items() if v}


def ps(c, p):
    return {key: c*v for key, v in p.items() if c*v}


def pp(p, q):
    result = {}
    for (i, j), v in p.items():
        for (k, l), w in q.items():
            key = (i+k, j+l)
            result[key] = result.get(key, F(0))+v*w
    return {key: v for key, v in result.items() if v}


def power(p, n):
    out = {(0, 0): F(1)}
    for _ in range(n):
        out = pp(out, p)
    return out


def moment(p):
    def one(n):
        if n % 2:
            return 0
        out = 1
        for i in range(1, n, 2):
            out *= i
        return out
    return sum(v*one(i)*one(j) for (i, j), v in p.items())


tilts = []
X, Y = {(1, 0): F(1)}, {(0, 1): F(1)}
for second in (pa(X, ps(2, Y)), ps(2, X)):
    z = [X, second]
    S = [[moment(pp(v, w)) for w in z] for v in z]
    A = [[F(2), F(-1)], [F(-1), F(1, 3)]]
    t = [pa(*(ps(2*S[i][j]*A[j][k], z[k]) for j in range(2) for k in range(2)))
         for i in range(2)]
    # P(z)=z0^4 + 3 z0^2 z1^2 - 2 z0 z1^3 + z1^4
    terms = [(F(1), 4, 0), (F(3), 2, 2), (F(-2), 1, 3), (F(1), 0, 4)]
    p = pa(*(ps(c, pp(power(z[0], i), power(z[1], j))) for c, i, j in terms))
    dp = {}
    for c, i, j in terms:
        if i:
            dp = pa(dp, ps(c*i, pp(pp(power(z[0], i-1), power(z[1], j)), t[0])))
        if j:
            dp = pa(dp, ps(c*j, pp(pp(power(z[0], i), power(z[1], j-1)), t[1])))
    residual = pa(*(ps(A[i][j], pp(z[i], z[j])) for i in range(2) for j in range(2)))
    cov = moment(pp(p, residual))-moment(p)*moment(residual)
    rhs = moment(dp)/2
    assert cov == rhs and cov != 0
    tilts.append(dict(covariance=[[str(v) for v in row] for row in S],
                      direct_covariance=str(cov), half_derivative=str(rhs),
                      without_half=str(moment(dp)), defect=str(cov-rhs)))

output = Path(__file__).with_name('complete-quartic-retraction-certificate.json')
certificate = dict(kind='exact rational finite algebra; no cutoff estimate',
                   gauge_fixtures=records, omitted_term_controls=load_bearing,
                   gaussian_tilt_fixtures=tilts, failures=[])
output.write_text(json.dumps(certificate, indent=2)+'\n')
print('Gauge/BCH fixtures: 8/8 pass; each of three correction types is nonzero in a fixture.')
print('Quadratic-tilt normalization: 2/2 correlated/singular moment checks pass; factor 1/2 required.')
print('Actual bound: finite signed identity only; required bound O(N^3) and limit remain unproved.')
print('Failures: 0. Certificate:', output)
