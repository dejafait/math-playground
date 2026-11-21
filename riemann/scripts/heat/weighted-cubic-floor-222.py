#!/usr/bin/env python3
"""One fixed-interval test. Exact algebra and rational bounds; no moment evaluator."""

from fractions import Fraction as F
from hashlib import sha256
from math import factorial
from pathlib import Path
import json

# Tiny exact sparse-polynomial arithmetic keeps this certificate self-contained.
NAMES = ("p", "q", "b", "r", "h", "s7", *[f"y{j}" for j in range(1, 8)])
ZERO_POWER = (0,) * len(NAMES)


class Poly:
    def __init__(self, value=0):
        if isinstance(value, Poly):
            self.terms = dict(value.terms)
        elif isinstance(value, dict):
            self.terms = {key: F(val) for key, val in value.items() if val}
        else:
            self.terms = {ZERO_POWER: F(value)} if value else {}

    @staticmethod
    def var(name):
        powers = list(ZERO_POWER)
        powers[NAMES.index(name)] = 1
        return Poly({tuple(powers): F(1)})

    def __add__(self, other):
        out = dict(self.terms)
        for key, val in Poly(other).terms.items():
            out[key] = out.get(key, F(0)) + val
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({key: -val for key, val in self.terms.items()})

    def __sub__(self, other):
        return self + (-Poly(other))

    def __rsub__(self, other):
        return Poly(other) - self

    def __mul__(self, other):
        out = {}
        for a, ca in self.terms.items():
            for b, cb in Poly(other).terms.items():
                key = tuple(x+y for x, y in zip(a, b))
                out[key] = out.get(key, F(0)) + ca * cb
        return Poly(out)

    __rmul__ = __mul__

    def __truediv__(self, value):
        return self * (1 / F(value))

    def __eq__(self, other):
        return self.terms == Poly(other).terms

    def evaluate(self, values):
        total = F(0)
        for powers, coeff in self.terms.items():
            for name, degree in zip(NAMES, powers):
                if degree:
                    coeff *= F(values[name]) ** degree
            total += coeff
        return total

    def __str__(self):
        if not self.terms:
            return "0"
        pieces = []
        for powers, coeff in sorted(self.terms.items(), reverse=True):
            monomial = "*".join(name if power == 1 else f"{name}^{power}"
                                for name, power in zip(NAMES, powers) if power)
            pieces.append(str(coeff) + ("*" + monomial if monomial else ""))
        return " + ".join(pieces)


def solve(matrix, rhs):
    a = [[F(z) for z in row] + [F(value)] for row, value in zip(matrix, rhs)]
    n = len(a)
    for i in range(n):
        pivot = next(j for j in range(i, n) if a[j][i])
        a[i], a[pivot] = a[pivot], a[i]
        den = a[i][i]
        a[i] = [z/den for z in a[i]]
        for j in range(n):
            if j != i:
                coeff = a[j][i]
                a[j] = [x-coeff*y for x, y in zip(a[j], a[i])]
    return [row[-1] for row in a]


def det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    return sum((-1)**j * matrix[0][j] * det([row[:j]+row[j+1:] for row in matrix[1:]])
               for j in range(len(matrix)))

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "scripts/heat/low-time-h2-uniform-195.json"
OUTPUT = ROOT / "scripts/heat/weighted-cubic-floor-222.json"
source_bytes = SOURCE.read_bytes()
data = json.loads(source_bytes)
checks = {}


def check(name, condition):
    checks[name] = bool(condition)


def rat(value):
    return str(value)


def exp_bounds(x, n=100):
    """Positive Taylor sum; bound the full tail by its largest term ratio."""
    x = F(x)
    assert 0 <= x < n + 2
    term = F(1)
    total = term
    for j in range(1, n + 1):
        term *= x / j
        total += term
    tail = term * x / (n + 1) / (1 - x / (n + 2))
    return total, total + tail


# Read every load-bearing saved mass upper bound, including closed endpoints.
mass_records = []
check("256_panels", len(data["panels"]) == 256)
for i, panel in enumerate(data["panels"]):
    lo = F(panel["lambda"]["lower"])
    hi = F(panel["lambda"]["upper"])
    ml = F(panel["moments"]["0"]["lower"])
    mu = F(panel["moments"]["0"]["upper"])
    check(f"mass_panel_{i}", panel["index"] == i and
          lo == F(i, 5120) and hi == F(i + 1, 5120) and 0 < ml <= mu < F(1, 2))
    mass_records.append({"index": i, "lambda": [rat(lo), rat(hi)],
                         "mass_lower": rat(ml), "mass_upper": rat(mu)})
