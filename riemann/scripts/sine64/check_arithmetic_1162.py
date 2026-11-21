"""Exact arithmetic checks for C750m; not an analytic proof audit."""
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import json


def record(q):
    q = F(q)
    return {"numerator": q.numerator, "denominator": q.denominator}


prime_powers = {}
for p in range(2, 101):
    if all(p % d for d in range(2, isqrt(p) + 1)):
        n = p
        while n < 101:
            prime_powers[n] = p
            n *= p

claimed = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
           43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
           4, 8, 16, 32, 64, 9, 27, 81, 25, 49]
subset = [23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
          73, 79, 83, 89, 97]
taylor = sum(F(7, 10)**k / factorial(k) for k in range(5))
e_upper = F(8, 3) + F(1, 24) / (1-F(1, 5))
t_lower = 6 * F(5, 2)**12
error_coefficient = (215 + 50) * 4 + 402
final_lower = F(153, 25) - F(21, 10) - F(error_coefficient, 100000)
checks = {
    "all_35_prime_powers": len(claimed) == 35 and sorted(claimed) == sorted(prime_powers),
    "17_prime_subset": len(subset) == 17 and all(prime_powers[p] == p for p in subset),
    "e_upper": e_upper == F(87, 32) and e_upper < F(11, 4),
    "L_upper": F(8, 3)**5 > 101,
    "log23_lower": F(11, 4)**3 < 23,
    "exp_point7": taylor == F(482921, 240000) and taylor > 2,
    "T_lower": t_lower > 100000,
    "error_coefficient": error_coefficient == 1462,
    "witness_lower": final_lower == F(200269, 50000) and final_lower > 4,
}
certificate = {
    "scope": "Exact elementary arithmetic only; analytic inequalities and domain/kernel proof require separate audit.",
    "prime_powers": prime_powers,
    "prime_subset": subset,
    "values": {
        "e_upper": record(e_upper), "exp_point7_partial_sum": record(taylor),
        "T_lower": record(t_lower), "error_coefficient": error_coefficient,
        "witness_lower": record(final_lower), "required_delta_upper_strict": 2,
    },
    "checks": checks,
    "failures": [name for name, ok in checks.items() if not ok],
}
path = Path(__file__).with_name("arithmetic-1162.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Exact arithmetic: {sum(checks.values())}/{len(checks)} checks passed.")
print(f"Witness bound: >{final_lower}; required delta <2; resource <-2.")
print(f"Failures: {certificate['failures']}")
print(f"Certificate: {path.relative_to(Path.cwd())}")
raise SystemExit(bool(certificate["failures"]))
