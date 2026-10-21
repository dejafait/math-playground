"""Exact synthetic checks of L181. No box value or flow-time estimate."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path
import json

N = 4
PERMS = [(p, (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3)))
         for p in permutations(range(3))]


def add(*polys):
    out = {}
    for p in polys:
        for key, val in p.items():
            out[key] = out.get(key, F(0)) + val
    return {k: v for k, v in out.items() if v}


def scale(p, c):
    return {k: c*v for k, v in p.items() if c*v}


def mul(p, q):
    out = {}
    for k, v in p.items():
        for l, w in q.items():
            key = tuple(sorted(k+l))
            out[key] = out.get(key, F(0)) + v*w
    return {k: v for k, v in out.items() if v}


def lin(row, color):
    return {(3*j+color,): F(v) for j, v in enumerate(row) if v}


def det(rows):
    return add(*(scale(mul(mul(lin(rows[0], p[0]), lin(rows[1], p[1])),
                          lin(rows[2], p[2])), sign) for p, sign in PERMS))


def cubic(h, rows):
    return add(*(scale(det([rows[i] for i in key]), v) for key, v in h.items()))


def directional(h, rows, directions):
    terms = []
    for key, v in h.items():
        for slot in range(3):
            terms.append(scale(det([directions[i] if j == slot else rows[i]
                                    for j, i in enumerate(key)]), v))
    return add(*terms)


def quadratic(a):
    out = {}
    for i, j, c in product(range(N), range(N), range(3)):
        key = tuple(sorted((3*i+c, 3*j+c)))
        out[key] = out.get(key, F(0)) + a[i][j]
    return {k: v for k, v in out.items() if v}


def expected(cov):
    @lru_cache(None)
    def moment(key):
        if not key:
            return F(1)
        if any(sum(k % 3 == c for k in key) % 2 for c in range(3)):
            return F(0)
        i, tail = key[0], key[1:]
        return sum((cov[i//3][j//3]*moment(tail[:k]+tail[k+1:])
                    for k, j in enumerate(tail) if i % 3 == j % 3), F(0))
    return lambda p: sum((v*moment(k) for k, v in p.items()), F(0))


def transpose(a):
    return list(map(list, zip(*a)))


def mm(a, b):
    return [[sum((F(x)*F(y) for x, y in zip(row, col)), F(0))
             for col in zip(*b)] for row in a]


def alt(h):
    return [(tuple(key[j] for j in p), sign*v)
            for key, v in h.items() for p, sign in PERMS]


def tensor_pair(h, k, b1, b2, b3):
    return sum((v*w*b1[r][u]*b2[s][v0]*b3[t][w0]
                for (r, s, t), v in alt(h)
                for (u, v0, w0), w in alt(k)), F(0))


def coefficients(p):
    # Coefficient of x_r^1 x_s^2 x_t^3 determines an invariant cubic.
    return {key: p.get(tuple(sorted(3*i+c for c, i in enumerate(key))), F(0))
            for key in combinations(range(N), 3)}


identity = [[F(i == j) for j in range(N)] for i in range(N)]
lower = [[1, 0, 0, 0], [F(1, 2), 1, 0, 0],
         [0, F(-1, 3), 2, 0], [F(1, 4), 0, F(1, 2), 1]]
covs = [identity, mm(lower, transpose(lower))]
matrices = [identity, [[1, F(1, 3), 0, -1], [F(1, 3), -2, F(1, 2), 0],
                       [0, F(1, 2), 0, 1], [-1, 0, 1, -1]]]
hs = [{key: F((-1)**j*(j+2), j+1) for j, key in enumerate(combinations(range(N), 3))},
      {(0, 1, 2): F(1), (0, 1, 3): F(-2), (0, 2, 3): F(3, 2), (1, 2, 3): F(-1, 4)}]
residual = {(0, 1, 2): F(-3), (0, 1, 3): F(2, 3), (0, 2, 3): F(1, 5), (1, 2, 3): F(4)}
action = {key: F(-1, 2) for key in combinations(range(N), 3)}
checks = []


def record(name, actual, required, **data):
    checks.append(dict(name=name, passed=actual == required, actual=str(actual),
                       required=str(required), exact_error=str(actual-required), **data))


for ci, cov in enumerate(covs):
    ev = expected(cov)
    for ai, a in enumerate(matrices):
        t = [[2*v for v in row] for row in mm(cov, a)]
        r, s, q = cubic(residual, identity), cubic(action, identity), quadratic(a)
        effective = add(r, scale(directional(action, identity, t), -1))
        k = coefficients(effective)
        assert effective == cubic(k, identity)
        for hi, h in enumerate(hs):
            f = cubic(h, identity)
            # Odd means and odd cubic/quadratic products vanish exactly.
            direct = ev(mul(f, r))-ev(mul(mul(f, q), s))+ev(q)*ev(mul(f, s))
            effective_value = ev(mul(f, effective))
            tensor_value = tensor_pair(h, k, cov, cov, cov)
            record('effective_cubic', effective_value, direct, covariance=ci, quadratic=ai, probe=hi)
            record('three_line_tensor', tensor_value, direct, covariance=ci, quadratic=ai, probe=hi)

# A full-space/forest rectangular test for the two probe contributions.
# Rational sample maps and weights stand for integrand evaluations ONLY;
# they neither discretize nor bound an actual Wilson-flow integral.
m = 5
full_action = {key: F((-1)**j, j+1) for j, key in enumerate(combinations(range(m), 3))}
full_probe = {key: F(j+1, j+2) for j, key in enumerate(combinations(range(m), 3))}
rtau = identity + [[F(1, 3), F(-1, 2), 0, 1]]
rs = [identity[0], [0, F(1, 2), 0, 0], [0, 0, F(1, 3), 0],
      [0, 0, 0, F(1, 4)], [1, 0, -1, F(1, 2)]]
direction = [[F((2*i+j) % 5-2, i+j+2) for j in range(N)] for i in range(m)]
weight, a_inverse_square = F(2, 7), F(9, 4)
f = add(cubic(full_probe, rtau),
        scale(directional(full_action, rs, direction), -2*a_inverse_square*weight))
for ci, cov in enumerate(covs):
    ev = expected(cov)
    k = residual
    direct = ev(mul(f, cubic(k, identity)))
    ztau, zs, zh = mm(rtau, cov), mm(rs, cov), mm(direction, cov)
    formula = tensor_pair(full_probe, k, ztau, ztau, ztau)
    formula -= 6*a_inverse_square*weight*tensor_pair(full_action, k, zh, zs, zs)
    record('full_space_flow_integrand_factor', formula, direct, covariance=ci)

ev = expected(identity)
toy = cubic({(0, 1, 2): F(1)}, identity)
radial = quadratic(identity)
joint = ev(mul(toy, toy))-ev(mul(mul(toy, radial), toy))+ev(radial)*ev(mul(toy, toy))
record('nonzero_sign_control', joint, F(-30))

failures = [c for c in checks if not c['passed']]
path = Path(__file__).with_name('joint-cubic-probe-certificate.json')
path.write_text(json.dumps(dict(scope='Synthetic exact algebra only; no actual-box value, time quadrature or cutoff bound',
                                checks=checks, failures=failures, passed=not failures), indent=2)+'\n')
print(json.dumps(dict(checks=len(checks), failures=len(failures),
                      maximum_exact_error=str(max(abs(F(c['exact_error'])) for c in checks)),
                      required_error='0', certificate=str(path))))
if failures:
    raise SystemExit(1)
