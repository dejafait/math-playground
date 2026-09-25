#!/usr/bin/env python3
"""Exact finite algebra checks for L349, not analytic or sampled-value tests."""

from fractions import Fraction as F

from check_endpoint_first_order import add, factors, multiply, scale


def monomial(t_degree, u_degree):
    return tuple(["t"] * t_degree + ["u"] * u_degree)


def main():
    # Here t = p^(-sigma) exp(-ia log p), u = exp(-iv log p).
    # Clearing the local denominator checks every retained coefficient
    # and the exact first omitted term, with t and u formal variables.
    for degree in range(1, 13):
        series = {(): F(1)}
        for k in range(1, degree + 1):
            series = add(series, {monomial(k, k): F(1),
                                  monomial(k, k - 1): F(-1)})
        cleared = multiply({(): F(1), ("t", "u"): F(-1)}, series)
        expected = {(): F(1), ("t",): F(-1),
                    monomial(degree + 1, degree + 1): F(-1),
                    monomial(degree + 1, degree): F(1)}
        assert cleared == expected, degree

    limit = 32
    fac = {n: factors(n) for n in range(1, limit + 1)}
    divisors = {n: [d for d in range(1, n + 1) if n % d == 0]
                for n in fac}
    mu = {n: 0 if any(e > 1 for e in f.values()) else (-1) ** len(f)
          for n, f in fac.items()}
    # Each log p is an independent formal variable; no floating-point logs.
    logs = {n: {(p,): F(e) for p, e in f.items()} for n, f in fac.items()}
    von_mangoldt = {
        n: {(next(iter(f)),): F(1)} if len(f) == 1 else {}
        for n, f in fac.items()
    }
    count = 0
    for m in fac:
        for n in fac:
            direct = {}
            constant = 0
            for j in divisors[m]:
                for k in divisors[n]:
                    multiplier = mu[m // j] * mu[n // k]
                    direct = add(direct, scale(add(logs[j], logs[k]), multiplier))
                    constant += multiplier
            expected = add(scale(von_mangoldt[m], int(n == 1)),
                           scale(von_mangoldt[n], int(m == 1)))
            assert direct == expected, (m, n)
            assert constant == int(m == 1 and n == 1), (m, n)
            count += 1

    print(f"OK: 12 exact local Euler identities; {count} formal linear "
          "divisor identities and constant cancellations.")
    print("This checks finite algebra only, not the uniform integral, "
          "infinite coefficient norms, or values at a_n.")


if __name__ == "__main__":
    main()
