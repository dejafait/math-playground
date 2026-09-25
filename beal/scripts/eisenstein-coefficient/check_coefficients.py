#!/usr/bin/env python3
"""Exact bounded algebra checks for L007; these are not Beal solutions."""

import json
from math import comb, gcd


def multiply(left, right):
    """Pairs are a+b*zeta, with zeta**2=zeta-1."""
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c + b * d


def power(value, exponent):
    result = (1, 0)
    for _ in range(exponent):
        result = multiply(result, value)
    return result


def recurrence(r, v, n, first, second):
    if n == 0:
        return first
    for _ in range(1, n):
        first, second = second, r * second - v * first
    return second


def valuation(value, prime):
    assert value != 0
    value = abs(value)
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def check_case(p, r, t):
    assert r % 2 and t % 2 and gcd(r, t) == 1 and r % 3
    v = (r * r + 3 * t * t) // 4
    assert r * r + 3 * t * t == 4 * v
    assert gcd(r, v) == gcd(t, v) == 1
    coefficient = recurrence(r, v, p, 0, 1)
    trace = recurrence(r, v, p, 2, r)
    a, b = power(((r - t) // 2, t), p)
    assert b == t * coefficient and 2 * a + b == trace
    assert trace * trace + 3 * b * b == 4 * v**p
    numerator = sum(
        comb(p, 2 * j + 1) * r ** (p - 2 * j - 1) * (-3 * t * t) ** j
        for j in range((p - 1) // 2 + 1)
    )
    assert numerator == 2 ** (p - 1) * coefficient
    assert coefficient % 3 and coefficient % 2 and trace % 2
    assert gcd(coefficient, v) == 1
    assert valuation(b, 3) == valuation(t, 3)
    assert gcd(abs(t), abs(coefficient)) == (p if t % p == 0 else 1)
    if t % p == 0:
        assert valuation(coefficient, p) == 1
        assert valuation(b, p) == valuation(t, p) + 1
    else:
        assert coefficient % p
    return v, coefficient, trace


def check_units():
    units = []
    for n in range(6):
        element = power((0, 1), n)
        a, b = element
        assert a * a + a * b + b * b == 1
        units.append(element)
    assert len(set(units)) == 6 and power((0, 1), 6) == (1, 0)
    for p in PRIMES:
        assert {power(unit, p) for unit in units} == set(units)


PRIMES = (5, 7, 11, 13, 19, 31)


def bounded_cases():
    total = at_p = negative_t = constrained_norm = high_3 = 0
    for p in PRIMES:
        t_values = set(range(1, 40, 2))
        t_values.update((p, p * p, 3 * p, 3 ** (p - 2),
                         3 ** (2 * p - 2), 3 ** (p - 2) * p ** (p - 1)))
        for r in range(-25, 26, 2):
            for absolute_t in sorted(t_values):
                for t in (absolute_t, -absolute_t):
                    if r % 3 == 0 or gcd(r, t) != 1:
                        continue
                    v, _, _ = check_case(p, r, t)
                    total += 1
                    at_p += t % p == 0
                    negative_t += t < 0
                    constrained_norm += v % 12 == 1
                    high_3 += valuation(t, 3) >= p - 2
    return {
        "primes": list(PRIMES),
        "r_values": list(range(-25, 26, 2)),
        "absolute_t_rule": "odd 1..39, p, p^2, 3p, 3^(p-2), 3^(2p-2), 3^(p-2)*p^(p-1)",
        "coprime_cases": total,
        "cases_with_p_dividing_t": at_p,
        "negative_t_cases": negative_t,
        "norm_congruent_to_1_modulo_12": constrained_norm,
        "cases_with_3_valuation_at_least_p_minus_2": high_3,
    }


def controls():
    v, coefficient, trace = check_case(5, 5, 1)
    assert (v, coefficient, trace) == (7, 149, -25)
    s = 3 * coefficient
    a, b = (s + trace) // 2, (s - trace) // 2
    assert (a, b) == (211, 236)
    assert gcd(a, b) == 1 and a * a - a * b + b * b == 3 * 7**5
    assert coefficient % (3**3) != 0
    v2, coefficient2, trace2 = check_case(5, 1, 5)
    assert (v2, coefficient2, trace2) == (19, 305, 1711)
    assert valuation(coefficient2, 5) == 1
    return {
        "isolated_factor": {"p": 5, "r": 5, "t": 1, "v": v,
                            "U_p": coefficient, "T_p": trace, "a": a, "b": b,
                            "coefficient_condition_satisfied": False},
        "exceptional_common_factor": {"p": 5, "r": 1, "t": 5, "v": v2,
                                      "U_p": coefficient2, "T_p": trace2},
    }


if __name__ == "__main__":
    check_units()
    print(json.dumps({
        "algebra_checks": bounded_cases(),
        "controls": controls(),
        "unit_power_maps_checked": list(PRIMES),
        "result": "PASS",
        "scope": "Exact bounded checks of identities and valuations; no full-system solution or exclusion.",
    }, indent=2))
