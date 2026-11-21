"""One fixed Polymath (14)-(19),(23)-(24) boundary test, not an RH test.

100 Decimal digits, 96 Machin terms, at most 128 elementary-series terms.
See the step2152 canonical record for inclusion proofs and qualifications.
No mesh, precision, cutoff, or formula sweep. Standard library only.
"""

import json
import platform
from decimal import (Context, Decimal, ROUND_FLOOR, ROUND_CEILING,
                     ROUND_HALF_EVEN, DivisionByZero, InvalidOperation,
                     Overflow, Underflow, Subnormal, Clamped)
from fractions import Fraction
from pathlib import Path

PREC = 100
DN = Context(prec=PREC, rounding=ROUND_FLOOR)
UP = Context(prec=PREC, rounding=ROUND_CEILING)
RN = Context(prec=PREC, rounding=ROUND_HALF_EVEN)
for ctx in (DN, UP, RN):
    for signal in (DivisionByZero, InvalidOperation, Overflow, Underflow,
                   Subnormal, Clamped):
        ctx.traps[signal] = True

STATS = {"log_calls": 0, "trig_calls": 0, "sqrt_squared_checks": 0,
         "max_log_radius": Decimal(0), "max_reduced_angle": Decimal(0),
         "max_log_tail": Decimal(0), "max_trig_tail": Decimal(0)}
ACTIVE = None


class I:
    def __init__(self, lo, hi=None):
        if isinstance(lo, float) or isinstance(hi, float):
            raise TypeError("No binary float inputs")
        self.lo = Decimal(lo)
        self.hi = self.lo if hi is None else Decimal(hi)
        if not (self.lo.is_finite() and self.hi.is_finite()
                and self.lo <= self.hi):
            raise ValueError("Invalid interval")

    @staticmethod
    def lift(x):
        return x if isinstance(x, I) else I(x)

    @staticmethod
    def rat(x):
        x = Fraction(x)
        a, b = Decimal(x.numerator), Decimal(x.denominator)
        return I(DN.divide(a, b), UP.divide(a, b))

    def __add__(self, x):
        x = I.lift(x)
        return I(DN.add(self.lo, x.lo), UP.add(self.hi, x.hi))

    __radd__ = __add__

    def __neg__(self):
        return I(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, x):
        return self + -I.lift(x)

    def __rsub__(self, x):
        return I.lift(x) + -self

    def __mul__(self, x):
        x = I.lift(x)
        pairs = [(a, b) for a in (self.lo, self.hi)
                 for b in (x.lo, x.hi)]
        return I(min(DN.multiply(a, b) for a, b in pairs),
                 max(UP.multiply(a, b) for a, b in pairs))

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = I.lift(x)
        if x.lo <= 0 <= x.hi:
            raise ZeroDivisionError("Real divisor contains zero")
        return self * I(DN.divide(Decimal(1), x.hi),
                        UP.divide(Decimal(1), x.lo))

    def __rtruediv__(self, x):
        return I.lift(x) / self

    def sq(self):
        a, b = self.lo.copy_abs(), self.hi.copy_abs()
        small = Decimal(0) if self.lo <= 0 <= self.hi else min(a, b)
        big = max(a, b)
        return I(DN.multiply(small, small), UP.multiply(big, big))

    def pow(self, n):
        assert isinstance(n, int) and n >= 0
        ans = I(1)
        for _ in range(n):
            ans = ans * self
        return ans

    def exp(self):
        return I(RN.next_minus(RN.exp(self.lo)),
                 RN.next_plus(RN.exp(self.hi)))

    def ln(self):
        if self.lo <= 0:
            raise ValueError("Logarithm domain")
        return I(RN.next_minus(RN.ln(self.lo)),
                 RN.next_plus(RN.ln(self.hi)))

    def sqrt(self):
        if self.lo < 0:
            raise ValueError("Square root domain")
        lo = Decimal(0) if self.lo == 0 else RN.next_minus(RN.sqrt(self.lo))
        hi = RN.next_plus(RN.sqrt(self.hi))
        assert Fraction(lo)**2 <= Fraction(self.lo)
        assert Fraction(hi)**2 >= Fraction(self.hi)
        STATS["sqrt_squared_checks"] += 2
        return I(lo, hi)

    def mag(self):
        return max(self.lo.copy_abs(), self.hi.copy_abs())

    def data(self):
        return {"lo": str(self.lo), "hi": str(self.hi)}


