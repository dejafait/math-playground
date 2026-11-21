#!/usr/bin/env python3
"""Fixed P=101, j=2,...,8 pilot for assessment1135; no parameter search.

Uses system MPFR via ctypes, with explicit directed rounding. All output
intervals are decimal rounded outwards. See the canonical record for
the digamma/Cauchy and paper162 exponential-response remainder proofs.
Run from riemann: python3 scripts/pivot-area/certify_1136.py
"""
import ctypes as ct
import ctypes.util
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

PREC = 384
DOWN, UP = 3, 2  # MPFR_RNDD, MPFR_RNDU
lib_path = ctypes.util.find_library("mpfr") or "/opt/homebrew/lib/libmpfr.dylib"
lib = ct.CDLL(lib_path)


class Raw(ct.Structure):
    _fields_ = [("prec", ct.c_long), ("sign", ct.c_int),
                ("exp", ct.c_long), ("limbs", ct.POINTER(ct.c_ulong))]


Ptr = ct.POINTER(Raw)
lib.mpfr_init2.argtypes = [Ptr, ct.c_long]
lib.mpfr_clear.argtypes = [Ptr]
lib.mpfr_set_str.argtypes = [Ptr, ct.c_char_p, ct.c_int, ct.c_int]
lib.mpfr_cmp.argtypes = [Ptr, Ptr]
lib.mpfr_cmp.restype = ct.c_int
lib.mpfr_number_p.argtypes = [Ptr]
lib.mpfr_number_p.restype = ct.c_int
lib.mpfr_get_str.argtypes = [ct.c_void_p, ct.POINTER(ct.c_long), ct.c_int,
                           ct.c_size_t, Ptr, ct.c_int]
lib.mpfr_get_str.restype = ct.c_void_p
lib.mpfr_free_str.argtypes = [ct.c_void_p]
lib.mpfr_get_version.restype = ct.c_char_p
for name in ["add", "sub", "mul", "div"]:
    getattr(lib, "mpfr_" + name).argtypes = [Ptr, Ptr, Ptr, ct.c_int]
for name in ["neg", "sqrt", "log", "exp", "sin", "cos", "atan"]:
    getattr(lib, "mpfr_" + name).argtypes = [Ptr, Ptr, ct.c_int]
lib.mpfr_const_pi.argtypes = [Ptr, ct.c_int]


class Real:
    def __init__(self, text="0", rounding=DOWN):
        self.raw = Raw()
        lib.mpfr_init2(ct.byref(self.raw), PREC)
        assert lib.mpfr_set_str(ct.byref(self.raw), str(text).encode(), 10, rounding) == 0

    def __del__(self):
        lib.mpfr_clear(ct.byref(self.raw))

    def __lt__(self, b):
        return lib.mpfr_cmp(ct.byref(self.raw), ct.byref(b.raw)) < 0

    def decimal(self, rounding):
        exponent = ct.c_long()
        p = lib.mpfr_get_str(None, ct.byref(exponent), 10, 105,
                            ct.byref(self.raw), rounding)
        digits = ct.string_at(p).decode()
        lib.mpfr_free_str(p)
        n = len(digits.lstrip("-"))
        return digits + "e" + str(exponent.value - n)


def op(name, a, b=None, rounding=DOWN):
    out = Real()
    args = [ct.byref(out.raw), ct.byref(a.raw)]
    if b is not None:
        args.append(ct.byref(b.raw))
    getattr(lib, "mpfr_" + name)(*args, rounding)
    assert lib.mpfr_number_p(ct.byref(out.raw)), name
    return out