max_index = max(range(len(mass_records)), key=lambda i: F(mass_records[i]["mass_upper"]))
mass_max = mass_records[max_index]["mass_upper"]
check("mass_upper_lt_0499", F(mass_max) < F(499,1000))
pi_lo = F(data["pi"]["lower"])
pi_hi = F(data["pi"]["upper"])
check("pi_coarse", 3 < pi_lo < pi_hi < 4)

# These are scalar bounds only, not a new integration or moment implementation.
e_lo, e_hi = exp_bounds(1)
check("pi_e_range", pi_lo * e_lo > F(17, 2) and pi_hi * e_hi < F(43, 5))
big_lo, big_hi = exp_bounds(F(167, 20))
check("exp_167_over_20_lt_4500", big_hi < 4500)
gauss_lo, gauss_hi = exp_bounds(F(5, 2))
check("exp_5_over_2_lt_15", gauss_hi < 15)
kernel_floor = F(476, 4500)
density_floor = F(1, 40)
check("kernel_floor_gt_one_tenth", kernel_floor > F(1, 10))
check("density_floor_paid", F(1, 8) * kernel_floor / F(1, 2) > density_floor)
length = F(3, 16)
legendre_norm = length**7 / 2800
epsilon = density_floor * legendre_norm

# Full three-row logarithmic reduction. p,q are ratios c0/c2,c1/c2.
p, q, b, r, h = [Poly.var(name) for name in ("p", "q", "b", "r", "h")]
S = {1: h, 2: b, 3: r}
for j in (4, 5, 6):
    S[j] = -p * S[j - 2] - q * S[j - 1]
d = [p, q, Poly(1)]
bn = {n: sum(d[i] * d[j] for i in range(3) for j in range(3)
             if i + j == n - 2) for n in range(2, 7)}
rows = [sum(d[j] * S[i + j + 2] for j in range(3)) for i in range(3)]
check("all_three_null_rows", all(row == 0 for row in rows))
beta = (-2 * sum(n * (2 * n + 1) * bn[n] * S[n + 1] for n in range(2, 6))
                + 4 * sum(n * bn[n] * sum(S[a] * S[n + 1 - a] for a in range(2, n))
                          for n in range(2, 7)))
s7 = Poly.var("s7")
Ss = {**S, 7: s7}
full_flux = sum(bn[n] * (-2 * n * (2 * n + 1) * Ss[n + 1]
                      + 4 * n * sum(Ss[a] * Ss[n + 1 - a] for a in range(1, n + 1)))
                         for n in range(2, 7))
check("all_row_flux", full_flux - (-156 * s7 + beta) == 0)

# Independently extract every finite-log coefficient, including y7's exact sign.
y = [Poly(1), *[Poly.var(f"y{j}") for j in range(1,8)]]
qraw = [(-1)**j * y[j] / factorial(2 * j) for j in range(8)]
rawS = {n: Poly(0) for n in range(1, 8)}
for n in range(1, 8):
    rawS[n] = -n * qraw[n] - sum(rawS[k] * qraw[n-k] for k in range(1, n))
poly = [Poly(0), *qraw[1:]]
power = [Poly(1)] + [Poly(0) for _ in range(7)]
logpoly = [Poly(0) for _ in range(8)]
for k in range(1, 8):
    power = [sum(power[j] * poly[n-j] for j in range(n+1)) for n in range(8)]
    logpoly = [z + (-1)**(k+1) * coeff / k for z, coeff in zip(logpoly, power)]
for n in range(1, 8):
    check(f"finite_log_{n}", rawS[n] + n * logpoly[n] == 0)
top_key = next(iter(y[7].terms))
check("seventh_moment_coefficient", rawS[7].terms[top_key] == F(7, factorial(14)))
check("flux_scale", F(156 * 7, factorial(14)) == F(6, factorial(12)))

# The one diagnostic law has density exp(-10u^2)/Z on u>=0.
# Its exact moments follow by one integration-by-parts recurrence.
yg = [F(factorial(2*j), factorial(j) * 40**j) for j in range(8)]
sub = {f"y{j}": yg[j] for j in range(1, 8)}
Sg = [rawS[n].evaluate(sub) for n in range(1, 8)]
check("gaussian_log_rows", Sg == [F(1, 40), 0, 0, 0, 0, 0, 0])
W = [[yg[i+j+1] for j in range(3)] for i in range(3)]
v = yg[4:7]
sol = solve(W, v)
projection = sum(a*b for a,b in zip(v, sol))
delta_g = yg[7] - projection
pc = [-z for z in sol] + [F(1)]
Pg = " + ".join(f"{pc[j]}*x^{j}" for j in range(4))
orthogonality = [sum(pc[j] * yg[j+i+1] for j in range(4))
                 for i in range(3)]
