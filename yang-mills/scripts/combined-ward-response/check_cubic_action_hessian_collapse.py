"""Exact L158 matrix/color/parity checks; no actual-probe cutoff values."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import json


def transpose(a):
    return [list(x) for x in zip(*a)]


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def add(a, b, sign=1):
    return [[x+sign*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a, s):
    return [[s*x for x in row] for row in a]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def inv(a):
    n = len(a)
    v = [list(map(F, row))+ident for row, ident in zip(a, eye(n))]
    for i in range(n):
        pivot = next(j for j in range(i, n) if v[j][i])
        v[i], v[pivot] = v[pivot], v[i]
        q = v[i][i]
        v[i] = [x/q for x in v[i]]
        for j in range(n):
            if j != i:
                q = v[j][i]
                v[j] = [x-q*y for x, y in zip(v[j], v[i])]
    return [row[n:] for row in v]


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def maxerr(a):
    return max(abs(x) for row in a for x in row)


def kron(a, b):
    return [[a[i][j]*b[r][s] for j in range(len(a[0])) for s in range(len(b[0]))]
            for i in range(len(a)) for r in range(len(b))]


def diag(v):
    return [[F(v[i]) if i == j else F(0) for j in range(len(v))] for i in range(len(v))]


def matvec(a, v):
    return [sum(x*y for x, y in zip(row, v)) for row in a]


def bracket(a, b):
    return [a[2]*b[1]-a[1]*b[2], a[0]*b[2]-a[2]*b[0], a[1]*b[0]-a[0]*b[1]]


# Four vertices, vertex zero pinned; the square and diagonal provide two cycles.
d = [[1, 0, 0], [-1, 1, 0], [0, -1, 1], [0, 0, -1], [0, 1, 0]]
s = [[1, 0, 0], [1, 1, 0], [0, 1, 1], [0, 0, 1], [0, 1, 0]]
z = transpose([[1, 1, 1, 1, 0], [1, 1, 0, 0, -1]])
l = mm(z, transpose(z))
a = mm(mm(z, [[2, -1], [-1, 3]]), transpose(z))
sigma = inv(add(l, mm(d, transpose(d))))
phi = [[1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 0, 0]]
r = add(eye(5), mm(d, phi), -1)
k = mm(mm(phi, sigma), transpose(phi))
c = mm(mm(r, sigma), transpose(r))
e = add(c, mm(mm(d, k), transpose(d)), -1)
checks = []


def record(name, actual, required):
    err = maxerr(add(actual, required, -1))
    checks.append(dict(name=name, actual=actual, required=required, maximum_exact_error=err))


record('Phi D = I', mm(phi, d), eye(3))
record('A D = 0', mm(a, d), [[0]*3 for _ in range(5)])
record('L E A = A', mm(mm(l, e), a), a)
record('E A = R Sigma A', mm(e, a), mm(mm(r, sigma), a))
noncommutator = maxerr(add(mm(a, l), mm(l, a), -1))
assert noncommutator > 0
hat = lambda x: kron(x, eye(3))
ah, lh, eh, kh, sh, rh = map(hat, (a, l, e, k, sigma, r))
ktr = mm(mm(s, k), transpose(s))
branches = []
for v, w in [([1, 2, -1, 3, 2], [2, -1, 4, 1, -2]),
             ([3, -2, 1, -1, 4], [1, 3, 2, -2, 5])]:
    h, ell = matvec(r, v), matvec(r, w)
    lell = matvec(l, ell)
    original_t = collapsed_t = original_v = collapsed_v = F(0)
    for color in range(3):
        tc = [int(j == color) for j in range(3)]
        bc = transpose([bracket(tc, basis) for basis in eye(3)])
        bh = kron(mm(diag(h), s), bc)
        bl = kron(mm(diag(ell), s), bc)
        bll = kron(mm(diag(lell), s), bc)
        original_t -= tr(mm(mm(mm(mm(mm(ah, bh), kh), transpose(bl)), lh), eh))
        collapsed_t -= tr(mm(mm(mm(ah, bh), kh), transpose(bl)))
        original_v += tr(mm(mm(mm(mm(ah, bh), kh), transpose(bll)), eh))
        collapsed_v += tr(mm(mm(mm(mm(mm(sh, ah), bh), kh), transpose(bll)), rh))
    scalar_t = -6*tr(mm(mm(mm(a, diag(h)), ktr), diag(ell)))
    row = dict(h=h, ell=ell, original_t=original_t, collapsed_t=collapsed_t,
               scalar_t=scalar_t, original_v=original_v, collapsed_v=collapsed_v,
               t_error=original_t-collapsed_t, v_error=original_v-collapsed_v,
               color_error=collapsed_t-scalar_t)
    branches.append(row)

# Check the complete frozen filters, entrywise, at rational sine/cosine points.
parity = []
for u, ts in product(([1, 2, -3, 4], [0, 1, 0, -2], [-2, 0, 3, 1]),
                     ([F(0), F(1, 3), F(1, 2), F(1, 4)],
                      [F(0), F(2, 3), F(1, 5), F(2, 5)],
                      [F(0), F(1, 7), F(3, 4), F(1, 6)])):
    ds = [4*t/(1+t*t) for t in ts]
    cs = [(1-t*t)/(1+t*t) for t in ts]
    hnorm = sum(x*x for x in ds)
    def symbol(dvalues):
        ls = [[hnorm*int(i == j)-dvalues[i]*dvalues[j] for j in range(4)] for i in range(4)]
        mdot = sum(uu*cc*dd for uu, cc, dd in zip(u, cs, dvalues))
        ms = [[cs[i]**2*(int(i == j)*mdot-u[j]*cs[j]*dvalues[i])
               for j in range(4)] for i in range(4)]
        return scale(add(mm(ls, ms), mm(transpose(ms), ls), -1), F(1, 2))
    pos, neg = symbol(ds), symbol([-x for x in ds])
    weighted = [[4*cs[i]*cs[j]/hnorm*(pos[i][j]+neg[i][j]) for j in range(4)] for i in range(4)]
    parity.append(dict(u=u, d=ds, cos_half=cs, positive_imaginary_symbol=pos,
                       reversed_imaginary_symbol=neg, paired_integrand=weighted,
                       maximum_exact_error=maxerr(weighted)))

failures = [row['name'] for row in checks if row['maximum_exact_error']]
failures += [f'branch:{j}' for j, row in enumerate(branches)
             if row['t_error'] or row['v_error'] or row['color_error']]
failures += [f'parity:{j}' for j, row in enumerate(parity) if row['maximum_exact_error']]
certificate = dict(scope='Exact finite matrix/color/parity checks, not actual probes or cutoff evidence',
                   matrices=dict(D=d, S=s, L=l, A=a, Sigma=sigma, Phi=phi, R=r, K=k, E=e),
                   noncommuting_A_L_maximum=noncommutator,
                   signed_E_diagonal=[e[i][i] for i in range(5)],
                   matrix_checks=checks, branches=branches, parity_checks=parity,
                   required_maximum_error=0, failures=failures, passed=not failures)
path = Path(__file__).with_name('cubic-action-hessian-collapse-certificate.json')
path.write_text(json.dumps(certificate, default=str, indent=2)+'\n')
print(f'Matrix identities: {len(checks)}; trace/color comparisons: {3*len(branches)}; parity cases: {len(parity)}.')
print(f'Exact maximum error: {max([row["maximum_exact_error"] for row in checks+parity]+[abs(row[key]) for row in branches for key in ("t_error", "v_error", "color_error")])}; required: 0.')
for row in branches:
    print(f'T original/required: {row["original_t"]}/{row["collapsed_t"]}; V original/required: {row["original_v"]}/{row["collapsed_v"]}.')
print(f'Noncommuting A,L: {noncommutator}; E diagonal: {[str(e[i][i]) for i in range(5)]}.')
print(f'Failures: {failures}; certificate: {path.relative_to(Path.cwd())}.')
assert not failures
