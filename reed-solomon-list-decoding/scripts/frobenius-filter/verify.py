#!/usr/bin/env python3
"""Exact arithmetic checks for L007; no list-size enumeration is claimed."""

from fractions import Fraction
import json
from math import isqrt
from pathlib import Path


def ceil_fraction(value):
    return (value.numerator + value.denominator - 1) // value.denominator


rates = (2, 4, 8, 16)
primes = (3, 5, 7, 11, 13, 17, 19)
table = []
cutoff_checks = 0
zero_slack_checks = 0
critical_slack_checks = 0
negative_denominators = []

for s in rates:
    first_prime = next(p for p in primes if p > s)
    strict_bound = Fraction(s * (first_prime - 1), first_prime - s)
    table.append({
        "rate": f"1/{s}",
        "least_prime_for_constant_zero_slack_bound": first_prime,
        "uniform_list_upper_bound": ceil_fraction(strict_bound) - 1,
        "remaining_primes": [p for p in primes if p < s],
        "remaining_prime_slack_cutoff": f"1/sqrt({s}*p) - 1/{s}",
    })

    for exponent in range(4, 13):
        n = 2**exponent
        k = n // s
        for p in primes:
            h = (k - 1) // p
            assert h + 1 == (k + p - 1) // p
            cutoff = isqrt(n * h) + 1
            assert cutoff**2 > n * h
            assert (cutoff - 1)**2 <= n * h
            assert cutoff <= n
            cutoff_checks += 1

            denominator = k * k - n * h
            if p > s:
                assert denominator > 0
                ratio = Fraction(n * (k - h), denominator)
                constant = Fraction(s * (p - 1), p - s)
                assert ratio < constant
                assert ratio.numerator // ratio.denominator <= ceil_fraction(constant) - 1
                zero_slack_checks += 1

            if p < s:
                # At gamma_c, A = ceil(sqrt(n*k/p)); use integer arithmetic.
                agreement = isqrt((n * k) // p)
                if p * agreement**2 < n * k:
                    agreement += 1
                assert p * agreement**2 >= n * k
                assert p * (agreement - 1)**2 < n * k
                assert k <= agreement <= n
                critical_denominator = agreement**2 - n * h
                assert p * critical_denominator >= n
                assert Fraction(n * (agreement - h), critical_denominator) <= p * n
                critical_slack_checks += 1
                if n == 4096:
                    assert denominator < 0
                    negative_denominators.append({
                        "n": n, "rate": f"1/{s}", "p": p,
                        "zero_slack_denominator": denominator,
                    })

assert [row["uniform_list_upper_bound"] for row in table] == [3, 15, 26, 255]
example = {"p": 3, "q": 81, "n": 16, "k": 4, "h": 1}
assert (example["q"] - 1) % example["n"] == 0
assert 4**2 - 16 == 0
assert Fraction(16 * (5 - 1), 5**2 - 16) == Fraction(64, 9)
example.update({"denominator_at_A_4": 0, "list_upper_bound_at_A_5": 7})

result = {
    "scope": "Exact arithmetic only; the symbolic proof is in L007.",
    "n_values": [2**exponent for exponent in range(4, 13)],
    "tested_primes": list(primes),
    "rate_table": table,
    "cutoff_checks": cutoff_checks,
    "zero_slack_strict_bound_checks": zero_slack_checks,
    "critical_slack_rounding_checks": critical_slack_checks,
    "negative_denominator_examples": negative_denominators,
    "smooth_finite_example": example,
}
output = Path(__file__).with_name("results.json")
output.write_text(json.dumps(result, indent=2) + "\n")
print(f"Passed {cutoff_checks} cutoff, {zero_slack_checks} strict-bound, "
      f"and {critical_slack_checks} critical-slack checks.")
print("Results saved to scripts/frobenius-filter/results.json.")
