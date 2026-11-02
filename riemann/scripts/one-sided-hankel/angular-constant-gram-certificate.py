"""Exact Gaussian-rational residues for the C645o anchor Gram witness.

No angular quadrature or floating point arithmetic enters a check.
"""
from dataclasses import dataclass
from fractions import Fraction as F
import json
from pathlib import Path


@dataclass(frozen=True)
class G:
    re: F
    im: F = F(0)

    @staticmethod
    def cast(value):
        return value if isinstance(value, G) else G(F(value))

    def __add__(self, other):
        other = G.cast(other)
        return G(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-G.cast(other))

    def __rsub__(self, other):
        return G.cast(other) - self

    def __mul__(self, other):
        other = G.cast(other)
        return G(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def conjugate(self):
        return G(self.re, -self.im)

    def abs_squared(self):
        return self.re * self.re + self.im * self.im

    def __truediv__(self, other):
        other = G.cast(other)
        den = other.abs_squared()
        if not den:
            raise ZeroDivisionError("Gaussian-rational denominator is zero")
        num = self * other.conjugate()
        return G(num.re / den, num.im / den)

    def __rtruediv__(self, other):
        return G.cast(other) / self


n = 12
x = G(F(-5, 4))
R = F(11, 8)
U = R * R
eta = F(1, 100)
a = x + G(F(0), F(1, 2))
ts = [F(j, n) for j in range(1, n)]


def W(v, z):
    if v == x:
        return G(F(1))
    out = x / v
    for t in ts:
        out *= (x - t * z) / (v - t * z)
        out *= (U * z - t * v) / (U * z - t * x)
    return out


def Wsharp(v, z):
    if v == x:
        return G(F(1))
    vb = v.conjugate()
    out = x / vb
    for t in ts:
        out *= (x * z - t) / (vb * z - t)
        out *= (U - t * vb * z) / (U - t * x * z)
    return out


def residue_W(v, j):
    t = ts[j]
    p = t * x / U
    out = (x / v) * ((x - t * p) / (v - t * p)) * (t * (x - v) / U)
    for k, s in enumerate(ts):
        if k != j:
            out *= (x - s * p) / (v - s * p)
            out *= (U * p - s * v) / (U * p - s * x)
    return p, out


def residue_Wsharp(v, j):
    vb = v.conjugate()
    t = ts[j]
    q = t / vb
    out = (x / vb) * ((x * q - t) / vb) * ((U - t * vb * q) / (U - t * x * q))
    for k, s in enumerate(ts):
        if k != j:
            out *= (x * q - s) / (vb * q - s)
            out *= (U - s * vb * q) / (U - s * x * q)
    return q, out


def integral(v, w):
    rows = [{"kind": "zero", "j": 0, "pole": G(F(0)),
             "residue": x * x / (v * w.conjugate())}]
    if v != x:
        for j in range(n - 1):
            p, res = residue_W(v, j)
            rows.append({"kind": "common", "j": j + 1,
                         "pole": p, "residue": res * Wsharp(w, p) / p})
    if w != x:
        for j in range(n - 1):
            q, res = residue_Wsharp(w, j)
            rows.append({"kind": "reflected", "j": j + 1,
                         "pole": q, "residue": W(v, q) * res / q})
    return sum((row["residue"] for row in rows), G(F(0))), rows


Iax, rows_ax = integral(a, x)
Ixa, rows_xa = integral(x, a)
Iaa, rows_aa = integral(a, a)
Kxx = 1 / (U - x * x)
Kxa = Ixa / (U - x * a.conjugate())
Kaa = Iaa / (U - a.abs_squared())
energy = Kxx + Kaa + Kxa + Kxa.conjugate()
determinant = Kxx * Kaa - Kxa.abs_squared()

# Termwise directed enclosures form a compact fully inspectable certificate.
# This certificate uses Iax, then conjugates and divides to obtain Kxa.
D = 10**9


def directed(value):
    floor_value = (value.numerator * D) // value.denominator
    return {"lower_numerator": floor_value,
            "upper_numerator": floor_value + 1, "denominator": D}


compact = []
for row in rows_ax:
    r = row["residue"]
    compact.append({"kind": row["kind"], "j": row["j"],
                    "real": directed(r.re), "imaginary": directed(r.im)})
sum_re_lo = F(sum(v["real"]["lower_numerator"] for v in compact), D)
sum_re_hi = F(sum(v["real"]["upper_numerator"] for v in compact), D)
sum_im_lo = F(sum(v["imaginary"]["lower_numerator"] for v in compact), D)
sum_im_hi = F(sum(v["imaginary"]["upper_numerator"] for v in compact), D)

# U-x*conj(a)=21/64-5i/8, so Re Kxa is
# [(21/64) Re Iax + (5/8) Im Iax]/[(21/64)^2+(5/8)^2].
alpha = F(21, 64)
beta = F(5, 8)
den = alpha * alpha + beta * beta
real_lo = (alpha * sum_re_lo + beta * sum_im_lo) / den
real_hi = (alpha * sum_re_hi + beta * sum_im_hi) / den

checks = {
    "n_at_least_5": n >= 5,
    "M_le_n_over_3": 2 <= F(n, 3),
    "a_on_anchor_line": a.re == x.re,
    "distinct_poles": a != x,
    "a_has_required_clearance": a.abs_squared() < (R - eta)**2,
    "anchor_has_required_clearance": x.abs_squared() < (R - eta)**2,
    "all_residue_poles_inside": all(row["pole"].abs_squared() < 1
                                     for rows in (rows_ax, rows_xa, rows_aa) for row in rows),
    "hermitian_means_independently_replayed": Ixa == Iax.conjugate(),
    "diagonal_mean_real": Iaa.im == 0,
    "all_compact_real_enclosures": all(F(r["real"]["lower_numerator"], D) <= row["residue"].re
        < F(r["real"]["upper_numerator"], D) for r, row in zip(compact, rows_ax)),
    "all_compact_imaginary_enclosures": all(F(r["imaginary"]["lower_numerator"], D) <= row["residue"].im
        < F(r["imaginary"]["upper_numerator"], D) for r, row in zip(compact, rows_ax)),
    "negative_entry_lower": F(-141, 1000) < real_lo <= Kxa.re,
    "negative_entry_upper": Kxa.re < real_hi < F(-140, 1000),
    "two_pole_energy_between_5757_and_5758_over_1000": F(5757, 1000) < energy.re < F(5758, 1000),
    "two_pole_energy_real": energy.im == 0,
    "gram_determinant_positive": determinant.im == 0 and determinant.re > 0,
}


def encode(value):
    if isinstance(value, F):
        return {"numerator": str(value.numerator), "denominator": str(value.denominator)}
    if isinstance(value, G):
        return {"real": encode(value.re), "imaginary": encode(value.im)}
    if isinstance(value, dict):
        return {key: encode(val) for key, val in value.items()}
    if isinstance(value, list):
        return [encode(val) for val in value]
    return value


certificate = {
    "status": "EXACT_RATIONAL_RESIDUE_CERTIFICATE",
    "parameters": {"n": n, "x": x, "a": a, "R": R, "eta": eta, "M": 2},
    "residues_Iax": rows_ax, "residues_Ixa": rows_xa, "residues_Iaa": rows_aa,
    "compact_anchor_residue_enclosures": compact,
    "compact_totals": {"real_lower": sum_re_lo, "real_upper": sum_re_hi,
                       "imaginary_lower": sum_im_lo, "imaginary_upper": sum_im_hi,
                       "Kxa_real_lower": real_lo, "Kxa_real_upper": real_hi},
    "exact_values": {"Iax": Iax, "Ixa": Ixa, "Iaa": Iaa,
                     "Kxx": Kxx, "Kxa": Kxa, "Kaa": Kaa,
                     "two_pole_energy": energy, "gram_determinant": determinant},
    "readable_bounds": {
        "Re_Kxa": "-141/1000 < Re K(x,x+i/2) < -140/1000",
        "two_pole_energy": "5757/1000 < mean ||q||_2^2 < 5758/1000",
        "required_uniform_squared_rate": "c^2 exp(-n/16), c>0 independent of n,Z,r",
        "conclusion": "Entrywise real positivity fails; uniform angular lower bound remains open.",
    },
    "checks": checks,
    "failures": [key for key, passed in checks.items() if not passed],
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(encode(certificate), indent=2) + "\n")
print("Exact residue checks:", len(checks), "; failures:", certificate["failures"])
print("Actual certified Re K(x,x+i/2): (-141/1000,-140/1000); positivity would require >=0")
print("Two-pole energy: (5757/1000,5758/1000); no asymptotic bound or countersequence")
print("Required uniform squared rate: c^2 exp(-n/16)")
print("Full certificate:", path)
if certificate["failures"]:
    raise SystemExit(1)
