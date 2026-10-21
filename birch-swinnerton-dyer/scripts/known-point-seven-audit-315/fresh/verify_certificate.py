"""Independent exact replay on the short model, including 13 sequential sums.

Imports no producer. Every saved input/output is replayed. Complete traces
and exact valuation quotients are written to verification.json.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import gcd
import hashlib
import json

HERE = Path(__file__).resolve().parent
A, B = -Q(7, 3), Q(107, 108)


def encode(q):
    return [q.numerator, q.denominator]


def read_q(v):
    assert isinstance(v, list) and len(v) == 2
    a, b = v
    assert type(a) is int and type(b) is int and b > 0 and gcd(abs(a), b) == 1
    return Q(a, b)


def decode(p):
    return None if p is None else tuple(read_q(c) for c in p)


def short(p):
    return None if p is None else (p[0]+Q(1, 3), p[1]+Q(1, 2))


def original(p):
    return None if p is None else [encode(p[0]-Q(1, 3)), encode(p[1]-Q(1, 2))]


def good(p):
    return p is None or p[1]**2 == p[0]**3+A*p[0]+B


def short_sum(p, q):
    assert good(p) and good(q)
    if p is None or q is None:
        return (q if p is None else p), {"branch": "identity"}
    x, y = p
    u, v = q
    if x == u and y == -v:
        return None, {"branch": "inverse"}
    if p == q:
        denominator = 2*y
        numerator = 3*x*x+A
        branch = "tangent"
    else:
        denominator = u-x
        numerator = v-y
        branch = "chord"
    assert denominator != 0
    m = numerator/denominator
    r = (m*m-x-u, y+m*((m*m-x-u)-x))
    # Third line intersection has this y-coordinate; negate it for the sum.
    r = r[0], -r[1]
    assert good(r)
    return r, {"branch": branch, "denominator": encode(denominator),
               "slope": encode(m)}


def valuation(n):
    assert n != 0
    unit, e = abs(n), 0
    while unit % 7 == 0:
        unit, e = divmod(unit, 7)[0], e+1
    assert unit % 7 != 0 and abs(n) == 7**e*unit
    return e, unit


def main():
    path = HERE / "certificate.json"
    cert = json.loads(path.read_text())
    assert cert["schema"] == "known-point-seven-307-v1"
    assert cert["model"] == [0, 1, 1, -2, 0] and cert["prime"] == 7
    P = (Q(0), Q(0))
    assert decode(cert["P"]) == P
    p = short(P)
    assert good(p)
    replay = {1: p}
    trace = []
    schedule = [(1, 1), (2, 1), (3, 3), (6, 6), (12, 1)]
    assert len(cert["chain"]) == len(schedule)
    for row, (a, b) in zip(cert["chain"], schedule):
        assert (row["left_scalar"], row["right_scalar"], row["output_scalar"]) == (a, b, a+b)
        assert short(decode(row["left"])) == replay[a]
        assert short(decode(row["right"])) == replay[b]
        r, details = short_sum(replay[a], replay[b])
        assert short(decode(row["output"])) == r
        assert row["branch"] == details["branch"]
        assert row["denominator"] == details["denominator"]
        assert row["slope"] == details["slope"]
        x, y = decode(row["left"])
        m = read_q(row["slope"])
        # A line in the original model must have this intercept; verify
        # both endpoints (or the tangent) and the sum's negated endpoint.
        intercept = y-m*x
        assert read_q(row["intercept"]) == intercept
        u, v = decode(row["right"])
        assert v == m*u+intercept
        if a == b:
            assert (2*y+1)*m == 3*x*x+2*x-2
        rx, ry = decode(row["output"])
        assert -ry-1 == m*rx+intercept
        replay[a+b] = r
        trace.append({"left_scalar": a, "right_scalar": b,
                      "output": original(r), **details})
    seq = None
    sequential = []
    for i in range(1, 14):
        seq, details = short_sum(seq, p)
        sequential.append({"scalar": i, "output": original(seq), **details})
    assert seq == replay[13]
    assert original(seq) == cert["W"] and seq is not None
    x, y = decode(cert["W"])
    assert y != 0
    t = -x/y
    valuations = {}
    for name, q in [("x", x), ("y", y), ("t", t)]:
        a, unit_a = valuation(q.numerator)
        b, unit_b = valuation(q.denominator)
        saved = cert["valuations"][name]
        assert saved == {"fraction": encode(q), "numerator_v7": a,
                         "denominator_v7": b, "v7": a-b}
        valuations[name] = {**saved, "numerator_abs_unit": unit_a,
                            "denominator_unit": unit_b}
    proj = cert["projective"]
    X, Y, Z = proj["primitive"]
    assert type(Z) is int and Z > 0 and gcd(gcd(abs(X), abs(Y)), Z) == 1
    assert Q(X, Z) == x and Q(Y, Z) == y
    assert Y*Y*Z+Y*Z*Z == X**3+X*X*Z-2*X*Z*Z
    assert proj["scale"] == x.denominator*y.denominator//gcd(x.denominator, y.denominator)
    raw = [int(x*proj["scale"]), int(y*proj["scale"]), proj["scale"]]
    assert proj["common_gcd"] == gcd(gcd(abs(raw[0]), abs(raw[1])), raw[2])
    assert [a//proj["common_gcd"] for a in raw] == [X, Y, Z]
    reduction = [X % 7, Y % 7, Z % 7]
    assert reduction == proj["reduction"]
    assert reduction[0] == reduction[2] == 0 and reduction[1] != 0
    assert valuations["x"]["v7"] == -2 and valuations["y"]["v7"] == -3
    actual = valuations["t"]["v7"]
    assert cert["threshold"] == {"required_t_v7": 1, "actual_t_v7": actual, "met": actual == 1}
    report = {"status": "PASS", "failures": [],
              "certificate_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
              "short_model": {"a": encode(A), "b": encode(B)},
              "binary_replay": trace, "sequential_replay": sequential,
              "W": cert["W"], "valuations": valuations,
              "projective": proj, "required_t_v7": 1, "actual_t_v7": actual,
              "threshold_met": actual == 1}
    out = HERE / "verification.json"
    out.write_text(json.dumps(report, indent=2)+"\n")
    print(f"PASS: 5 binary and 13 sequential branches; projective reduction O; "
          f"v7(x)=-2, v7(y)=-3, v7(t)={actual} (required 1); failures=0; {out}")


if __name__ == "__main__":
    main()
