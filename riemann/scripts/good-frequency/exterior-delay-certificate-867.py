"""Exact-integer dyadic certificate for ONE fixed nine-point Haar dual.

No floating-point value participates in an enclosure or sign decision.
Run from the active notebook with Python 3; all output stays beside this file.
"""
from dataclasses import dataclass
import json
from math import factorial, isqrt
from pathlib import Path

BITS = 128
S = 1 << BITS


def ceildiv(n, d):
    assert d > 0
    return -((-n) // d)


@dataclass(frozen=True)
class I:
    lo: int
    hi: int

    def __post_init__(self):
        assert self.lo <= self.hi

    @staticmethod
    def q(n, d=1):
        assert d > 0
        return I(n*S // d, ceildiv(n*S, d))

    def __add__(self, b):
        return I(self.lo + b.lo, self.hi + b.hi)

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, b):
        return self + (-b)

    def __mul__(self, b):
        v = [self.lo*b.lo, self.lo*b.hi, self.hi*b.lo, self.hi*b.hi]
        return I(min(v) // S, ceildiv(max(v), S))

    def __truediv__(self, b):
        assert b.lo > 0 or b.hi < 0, "denominator interval meets zero"
        if b.hi < 0:
            return (-self) / (-b)
        return self * I(S*S // b.hi, ceildiv(S*S, b.lo))

    def sq(self):
        low = 0 if self.lo <= 0 <= self.hi else min(self.lo**2, self.hi**2)
        return I(low // S, ceildiv(max(self.lo**2, self.hi**2), S))

    def sqrt(self):
        assert self.lo >= 0
        low = isqrt(self.lo*S)
        high = isqrt(self.hi*S)
        if high*high < self.hi*S:
            high += 1
        assert low*low <= self.lo*S and high*high >= self.hi*S
        return I(low, high)

    def widen(self, radius):
        assert radius.lo >= 0
        return I(self.lo - radius.hi, self.hi + radius.hi)

    def abs_upper(self):
        return max(abs(self.lo), abs(self.hi))

    def record(self):
        scale = 10**12

        def decimal(n):
            sign = "-" if n < 0 else ""
            a, b = divmod(abs(n), scale)
            return f"{sign}{a}.{b:012d}"

        return {"dyadic_numerators": [str(self.lo), str(self.hi)],
                "decimal_enclosure": [decimal(self.lo*scale // S),
                                      decimal(ceildiv(self.hi*scale, S))]}


Q = I.q
ONE = Q(1)
domains = {"log_unit_calls": 0, "cosine_calls": 0, "atan_calls": 0,
           "max_abs_log_series_argument_numerator": 0,
           "max_abs_cosine_argument_numerator": 0,
           "max_abs_atan_argument_numerator": 0}


def log_unit(x):
    assert S <= x.lo <= x.hi <= 2*S
    y = (x-ONE)/(x+ONE)
    a = y.abs_upper()
    assert a <= S//2
    domains["log_unit_calls"] += 1
    domains["max_abs_log_series_argument_numerator"] = max(
        domains["max_abs_log_series_argument_numerator"], a)
    term, total = y, Q(0)
    y2 = y.sq()
    for j in range(80):
        total = total + term/Q(2*j+1)
        term = term*y2
    # 2 sum_{j>=80} |y|^(2j+1)/(2j+1) < 2^-160 for |y|<=1/2.
    return (Q(2)*total).widen(Q(1, 1 << 160))


LOG2 = log_unit(Q(2))


def log_point(n):
    assert n > 0
    exponent = n.bit_length()-1-BITS
    r = Q(n, 1 << (exponent+BITS))
    return log_unit(r) + Q(exponent)*LOG2


def log_interval(x):
    assert x.lo > 0
    return I(log_point(x.lo).lo, log_point(x.hi).hi)


def atan_small(x):
    a = x.abs_upper()
    assert a <= S//4
    domains["atan_calls"] += 1
    domains["max_abs_atan_argument_numerator"] = max(
        domains["max_abs_atan_argument_numerator"], a)
    term, total = x, Q(0)
    x2 = x.sq()
    for j in range(64):
        v = term/Q(2*j+1)
        total = total + (v if j % 2 == 0 else -v)
        term = term*x2
    # Alternating-series tail <= |x|^129/129 < 2^-256.
    return total.widen(Q(1, 1 << 256))


def cosine(x):
    a = x.abs_upper()
    assert a <= 4*S
    domains["cosine_calls"] += 1
    domains["max_abs_cosine_argument_numerator"] = max(
        domains["max_abs_cosine_argument_numerator"], a)
    term, total = ONE, ONE
    x2 = x.sq()
    for j in range(1, 33):
        term = -(term*x2)/Q((2*j-1)*(2*j))
        total = total + term
    # Degree65 Taylor polynomial (odd coefficients zero), real remainder.
    assert 4**66 * (1 << 150) < factorial(66)
    return total.widen(Q(1, 1 << 150))


PI = Q(16)*atan_small(Q(1, 5))-Q(4)*atan_small(Q(1, 239))
T = Q(4)*log_interval(Q(3))
LOGPI = log_interval(PI)
primes = [p for p in range(2, 81)
          if all(p % d for d in range(2, isqrt(p)+1))]
pp = []
for p in primes:
    n = p
    while n < 81:
        pp.append((n, p, log_interval(Q(p))/Q(n).sqrt(), log_interval(Q(n))))
        n *= p
pp.sort()
expected = [2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,
            37,41,43,47,49,53,59,61,64,67,71,73,79]
assert [n for n, p, weight, delay in pp] == expected


def archimedean(t):
    y2 = (t/Q(2)).sq()
    a = Q(1025, 4)  # Re(z+256)
    den = a.sq()+y2
    shifted_main = log_interval(den)/Q(2)-a/(Q(2)*den)-LOGPI
    corrections = []
    total = Q(0)
    for j in range(256):
        x = Q(4*j+1, 4)
        term = x/(x.sq()+y2)
        corrections.append(term.record())
        total = total+term
    # DLMF5.11(ii): sec^3(arg(Z)/2)/(12|Z|^2) < 1/(4|Z|^2).
    error = ONE/(Q(4)*den)
    m = (shifted_main-total).widen(error)
    return m, {"shift": 256, "squared_modulus": den.record(),
               "shifted_main_minus_logpi": shifted_main.record(),
               "recurrence_terms": corrections, "recurrence_sum": total.record(),
               "absolute_remainder_bound": error.record(), "m": m.record()}


nodes = []
weighted = Q(0)
for j in range(5):
    t = Q(2*j)*PI/(Q(9)*T)
    m, arch = archimedean(t)
    arithmetic, terms = Q(0), []
    for n, p, weight, delay in pp:
        angle = t*delay
        c = cosine(angle)
        v = Q(2)*weight*c
        arithmetic = arithmetic+v
        terms.append({"n": n, "prime": p, "angle": angle.record(),
                      "cosine": c.record(), "complete_term": v.record()})
    w = m-arithmetic
    factor = (t.sq()+Q(1,4)).sq()
    h = factor*w
    mult = 1 if j == 0 else 2
    weighted = weighted+Q(mult)*h
    nodes.append({"j": j, "multiplicity": mult, "t": t.record(),
                  "archimedean": arch, "arithmetic_terms": terms,
                  "arithmetic_sum": arithmetic.record(), "w": w.record(),
                  "primitive_factor": factor.record(), "h": h.record()})
mean = weighted/Q(9)

# Exact polynomial check of the geometric-sum identities at a primitive
# ninth root of unity; this is additional evidence, not approximate moments.
annihilation = []
for k in range(1, 9):
    coeff = [sum((k*j) % 9 == r for j in range(-4,5)) for r in range(9)]
    rem = coeff[:]
    quotient = [0,0,0]
    # Divide by Phi_9(X)=X^6+X^3+1.
    for d in range(8,5,-1):
        c = rem[d]
        quotient[d-6] = c
        for e in [0,3,6]:
            rem[d-6+e] -= c
    assert rem == [0]*9
    annihilation.append({"k": k, "phase_polynomial": coeff,
                         "quotient_by_Phi9": quotient, "remainder": rem})

failures = []
if mean.hi*50 >= -49*S:
    failures.append("Mean upper endpoint did not meet strict -49/50 threshold")
certificate = {
    "status": "CERTIFIED_FIXED_FAMILY_INFEASIBLE" if not failures else "INCONCLUSIVE",
    "method": "Exact-integer outward dyadic intervals; exact root-of-unity annihilation",
    "arithmetic": {"bits": BITS, "common_denominator": str(S),
                   "log_terms": 80, "log_tail_bound": "2^-160",
                   "atan_terms": 64, "atan_tail_bound": "2^-256",
                   "cos_terms": 33, "cos_tail_bound": "2^-150",
                   "floating_point_used_for_decisions": False},
    "constants": {"pi": PI.record(), "log2": LOG2.record(), "T": T.record()},
    "prime_powers": [{"n": n, "prime": p, "weight": weight.record(),
                      "log_n": delay.record()} for n,p,weight,delay in pp],
    "nodes": nodes,
    "annihilation": annihilation,
    "domains": {k: str(v) if "numerator" in k else v for k,v in domains.items()},
    "result": {"nine_point_mean": mean.record(), "required_strict_upper": "-49/50",
               "positive_functional_mass": "1", "cosine_moments": [0]*8,
               "failures": failures},
}
out = Path(__file__).with_name("exterior-delay-certificate-867.json")
out.write_text(json.dumps(certificate, indent=2)+"\n")
summary = {"status": certificate["status"], "T": T.record()["decimal_enclosure"],
           "nodes": [{"j": v["j"], "multiplicity": v["multiplicity"],
                      **{key: v[key]["decimal_enclosure"] for key in ["t","w","h"]}}
                     for v in nodes],
           "mean": mean.record()["decimal_enclosure"],
           "required_strict_upper": "-49/50", "failures": failures,
           "full_certificate": str(out)}
summary_path = out.with_name("exterior-delay-summary-867.json")
summary_path.write_text(json.dumps(summary, indent=2)+"\n")
print(f"{certificate['status']}: mean in {summary['mean']}; required upper < -49/50 < 0.")
print(f"31 prime powers at each of 5 distinct nodes; all 8 moments vanish exactly. Failures: {failures}.")
print(f"Full certificate: {out}; summary: {summary_path}")
if failures:
    raise SystemExit(1)
