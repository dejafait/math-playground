"""Finite interval certificate for det H_1, not a proof of RH.

Uses only Python's standard library. See PROOF.md, Lemmas 33, 35–36.
Every endpoint operation is outward rounded; exp is widened by one
representable neighbor on either side of its correctly rounded result.
"""

import argparse
import json
from decimal import (
    Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN,
    DivisionByZero, InvalidOperation, Overflow, Underflow, Subnormal,
)
from fractions import Fraction
from math import comb, factorial


PRECISION = 70
DOWN = Context(prec=PRECISION, rounding=ROUND_FLOOR)
UP = Context(prec=PRECISION, rounding=ROUND_CEILING)
NEAR = Context(prec=PRECISION, rounding=ROUND_HALF_EVEN)
for context in (DOWN, UP, NEAR):
    for signal in (DivisionByZero, InvalidOperation, Overflow, Underflow, Subnormal):
        context.traps[signal] = True


class I:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        if isinstance(lo, float) or isinstance(hi, float):
            raise TypeError("Binary floating-point inputs are forbidden")
        self.lo = Decimal(lo)
        self.hi = self.lo if hi is None else Decimal(hi)
        if not (self.lo.is_finite() and self.hi.is_finite() and self.lo <= self.hi):
            raise ValueError("Invalid interval")

    @staticmethod
    def lift(value):
        return value if isinstance(value, I) else I(value)

    @staticmethod
    def rational(value):
        value = Fraction(value)
        numerator, denominator = Decimal(value.numerator), Decimal(value.denominator)
        return I(DOWN.divide(numerator, denominator), UP.divide(numerator, denominator))

    def __add__(self, other):
        other = I.lift(other)
        return I(DOWN.add(self.lo, other.lo), UP.add(self.hi, other.hi))

    __radd__ = __add__

    def __neg__(self):
        return I(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, other):
        return self + (-I.lift(other))

    def __rsub__(self, other):
        return I.lift(other) + (-self)

    def __mul__(self, other):
        other = I.lift(other)
        pairs = [(a, b) for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return I(min(DOWN.multiply(a, b) for a, b in pairs),
                 max(UP.multiply(a, b) for a, b in pairs))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = I.lift(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError("Interval divisor contains zero")
        reciprocal = I(DOWN.divide(Decimal(1), other.hi),
                       UP.divide(Decimal(1), other.lo))
        return self * reciprocal

    def __pow__(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Only nonnegative integer powers")
        result, base = I(1), self
        while n:
            if n & 1:
                result = result * base
            base = base * base
            n //= 2
        return result

    def exp(self):
        lower = NEAR.exp(self.lo)
        upper = NEAR.exp(self.hi)
        return I(NEAR.next_minus(lower), NEAR.next_plus(upper))

    def magnitude(self):
        return max(self.lo.copy_abs(), self.hi.copy_abs())

    def data(self):
        return {"lower": str(self.lo), "upper": str(self.hi)}


ORDER = 8


def constant(value):
    return [I.lift(value)] + [I(0) for _ in range(ORDER)]


def variable(value):
    result = constant(value)
    result[1] = I(1)
    return result


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def scale(a, scalar):
    return [x * scalar for x in a]


def multiply(a, b):
    return [sum((a[j] * b[n-j] for j in range(n+1)), I(0))
            for n in range(ORDER+1)]


def exponential(a):
    b = [a[0].exp()]
    for n in range(1, ORDER+1):
        b.append(sum((j * a[j] * b[n-j] for j in range(1, n+1)), I(0)) / n)
    return b


def theta_kernel_jet(u, pi):
    ujet = variable(u)
    e2u = exponential(scale(ujet, 2))
    ehalf = exponential(scale(ujet, I.rational(Fraction(1, 2))))
    total = constant(0)
    for n in range(1, 5):
        v = scale(e2u, pi * (n*n))
        polynomial = add(scale(multiply(v, v), 8), scale(v, -12))
        total = add(total, multiply(polynomial, exponential(scale(v, -1))))
    return multiply(ehalf, total)


def moment_jet(u, k, kernel):
    power = [comb(k, j) * (u ** (k-j)) if j <= k else I(0)
             for j in range(ORDER+1)]
    return multiply(power, kernel)


def arctan_bounds(denominator, terms=96):
    x = Fraction(1, denominator)
    partial = sum(((-1)**j * x**(2*j+1) / (2*j+1) for j in range(terms)), Fraction(0))
    next_term = (-1)**terms * x**(2*terms+1) / (2*terms+1)
    return min(partial, partial + next_term), max(partial, partial + next_term)


def pi_bounds():
    a, b = arctan_bounds(5), arctan_bounds(239)
    low, high = 16*a[0] - 4*b[1], 16*a[1] - 4*b[0]
    return I(I.rational(low).lo, I.rational(high).hi)


def tail_bound():
    integral_coefficient = sum((Fraction(factorial(6), factorial(6-j)) *
                                Fraction(50**(6-j), 3**(j+1))
                                for j in range(7)), Fraction(0))
    return 128 * I(-150).exp() * I.rational(integral_coefficient) + 57600000 * I(-74).exp()


def certify(panels):
    # Dyadic panels make centers and half widths exact finite decimals.
    if panels < 1 or panels & (panels-1):
        raise ValueError("Panel count must be a positive power of two")
    pi = pi_bounds()
    h = I.rational(Fraction(1, panels))
    totals = {k: I(0) for k in (0, 2, 4, 6, 8)}
    error_totals = {k: I(0) for k in totals}
    for panel in range(panels):
        center = I.rational(Fraction(2*panel+1, panels))
        domain = I(I.rational(Fraction(2*panel, panels)).lo,
                   I.rational(Fraction(2*panel+2, panels)).hi)
        midpoint_kernel = theta_kernel_jet(center, pi)
        domain_kernel = theta_kernel_jet(domain, pi)
        for k in totals:
            coefficients = moment_jet(center, k, midpoint_kernel)
            derivative_bound = moment_jet(domain, k, domain_kernel)[8].magnitude()
            polynomial_integral = sum((2 * coefficients[j] * (h ** (j+1)) / (j+1)
                                       for j in (0, 2, 4, 6)), I(0))
            remainder = 2 * I(derivative_bound) * (h ** 9) / 9
            enclosure = polynomial_integral + I(remainder.hi.copy_negate(), remainder.hi)
            totals[k] = totals[k] + enclosure
            error_totals[k] = error_totals[k] + remainder
    tail = tail_bound()
    moments = {k: total + I(0, tail.hi) for k, total in totals.items()}
    if any(moment.lo <= 0 for moment in moments.values()):
        raise ArithmeticError("Moment enclosure is not strictly positive; refine panels")
    m0 = moments[0]
    a, b = moments[2] / (2*m0), moments[4] / (24*m0)
    c, d = moments[6] / (720*m0), moments[8] / (40320*m0)
    s2 = a**2 - 2*b
    s3 = a**3 - 3*a*b + 3*c
    s4 = a**4 - 4*a**2*b + 2*b**2 + 4*a*c - 4*d
    determinant = s2*s4 - s3**2
    expanded = a**2*b**2 - 4*b**3 - 2*a**3*c + 10*a*b*c - 9*c**2 - 4*a**2*d + 8*b*d
    # Both independently evaluated algebraic expressions must overlap.
    if max(determinant.lo, expanded.lo) > min(determinant.hi, expanded.hi):
        raise ArithmeticError("Equivalent determinant enclosures do not overlap")
    return {
        "scope": "finite det H_1 only; not RH",
        "precision": PRECISION, "panels": panels, "taylor_order": ORDER,
        "theta_terms": 4, "u_cutoff": 2,
        "pi": pi.data(), "common_tail_bound": tail.data(),
        "quadrature_error_bounds": {str(k): value.data() for k, value in error_totals.items()},
        "moments": {str(k): value.data() for k, value in moments.items()},
        "S2": s2.data(), "S3": s3.data(), "S4": s4.data(),
        "determinant": determinant.data(), "expanded_determinant": expanded.data(),
        "finite_sign_certified": determinant.lo > 0 and s2.lo > 0,
    }


def self_check():
    # Exact rational containment checks exercise signs and divisions.
    for a in (Fraction(-7, 3), Fraction(0), Fraction(5, 7)):
        for b in (Fraction(-11, 5), Fraction(2, 9)):
            ia, ib = I.rational(a), I.rational(b)
            for enclosed, exact in ((ia+ib, a+b), (ia*ib, a*b), (ia/ib, a/b)):
                assert Fraction(enclosed.lo) <= exact <= Fraction(enclosed.hi)
    assert I(0).exp().lo <= 1 <= I(0).exp().hi
    # For exp(u), every normalized coefficient at 0 equals 1/n!.
    coefficients = exponential(variable(I(0)))
    for n, coefficient in enumerate(coefficients):
        assert Fraction(coefficient.lo) <= Fraction(1, factorial(n)) <= Fraction(coefficient.hi)
    assert pi_bounds().lo > 3 and pi_bounds().hi < 4


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--panels", type=int, default=32)
    args = parser.parse_args()
    self_check()
    print(json.dumps(certify(args.panels), indent=2))
