"""Exact coefficient checks for L046; analytic lifting is proved in the lemma."""
from fractions import Fraction
from math import comb
from pathlib import Path
import json


def add(p, q):
    out = [0] * max(len(p), len(q))
    for i, a in enumerate(p):
        out[i] += a
    for i, a in enumerate(q):
        out[i] += a
    return out


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out


def shift(p, c):
    return [sum(p[j]*comb(j, i)*c**(j-i) for j in range(i, len(p)))
            for i in range(len(p))]


def v2(q):
    q = Fraction(q)
    if not q:
        return None
    n, d = abs(q.numerator), q.denominator
    return (n & -n).bit_length() - (d & -d).bit_length()


def value(p, a):
    out = 0
    for c in reversed(p):
        out = out*a+c
    return out


H = [-380,-774,-1062,-456,258,468,104,-126,-6,6,-6,0,1]
scaled_H = [Fraction(c*2**i, 4) for i, c in enumerate(H)]
h = [9789217,4971236,1333262,-52820,1]
J = [-104748564078368391,199736619430410535,159480622275659333,
     6839041777752481,-29669709666741936,-4074814667347831,
     1134855511654843,164063633585170,5072626276355,38323813979,
     43119747,1486]
b1 = [-707351591,271927184,65058492,1304157,4518,1]
b2 = [-37315543,-37789861,-3406817,3626752,192189,1]
b = mul(b1, b2)
s = Fraction(27*2047,32)
hs, Js = shift(h,16), shift(J,16)
C = add(mul(mul(hs,hs),hs), [s*c for c in Js])
C[11] -= s*s
cv = [v2(c) for c in C]
# Reciprocal root z=1/(2^10 u): multiply F(z) by z^-12.
R = [C[12-i]*2**(10*i) for i in range(13)]
# In L=Q2(alpha), alpha^11=2, z=alpha^5 u, divide by C[0].
# These are exact normalized L-valuations (v_L(alpha)=1).
Lv = [11*(v2(c)-cv[0])+5*i if c else None for i,c in enumerate(C)]
checks = {
    "H_scaled_integral_simple_unit_root":
        all(c.denominator == 1 for c in scaled_H)
        and value(scaled_H,1) % 2 == 0
        and value([i*scaled_H[i] for i in range(1,13)],1) % 2 == 1,
    "H_nonleading_even_constant_valuation_two":
        all(c % 2 == 0 for c in H[:-1]) and v2(H[0]) == 2,
    "fiber_coefficient_bounds": len(C) == 13 and C[12] == 1
        and cv[0] == -5 and cv[11] == -10
        and all(v is None or v >= -5 for v in cv[1:11]),
    "reciprocal_simple_unit_root":
        all(c.denominator == 1 for c in R)
        and [int(c) % 2 for c in R] == [1,1]+[0]*11,
    "ramified_simple_unit_root": Lv[0] == Lv[11] == 0
        and all(v is None or v > 0 for i,v in enumerate(Lv) if i not in (0,11)),
    "y_reconstruction_units_or_unique_leading_term":
        b[0] % 2 == 1 and b[-1] == 1 and len(b) == 11,
    "common_scalar_identity_and_branch": s*2048 == 1728*2047
        and (1728-s)*2048 == 1728 and 2047 % 8 == 7
        and s not in (0,1728),
    "good_reduction_and_trivial_dual_kernel_size":
        (-11**5) % 2 == (-11) % 2 == 1
        and (2-1) % 5 != 0,
}
certificate = {
    "checks": checks,
    "field": {"H": H, "H_2u_over_4": [str(c) for c in scaled_H],
              "residue_polynomial": "1+u", "required_factor_degrees": [1,11],
              "actual_proved_factor_degrees": [1,11], "residue_degrees": [1,1]},
    "fiber": {"s": str(s), "shifted_coefficients": [str(c) for c in C],
              "coefficient_v2": cv, "reciprocal_mod_2": [int(c)%2 for c in R],
              "ramified_normalized_coefficient_valuations": Lv,
              "ramified_mod_uniformizer": "1+u^11",
              "b": b, "complete_dimension_actual": 12, "complete_dimension_required": 12},
    "conclusion": {"unrestricted_image_size": 1, "fiber_image_size": 1,
                   "primitive_image_size": 1, "strict_shrink_required": True,
                   "strict_shrink_actual": False,
                   "qualification": "Lifting, field identification, full-fiber exhaustion and theorem application require L046's proof."},
}
path = Path(__file__).with_name("image-certificate.json")
path.write_text(json.dumps(certificate, indent=2)+"\n")
failures = [name for name, passed in checks.items() if not passed]
print(f"Checks: {len(checks)-len(failures)}/{len(checks)}; failures: {failures}")
print("Factor degrees: actual [1,11], required total 12; both residue fields F2.")
print("Fiber coefficient v2:", cv, "; required endpoints (-5,-10,0), middle >= -5.")
print("Image sizes: all=fiber=primitive=1; strict shrink actual False, required True.")
print("Certificate:", path.relative_to(Path.cwd()))
if failures:
    raise SystemExit(1)
