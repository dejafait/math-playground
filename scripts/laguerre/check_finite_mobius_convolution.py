#!/usr/bin/env python3
"""Exact finite algebra checks for L328; no numerical zeta or sign certificate."""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from math import ceil, floor, gcd, prod


def prime_factors(n):
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            exponent = 0
            while n % d == 0:
                n //= d
                exponent += 1
            result.append((d, exponent))
        d += 1
    if n > 1:
        result.append((n, 1))
    return result


@lru_cache(None)
def mu(n):
    factors = prime_factors(n)
    return 0 if any(e > 1 for _, e in factors) else (-1) ** len(factors)


@lru_cache(None)
def omega(n):
    # An exactly additive substitute for log, used for identities only.
    return sum((e * F(p + 1, p) for p, e in prime_factors(n)), F(0))


def check_convolution():
    coefficient_checks = 0
    stable_checks = 0
    for R, N in ((2, 9), (3, 12), (4, 18), (5, 24), (6, 30)):
        c = [0] * (R * N + 1)
        dual = defaultdict(F)
        for m in range(1, R + 1):
            for j in range(1, N + 1):
                c[j * m] += mu(m)
                # Multiply the coefficient at reduced b/d by sqrt(bd).
                dual[F(j, m)] += F(mu(m), gcd(j, m))
        for ell in range(1, R * N + 1):
            expected = sum(mu(m) for m in range(1, R + 1)
                           if ell % m == 0 and ell // m <= N)
            assert c[ell] == expected
        assert c[1] == 1 and all(c[ell] == 0 for ell in range(2, R + 1))

        def H(b, d):
            return sum((F(mu(k * d), k)
                        for k in range(1, min(R // d, N // b) + 1)), F(0))

        for b in range(1, N + 1):
            for d in range(1, R + 1):
                if gcd(b, d) == 1:
                    assert dual[F(b, d)] == H(b, d)

        rough = [ell for ell in range(R + 1, N + 1)
                 if all(gcd(ell, m) == 1 for m in range(1, R + 1))][:5]
        assert rough
        L = F(7, 2)
        raw_a = {ell: defaultdict(F) for ell in rough}
        raw_d = {ell: defaultdict(F) for ell in rough}
        # Independently expand all four original indices before grouping.
        # At ratio ell the product amplitude, times sqrt(ell), is rational.
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                for m in range(1, R + 1):
                    for l in range(1, R + 1):
                        signed = mu(m) * mu(l)
                        ratio_a = F(k * l, j * m)
                        if ratio_a in raw_a:
                            frequency = 2 * L - omega(j * k * m * l)
                            raw_a[ratio_a][frequency] += F(signed, j * m)
                        ratio_d = F(j * l, m * k)
                        if ratio_d in raw_d:
                            frequency = -2 * L + omega(j * k) - omega(m * l)
                            raw_d[ratio_d][frequency] += F(signed, m * k)

        for ell in rough:
            for t in range(1, N // ell + 1):
                assert c[ell * t] == c[t]
                stable_checks += 1
            for b in range(1, N // ell + 1):
                for d in range(1, R + 1):
                    if gcd(b, d) == 1 and ell * b * R <= N * d:
                        assert H(ell * b, d) == H(b, d)
                        stable_checks += 1
            for p in (2, 4, 8):
                r = F(4 * p, 3)
                normalization = 2 * (2 * r) ** p
                left_a = sum((coefficient * frequency ** p
                              for frequency, coefficient in raw_a[ell].items()), F(0))
                left_d = sum((coefficient * frequency ** p
                              for frequency, coefficient in raw_d[ell].items()), F(0))
                right_a = sum((F(c[t] * c[ell * t], t)
                               * (2 * L - omega(ell) - 2 * omega(t)) ** p
                               for t in range(1, R * N // ell + 1)), F(0))
                right_d = sum((H(ell * b, d) * H(b, d) / (b * d)
                               * (omega(ell) + 2 * (omega(b) - omega(d)) - 2 * L) ** p
                               for b in range(1, N // ell + 1)
                               for d in range(1, R + 1) if gcd(b, d) == 1), F(0))
                assert left_a / normalization == right_a / normalization
                assert left_d / normalization == right_d / normalization
                coefficient_checks += 2
    print(f"Direct/dual grouped even coefficients: {coefficient_checks} exact checks passed")
    print(f"Stable rough-ratio divisor identities: {stable_checks} exact checks passed")


def check_rough_counts():
    checks = 0
    for R in range(2, 16):
        primes = [p for p in range(2, R + 1) if prime_factors(p) == [(p, 1)]]
        P = prod(primes)
        density = prod(F(p - 1, p) for p in primes)
        assert density >= F(1, R)
        assert len(primes) <= F(R, 2) + 1
        divisors = [(1, 1)]
        for p in primes:
            divisors += [(d * p, -sign) for d, sign in divisors]
        for Y in (F(1), F(17, 3), F(80, 3), F(255, 2)):
            actual = sum(gcd(j, P) == 1 for j in range(ceil(Y), floor(2 * Y) + 1))
            exact = sum(sign * (floor(2 * Y / d) - ceil(Y / d) + 1)
                        for d, sign in divisors)
            assert actual == exact
            assert abs(actual - Y * density) <= 2 ** len(primes)
            checks += 1
    log_four_thirds_upper = F(1, 3) - F(1, 18) + F(1, 81)
    kappa_lower = F(1, 4) - F(3, 4) * log_four_thirds_upper
    assert kappa_lower == F(7, 216) and kappa_lower > F(1, 32)
    gamma_lower = F(3, 4) * 2 * (F(1, 3) + F(1, 81)) - F(1, 2)
    assert gamma_lower == F(1, 54) and gamma_lower > F(1, 200)
    print(f"Finite rough counts: {checks} exact checks; exponent comparisons passed")


if __name__ == "__main__":
    check_convolution()
    check_rough_counts()
