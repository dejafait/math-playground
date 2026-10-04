"""Exact finite-group checks for the pinned forest Ward specialization.

Rational unit quaternions and dual numbers check the actual endpoint-averaged
clover rule. They do not integrate Wilson flow or estimate a continuum limit.
"""

from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from random import Random


ZERO = (F(0),) * 4
ONE = (F(1), F(0), F(0), F(0))
N = 4
A = F(8, N)
SUPPORT = (2, 2, 2, 2)
U_COEFFICIENTS = (F(2, 3), F(-1, 2), F(3, 5), F(4, 7))


def plus(p, q):
    return tuple(x + y for x, y in zip(p, q))


def scale(s, q):
    return tuple(s * x for x in q)


def mul(p, q):
    w, x, y, z = p
    v, r, s, t = q
    return (w*v - x*r - y*s - z*t,
            w*r + x*v + y*t - z*s,
            w*s + y*v + z*r - x*t,
            w*t + z*v + x*s - y*r)


def conj(q):
    return (q[0], -q[1], -q[2], -q[3])


def dmul(p, q):
    return mul(p[0], q[0]), plus(mul(p[1], q[0]), mul(p[0], q[1]))


def dconj(p):
    return conj(p[0]), conj(p[1])


def dplus(p, q):
    return plus(p[0], q[0]), plus(p[1], q[1])


def dscale(s, p):
    return scale(s, p[0]), scale(s, p[1])


def move(v, axis, amount):
    w = list(v)
    w[axis] += amount
    return tuple(w)


def interior(v):
    return all(0 < j < N for j in v)


VERTICES = tuple(product(range(N + 1), repeat=4))
INTERIOR = tuple(v for v in VERTICES if interior(v))
ALL_EDGES = tuple((axis, v) for v in VERTICES for axis in range(4)
                  if v[axis] < N)
VARIABLE = tuple(e for e in ALL_EDGES
                 if interior(e[1]) or interior(move(e[1], e[0], 1)))
assert len(VARIABLE) == 4 * N * (N - 1)**3


@lru_cache(None)
def word(v, rho, nu, sr, sn):
    steps = [(rho, sr), (nu, sn), (rho, -sr), (nu, -sn)]
    if sr * sn < 0:
        steps = [(axis, -sign) for axis, sign in reversed(steps)]
    point, result = v, []
    for axis, sign in steps:
        tail = point if sign > 0 else move(point, axis, -1)
        result.append(((axis, tail), sign))
        point = move(point, axis, sign)
    assert point == v
    return tuple(result)


def loop(links, edges):
    value = (ONE, ZERO)
    for edge, sign in edges:
        factor = links[edge] if sign > 0 else dconj(links[edge])
        value = dmul(value, factor)
    return value


def coefficients(links):
    """X_e, including all clover and endpoint transport derivatives."""
    clovers = {}
    for rho in range(4):
        for nu in range(rho + 1, 4):
            c = (ZERO, ZERO)
            for sr, sn in product((-1, 1), repeat=2):
                q = loop(links, word(SUPPORT, rho, nu, sr, sn))
                c = dplus(c, dscale(F(1, 8), dplus(q, dscale(-1, dconj(q)))))
            clovers[rho, nu] = c
            clovers[nu, rho] = dscale(-1, c)
    result = {}
    for e in ACTIVE_FULL:
        nu, x = e
        y = move(x, nu, 1)
        c = (ZERO, ZERO)
        for rho in range(4):
            if rho == nu:
                continue
            term = clovers[rho, nu]
            if y == SUPPORT:
                term = dmul(dmul(links[e], term), dconj(links[e]))
            c = dplus(c, dscale(U_COEFFICIENTS[rho] / (2*A), term))
        result[e] = c
    return result


ACTIVE_FULL = frozenset((axis, v) for axis in range(4)
                        for v in (SUPPORT, move(SUPPORT, axis, -1)))
GENERATOR = tuple(tuple(F(1, 2) if j == color + 1 else F(0)
                        for j in range(4)) for color in range(3))
# q0 I - i qj sigma_j uses -i sigma_j/2 as its orthonormal Lie basis.
# Simultaneous basis reversal changes no scalar divergence identity.


def rational_unit(rng):
    r = [F(rng.randint(-2, 2), 2) for _ in range(3)]
    norm = sum(x*x for x in r)
    q = ((1 - norm)/(1 + norm), *(2*x/(1 + norm) for x in r))
    assert mul(q, conj(q)) == ONE
    return q


def forest_paths(axis, reverse):
    paths = {}
    for v in VERTICES:
        path = []
        if interior(v):
            indices = range(N - 1, v[axis] - 1, -1) if reverse else range(v[axis])
            for j in indices:
                tail = list(v)
                tail[axis] = j
                path.append(((axis, tuple(tail)), -1 if reverse else 1))
        paths[v] = tuple(path)
    forest = frozenset(e for path in paths.values() for e, _ in path)
    assert len(forest) == len(INTERIOR)
    return paths, forest


