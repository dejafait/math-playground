"""Exact BCH and connected-contraction checks; not a box cutoff computation."""
from fractions import Fraction as F
from itertools import product
from math import factorial
from functools import lru_cache
from pathlib import Path
import json

N = 3
ZERO = (0,) * N


def add(*polys):
    out = {}
    for p in polys:
        for e, v in p.items():
            out[e] = out.get(e, F(0)) + v
    return {e: v for e, v in out.items() if v}


def scale(c, p):
    return {e: c * v for e, v in p.items() if c * v}


def mul(p, q):
    out = {}
    for e, v in p.items():
        for f, w in q.items():
            h = tuple(a + b for a, b in zip(e, f))
            if sum(h) <= 4:
                out[h] = out.get(h, F(0)) + v * w
    return {e: v for e, v in out.items() if v}


def vadd(*vectors):
    return tuple(add(*(v[i] for v in vectors)) for i in range(N))


def vscale(c, v):
    return tuple(scale(c, p) for p in v)


def dot(v, w):
    return add(*(mul(p, q) for p, q in zip(v, w)))


def bracket(v, w):
    # [i sigma_a/2, i sigma_b/2] = -epsilon_abc i sigma_c/2.
    return tuple(add(scale(-1, mul(v[(i + 1) % 3], w[(i + 2) % 3])),
                     mul(v[(i + 2) % 3], w[(i + 1) % 3])) for i in range(N))


def quatmul(left, right):
    s, v = left
    t, w = right
    return (add(mul(s, t), scale(F(-1, 4), dot(v, w))),
            vadd(tuple(mul(s, p) for p in w),
                 tuple(mul(t, p) for p in v), vscale(F(1, 2), bracket(v, w))))


def homogeneous(p, degree):
    return {e: v for e, v in p.items() if sum(e) == degree}


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(N))
                       for j in range(N)) for i in range(N))


def quadratic(matrix):
    p = {}
    for i, j in product(range(N), repeat=2):
        e = tuple(int(k == i) + int(k == j) for k in range(N))
        p = add(p, {e: matrix[i][j]})
    return p


def wick_moment_function(cov):
    @lru_cache(None)
    def moment(e):
        if not sum(e):
            return F(1)
        if sum(e) % 2:
            return F(0)
        i = next(k for k, a in enumerate(e) if a)
        left = list(e)
        left[i] -= 1
        total = F(0)
        for j, count in enumerate(left):
            if count:
                tail = left.copy()
                tail[j] -= 1
                total += count * cov[i][j] * moment(tuple(tail))
        return total
    return moment


def fullmul(p, q):
    # Moment products need all degrees through eight, without Taylor truncation.
    out = {}
    for e, v in p.items():
        for f, w in q.items():
            h = tuple(a + b for a, b in zip(e, f))
            out[h] = out.get(h, F(0)) + v * w
    return out


def expected(p, moment):
    return sum(v * moment(e) for e, v in p.items())


def cumulant(p, q, r, moment):
    ep, eq, er = (expected(x, moment) for x in (p, q, r))
    return (expected(fullmul(fullmul(p, q), r), moment)
            - expected(fullmul(p, q), moment) * er
            - expected(fullmul(p, r), moment) * eq
            - expected(fullmul(q, r), moment) * ep + 2 * ep * eq * er)


def pairings(indices):
    if not indices:
        yield ()
        return
    first, *rest = indices
    for j, partner in enumerate(rest):
        for tail in pairings(rest[:j] + rest[j + 1:]):
            yield ((first, partner),) + tail


groups = (0, 0, 1, 1, 2, 2, 2, 2)
classes = {0: [], 1: []}
for pairs in pairings(list(range(8))):
    reached = {0}
    while True:
        expanded = reached | {groups[j] for i, j in pairs if groups[i] in reached}
        expanded |= {groups[i] for i, j in pairs if groups[j] in reached}
        if expanded == reached:
            break
        reached = expanded
    if len(reached) == 3:
        internal = sum(i >= 4 and j >= 4 for i, j in pairs)
        classes[internal].append(pairs)


edge_sets = (
    (((1, 0, 1), (0, 1, 0), (0, 0, 1)),
     ((0, 1, 0), (1, 0, 0), (0, 0, 1)),
     ((-1, 0, 0), (0, -1, 1), (1, 0, 0)),
     ((0, -1, 0), (0, 0, -1), (0, 1, 0))),
    (((1, 0, 0), (0, 0, 0), (0, 0, 0)),
     ((0, 0, 0), (0, 1, 0), (0, 0, 0)),
     ((-1, 0, 0), (0, 0, 0), (0, 0, 0)),
     ((0, 0, 0), (0, -1, 0), (0, 0, 0))),
    (((1, 1, 0), (0, 0, 1), (0, 1, 0)),
     ((0, 0, 0), (0, 0, 0), (0, 0, 0)),
     ((0, -1, 0), (1, 0, 1), (0, 0, 1)),
     ((0, 0, 0), (0, 0, 0), (0, 0, 0))),
)
covariances = (((2, 1, 0), (1, 3, 1), (0, 1, 2)),
               ((1, 0, 0), (0, 2, 0), (0, 0, 3)))
