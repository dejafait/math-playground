"""One analytic boundary-reserve bound; no lobe quadrature or parameter sweep.

See L913. Retains L037's trusted Decimal arithmetic contract.
"""

import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "hankel"))
from certify_hankel import I, PRECISION, pi_bounds, self_check


def certify():
    self_check()
    pi = pi_bounds()
    q = 9 * pi / 32
    a = pi / 16
    h = q / 2
    e = q.exp()
    ratio = I.rational(Fraction(81, 16)) * (-5 * pi).exp()
    theta_sum = 1 + 16 * (-3 * pi).exp() / (1 - ratio)
    coefficient = 8 * pi**2 * theta_sum
    beta = 2 * pi * e - I.rational(Fraction(9, 2))
    d = pi * (e**2 + 1)
    lam = 2 * d - 9
    inner = coefficient**2 / (16 * pi) * (3 * q - 2 * pi * e).exp()
    outer = (2 * coefficient**2 * (I.rational(Fraction(9, 2)) * q - d).exp()
             * (h**2 / lam + 2 * h / lam**2 + I(2) / lam**3))
    density = inner + outer
    sine_integral = 16 * (1 + (-beta * a).exp()) / (beta**2 + 256)
    reserve_bound = 2 * density * sine_integral
    required = I.rational(Fraction(15, 10**6))
    proper_margin = I.rational(Fraction(23960, 10**8))
    residual_proper = proper_margin - reserve_bound
    full_margin = I.rational(Fraction(159908498950, 10**16))
    full_after_bound = full_margin - reserve_bound
    checks = {
        "geometric_ratio_below_one": 0 < ratio.lo <= ratio.hi < 1,
        "exp_Q_above_two": e.lo > 2,
        "positive_decay": beta.lo > 0 and lam.lo > 0,
        "two_piece_decay_comparison": (pi * (e**2 - 1) - beta).lo > 0,
        "positive_density_bound": inner.lo > 0 and outer.lo > 0,
        "proper_cut_bound_remains_positive": residual_proper.lo > 0,
        "upper_bound_exceeds_required_threshold": reserve_bound.lo > required.hi,
        "saved_full_cut_lower_bound_does_not_pay_upper_bound": full_after_bound.hi < 0,
        "displayed_U_enclosure": (
            Fraction(4284047, 10**11) < Fraction(reserve_bound.lo)
            and Fraction(reserve_bound.hi) < Fraction(4284048, 10**11)),
        "displayed_proper_cut_margin": Fraction(residual_proper.lo) > Fraction(19675952, 10**11),
        "displayed_full_lower_estimate": (
            Fraction(-2684963, 10**11) < Fraction(full_after_bound.lo)
            and Fraction(full_after_bound.hi) < Fraction(-2684962, 10**11)),
    }
    failures = [key for key, passed in checks.items() if not passed]
    bound_passes = reserve_bound.hi < required.lo
    return {
        "scope": "x=16,y=0; exterior inward payment; Q=9pi/32; no quadrature",
        "arithmetic_contract": "L037; Python Decimal/exp and execution trusted",
        "precision": PRECISION,
        "formula_proof": "lemmas/L913-monotone-exterior-payment-boundary-reserve-unpaid.md",
        "constants": {key: val.data() for key, val in {
            "pi": pi, "Q": q, "a": a, "h": h, "exp_Q": e,
            "theta_ratio": ratio, "theta_sum": theta_sum,
            "kernel_coefficient": coefficient, "beta": beta,
            "D": d, "lambda": lam,
        }.items()},
        "bounds": {key: val.data() for key, val in {
            "rho_Q_inner_majorant": inner, "rho_Q_outer_majorant": outer,
            "rho_Q_majorant": density, "weighted_exponential_integral": sine_integral,
            "combined_raw_charge_upper_bound_U": reserve_bound,
            "required_U_strictly_below": required,
            "U_minus_required": reserve_bound - required,
            "U_over_required": reserve_bound / required,
            "saved_proper_cut_strict_lower_bound": proper_margin,
            "reduced_proper_cut_strict_lower_bound": residual_proper,
            "saved_full_cut_strict_lower_bound": full_margin,
            "full_cut_lower_bound_minus_U": full_after_bound,
        }.items()},
        "input_provenance": {
            "proper_lower_bound": "L905 audited raw-cut table: weakest proper cut >0.00023960",
            "full_lower_bound": "L912 audited rational raw enclosure: >0.0000159908498950",
        },
        "checks": checks,
        "verification_failures": failures,
        "result": {
            "decision": "RESERVE_BOUND_UNPAID" if not bound_passes else "RESERVE_BOUND_PAID",
            "required_bound_passed": bound_passes,
            "required_failures": [] if bound_passes else ["U is not below 15/10^6"],
            "qualification": "C<=U; an oversized U is no lower bound for C and no negative Hall cut",
            "next_operation": "stop this envelope test; no refinement or sweep",
        },
    }


if __name__ == "__main__":
    certificate = certify()
    path = HERE / "boundary-reserve-170.json"
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    print("Result:", certificate["result"]["decision"])
    print("Raw charge upper-bound U:", certificate["bounds"]["combined_raw_charge_upper_bound_U"])
    print("Required U <:", certificate["bounds"]["required_U_strictly_below"])
    print("Reduced proper-cut lower bound:", certificate["bounds"]["reduced_proper_cut_strict_lower_bound"])
    print("Verification failures:", certificate["verification_failures"])
    print("Unmet requirement:", certificate["result"]["required_failures"])
    print("Certificate:", path.relative_to(HERE.parent.parent))
    if certificate["verification_failures"]:
        raise SystemExit(1)
