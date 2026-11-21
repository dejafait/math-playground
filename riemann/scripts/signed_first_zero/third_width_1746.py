"""One fixed rational enclosure for C033k; no point sampling or refinement.

The external zero/count inputs and analytic arguments are not verified here.
Each of 16 by 16 parameter rectangles covers a continuum. All arithmetic is
exact Fraction arithmetic; decimal values are explicitly labelled previews.
"""

from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json


class I:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = F(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = other if isinstance(other, I) else I(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -other if isinstance(other, I) else self + -F(other)

    def __mul__(self, other):
        other = other if isinstance(other, I) else I(other)
        products = [a * b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return I(min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = other if isinstance(other, I) else I(other)
        assert other.lo > 0 or other.hi < 0
        return self * I(1 / other.hi, 1 / other.lo)

    def square(self):
        if self.lo <= 0 <= self.hi:
            return I(0, max(self.lo**2, self.hi**2))
        return I(min(self.lo**2, self.hi**2), max(self.lo**2, self.hi**2))

    def hull(self, other):
        return I(min(self.lo, other.lo), max(self.hi, other.hi))

    def positive_power(self, n):
        assert self.lo >= 0
        return I(self.lo**n, self.hi**n)


def rational(x):
    return {"numerator": str(x.numerator), "denominator": str(x.denominator),
            "decimal_preview": float(x)}


def interval(x):
    return {"lower": rational(x.lo), "upper": rational(x.hi)}


def symmetric(x):
    return I(-x, x)


def s2(x):
    return (3 + x) / (1 - x)**3


def s4(x):
    return (8*x*(1+11*x+11*x*x+x**3)/(1-x)**5
            + 56*x*(1+4*x+x*x)/(1-x)**4
            + 142*x*(1+x)/(1-x)**3 + 154*x/(1-x)**2
            + 60/(1-x))


N = 20
CELLS = 16
ys = [F(1, 8), F(3, 16), F(1, 4)]
q = F(3, 8)
M = 3 * (q**18 + 504*q**40)
J4 = F(16,45)*F(101,100)/(6*250) + F(128,15)*F(40,27*14**3)
J6 = F(16,45)*F(101,100)/(10*250) + F(512,15)*F(32,25*14**5)
epsilon = F(16,15)*F(8,7)*F(441,6)*q**20
tail = [epsilon * F(4433,64)**k for k in range(3)]
series_tail = [F(9 * 2**(N+1), factorial(N+1-k)) for k in range(3)]
sine1, sine2 = F(16,10**9), F(4,10**6)
sinc = I(1-F(1,10**10), 1/(1-F(1,10**10)))

checks = []


def check(name, actual, upper):
    checks.append({"name": name, "actual": rational(actual),
                   "required_strict_upper": rational(F(upper)),
                   "passed": actual < upper})


check("second_order_shell_ratio", F(22,21)**2 * (F(35,31)*F(147,143))**2/16, F(1,8))
check("epsilon0", tail[0], F(1,10**6))
check("epsilon1", tail[1], F(1,10**4))
check("epsilon2", tail[2], F(2,1000))
check("J6", J6, F(1,4000))
check("normalized_H_t", (18+tail[1])/(1-tail[0]), 19)
check("normalized_H_tt", (36+tail[2])/(1-tail[0]), 37)
check("phase_log_t_bound", F(57+19), 80)
check("phase_tt_relative_bound", F(57**2+2+2*57*19+37), 5500)
check("second_sinc_log_error_pair", F(2*(2*80**2+5500),10**10), sine2)

# Integral coefficients of (alpha_+^n + alpha_-^n)/2, divided by y.
# alpha_+/- = -x^2/4 +/- r*x/2, v=r^2. All terms at fixed n
# have the same sign (-1)^n; no power-series coefficients are guessed.
coeff = {}
for y in ys:
    coeff[y] = [
        [F(comb(n, 2*j), 4**(n-j)) * y**(2*n-2*j) / (2*n-2*j+1)
         for j in range(n//2+1)] for n in range(N+1)
    ]


def core_jets(y, t, v):
    tp = [t.positive_power(n) for n in range(N+1)]
    vp = [v.positive_power(n) for n in range(N//2+1)]
    moments = [sum((c*vp[j] for j, c in enumerate(row)), I(0))
               for row in coeff[y]]
    result = []
    for k in range(3):
        value = sum((moments[n]*tp[n-k] * F((-1)**n, factorial(n-k))
                     for n in range(k, N+1)), I(0))
        value = value + symmetric(series_tail[k])
        if k == 0:
            value = I(max(value.lo, F(1)), min(value.hi, F(9)))
        result.append(value)
    return result


def ratio_data(base, current, scale, e0, e1, e2, full):
    # Output r, B=(log r)_t, C=(log r)_tt, all on this rectangle.
    B = current[1]/current[0] - base[1]/base[0]
    C = (current[2]/current[0] - (current[1]/current[0]).square()
         - base[2]/base[0] + (base[1]/base[0]).square())
    r = scale * current[0]/base[0]
    if full:
        r = r * I(1-e0, 1/(1-e0)) * sinc
        B = B + symmetric(e1+sine1)
        C = C + symmetric(e2+sine2)
    return r, B, C


def wronskian(data2, data3):
    r2, b2, c2 = data2
    r3, b3, c3 = data3
    return r2*r3*(b2*c3-b3*c2+b2*b3*(b3-b2))


records = []
global_bounds = {}


def accumulate(name, x):
    global_bounds[name] = x if name not in global_bounds else global_bounds[name].hull(x)


for ti in range(CELLS):
    t = I(F(1,2)+F(ti,2*CELLS), F(1,2)+F(ti+1,2*CELLS))
    for vi in range(CELLS):
        v = I(196+F(29*vi,CELLS), 196+F(29*(vi+1),CELLS))
        core = [core_jets(y, t, v) for y in ys]
        full = [[jet[k]+symmetric(tail[k]) for k in range(3)] for jet in core]
        for jet in full:
            jet[0] = I(max(jet[0].lo, 1-tail[0]), jet[0].hi)
        ds, cs = [], []
        for j in (1,2):
            y = ys[j]
            dy = y*y-ys[0]**2
            D2 = 4*dy*(M*s2(y*y/4)/12 + (J4+4*M/3)*s2(y*y))
            D4 = 4*dy*(M*s4(y*y/4)/48 + (J6+4*M/3)*s4(y*y))
            E1 = D2/t.lo**2
            E2 = D4/t.lo**4 + 2*D2/t.lo**3
            d = ratio_data(full[0], full[j], y/ys[0], dy, E1, E2, True)
            c = ratio_data(core[0], core[j], y/ys[0], 0, 0, 0, False)
            ds.append(d)
            cs.append(c)
            r, b, cc = d
            rt = r*b
            rtt = r*(b.square()+cc)
            rs = -t.positive_power(2)*rt
            rss = t.positive_power(4)*rtt + 2*t.positive_power(3)*rt
            if j == 2:
                rs = I(rs.lo, min(rs.hi, -F(1,2000)))  # Audited C033g.
            accumulate(f"r{j+1}_s", rs)
            accumulate(f"r{j+1}_ss", rss)
        wcore = wronskian(*cs)
        wfull = wronskian(*ds)
        ws = -t.positive_power(6)*wfull
        accumulate("core_W_t", wcore)
        accumulate("full_W_t", wfull)
        accumulate("full_W_s", ws)
        records.append({"t_index": ti, "v_index": vi, "t": interval(t), "r_squared": interval(v),
                        "core_W_t": interval(wcore), "full_W_t": interval(wfull),
                        "full_W_s": interval(ws)})

# Newton row operations + Genocchi--Hermite, including repeated sites.
determinant = (global_bounds["r2_s"]*global_bounds["r3_ss"]
               -global_bounds["r3_s"]*global_bounds["r2_ss"])/2
# A short rational outer enclosure for the canonical statement.
rounded = I(determinant.lo.__floor__(), determinant.hi.__ceil__())
failures = [c["name"] for c in checks if not c["passed"]]
certificate = {
    "step_id": "2026-11-19-third-width-enclosure-1746",
    "canonical_proof": "lemmas/C033k-third-width-normalized-enclosure.md",
    "assessment": "drafts/literature/2026-11-19-third-width-determinant-test-1745.md",
    "scope": "Full qualified complex divisor; one fixed continuum cover, no sampling or adaptive refinement.",
    "cover": {"inverse_width_cells": CELLS, "first_ordinate_squared_cells": CELLS,
              "t_interval": interval(I(F(1,2),1)), "r_squared_interval": interval(I(196,225)),
              "Taylor_degree": N, "parameter_rectangles": len(records)},
    "constants": {"M": rational(M), "J4": rational(J4), "J6": rational(J6),
                  "normalized_tail_derivatives": [rational(x) for x in tail],
                  "core_Taylor_remainders": [rational(x) for x in series_tail]},
    "checks": checks, "arithmetic_failures": failures,
    "global_bounds": {k: interval(v) for k,v in global_bounds.items()},
    "conclusion": {
        "Delta3_enclosure": interval(determinant), "rounded_Delta3_enclosure": interval(rounded),
        "required": "One orientation with a strictly positive uniform margin, including all collision patterns.",
        "strict_margin_certified": determinant.lo > 0 or determinant.hi < 0,
        "full_W_strict_sign_certified": global_bounds["full_W_s"].lo > 0 or global_bounds["full_W_s"].hi < 0,
        "verdict": "INCONCLUSIVE: zero-containing enclosure; park without refining the cover.",
        "analytic_audit": "PENDING; exact arithmetic is not a proof or external-source audit.",
    },
    "rectangles": records,
}
output = Path(__file__).with_name("third-width-1746.json")
output.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"Rational side checks: {len(checks)-len(failures)}/{len(checks)} passed; failures={failures}")
print(f"Single fixed continuum cover: {len(records)} rectangles; Taylor degree {N}; no refinements")
for name in ("core_W_t", "full_W_t", "full_W_s"):
    x = global_bounds[name]
    print(f"{name}: enclosure preview [{float(x.lo):.12g}, {float(x.hi):.12g}]")
print(f"Delta3 rigorous integer enclosure: [{rounded.lo}, {rounded.hi}]; required: either strict sign")
print(f"Strict determinant margin certified: {certificate['conclusion']['strict_margin_certified']}")
print(f"Complete exact certificate: {output.relative_to(Path.cwd())}")
print("Analytic proof and qualified source correctness remain outside this arithmetic check.")
raise SystemExit(bool(failures))
