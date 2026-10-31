#!/usr/bin/env python3
"""Fixed L510 replay via integer polynomials; no grid or generator import.

The symmetric numerator is derived in y=x^2, with integer-scaled A,B.
Full evidence goes to l510-independent-audit.json. Range inequalities and
budget implications are justified in canonical L510, not by sampling.
"""
import json
from fractions import Fraction as F
from pathlib import Path


def plus(*terms):
    result = {}
    for term in terms:
        for degree, coefficient in term.items():
            result[degree] = result.get(degree, 0) + coefficient
    return {d: c for d, c in result.items() if c}


def times(*terms):
    result = {0: 1}
    for term in terms:
        new = {}
        for i, a in result.items():
            for j, b in term.items():
                new[i+j] = new.get(i+j, 0) + a*b
        result = {d: c for d, c in new.items() if c}
    return result


def coeffs(term, degree):
    return [term.get(d, 0) for d in range(degree+1)]


def main():
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)

    # Aint=U-352x, Bint=U+352x, Mint=256y-441.
    # C=Aint*Bint. Avoid the generator's six-factor expansion in x.
    U = {0: 377, 1: 256}
    C = plus(times(U, U), {1: -(352**2)})
    M = {0: -441, 1: 256}
    paired = plus(times({0: 2}, U, C),
                  times({0: -2048}, U, U), times({0: 1024}, C))
    Q = plus(times(paired, M, M),
             times({0: 441, 1: 256}, C, C))
    expected = [1445312501451, -16326866594048, 61357440761856,
                -566298148864, -2203318222848, 3298534883328]
    actual = coeffs(Q, 5)
    check("C_identity", coeffs(C, 2) == [142129, 69120, 65536])
    check("Q_degree_five", max(Q) == 5)
    for degree, (got, required) in enumerate(zip(actual, expected)):
        check(f"Q_coefficient_{degree}", got == required)
    check("scaling_256_power_5_equals_twice_549755813888",
          256**5 == 2*549755813888)

    old = json.loads(Path(__file__).with_name(
        "finite-grid-separation-certificate.json").read_text())["separation"]
    check("selected_parameters", (old["h"], old["r"]) == ("11/16", "21/16"))
    check("saved_Q_all_coefficients", list(map(F, old["polynomial"]["Q_y_ascending"])) == actual)
    denominator_y = times(C, C, M, M)
    denominator_x = [F(denominator_y.get(d//2, 0), 256**6) if d % 2 == 0
                     else F(0) for d in range(13)]
    numerator_x = [F(Q.get(d//2, 0), 549755813888) if d % 2 == 0
                   else F(0) for d in range(11)]
    check("saved_denominator_all_coefficients", denominator_x ==
          list(map(F, old["polynomial"]["denominator_x_ascending"])))
    check("saved_numerator_all_coefficients", numerator_x ==
          list(map(F, old["polynomial"]["numerator_x_ascending"])))
    check("saved_scale", F(old["polynomial"]["scale"]) == F(1, 549755813888))

    S = 50000000000000
    c0, c1, c2, c3, c4, c5 = actual
    residual = 4*S*c0-c1*c1
    q = {0: c0, 1: c1, 2: S}
    R = {0: c2-S, 1: c3, 2: c4, 3: c5}
    check("Q_split_identity", Q == plus(q, times({2: 1}, R)))
    check("square_identity", times({0: 4*S}, q) ==
          plus(times({0: c1, 1: 2*S}, {0: c1, 1: 2*S}), {0: residual}))
    check("square_remainder_exact", residual == 22495927510359459970973696)
    check("square_remainder_positive", S > 0 and residual > 0)
    low = c2-S+c3+c4
    high = c3+c4+c5
    # R-low=(-c3)(1-y)+(-c4)(1-y^2)+c5*y^3 on [0,1].
    low_decomposition = plus({0: low}, times({0: -c3}, {0: 1, 1: -1}),
                             times({0: -c4}, {0: 1, 2: -1}), {3: c5})
    check("low_range_identity", R == low_decomposition)
    check("low_range_nonnegative_multipliers", -c3 >= 0 and -c4 >= 0 and c5 >= 0)
    check("low_bound_exact_and_positive", low == 8587824390144 and low > 0)
    # R=R0+high*y^3+(-c3)(y^3-y)+(-c4)(y^3-y^2) on [1,infinity).
    high_decomposition = plus({0: c2-S, 3: high},
                              times({0: -c3}, {1: -1, 3: 1}),
                              times({0: -c4}, {2: -1, 3: 1}))
    check("high_range_identity", R == high_decomposition)
    check("high_bound_exact_and_positive", high == 528918511616 and high > 0
          and c2-S == 11357440761856 and c2-S > 0)
    check("saved_R_and_remainder", list(map(F, old["positivity"]["R_y_ascending"])) == coeffs(R, 3)
          and F(old["positivity"]["square_residual"]) == residual)
    check("saved_range_bounds", F(old["positivity"]["low_R_lower_bound"]) == low
          and F(old["positivity"]["high_R_constant"]) == c2-S
          and F(old["positivity"]["high_R_cubic_coefficient"]) == high
          and F(old["positivity"]["split"]) == S)

    h, r, s = F(11, 16), F(21, 16), F(7, 16)
    pair_value = 2*((s-h)**2-1)/((s-h)**2+1)**2
    alpha, beta = 1/(s+r)**2, 1/(s-r)**2
    upper = pair_value+alpha+beta
    check("witness_domain_and_displacement", s not in (-r, r) and s-h == -F(1, 4))
    check("pair_value", pair_value == -F(480, 289))
    check("allocation_positive_coefficients", alpha == F(16, 49) and beta == F(64, 49))
    check("allocation_upper_bound", upper == -F(400, 14161) and upper < 0)
    obstruction = old["allocation_obstruction"]
    check("saved_obstruction_all_numeric_values", all(
        F(obstruction[key]) == value for key, value in {
            "x": s, "pair_value": pair_value, "alpha_h_coefficient": alpha,
            "beta_h_coefficient": beta, "full_budget_upper_bound": upper,
            "required_lower_bound": F(0), "strict_margin": -upper}.items()))
    # Each pair has quadratic numerator leading coefficient 2, quartic
    # denominator leading coefficient 1; each real term contributes 1.
    tail = F(actual[-1], 549755813888)
    check("tail_leading_ratio", tail == 6 and denominator_x[-1] == 1)

    evidence = {
        "target": "Audit L510's all-real aggregate positivity, denominator identity and four-constant allocation obstruction.",
        "method": "Independent symmetric integer-polynomial derivation in y=x^2; no generator import or numerical sampling",
        "Q_actual": actual, "Q_required": expected,
        "C_y_ascending": coeffs(C, 2), "paired_y_ascending": coeffs(paired, 3),
        "denominator_x_ascending": list(map(str, denominator_x)),
        "numerator_x_ascending": list(map(str, numerator_x)),
        "square_remainder": str(residual), "required_square_remainder": ">0",
        "R_y_ascending": coeffs(R, 3),
        "low_bound": low, "required_low_bound": ">0",
        "high_constant": c2-S, "high_cubic_coefficient": high,
        "required_high_bounds": "constant>0, cubic coefficient>=0",
        "allocation_upper_bound": str(upper), "required_allocation_value": ">=0 for feasibility",
        "tail_limit": str(tail),
        "manual_domain_checks": [
            "A=(x-h)^2+1>=1, B=(x+h)^2+1>=1; M!=0 on the stated domain",
            "For 0<=y<=1, 1-y,1-y^2,y^3>=0",
            "For y>=1, y^3-y=y(y-1)(y+1)>=0; y^3-y^2=y^2(y-1)>=0",
            "At +/-r only its corresponding inverse-square term diverges; the other terms are bounded",
            "Original nonnegative four-constant budgets imply alpha_h<=1 and beta_h<=1; positive coefficients preserve the upper inequality",
        ],
        "checks": checks, "failures": [name for name, passed in checks.items() if not passed],
        "limitations": "Only fixed finite first-sign separation; no original grid audit, Xi transfer, infinite assembly, higher signs or novelty certification",
    }
    evidence["passed"] = not evidence["failures"]
    output = Path(__file__).with_name("l510-independent-audit.json")
    output.write_text(json.dumps(evidence, indent=2)+"\n")
    print(f"Exact checks: {sum(checks.values())}/{len(checks)}; failures: {evidence['failures']}")
    print(f"Square remainder {residual}>0; R bounds: {low}>0, {c2-S}+{high}*y^3>0")
    print(f"Allocation upper bound {upper}<0; required >=0. Tail limit {tail}.")
    print(f"Certificate: {output.relative_to(Path.cwd())}")
    return 0 if evidence["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
