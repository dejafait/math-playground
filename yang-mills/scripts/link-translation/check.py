"""Exact interior-stencil checks for L009; no mesh limit inferred numerically."""

from collections import defaultdict
from fractions import Fraction
from itertools import product


axes = range(4)
origin = (0, 0, 0, 0)


def shift(vertex, axis, amount):
    result = list(vertex)
    result[axis] += amount
    return tuple(result)


def add_scaled(target, source, scale):
    for key, value in source.items():
        target[key] += scale * value


def nonzero(row):
    return {key: value for key, value in row.items() if value}


def loop_row(vertex, rho, nu, sr, sn):
    """Build a based loop word, reversing it when its area is negative."""
    word = [(rho, sr), (nu, sn), (rho, -sr), (nu, -sn)]
    if sr * sn < 0:
        word = [(axis, -sign) for axis, sign in reversed(word)]
    row = defaultdict(Fraction)
    point = vertex
    for axis, sign in word:
        tail = point if sign > 0 else shift(point, axis, -1)
        row[(axis, tail)] += sign
        point = shift(point, axis, sign)
    assert point == vertex
    return nonzero(row)


def clover_circulation(vertex, rho, nu):
    row = defaultdict(Fraction)
    for sr, sn in product((-1, 1), repeat=2):
        loop = loop_row(vertex, rho, nu, sr, sn)
        lower = shift(shift(vertex, rho, min(sr, 0)), nu, min(sn, 0))
        # Independent canonical plaquette boundary, based at its lower corner.
        canonical = {
            (rho, lower): 1,
            (nu, shift(lower, rho, 1)): 1,
            (rho, shift(lower, nu, 1)): -1,
            (nu, lower): -1,
        }
        assert loop == canonical
        add_scaled(row, loop, Fraction(1, 4))
    return nonzero(row)


def gradient_composition(row, a):
    scalar_row = defaultdict(Fraction)
    for (axis, tail), coefficient in row.items():
        scalar_row[shift(tail, axis, 1)] += coefficient / a
        scalar_row[tail] -= coefficient / a
    return nonzero(scalar_row)


def curvature(rho, nu):
    if rho == nu:
        return 0
    if rho > nu:
        return -curvature(nu, rho)
    return 2 + 3 * rho + nu


def affine_potential(edge, a):
    nu, tail = edge
    # A_nu = (1/2) sum_rho F_rho nu x_rho at the edge midpoint.
    return sum(Fraction(1, 2) * curvature(rho, nu)
               * a * (tail[rho] + Fraction(rho == nu, 2)) for rho in axes)


checks = 0
for a in (Fraction(1), Fraction(2, 5), Fraction(3, 7)):
    for nu in axes:
        endpoint = shift(origin, nu, 1)
        row = defaultdict(Fraction)
        expected = Fraction(0)
        for rho in axes:
            if rho == nu:
                continue
            # Separate coefficients at the two endpoints: no divergence-free
            # cancellation is available to hide an orientation/scale error.
            lower_weight = Fraction(2 + rho, 3)
            upper_weight = Fraction(5 - rho + nu, 7)
            for vertex, weight in ((origin, lower_weight),
                                   (endpoint, upper_weight)):
                circulation = clover_circulation(vertex, rho, nu)
                add_scaled(row, circulation, weight / (2 * a))
            expected += (lower_weight + upper_weight) * curvature(rho, nu) / 2
        row = nonzero(row)
        assert not gradient_composition(row, a), "K d is not zero"
        assert row.get((nu, origin), 0) == 0, "Nonzero diagonal entry of K"
        value = sum(coefficient * affine_potential(edge, a)
                    for edge, coefficient in row.items())
        assert value == expected, (a, nu, value, expected)
        checks += 1

print(f"{checks} exact generator-row checks at three rational mesh sizes.")
print("All based loops have the required orientation; K d = 0 and diag K = 0.")
print("Constant-curvature affine potentials give the exact endpoint-averaged u F.")
print("The all-mode Gaussian residual limit is proved in L009, not by this check.")
