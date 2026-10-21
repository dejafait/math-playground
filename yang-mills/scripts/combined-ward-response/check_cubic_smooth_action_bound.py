"""Exact finite checks for L159; no actual-probe values or cutoff inference."""
from fractions import Fraction as F
from pathlib import Path
import json


def tp(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def add(a, b, sign=1):
    return [[x+sign*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def inv(a):
    n = len(a)
    v = [list(map(F, row))+ident for row, ident in zip(a, eye(n))]
    for i in range(n):
        p = next(j for j in range(i, n) if v[j][i])
        v[i], v[p] = v[p], v[i]
        q = v[i][i]
        v[i] = [x/q for x in v[i]]
        for j in range(n):
            if j != i:
                q = v[j][i]
                v[j] = [x-q*y for x, y in zip(v[j], v[i])]
    return [row[n:] for row in v]


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def diag(v):
    return [[F(v[i]) if i == j else F(0) for j in range(len(v))] for i in range(len(v))]


def mv(a, v):
    return [sum(x*y for x, y in zip(row, v)) for row in a]


def kron(a, b):
    return [[a[i][j]*b[r][s] for j in range(len(a[0])) for s in range(len(b[0]))]
            for i in range(len(a)) for r in range(len(b))]


def chain(*xs):
    a = xs[0]
    for b in xs[1:]:
        a = mm(a, b)
    return a


def maxerr(a, b):
    return max(abs(x-y) for ar, br in zip(a, b) for x, y in zip(ar, br))


identities = []


def check(name, actual, required):
    err = maxerr(actual, required)
    identities.append(dict(name=name, actual=actual, required=required, maximum_exact_error=err))


# Same pinned graph as L158, reproduced locally without running its producer.
d = [[1, 0, 0], [-1, 1, 0], [0, -1, 1], [0, 0, -1], [0, 1, 0]]
s = [[1, 0, 0], [1, 1, 0], [0, 1, 1], [0, 0, 1], [0, 1, 0]]
cycles = tp([[1, 1, 1, 1, 0], [1, 1, 0, 0, -1]])
l = mm(cycles, tp(cycles))
a = chain(cycles, [[2, -1], [-1, 3]], tp(cycles))
sigma = inv(add(l, mm(d, tp(d))))
phi = [[1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 0, 0]]
r = add(eye(5), mm(d, phi), -1)
k = chain(phi, sigma, tp(phi))
h = mv(r, [1, 2, -1, 3, 2])
ell = mv(r, [2, -1, 4, 1, -2])
q = mv(l, ell)
o = chain(tp(s), diag(q), d)
check('complete action column is co-closed', [[x] for x in mv(tp(d), q)], [[0], [0], [0]])
check('transport diagonal vanishes', [[o[i][i]] for i in range(3)], [[0], [0], [0]])
check('transport is skew', add(o, tp(o)), [[0]*3 for _ in range(3)])
prefix_actual = tr(chain(k, o, phi, sigma, tp(phi), tp(o)))
prefix_required = tr(chain(k, o, k, tp(o)))
check('prefix squared-HS Gram identity', [[prefix_actual]], [[prefix_required]])


def bracket(a, b):
    return [a[2]*b[1]-a[1]*b[2], a[0]*b[2]-a[2]*b[0], a[1]*b[0]-a[0]*b[1]]


hat = lambda x: kron(x, eye(3))
colored = F(0)
for color in range(3):
    tc = [int(j == color) for j in range(3)]
    bc = tp([bracket(tc, basis) for basis in eye(3)])
    bh = kron(mm(diag(h), s), bc)
    bq = kron(mm(diag(q), s), bc)
    colored += tr(chain(hat(sigma), hat(a), bh, hat(k), tp(bq), hat(r)))
scalar = 6*tr(chain(sigma, a, diag(h), s, k, tp(s), diag(q), r))
check('full V branch color reduction', [[colored]], [[scalar]])

inequalities = []
for n in (2, 4, 7):
    m = [[F(min(i+1, j+1)) for j in range(n)] for i in range(n)]
    b = [[F(i == j)-F(i == j+1) for j in range(n)] for i in range(n)]
    j = add(tp(b), b, -1)
    check(f'anchored inverse, n={n}', mm(tp(b), b), inv(m))
    check(f'anchored derivative covariance, n={n}', chain(b, m, tp(b)), eye(n))
    lap = [[2*F(i == j)-F(abs(i-j) == 1) for j in range(n)] for i in range(n)]
    g = inv(lap)
    check(f'Dirichlet inverse, n={n}', mm(lap, g), eye(n))
    for name, covariance in [('axial', m), ('transverse', g)]:
        actual = tr(chain(covariance, j, covariance, tp(j)))
        required = 4*tr(covariance)
        inequalities.append(dict(name=f'{name} squared-HS transport, n={n}',
                                 actual=actual, required_upper_bound=required,
                                 slack=required-actual, passed=0 <= actual <= required))

failures = [row['name'] for row in identities if row['maximum_exact_error']]
failures += [row['name'] for row in inequalities if not row['passed']]
certificate = dict(scope='Exact algebra and finite energy instances only; uniform bounds are analytic in L159',
                   matrices=dict(D=d, S=s, L=l, A=a, Sigma=sigma, Phi=phi, R=r, K=k),
                   exterior=dict(h=h, ell=ell, q=q, O_q=o),
                   identities=identities, inequalities=inequalities,
                   required_maximum_exact_error=0, failures=failures, passed=not failures)
path = Path(__file__).with_name('cubic-smooth-action-bound-certificate.json')
path.write_text(json.dumps(certificate, default=str, indent=2)+'\n')
print(f'Exact identities: {len(identities)}; maximum error {max(row["maximum_exact_error"] for row in identities)}; required 0.')
for row in inequalities:
    print(f'{row["name"]}: actual {row["actual"]}; required <= {row["required_upper_bound"]}; slack {row["slack"]}.')
print(f'Prefix squared-HS: actual {prefix_actual}; required {prefix_required}.')
print(f'Color trace: actual {colored}; required {scalar}.')
print(f'Failures: {failures}; certificate: {path.relative_to(Path.cwd())}.')
assert not failures
