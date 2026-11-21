"""Exact rational interval certificate for L709; no floating point decisions.

Composite Simpson errors use the analytic fourth-derivative bounds
proved in L709. Cell maxima use its second-derivative bound. The log
routine encloses a rational logarithm by an integer-rounded atanh series.
This certifies auxiliary rate inequalities, not the analytic lemma.
"""
from fractions import Fraction as F
from pathlib import Path
import json

SCALE = 1 << 100
TERMS = 40
PANELS = 32
CELLS = 200
d, R, U, A, Y = F(5, 4), F(11, 8), F(121, 64), F(27, 10), F(9, 20)


def ceildiv(a, b):
    return -(-a // b)


def fixed(q):
    q = F(q)
    return (q.numerator * SCALE // q.denominator,
            ceildiv(q.numerator * SCALE, q.denominator))


def log_unit(a, b):
    """1 <= a/b <= 2. Return integers enclosing SCALE*log(a/b)."""
    assert b <= a <= 2*b
    zl = (a-b)*SCALE // (a+b)
    zu = ceildiv((a-b)*SCALE, a+b)
    z2l, z2u = zl*zl // SCALE, ceildiv(zu*zu, SCALE)
    pl, pu = zl, zu
    lo = hi = 0
    for k in range(TERMS):
        odd = 2*k+1
        lo += (2*pl) // odd
        hi += ceildiv(2*pu, odd)
        pl = pl*z2l // SCALE
        pu = ceildiv(pu*z2u, SCALE)
    # z <= 1/3. A larger z <= 1/2 gives this uniform exact remainder.
    remainder = ceildiv(8*SCALE, 3*(2*TERMS+1)*(1 << (2*TERMS+1)))
    return lo, hi+remainder


LOG2 = log_unit(2, 1)


def logq(q):
    q = F(q)
    assert q > 0
    a, b = q.numerator, q.denominator
    sign = 1
    if a < b:
        a, b = b, a
        sign = -1
    power = 0
    while a > 2*b:
        b *= 2
        power += 1
    lo, hi = log_unit(a, b)
    lo += power*LOG2[0]
    hi += power*LOG2[1]
    return (lo, hi) if sign == 1 else (-hi, -lo)


def q_squared(t, x, c):
    D = d+c
    return ((d*d+t*t/4)*(t*t*D*D+(U/2-t*x)**2)
            / ((d*d*t*t+U*U/4)*(D*D+(t/2-x)**2)))


def derivative(t, x, c):
    D = d+c
    return ((t/2-x)/(D*D+(t/2-x)**2)
            - t*(U/2-t*x)/(t*t*D*D+(U/2-t*x)**2))


def simpson(x, c, with_log=True):
    llo = lhi = dlo = dhi = 0
    for j in range(PANELS+1):
        t = F(j, PANELS)
        wt = 1 if j in (0, PANELS) else (4 if j % 2 else 2)
        if with_log:
            ll, lh = logq(q_squared(t, x, c))
            llo += wt*ll
            lhi += wt*lh
        dl, dh = fixed(derivative(t, x, c))
        dlo += wt*dl
        dhi += wt*dh
    # The proof uses the elementary cubic Taylor remainder bound
    # K/(45*N^4), without importing the sharper Simpson error theorem.
    log_error = F(256, 45*PANELS**4)
    derivative_error = F(512, 45*PANELS**4)
    rate = (F(llo, 6*PANELS*SCALE)-log_error,
            F(lhi, 6*PANELS*SCALE)+log_error)
    der = (F(dlo, 3*PANELS*SCALE)-derivative_error,
           F(dhi, 3*PANELS*SCALE)+derivative_error)
    return rate, der


def enc(q):
    q = F(q)
    return {"numerator": q.numerator, "denominator": q.denominator,
            "decimal_preview": float(q)}


checks, rate_certificates = {}, {}


def check(name, actual, relation, required):
    actual, required = F(actual), F(required)
    passed = {"<": actual < required, ">": actual > required,
              "=": actual == required}[relation]
    checks[name] = {"actual": enc(actual), "relation": relation,
                    "required": enc(required), "pass": passed}


for label, c, threshold in (("upper_contour", F(3, 20), F(-41, 1000)),
                            ("lower_contour", F(-1, 10), F(74, 1000)),
                            ("real_line", F(0), F(24, 1000))):
    rows = []
    radius = F(1, 2*CELLS)
    for k in range(CELLS):
        x = -1+F(2*k+1, 2*CELLS)
        rate, der = simpson(x, c)
        der_abs = max(abs(der[0]), abs(der[1]))
        upper = rate[1]+der_abs*radius+radius**2/(d+c)**2
        rows.append({"cell": k, "midpoint": enc(x),
                     "rate_at_midpoint": [enc(v) for v in rate],
                     "derivative_at_midpoint": [enc(v) for v in der],
                     "whole_cell_upper": enc(upper)})
    worst = max(rows, key=lambda row: F(row["whole_cell_upper"]["numerator"],
                                      row["whole_cell_upper"]["denominator"]))
    bound = F(worst["whole_cell_upper"]["numerator"],
              worst["whole_cell_upper"]["denominator"])
    check(label+"_rate", bound, "<", threshold)
    rate_certificates[label] = {"c": enc(c), "worst_cell": worst,
                                "cells": rows}

negative, _ = simpson(-Y, F(0))
positive, _ = simpson(Y, F(0))
check("negative_endpoint_rate", negative[0], ">", F(51, 2500))
check("positive_endpoint_rate", positive[1], "<", F(-1, 10))

derivative_rows = []
radius = (1-Y)/(2*CELLS)
for k in range(CELLS):
    x = -1+(1-Y)*F(2*k+1, 2*CELLS)
    _, der = simpson(x, F(0), with_log=False)
    lower = der[0]-2*radius/(d*d)
    derivative_rows.append({"cell": k, "midpoint": enc(x),
                            "whole_cell_lower": enc(lower)})
derivative_min = min(F(row["whole_cell_lower"]["numerator"],
                       row["whole_cell_lower"]["denominator"])
                     for row in derivative_rows)
check("negative_tail_derivative", derivative_min, ">", F(1, 25))

omega_upper = A*(F(logq(F(9, 5))[1], SCALE)-F(4, 5)
                 +F(121, 100)*F(logq(F(201, 121))[1], SCALE))
check("omega_star_upper", omega_upper, "<", F(10851, 10000))
check("positive_bump_endpoint", omega_upper+F(1, 3000), "<", F(543, 500))
check("bump_density_rate", F(-41, 1000)+F(3, 20)*F(543, 500)/A,
      "=", F(29, 1500))
check("bump_vs_endpoint_gap", F(51, 2500)-F(29, 1500), ">", F(1, 1000))
check("high_frequency_rate", F(74, 1000)-F(1, 10)*F(9, 4)/A,
      "<", F(-9, 1000))

v_squared = F(59657, 61952)
tail_rate = F(24, 1000)+(v_squared-1)/6
check("relative_finite_tail_rate", tail_rate-F(1, 50), "<", F(-1, 500))
check("far_factor_limit_squared", F(29696, 40241), "<", F(81, 100))
check("negative_halfline_monotonicity", 1+R+U/4, ">", F(7, 5)**2)
check("positive_tail_endpoint_comparison", R, ">", 2*Y)

# All t derivatives used by Simpson have the advertised uniform bounds.
# For x in [-1,Y], c in [-1/10,3/20], the four linear factors in
# the proof have the stated lower bounds, including the 4/5 bound.
check("numerator_minimum_squared", (U/2)**2*F(23, 20)**2 /
      (F(23, 20)**2+Y*Y), ">", F(4, 5)**2)
fourth = 6*((F(1, 2)/d)**4+(d/(U/2))**4
            +((F(7, 5)**2+1)/F(4, 5)**2)**2
            +(F(1, 2)/F(23, 20))**4)
check("log_fourth_derivative_bound", fourth, "<", 256)
# sqrt((7/5)^2+1) < 7/4 bounds the cubic numerator here.
check("slope_modulus_squared", F(7, 5)**2+1, "<", F(7, 4)**2)
derivative_fourth = (24*(U/2)*F(7, 4)**3/F(4, 5)**5
                     +24*F(1, 2)**4/F(23, 20)**5)
check("derivative_fourth_derivative_bound", derivative_fourth, "<", 512)

# A pole crossed by the upper contour for a spatial point already in |z|<1.
pole_a_squared = F(33, 25)**2+F(2, 5)**2
z_pole_squared = U/pole_a_squared
check("crossed_resolvent_spatial_radius_squared", z_pole_squared, "<", 1)
check("crossed_resolvent_height", F(7, 100), "<", F(3, 20))

certificate = {
    "purpose": "Auxiliary phase-sensitive rates and exact pole geometry for L709",
    "arithmetic": "Integer and Fraction arithmetic; previews do not decide checks",
    "parameters": {"scale": SCALE, "log_series_terms": TERMS,
                   "simpson_panels": PANELS, "cells": CELLS},
    "proof_obligations": [
        "L709's derivative and real-halfline reduction arguments",
        "Uniform finite-product Riemann comparisons and angular neighborhoods",
        "Contour shifts, Fourier pairing, both endpoint tails and finite moments",
        "The fixed L703 profile and its exact Fourier identity",
    ],
    "checks": checks,
    "rate_certificates": rate_certificates,
    "negative_tail_derivative_cells": derivative_rows,
    "endpoint_enclosures": {"negative": [enc(v) for v in negative],
                             "positive": [enc(v) for v in positive]},
    "failures": [name for name, row in checks.items() if not row["pass"]],
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2)+"\n")
for name in ("upper_contour_rate", "lower_contour_rate", "real_line_rate",
             "negative_endpoint_rate", "negative_tail_derivative",
             "relative_finite_tail_rate", "crossed_resolvent_spatial_radius_squared"):
    row = checks[name]
    print(f"{name}: actual {row['actual']['decimal_preview']:.12g} "
          f"{row['relation']} required {row['required']['decimal_preview']:.12g}; "
          f"pass={row['pass']}")
print(f"Checks: {len(checks)}; failures: {certificate['failures']}; certificate: {path}")
if certificate["failures"]:
    raise SystemExit(1)