class I:
    def __init__(self, value=0, high=None):
        self.lo = value if isinstance(value, Real) else Real(value, DOWN)
        if high is None:
            self.hi = value if isinstance(value, Real) else Real(value, UP)
        else:
            self.hi = high if isinstance(high, Real) else Real(high, UP)
        assert not self.hi < self.lo

    @staticmethod
    def cast(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, b):
        b = I.cast(b)
        return I(op("add", self.lo, b.lo), op("add", self.hi, b.hi, UP))

    __radd__ = __add__

    def __neg__(self):
        return I(op("neg", self.hi), op("neg", self.lo, rounding=UP))

    def __sub__(self, b):
        return self + (-I.cast(b))

    def __rsub__(self, b):
        return I.cast(b) - self

    def __mul__(self, b):
        b = I.cast(b)
        pairs = [(x, y) for x in (self.lo, self.hi) for y in (b.lo, b.hi)]
        return I(min(op("mul", x, y) for x, y in pairs),
                 max(op("mul", x, y, UP) for x, y in pairs))

    __rmul__ = __mul__

    def __truediv__(self, b):
        b = I.cast(b)
        zero = Real()
        if not (b.hi < zero or zero < b.lo):
            raise ArithmeticError("interval division through zero")
        inv = I(op("div", Real(1), b.hi), op("div", Real(1), b.lo, UP))
        return self * inv

    def __rtruediv__(self, b):
        return I.cast(b) / self

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        result, a = I(1), self
        while n:
            if n & 1:
                result = result * a
            a = a * a
            n //= 2
        return result

    def unary(self, name):
        # Only monotone functions: sqrt, log, exp, atan.
        assert name in ("sqrt", "log", "exp", "atan")
        return I(op(name, self.lo), op(name, self.hi, rounding=UP))

    def trig(self, name):
        # Both sin and cos are globally 1-Lipschitz. Evaluate at the
        # exact binary lower endpoint, then add the entire input width.
        assert name in ("sin", "cos")
        width = op("sub", self.hi, self.lo, UP)
        return I(op("sub", op(name, self.lo), width),
                 op("add", op(name, self.lo, rounding=UP), width, UP))

    def positive(self):
        return Real(0) < self.lo

    def abs(self):
        if not self.lo < Real(0):
            return self
        if not Real(0) < self.hi:
            return -self
        return I(0, max(op("neg", self.lo, rounding=UP), self.hi))

    def dump(self):
        return [self.lo.decimal(DOWN), self.hi.decimal(UP)]


class C:
    def __init__(self, real=0, imag=0):
        self.r, self.i = I.cast(real), I.cast(imag)

    @staticmethod
    def cast(x):
        return x if isinstance(x, C) else C(x)

    def __add__(self, b):
        b = C.cast(b)
        return C(self.r + b.r, self.i + b.i)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.r, -self.i)

    def __sub__(self, b):
        return self + (-C.cast(b))

    def __mul__(self, b):
        b = C.cast(b)
        return C(self.r * b.r - self.i * b.i, self.r * b.i + self.i * b.r)

    __rmul__ = __mul__

    def inv(self):
        den = self.r * self.r + self.i * self.i
        return C(self.r / den, -self.i / den)

    def dump(self):
        return {"real": self.r.dump(), "imag": self.i.dump()}


def bernoulli(n):
    vals = [Fraction(1)]
    for m in range(1, n + 1):
        vals.append(-sum(Fraction(math.comb(m + 1, k)) * vals[k]
                         for k in range(m)) / (m + 1))
    return vals


BERN = bernoulli(64)
N, SHIFT, EXP_TERMS = 32, 128, 32
REM = (I(abs(BERN[64].numerator)) / BERN[64].denominator / 64
       * I(2)**65 / I(127)**64)


def psi_pair(y):
    # DLMF5.11.2 through k=31 at z=128+1/4+iy. On the radius-one
    # disk Re(z)>127, |arg(z)|<pi/2. DLMF5.11(ii) gives |R|<=REM;
    # Cauchy gives |R'|<=REM. No differentiation of an O-term is used.
    z = C(I(1)/4 + SHIFT, y)
    inv = z.inv()
    logz = C((z.r*z.r + z.i*z.i).unary("log")/2,
             (z.i/z.r).unary("atan"))
    psi = logz - inv * (I(1)/2)
    trigamma = inv + inv*inv*(I(1)/2)
    even_power = inv*inv
    for k in range(1, N):
        b = I(BERN[2*k].numerator) / BERN[2*k].denominator
        psi = psi - even_power * (b/(2*k))
        trigamma = trigamma + even_power*inv*b
        even_power = even_power*inv*inv
    err = I(op("neg", REM.hi), REM.hi)
    psi = psi + C(err, err)
    trigamma = trigamma + C(err, err)
    for h in range(SHIFT):
        invh = C(I(1)/4 + h, y).inv()
        psi = psi - invh
        trigamma = trigamma + invh*invh
    return psi, trigamma


