"""Independent rational replay of C750m; analytic audit is canonical Section 7."""
from fractions import Fraction as Q
from pathlib import Path
import json


def exact(x):
    x = Q(x)
    return {"numerator": x.numerator, "denominator": x.denominator}


# Independent sieve and factorization, including every integer in the window.
composite = set()
primes = []
for n in range(2, 101):
    if n not in composite:
        primes.append(n)
        composite.update(range(n * n, 101, n))
active = {}
for n in range(2, 101):
    factors = []
    rest = n
    for p in primes:
        while rest % p == 0:
            factors.append(p)
            rest //= p
    if len(set(factors)) == 1:
        active[n] = factors[0]
claimed_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
claimed_powers = [4, 8, 16, 32, 64, 9, 27, 81, 25, 49]
subset = [p for p in primes if p >= 23]
term = Q(1)
taylor = term
for k in range(1, 5):
    term *= Q(7, 10 * k)
    taylor += term
e_upper = Q(8, 3) + Q(5, 96)
t_lower = 6 * Q(5, 2) ** 12
a_lower = len(subset) * Q(6, 10)
d_lower = len(subset) * Q(18, 50)
error_coefficient = 4 * (200 + 15) + 4 * Q(200, 4) + 402
witness_lower = d_lower - Q(21, 10) - error_coefficient / 100000
checks = {
    "all_primes": primes == claimed_primes,
    "all_prime_powers": sorted(active) == sorted(claimed_primes + claimed_powers),
    "35_terms": len(active) == 35,
    "17_term_lower_subset": len(subset) == 17 and min(subset) == 23 and max(subset) == 97,
    "e_upper": e_upper < Q(11, 4) < 3,
    "L_lower_and_upper": 3**4 < 101 < Q(8, 3)**5,
    "log23_lower": Q(11, 4)**3 < 23,
    "log4pi_below3": Q(8, 3)**3 > 16,
    "log3_below2": Q(8, 3)**2 > 3,
    "A_lower": a_lower == Q(51, 5),
    "d_lower": d_lower == Q(153, 25),
    "T_lower": t_lower > 100000,
    "log2_upper": taylor == Q(482921, 240000) and taylor > 2,
    "low_leakage_coefficient": Q(64, 9) / 2 == Q(32, 9),
    "low_leakage_below_one": Q(32, 9 * 3 * 2) < 1,
    "high_leakage_coefficient": Q(64, 9) / 3 == Q(64, 27),
    "high_leakage_below_one": Q(16, 27 * 3 * 2) < 1,
    "envelope_positive": a_lower + 2 - Q(21, 10) - Q(2, 25000) > 0,
    "complete_error_coefficient": error_coefficient == 1462,
    "strict_witness_threshold": witness_lower == Q(200269, 50000) and witness_lower > 4,
    "norm_budget_stop": 2 - witness_lower < -2,
}
certificate = {
    "scope": "Exact rational and finite-integer replay only. Section 7 of C750m independently audits all analytic claims; these booleans do not verify them.",
    "active_prime_powers": active,
    "subset": subset,
    "values": {"T_lower": exact(t_lower), "A_lower": exact(a_lower),
               "d_lower": exact(d_lower), "exp_point7_partial": exact(taylor),
               "error_coefficient": exact(error_coefficient),
               "witness_lower_strict": exact(witness_lower),
               "witness_margin_over4": exact(witness_lower - 4),
               "required_norm_upper_strict": 2,
               "resource_upper_strict": exact(2 - witness_lower)},
    "checks": checks,
    "failures": [key for key, ok in checks.items() if not ok],
}
path = Path(__file__).with_name("audit-arithmetic-1164.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Arithmetic audit: {sum(checks.values())}/{len(checks)} passed; failures={certificate['failures']}")
print(f"Actual witness >{witness_lower}; required norm <2; resource <{2-witness_lower}.")
print(f"Certificate: {path.relative_to(Path.cwd())}")
raise SystemExit(bool(certificate["failures"]))
