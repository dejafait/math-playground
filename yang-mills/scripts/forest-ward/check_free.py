"""Finite checks of the forest free operator; no ultraviolet estimate.

Exact rational stencil/path checks are followed by Gaussian matrix checks.
The N=4 sample uses one-site rational coefficients, not L008's smooth u_a.
Its two quadratics retain L008's plaquette-average and clover-product rules.
The proof in L017 covers the original coefficients and the actual probes.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product

import numpy as np


N = 4
A = F(8, N)
TAU = F(1, 16)
SUPPORT = (2, 2, 2, 2)
COEFFICIENTS = (F(2, 3), F(-1, 2), F(3, 5), F(4, 7))
AXES = range(4)
VERTICES = tuple(product(range(N + 1), repeat=4))


def move(v, axis, step):
    w = list(v)
    w[axis] += step
    return tuple(w)


def interior(v):
    return all(0 < j < N for j in v)


INTERIOR = tuple(v for v in VERTICES if interior(v))
EDGES = tuple((mu, v) for v in VERTICES for mu in AXES if v[mu] < N
              and (interior(v) or interior(move(v, mu, 1))))
INDEX = {e: j for j, e in enumerate(EDGES)}
PLAQUETTES = tuple((mu, nu, v) for mu, nu in combinations(AXES, 2)
                   for v in VERTICES if v[mu] < N and v[nu] < N
                   and all(0 < v[rho] < N for rho in AXES
                           if rho not in (mu, nu)))
P_INDEX = {p: j for j, p in enumerate(PLAQUETTES)}


def clean(row):
    return {key: value for key, value in row.items() if value}


def add(target, row, weight=F(1)):
    for key, value in row.items():
        target[key] += weight * value


def boundary(mu, nu, v):
    return {(mu, v): F(1), (nu, move(v, mu, 1)): F(1),
            (mu, move(v, nu, 1)): F(-1), (nu, v): F(-1)}


def clover(v, mu, nu):
    if mu == nu:
        return {}
    if mu > nu:
        return {e: -w for e, w in clover(v, nu, mu).items()}
    row = defaultdict(F)
    for sm, sn in product((0, 1), repeat=2):
        lower = move(move(v, mu, -sm), nu, -sn)
        add(row, boundary(mu, nu, lower), F(1, 4))
    return clean(row)


def u(v, mu):
    return COEFFICIENTS[mu] if v == SUPPORT else F(0)


K_ROWS = {}
for edge in EDGES:
    nu, x = edge
    y = move(x, nu, 1)
    row = defaultdict(F)
    for rho in AXES:
        if rho != nu:
            for v in (x, y):
                if u(v, rho):
                    add(row, clover(v, rho, nu), u(v, rho) / (2 * A))
    K_ROWS[edge] = clean(row)
    assert set(K_ROWS[edge]).issubset(INDEX)
    assert K_ROWS[edge].get(edge, 0) == 0
    gradient = defaultdict(F)
    for (mu, tail), weight in K_ROWS[edge].items():
        if interior(tail):
            gradient[tail] -= weight
        head = move(tail, mu, 1)
        if interior(head):
            gradient[head] += weight
    assert not clean(gradient), "K must annihilate pinned gradients"


def paths(axis, reverse):
    result = {}
    for v in VERTICES:
        path = []
        if interior(v):
            levels = range(N - 1, v[axis] - 1, -1) if reverse else range(v[axis])
            for j in levels:
                tail = list(v)
                tail[axis] = j
                path.append(((axis, tuple(tail)), -1 if reverse else 1))
        result[v] = tuple(path)
    return result


C = np.zeros((len(PLAQUETTES), len(EDGES)))
for j, (mu, nu, v) in enumerate(PLAQUETTES):
    for e, weight in boundary(mu, nu, v).items():
        if e in INDEX:
            C[j, INDEX[e]] = float(weight)
G = np.zeros((len(EDGES), len(INTERIOR)))
V_INDEX = {v: j for j, v in enumerate(INTERIOR)}
for e, j in INDEX.items():
    mu, tail = e
    for v, sign in ((tail, -1), (move(tail, mu, 1), 1)):
        if v in V_INDEX:
            G[j, V_INDEX[v]] = sign
assert not np.any(C @ G)
K = np.zeros((len(EDGES), len(EDGES)))
for e, row in K_ROWS.items():
    for source, weight in row.items():
        K[INDEX[e], INDEX[source]] = float(weight)

# Quadratic matrices in x = a A coordinates, retaining average of squares
# in the triplet and products of averaged curvatures in the shear.
Q = [np.zeros((len(EDGES), len(EDGES))) for _ in range(2)]
for v in INTERIOR:
    w = [(u(move(v, mu, 1), mu) - u(move(v, mu, -1), mu)) / (2 * A)
         for mu in AXES]
    s = {(mu, nu): (u(move(v, mu, 1), nu) - u(move(v, mu, -1), nu)
                   + u(move(v, nu, 1), mu) - u(move(v, nu, -1), mu)) / (2 * A)
         for mu, nu in combinations(AXES, 2)}
    bars = {}
    for mu, nu in combinations(AXES, 2):
        rows = [C[P_INDEX[mu, nu, move(move(v, mu, -sm), nu, -sn)]]
                for sm, sn in product((0, 1), repeat=2)]
        bars[mu, nu] = sum(rows) / 4
        bars[nu, mu] = -bars[mu, nu]
        if w[mu] + w[nu]:
            for row in rows:
                Q[0] += float((w[mu] + w[nu]) / 4) * np.outer(row, row)
    for mu in AXES:
        bars[mu, mu] = np.zeros(len(EDGES))
    for mu, nu in combinations(AXES, 2):
        if s[mu, nu]:
            for alpha in AXES:
                left, right = bars[mu, alpha], bars[nu, alpha]
                Q[1] += float(s[mu, nu]) * (np.outer(left, right)
                                          + np.outer(right, left)) / 2

L = C.T @ C
DELTA = L + G @ G.T
SIGMA = np.linalg.inv(DELTA)


def heat(matrix):
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * np.exp(-float(TAU) * values / float(A**2))) @ vectors.T


WILSON_HEAT, HODGE_HEAT = heat(L), heat(DELTA)
assert np.max(np.abs(C @ (WILSON_HEAT - HODGE_HEAT))) < 2e-12
Q_FLOW = [HODGE_HEAT @ q @ HODGE_HEAT for q in Q]
FULL_RESPONSE = np.array([6 * np.trace(q @ K @ SIGMA) for q in Q_FLOW])
assert np.linalg.norm(FULL_RESPONSE) > 1e-5

for axis, reverse in ((0, False), (1, True)):
    path_map = paths(axis, reverse)
    forest = {e for path in path_map.values() for e, _ in path}
    remaining = tuple(e for e in EDGES if e not in forest)
    indices = [INDEX[e] for e in remaining]
    assert len(forest) == len(INTERIOR) == 81
    potentials = {}
    for v, path in path_map.items():
        row = defaultdict(F)
        for e, sign in path:
            add(row, K_ROWS[e], sign)
        potentials[v] = clean(row)
    reduced_rows = {}
    for e in EDGES:
        nu, x = e
        row = defaultdict(F)
        add(row, K_ROWS[e])
        add(row, potentials[x])
        add(row, potentials[move(x, nu, 1)], F(-1))
        reduced_rows[e] = {source: weight for source, weight in clean(row).items()
                           if source not in forest}
    assert all(not reduced_rows[e] for e in forest)
    diagonal = [reduced_rows[e].get(e, F(0)) for e in remaining]
    assert sum(diagonal) == 0
    assert any(diagonal), "Sample must detect nonzero reduced diagonal entries"

    # Independent plaquette-boundary contraction checks the curvature map
    # exactly, including plaquettes adjacent to each pinned face.
    exact_missing_path_error = F(0)
    for mu, nu, v in PLAQUETTES:
        actual, expected, naive_curvature = defaultdict(F), defaultdict(F), defaultdict(F)
        for e, sign in boundary(mu, nu, v).items():
            if e in INDEX:
                add(actual, reduced_rows[e], sign)
                add(expected, {source: weight for source, weight in K_ROWS[e].items()
                               if source not in forest}, sign)
                if e not in forest:
                    add(naive_curvature,
                        {source: weight for source, weight in K_ROWS[e].items()
                         if source not in forest}, sign)
        assert clean(actual) == clean(expected)
        add(naive_curvature, expected, F(-1))
        exact_missing_path_error = max(exact_missing_path_error,
                                       max(map(abs, naive_curvature.values()), default=F(0)))
    assert exact_missing_path_error > 0

    kf = np.zeros((len(remaining), len(remaining)))
    reduced_index = {e: j for j, e in enumerate(remaining)}
    for e in remaining:
        for source, weight in reduced_rows[e].items():
            kf[reduced_index[e], reduced_index[source]] = float(weight)
    cf = C[:, indices]
    hessian = cf.T @ cf
    sigma_f = np.linalg.inv(hessian)
    curvature_error = np.max(np.abs(cf @ sigma_f @ cf.T - C @ SIGMA @ C.T))
    assert curvature_error < 2e-12
    insertion = (hessian @ kf + kf.T @ hessian) / 2
    responses, covariances = [], []
    for q, q_full in zip(Q, Q_FLOW):
        qf = (WILSON_HEAT @ q @ WILSON_HEAT)[np.ix_(indices, indices)]
        responses.append(6 * np.trace(qf @ kf @ sigma_f))
        covariances.append(6 * np.trace(qf @ sigma_f @ insertion @ sigma_f))
        assert np.max(np.abs(qf - q_full[np.ix_(indices, indices)])) < 2e-12
    response_error = max(np.max(np.abs(np.array(responses) - FULL_RESPONSE)),
                         np.max(np.abs(np.array(covariances) - FULL_RESPONSE)))
    assert response_error < 2e-10
    naive = K[np.ix_(indices, indices)]
    missing_path_error = np.max(np.abs(cf @ naive - (C @ K)[:, indices]))
    assert abs(missing_path_error - float(exact_missing_path_error)) < 1e-15
    print(f"Forest {axis + 1}, {'upper' if reverse else 'lower'} face: "
          f"{sum(bool(x) for x in diagonal)} nonzero reduced diagonal entries; "
          "exact total trace 0 and exact curvature/action-variation equality.")
    print(f"Gaussian curvature error {curvature_error:.3g}; "
          f"two-response/IBP error {response_error:.3g}; "
          f"exact curvature error after deleting paths {exact_missing_path_error}.")

print("Three-color sample flowed responses:", FULL_RESPONSE.tolist())
print("These finite samples test the representation; L017 proves the actual-probe comparison.")
