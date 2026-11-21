"""Exact scalar checks for L789; analytic domain arguments are in the lemma.

Run from riemann: python3 scripts/complex-moment-audit/tube-saddle-470.py
Only fractions and finite positive exponential sums are used.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def exp_lower(x, degree):
    term = total = F(1)
    for n in range(1, degree + 1):
        term *= x / n
        total += term
    return total


checks = []


def check(name, lhs, rhs, relation="<"):
    lhs, rhs = F(lhs), F(rhs)
    passed = lhs < rhs if relation == "<" else lhs > rhs
    checks.append(dict(name=name, lhs=str(lhs), relation=relation,
                       rhs=str(rhs), passed=passed))


def ceiling_decimal(x, places=8):
    scale = 10 ** places
    integer = -(-x.numerator * scale // x.denominator)
    return f"{integer // scale}.{integer % scale:0{places}d}"


pi_lower = F(223, 71)  # Classical Archimedean lower bound.
t = F(2, 5)
cos_lower = 1 - t*t/2 + t**4/24 - t**6/720
tubes = []
for x0, x_lower, required, unit in [
    (F(3, 10), F(33201, 10000), F(11, 10**12), F(1, 10**12)),
    (F(7, 20), F(40551, 10000), F(11, 10**15), F(1, 10**14)),
    (F(2, 5), F(49530, 10000), F(1, 10**15), F(1, 10**15)),
]:
    label = str(x0)
    check(f"exp(4*x0) lower {label}", exp_lower(4*x0, 20), x_lower, ">")
    a = 2*pi_lower*x_lower
    exponent = 3*pi_lower*x_lower*cos_lower
    m = exponent // 4
    delta = exponent - 4*m
    denominator = exp_lower(F(4), 16)**m * exp_lower(delta, 16)
    q_upper = 16 / denominator
    check(f"q admissible {label}", q_upper, 1)
    majorant = (a+3)/(a-3) * q_upper/(1-q_upper)
    check(f"tube majorant {label}", majorant, required)
    tubes.append(dict(x0=label, X_lower=str(x_lower), exponent_lower=str(exponent),
                      m=int(m), delta=str(delta), q_upper=str(q_upper),
                      majorant=str(majorant), required=str(required),
                      unit=str(unit), scaled_upper=ceiling_decimal(majorant/unit)))

check("e^4 > 50", exp_lower(F(4), 7), 50, ">")
check("e^3 > 10", exp_lower(F(3), 3), 10, ">")
check("K(1) upper versus k0", 648, 10**9)
check("5 log(k0)+1 coarse upper versus k0", 136, 10**9)
check("H0/B0 lower", 1-F(9, 2)/300-F(6, 300*297), F(21, 25), ">")
check("disk denominator lower", F(4, 5)-F(3, 300), F(7, 10), ">")
h1 = 5 + 24*F(5, 4)/(F(7, 10)**2 * 300**2)
h2 = 20 + (96*F(5, 4)/F(7, 10)**2 + 192*F(5, 4)**2/F(7, 10)**3)/300**2
check("Hprime/B0", h1, F(51, 10))
check("Hsecond/B0", h2, 22)
k2 = (F(102, 10)+F(21, 20)*22)/F(21, 25)
check("Ksecond/k", k2, 60)
rho = F(11, 10**15)
perturb = F(1, 40)*25*rho/(1-rho)
check("full map perturbation/k", perturb, F(7, 10**15))
for radius in [F(1, 20), F(3, 200)]:
    linear = 4*radius
    error = 30*radius**2 + F(1, 20)
    check(f"principal Rouche radius {radius}", error, linear)
    check(f"full Rouche radius {radius}", error+F(7, 10**15), linear)
    check(f"extended parameter disk Rouche radius {radius}",
          30*radius**2+F(51, 1000)+F(7, 10**15), linear)

summary = dict(
    all_passed=all(c["passed"] for c in checks), checks=len(checks),
    failures=[c["name"] for c in checks if not c["passed"]],
    tubes=[{key: row[key] for key in ["x0", "unit", "scaled_upper", "required"]} for row in tubes],
    Hprime_over_B0_upper=ceiling_decimal(h1), Hprime_required="5.1",
    Hsecond_over_B0_upper=ceiling_decimal(h2), Hsecond_required="22",
    Ksecond_over_k_bound=str(k2), Ksecond_required="60",
    perturbation_in_units_1e_minus_15=ceiling_decimal(perturb*10**15),
    perturbation_required_in_same_units="7",
    outer_full_error_over_k=str(F(1, 8)+F(7, 10**15)), outer_linear_lower="1/5",
    inner_full_error_over_k=str(F(227, 4000)+F(7, 10**15)), inner_linear_lower="3/50",
)
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(dict(summary=summary, tubes=tubes, checks=checks), indent=2)+"\n")
print(json.dumps(summary, indent=2))
print(f"Full exact certificate: {path.relative_to(Path.cwd())}")
assert summary["all_passed"], summary["failures"]
