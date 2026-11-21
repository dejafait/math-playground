#!/usr/bin/env python3
"""Fixed-law complete-expression certificate; standard-library rational intervals."""
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import json


class I:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi
        # Outward dyadic rounding controls certificate size; all arithmetic
        # before each rounding is exact. This is not floating point.
        scale = 2**192
        low = self.lo.numerator*scale // self.lo.denominator
        high = -((-self.hi.numerator*scale) // self.hi.denominator)
        self.lo, self.hi = F(low, scale), F(high, scale)

    def __add__(self, other):
        other = box(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -box(other)

    def __rsub__(self, other):
        return box(other) + -self

    def __mul__(self, other):
        other = box(other)
        values = [x*y for x in (self.lo, self.hi) for y in (other.lo, other.hi)]
        return I(min(values), max(values))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = box(other)
        assert other.lo > 0 or other.hi < 0, "division interval contains zero"
        return self * I(1/other.hi, 1/other.lo)

    def __rtruediv__(self, other):
        return box(other) / self

    def __pow__(self, n):
        if n < 0:
            return 1 / self**(-n)
        value = I(1)
        for _ in range(n):
            value = value * self
        return value


def box(value):
    return value if isinstance(value, I) else I(value)


def atan_bounds(q, terms):
    x = F(1, q)
    partial = sum((-1)**j * x**(2*j+1)/(2*j+1) for j in range(terms))
    adjacent = partial + (-1)**terms * x**(2*terms+1)/(2*terms+1)
    return I(min(partial, adjacent), max(partial, adjacent))


def subset(interval, lo, hi):
    return F(lo) < interval.lo and interval.hi < F(hi)


def overlap(a, b):
    return max(a.lo, b.lo) <= min(a.hi, b.hi)


def encode(value):
    if isinstance(value, I):
        # Fractions are the evidence; decimals are outward-rounded summaries.
        scale = 10**12
        low = value.lo.numerator*scale // value.lo.denominator
        high = -((-value.hi.numerator*scale) // value.hi.denominator)
        return {"lo": str(value.lo), "hi": str(value.hi),
                "decimal_outer": [str(F(low, scale)), str(F(high, scale))]}
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value


pi = 16*atan_bounds(5, 32) - 4*atan_bounds(239, 8)
scale = 10**50
sqrt_floor = isqrt(2*scale*scale)
sqrt2 = I(F(sqrt_floor, scale), F(sqrt_floor+1, scale))
t = pi**2/128
alpha = [-t, -9*t]
sigma = F(9, 8)
# These are G_*(8z)'s coefficients, retaining all (2n)! and 8^n factors.
g = [8**n * F(1+3**(2*n)+4*2**(2*n), 2*factorial(2*n)) for n in range(6)]
inverse = []
for n in range(6):
    inverse.append((int(n == 0)-sum(g[j]*inverse[n-j] for j in range(1, n+1)))/g[0])
P = [9*t**2, 10*t, I(1)]
P2 = [sum(P[j]*P[n-j] for j in range(3) if 0 <= n-j < 3) for n in range(5)]
beta = {m: sum(P2[j]*inverse[m+2-j] for j in range(min(4, m+2)+1))
        for m in range(-2, 4)}


def T(x):
    return sum(beta[m]*x**m for m in beta)


def Tprime(x):
    return sum(m*beta[m]*x**(m-1) for m in beta)


d = [(2+sqrt2/2)/(2*pi), -27*(2-sqrt2/2)/(2*pi)]
weights = [d[0]*t**3, -d[1]*(9*t)**3]
h = [-T(x)/x**3 for x in alpha]
K12 = (h[0]-h[1])/(alpha[0]-alpha[1])
Mdiag = [3*T(x)/x**4-Tprime(x)/x**3 for x in alpha]
Kdiag = [Mdiag[j]+1/(d[j]*alpha[j]**3) for j in range(2)]
K = [[Kdiag[0], K12], [K12, Kdiag[1]]]
M = [[Mdiag[0], K12], [K12, Mdiag[1]]]
det = Mdiag[0]*Mdiag[1]-K12**2
second_pivot = det/Mdiag[0]
det_I_CS = -weights[0]*weights[1]*det
# Finite bounds used in the analytic contour proof, written in the lemma.
cosh1_upper = sum(F(1, factorial(2*j)) for j in range(4)) + F(1, factorial(8))*F(90, 89)
u = pi-3
sin3_lower = u-u**3/6
checks = {
    "pi_in_3_14_to_22_over_7": subset(pi, F(157,50), F(22,7)),
    "sqrt2_bounds_by_integer_squares": sqrt_floor**2 < 2*scale**2 < (sqrt_floor+1)**2,
    "t_between_0_and_2_over_25": subset(t, 0, F(2,25)),
    "two_negative_distinct_interior_nodes": alpha[1].lo > -1 and alpha[1].hi < alpha[0].lo < alpha[0].hi < 0,
    "next_cosh2_root_outside_w9": 25*pi.lo**2/16 > 9,
    "cosh_plus2_roots_outside_w9": pi.lo**2 > 9,
    "cosh1_less_5_over_3": cosh1_upper < F(5,3),
    "sin3_greater_1_over_10": sin3_lower.lo > F(1,10),
    "near_imaginary_contour_angle_gap_less_1_over_3": 2*pi.hi-F(299,50) < F(1,3),
    "near_imaginary_contour_v_exceeds_299_over_100": F(299,100)**2 < 9-F(1,100),
    "contour_P_upper_less_5_over_2": (sigma+F(2,25))*(sigma+F(18,25)) < F(5,2),
    "M_b_at_m_sigma_1_over_125_less_337": 125*(1+F(18,25)/sigma)**2 < 337,
    "inverse_series_local_convolution_exact": all(sum(g[j]*inverse[n-j] for j in range(n+1)) == int(n==0) for n in range(6)),
    "complete_residue_signs": d[0].lo > 0 and d[1].hi < 0,
    "positive_diagonal_weights": all(w.lo > 0 for w in weights),
    "diagonal_cancellation_consistent": all(overlap(Kdiag[j]+(1 if j==0 else -1)/weights[j], Mdiag[j]) for j in range(2)),
    "M11_between_5063_and_5064": subset(Mdiag[0], 5063, 5064),
    "M12_between_0062_and_0063": subset(K12, F(62,1000), F(63,1000)),
    "M22_between_minus_0454_and_minus_0453": subset(Mdiag[1], F(-454,1000), F(-453,1000)),
    "det_between_minus_2294_and_minus_2293": subset(det, -2294, -2293),
    "second_LDL_pivot_strictly_negative": second_pivot.hi < 0,
    "det_I_CS_strictly_positive": det_I_CS.lo > 0,
}
certificate = {
    "target": "mu=(delta_1+delta_3)/2+2delta_2; r=3,R=8,k=2,sigma=9/8",
    "method": "Exact analytic complete-tail identity; rational intervals, no series truncation at nodes",
    "pi_method": "Machin identity with adjacent alternating sums: atan(1/5)32, atan(1/239)8",
    "pi": pi, "sqrt2": sqrt2, "t": t, "alpha": alpha,
    "G8_coefficients_0_to_5": g, "inverse_local_coefficients_0_to_5": inverse,
    "P_squared_coefficients": P2, "beta_minus2_to3": beta,
    "residues": d, "E_squared_weights": weights,
    "h3_at_nodes_complete": h, "K_complete": K,
    "residual_positive_diagonal_congruence_M": M,
    "det_M": det, "LDL_pivots_M": [Mdiag[0], second_pivot],
    "det_I_CS": det_I_CS,
    "analytic_bounds": {"sigma": sigma, "m_sigma": F(1,125), "M_b": 337,
                        "cosh1_upper": cosh1_upper, "sin3_lower": sin3_lower,
                        "G_growth": "3 exp(3 sqrt(abs(w)))"},
    "actual_inertia_J_minus_Q": [1,0,1], "required_inertia_J": [1,0,1],
    "checks": checks, "failures": [name for name, okay in checks.items() if not okay],
    "scope": "One model only. Analytic root enumeration and complete-tail justification are in L784; no actual-Xi sign or generic implication.",
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(encode(certificate), indent=2)+"\n")
print(f"Checks: {sum(checks.values())}/{len(checks)}; failures: {certificate['failures']}")
print("Certified M11 in (5063,5064), M12 in (.062,.063), M22 in (-.454,-.453)")
print("Certified det(M) in (-2294,-2293); LDL pivots (+,-)")
print("Actual inertia(J-Q)=(1,0,1); required inertia(J)=(1,0,1): matches for this model")
print(f"Full certificate: {path}")
assert all(checks.values()), certificate['failures']
