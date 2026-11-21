"""Independent scalar/accounting audit of L913; no quadrature or new bound.

The general crossing-cut and analytic-domain proofs are checked in L913.
Decimal operations/exp retain L037's trusted implementation contract.
"""

import hashlib
import itertools
import json
import sys
from fractions import Fraction
from math import comb, factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE.parent / "hankel"))
import certify_hankel as arithmetic

I = arithmetic.I
for context in (arithmetic.DOWN, arithmetic.UP, arithmetic.NEAR):
    context.prec = 100


def audit():
    arithmetic.self_check()
    source = HERE / "boundary-reserve-170.json"
    saved = json.loads(source.read_text())
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)

    def inside(name, value, original):
        check(name, Fraction(original["lower"]) <= Fraction(value.lo)
              <= Fraction(value.hi) <= Fraction(original["upper"]))

    # Recompute from the exact same definitions, with independent expression
    # assembly and more precision; no call to boundary_reserve_170.certify.
    pi = arithmetic.pi_bounds()
    a = pi / 16
    q = 9 * a / 2
    h = q / 2
    e = q.exp()
    ratio = I.rational(Fraction(81, 16)) / (5 * pi).exp()
    theta_sum = 1 + I(16) / ((3 * pi).exp() * (1 - ratio))
    c = 8 * pi * pi * theta_sum
    beta = (4 * pi * e - 9) / 2
    d = pi * ((2 * q).exp() + 1)
    lam = 2 * (d - I.rational(Fraction(9, 2)))
    peak = c * c * (9 * h - 2 * pi * e).exp()
    inner = peak / (16 * pi * (3 * h).exp())
    outer_moment = sum(
        (comb(2, j) * factorial(j) * h**(2-j) / lam**(j+1)
         for j in range(3)), I(0))
    outer = 2 * c * c * (9 * h - d).exp() * outer_moment
    density = inner + outer
    sine_integral = (1 + I(1) / (beta * a).exp()) / (beta * beta / 16 + 16)
    u = 2 * density * sine_integral
    required = I("0.000015")
    proper = I("0.00023960")
    full = I("0.0000159908498950")
    constants = {
        "pi": pi, "Q": q, "a": a, "h": h, "exp_Q": e,
        "theta_ratio": ratio, "theta_sum": theta_sum,
        "kernel_coefficient": c, "beta": beta, "D": d, "lambda": lam,
    }
    bounds = {
        "rho_Q_inner_majorant": inner, "rho_Q_outer_majorant": outer,
        "rho_Q_majorant": density,
        "weighted_exponential_integral": sine_integral,
        "combined_raw_charge_upper_bound_U": u,
        "required_U_strictly_below": required,
        "U_minus_required": u - required, "U_over_required": u / required,
        "saved_proper_cut_strict_lower_bound": proper,
        "reduced_proper_cut_strict_lower_bound": proper-u,
        "saved_full_cut_strict_lower_bound": full,
        "full_cut_lower_bound_minus_U": full-u,
    }
    for group, values in (("constants", constants), ("bounds", bounds)):
        check(group + "_complete_keys", set(values) == set(saved[group]))
        for key, value in values.items():
            inside(group + "/" + key, value, saved[group][key])

    # Recheck every saved verification claim, independently of its stored flag.
    reconstructed = {
        "geometric_ratio_below_one": 0 < ratio.lo <= ratio.hi < 1,
        "exp_Q_above_two": e.lo > 2,
        "positive_decay": beta.lo > 0 and lam.lo > 0,
        "two_piece_decay_comparison": (pi*(e*e-1)-beta).lo > 0,
        "positive_density_bound": inner.lo > 0 and outer.lo > 0,
        "proper_cut_bound_remains_positive": (proper-u).lo > 0,
        "upper_bound_exceeds_required_threshold": u.lo > required.hi,
        "saved_full_cut_lower_bound_does_not_pay_upper_bound": (full-u).hi < 0,
        "displayed_U_enclosure": Fraction("0.00004284047") < Fraction(u.lo)
            and Fraction(u.hi) < Fraction("0.00004284048"),
        "displayed_proper_cut_margin": Fraction((proper-u).lo)
            > Fraction("0.00019675952"),
        "displayed_full_lower_estimate": Fraction("-0.00002684963")
            < Fraction((full-u).lo) <= Fraction((full-u).hi)
            < Fraction("-0.00002684962"),
    }
    check("saved_check_keys", set(reconstructed) == set(saved["checks"]))
    for key, value in reconstructed.items():
        check("claim/" + key, value and saved["checks"][key] is True)
    check("source_no_verification_failures", saved["verification_failures"] == [])
    check("source_precision", saved["precision"] == 70)
    check("source_result", saved["result"]["decision"] == "RESERVE_BOUND_UNPAID"
          and saved["result"]["required_bound_passed"] is False
          and saved["result"]["required_failures"] == ["U is not below 15/10^6"])

    # L905's audited raw table, expanded to all fourteen proper subsets.
    # These are reused strict lower bounds, not new integral evaluations.
    raw_lowers = {
        (-2,): "0.00114816", (1,): "0.00114816",
        (-1,): "0.00224814", (0,): "0.00224814",
        (-2,-1): "0.00182739", (0,1): "0.00182739",
        (-2,0): "0.00339630", (-1,1): "0.00339630",
        (-2,1): "0.00229633", (-1,0): "0.00066034",
        (-2,-1,0): "0.00023960", (-1,0,1): "0.00023960",
        (-2,-1,1): "0.00297556", (-2,0,1): "0.00297556",
    }
    cut_rows = []
    core = (-2, -1, 0, 1)
    for size in range(1, 5):
        for subset in itertools.combinations(core, size):
            neighbors = sorted({j for k in subset for j in (k, k+1)})
            boundaries = [j for j in (-2, 2) if j in neighbors]
            check("boundary_incidence/" + str(subset),
                  (-2 in boundaries) == (-2 in subset)
                  and (2 in boundaries) == (1 in subset))
            lower = full if size == 4 else I(raw_lowers[subset])
            residual = lower - len(boundaries) * u / 2
            if size < 4:
                check("proper_cut/" + str(subset),
                      Fraction(residual.lo) > Fraction(196, 10**6))
            cut_rows.append({
                "S": subset, "T": neighbors, "charged_resources": boundaries,
                "raw_cut_strict_lower_bound": lower.data(),
                "reduced_cut_strict_lower_estimate": residual.data(),
                "conclusion": "POSITIVE" if size < 4 else "UNRESOLVED",
            })
    check("all_core_subsets", len(cut_rows) == 15 and len(raw_lowers) == 14)

    failures = [name for name, passed in checks.items() if not passed]
    return {
        "scope": "L913 audit only; same U, same F; no lobe integrations",
        "precision": 100,
        "arithmetic_contract": "L037; Decimal/exp/Python execution trusted",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "arithmetic_sha256": hashlib.sha256(
            (HERE.parent / "hankel/certify_hankel.py").read_bytes()).hexdigest(),
        "constants": {key: value.data() for key, value in constants.items()},
        "bounds": {key: value.data() for key, value in bounds.items()},
        "core_cuts": cut_rows, "checks": checks,
        "verification_failures": failures,
        "result": {
            "audit_passed": not failures,
            "check_count": len(checks),
            "required_bound_passed": False,
            "unmet_requirement": "U < 15/10^6",
            "qualification": "C<=U only; full reduced core sign unresolved",
        },
    }


if __name__ == "__main__":
    certificate = audit()
    path = HERE / "boundary-reserve-audit-172.json"
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    print("Audit passed:", certificate["result"]["audit_passed"],
          "checks:", certificate["result"]["check_count"])
    print("U:", certificate["bounds"]["combined_raw_charge_upper_bound_U"])
    print("Required U < 0.000015: unpaid; full reduced core unresolved")
    print("Verification failures:", certificate["verification_failures"])
    print("Certificate:", path.relative_to(ROOT))
    if certificate["verification_failures"]:
        raise SystemExit(1)
