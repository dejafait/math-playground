#!/usr/bin/env python3
"""Exact finite algebra checks for L318; no actual-zeta sign computation."""

from collections import defaultdict
from fractions import Fraction as F
from math import factorial, gcd


PRIMES = (2, 3, 5, 7, 11)


def exponents(n):
    result = []
    for p in PRIMES:
        power = 0
        while n % p == 0:
            n //= p
            power += 1
        result.append(power)
    assert n == 1
    return tuple(result)


def log_symbol(n):
    # Rational substitutions for independent prime logarithms, extended additively.
    return sum(F(p, p + 1) * e for p, e in zip(PRIMES, exponents(n)))


def reciprocal_sqrt(n):
    # Return (d,c) with d squarefree and 1/sqrt(n) = c*sqrt(d).
    root, squarefree = 1, 1
    for p, e in zip(PRIMES, exponents(n)):
        root *= p ** (e // 2)
        squarefree *= p ** (e % 2)
    assert root * root * squarefree == n
    return squarefree, F(1, root * squarefree)


def clean(coefficients):
    return {key: value for key, value in coefficients.items() if value}


def check_regrouping():
    checks = 0
    for count in (1, 2, 4, 8, 12):
        for theta_prime in (F(5, 3), F(17, 5)):
            for kappa in (F(0), F(1, 2), F(7, 3)):
                def kernel(v):
                    return v ** 4 - kappa * v ** 2

                direct = defaultdict(F)
                for n in range(1, count + 1):
                    for m in range(1, count + 1):
                        radical, weight = reciprocal_sqrt(n * m)
                        ratio = tuple(x - y for x, y in zip(exponents(n), exponents(m)))
                        product = tuple(x + y for x, y in zip(exponents(n), exponents(m)))
                        direct[('ratio', ratio, radical)] += weight * kernel(
                            2 * theta_prime - log_symbol(n) - log_symbol(m))
                        direct[('product', product, radical)] += weight * kernel(
                            log_symbol(m) - log_symbol(n))

                grouped = defaultdict(F)
                for p in range(1, count + 1):
                    for q in range(1, count + 1):
                        if gcd(p, q) != 1:
                            continue
                        radical, weight = reciprocal_sqrt(p * q)
                        ratio = tuple(x - y for x, y in zip(exponents(p), exponents(q)))
                        coefficient = sum(
                            kernel(2 * theta_prime - log_symbol(p * q) - 2 * log_symbol(d)) / d
                            for d in range(1, count // max(p, q) + 1))
                        grouped[('ratio', ratio, radical)] += weight * coefficient
                for k in range(1, count * count + 1):
                    divisors = [n for n in range(1, count + 1)
                                if k % n == 0 and k // n <= count]
                    if not divisors:
                        continue
                    radical, weight = reciprocal_sqrt(k)
                    coefficient = sum(kernel(log_symbol(k // n) - log_symbol(n))
                                      for n in divisors)
                    grouped[('product', exponents(k), radical)] += weight * coefficient
                assert clean(direct) == clean(grouped), (count, theta_prime, kappa)
                checks += 1
    print(f"Product/ratio regrouping: {checks} exact formal phase-coefficient checks passed")


def multiply(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def check_limiting_jet():
    b, tau = F(1, 2), F(1, 3)
    denominator = (b * b + tau * tau, -2 * tau, F(1))
    coefficients = []
    for j in range(5):
        rhs = F(1) if j == 0 else F(0)
        rhs -= sum(denominator[k] * coefficients[j - k]
                   for k in range(1, min(2, j) + 1))
        coefficients.append(rhs / denominator[0])
    taylor_jet = [factorial(j) * c for j, c in enumerate(coefficients)]

    inverse = (b / denominator[0], -tau / denominator[0])
    power = inverse
    i_powers = ((F(1), F(0)), (F(0), F(1)), (F(-1), F(0)), (F(0), F(-1)))
    integral_jet = []
    for j in range(5):
        integral_jet.append(2 * factorial(j) * multiply(i_powers[j % 4], power)[0])
        power = multiply(power, inverse)
    assert taylor_jet == integral_jet
    u = taylor_jet
    q = u[1] ** 2 - u[0] * u[2]
    t = u[0] * u[4] - 4 * u[1] * u[3] + 3 * u[2] ** 2
    assert q == F(466560, 28561) > 0
    assert t == F(-1390722048, 4826809) < 0
    print(f"Independent rational jets agree: Q = {q}; T = {t}")


if __name__ == '__main__':
    check_regrouping()
    check_limiting_jet()
