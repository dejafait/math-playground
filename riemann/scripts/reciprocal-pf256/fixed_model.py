#!/usr/bin/env python3
"""Exact scalar checks for L561; does not certify global PF256."""

from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


def rational(value):
    value = F(value)
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def main():
    A, b, m = F(2**20), F(1, 4), 270
    radius2 = A*A + b*b
    q2 = -2*(A*A-b*b)/radius2**2
    q4 = 1/radius2**2
    q = 1+q2*A*A+q4*A**4
    dq = 2*q2*A+4*q4*A**3
    ddq = 2*q2+12*q4*A*A
    real_curvature = m*(1/(A-1)**2+1/(A+1)**2)
    root_curvature = (real_curvature - 2/b**2
                      + 2*(4*A*A-b*b)/(4*A*A+b*b)**2)
    jet_curvature = real_curvature+(dq*dq-q*ddq)/(q*q)
    sign_upper = -32+F(2701, 2)/(A*A)

    epsilon = b*b/(A*A)
    weighted_base_mass = A*(2*A+1)/(2*(A+1)**2)
    error_bound = radius2*b*b*(2*A-1)/(2*A*(A-1)**4)
    density_ratio_lower = (1+epsilon)*weighted_base_mass-error_bound
    error_simplified = 32*b*b/(A*A)
    elementary_lower = F(64, 81)-F(1, 32)

    q_at_one = 1+q2+q4
    tail_coefficient = 1/(2**m*factorial(m-1)*q_at_one)
    checks = []

    def check(name, actual, relation, required, passed):
        checks.append({"name": name, "actual": rational(actual),
                       "relation": relation, "required": rational(required),
                       "passed": bool(passed)})

    check("q(A) nonzero and positive", q, ">", 0, q > 0)
    check("root sum equals independent quartic jet", root_curvature-jet_curvature,
          "=", 0, root_curvature == jet_curvature)
    check("root curvature upper bound", root_curvature, "<", sign_upper,
          root_curvature < sign_upper)
    check("upper bound below -31", sign_upper, "<", -31, sign_upper < -31)
    check("weighted error bound simplification", error_bound, "<=", error_simplified,
          error_bound <= error_simplified)
    check("weighted base mass lower bound", weighted_base_mass, ">=", F(64, 81),
          weighted_base_mass >= F(64, 81))
    check("simplified error at most 1/32", error_simplified, "<=", F(1, 32),
          error_simplified <= F(1, 32))
    check("elementary density ratio exceeds 1/2", elementary_lower, ">", F(1, 2),
          elementary_lower > F(1, 2))
    check("exact density ratio exceeds 1/2", density_ratio_lower, ">", F(1, 2),
          density_ratio_lower > F(1, 2))
    check("Q(1) positive", q_at_one, ">", 0, q_at_one > 0)
    check("positive slow-pole leading coefficient", tail_coefficient, ">", 0,
          tail_coefficient > 0)
    check("Fourier regularity includes required order", 542, ">=", 510, 542 >= 510)
    check("smallest factor in (269)_255", 269-254, ">", 0, 269-254 > 0)

    certificate = {
        "status": "PARTIAL_MODEL_ONLY",
        "inputs": {"A": rational(A), "b": rational(b), "real_pole_multiplicity": m},
        "first_sign": {
            "normalized_D1": rational(root_curvature),
            "independent_quartic_jet_value": rational(jet_curvature),
            "required": "normalized D1 < 0; proved stronger normalized D1 < -31",
            "quartic_at_A": rational(q),
            "quartic_prime_at_A": rational(dq),
            "quartic_second_at_A": rational(ddq),
        },
        "density": {
            "weighted_base_mass": rational(weighted_base_mass),
            "weighted_error_upper": rational(error_bound),
            "ratio_lower": rational(density_ratio_lower),
            "required": "p_*(x)/ell^{*270}(x) > 1/2 for every real x",
            "analytic_justification": "lemmas/L561-fixed-high-rank-reciprocal-density-partial-certificate.md",
        },
        "determinants": {
            "origin": "Analytic positive moment-matrix proof for 1<=k<=256; not numerical sampling.",
            "tail": {
                "R_leading_coefficient": rational(tail_coefficient),
                "Hk_leading_formula": "exp(-k*x)*alpha^k*prod_{j=0}^{k-1}(j!*(269)_j)*x^(k*(270-k))",
                "range": "1<=k<=256",
                "effective_cutoff": None,
            },
            "global_signs": "UNRESOLVED: the intervening real range has no certificate.",
            "strict_PF256": "NOT ESTABLISHED; Sra C.6 not invoked.",
        },
        "checks": checks,
        "failures": [c["name"] for c in checks if not c["passed"]],
    }
    path = Path(__file__).with_name("fixed-model-partial-certificate.json")
    path.write_text(json.dumps(certificate, indent=2)+"\n", encoding="utf-8")
    print(f"Scalar checks: {len(checks)}; failures: {certificate['failures']}")
    print(f"Normalized D1: {float(root_curvature):.12g}; required < 0; exact bound < -31")
    print(f"Density ratio lower: {float(density_ratio_lower):.12g}; required > 0.5")
    print("Global H_k / strict PF256: UNRESOLVED; origin and existential tails only")
    print(f"Full certificate: {path}")
    if certificate["failures"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
