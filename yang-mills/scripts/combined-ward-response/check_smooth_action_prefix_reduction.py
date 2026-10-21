"""Exact finite checks for L175; no cutoff or actual-probe inference."""
from fractions import Fraction as F
from pathlib import Path
import json


def tp(a):
    return [list(r) for r in zip(*a)]


def mm(a, b):
    return [[sum(x*y for x, y in zip(r, c)) for c in zip(*b)] for r in a]


def chain(*xs):
    a = xs[0]
    for b in xs[1:]:
        a = mm(a, b)
    return a


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def add(a, b, sign=1):
    return [[x+sign*y for x, y in zip(r, s)] for r, s in zip(a, b)]


def inv(a):
    n = len(a)
    v = [list(map(F, r))+s for r, s in zip(a, eye(n))]
    for i in range(n):
        p = next(j for j in range(i, n) if v[j][i])
        v[i], v[p] = v[p], v[i]
        z = v[i][i]
        v[i] = [x/z for x in v[i]]
        for j in range(n):
            if j != i:
                z = v[j][i]
                v[j] = [x-z*y for x, y in zip(v[j], v[i])]
    return [r[n:] for r in v]


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def diag(v):
    return [[F(v[i]) if i == j else F(0) for j in range(len(v))] for i in range(len(v))]


def mv(a, v):
    return [sum(x*y for x, y in zip(r, v)) for r in a]


def kron(a, b):
    return [[a[i][j]*b[r][s] for j in range(len(a[0])) for s in range(len(b[0]))]
            for i in range(len(a)) for r in range(len(b))]


def bracket(a, b):
    return [a[2]*b[1]-a[1]*b[2], a[0]*b[2]-a[2]*b[0], a[1]*b[0]-a[0]*b[1]]


# The pinned two-cycle graph from L159, with all normal end edges retained.
d = [[1, 0, 0], [-1, 1, 0], [0, -1, 1], [0, 0, -1], [0, 1, 0]]
s = [[1, 0, 0], [1, 1, 0], [0, 1, 1], [0, 0, 1], [0, 1, 0]]
cycles = tp([[1, 1, 1, 1, 0], [1, 1, 0, 0, -1]])
l = chain(cycles, tp(cycles))
a = chain(cycles, [[2, -1], [-1, 3]], tp(cycles))
q3 = chain(cycles, [[1, 0], [0, -2]], tp(cycles))
q6 = chain(cycles, [[0, 1], [1, 0]], tp(cycles))
agen = add(add(a, q3), q6)
sigma = inv(add(l, chain(d, tp(d))))
phi = [[1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 0, 0]]
r = add(eye(5), chain(d, phi), -1)
k = chain(phi, sigma, tp(phi))
f = chain(phi, sigma)
hat = lambda x: kron(x, eye(3))
identities, inequalities, cases = [], [], []


def check(name, actual, required):
    identities.append(dict(name=name, actual=actual, required=required,
                           exact_error=actual-required))


for number, (v, w) in enumerate([
        ([1, 2, -1, 3, 2], [2, -1, 4, 1, -2]),
        ([-2, 1, 3, -4, 1], [3, 2, -1, 5, 4])], 1):
    h, ell = mv(r, v), mv(r, w)
    q = mv(l, ell)
    mh, mq = diag(h), diag(q)
    oq = chain(tp(s), mq, d)
    direct = 6*tr(chain(sigma, a, mh, s, k, tp(s), mq))
    prefix = lambda b: -6*tr(chain(k, oq, f, b, mh, s))
    scalar = 6*tr(chain(sigma, a, mh, s, k, tp(s), mq, r))
    colored = F(0)
    for color in range(3):
        tc = [int(j == color) for j in range(3)]
        bc = tp([bracket(tc, e) for e in eye(3)])
        bh, bq = kron(chain(mh, s), bc), kron(chain(mq, s), bc)
        colored += tr(chain(hat(sigma), hat(a), bh, hat(k), tp(bq), hat(r)))
    check(f'case {number}: full color normalization', colored, scalar)
    check(f'case {number}: ordered direct/prefix split', scalar, direct+prefix(a))
    check(f'case {number}: both signed Q subtractions', scalar,
          direct+prefix(agen)-prefix(q3)-prefix(q6))
    gram = tr(chain(k, oq, phi, sigma, tp(phi), tp(oq)))
    check(f'case {number}: prefix Gram identity', gram, tr(chain(k, oq, k, tp(oq))))
    check(f'case {number}: complete action transport skew',
          sum(x*x for row in add(oq, tp(oq)) for x in row), F(0))
    u = chain(mq, s, k, tp(s), mq)
    norm_squared = tr(chain(sigma, u))
    actual = norm_squared**2
    required = tr(chain(sigma, sigma))*tr(chain(u, u))
    inequalities.append(dict(name=f'case {number}: direct squared trace Cauchy-Schwarz',
                             direct_squared_HS=norm_squared, actual=actual,
                             required_upper_bound=required,
                             passed=0 <= actual <= required))
    cases.append(dict(h=h, ell=ell, q=q, O_q=oq, direct=direct,
                      prefix=prefix(a), full=scalar,
                      generator_prefix=prefix(agen), Q3_prefix=prefix(q3),
                      Q6_prefix=prefix(q6), prefix_squared_HS=gram))

failures = [x['name'] for x in identities if x['exact_error']]
failures += [x['name'] for x in inequalities if not x['passed']]
if not any(x['full'] and x['prefix'] and x['direct'] for x in cases):
    failures.append('missing nonzero full/direct/prefix control')
certificate = dict(
    scope='Exact finite algebra only; no mesh asymptotics or actual-probe value.',
    matrices=dict(D=d, S=s, L=l, A=a, Q3=q3, Q6=q6, A_gen=agen,
                  Sigma=sigma, Phi=phi, R=r, K=k, F=f),
    cases=cases, identities=identities, inequalities=inequalities,
    required_exact_error=0, failures=failures, passed=not failures)
path = Path(__file__).with_name('smooth-action-prefix-reduction-certificate.json')
path.write_text(json.dumps(certificate, default=str, indent=2)+'\n')
print(f'Exact identities: {len(identities)}; maximum error {max(abs(x["exact_error"]) for x in identities)}; required 0.')
for index, row in enumerate(cases, 1):
    print(f'Case {index}: full {row["full"]}; direct {row["direct"]}; prefix {row["prefix"]}.')
for row in inequalities:
    print(f'{row["name"]}: actual {row["actual"]}; required <= {row["required_upper_bound"]}; passed {row["passed"]}.')
print(f'Failures: {failures}; certificate: {path.relative_to(Path.cwd())}.')
assert not failures