def upper(x):
    return I(I.lift(x).hi)


def inflate(x, radius):
    return x + I(radius.copy_negate(), radius)


def guard(name, condition, evidence):
    if ACTIVE is not None:
        ACTIVE.append({"name": name, "passed": bool(condition),
                       "evidence": evidence})
    if not condition:
        raise ValueError(name)


class C:
    def __init__(self, re=0, im=0):
        self.re, self.im = I.lift(re), I.lift(im)

    @staticmethod
    def lift(x):
        return x if isinstance(x, C) else C(x)

    def __add__(self, x):
        x = C.lift(x)
        return C(self.re + x.re, self.im + x.im)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, x):
        return self + -C.lift(x)

    def __rsub__(self, x):
        return C.lift(x) + -self

    def __mul__(self, x):
        x = C.lift(x)
        return C(self.re*x.re-self.im*x.im,
                 self.re*x.im+self.im*x.re)

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = C.lift(x)
        den = x.re.sq() + x.im.sq()
        guard("complex divisor away from zero", den.lo > 0, den.data())
        return C((self.re*x.re+self.im*x.im)/den,
                 (self.im*x.re-self.re*x.im)/den)

    def __rtruediv__(self, x):
        return C.lift(x) / self

    def conj(self):
        return C(self.re, -self.im)

    def modulus(self):
        return (self.re.sq()+self.im.sq()).sqrt()

    def log(self):
        # Here |Im z| is large and nonzero. Rotate by +/-i A first.
        sign = 1 if self.im.lo > 0 else -1
        guard("log imaginary sign", self.im.lo > 0 or self.im.hi < 0,
              self.im.data())
        a = I(self.im.mag())
        w = self / C(0, a*sign) - 1
        rho = upper(w.modulus())
        guard("log series radius", rho.hi < 1, rho.data())
        # |w|<1 => 1+w lies in the open right half-plane. Explicitly
        # check the rotated argument remains inside the principal branch.
        guard("principal log rotation", (1+w.re).lo > 0,
              (1+w.re).data())
        term, total = C(1), C(0)
        for n in range(1, 129):
            term = term*w
            total = total + term*((1 if n % 2 else -1)*I.rat(Fraction(1, n)))
        tail = upper(rho.pow(129)/(129*(1-rho)))
        total = C(inflate(total.re, tail.hi), inflate(total.im, tail.hi))
        STATS["log_calls"] += 1
        STATS["max_log_radius"] = max(STATS["max_log_radius"], rho.hi)
        STATS["max_log_tail"] = max(STATS["max_log_tail"], tail.hi)
        return C(a.ln(), PI*sign/2) + total

    def exp(self):
        sin, cos = trig(self.im)
        scale = self.re.exp()
        return C(scale*cos, scale*sin)

    def data(self):
        return {"re": self.re.data(), "im": self.im.data()}


def trig(x):
    # The chosen integer can be arbitrary: inclusion uses the full PI
    # interval. Verify the entire reduced interval fits |r|<=4.
    midpoint = RN.divide(RN.add(x.lo, x.hi), Decimal(2))
    q = DN.divide(midpoint, RN.multiply(Decimal(2), PI.lo))
    n = int(q.to_integral_value(rounding=ROUND_FLOOR))
    r = x - 2*n*PI
    # If floor reduction places the range near 2pi, shift once more.
    if r.hi > Decimal(4):
        n += 1
        r = x - 2*n*PI
    a = I(r.mag())
    guard("trig reduction", a.hi <= 4,
          {"integer": n, "reduced": r.data()})
    rr = r.sq()
    cosine, sine = I(1), r
    ct, st = I(1), r
    for k in range(1, 128):
        ct = -ct*rr/((2*k-1)*(2*k))
        st = -st*rr/((2*k)*(2*k+1))
        cosine, sine = cosine+ct, sine+st
    # Absolute tails start at degrees 256 (cos) and 257 (sin).
    # Later ratios are no larger than these next ratios (<1).
    from math import factorial
    cnext = a.pow(256)/factorial(256)
    snext = a.pow(257)/factorial(257)
    cb = upper(cnext/(1-a.sq()/(257*258)))
    sb = upper(snext/(1-a.sq()/(258*259)))
    STATS["trig_calls"] += 1
    STATS["max_reduced_angle"] = max(STATS["max_reduced_angle"], a.hi)
    STATS["max_trig_tail"] = max(STATS["max_trig_tail"], cb.hi, sb.hi)
    return inflate(sine, sb.hi), inflate(cosine, cb.hi)


