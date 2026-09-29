#!/usr/bin/env python3
"""Exact local algebra checks for L016; no assertion about global gluing."""

from fractions import Fraction
from itertools import product


NAMES = "tau beta A0 A1 A2 B0 B1 B2 D0 D1 D2 a b c e x y".split()
ZERO_MONOMIAL = (0,) * len(NAMES)
ZERO = {}
ONE = {ZERO_MONOMIAL: Fraction(1)}


def add(*polynomials):
    out = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            out[monomial] = out.get(monomial, 0) + coefficient
    return {m: c for m, c in out.items() if c}


def scale(polynomial, coefficient):
    return {m: coefficient * c for m, c in polynomial.items()
            if coefficient * c}


def multiply(left, right):
    out = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            monomial = tuple(a + b for a, b in zip(lm, rm))
            if monomial[0] < 3:  # Work exactly modulo tau^3.
                out[monomial] = out.get(monomial, 0) + lc * rc
    return {m: c for m, c in out.items() if c}


def variable(name):
    monomial = list(ZERO_MONOMIAL)
    monomial[NAMES.index(name)] = 1
    return {tuple(monomial): Fraction(1)}


def power(polynomial, exponent):
    out = ONE
    for _ in range(exponent):
        out = multiply(out, polynomial)
    return out


def specialize_zero(polynomial, names):
    indices = [NAMES.index(name) for name in names]
    return {m: c for m, c in polynomial.items()
            if all(m[i] == 0 for i in indices)}


UNIT, Q, Z = ((ONE, ZERO, ZERO), (ZERO, ONE, ZERO),
              (ZERO, ZERO, ONE))
BASIS = (UNIT, Q, Z)


def table(qq, qz, zz):
    return ((UNIT, Q, Z), (Q, qq, qz), (Z, qz, zz))


def vmul(left, right, multiplication):
    return tuple(add(*(multiply(multiply(left[i], right[j]),
                                multiplication[i][j][k])
                       for i in range(3) for j in range(3)))
                 for k in range(3))


def vsub(left, right):
    return tuple(add(a, scale(b, -1)) for a, b in zip(left, right))


def trace(value, multiplication):
    return add(*(vmul(value, basis, multiplication)[i]
                 for i, basis in enumerate(BASIS)))


def check_associative(multiplication):
    for left, middle, right in product(BASIS, repeat=3):
        assert vmul(vmul(left, middle, multiplication), right,
                    multiplication) == vmul(
                        left, vmul(middle, right, multiplication),
                        multiplication)


def main():
    tau = variable("tau")
    tau2 = power(tau, 2)
    beta = variable("beta")
    coeff = {name: variable(name) for name in NAMES[2:11]}
    qq = tuple(multiply(tau2, coeff[f"A{i}"]) for i in range(3))
    qz = tuple(multiply(tau2, coeff[f"B{i}"]) for i in range(3))
    zz = (multiply(tau2, coeff["D0"]),
          add(multiply(tau, beta), multiply(tau2, coeff["D1"])),
          multiply(tau2, coeff["D2"]))
    general = table(qq, qz, zz)

    # The two independent nontrivial basis associators force all scalar terms.
    assert vsub(vmul(qq, Z, general), vmul(Q, qz, general)) == (
        ZERO, scale(multiply(tau2, coeff["B0"]), -1),
        multiply(tau2, coeff["A0"]))
    assert vsub(vmul(qz, Z, general), vmul(Q, zz, general)) == (
        ZERO, scale(multiply(tau2, coeff["D0"]), -1),
        multiply(tau2, coeff["B0"]))

    restricted = tuple(tuple(tuple(specialize_zero(p, ("A0", "B0", "D0"))
                                        for p in vector)
                                  for vector in row) for row in general)
    check_associative(restricted)
    assert trace(Q, restricted) == multiply(tau2, add(coeff["A1"], coeff["B2"]))
    assert trace(Z, restricted) == multiply(tau2, add(coeff["B1"], coeff["D2"]))
    third = Fraction(1, 3)
    for left, right in product(BASIS, repeat=2):
        assert scale(trace(vmul(left, right, restricted), restricted), third) == (
            multiply(scale(trace(left, restricted), third),
                     scale(trace(right, restricted), third)))

    # The invariant cubic u wedge m(u,u) for trace-free multiplication.
    a, b, c, e, x, y = (variable(name) for name in "a b c e x y".split())
    normal_q = add(multiply(a, power(x, 2)),
                   scale(multiply(c, multiply(x, y)), 2),
                   multiply(e, power(y, 2)))
    normal_z = add(multiply(b, power(x, 2)),
                   scale(multiply(a, multiply(x, y)), -2),
                   scale(multiply(c, power(y, 2)), -1))
    wedge = add(multiply(x, normal_z), scale(multiply(y, normal_q), -1))
    assert wedge == add(multiply(b, power(x, 3)),
                        scale(multiply(a, multiply(power(x, 2), y)), -3),
                        scale(multiply(c, multiply(x, power(y, 2))), -3),
                        scale(multiply(e, power(y, 3)), -1))

    # Poonen's table with a=d=tau, b=c=0: trace need not be a section.
    unrestricted = table((ZERO, ZERO, scale(tau, -1)),
                         (scale(tau2, -1), ZERO, ZERO),
                         (ZERO, tau, ZERO))
    check_associative(unrestricted)
    assert trace(Q, unrestricted) == trace(Z, unrestricted) == ZERO
    assert scale(trace(vmul(Q, Z, unrestricted), unrestricted), third) == scale(tau2, -1)
    assert third - 1 == Fraction(-2, 3)  # Determinant of the two residue equations.
    print("PASS: all order-two scalar terms are forced to zero in the fibre-restricted algebra.")
    print("PASS: normalized trace is multiplicative for every remaining order-two coefficient.")
    print("PASS: trace-free cubic tensor and mixed-residue rank identities.")
    print("PASS: unrestricted cubic example has nonzero trace defect -tau^2.")


if __name__ == "__main__":
    main()