def compensated(links, paths):
    x = coefficients(links)
    omega = {v: (ZERO, ZERO) for v in VERTICES}
    for v, path in paths.items():
        for edge, sign in path:
            omega[v] = dplus(omega[v], dscale(sign, x.get(edge, (ZERO, ZERO))))
    result = {}
    for e in VARIABLE:
        axis, tail = e
        head = move(tail, axis, 1)
        transported = dmul(dmul(links[e], omega[head]), dconj(links[e]))
        result[e] = dplus(dplus(x.get(e, (ZERO, ZERO)), omega[tail]),
                          dscale(-1, transported))
    return x, omega, result


def divergence(links, edges, selector):
    result = F(0)
    for e in edges:
        for color, generator in enumerate(GENERATOR):
            varied = links.copy()
            varied[e] = links[e][0], mul(generator, links[e][0])
            _, derivative = selector(varied).get(e, (ZERO, ZERO))
            result += 2 * derivative[color + 1]
    return result


def quotient(links, paths):
    p = {v: loop(links, path) for v, path in paths.items()}
    return {e: dmul(dmul(p[e[1]], links[e]), dconj(p[move(e[1], e[0], 1)]))
            for e in ALL_EDGES}


def scalar_action_derivative(links):
    result = F(0)
    for mu in range(4):
        for nu in range(mu + 1, 4):
            for v in VERTICES:
                if v[mu] < N and v[nu] < N:
                    _, derivative = loop(links, word(v, mu, nu, 1, 1))
                    result -= 4 * derivative[0]  # 4P = 4(1 - q0)
    return result


def plaquette_prediction(links):
    def u(v, axis):
        return U_COEFFICIENTS[axis] if v == SUPPORT else F(0)

    result, total_strain = F(0), F(0)
    for mu in range(4):
        for nu in range(mu + 1, 4):
            for sm, sn in product((0, 1), repeat=2):
                v = move(move(SUPPORT, mu, -sm), nu, -sn)
                vm, vn = move(v, mu, 1), move(v, nu, 1)
                vmn = move(vm, nu, 1)
                b = (u(vm, mu) + u(vmn, mu) - u(v, mu) - u(vn, mu)
                     + u(vn, nu) + u(vmn, nu) - u(v, nu) - u(vm, nu)) / (2*A)
                q, _ = loop(links, word(v, mu, nu, 1, 1))
                result += F(3, 8) * b * 2*q[0]
                total_strain += b
    assert total_strain == 0
    return result


for case, (axis, reverse) in enumerate(((0, False), (1, True))):
    paths, forest = forest_paths(axis, reverse)
    rng = Random(261025 + case)
    slice_links = {e: (rational_unit(rng) if e in VARIABLE and e not in forest
                       else ONE, ZERO) for e in ALL_EDGES}
    x, omega, y = compensated(slice_links, paths)
    assert all(y[f] == (ZERO, ZERO) for f in forest)
    assert all(omega[v] == (ZERO, ZERO) for v in VERTICES if not interior(v))
    touched = {v for v, path in paths.items() if any(e in ACTIVE_FULL for e, _ in path)}
    active_reduced = tuple(e for e in VARIABLE if e not in forest
                           and (e in ACTIVE_FULL or e[1] in touched
                                or move(e[1], e[0], 1) in touched))
    full = divergence(slice_links, ACTIVE_FULL, coefficients)
    restricted = divergence(slice_links, ACTIVE_FULL - forest, coefficients)
    reduced = divergence(slice_links, active_reduced,
                         lambda links: compensated(links, paths)[2])
    assert reduced == full == plaquette_prediction(slice_links)
    assert full != restricted, "Test must detect discarded compensator derivatives"
    full_direction = {e: (q, mul(x.get(e, (ZERO, ZERO))[0], q))
                      for e, (q, _) in slice_links.items()}
    slice_direction = {e: (q, mul(y.get(e, (ZERO, ZERO))[0], q))
                       for e, (q, _) in slice_links.items()}
    assert scalar_action_derivative(full_direction) == scalar_action_derivative(slice_direction)

    # Nontrivial off-slice gauge coordinates test inverse path orientations,
    # equivariance and the derivative of the full retraction, independently
    # of the reduced-divergence calculation above.
    k = {v: rational_unit(rng) if interior(v) else ONE for v in VERTICES}
    original = {e: (mul(mul(k[e[1]], q), conj(k[move(e[1], e[0], 1)])), ZERO)
                for e, (q, _) in slice_links.items()}
    recovered = quotient(original, paths)
    assert all(recovered[e][0] == slice_links[e][0] for e in ALL_EDGES)
    original_x = coefficients(original)
    original_direction = {e: (q, mul(original_x.get(e, (ZERO, ZERO))[0], q))
                          for e, (q, _) in original.items()}
    retracted_direction = quotient(original_direction, paths)
    assert retracted_direction == slice_direction
    compensation = reduced - restricted
    print(f"Forest {axis + 1}, {'upper' if reverse else 'lower'} face roots: "
          f"{len(forest)} pinned tree links, {len(active_reduced)} active remaining links; "
          "path derivative, action derivative and full/reduced divergence agree exactly.")
    print(f"Nonzero compensator divergence equals omitted tree divergence: {compensation}.")

print("Both checks use the clover rule with one-site rational coefficients strictly inside the box.")
print("The all-mesh proof covers the original displacement and both Wilson-flow probes.")
