"""Exact nonlocal quartic response checks; no lattice asymptotic claim."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json

n, colors = 4, 3
m = n * colors
S = [[F(x) for x in row] for row in
     [[2, 1, 0, 1], [1, 3, 1, 0], [0, 1, 4, 1], [1, 0, 1, 5]]]
edges = [(0, 1), (1, 2), (2, 0), (2, -1)]
D = [[F(1, 2) if i == j else F(1, 10) for j in range(4)] for i in range(4)]
A = [[F(x) for x in row] for row in
     [[1, 1, 0, 0], [1, -2, 0, 1], [0, 0, 2, 0], [0, 1, 0, -1]]]
Bs = [[[F(x) for x in row] for row in rows] for rows in [
    [[1, 0, 1, 0], [0, -1, 0, 0], [1, 0, 2, 0], [0, 0, 0, 0]],
    [[0, 1, 0, 1], [1, 2, 0, 0], [0, 0, -1, 1], [1, 0, 1, 1]]]]


def add(*ps):
    out = {}
    for p in ps:
        for e, c in p.items():
            out[e] = out.get(e, F(0)) + c
    return {e: c for e, c in out.items() if c}


def scale(c, p):
    return {e: c * v for e, v in p.items() if c * v}


def mul(p, q):
    out = {}
    for e, c in p.items():
        for h, d in q.items():
            t = tuple(a + b for a, b in zip(e, h))
            out[t] = out.get(t, F(0)) + c * d
    return {e: c for e, c in out.items() if c}


def variable(vertex, color):
    if vertex < 0:
        return {}
    return {tuple(int(j == color * n + vertex) for j in range(m)): F(1)}


@lru_cache(None)
def moment(e):
    if not any(e):
        return F(1)
    if any(sum(e[c*n:(c+1)*n]) % 2 for c in range(colors)):
        return F(0)
    i = next(j for j, v in enumerate(e) if v)
    tail = list(e)
    tail[i] -= 1
    total = F(0)
    for j in range(i//n*n, (i//n+1)*n):
        if tail[j] and S[i % n][j % n]:
            h = tail.copy()
            h[j] -= 1
            total += tail[j] * S[i % n][j % n] * moment(tuple(h))
    return total


def expect(p):
    return sum((c * moment(e) for e, c in p.items()), F(0))


def quad(M):
    return add(*(scale(M[i][j], mul(variable(i, c), variable(j, c)))
                 for c in range(colors) for i in range(n) for j in range(n)))


def mm(*matrices):
    R = matrices[0]
    for M in matrices[1:]:
        R = [[sum((R[i][k] * M[k][j] for k in range(n)), F(0))
              for j in range(n)] for i in range(n)]
    return R


def entry(M, i, j):
    return F(0) if i < 0 or j < 0 else M[i][j]


def phi(M, H, kernel=D):
    total = F(0)
    for e, (v, vp) in enumerate(edges):
        for h, (w, wp) in enumerate(edges):
            total += kernel[e][h] * (
                entry(M, v, w)*entry(H, vp, wp) + entry(H, v, w)*entry(M, vp, wp)
                - entry(M, v, wp)*entry(H, vp, w) - entry(H, v, wp)*entry(M, vp, w))/2
    return total


Q = [[add(mul(variable(v, (c+1) % 3), variable(vp, (c+2) % 3)),
          scale(-1, mul(variable(v, (c+2) % 3), variable(vp, (c+1) % 3))))
      for c in range(colors)] for v, vp in edges]
Z = scale(F(1, 8), add(*(scale(D[e][h], mul(Q[e][c], Q[h][c]))
                       for e in range(4) for h in range(4) for c in range(colors))))
checks = []


def check(kind, actual, required, **extra):
    checks.append(dict(kind=kind, actual=str(actual), required=str(required),
                       passed=actual == required, **extra))


check('pinned_edge_polynomial', sum(len(p) for p in Q[-1]), 0)
check('quartic_expectation', expect(Z), F(3, 4) * phi(S, S))
r = quad(A)
for case, B in enumerate(Bs):
    f = quad(B)
    ef, er, ez = expect(f), expect(r), expect(Z)
    actual = (expect(mul(mul(f, r), Z)) - ef*expect(mul(r, Z))
              - er*expect(mul(f, Z)) - ez*expect(mul(f, r)) + 2*ef*er*ez)
    U, V, W = mm(S, B, S), mm(S, A, S), mm(S, B, S, A, S)
    Wsum = [[W[i][j] + W[j][i] for j in range(n)] for i in range(n)]
    one_pair, no_pair = 6*phi(S, Wsum), 6*phi(U, V)
    diagonal = [[D[i][j] if i == j else F(0) for j in range(4)] for i in range(4)]
    diagonal_only = 6*phi(S, Wsum, diagonal) + 6*phi(U, V, diagonal)
    check('complete_cumulant', actual, one_pair + no_pair, case=case,
          one_internal_pair=str(one_pair), no_internal_pair=str(no_pair),
          diagonal_only=str(diagonal_only), off_diagonal_difference=str(actual-diagonal_only))

failures = [x for x in checks if not x['passed']]
out = Path(__file__).with_name('signed-upper-defect-certificate.json')
def encoded(M):
    return [[str(x) for x in row] for row in M]
out.write_text(json.dumps(dict(
    scope='Exact rational Gaussian surrogate with three colors, nonlocal kernel and pinned end; not original-box evaluation',
    inputs=dict(covariance=encoded(S), residual=encoded(A), probes=[encoded(B) for B in Bs],
                defect=encoded(D), edges=edges), checks=checks, failures=failures,
    bounds=dict(actual='Exact finite cumulant identity; analytic R=O(a^-1) in L051',
                required='Bound/limit of a^2*(-kappa(f,r,Z)+E); full response logarithm and reflected error <=c_box/2')
), indent=2) + '\n')
print(f"{'PASS' if not failures else 'FAIL'}: {len(checks)} rational checks; failures={len(failures)}")
for x in checks:
    if x['kind'] == 'complete_cumulant':
        print(f"case {x['case']}: actual={x['actual']}; required={x['required']}; off-diagonal={x['off_diagonal_difference']}")
print('Actual: finite identity and analytic R=O(a^-1); required: complete scaled group and logarithm.')
print(f'Certificate: {out.relative_to(Path.cwd())}')
assert not failures
