#!/usr/bin/env python3
"""Exact finite arithmetic supporting C030i; no zero sampling."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json


def value(q):
    q = Q(q)
    return {"numerator": q.numerator, "denominator": q.denominator}


checks = []


def check(name, actual, required):
    actual, required = Q(actual), Q(required)
    checks.append({"name": name, "actual": value(actual),
                   "required_strict_lower_bound": value(required),
                   "difference": value(actual - required),
                   "passed": actual > required})


z = Q(9, 11)
log_terms = [2 * z ** (2 * k + 1) / (2 * k + 1) for k in range(20)]
exp_terms = [Q(46, 25) ** k / factorial(k) for k in range(9)]
check("positive finite lower sum for log(10)", sum(log_terms), Q(23, 10))
check("positive finite lower sum for exp(46/25)", sum(exp_terms), Q(44, 7))
check("25/pi lower bound from pi<22/7", Q(175, 22), Q("7.95"))
check("e lower sum implies e>5/2", sum(Q(1, factorial(k)) for k in range(4)), Q(5, 2))
alpha = Q("0.1038") + Q(2, 5) * Q("0.2573")
increment = (Q("7.95") - 2 * alpha) * Q("4.6") - Q("7.95") * Q("1.84") - alpha - 2 * Q("9.3675")
check("HSW uniform interval increment lower bound", increment, 1)
count_margin = (Q("0.58") - Q("0.3611")) * 1000 + Q("3.463") - Q("10.3675")
check("printed quadratic envelope minus HSW envelope at 1000", count_margin, 0)
quadratic_margin = Q(5, 6) * 1000 ** 2 - Q("0.58") * 1000 - Q("3.463")
check("r^2 minus printed envelope at 1000", quadratic_margin, 0)
check("derivative of last difference at 1000", Q(5, 3) * 1000 - Q("0.58"), 0)
check("Rosser-source increment at log(r)>4", Q(29, 5) * 4 - Q(89, 5), 1)

certificate = {
    "purpose": "Exact finite arithmetic only. Uniform calculus, zero-count imports, endpoint and node arguments are in lemmas/C030i-actual-zero-separated-nodes-and-count-audited.md.",
    "log_lower_terms": [value(q) for q in log_terms],
    "exp_lower_terms": [value(q) for q in exp_terms],
    "alpha": value(alpha),
    "checks": checks,
    "failures": [c["name"] for c in checks if not c["passed"]],
    "passed": all(c["passed"] for c in checks),
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(certificate, indent=2) + "\n")
for c in checks:
    a, b = c["actual"], c["required_strict_lower_bound"]
    print(f'{c["name"]}: actual={a["numerator"]}/{a["denominator"]}, required>{b["numerator"]}/{b["denominator"]}, passed={c["passed"]}')
print(f'failures={certificate["failures"]}; certificate={out.relative_to(Path.cwd())}')
raise SystemExit(0 if certificate["passed"] else 1)
