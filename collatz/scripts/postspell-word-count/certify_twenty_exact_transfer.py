#!/usr/bin/env python3
"""Certify L049's scalar obstruction; no heights or cycle are constructed."""
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

checks = []


def check(name, actual, relation, required):
    actual, required = F(actual), F(required)
    passed = {"<": actual < required, ">": actual > required,
              "=": actual == required}[relation]
    checks.append({"name": name, "actual": str(actual),
                   "relation": relation, "required": str(required),
                   "passed": passed})


def log_enclosure(t, m=12):
    x = (t - 1) / (t + 1)
    lower = 2 * sum((x**(2*k+1) / (2*k+1) for k in range(m)), F(0))
    remainder = 2*x**(2*m+1) / ((2*m+1)*(1-x*x))
    return {"argument": str(t), "x": str(x), "terms": m,
            "lower": str(lower), "remainder_upper": str(remainder),
            "upper": str(lower + remainder)}


def sums(q):
    S = sum((q**j for j in range(20)), F(0))
    U = sum((sum((q**k for k in range(j)), F(0))
             for j in range(20)), F(0))
    # Independent responses to unit initial height and unit additive forcing.
    homogeneous, additive = F(1), F(0)
    sum_h, sum_a = homogeneous, additive
    for _ in range(19):
        homogeneous, additive = q*homogeneous, q*additive+1
        sum_h += homogeneous
        sum_a += additive
    check(f"twenty homogeneous occurrences at {q}", S, "=", sum_h)
    check(f"nineteen additive transfers at {q}", U, "=", sum_a)
    check(f"additive geometric identity at {q}", U, "=", (S-20)/(q-1))
    return S, U


logs = {"log2": log_enclosure(F(2)), "log3": log_enclosure(F(3)),
        "cJ": log_enclosure(F(11, 4))}
check("delta strict lower bound via integer powers", 3**12, ">", 2**19)
check("log2 strict lower bound", F(logs["log2"]["lower"]), ">", F(6931, 10000))
check("log3 strict upper bound", F(logs["log3"]["upper"]), "<", F(10987, 10000))
check("cJ strict lower bound", F(logs["cJ"]["lower"]), ">", 1)
check("cJ strict upper bound", F(logs["cJ"]["upper"]), "<", F(41, 40))
delta_lo, delta_hi = F(19, 12), F(793, 500)
check("delta strict upper bound", F(10987, 6931), "<", delta_hi)
q_lo, q_hi = F(47, 25), F(189, 100)
b_lo, b_hi = F(19, 64), F(31, 100)
check("transfer coefficient strict lower enclosure", 3*delta_lo**2/4, ">", q_lo)
check("transfer coefficient strict upper enclosure", 3*delta_hi**2/4, "<", q_hi)
check("transfer additive lower endpoint", delta_lo*(3*delta_lo-4)/4, "=", b_lo)
check("transfer additive strict upper enclosure", delta_hi*(3*delta_hi-4)*F(41, 40)/4, "<", b_hi)
S_lo, U_lo = sums(q_lo)
S_hi, U_hi = sums(q_hi)

# e < sum_{k=0}^4 1/k! + (1/5!)/(1-1/6), since every later ratio <=1/6.
e_upper = sum((F(1, factorial(k)) for k in range(5)), F(0)) + F(1, 120)/(1-F(1, 6))
e_lower = sum((F(1, factorial(k)) for k in range(6)), F(0))
check("e upper enclosure evaluation", e_upper, "=", F(1631, 600))
check("e strict upper bound", e_upper, "<", F(11, 4))
check("log20 strict lower guard", e_upper**2, "<", 20)
check("log20 strict upper guard", e_lower**3, ">", 20)

N, C, M = 370000000, 338460000, 225640000
check("primitive count ray start", F(3, 2)*M, "=", C)
check("scalar length above required ray", N, ">", C)
check("scalar length above stronger 8M/5 guard", N, ">", F(8, 5)*M)
check("logN strict lower guard", F(11, 4)**19, "<", N)
check("logN strict upper guard", e_lower**20, ">", N)
constant = F(24, 5)*20 + F(69*20, 1034)
rhs_lo = F(399, 5)*S_lo*19 + 6*(8+2)*S_lo + 6*b_lo*U_lo + constant
rhs_hi = F(399, 5)*S_hi*20 + 6*(8+3)*S_hi + 6*b_hi*U_hi + constant
check("scalar RHS interval nonempty", rhs_lo, "<", rhs_hi)
check("certified surviving scalar length", rhs_lo, ">", N)
check("reported strict RHS lower bound", rhs_lo, ">", 545558861)
check("reported strict RHS upper bound", rhs_hi, "<", 632443324)

failures = [record for record in checks if not record["passed"]]
certificate = {
    "lemma": "L049", "occurrences": 20, "transfers": 19,
    "scope": "Exact twenty-word necessary scalar inequality only; no simultaneous height, parameter, parity, primitive count or cycle realization.",
    "log_enclosures": logs,
    "delta_lower": str(delta_lo), "delta_upper": str(delta_hi),
    "q_lower": str(q_lo), "q_upper": str(q_hi),
    "b_lower": str(b_lo), "b_upper": str(b_hi),
    "S_lower": str(S_lo), "U_lower": str(U_lo),
    "S_upper": str(S_hi), "U_upper": str(U_hi),
    "e_lower": str(e_lower), "e_upper": str(e_upper),
    "log20_bounds": [2, 3], "logN_bounds": [19, 20],
    "N": N, "C": C, "M": M, "constant": str(constant),
    "rhs_strict_lower": str(rhs_lo), "rhs_strict_upper": str(rhs_hi),
    "survival_margin_strict_lower": str(rhs_lo-N),
    "checks": checks, "failures": failures}
path = Path(__file__).with_name("twenty-exact-transfer-certificate.json")
path.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"checks={len(checks)}, failures={len(failures)}")
print(f"occurrences=20, transfers=19; q in ({q_lo}, {q_hi}), b in ({b_lo}, {b_hi})")
print(f"scalar N={N}; required N>={C}; stronger 8M/5={F(8, 5)*M}")
print(f"RHS > {rhs_lo.numerator//rhs_lo.denominator}; RHS < {-(-rhs_hi.numerator//rhs_hi.denominator)}")
print(f"survival margin > {(rhs_lo-N).numerator//(rhs_lo-N).denominator}; no actual feasibility inferred")
print(f"certificate: {path.relative_to(Path.cwd())}")
if failures:
    print("failed checks: "+", ".join(record["name"] for record in failures))
    raise SystemExit(1)
