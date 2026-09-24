#!/usr/bin/env python3
"""Exact Leibniz check of L316's two product identities, using integer polynomials.

This is an algebra check, not a numerical zeta or sign certificate.
"""
from math import comb


NAMES = ("b1", "b2", "b3", "b4", "u0", "u1", "u2", "u3", "u4")
ZERO = (0,) * len(NAMES)


def add(*polys):
    result = {}
    for poly in polys:
        for powers, coefficient in poly.items():
            result[powers] = result.get(powers, 0) + coefficient
    return {powers: coefficient for powers, coefficient in result.items() if coefficient}


def scale(poly, coefficient):
    return {powers: value * coefficient for powers, value in poly.items() if value * coefficient}


def mul(left, right):
    result = {}
    for lp, lc in left.items():
        for rp, rc in right.items():
            powers = tuple(a + b for a, b in zip(lp, rp))
            result[powers] = result.get(powers, 0) + lc * rc
    return {powers: coefficient for powers, coefficient in result.items() if coefficient}


def variable(index):
    powers = list(ZERO)
    powers[index] = 1
    return {tuple(powers): 1}


def differentiate_b(poly):
    """Formal derivative b_j -> b_(j+1); only j<=3 is needed."""
    result = {}
    for powers, coefficient in poly.items():
        for index in range(3):
            if powers[index]:
                new_powers = list(powers)
                new_powers[index] -= 1
                new_powers[index + 1] += 1
                result = add(result, {tuple(new_powers): coefficient * powers[index]})
    return result


def main():
    b1, b2, b3, b4, *u = [variable(index) for index in range(len(NAMES))]
    # G_j = (exp(b))^(j) / exp(b), constructed by differentiation.
    g = [{ZERO: 1}]
    for _ in range(4):
        g.append(add(differentiate_b(g[-1]), mul(b1, g[-1])))
    # Leibniz, independent of the Taylor-product proof in L316.
    f = [add(*(scale(mul(g[k], u[j - k]), comb(j, k)) for k in range(j + 1)))
         for j in range(5)]
    q = lambda v: add(mul(v[1], v[1]), scale(mul(v[0], v[2]), -1))
    t = lambda v: add(mul(v[0], v[4]), scale(mul(v[1], v[3]), -4),
                      scale(mul(v[2], v[2]), 3))
    expected_q = add(q(u), scale(mul(b2, mul(u[0], u[0])), -1))
    expected_t = add(t(u), scale(mul(b2, q(u)), -12),
                     mul(add(b4, scale(mul(b2, b2), 6)), mul(u[0], u[0])))
    for name, actual, expected in (("Q", q(f), expected_q), ("T", t(f), expected_t)):
        residual = add(actual, scale(expected, -1))
        if residual:
            raise AssertionError((name, residual))
        print(f"{name}: exact polynomial residual is zero")
    print("The b1 and b3 terms cancel; the comparison follows by subtracting kappa * Q.")


if __name__ == "__main__":
    main()
