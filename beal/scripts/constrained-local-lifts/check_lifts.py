#!/usr/bin/env python3
"""Exact bounded checks of L006; local points are not integer solutions."""

import json
from itertools import product
from math import gcd, isqrt


def valuation(value, prime):
    assert value != 0
    count = 0
    while value % prime == 0:
        value //= prime
        count += 1
    return count


def binary_root(delta, precision):
    root = 1
    assert delta % 8 == 1
    for k in range(2, precision):
        assert (root * root - delta) % (2 ** (k + 1)) == 0
        error = (root * root - delta) // (2 ** (k + 1))
        digit = (-error) % 2
        lifted = root + digit * 2**k
        assert (lifted - root) % (2**k) == 0
        assert (lifted * lifted - delta) % (2 ** (k + 2)) == 0
        root = lifted
    return root


def ternary_root(delta, precision):
    root = 1
    assert delta % 3 == 1
    for k in range(1, precision):
        modulus = 3**k
        assert (root * root - delta) % modulus == 0
        error = (root * root - delta) // modulus
        digit = (-error * pow(2 * root, -1, 3)) % 3
        lifted = root + digit * modulus
        assert (lifted - root) % modulus == 0
        assert (lifted * lifted - delta) % (3 * modulus) == 0
        root = lifted
    return root


def check_lifts():
    exponents = (19, 31, 37, 43, 61, 67, 73, 97)
    u_values = (1, 3, 5, 9, 13, 27, 39, 81)
    v_values = (1, 13, 37, 61, 169, 181)
    precision_2, precision_3 = 64, 40
    binary_modulus = 2 ** (precision_2 + 2)
    ternary_modulus = 3**precision_3
    equation_modulus = 2**precision_2 * ternary_modulus
    cases = divisible_u = 0
    for p, u, v in product(exponents, u_values, v_values):
        if gcd(u, v) != 1:
            continue
        assert p % 3 == 1 and u % 2 == 1 and v % 12 == 1
        coefficient = 3 ** (2 * p - 3)
        s = 3 ** (p - 1) * u**p
        c = 3 * u * v
        delta = 4 * v**p - coefficient * u ** (2 * p)
        root_2 = binary_root(delta, precision_2 + 1)
        root_3 = ternary_root(delta, precision_3)
        assert (root_2 * root_2 - delta) % binary_modulus == 0
        assert (root_3 * root_3 - delta) % ternary_modulus == 0
        crt_digit = (
            (root_3 - root_2) * pow(binary_modulus, -1, ternary_modulus)
        ) % ternary_modulus
        d = root_2 + binary_modulus * crt_digit
        assert (d * d - delta) % (binary_modulus * ternary_modulus) == 0
        assert (s + d) % 2 == 0 and (s - d) % 2 == 0
        a, b = (s + d) // 2, (s - d) // 2
        assert (a**3 + b**3 - c**p) % equation_modulus == 0
        assert valuation(a * b, 2) == 1 and c % 2 == 1
        assert valuation(s * s - d * d, 2) == 3
        assert a % 3 != 0 and b % 3 != 0 and d % 3 != 0
        assert valuation(c, 3) == 1 + valuation(u, 3)
        assert valuation(s, 3) == p - 1 + p * valuation(u, 3)
        assert valuation(a * a - a * b + b * b, 3) == 1
        cases += 1
        divisible_u += u % 3 == 0
    return {
        "exponents": list(exponents),
        "u_values": list(u_values),
        "v_values": list(v_values),
        "coprime_parameter_cases": cases,
        "cases_with_3_dividing_u": divisible_u,
        "equation_precision_at_2": precision_2,
        "equation_precision_at_3": precision_3,
        "combined_crt_cases": cases,
    }


def check_real_nonsquare_control():
    p, u, v = 19, 5, 181
    s = 3 ** (p - 1) * u**p
    delta = 4 * v**p - 3 ** (2 * p - 3) * u ** (2 * p)
    root = isqrt(delta)
    assert gcd(u, v) == 1 and u % 2 == 1 and v % 12 == 1
    assert all(v % divisor != 0 for divisor in range(2, isqrt(v) + 1))
    assert 0 < delta < s * s
    assert root * root < delta < (root + 1) ** 2
    assert delta == 13272700465307974015006493558304900267225409
    assert root == 3643171758963331393128
    return {
        "p": p,
        "u": u,
        "v": v,
        "s": s,
        "delta": delta,
        "floor_sqrt_delta": root,
        "strict_real_positivity_interval": True,
        "integer_square": False,
    }


if __name__ == "__main__":
    print(json.dumps({
        "lifts": check_lifts(),
        "real_nonsquare_control": check_real_nonsquare_control(),
        "result": "PASS",
        "scope": "Bounded checks of constrained local lifts; no Beal proof or counterexample.",
    }, indent=2))
