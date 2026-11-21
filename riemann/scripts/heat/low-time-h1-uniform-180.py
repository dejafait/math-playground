"""Fixed-budget outward interval attempt for actual logarithmic H1.

Run from riemann: python3 scripts/heat/low-time-h1-uniform-180.py
Complete evidence is saved beside this script, not printed.
The tilted-tail proof and scope are in drafts/2026-11-09-low-time-h1-uniform-attempt-180.md.
"""

import json
from decimal import Decimal
from fractions import Fraction
from math import factorial
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "hankel"))
import certify_hankel as base

PRECISION = 100
PARAMETER_PANELS = 256
SPATIAL_PANELS = 64
ORDERS = (0, 2, 4, 6, 8)
OUTPUT = Path(__file__).with_suffix(".json")
base.PRECISION = PRECISION
for ctx in (base.DOWN, base.UP, base.NEAR):
    ctx.prec = PRECISION
    ctx.clear_flags()
I = base.I


def tilt_jet(u, lam):
    exponent = base.constant(0)
    exponent[0] = lam * u**2
    exponent[1] = 2 * lam * u
    exponent[2] = lam
    return base.exponential(exponent)


def tilted_tail():
    beta = I.rational(Fraction(119, 40))
    coefficient = sum((I(factorial(6) // factorial(6-j)) * 50**(6-j)
                       / beta**(j+1) for j in range(7)), I(0))
    spatial = 128 * (-50*beta).exp() * coefficient
    theta = 57600000 * (1-25*beta).exp()
    return spatial, theta, spatial + theta


def checks():
    base.self_check()
    # exp(lambda*u^2) has exact normalized coefficients at u=0.
    lam_exact = Fraction(1, 20)
    jet = tilt_jet(I(0), I.rational(lam_exact))
    for n, enclosed in enumerate(jet):
        exact = (lam_exact**(n//2) / factorial(n//2)) if n % 2 == 0 else Fraction(0)
        assert Fraction(enclosed.lo) <= exact <= Fraction(enclosed.hi)
    # Verify the elementary numerical premises used in the tail estimate.
    assert sum((Fraction(4)**j / factorial(j) for j in range(8)), Fraction(0)) > 50
    assert 16 * I(-9).exp().hi < Decimal("0.5")
    assert 16 * (-11*I.rational(Fraction(119, 40))).exp().hi < Decimal("0.5")
    assert all(ctx.prec == 100 for ctx in (base.DOWN, base.UP, base.NEAR))


def prepare(pi):
    h = I.rational(Fraction(1, SPATIAL_PANELS))
    weights = {j: 2*h**(j+1)/(j+1) for j in (0, 2, 4, 6)}
    remainder_weight = 2*h**9/9
    cached = []
    for i in range(SPATIAL_PANELS):
        center = I.rational(Fraction(2*i+1, SPATIAL_PANELS))
        domain = I(I.rational(Fraction(2*i, SPATIAL_PANELS)).lo,
                   I.rational(Fraction(2*i+2, SPATIAL_PANELS)).hi)
        mid_kernel = base.theta_kernel_jet(center, pi)
        dom_kernel = base.theta_kernel_jet(domain, pi)
        cached.append((center, domain,
                       {k: base.moment_jet(center, k, mid_kernel) for k in ORDERS},
                       {k: base.moment_jet(domain, k, dom_kernel) for k in ORDERS}))
    return cached, weights, remainder_weight


def certify_panel(lam, cached, weights, remainder_weight, tail):
    totals = {k: I(0) for k in ORDERS}
    errors = {k: I(0) for k in ORDERS}
    for center, domain, midpoint, full in cached:
        mid_tilt = tilt_jet(center, lam)
        dom_tilt = tilt_jet(domain, lam)
        for k in ORDERS:
            coefficients = base.multiply(midpoint[k], mid_tilt)
            eighth = base.multiply(full[k], dom_tilt)[8]
            error = I(eighth.magnitude()) * remainder_weight
            integral = sum((coefficients[j]*weights[j] for j in weights), I(0))
            totals[k] = totals[k] + integral + I(error.hi.copy_negate(), error.hi)
            errors[k] = errors[k] + error
    moments = {k: totals[k] + I(0, tail.hi) for k in ORDERS}
    if any(value.lo <= 0 for value in moments.values()):
        return {"lambda": lam.data(), "moments": {str(k): v.data() for k, v in moments.items()},
                "quadrature_error_bounds": {str(k): v.data() for k, v in errors.items()},
                "status": "unresolved_moment_lower_bound", "strict_signs_certified": False}
    m0 = moments[0]
    a, b = moments[2]/(2*m0), moments[4]/(24*m0)
    c, d = moments[6]/(720*m0), moments[8]/(40320*m0)
    s2 = a**2 - 2*b
    s3 = a**3 - 3*a*b + 3*c
    s4 = a**4 - 4*a**2*b + 2*b**2 + 4*a*c - 4*d
    determinant = s2*s4 - s3**2
    expanded = a**2*b**2 - 4*b**3 - 2*a**3*c + 10*a*b*c - 9*c**2 - 4*a**2*d + 8*b*d
    if max(determinant.lo, expanded.lo) > min(determinant.hi, expanded.hi):
        raise ArithmeticError("Equivalent determinant enclosures fail overlap")
    certified = s2.lo > 0 and determinant.lo > 0
    return {
        "lambda": lam.data(), "moments": {str(k): v.data() for k, v in moments.items()},
        "quadrature_error_bounds": {str(k): v.data() for k, v in errors.items()},
        "coefficients": {key: val.data() for key, val in zip(("a", "b", "c", "d"), (a, b, c, d))},
        "S2": s2.data(), "S3": s3.data(), "S4": s4.data(),
        "determinant": determinant.data(), "expanded_determinant": expanded.data(),
        "status": "strict_signs_certified" if certified else "unresolved_interval_width",
        "strict_signs_certified": certified,
    }


def main():
    checks()
    pi = base.pi_bounds()
    spatial_tail, theta_tail, tail = tilted_tail()
    cached, weights, remainder_weight = prepare(pi)
    result = {
        "scope": "actual H1 on [0,1/20] only; no contact or RH claim",
        "precision": PRECISION, "parameter_panels": PARAMETER_PANELS,
        "spatial_panels": SPATIAL_PANELS, "theta_terms": 4,
        "spatial_cutoff": 2, "taylor_remainder_order": 8,
        "pi": pi.data(), "beta": "119/40",
        "tails": {"spatial": spatial_tail.data(), "theta": theta_tail.data(), "total": tail.data()},
        "arithmetic_contract": "L037; unmodified base interval primitives with contexts set to 100 digits",
        "self_checks_passed": True, "status": "running", "panels": [],
    }
    for p in range(PARAMETER_PANELS):
        lam = I(I.rational(Fraction(p, 20*PARAMETER_PANELS)).lo,
                I.rational(Fraction(p+1, 20*PARAMETER_PANELS)).hi)
        panel = certify_panel(lam, cached, weights, remainder_weight, tail)
        panel["index"] = p
        result["panels"].append(panel)
        # Preserve complete finished panels if the calculation is interrupted.
        if (p+1) % 32 == 0:
            OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
            print(f"Completed {p+1}/{PARAMETER_PANELS} closed parameter panels", flush=True)
    failed = [row["index"] for row in result["panels"] if not row["strict_signs_certified"]]
    result["failed_panels"] = failed
    result["status"] = "certified" if not failed else "unresolved"
    rows = result["panels"]
    result["summary"] = {
        "required_lower_bound": ">0 for both S2 and determinant on every closed panel",
        "certified_panel_count": PARAMETER_PANELS-len(failed),
        "failed_panel_count": len(failed),
        "minimum_mass_lower": str(min(Decimal(r["moments"]["0"]["lower"]) for r in rows)),
        "minimum_S2_lower": str(min(Decimal(r["S2"]["lower"]) for r in rows)),
        "minimum_determinant_lower": str(min(Decimal(r["determinant"]["lower"]) for r in rows)),
        "maximum_determinant_upper": str(max(Decimal(r["determinant"]["upper"]) for r in rows)),
        "determinant_zero_containing_panels": sum(Decimal(r["determinant"]["lower"]) <= 0 <= Decimal(r["determinant"]["upper"]) for r in rows),
        "exceptional_arithmetic": False,
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result["summary"], indent=2))
    print(f"Complete certificate and failed panel list: {OUTPUT.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