def atan_bounds(d):
    x = Fraction(1, d)
    p = sum(((-1)**j*x**(2*j+1)/(2*j+1) for j in range(96)), Fraction(0))
    e = x**193/193  # next term is positive
    return p, p+e


a5, a239 = atan_bounds(5), atan_bounds(239)
PI_RATIONAL = (16*a5[0]-4*a239[1], 16*a5[1]-4*a239[0])
PI = I(I.rat(PI_RATIONAL[0]).lo, I.rat(PI_RATIONAL[1]).hi)
LOGPI = PI.ln()
LOG2 = I(2).ln()
LOG16 = I(16).ln()
LOG3 = I(3).ln()
X = I(200)
R = X/(4*PI)
LOGR = R.ln()
LOGN = [None, I(0), LOG2, LOG3]


def alpha(s):
    return 1/(s*2) + 1/(s-1) + (s.log()-C(LOG2+LOGPI))/2


def logm(t, s, al):
    # Source (7),(10); log(s/2)=Log(s)-log(2), same principal branch.
    return (s.log()+(s-1).log()-s*(LOGPI/2)
            +C((LOG2+LOGPI)/2-LOG16)
            +(s/2-C(I.rat(Fraction(1, 2))))*(s.log()-C(LOG2))
            -s/2 + al*al*(t/4))


def evaluate(t, y):
    s = C((1+y)/2, -100)
    a = C((1-y)/2, 100)
    ap = C((1+y)/2, 100)
    als, ala, alap = alpha(s), alpha(a), alpha(ap)
    logs, loga = logm(t, s, als), logm(t, a, ala)
    gamma = (loga-logs).exp()
    star = s + als*(t/2)
    kappa = (ala-alap)*(t/2)
    # exp(logs) is never zero as a mathematical expression; all its
    # inputs are finite and principal branches were guarded above.
    guard("nonzero explicit normalizer", True,
          {"log_B": logs.data(), "s_imaginary": s.im.data()})
    first, second, eab = C(0), C(0), I(0)
    gabs, kabs = upper(gamma.modulus()), upper(kappa.modulus())
    nfactor = (kabs*LOG3).exp()
    terms = []
    for n in range(1, 4):
        l = LOGN[n]
        b = (t*l.sq()/4).exp()
        f1 = (C(t*l.sq()/4)-star*l).exp()
        f2 = (C(t*l.sq()/4+y*l)-(star.conj()+kappa)*l).exp()
        first, second = first+f1, second+f2
        weight = b*(-star.re*l).exp()
        delta = ((t.sq()*(LOGR-2*l).sq()/16+I('0.626'))
                 /(X-I('6.66'))).exp()-1
        error = (1+gabs*nfactor*(y*l).exp())*weight*delta
        eab = eab+error
        terms.append({"n": n, "first": f1.data(), "second": f2.data(),
                      "error23": error.data()})
    f = first+gamma*second
    aux = C(LOGR, PI/2).modulus()
    ec = (-(1+y)*LOGR/4-t*LOGR.sq()/16
          +I('1.24')*((y*LOG3).exp()+(-y*LOG3).exp())/(3-I('0.125'))
          +(3*aux+I('10.44'))/(X-12)).exp()
    lower = f.modulus().lo
    error = (eab+ec).hi
    margin = DN.subtract(lower, error)
    return {"f": f.data(), "gamma": gamma.data(), "s_star": star.data(),
            "kappa": kappa.data(), "terms": terms,
            "error23": eab.data(), "error24": ec.data(),
            "modulus_lower": str(lower), "error_upper": str(error),
            "margin_lower": str(margin), "passed": margin > 0}


