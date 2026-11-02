"""Exact rational certificate for the fixed-ellipse completion separator.

Run from riemann: python3 scripts/coupled-flux/exact_completion_separator.py
The analytic meaning and global C1 extension are proved in L593.
No numerical quadrature, floating point, or external packages are used.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


def add(*ps):
    q = {}
    for p in ps:
        for e, a in p.items():
            q[e] = q.get(e, F(0)) + a
    return {e: a for e, a in q.items() if a}


def scale(p, a):
    return {e: a * b for e, b in p.items() if a * b}


def mul(p, q):
    out = {}
    for e, a in p.items():
        for f, b in q.items():
            g = tuple(i + j for i, j in zip(e, f))
            out[g] = out.get(g, F(0)) + a * b
    return {e: a for e, a in out.items() if a}


def mono(a, i, j, k=0):
    return {(i, j, k): F(a)}


def moment(e):
    i, j, k = e
    if i % 2 or j % 2:
        return F(0)
    p, q = i // 2, j // 2
    circle = F(factorial(2 * p) * factorial(2 * q),
               4 ** (p + q) * factorial(p) * factorial(q) * factorial(p + q))
    curvature = F(1, 6) * F(1, 12) ** k + F(5, 6) * F(-7, 60) ** k
    return F(2 ** p, 6 ** q) * circle * curvature


def expectation(p):
    return sum((a * moment(e) for e, a in p.items()), F(0))


def transpose(A):
    return [list(row) for row in zip(*A)]


def matmul(A, B):
    return [[sum((a * b for a, b in zip(row, col)), F(0))
             for col in zip(*B)] for row in A]


def sub(A, B):
    return [[a - b for a, b in zip(ar, br)] for ar, br in zip(A, B)]


class Interval:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = F(lo if hi is None else hi)
        assert self.lo <= self.hi

    @staticmethod
    def coerce(x):
        return x if isinstance(x, Interval) else Interval(x)

    def __add__(self, other):
        other = self.coerce(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        other = self.coerce(other)
        vals = [a * b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return Interval(min(vals), max(vals))

    __rmul__ = __mul__


def spectral_cross(j, k, N=20):
    # Re((iu)^j(-iu)^k exp(-iu)), integrated over [-1/2,1/2].
    value = F(0)
    for n in range(N + 1):
        power, phase = j + k + n, (j - k - n) % 4
        if power % 2 == 0 and phase in (0, 2):
            value += F(1 if phase == 0 else -1,
                       factorial(n) * 2 ** power * (power + 1))
    # Integral exponential-Taylor remainder, using exp(1/2)<2.
    error = F(2, factorial(N + 1) * 2 ** (j + k + N + 1) * (j + k + N + 2))
    return Interval(value - error, value + error)


def coarse(a, denominator=10 ** 12):
    lo = a.lo.numerator * denominator // a.lo.denominator
    hi = -((-a.hi.numerator * denominator) // a.hi.denominator)
    return Interval(F(lo, denominator), F(hi, denominator))


def serial(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, Interval):
        return {"lower": str(value.lo), "upper": str(value.hi)}
    if isinstance(value, list):
        return [serial(v) for v in value]
    if isinstance(value, dict):
        return {str(k): serial(v) for k, v in value.items()}
    return value


def polynomial_record(p):
    return [{"powers_x_y_k": list(e), "coefficient": str(a)}
            for e, a in sorted(p.items())]


x, y, z = mono(1, 1, 0), mono(1, 0, 1), mono(1, 1, 0, 1)
b0 = [x, y, z]
# Rational functions A,B and their derivatives, evaluated only at r^2=1.
A = add(mono(2, 3, 0), mono(-3, 1, 0))
B = add(mono(3, 0, 1), mono(-24, 0, 3))
Ax = add(mono(6, 2, 0), mono(-2, 4, 0), mono(-3, 0, 0))
Ay = mono(-24, 3, 1)
Bx = mono(24, 1, 3)
By = add(mono(3, 0, 0), mono(-72, 0, 2), mono(288, 0, 4))
DA, DB = add(mul(Ax, y), mul(Ay, z)), add(mul(Bx, y), mul(By, z))
fp, gp = add(A, scale(B, F(2))), add(scale(A, F(-1, 2)), scale(B, F(-5, 8)))
DF = add(DA, scale(DB, F(2)))
DG = add(scale(DA, F(-1, 2)), scale(DB, F(-5, 8)))
h = [DF, add(fp, DG), gp]
K0 = [[F(1), F(0), F(-1, 12)],
      [F(0), F(1, 12), F(0)],
      [F(-1, 12), F(0), F(1, 80)]]
Kinv = [[F(9, 4), F(0), F(15)], [F(0), F(12), F(0)],
        [F(15), F(0), F(180)]]
J = [[expectation(mul(a, b)) for b in b0] for a in h]
L = matmul(J, Kinv)
Eh = [[expectation(mul(a, b)) for b in h] for a in h]
C = sub(Eh, matmul(L, transpose(J)))
hp = [add(a, *[scale(b, -l) for b, l in zip(b0, row)])
      for a, row in zip(h, L)]
D = [[spectral_cross(j, k) for k in range(3)] for j in range(3)]
T = sub(K0, matmul(matmul(transpose(D), Kinv), D))
m = sum((L[i][j] * D[j][i] for i in range(3) for j in range(3)), Interval(0))
error_square = 3 * sum((T[i][j] * C[j][i] for i in range(3) for j in range(3)), Interval(0))
identity = [[F(int(i == j)) for j in range(3)] for i in range(3)]
checks = {
    "K0_inverse": matmul(K0, Kinv) == identity,
    "marginal_K0": [[expectation(mul(a, b)) for b in b0] for a in b0] == K0,
    "marginal_centered": all(expectation(a) == 0 for a in b0),
    "orthogonal_projection": all(expectation(mul(a, b)) == 0 for a in hp for b in b0),
    "residual_covariance": C == [[expectation(mul(a, b)) for b in hp] for a in hp],
    "main_above_21_over_10000": m.lo > F(21, 10000),
    "error_square_nonnegative_lower": error_square.lo >= 0,
    "error_square_below_1_over_250000": error_square.hi < F(1, 250000),
}
failures = [key for key, passed in checks.items() if not passed]
certificate = {
    "status": "PASS" if not failures else "FAIL", "arithmetic": "exact fractions and outward rational intervals",
    "scope": "Arithmetic in L593 only; the analytic C1 cutoff and universal-law argument are in its proof.",
    "spectral_taylor_degree": 20,
    "spectral_remainder": "2 / ((N+1)! * 2^(j+k+N+1) * (j+k+N+2))",
    "polynomials_on_ellipse": {name: polynomial_record(p) for name, p in
                               [("A", A), ("B", B), ("Ax", Ax), ("Ay", Ay), ("Bx", Bx), ("By", By),
                                ("h0", h[0]), ("h1", h[1]), ("h2", h[2])]},
    "K0": K0, "K0_inverse": Kinv, "J": J, "L": L,
    "E_hh_transpose": Eh, "C": C, "D_intervals": D, "T_intervals": T,
    "main_interval": m, "error_square_interval": error_square,
    "outward_summary": {"main": coarse(m), "error_square": coarse(error_square)},
    "thresholds": {"main_required_strictly_above": F(21, 10000),
                   "error_square_required_strictly_below": F(1, 250000),
                   "derivative_mean_strictly_above": F(1, 10000)},
    "checks": checks, "failures": failures,
}
path = Path(__file__).with_name("exact_completion_separator.json")
path.write_text(json.dumps(serial(certificate), indent=2) + "\n")
print(json.dumps(serial({"status": certificate["status"], "actual_outward_bounds": certificate["outward_summary"],
                         "required_bounds": certificate["thresholds"], "failures": failures})))
print(f"Full exact certificate: {path}")
raise SystemExit(bool(failures))
