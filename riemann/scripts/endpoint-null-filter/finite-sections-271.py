#!/usr/bin/env python3
"""Exact finite sections of L990, with dyadic outward solution bounds.

No infinite-horizon assertion is made. The certificate contains every
primitive integer row and every interval, rather than just samples.
--verify checks rows by the defining finite polynomial sum (independent
of the generation recurrence) and all interval inclusions with Fraction.
Run from riemann: python3 scripts/endpoint-null-filter/finite-sections-271.py
Then: .../finite-sections-271.py --verify
The retained first enclosure run is reproducible with --precision 256.
"""
import argparse
from fractions import Fraction
import json
from math import factorial, gcd, lcm
from pathlib import Path
import sys

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
CERT = ROOT / "finite-sections-271.json"
REPLAY = ROOT / "finite-sections-replay-271.json"
START, END, PRECISION = 32, 1024, 1024
HORIZONS = (64, 128, 256, 512, 1024)


def primitive(v):
    g = gcd(*v)
    return tuple(a // g for a in v) if g else tuple(v)


def laguerre_recurrence(n, u):
    # q_k = k! L_k^(2)(u); retain degrees n-1,n,n+1.
    previous, current = 1, 3 - u
    found = {}
    for k in range(1, n + 1):
        if k >= n - 1:
            found[k] = current
        previous, current = current, (2*k+3-u)*current-k*(k+2)*previous
    found[n+1] = current
    return [found[k] for k in (n-1, n, n+1)]


def laguerre_sum(k, u):
    # Independent definition: k! sum_r (-u)^r binom(k+2,k-r)/r!.
    term = factorial(k) * (k+2)*(k+1)//2
    total = term
    for r in range(k):
        numerator = -term*u*(k-r)
        denominator = (r+1)*(r+3)
        term, remainder = divmod(numerator, denominator)
        assert remainder == 0
        total += term
    return total


def integer_row(n, direct=False):
    degrees = (n-1, n, n+1)
    facts = [factorial(k) for k in degrees]
    denominators = [k*f for k, f in zip(degrees, facts)]
    common = lcm(*denominators)
    rows = []
    for u in (n, 2*n):
        q = [laguerre_sum(k, u) for k in degrees] if direct else laguerre_recurrence(n, u)
        rows.append(primitive([(a-f)*(common//d) for a, f, d in zip(q, facts, denominators)]))
    a, b = rows
    return primitive((a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]))


def rounded_next(d, x, y):
    # x,y are [lo,hi,e] representing [lo,hi]*2**e.
    exponent = min(x[2], y[2])
    terms = []
    for coefficient, interval in zip(d[:2], (x, y)):
        endpoints = [coefficient*t*(1 << (interval[2]-exponent)) for t in interval[:2]]
        terms.append((min(endpoints), max(endpoints)))
    lo, hi = -sum(t[1] for t in terms), -sum(t[0] for t in terms)
    denominator = d[2]
    assert denominator != 0
    if denominator < 0:
        lo, hi, denominator = -hi, -lo, -denominator
    magnitude = max(abs(lo), abs(hi))
    if not magnitude:
        return [0, 0, 0]
    power = magnitude.bit_length()-denominator.bit_length()
    below = magnitude < (denominator << power) if power >= 0 else (magnitude << -power) < denominator
    if below:
        power -= 1
    shift = PRECISION-1-power
    if shift >= 0:
        lo, hi = lo << shift, hi << shift
    else:
        denominator <<= -shift
    return [lo//denominator, -((-hi)//denominator), exponent-shift]


def encode_interval(v):
    return {"lo": str(v[0]), "hi": str(v[1]), "exponent": v[2]}


def decode_interval(v):
    return [int(v["lo"]), int(v["hi"]), v["exponent"]]


def compare_power(integer, exponent, power):
    """Sign of nonnegative integer*2**exponent - 2**power."""
    if exponent <= power:
        right = 1 << (power-exponent)
        return (integer > right)-(integer < right)
    left = integer << (exponent-power)
    return (left > 1)-(left < 1)


def statistics(intervals, complete):
    failures, samples = [], []
    peak_rate = Fraction(0)
    peak_index = START
    for offset, interval in enumerate(intervals):
        k = START+offset
        lo, hi, exponent = interval
        absolute_upper = max(abs(lo), abs(hi))
        if compare_power(absolute_upper, exponent, 4*offset) > 0:
            failures.append(k)
        upper_log2 = (absolute_upper-1).bit_length()+exponent if absolute_upper else None
        if offset and upper_log2 is not None and Fraction(upper_log2, offset) > peak_rate:
            peak_rate, peak_index = Fraction(upper_log2, offset), k
        if k-2 in HORIZONS:
            absolute_lower = lo if lo > 0 else (-hi if hi < 0 else 0)
            lower_log2 = absolute_lower.bit_length()-1+exponent if absolute_lower else None
            required_integer_power = (offset+99)//100
            passed = compare_power(absolute_lower, exponent, required_integer_power) >= 0
            samples.append({"last_row": k-2, "endpoint_index": k,
                "endpoint_log2_abs_lower_floor": lower_log2,
                "endpoint_log2_abs_upper_ceiling": upper_log2,
                "required_lower_power_ceiling": required_integer_power,
                "lower_threshold_pass": passed,
                "max_upper_log2_per_step_so_far": str(peak_rate),
                "max_upper_rate_index": peak_index})
    return {"complete_through_requested_horizon": complete,
        "upper_envelope_base2_rate_required": 4,
        "lower_endpoint_base2_rate_required": "1/100",
        "upper_envelope_failures": failures, "sections": samples,
        "infinite_horizon_verified": False,
        "unpaid": ["eventual nonzero forward pivots or singular-row treatment",
                   "section-independent finite exponential upper bound",
                   "positive infinite exponential limsup"]}


def generate():
    intervals = [[1, 1, 0], [0, 0, 0]]
    rows, failure = [], None
    for n in range(START, END+1):
        d = integer_row(n)
        row = {"n": n, "d": [str(t) for t in d]}
        rows.append(row)
        if d == (0, 0, 0):
            failure = {"n": n, "reason": "undefined exact coefficient vector"}
            break
        if d[2] == 0:
            failure = {"n": n, "reason": "zero forward pivot; implicit system not resolved"}
            break
        intervals.append(rounded_next(d, intervals[-2], intervals[-1]))
    cert = {"task": "finite exact homogeneous sections only", "start": START,
        "last_row_requested": END, "precision_bits": PRECISION,
        "initial_values": [1, 0], "row_definition": "positive primitive multiple of L990 a_n cross b_n",
        "rows": rows, "solution_intervals": [encode_interval(v) for v in intervals],
        "failure": failure, "summary": statistics(intervals, failure is None)}
    CERT.write_text(json.dumps(cert, separators=(",", ":"))+"\n")
    print(json.dumps({"certificate": str(CERT.relative_to(ROOT.parent.parent)),
                      "bytes": CERT.stat().st_size, "failure": failure,
                      "summary": cert["summary"]}, indent=2))


def endpoints(v):
    scale = Fraction(1 << v[2]) if v[2] >= 0 else Fraction(1, 1 << -v[2])
    return [v[0]*scale, v[1]*scale]


def verify():
    cert = json.loads(CERT.read_text())
    assert cert["start"] == START and cert["last_row_requested"] == END
    assert cert["failure"] is None
    assert len(cert["rows"]) == END-START+1
    intervals = [decode_interval(v) for v in cert["solution_intervals"]]
    assert len(intervals) == END-START+3
    assert intervals[:2] == [[1, 1, 0], [0, 0, 0]]
    checked_rows, checked_inclusions = 0, 0
    for i, row in enumerate(cert["rows"]):
        n = START+i
        assert row["n"] == n
        d = tuple(int(t) for t in row["d"])
        assert d == integer_row(n, direct=True), (n, "independent polynomial row mismatch")
        assert d[2] != 0 and gcd(*d) == 1
        checked_rows += 1
        x, y, z = (endpoints(intervals[i+j]) for j in range(3))
        corners = [-(d[0]*a+d[1]*b)/d[2] for a in x for b in y]
        assert z[0] <= min(corners) <= max(corners) <= z[1], (n, "failed rational interval enclosure")
        checked_inclusions += 1
    summary = statistics(intervals, True)
    assert summary == cert["summary"]
    result = {"passed": True, "independent_exact_polynomial_rows_checked": checked_rows,
        "exact_rational_interval_inclusions_checked": checked_inclusions,
        "summary": summary, "scope": "all stored finite rows and bounds; no infinite inference"}
    REPLAY.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"verification": str(REPLAY.relative_to(ROOT.parent.parent)), **result}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--precision", type=int, default=1024)
    args = parser.parse_args()
    if args.precision < 2:
        parser.error("precision must be at least 2 bits")
    PRECISION = args.precision
    if PRECISION != 1024:
        CERT = ROOT / f"finite-sections-271-first-pass-{PRECISION}bit.json"
        REPLAY = ROOT / f"finite-sections-replay-271-{PRECISION}bit.json"
    verify() if args.verify else generate()
