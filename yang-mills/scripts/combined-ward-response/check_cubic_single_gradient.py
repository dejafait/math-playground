"""Exact one-cycle checks for L157; no actual-probe or cutoff computation."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import json


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def bracket(a, b):
    return (a[2]*b[1]-a[1]*b[2], a[0]*b[2]-a[2]*b[0],
            a[1]*b[0]-a[0]*b[1])


def basis(j):
    return [tuple(int(3*v+c == j) for c in range(3)) for v in range(4)]


def gradient(phi):
    return [tuple(phi[(e+1) % 4][c]-phi[e][c] for c in range(3))
            for e in range(4)]


def endpoint(phi):
    return [tuple(phi[(e+1) % 4][c]+phi[e][c] for c in range(3))
            for e in range(4)]


def laplace(h):
    return [tuple(sum(row[c] for row in h) for c in range(3))]*4


def third_action(h, z, g):
    vectors = (h, z, g)
    # Third derivative, hence six times the symmetric Taylor tensor.
    return F(1, 2)*sum(
        dot(vectors[p[0]][i], bracket(vectors[p[1]][j], vectors[p[2]][k]))
        for i, j, k in combinations(range(4), 3)
        for p in permutations(range(3)))


def flatten(h):
    return [x for row in h for x in row]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[dot(row, col) for col in zip(*b)] for row in a]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def bilinear_matrix(h):
    return transpose([flatten([bracket(v, p) for v, p in zip(h, endpoint(basis(j)))])
                      for j in range(12)])


checks = []
for hi, zi, pi in product(range(12), repeat=3):
    h, z, phi = basis(hi), basis(zi), basis(pi)
    actual = third_action(h, z, gradient(phi))
    required = -F(1, 2)*sum(
        dot(lh, bracket(ze, pe))+dot(lz, bracket(he, pe))
        for lh, lz, he, ze, pe in zip(laplace(h), laplace(z), h, z, endpoint(phi)))
    checks.append(dict(h=hi, z=zi, phi=pi, actual=str(actual),
                       required=str(required), error=str(actual-required)))

# Independent tensor contraction versus the trace formula, with a signed
# color-diagonal rough matrix. F_R=F_S=the cycle action in this algebra test.
d = transpose([flatten(gradient(basis(j))) for j in range(12)])
lmat = transpose([flatten(laplace(basis(j))) for j in range(12)])
kv = [[3, 1, 0, 0], [1, 4, 1, 0], [0, 1, 5, 1], [0, 0, 1, 6]]
ev = [[1, 1, 0, 0], [1, -2, 1, 0], [0, 1, 3, 1], [0, 0, 1, -4]]
k = [[kv[i//3][j//3]*int(i % 3 == j % 3) for j in range(12)] for i in range(12)]
e = [[ev[i//3][j//3]*int(i % 3 == j % 3) for j in range(12)] for i in range(12)]
cg = mm(mm(d, k), transpose(d))
contractions = []
for hc, lc in [([1, 2, -1, 3], [2, -1, 4, 1]),
               ([0, 1, 0, -1], [1, 3, 2, -2])]:
    h, ell = [[x, 0, 0] for x in hc], [[x, 0, 0] for x in lc]
    th = [[third_action(h, basis(i), basis(j))/6 for j in range(12)] for i in range(12)]
    tl = [[third_action(ell, basis(i), basis(j))/6 for j in range(12)] for i in range(12)]
    direct = -72*trace(mm(mm(mm(th, cg), tl), e))
    qh0 = mm(lmat, bilinear_matrix(h))
    ql0 = mm(lmat, bilinear_matrix(ell))
    blh, bll = bilinear_matrix(laplace(h)), bilinear_matrix(laplace(ell))
    # A_R=L/2, whereas the action Q_L uses L without the half.
    qh = [[F(qh0[i][j]-blh[i][j], 2) for j in range(12)] for i in range(12)]
    ql = [[ql0[i][j]-bll[i][j] for j in range(12)] for i in range(12)]
    reduced = -trace(mm(mm(mm(qh, k), transpose(ql)), e))
    contractions.append(dict(h=hc, ell=lc, direct=str(direct), reduced=str(reduced),
                             error=str(direct-reduced)))

failures = [f'basis:{i}' for i, row in enumerate(checks) if row['error'] != '0']
failures += [f'contraction:{i}' for i, row in enumerate(contractions) if row['error'] != '0']
path = Path(__file__).with_name('cubic-single-gradient-certificate.json')
path.write_text(json.dumps(dict(
    scope='One-cycle action identity and signed mixed-sector algebra; not actual probes or cutoff evidence',
    checks=checks, check_count=len(checks), contractions=contractions,
    maximum_absolute_error=str(max(abs(F(row['error'])) for row in checks+contractions)),
    failures=failures, passed=not failures), indent=2)+'\n')
print(f'One-gradient basis checks: {len(checks)}; exact error required: 0; failures: {len(failures)}.')
for row in contractions:
    print(f'Signed contraction: direct={row["direct"]}, required trace={row["reduced"]}, error={row["error"]}.')
print(f'Certificate: {path.relative_to(Path.cwd())}; failures: {failures}.')
assert not failures
