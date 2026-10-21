"""Exact rational correction contraction; surrogate, not box asymptotics."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations
from pathlib import Path
import json

n = 5
m = 3*n
zero = (0,)*m
S = [[F(0) for _ in range(n)] for _ in range(n)]
for i, v in enumerate([2, 3, 5, F(1, 2), F(3, 4)]):
    S[i][i] = F(v)
S[3][4] = S[4][3] = F(1, 4)
# (noise coordinate, first vertex, second vertex); -1 is pinned zero.
edges = [(3, 0, 1), (4, 1, 2), (3, 2, -1)]


def matrix(entries):
    M = [[F(0) for _ in range(n)] for _ in range(n)]
    for i, j, v in entries:
        M[i][j] += F(v, 2) if i != j else F(v)
        if i != j:
            M[j][i] += F(v, 2)
    return M


A = matrix([(0, 0, 1), (1, 4, 3), (3, 3, -2), (3, 4, 1), (2, 2, -1)])
Bs = [matrix(entries) for entries in [
    [(0, 0, 1), (1, 1, -1), (2, 2, 2)],
    [(0, 3, 2), (1, 4, -1), (3, 3, 1), (4, 4, 2), (0, 1, 1)]]]


def add(*polys):
    result = {}
    for p in polys:
        for e, c in p.items():
            result[e] = result.get(e, F(0))+c
    return {e: c for e, c in result.items() if c}


def scale(c, p):
    return {e: c*v for e, v in p.items() if c*v}


def mul(p, q):
    result = {}
    for e, c in p.items():
        for h, d in q.items():
            t = tuple(a+b for a, b in zip(e, h))
            result[t] = result.get(t, F(0))+c*d
    return {e: c for e, c in result.items() if c}


def var(i, color):
    if i < 0:
        return {}
    return {tuple(int(j == color*n+i) for j in range(m)): F(1)}


@lru_cache(None)
def moment(e):
    if not any(e):
        return F(1)
    if any(sum(e[c*n:(c+1)*n]) % 2 for c in range(3)):
        return F(0)
    i = next(j for j, v in enumerate(e) if v)
    tail = list(e)
    tail[i] -= 1
    total = F(0)
    for j in range(i//n*n, (i//n+1)*n):
        if tail[j] and S[i % n][j % n]:
            h = tail.copy()
            h[j] -= 1
            total += tail[j]*S[i % n][j % n]*moment(tuple(h))
    return total


def expect(p):
    return sum((c*moment(e) for e, c in p.items()), F(0))


def quad(M):
    return add(*(scale(M[i][j], mul(var(i, c), var(j, c)))
                 for c in range(3) for i in range(n) for j in range(n)))


def cumulant(f, r, p):
    ef, er, ep = expect(f), expect(r), expect(p)
    return (expect(mul(mul(f, r), p))-ef*expect(mul(r, p))
            -er*expect(mul(f, p))-ep*expect(mul(f, r))+2*ef*er*ep)


def mm(*matrices):
    M = matrices[0]
    for H in matrices[1:]:
        M = [[sum((M[i][k]*H[k][j] for k in range(n)), F(0))
              for j in range(n)] for i in range(n)]
    return M


def at(M, i, j):
    return F(0) if min(i, j) < 0 else M[i][j]


Q = [[add(mul(var(v, (c+1) % 3), var(vp, (c+2) % 3)),
          scale(-1, mul(var(v, (c+2) % 3), var(vp, (c+1) % 3))))
      for c in range(3)] for _, v, vp in edges]
cubic = scale(F(1, 2), add(*(mul(var(j, c), Q[e][c])
                          for e, (j, _, _) in enumerate(edges) for c in range(3))))
square = scale(F(1, 2), mul(cubic, cubic))
effective = scale(F(1, 8), add(*(scale(S[j][k], mul(Q[e][c], Q[h][c]))
    for e, (j, _, _) in enumerate(edges) for h, (k, _, _) in enumerate(edges)
    for c in range(3))))
checks = []


def check(kind, actual, required, **extra):
    checks.append(dict(kind=kind, actual=str(actual), required=str(required),
                       passed=actual == required, **extra))


check('pinned_product', sum(len(p) for p in Q[-1]), 0)
check('untilted_conditioning', expect(square), expect(effective))
r = quad(A)
for case, B in enumerate(Bs):
    U, V, W = mm(S, B, S), mm(S, A, S), mm(S, B, S, A, S)
    T = [[W[i][j]+W[j][i] for j in range(n)] for i in range(n)]
    parts = [F(0)]*4
    for j, v, vp in edges:
        for k, w, wp in edges:
            def det(M):
                return at(M, v, w)*at(M, vp, wp)-at(M, v, wp)*at(M, vp, w)
            def delta(M):
                return (at(S, v, w)*at(M, vp, wp)+at(M, v, w)*at(S, vp, wp)
                        -at(S, v, wp)*at(M, vp, w)-at(M, v, wp)*at(S, vp, w))
            def pair(x, y):
                return at(U, j, x)*at(V, k, y)+at(V, j, x)*at(U, k, y)
            parts[0] += 3*T[j][k]*det(S)
            parts[1] += 3*U[j][k]*delta(V)
            parts[2] += 3*V[j][k]*delta(U)
            parts[3] += 3*(-pair(w, v)*at(S, vp, wp)+pair(w, vp)*at(S, v, wp)
                          +pair(wp, v)*at(S, vp, w)-pair(wp, vp)*at(S, v, w))
    f = quad(B)
    actual = cumulant(f, r, square)-cumulant(f, r, effective)
    check('complete_correction', actual, sum(parts), case=case,
          parts=[str(x) for x in parts],
          cubic_pair=str(cumulant(f, r, square)),
          effective=str(cumulant(f, r, effective)))
    shifted = add(f, {zero: F(7)})
    check('constant_shift', cumulant(shifted, r, square)-cumulant(shifted, r, effective),
          sum(parts), case=case)

failures = [x for x in checks if not x['passed']]
encode = lambda M: [[str(v) for v in row] for row in M]
out = Path(__file__).with_name('observable-correction-certificate.json')
out.write_text(json.dumps(dict(
    scope='Rational three-color Gaussian surrogate; correlated noise, adjacent edges and a pinned end; not the original box',
    inputs=dict(covariance=encode(S), residual=encode(A), probes=[encode(B) for B in Bs], edges=edges),
    checks=checks, failures=failures,
    bounds=dict(actual='Exact finite correction decomposition; analytic second-noise-derivative piece O(1) in L052',
                required='Full E and defect at a^2 scale, complete logarithm, interacting reflected error <=c_box/2')
), indent=2)+'\n')
print(f"{'PASS' if not failures else 'FAIL'}: {len(checks)} exact checks; failures={len(failures)}")
for x in checks:
    if x['kind'] == 'complete_correction':
        print(f"case {x['case']}: actual={x['actual']}; required={x['required']}; parts={x['parts']}")
print('Actual: finite algebra and one analytic O(1) piece; required: full scaled correction and logarithm.')
print(f'Certificate: {out.relative_to(Path.cwd())}')
assert not failures
