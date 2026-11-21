"""Fixed-budget outward interval attempt for actual logarithmic H2.

Run from riemann: python3 scripts/heat/low-time-h2-uniform-195.py
Complete evidence is saved beside this script, not printed.
The full proof and scope are in lemmas/L917-low-time-twelfth-moment-enclosures-and-h2-budget-stop.md.
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
ORDERS = (0, 2, 4, 6, 8, 10, 12)
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
    coefficient = sum((I(factorial(8) // factorial(8-j)) * 50**(8-j)
                       / beta**(j+1) for j in range(9)), I(0))
    spatial = 128 * (-50*beta).exp() * coefficient
    theta = 3225600000 * (1-25*beta).exp()
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
    e = [I(1)] + [moments[2*n]/(factorial(2*n)*m0) for n in range(1, 7)]
    a,b,c,d,e5,f = e[1:]
    s = {
        1: a,
        2: a**2 - 2*b,
        3: a**3 - 3*a*b + 3*c,
        4: a**4 - 4*a**2*b + 2*b**2 + 4*a*c - 4*d,
        5: a**5 - 5*a**3*b + 5*a*b**2 + 5*a**2*c - 5*b*c - 5*a*d + 5*e5,
        6: a**6 - 6*a**4*b + 9*a**2*b**2 - 2*b**3 + 6*a**3*c
           - 12*a*b*c + 3*c**2 - 6*a**2*d + 6*b*d + 6*a*e5 - 6*f,
    }
    minor1 = s[2]
    minor2 = s[2]*s[4] - s[3]**2
    # Cofactor expansion, retaining each signed term.
    cofactors = [s[4]*s[6]-s[5]*s[5],
                 s[3]*s[6]-s[5]*s[4],
                 s[3]*s[5]-s[4]*s[4]]
    terms = [s[2]*cofactors[0], -s[3]*cofactors[1], s[4]*cofactors[2]]
    minor3 = sum(terms, I(0))
    expanded = (s[2]*s[4]*s[6] + 2*s[3]*s[4]*s[5]
                - s[2]*s[5]*s[5] - s[6]*s[3]*s[3] - s[4]*s[4]*s[4])
    if max(minor3.lo, expanded.lo) > min(minor3.hi, expanded.hi):
        raise ArithmeticError("Equivalent H2 determinant enclosures fail overlap")
    minors = {"1":minor1, "2":minor2, "3":minor3}
    failed = [key for key,val in minors.items() if val.lo <= 0]
    return {
        "lambda": lam.data(), "moments": {str(k): v.data() for k, v in moments.items()},
        "quadrature_error_bounds": {str(k): v.data() for k, v in errors.items()},
        "normalized_coefficients": {str(n): e[n].data() for n in range(1,7)},
        "S": {str(n): s[n].data() for n in range(1,7)},
        "leading_minors": {key:val.data() for key,val in minors.items()},
        "determinant_cofactors": [v.data() for v in cofactors],
        "determinant_terms": [v.data() for v in terms],
        "expanded_determinant": expanded.data(),
        "failed_minors": failed,
        "status": "strict_signs_certified" if not failed else "unresolved_interval_width",
        "strict_signs_certified": not failed,
    }


def main():
    checks()
    pi = base.pi_bounds()
    spatial_tail, theta_tail, tail = tilted_tail()
    cached, weights, remainder_weight = prepare(pi)
    result = {
        "scope": "actual H2 on [0,1/20] only; no contact or RH claim",
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
        "required_lower_bound": ">0 for all three leading minors on all 256 closed panels",
        "certified_panel_count": PARAMETER_PANELS-len(failed),
        "failed_panel_count": len(failed),
        "minimum_mass_lower": str(min(Decimal(r["moments"]["0"]["lower"]) for r in rows)),
        "tail_upper": str(tail.hi),
        "leading_minors": {
            key: {
                "minimum_lower": str(min(Decimal(r["leading_minors"][key]["lower"]) for r in rows)),
                "maximum_upper": str(max(Decimal(r["leading_minors"][key]["upper"]) for r in rows)),
                "strict_positive_count": sum(Decimal(r["leading_minors"][key]["lower"]) > 0 for r in rows),
                "zero_containing_count": sum(Decimal(r["leading_minors"][key]["lower"]) <= 0 <= Decimal(r["leading_minors"][key]["upper"]) for r in rows),
                "strict_negative_count": sum(Decimal(r["leading_minors"][key]["upper"]) < 0 for r in rows),
            } for key in ("1","2","3")
        },
        "exceptional_arithmetic": False,
    }
    from decimal import DivisionByZero, InvalidOperation, Overflow, Underflow, Subnormal
    signals = (DivisionByZero, InvalidOperation, Overflow, Underflow, Subnormal)
    result["arithmetic"] = {name: {
        "precision":ctx.prec, "rounding":ctx.rounding,
        "traps": {sig.__name__: ctx.traps[sig] for sig in signals},
        "exceptional_flags": {sig.__name__: ctx.flags[sig] for sig in signals},
    } for name,ctx in (("DOWN",base.DOWN),("UP",base.UP),("NEAR",base.NEAR))}
    assert all(ctx.traps[sig] and not ctx.flags[sig] for ctx in (base.DOWN,base.UP,base.NEAR) for sig in signals)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result["summary"], indent=2))
    print(f"Complete certificate and failed panel list: {OUTPUT.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
