#!/usr/bin/env python3
"""Audit every C614a certificate cell; preserve the original certificate.

Replay binary64 endpoints and independently enclose each box with 50-digit
directed Decimal arithmetic, longer Taylor series and a positive-series H.
This is a second implementation, not a formal verification of either runtime.
Full per-cell evidence and failures go to two-packet-audit.json.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as R
from functools import lru_cache
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform
import sys
import time

BASE = Path(__file__).resolve().parent
LOW = Context(prec=50, rounding=ROUND_FLOOR)
HIGH = Context(prec=50, rounding=ROUND_CEILING)


def decimal(x):
    return D.from_float(x) if isinstance(x, float) else D(x)


class Q:
    def __init__(self, lo, hi=None):
        if isinstance(lo, R):
            assert hi is None
            self.lo = LOW.divide(D(lo.numerator), D(lo.denominator))
            self.hi = HIGH.divide(D(lo.numerator), D(lo.denominator))
        else:
            self.lo = decimal(lo)
            self.hi = decimal(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = other if isinstance(other, Q) else Q(other)
        return Q(LOW.add(self.lo, other.lo), HIGH.add(self.hi, other.hi))

    __radd__ = __add__

    def __neg__(self):
        # copy_negate is exact and does not use the default Decimal context.
        return Q(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, other):
        return self + -(other if isinstance(other, Q) else Q(other))

    def __rsub__(self, other):
        return Q(other) + -self

    def __mul__(self, other):
        other = other if isinstance(other, Q) else Q(other)
        pairs = [(a, b) for a in (self.lo, self.hi)
                 for b in (other.lo, other.hi)]
        return Q(min(LOW.multiply(a, b) for a, b in pairs),
                 max(HIGH.multiply(a, b) for a, b in pairs))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = other if isinstance(other, Q) else Q(other)
        assert other.lo > 0
        return self * Q(LOW.divide(D(1), other.hi),
                        HIGH.divide(D(1), other.lo))

    def square(self):
        lower = (D(0) if self.lo <= 0 <= self.hi else
                 min(LOW.multiply(self.lo, self.lo),
                     LOW.multiply(self.hi, self.hi)))
        return Q(lower, max(HIGH.multiply(self.lo, self.lo),
                            HIGH.multiply(self.hi, self.hi)))

    def nonnegative(self):
        return Q(max(D(0), self.lo), self.hi)


def arctan(q, count):
    value = sum((R((-1)**k, (2*k+1)*q**(2*k+1))
                 for k in range(count)), R())
    remainder = R((-1)**count, (2*count+1)*q**(2*count+1))
    return min(value, value+remainder), max(value, value+remainder)


al, ah = arctan(5, 80)
bl, bh = arctan(239, 24)
PI_RATIONAL = (16*al-4*bh, 16*ah-4*bl)
PI = Q(Q(PI_RATIONAL[0]).lo, Q(PI_RATIONAL[1]).hi)
assert PI_RATIONAL[0] > R(157, 50)
assert PI_RATIONAL[1]**2 < 10
assert R(22, 7)**100 / math.factorial(100) < R(1, 10**100)
assert R(3, math.factorial(51)) < R(1, 10**65)
assert R(2)*4**100 / math.factorial(101) < R(1, 10**90)


@lru_cache(maxsize=None)
def trig_endpoint(a):
    exact = R.from_float(a)
    quotient = (exact+1)//2
    reduced = exact-2*quotient
    assert -1 <= reduced <= 1
    # Verify exact reduction also in the original binary64 implementation.
    original = a-2*math.floor((a+1)/2)
    assert R.from_float(original) == reduced
    x = PI*Q(reduced)
    negative_square = -x.square()
    sine = st = x
    cosine = ct = Q(1)
    for k in range(1, 50):
        st = st*negative_square/((2*k)*(2*k+1))
        ct = ct*negative_square/((2*k)*(2*k-1))
        sine, cosine = sine+st, cosine+ct
    tail = Q('-1e-100', '1e-100')
    return sine+tail, cosine+tail


@lru_cache(maxsize=None)
def trig(lo, hi):
    sl, cl = trig_endpoint(lo)
    sh, ch = trig_endpoint(hi)
    slo, shi = min(sl.lo, sh.lo), max(sl.hi, sh.hi)
    clo, chi = min(cl.lo, ch.lo), max(cl.hi, ch.hi)
    # Integer and half-integer extrema, with exact dyadic comparisons.
    for k in range(math.floor(lo)-1, math.ceil(hi)+1):
        if lo <= k <= hi:
            if k % 2:
                clo = D(-1)
            else:
                chi = D(1)
        if lo <= k+0.5 <= hi:
            if k % 2:
                slo = D(-1)
            else:
                shi = D(1)
    return Q(max(D(-1), slo), min(D(1), shi)), Q(max(D(-1), clo), min(D(1), chi))


@lru_cache(maxsize=None)
def exponential(x):
    assert 0 <= x <= 16
    y = Q(x)/16
    total = term = Q(1)
    for k in range(1, 51):
        term = term*y/k
        total = total+term
    total = total+Q(0, '1e-65')
    for _ in range(4):
        total = total.square()
    return total


def hyperbolic(b):
    assert b.lo >= 0
    x = PI*b
    ex = Q(exponential(max(D(0), x.lo)).lo, exponential(x.hi).hi)
    reciprocal = Q(1)/ex
    return ((ex-reciprocal)/2).nonnegative(), (ex+reciprocal)/2


@lru_cache(maxsize=None)
def h_endpoint(b):
    # Independent positive sinh(x)/x series for all needed 0<=b<=1.
    assert 0 <= b <= 1
    x2 = (PI*Q(b)).square()
    total = term = Q(1)
    for k in range(1, 50):
        term = term*x2/((2*k)*(2*k+1))
        total = total+term
    return (total+Q(0, '1e-90')).square()


def h(b):
    assert b.lo >= 0
    return Q(max(D(1), h_endpoint(b.lo).lo), h_endpoint(b.hi).hi)


def f(a, b, sine, cosine):
    sinh, cosh = hyperbolic(b)
    denominator = PI*(a.square()+b.square())
    real = (a*sine*cosh+b*cosine*sinh)/denominator
    imag = (a*cosine*sinh-b*sine*cosh)/denominator
    return real.square()-imag.square()


def defect(box):
    a, u, r = [Q(*pair) for pair in box]
    v = (u*r).nonnegative()
    bminus = (u*(1-r).nonnegative()).nonnegative()
    bplus = (u*(1+r)).nonnegative()
    sine, cosine = trig(*box[0])
    return (2*(h((2*u).nonnegative())-1)
            +8*(h((2*v).nonnegative())-1)
            +8*(f(a, bminus, sine, cosine)+f(a, bplus, sine, cosine)))


def audit(report):
    raw = (BASE/'two-packet-cover.json').read_bytes()
    cert = json.loads(raw)
    report['input_sha256'] = hashlib.sha256(raw).hexdigest()
    script = BASE/'certify_two_packet.py'
    assert hashlib.sha256(script.read_bytes()).hexdigest() == cert['script_sha256']
    spec = importlib.util.spec_from_file_location('original_two_packet', script)
    original = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(original)
    root = [[0.5, 4.0], [3/64, 0.5], [0.0, 1.0]]
    assert cert['root'] == root
    assert not cert['failures'] and not cert['uncovered'] and not cert['high_depth']['failures']
    leaves = {row['address']: row for row in cert['accepted']}
    splits = {row['address']: row for row in cert['splits']}
    assert len(leaves) == len(cert['accepted'])
    assert len(splits) == len(cert['splits'])
    assert not (leaves.keys() & splits.keys())
    pending = [('', root)]
    seen_leaves, seen_splits = set(), set()
    while pending:
        address, box = pending.pop()
        if address in splits:
            row = splits[address]
            axis, mid = row['axis'], row['mid']
            assert axis in (0, 1, 2) and box[axis][0] < mid < box[axis][1]
            assert math.isfinite(mid)
            for bit, pair in [('0', [box[axis][0], mid]), ('1', [mid, box[axis][1]])]:
                child = [list(p) for p in box]
                child[axis] = pair
                pending.append((address+bit, child))
            seen_splits.add(address)
            continue
        assert address in leaves, ('uncovered', address, box)
        row = leaves[address]
        assert row['box'] == box
        replay = original.defect(box)
        assert (replay.lo, replay.hi) == (row['lower'], row['upper'])
        assert R.from_float(replay.lo) > R(1, 100000)
        bound = defect(box)
        assert bound.lo > D('0.00001'), (address, str(bound.lo))
        report['compact'].append({'address': address, 'box': box,
                                  'binary64_lower': replay.lo,
                                  'decimal_lower': str(bound.lo),
                                  'decimal_upper': str(bound.hi)})
        seen_leaves.add(address)
    assert seen_leaves == leaves.keys() and seen_splits == splits.keys()
    assert len(leaves) == len(splits)+1 == 8553
    grid = [0.5+3.5*k/256 for k in range(257)]
    assert cert['high_depth']['grid'] == grid
    cells = cert['high_depth']['accepted']
    assert len(cells) == 256
    for k, row in enumerate(cells):
        lo, hi = grid[k:k+2]
        assert row['a'] == [lo, hi]
        sine, cosine = original.trig_range(lo, hi)
        replay = 16*(original.h_at(0.5)+original.f_range(
            original.I(lo, hi), original.I(0.5), sine, cosine))-20
        assert (replay.lo, replay.hi) == (row['lower'], row['upper'])
        assert replay.lo > 3
        sine, cosine = trig(lo, hi)
        bound = 16*(h_endpoint(D('0.5'))+f(Q(lo, hi), Q('0.5'), sine, cosine))-20
        assert bound.lo > 3, (k, str(bound.lo))
        report['large_depth'].append({'a': [lo, hi], 'binary64_lower': replay.lo,
                                      'decimal_lower': str(bound.lo),
                                      'decimal_upper': str(bound.hi)})
    coefficient = R(8, 3)*R(157, 50)**2-25-R(100, 253)-R(32, 171)
    spacing = R(2, 5)-(R(80, 3)+R(32, 171))/400
    assert coefficient > R(7, 10) and spacing > R(3, 10)
    report['constants'] = {'small_depth': str(coefficient), 'required': '7/10',
                           'small_spacing': str(spacing), 'spacing_required': '3/10',
                           'pi_lower': str(PI_RATIONAL[0]), 'pi_upper': str(PI_RATIONAL[1]),
                           'trig_tail_upper': '1e-100', 'exp_tail_upper': '1e-65',
                           'sinh_over_x_tail_upper': '1e-90'}
    report['summary'] = {'complete': True, 'failures': 0,
                         'compact_leaves': len(seen_leaves), 'splits': len(seen_splits),
                         'large_depth_cells': len(cells),
                         'binary64_compact_minimum': min(x['binary64_lower'] for x in report['compact']),
                         'decimal_compact_minimum': str(min(D(x['decimal_lower']) for x in report['compact'])),
                         'compact_required_floor': '1/100000',
                         'binary64_large_depth_minimum': min(x['binary64_lower'] for x in report['large_depth']),
                         'decimal_large_depth_minimum': str(min(D(x['decimal_lower']) for x in report['large_depth'])),
                         'large_depth_required_floor': '3',
                         'all_binary64_bounds_replayed_exactly': True,
                         'all_partition_nodes_checked': True}


def main():
    started = time.monotonic()
    report = {'kind': 'independent code/coverage/arithmetic audit of C614a',
              'qualification': 'same research notebook; separate invocation and implementation, no external or formal verification',
              'runtime': {'python': sys.version, 'platform': platform.platform(),
                          'decimal_precision': 50, 'roundings': ['ROUND_FLOOR', 'ROUND_CEILING']},
              'audit_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'summary': {'complete': False}, 'failures': [], 'compact': [], 'large_depth': []}
    try:
        audit(report)
    except Exception as exc:
        report['failures'].append({'type': type(exc).__name__, 'message': str(exc)})
        raise
    finally:
        report['summary']['seconds'] = time.monotonic()-started
        path = BASE/'two-packet-audit.json'
        path.write_text(json.dumps(report, separators=(',', ':'))+'\n')
        print(json.dumps(report['summary'], indent=2))
        print('Failures:', report['failures'])
        print('Full audit certificate:', path)


if __name__ == '__main__':
    main()
