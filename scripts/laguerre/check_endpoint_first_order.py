#!/usr/bin/env python3
"""Exact algebra checks for L348; no asymptotic or sampled-value certification."""

from fractions import Fraction as F


def add(left, right):
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, F(0)) + coefficient
    return {m: c for m, c in result.items() if c}


def scale(poly, factor):
    return {m: c * factor for m, c in poly.items() if c * factor}


def multiply(left, right):
    result = {}
    for m, c in left.items():
        for n, d in right.items():
            monomial = tuple(sorted(m + n))
            result[monomial] = result.get(monomial, F(0)) + c * d
    return {m: c for m, c in result.items() if c}


def factors(number):
    result, divisor = {}, 2
    while divisor * divisor <= number:
        while number % divisor == 0:
            result[divisor] = result.get(divisor, 0) + 1
            number //= divisor
        divisor += 1
    if number > 1:
        result[number] = 1
    return result


def main():
    limit = 32
    fac = {n: factors(n) for n in range(1, limit + 1)}
    divisors = {n: [d for d in range(1, n + 1) if n % d == 0]
                for n in fac}
    mu = {n: 0 if any(e > 1 for e in f.values()) else (-1) ** len(f)
          for n, f in fac.items()}
    # Each log p is an independent formal variable: no floating-point logs.
    logs = {n: {(p,): F(e) for p, e in f.items()} for n, f in fac.items()}
    lam = {n: {(next(iter(f)),): F(1)} if len(f) == 1 else {}
           for n, f in fac.items()}
    second = {}
    for n in fac:
        second[n] = {}
        for d in divisors[n]:
            second[n] = add(second[n], scale(multiply(logs[d], logs[d]), mu[n // d]))

    count = 0
    for m in fac:
        for n in fac:
            direct = {}
            for j in divisors[m]:
                for k in divisors[n]:
                    total_log = add(logs[j], logs[k])
                    polynomial = add(total_log, scale(multiply(total_log, total_log), -F(1, 8)))
                    direct = add(direct, scale(polynomial, mu[m // j] * mu[n // k]))
            linear = add(scale(lam[m], int(n == 1)), scale(lam[n], int(m == 1)))
            quadratic = add(scale(second[m], int(n == 1)), scale(second[n], int(m == 1)))
            quadratic = add(quadratic, scale(multiply(lam[m], lam[n]), 2))
            assert direct == add(linear, scale(quadratic, -F(1, 8))), (m, n)
            count += 1

    # Clear the zeta denominators first, then check conjugate-pair algebra.
    x, y, u = ({(name,): F(1)} for name in ("x", "y", "u"))
    x2, y2 = multiply(x, x), multiply(y, y)
    re_second = add(u, add(x2, scale(y2, -1)))
    absolute_square = add(x2, y2)
    uncombined = add(scale(x, -2), scale(add(re_second, absolute_square), -F(1, 4)))
    combined = add(scale(x, -2), add(scale(u, -F(1, 4)), scale(x2, -F(1, 2))))
    assert uncombined == combined

    # For L=kappa/w+O(1), the 1/w coefficient of w*(-2L-L'/4-L^2/2).
    for kappa, expected in ((F(-1), -F(3, 4)), (F(1), -F(1, 4))):
        assert kappa / 4 - kappa * kappa / 2 == expected
    assert max(3 * F(1, 4), abs(F(1, 4) - 1)) == F(3, 4)

    print(f"OK: {count} formal divisor-polynomial identities, conjugate-pair algebra, "
          "two Laurent leading coefficients, and the minimax equality point.")
    print("These finite checks do not certify analytic remainders, infinite-series "
          "bounds, sampled values, or Laguerre signs.")


if __name__ == "__main__":
    main()