B = ((2, -1, 1), (-1, 0, 2), (1, 2, -2))
R = ((0, 1, -1), (1, 3, 0), (-1, 0, 1))
variables = tuple({tuple(int(i == j) for i in range(N)): F(1)} for j in range(N))
checks = []
failures = []
for edge_case, edge_matrices in enumerate(edge_sets):
    edges = [tuple(add(*(scale(F(c), variables[j]) for j, c in enumerate(row)))
                   for row in matrix) for matrix in edge_matrices]
    w1 = w2 = w3 = ({}, {}, {})
    quat = ({ZERO: F(1)}, ({}, {}, {}))
    for X in edges:
        old1, old2, old3 = w1, w2, w3
        w1 = vadd(old1, X)
        w2 = vadd(old2, vscale(F(1, 2), bracket(old1, X)))
        w3 = vadd(old3, vscale(F(1, 2), bracket(old2, X)),
                  vscale(F(1, 12), bracket(old1, bracket(old1, X))),
                  vscale(F(1, 12), bracket(X, bracket(X, old1))))
        norm2 = dot(X, X)
        scalar = add({ZERO: F(1)}, scale(F(-1, 8), norm2),
                     scale(F(1, 384), mul(norm2, norm2)))
        vector = vadd(X, tuple(scale(F(-1, 24), mul(norm2, p)) for p in X))
        quat = quatmul(quat, (scalar, vector))
    q = add(scale(F(1, 2), dot(w2, w2)), dot(w1, w3))
    radial = scale(F(-1, 96), mul(dot(w1, w1), dot(w1, w1)))
    trace_quartic = scale(-4, homogeneous(quat[0], 4))
    defect = add(trace_quartic, scale(-1, add(q, radial)))
    checks.append({"type": "BCH_vs_product_trace", "edge_case": edge_case,
                   "defect": {str(e): str(v) for e, v in defect.items()}})
    if defect:
        failures.append({"type": "BCH", "edge_case": edge_case})
    if edge_case == 1:
        assert not any(w1)
        assert q == {(2, 2, 0): F(1, 2)}
        checks.append({"type": "zero_curvature_obstruction",
                       "q": "x0^2*x1^2/2", "value_at_x0_x1_equal_one": "1/2"})
    for cov_case, cov in enumerate(covariances):
        U = matmul(matmul(cov, B), cov)
        V = matmul(matmul(cov, R), cov)
        W = matmul(matmul(matmul(matmul(cov, B), cov), R), cov)
        tensor = {}
        for indices in product(range(N), repeat=4):
            e = tuple(indices.count(i) for i in range(N))
            multiplicity = factorial(4)
            for count in e:
                multiplicity //= factorial(count)
            tensor[indices] = q.get(e, F(0)) / multiplicity
        fourth = 24 * sum(k * U[a][b] * V[c][d]
                          for (a, b, c, d), k in tensor.items())
        second = 48 * sum(k * cov[c][d] * W[a][b]
                          for (a, b, c, d), k in tensor.items())
        totals = {0: F(0), 1: F(0)}
        for e, coefficient in q.items():
            action_indices = tuple(i for i, count in enumerate(e) for _ in range(count))
            for a, b, c, d in product(range(N), repeat=4):
                factor = coefficient * B[a][b] * R[c][d]
                if not factor:
                    continue
                indices = (a, b, c, d) + action_indices
                for internal, pairs_list in classes.items():
                    for pairs in pairs_list:
                        value = factor
                        for i, j in pairs:
                            value *= cov[indices[i]][indices[j]]
                        totals[internal] += value
        moment_result = cumulant(quadratic(B), quadratic(R), q,
                                 wick_moment_function(cov))
        ok = totals[0] == fourth and totals[1] == second and moment_result == fourth + second
        checks.append({"type": "connected_quartic", "edge_case": edge_case,
                       "covariance_case": cov_case, "q": {str(e): str(v) for e, v in q.items()},
                       "covariance": cov, "probe_matrix": B, "residual_matrix": R,
                       "fourth_chaos_pairings": str(totals[0]), "fourth_chaos_formula": str(fourth),
                       "quadratic_chaos_pairings": str(totals[1]), "quadratic_chaos_formula": str(second),
                       "full_moment_cumulant": str(moment_result),
                       "negative_action_contribution": str(-moment_result), "pass": ok})
        if not ok:
            failures.append({"type": "contraction", "edge_case": edge_case, "covariance_case": cov_case})
out = Path(__file__).with_name("nonradial-action-certificate.json")
out.write_text(json.dumps({"scope": "Exact finite algebra only; no original-box numerical evaluation",
                          "connected_pairing_counts": {str(k): len(v) for k, v in classes.items()},
                          "checks": checks, "failures": failures,
                          "cutoff_bounds": {"actual": "not established", "required": "full Gamma logarithm and no faster growth"}},
                         indent=2) + "\n")
print(f"{'PASS' if not failures else 'FAIL'}: {len(checks)} exact checks; failures={len(failures)}")
print("Actual/required cutoff bounds: not established / full Gamma logarithm and no faster growth.")
print(f"Certificate: {out.relative_to(Path.cwd())}")
assert not failures, failures
