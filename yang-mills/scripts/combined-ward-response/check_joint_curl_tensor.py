"""Exact integer-interval certificate for L127's necessary curl test.

Run from the notebook: python3 scripts/combined-ward-response/check_joint_curl_tensor.py
All load-bearing arithmetic uses integers/Fraction/isqrt, never libm.
"""
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

SCALE = 10**30
N = 256


def ceildiv(a, b):
    return -((-a) // b)


class I:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = lo, lo if hi is None else hi

    @staticmethod
    def rat(v):
        v = F(v)
        return I(v.numerator * SCALE // v.denominator,
                 ceildiv(v.numerator * SCALE, v.denominator))

    def __add__(self, other):
        return I(self.lo + other.lo, self.hi + other.hi)

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        vals = [a * b for a in (self.lo, self.hi)
                for b in (other.lo, other.hi)]
        return I(min(vals) // SCALE, ceildiv(max(vals), SCALE))

    def __truediv__(self, other):
        assert other.lo > 0
        vals = [(a * SCALE, b) for a in (self.lo, self.hi)
                for b in (other.lo, other.hi)]
        return I(min(a // b for a, b in vals),
                 max(ceildiv(a, b) for a, b in vals))

    def sqrt(self):
        assert self.lo >= 0
        lo = math.isqrt(self.lo * SCALE)
        hi = math.isqrt(self.hi * SCALE)
        hi += hi * hi < self.hi * SCALE
        return I(lo, hi)

    def data(self):
        return [str(self.lo), str(self.hi)]


def atan_bounds(q, terms):
    s = sum(((-1)**j * F(1, (2*j+1)*q**(2*j+1))
             for j in range(terms)), F(0))
    following = (-1)**terms * F(1, (2*terms+1)*q**(2*terms+1))
    return min(s, s + following), max(s, s + following)


def cosine(t):
    term = total = I.rat(1)
    t2 = t*t
    for j in range(1, 48):
        term = -(term*t2) / I.rat((2*j-1)*(2*j))
        total = total + term
    rem = I.rat(F(4**96, math.factorial(96))).hi
    return I(max(-SCALE, total.lo-rem), min(SCALE, total.hi+rem))


def transpose(a):
    return list(map(list, zip(*a)))


def matmul(a, b):
    return [[sum((x*y for x, y in zip(row, col)), F(0))
             for col in zip(*b)] for row in a]


def exact_stencil_checks():
    # Rational points on d^2/4+eta^2=1; all three planes retained.
    choices = [(F(6, 5), F(4, 5)), (F(8, 5), F(3, 5)),
               (F(24, 13), F(5, 13))]
    records = []
    for x, A in choices:
        for y, B in choices:
            for z, C in choices:
                lam = x*x+y*y+z*z
                normal = [z, -y, x]
                p = [[F(i == j)-normal[i]*normal[j]/lam
                      for j in range(3)] for i in range(3)]
                np = [F(0), -B, F(0)]
                pp = [[-(np[i]*normal[j]+normal[i]*np[j])/lam
                       +normal[i]*normal[j]*2*y*B/lam**2
                       for j in range(3)] for i in range(3)]
                base = [[A*B*B*x, F(0), F(0)],
                        [F(0), A*C*C*x, F(0)],
                        [-A*B*B*z, A*C*C*y, F(0)]]
                bp = [[-A*B*y*x/2, F(0), F(0)],
                      [F(0), F(0), F(0)],
                      [A*B*y*z/2, A*C*C*B, F(0)]]
                a, b = matmul(bp, p), matmul(base, pp)
                gp = [[a[i][j]+b[i][j] for j in range(3)]
                      for i in range(3)]
                f2, f3 = [2*A*y, 2*A*z, F(0)], [-2*B*x, F(0), 2*B*z]
                def pair(v, w):
                    return sum((v[i]*gp[i][j]*w[j]
                                for i in range(3) for j in range(3)), F(0))
                actual = -(pair(f3, f2)-pair(f2, f3))/(2*lam)
                required = -A*A*B*B*z*z/lam * (
                    y*y+(y*y-z*z)*(x*x+z*z)/(2*lam))
                records.append({"d": list(map(str, (x, y, z))),
                                "actual": str(actual), "required": str(required),
                                "residual": str(actual-required)})
    return records


def main():
    al, au = atan_bounds(5, 60)
    bl, bu = atan_bounds(239, 20)
    pi_lo, pi_hi = 16*al-4*bu, 16*au-4*bl
    assert F(3) < pi_lo <= pi_hi < F(22, 7)
    pi = I(I.rat(pi_lo).lo, I.rat(pi_hi).hi)
    two, four, six, eight = (I.rat(v) for v in (2, 4, 6, 8))
    nodes = []
    xs = []
    for j in range(N):
        theta = pi * I.rat(F(2*j+1, 2*N))
        cos = cosine(theta)
        v = two-two*cos
        v = I(max(0, v.lo), min(4*SCALE, v.hi))
        assert v.lo > 0
        xs.append(v)
        nodes.append({"index": j, "theta": theta.data(),
                      "cos": cos.data(), "d_squared": v.data()})
    total = I.rat(0)
    points = []
    for j, x in enumerate(xs):
        a = I.rat(1)-x/four
        for m, z in enumerate(xs):
            k = x+z
            root = (k*(k+four)).sqrt()
            value = a*z/eight * (k+four-(k*k+six*k+two*z)/root)
            points.append([j, m, *value.data()])
            total = total+value
    midpoint_lo = F(total.lo, N*N*SCALE)
    midpoint_hi = F(total.hi, N*N*SCALE)
    # C_theta2 <=70, C_theta4 <=108; pi^2<10.
    quadrature = F(1780, 24*N*N)
    integral_lo, integral_hi = midpoint_lo-quadrature, midpoint_hi+quadrature
    tau_lo, tau_hi = -integral_hi, -integral_lo
    checks = exact_stencil_checks()
    failures = []
    if not all(r["residual"] == "0" for r in checks):
        failures.append("exact complete-plane derivative formula")
    if not F(7, 1000) < tau_lo <= tau_hi < F(1, 100):
        failures.append("required 7/1000 < tau < 1/100")
    cert = {"schema": "joint-curl-tensor-exact-interval-v1", "n": N,
            "scale": str(SCALE), "method": "exact scaled-integer intervals",
            "pi_proof": {"identity": "16 atan(1/5)-4 atan(1/239)",
                         "terms": [60, 20], "lower": str(pi_lo),
                         "upper": str(pi_hi), "scaled_interval": pi.data()},
            "cosine_proof": {"terms": 48,
                             "remainder_bound": str(F(4**96, math.factorial(96)))},
            "nodes": nodes, "points": points, "total": total.data(),
            "exact_stencil_checks": checks,
            "bounds": {"midpoint_lower": str(midpoint_lo),
                       "midpoint_upper": str(midpoint_hi),
                       "second_derivative_bounds": [70, 108],
                       "quadrature_error": str(quadrature),
                       "integral_lower": str(integral_lo),
                       "integral_upper": str(integral_hi),
                       "tau_lower": str(tau_lo), "tau_upper": str(tau_hi),
                       "required": "7/1000 < tau < 1/100"},
            "failures": failures,
            "qualification": "Universal stencil test; no actual-probe sign."}
    path = Path(__file__).with_name("joint-curl-tensor-certificate.json")
    path.write_text(json.dumps(cert, indent=2)+"\n")
    print(f"Exact stencil checks: {len(checks)}; nodes: {N*N}")
    print(f"tau interval: ({float(tau_lo):.12f}, {float(tau_hi):.12f}); "
          "required (0.007, 0.010)")
    print(f"Quadrature error <= {float(quadrature):.12f}; failures: {failures}")
    print(f"Full certificate: {path}")
    if failures:
        raise SystemExit(1)


def audit():
    """Replay every saved input and midpoint record, without printing them."""
    path = Path(__file__).with_name("joint-curl-tensor-certificate.json")
    cert = json.loads(path.read_text())
    assert cert["n"] == N and cert["scale"] == str(SCALE)
    al, au = atan_bounds(5, 60)
    bl, bu = atan_bounds(239, 20)
    pi_lo, pi_hi = 16*al-4*bu, 16*au-4*bl
    assert cert["pi_proof"]["lower"] == str(pi_lo)
    assert cert["pi_proof"]["upper"] == str(pi_hi)
    pi = I(I.rat(pi_lo).lo, I.rat(pi_hi).hi)
    two, four, six, eight = (I.rat(v) for v in (2, 4, 6, 8))
    xs = []
    assert len(cert["nodes"]) == N
    for j, row in enumerate(cert["nodes"]):
        theta = pi * I.rat(F(2*j+1, 2*N))
        c = cosine(theta)
        x = two-two*c
        x = I(max(0, x.lo), min(4*SCALE, x.hi))
        assert row == {"index": j, "theta": theta.data(),
                       "cos": c.data(), "d_squared": x.data()}
        assert x.lo > 0
        xs.append(x)
    assert len(cert["points"]) == N*N
    total = I.rat(0)
    for j, x in enumerate(xs):
        for m, z in enumerate(xs):
            k = x+z
            root = (k*(k+four)).sqrt()
            value = (I.rat(1)-x/four)*z/eight * (
                k+four-(k*k+six*k+two*z)/root)
            assert cert["points"][j*N+m] == [j, m, *value.data()]
            total = total+value
    assert cert["total"] == total.data()
    b = cert["bounds"]
    midpoint_lo, midpoint_hi = F(total.lo, N*N*SCALE), F(total.hi, N*N*SCALE)
    error = F(1780, 24*N*N)
    tau_lo, tau_hi = -midpoint_hi-error, -midpoint_lo+error
    required_values = {"midpoint_lower": midpoint_lo, "midpoint_upper": midpoint_hi,
                       "quadrature_error": error, "integral_lower": -tau_hi,
                       "integral_upper": -tau_lo, "tau_lower": tau_lo,
                       "tau_upper": tau_hi}
    for key, value in required_values.items():
        assert b[key] == str(value)
    assert F(7, 1000) < tau_lo <= tau_hi < F(1, 100)
    assert cert["exact_stencil_checks"] == exact_stencil_checks()
    assert not cert["failures"]
    result = {"certificate": path.name, "all_nodes_checked": N,
              "all_points_checked": N*N, "exact_matrix_checks": 27,
              "tau_lower": str(tau_lo), "tau_upper": str(tau_hi),
              "required": "7/1000 < tau < 1/100", "failures": [],
              "qualification": "Full saved-record replay, using the same arithmetic implementation."}
    audit_path = path.with_name("joint-curl-tensor-audit.json")
    audit_path.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Saved-record audit: {N} inputs, {N*N} points, 27 matrices; failures: []")
    print(f"tau in ({float(tau_lo):.12f}, {float(tau_hi):.12f}); required (0.007, 0.010)")
    print(f"Audit: {audit_path}")


if __name__ == "__main__":
    if sys.argv[1:] == ["--audit"]:
        audit()
    elif not sys.argv[1:]:
        main()
    else:
        raise SystemExit("Usage: check_joint_curl_tensor.py [--audit]")
