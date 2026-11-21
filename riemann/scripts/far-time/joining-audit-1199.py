"""Exact finite constants for C030j; the uniform proof is in the lemma."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


def rational(x):
    x = F(x)
    return {"numerator": x.numerator, "denominator": x.denominator}


def exp_partial(x, degree):
    return [F(x) ** k / factorial(k) for k in range(degree + 1)]


checks = []


def greater(name, actual, required, terms=None):
    actual, required = F(actual), F(required)
    row = {"name": name, "actual": rational(actual),
           "required_strict_lower_bound": rational(required),
           "margin": rational(actual - required), "passed": actual > required}
    if terms is not None:
        row["terms"] = [rational(t) for t in terms]
    checks.append(row)


e_lower_terms = exp_partial(F(1), 4)
greater("exp(10) > (sum_0^4 1/k!)^10 > 20000",
        sum(e_lower_terms) ** 10, 20000, e_lower_terms)
terms = exp_partial(F(7, 3), 8)
greater("exp(7/3) > partial_sum_8 > 10", sum(terms), 10, terms)
terms = exp_partial(F(7, 4), 4)
greater("exp(7/4) > partial_sum_4 > 243/50", sum(terms), F(243, 50), terms)
greater("exp(2) > partial_sum_2 > 4", F(1) + 2 + 2, 4)

greater("general: 1 - (9/1600 + 1/16000000) > 0",
        1 - (F(9, 1600) + F(1, 16000000)), 0)
greater("general: Delta >= 400000000-22500-1/4 > 0",
        F(400000000) - 22500 - F(1, 4), 0)
greater("general N=1: tau*T^2=100 > 4", 100, 4)

n, t, tau = 3, F(10000), F(1, 1000000)
d = F(22500 * n * n)
s = sum(F(1, (factorial(j - 1) * factorial(n - j)) ** 2)
        for j in range(1, n + 1))
delta = t*t - d - F(1, 4)
a = delta*tau
prefactor = F(4, 10000) * F(3, 10000) ** (2*n-2) * s * t ** (4*n)
greater("special: T > max(1000,150N)", t, max(1000, 150*n))
greater("special: Delta > 0", delta, 0)
greater("special: tau*T^2=100 > 4N=12", tau*t*t, 4*n)
greater("special: Delta*tau > 98+7/4", a, 98 + F(7, 4))
greater("near-time: 1/360 > special tau >= general tau", F(1, 360), tau)

identities = {
    "S_3_equals_3/2": s == F(3, 2),
    "D_3_equals_202500": d == 202500,
    "special_exponent_equals_399189999/4000000": a == F(399189999, 4000000),
    "special_prefactor_equals_(243/50)*10^30": prefactor == F(243, 50)*10**30,
    "special_target_prefactor/((243/50)*10^42)_equals_10^-12":
        prefactor / (F(243, 50)*10**42) == F(1, 10**12),
    "general_log_bound_coefficients": (2+40-99 == -57 and 6-99 == -93),
}
passed = all(c["passed"] for c in checks) and all(identities.values())
report = {
    "purpose": "Finite rational checks only; uniform N proof and imported analytic inputs are not machine verified.",
    "checks": checks, "identities": identities,
    "special": {"N": n, "T": rational(t), "tau": rational(tau),
                "D": rational(d), "S": rational(s), "Delta": rational(delta),
                "exponent": rational(a), "prefactor": rational(prefactor),
                "strict_rho_upper_bound": rational(F(1, 10**12))},
    "passed": passed,
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(report, indent=2) + "\n")
for c in checks:
    v, b = c["actual"], c["required_strict_lower_bound"]
    print(f'{c["name"]}: {"PASS" if c["passed"] else "FAIL"}; actual={v["numerator"]}/{v["denominator"]}; required>{b["numerator"]}/{b["denominator"]}')
print(f'Identities: {sum(identities.values())}/{len(identities)}; failures={[k for k,v in identities.items() if not v]}')
print(f'Certificate: {out}; passed={passed}; special rho required<1, proved<1/10^12 by the lemma argument')
raise SystemExit(0 if passed else 1)
