"""Fixed rational scalar chain; no p-adic approximations or external packages."""
from fractions import Fraction as F
from pathlib import Path
from math import gcd, lcm
import json

HERE = Path(__file__).resolve().parent


def scalar(q):
    q = F(q)
    return [q.numerator, q.denominator]


def point(p):
    return None if p is None else [scalar(c) for c in p]


def on_curve(p):
    if p is None:
        return True
    x, y = p
    return y*y+y == x*x*x+x*x-2*x


def add(p, q):
    assert on_curve(p) and on_curve(q)
    if p is None or q is None:
        return (q if p is None else p), {"branch": "identity"}
    x, y = p
    u, v = q
    if x == u and y+v+1 == 0:
        return None, {"branch": "inverse", "inverse_sum": scalar(y+v+1)}
    if p == q:
        den = 2*y+1
        assert den != 0
        slope = (3*x*x+2*x-2)/den
        intercept = (-x*x*x-2*x-y)/den
        branch = "tangent"
    else:
        den = u-x
        assert den != 0
        slope = (v-y)/den
        intercept = (y*u-v*x)/den
        branch = "chord"
    rx = slope*slope-1-x-u
    ry = -slope*rx-intercept-1
    r = rx, ry
    assert on_curve(r)
    return r, {"branch": branch, "denominator": scalar(den),
               "slope": scalar(slope), "intercept": scalar(intercept)}


def valuation(n):
    assert n != 0
    n = abs(n)
    e = 0
    while n % 7 == 0:
        n //= 7
        e += 1
    return e


def val_data(q):
    q = F(q)
    a, b = valuation(q.numerator), valuation(q.denominator)
    return {"fraction": scalar(q), "numerator_v7": a,
            "denominator_v7": b, "v7": a-b}


def main():
    points = {1: (F(0), F(0))}
    rows = []
    for a, b in [(1, 1), (2, 1), (3, 3), (6, 6), (12, 1)]:
        r, details = add(points[a], points[b])
        points[a+b] = r
        rows.append({"left_scalar": a, "right_scalar": b,
                     "left": point(points[a]), "right": point(points[b]),
                     "output_scalar": a+b, "output": point(r), **details})
    w = points[13]
    assert w is not None
    x, y = w
    t = -x/y
    scale = lcm(x.denominator, y.denominator)
    raw = [int(x*scale), int(y*scale), scale]
    common = gcd(gcd(abs(raw[0]), abs(raw[1])), raw[2])
    primitive = [a//common for a in raw]
    X, Y, Z = primitive
    assert Y*Y*Z+Y*Z*Z == X**3+X*X*Z-2*X*Z*Z
    cert = {"schema": "known-point-seven-307-v1",
            "model": [0, 1, 1, -2, 0], "prime": 7, "P": point(points[1]),
            "chain": rows, "W": point(w),
            "valuations": {"x": val_data(x), "y": val_data(y), "t": val_data(t)},
            "projective": {"scale": scale, "common_gcd": common,
                           "primitive": primitive,
                           "reduction": [a % 7 for a in primitive]},
            "threshold": {"required_t_v7": 1, "actual_t_v7": val_data(t)["v7"],
                          "met": val_data(t)["v7"] == 1}}
    out = HERE / "certificate.json"
    out.write_text(json.dumps(cert, indent=2)+"\n")
    print(f"built {out}: 5 full chain branches; t valuation "
          f"actual={val_data(t)['v7']}, required=1; failures=0")


if __name__ == "__main__":
    main()
