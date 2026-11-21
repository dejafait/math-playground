"""Exact rational enclosure-box test for the approved dictionary1570.

This is not an optimizer for the actual kernels. Analytic enclosure and
box-optimality proofs, including all conditional inputs, are in draft1571.
No zero coordinate or external numerical library is used.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

checks = []


def check(name, actual, required, relation="<"):
    passed = actual < required if relation == "<" else actual > required
    checks.append(dict(name=name, actual_exact=str(actual),
                       required_exact=str(required), relation=relation,
                       passed=passed))


base, eps = Q(3, 8), Q(1, 10**100)
check("high_gaussian_tail", Q(3, 25)*100**2*base**312, eps)
check("sqrt10_less_than_13_over_4_squared", Q(10), Q(13, 4)**2)
check("compact_low_exponent_exceeds_14", Q(1849, 128), Q(14), ">")
S2 = Q(40, 196)+Q(3, 25)
SG = 40*base**6+eps
A2 = 3*(40*base**18+eps)
Ac = 27*(40*base**14+eps)
B = 3*Ac+Q(9, 5)*(Q(16, 45)*(SG/3+12*S2)+A2/3)
E = 8*B
K = E.numerator//E.denominator+1
check("E_bound_below_integer_K", E, Q(K))
check("all_odd_angles_below_1", 16*A2, Q(1))
Pmin = Q(1, 12)*Q(1, 3)**57-3*eps
check("retained_spatial_profile_lower_positive", Pmin, Q(0), ">")
# For imaginary w=i*y: 0<y*lo<Im(kappa)<y*hi.
lo = 3*Pmin/Q(3)**K
hi = 8*A2*Q(3)**K
check("imaginary_box_nonempty", hi, lo, ">")
rho = (hi-lo)/(hi+lo)
gap = 1-rho
check("box_radius_ratio_exceeds_999_over_1000", rho, Q(999, 1000), ">")
check("certified_residual_below_1", rho, Q(1))
Llo = Q(1, 3)**(K+1)

dictionary = []
for axis in ["real", "imaginary"]:
    for a in [Q(1, 4), Q(1, 2), Q(1), Q(2)]:
        for part in ["Re", "Im"]:
            name = f"{part}_kappa_{axis}_{a}"
            nonzero = (axis == "real" and part == "Re") or (
                       axis == "imaginary" and part == "Im")
            if not nonzero:
                lower = upper = Q(0)
            elif axis == "real":
                upper = 16*a*A2*Q(3)**K
                lower = -upper
            else:
                lower, upper = a*lo, a*hi
            dictionary.append(dict(name=name, lower=str(lower),
                                   upper=str(upper), coefficient_sign="free"))
for s in [Q(1, 16), Q(1, 4), Q(1), Q(4)]:
    dictionary.append(dict(name=f"L_{s}", lower=str(Llo), upper="1",
                           coefficient_sign="nonnegative"))

chosen = "Im_kappa_imaginary_1/4"
coefficients = {d["name"]: "0" for d in dictionary}
coefficients[chosen] = str(-2/(Q(1, 4)*(lo+hi)))


def residual_box():
    center, radius = Q(1), Q(0)
    for d in dictionary:
        a = Q(coefficients[d["name"]])
        l, u = Q(d["lower"]), Q(d["upper"])
        center += a*(l+u)/2
        radius += abs(a)*(u-l)/2
        if d["coefficient_sign"] == "nonnegative":
            if a < 0:
                raise AssertionError("positive-cone coefficient is negative")
    return center, radius, abs(center)+radius


center, radius, residual = residual_box()
if center != 0 or residual != rho:
    raise AssertionError("candidate does not attain the exact box lower bound")

# Both allowed generation grids are solved in this deliberately conservative
# box model. The same width-uniform bounds hold at every row, so the exact
# solution and dual lower bound in draft1571 solve each finite program.
solves = []
for n in [128, 256]:
    solves.append(dict(grid_denominator=n,
                       widths=[str(1+Q(j, n)) for j in range(n+1)],
                       interval_dictionary="/dictionary",
                       coefficients="/candidate/coefficients",
                       exact_primal_value=str(rho),
                       exact_box_lower_bound=str(rho),
                       optimality_proof="draft1571, Exact box minimax calculation"))

validation = [dict(left=str(1+Q(j, 128)), right=str(1+Q(j+1, 128)),
                   interval_dictionary="/dictionary",
                   residual_upper=str(residual), endpoints_included=True)
              for j in range(128)]
failures = []
if not residual < Q(1, 2):
    failures.append(dict(name="requested_strict_residual",
                         actual_certified_upper=str(residual),
                         required_strict_upper="1/2",
                         meaning="Enclosure bound fails; actual residual is not bounded below."))
certificate = dict(
    analytic_record="drafts/2026-11-18-bounded-variation-dual-calculation-1571.md",
    target_assessment="drafts/literature/2026-11-18-bounded-variation-continuum-dual-test-1570.md",
    assumptions=["C032j/m/q fixed-v1 probability/analytic inputs, conditional as recorded",
                 "full divisor with multiplicity, gamma>14, |delta|<1/2, no ordinate zero",
                 "zeros through 100 real; at least one ordinate in (14,15)",
                 "N(100)<40; sum_gamma_gt_100 gamma^-2<3/25 from C032s and calculation1564",
                 "3<pi<4, 8/3<e<3, exp(1/16)<16/15"],
    inputs_not_supplied=["certified individual finite-zero coordinate intervals"],
    elementary_bounds={k: str(v) for k, v in dict(eps=eps, S2=S2, SG=SG,
                           A2=A2, Ac=Ac, B2=B, E_disk=E, K=K,
                           Pmin=Pmin, imaginary_lo_per_y=lo,
                           imaginary_hi_per_y=hi, L_lower=Llo).items()},
    dictionary=dictionary,
    candidate=dict(coefficients=coefficients, residual_center=str(center),
                   residual_radius=str(radius), certified_residual_upper=str(residual)),
    solves=solves,
    validation=dict(subinterval_count=128, maximum_allowed=4096,
                    cells=validation, coefficient_error_accounting="exact sum |a_j|*(u_j-l_j)/2",
                    arithmetic_rounding_allowance="0; all arithmetic rational"),
    results=dict(box_optimum=str(rho), gap_below_one=str(gap),
                 required_strict_upper="1/2", uniform_target_certified=False,
                 actual_dictionary_lower_bound_certified=False,
                 dominant_error="coarse full-divisor/primitive enclosure width, amplified by coefficients",
                 scope="Exact optimum of stated independent interval boxes only; no actual kernel optimum inferred."),
    arithmetic_checks=checks, failures=failures,
    arithmetic_failures=[c["name"] for c in checks if not c["passed"]])
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"certified residual upper = 1 - {float(gap):.12g}; required < 1/2")
print(f"box optimum > 999/1000; E_disk < {K}; 2 solves; 128 closed validation cells")
print(f"dominant error: {certificate['results']['dominant_error']}")
print(f"failed target inequalities={len(failures)}; arithmetic failures={len(certificate['arithmetic_failures'])}")
print(f"certificate={path}; proof={certificate['analytic_record']}")
raise SystemExit(bool(certificate["arithmetic_failures"]))
