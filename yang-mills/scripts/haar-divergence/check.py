"""Exact SU(2) loop differentiation for L010; no interacting limit inferred."""

from fractions import Fraction as F
from itertools import product
from random import Random


ZERO = (F(0),) * 4
ONE = (F(1), F(0), F(0), F(0))
ORIGIN = (0, 0, 0, 0)
AXES = range(4)


def add(p, q):
    return tuple(x + y for x, y in zip(p, q))


def scale(c, q):
    return tuple(c * x for x in q)


def mul(p, q):
    # Unit quaternions represent q0 I - i sum_j qj sigma_j.
    w, x, y, z = p
    v, r, s, t = q
    return (w*v - x*r - y*s - z*t,
            w*r + x*v + y*t - z*s,
            w*s + y*v + z*r - x*t,
            w*t + z*v + x*s - y*r)


def conj(q):
    return (q[0], -q[1], -q[2], -q[3])


def dual_mul(p, q):
    return (mul(p[0], q[0]), add(mul(p[1], q[0]), mul(p[0], q[1])))


def shift(vertex, axis, amount):
    result = list(vertex)
    result[axis] += amount
    return tuple(result)


def word(vertex, rho, nu, sr, sn):
    steps = [(rho, sr), (nu, sn), (rho, -sr), (nu, -sn)]
    if sr * sn < 0:
        steps = [(axis, -sign) for axis, sign in reversed(steps)]
    point = vertex
    result = []
    for axis, sign in steps:
        tail = point if sign > 0 else shift(point, axis, -1)
        result.append(((axis, tail), sign))
        point = shift(point, axis, sign)
    assert point == vertex
    return result


class Configuration:
    def __init__(self):
        self.rng = Random(261009)
        self.links = {}

    def link(self, edge):
        if edge not in self.links:
            r = [F(self.rng.randint(-3, 3), 4) for _ in range(3)]
            radius = sum(x*x for x in r)
            q = ((1-radius)/(1+radius), *(2*x/(1+radius) for x in r))
            assert mul(q, conj(q)) == ONE
            self.links[edge] = q
        return self.links[edge]

    def dual_link(self, edge, sign, varied, color):
        q = self.link(edge)
        generator = tuple(F(1, 2) if j == color+1 else F(0) for j in range(4))
        dq = mul(generator, q) if edge == varied else ZERO
        return (q, dq) if sign > 0 else (conj(q), conj(dq))

    def loop(self, edges, varied=None, color=0):
        result = (ONE, ZERO)
        for edge, sign in edges:
            result = dual_mul(result, self.dual_link(edge, sign, varied, color))
        return result

    def clover(self, vertex, rho, nu, varied, color):
        value, derivative = ZERO, ZERO
        for sr, sn in product((-1, 1), repeat=2):
            q, dq = self.loop(word(vertex, rho, nu, sr, sn), varied, color)
            value = add(value, scale(F(1, 8), add(q, scale(-1, conj(q)))))
            derivative = add(derivative, scale(F(1, 8), add(dq, scale(-1, conj(dq)))))
        return value, derivative


def displacement(vertex):
    # Finite support and independent endpoint coefficients; no continuum
    # divergence-free assumption is used in the exact group identity.
    if vertex == ORIGIN:
        return (F(2, 3), F(-1, 2), F(3, 5), F(4, 7))
    if vertex == shift(ORIGIN, 0, 1):
        return (F(-3, 7), F(4, 5), F(1, 3), F(-2, 9))
    return ZERO


def divergence_row(config, edge, a):
    nu, x = edge
    y = shift(x, nu, 1)
    result = F(0)
    for color in range(3):
        derivative = ZERO
        for rho in AXES:
            if rho == nu:
                continue
            if displacement(x)[rho]:
                _, dc = config.clover(x, rho, nu, edge, color)
                derivative = add(derivative, scale(displacement(x)[rho]/(2*a), dc))
            if displacement(y)[rho]:
                c = config.clover(y, rho, nu, edge, color)
                left = config.dual_link(edge, 1, edge, color)
                right = config.dual_link(edge, -1, edge, color)
                _, dc = dual_mul(dual_mul(left, c), right)
                derivative = add(derivative, scale(displacement(y)[rho]/(2*a), dc))
        # Lie algebra coefficients are twice the vector quaternion components.
        result += 2 * derivative[color+1]
    return result


def plaquette_trace(config, z, mu, nu):
    q, _ = config.loop(word(z, mu, nu, 1, 1))
    return 2*q[0]


def row_prediction(config, edge, a):
    nu, x = edge
    y = shift(x, nu, 1)
    result = F(0)
    for rho in AXES:
        if rho == nu:
            continue
        left = plaquette_trace(config, shift(x, rho, -1), rho, nu)
        right = plaquette_trace(config, x, rho, nu)
        result += F(3, 16)/a * (displacement(x)[rho] + displacement(y)[rho]) * (left-right)
    return result


def strain(z, mu, nu, a):
    xm = shift(z, mu, 1)
    xn = shift(z, nu, 1)
    xmn = shift(xm, nu, 1)
    return (displacement(xm)[mu] + displacement(xmn)[mu]
            - displacement(z)[mu] - displacement(xn)[mu]
            + displacement(xn)[nu] + displacement(xmn)[nu]
            - displacement(z)[nu] - displacement(xm)[nu]) / (2*a)


support = (ORIGIN, shift(ORIGIN, 0, 1))
edges = sorted({(nu, tail) for v in support for nu in AXES
                for tail in (v, shift(v, nu, -1))})
plaquettes = sorted({(mu, nu, shift(shift(v, mu, -sm), nu, -sn))
                     for v in support for mu in AXES for nu in AXES if mu < nu
                     for sm, sn in product((0, 1), repeat=2)})
config = Configuration()
row_checks = 0
for a in (F(1), F(2, 5), F(3, 7)):
    actual = F(0)
    for edge in edges:
        value = divergence_row(config, edge, a)
        assert value == row_prediction(config, edge, a), (edge, a)
        actual += value
        row_checks += 1
    total_strain = sum(strain(z, mu, nu, a) for mu, nu, z in plaquettes)
    assert total_strain == 0
    regrouped = F(3, 8) * sum(strain(z, mu, nu, a) * plaquette_trace(config, z, mu, nu)
                             for mu, nu, z in plaquettes)
    wilson_form = -F(3, 4) * sum(strain(z, mu, nu, a) * (1-plaquette_trace(config, z, mu, nu)/2)
                               for mu, nu, z in plaquettes)
    assert actual == regrouped == wilson_form
    assert actual != 0, "Chosen nonlinear test configuration unexpectedly cancels"

print(f"{row_checks} exact link-divergence checks at three rational mesh sizes.")
print("Endpoint transport derivatives included; both plaquette regroupings agree exactly.")
print("Constant term telescopes to zero; full nonlinear divergence is nonzero in this test.")
print("The coefficient -3/32 and the all-mode response limit are proved in L010.")