def main():
    global ACTIVE
    out = Path(__file__).with_name('fixed-boundary-2152.json')
    cutoff = (R+I(0, I.rat(Fraction(1, 5)).hi)/16).sqrt()
    cutoff_ok = cutoff.lo >= 3 and cutoff.hi < 4
    certificate = {
        "source": "https://arxiv.org/html/1904.12438v2#S1",
        "formulas": "(6)-(19), (23)-(24); no (20)-(22) or ABC correction",
        "runtime": platform.python_version(), "precision": PREC,
        "grid": {"time_intervals": 32, "height_intervals": 64,
                 "time_endpoints": "j/160", "height_endpoints": "k/64"},
        "series": {"machin_terms": 96, "log_terms": 128,
                   "sine_nonzero_terms": 128, "cosine_nonzero_terms": 128},
        "pi": PI.data(),
        "pi_exact": [{"num": str(q.numerator), "den": str(q.denominator)}
                     for q in PI_RATIONAL],
        "cutoff_guard": {"sqrt_range": cutoff.data(), "N": 3,
                         "passed": cutoff_ok},
        "boxes": [], "failures": [],
        "endpoint": "Conditional continuity extension only if all margins positive",
        "status": "IN_PROGRESS"}
    if not cutoff_ok:
        certificate['failures'].append({"guard": "constant cutoff N=3"})
    else:
        for j in range(32):
            for k in range(64):
                t = I(I.rat(Fraction(j, 160)).lo,
                      I.rat(Fraction(j+1, 160)).hi)
                y = I(I.rat(Fraction(k, 64)).lo,
                      I.rat(Fraction(k+1, 64)).hi)
                box = {"j": j, "k": k,
                       "t_rational": [f"{j}/160", f"{j+1}/160"],
                       "y_rational": [f"{k}/64", f"{k+1}/64"],
                       "t": t.data(), "y": y.data(), "N": 3, "guards": []}
                ACTIVE = box['guards']
                try:
                    box.update(evaluate(t, y))
                    if not box['passed']:
                        certificate['failures'].append({"j": j, "k": k,
                            "reason": "nonpositive sufficient margin",
                            "margin_lower": box['margin_lower']})
                except (ArithmeticError, ValueError, AssertionError) as exc:
                    box['passed'] = False
                    box['exception'] = f"{type(exc).__name__}: {exc}"
                    certificate['failures'].append({"j": j, "k": k,
                                                   "reason": box['exception']})
                certificate['boxes'].append(box)
            # Preserve unfinished full evidence after every time row.
            certificate['completed_time_rows'] = j+1
            out.write_text(json.dumps(certificate, indent=2)+'\n')
    ACTIVE = None
    margins = [Decimal(b['margin_lower']) for b in certificate['boxes']
               if 'margin_lower' in b]
    certificate['statistics'] = {key: str(v) if isinstance(v, Decimal) else v
                                 for key, v in STATS.items()}
    certificate['summary'] = {
        "evaluated_boxes": len(certificate['boxes']),
        "enclosed_boxes": len(margins),
        "positive_boxes": sum(b['passed'] for b in certificate['boxes']),
        "failures": len(certificate['failures']),
        "minimum_margin_lower": str(min(margins)) if margins else None,
        "maximum_margin_lower": str(max(margins)) if margins else None,
        "required_margin": ">0 on every box",
        "all_passed": cutoff_ok and len(margins) == 2048
                      and not certificate['failures']}
    certificate['status'] = ('UNVERIFIED_LOCAL_CERTIFICATE'
        if certificate['summary']['all_passed'] else 'FIXED_TEST_INCONCLUSIVE')
    out.write_text(json.dumps(certificate, indent=2)+'\n')
    print(json.dumps(certificate['summary'], indent=2))
    print(f"Certificate: {out.relative_to(Path.cwd())}")


if __name__ == '__main__':
    main()