def prime_powers(P):
    result = []
    for p in range(2, P):
        if any(p % d == 0 for d in range(2, math.isqrt(p) + 1)):
            continue
        n, power = p, 1
        while n < P:
            result.append((n, p, power))
            n *= p
            power += 1
    return sorted(result)


def dump_matrix(mat):
    return [[v.dump() for v in row] for row in mat]


def main():
    P, size = 101, 9
    pi = I()
    lib.mpfr_const_pi(ct.byref(pi.lo.raw), DOWN)
    lib.mpfr_const_pi(ct.byref(pi.hi.raw), UP)
    a = I(P).unary("log") / 2
    alpha = ((a/2).unary("exp") - (-a/2).unary("exp"))**2 / 4
    powers = prime_powers(P)
    prime_data = [(n, p, k, I(p).unary("log")/I(n).unary("sqrt"),
                   I(n).unary("log")) for n, p, k in powers]
    cJ = I(2*EXP_TERMS) + I(1)/2
    deltaF = (-2*a*cJ).unary("exp") / (1-(-4*a).unary("exp"))
    deltaR = deltaF/(cJ*cJ)
    source, u, v, diag = [], [], [], []
    components = {key: [] for key in ("prime", "digamma", "exponential", "pole")}
    for q in range(size):
        gamma = 1/I(2).unary("sqrt") if q == 0 else I(1)
        x = pi*q/a
        psi, trigamma = psi_pair(x/2)
        s = sum((w*(q*pi*ln/a).trig("sin") for n,p,k,w,ln in prime_data), I())
        prime_diag = -2*sum((w*(1-ln/(2*a))*(q*pi*ln/a).trig("cos")
                            for n,p,k,w,ln in prime_data), I())
        if q:
            prime_diag += s/(pi*q)
        sumF, sumR = I(), I()
        for ell in range(EXP_TERMS):
            c = I(2*ell) + I(1)/2
            ex = (-2*a*c).unary("exp")
            den = c*c + x*x
            sumF += x*x*ex/den
            sumR += c*c*ex/(den*den)
        F = x*psi.i/2 - sumF - alpha/(I(1)/4+x*x)
        if q:
            F += I(op("neg", deltaF.hi), 0)
            R = psi.i/(4*x) + trigamma.r/8
        else:
            R = trigamma.r/4
        R = R - sumR + alpha/(I(1)/4+x*x)**2 + I(op("neg", deltaR.hi), 0)
        uq = gamma*(2*q*s/pi + 2*a/(pi*pi)*F)
        components["prime"].append(gamma*2*q*s/pi)
        components["digamma"].append(gamma*2*a/(pi*pi)*(x*psi.i/2))
        exp_part = -sumF + (I(op("neg", deltaF.hi),0) if q else I())
        components["exponential"].append(gamma*2*a/(pi*pi)*exp_part)
        components["pole"].append(-gamma*2*a/(pi*pi)*alpha/(I(1)/4+x*x))
        dq = psi.r - pi.unary("log") + 2/a*gamma*gamma*R + prime_diag
        u.append(uq)
        v.append(gamma)
        diag.append(dq)
        source.append({"q":q,"gamma":gamma.dump(),"x":x.dump(),
                       "psi":psi.dump(),"trigamma":trigamma.dump(),
                       "s":s.dump(),"prime_diag":prime_diag.dump(),
                       "F":F.dump(),"R":R.dump(),"u":uq.dump(),"Aqq":dq.dump()})
    A = [[diag[q] if q == r else (u[q]*v[r]-v[q]*u[r])/(q*q-r*r)
          for r in range(size)] for q in range(size)]
    L = [[I(int(i == j)) for j in range(size)] for i in range(size)]
    D, failures = [], []
    for k in range(size):
        pivot = A[k][k] - sum((L[k][h]*L[k][h]*D[h] for h in range(k)), I())
        D.append(pivot)
        if not pivot.positive():
            failures.append({"type":"uncertified_core", "order":k+1,"pivot":pivot.dump()})
            break
        for i in range(k+1, size):
            L[i][k] = (A[i][k] - sum((L[i][h]*L[k][h]*D[h]
                                      for h in range(k)), I()))/pivot

    def solve(rhs, j):
        assert j <= len(D) and all(d.positive() for d in D[:j])
        y = []
        for i in range(j):
            y.append(rhs[i]-sum((L[i][h]*y[h] for h in range(i)), I()))
        z = [y[i]/D[i] for i in range(j)]
        ans = [I() for i in range(j)]
        for i in reversed(range(j)):
            ans[i] = z[i] - sum((L[h][i]*ans[h] for h in range(i+1,j)), I())
        return ans

    tests = []
    for j in range(2,9):
        if j >= len(D) or not all(d.positive() for d in D[:j+1]):
            tests.append({"j":j,"status":"INELIGIBLE_UNCERTIFIED_CORE"})
            continue
        m = [A[q][j] for q in range(j)]
        sm, su, sv = solve(m,j), solve(u,j), solve(v,j)
        dot = lambda a,b: sum((a[k]*b[k] for k in range(j)),I())
        G = [[dot(u,su),dot(u,sv)],[dot(v,su),dot(v,sv)]]
        # Both off-diagonal computations enclose the same exact number.
        cross = I(max(G[0][1].lo,G[1][0].lo),min(G[0][1].hi,G[1][0].hi))
        G[0][1] = G[1][0] = cross
        r = [u[j]-dot(u,sm), v[j]-dot(v,sm)]
        residual_components = {key: vals[j]-dot(vals,sm) for key,vals in components.items()}
        residual_sum = sum(residual_components.values(),I())
        assert not (residual_sum.hi < r[0].lo or r[0].hi < residual_sum.lo)
        rawp = A[j][j]-dot(m,sm)
        p = I(max(rawp.lo,D[j].lo), min(rawp.hi,D[j].hi))
        assert p.positive()
        lhs = r[0]*r[0]*G[1][1] - 2*r[0]*r[1]*cross + r[1]*r[1]*G[0][0]
        rhs = P**2*(j+1)**5*p
        margin = rhs-lhs
        # Diagnostic obstruction to separately paying the four signed
        # source channels. adj(G) is positive semidefinite. The triangle
        # estimate in its seminorm is:
        # sqrt(area) <= sqrt(Gvv)*sum|r_u,channel| + sqrt(Guu)*|r_v|.
        # A lower bound for this proposed UPPER BUDGET above sqrt(rhs)
        # only rejects that payment; it does not refute H.
        assert G[0][0].positive() and G[1][1].positive()
        triangle_budget = (G[1][1].unary("sqrt") *
                           sum((val.abs() for val in residual_components.values()),I())
                           + G[0][0].unary("sqrt")*r[1].abs())**2
        status = "PASS" if margin.positive() else ("VIOLATION" if (-margin).positive() else "INCONCLUSIVE")
        if status != "PASS":
            failures.append({"type":status,"j":j})
        test = {"j":j,"status":status,"m": [x.dump() for x in m],
                "solve_m":[x.dump() for x in sm],"solve_u":[x.dump() for x in su],
                "solve_v":[x.dump() for x in sv],"G":dump_matrix(G),
                "r":[x.dump() for x in r],"pivot":p.dump(),"lhs":lhs.dump(),
                "rhs":rhs.dump(),"margin":margin.dump(),"ratio":(lhs/rhs).dump(),
                "area_increment":(lhs/p).dump(),
                "u_residual_channels":{key: val.dump() for key,val in residual_components.items()},
                "separate_channel_upper_budget":triangle_budget.dump(),
                "separate_channel_budget_over_rhs":(triangle_budget/rhs).dump()}
        tests.append(test)

    # Exact decimal thresholds for the human-readable canonical table.
    # These comparisons use the full interval endpoints, never floats.
    pivot_lower = [".027", "7.59e-7", "5.84e-10", "9.01e-13", "4.21e-15",
                   "4.36e-17", "5.32e-19", "1.16e-20", "4.40e-22"]
    ratio_upper = [".288210", ".433150", ".460314", ".439972", ".557627", ".599685", ".469076"]
    budget_lower = ["1.38e7", "4.06e10", "6.02e13", "5.76e16", "6.40e19", "5.51e22", "4.00e25"]
    pivot_checks = [{"order":k+1,"lower":b,"verified":(D[k]-I(b)).positive()}
                    for k,b in enumerate(pivot_lower)] if len(D)==9 else []
    rows = []
    for index,t in enumerate(tests):
        if "ratio" not in t:
            continue
        ratio = I(*t["ratio"])
        budget = I(*t["separate_channel_budget_over_rhs"])
        rows.append({"j":t["j"],"ratio_upper":ratio_upper[index],
                     "ratio_verified":(I(ratio_upper[index])-ratio).positive(),
                     "budget_ratio_lower":budget_lower[index],
                     "budget_verified":(budget-I(budget_lower[index])).positive()})
    claims = {"positive_pivots":pivot_checks,"pilot_and_budget":rows,
              "digamma_error_lt_3e_minus79":(I("3e-79")-REM).positive(),
              "deltaF_lt_6e_minus130":(I("6e-130")-deltaF).positive(),
              "deltaR_lt_2e_minus133":(I("2e-133")-deltaR).positive()}
    if not (len(pivot_checks)==9 and all(t["verified"] for t in pivot_checks)
            and len(rows)==7 and all(t["ratio_verified"] and t["budget_verified"] for t in rows)
            and all(claims[k] for k in ("digamma_error_lt_3e_minus79",
                                       "deltaF_lt_6e_minus130","deltaR_lt_2e_minus133"))):
        failures.append({"type":"CANONICAL_TABLE_CLAIM_FAILURE"})

    out = {"schema":"pivot-area-1136-v1","P":P,"tested_j":list(range(2,9)),
           "precision_bits":PREC,"mpfr_version":lib.mpfr_get_version().decode(),
           "mpfr_library":lib_path,"source":"paper162/v1 Section2(8)-(12)",
           "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "a":a.dump(),"pi":pi.dump(),"alpha":alpha.dump(),
           "prime_powers":[{"n":n,"prime":p,"power":k,"weight":w.dump(),"log_n":ln.dump()}
                           for n,p,k,w,ln in prime_data],
           "digamma":{"shift":SHIFT,"N":N,"error_psi_and_derivative":REM.dump(),
                      "bernoulli_even":[str(BERN[2*k]) for k in range(1,N+1)]},
           "response_tail":{"terms":EXP_TERMS,"deltaF":deltaF.dump(),"deltaR":deltaR.dump()},
           "source_rows":source,"matrix":dump_matrix(A),"LDL_L":dump_matrix(L),
           "source_u_channels":{key:[val.dump() for val in vals] for key,vals in components.items()},
           "LDL_pivots":[d.dump() for d in D],"tests":tests,"claims":claims,"failures":failures,
           "interpretation":"Finite pilot only; no universal H, all-support sign or RH conclusion."}
    path = Path(__file__).with_name("certificate-1136.json")
    path.write_text(json.dumps(out,indent=2)+"\n")
    print(f"P={P}; {len(prime_data)} prime powers; MPFR {out['mpfr_version']}; {PREC} bits")
    print("Digamma/derivative absolute error < 3e-79:", claims["digamma_error_lt_3e_minus79"])
    print("Certified positive leading cores:", sum(d.positive() for d in D), "required: 9")
    for t in tests:
        if "ratio" in t:
            # This is only a display; certified decimal endpoints are in JSON.
            print(f"j={t['j']}: {t['status']}; lhs/rhs <= {float(t['ratio'][1]):.8g} (required <=1); "
                  f"pivot >= {float(t['pivot'][0]):.8g}; separate-channel budget/rhs >= "
                  f"{float(t['separate_channel_budget_over_rhs'][0]):.8g}")
        else:
            print(f"j={t['j']}: {t['status']}")
    print("Failures:", failures)
    print("Full certificate:", path)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