norm = sum(pc[i]*pc[j]*yg[i+j+1] for i in range(4) for j in range(4))
check("gaussian_all_three_orthogonalities", orthogonality == [0, 0, 0])
check("gaussian_norm", delta_g == norm == F(63, 16000000))
check("gaussian_raw_block_pd", all(det([row[:i] for row in W[:i]]) > 0 for i in range(1,4)))
check("gaussian_density_floor", F(129,260) < F(1,2) and F(1,30) > density_floor)
gap = F(str(delta_g)) - epsilon
ratio = F(str(delta_g)) / epsilon
check("fixed_floor_insufficient_for_relaxation", gap > 0 and ratio > 50000)

failures = [name for name, value in checks.items() if not value]
result = {
    "scope": "one fixed x interval [1/16,1/4]; exact conditional flux bridge and a sufficient-floor stop; no actual contact/sign claim",
    "status": "passed" if not failures else "failed",
    "failures": failures, "checks": checks,
    "development_note": "An initial invocation stopped at a missing sympy import before calculating or writing evidence. This final producer uses only Python standard-library exact rational arithmetic.",
    "source": {"path": str(SOURCE.relative_to(ROOT)), "sha256": sha256(source_bytes).hexdigest(),
               "use": "only saved mass upper bounds and pi enclosure, with L917 arithmetic qualification",
               "all_mass_records": mass_records, "maximum_upper_index": max_index,
               "maximum_upper": mass_max, "required_mass_upper": "1/2",
               "pi": [rat(pi_lo),rat(pi_hi)]},
    "exponentials": {"method": "N=100 positive Taylor sum; tail t101/(1-x/102)",
                     "e": [rat(e_lo),rat(e_hi)],
                     "exp_167_over_20": [rat(big_lo),rat(big_hi)],
                     "exp_5_over_2": [rat(gauss_lo),rat(gauss_hi)]},
    "floor": {"kernel_at_half_lower": rat(kernel_floor), "weighted_density_lower": rat(density_floor),
              "interval_length": rat(length), "monic_cubic_lebesgue_minimum": rat(legendre_norm),
              "epsilon": rat(epsilon)},
    "algebra": {"ratio_vector": [str(z) for z in d], "all_null_rows": [str(z) for z in rows],
                "S4_S5_S6": [str(S[j]) for j in (4,5,6)], "b2_through_b6": [str(bn[n]) for n in range(2,7)],
                "B_divided_by_c2_squared": str(beta), "flux_divided_by_c2_squared": str(full_flux),
                "S7_raw": str(rawS[7]), "required_y7": "14!/7 * (beta/156 + sum_{k=1}^6 S_k q_{7-k})",
                "required_norm": "D=required_y7-v^T W^{-1}v; Phi=-(6c2^2/12!)(delta-D)"},
    "diagnostic": {"law": "exp(-10u^2)du/Z on u>=0, not actual theta", "c": [0,0,1],
                   "Z_upper": "129/260", "weighted_density_lower": "1/30",
                   "moments_0_through_7": [str(z) for z in yg], "S1_through_S7": [str(z) for z in Sg],
                   "W": [[str(z) for z in row] for row in W],
                   "v": [str(z) for z in v], "monic_minimizer": str(Pg),
                   "orthogonality": [str(z) for z in orthogonality],
                   "projection": str(projection), "required_norm": str(delta_g),
                   "actual_norm": str(delta_g), "fixed_floor": rat(epsilon),
                   "unpaid_floor_gap": rat(gap), "required_over_floor": rat(ratio),
                   "flux": "0", "excluded_actual_information": "exact theta kernel; in particular L917 S2>0 is not satisfied"},
    "decision": "The sufficient comparison D<=epsilon fails in the explicitly enlarged floor-plus-contact-row class. Actual-theta D<=epsilon is unpaid; stop without refinement."
}
OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
print("status:", result["status"], "; checks:", len(checks), "; failures:", failures)
print("full-band M0 upper: <0.499; required: <=0.5; exact maximum saved:", max_index)
print("fixed cubic floor:", epsilon, "(~", float(epsilon), ")")
print("diagnostic required norm:", delta_g, "; flux: 0; actual-theta threshold: unpaid")
print("required/floor:", float(ratio), "; certificate:", OUTPUT.relative_to(ROOT))
if failures:
    raise SystemExit(1)
