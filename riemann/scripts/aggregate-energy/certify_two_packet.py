#!/usr/bin/env python3
"""Directed binary64 interval cover of the L614 inverse-order case.

No sampled sign is accepted. Every elementary operation is rounded out
with nextafter. Trig/exp use Taylor polynomials with explicit tails;
pi is enclosed by exact rational Machin series. Requires only Python's
standard library. Run from riemann. All accepted boxes and failures are
written to two-packet-cover.json; concise coverage/sign results print.
"""
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import time

assert sys.float_info.radix == 2 and sys.float_info.mant_dig == 53
assert sys.float_info.rounds == 1

def down(x):
    return math.nextafter(x, -math.inf)


def up(x):
    return math.nextafter(x, math.inf)


class I:
    __slots__ = ('lo', 'hi')

    def __init__(self, lo, hi=None):
        self.lo = float(lo)
        self.hi = float(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = other if isinstance(other, I) else I(other)
        return I(down(self.lo + other.lo), up(self.hi + other.hi))

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other if isinstance(other, I) else -I(other))

    def __rsub__(self, other):
        return I(other) + (-self)

    def __mul__(self, other):
        other = other if isinstance(other, I) else I(other)
        values = (self.lo*other.lo, self.lo*other.hi,
                  self.hi*other.lo, self.hi*other.hi)
        return I(down(min(values)), up(max(values)))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = other if isinstance(other, I) else I(other)
        assert other.lo > 0 or other.hi < 0
        return self * I(down(1/other.hi), up(1/other.lo))

    def square(self):
        lo = 0.0 if self.lo <= 0 <= self.hi else down(min(self.lo*self.lo, self.hi*self.hi))
        return I(max(0.0, lo), up(max(self.lo*self.lo, self.hi*self.hi)))

    def nonnegative(self):
        """Only call when nonnegativity is proved independently."""
        return I(max(0.0, self.lo), self.hi)


def atan_bounds(q, count):
    value = sum((Fraction((-1)**k, (2*k+1)*q**(2*k+1))
                 for k in range(count)), Fraction())
    following = Fraction((-1)**count, (2*count+1)*q**(2*count+1))
    return min(value, value+following), max(value, value+following)


al, ah = atan_bounds(5, 48)
bl, bh = atan_bounds(239, 12)
PI_RATIONAL = (16*al-4*bh, 16*ah-4*bl)
PI = I(down(float(PI_RATIONAL[0])), up(float(PI_RATIONAL[1])))
assert Fraction.from_float(PI.lo) < PI_RATIONAL[0]
assert Fraction.from_float(PI.hi) > PI_RATIONAL[1]
# For |x|<=pi, the tails after degree 59/58 are < 1e-50.
assert Fraction(22, 7)**60 / math.factorial(60) < Fraction(1, 10**50)
assert Fraction(22, 7)**60 / math.factorial(60) < Fraction.from_float(1e-49)
# exp(y), 0<=y<=1: tail after degree 24 <=3/25! <1e-24.
assert Fraction(3, math.factorial(25)) < Fraction(1, 10**24)
assert Fraction(3, math.factorial(25)) < Fraction.from_float(1e-24)


@lru_cache(maxsize=None)
def trig_at(a):
    # a is a dyadic endpoint. Reduce sin(pi*a), cos(pi*a) exactly.
    reduced = a - 2*math.floor((a+1)/2)
    assert -1 <= reduced <= 1
    x = PI*reduced
    minus_x2 = -x.square()
    sine = term_s = x
    cosine = term_c = I(1)
    for k in range(1, 30):
        term_s = term_s*minus_x2/((2*k)*(2*k+1))
        term_c = term_c*minus_x2/((2*k-1)*(2*k))
        sine = sine+term_s
        cosine = cosine+term_c
    tail = I(-1e-49, 1e-49)  # strictly wider than the proved tail
    return sine+tail, cosine+tail


@lru_cache(maxsize=None)
def trig_range(lo, hi):
    sl, cl = trig_at(lo)
    sh, ch = trig_at(hi)
    slo, shi = min(sl.lo, sh.lo), max(sl.hi, sh.hi)
    clo, chi = min(cl.lo, ch.lo), max(cl.hi, ch.hi)
    # All extrema are integers (cosine) or half-integers (sine).
    for k in range(math.floor(lo)-1, math.ceil(hi)+1):
        if lo <= k <= hi:
            if k % 2: clo = -1.0
            else: chi = 1.0
        if lo <= k+0.5 <= hi:
            if k % 2: slo = -1.0
            else: shi = 1.0
    return I(max(-1, slo), min(1, shi)), I(max(-1, clo), min(1, chi))


@lru_cache(maxsize=100000)
def exp_at(x):
    assert 0 <= x <= 32
    y = I(x)/32
    total = term = I(1)
    for k in range(1, 25):
        term = term*y/k
        total = total+term
    total = total+I(0, 1e-24)
    for _ in range(5):
        total = total.square()
    return total


def hyperbolic(b):
    assert b.lo >= 0
    x = PI*b
    e = I(exp_at(max(0, x.lo)).lo, exp_at(x.hi).hi)
    inv = I(1)/e
    return ((e-inv)/2).nonnegative(), (e+inv)/2


@lru_cache(maxsize=100000)
def h_at(b):
    if b == 0:
        return I(1)
    x = PI*b
    if b < 1/64:
        # sinh(x)/x = sum x^(2k)/(2k+1)!; x<1/16.
        x2 = x.square()
        total = term = I(1)
        for k in range(1, 10):
            term = term*x2/((2*k)*(2*k+1))
            total = total+term
        # Tail < 2*(1/16)^20/21! <1e-40.
        assert Fraction(2, 16**20*math.factorial(21)) < Fraction(1,10**40)
        assert Fraction(2, 16**20*math.factorial(21)) < Fraction.from_float(1e-40)
        return (total+I(0,1e-40)).square()
    sinh, _ = hyperbolic(I(b))
    return (sinh/x).square()


def h_range(b):
    # H is increasing on nonnegative arguments, by its positive series.
    assert b.lo >= 0
    return I(max(1, h_at(b.lo).lo), h_at(b.hi).hi)


def f_range(a, b, sine, cosine):
    sinh, cosh = hyperbolic(b)
    denominator = PI*(a.square()+b.square())
    real = (a*sine*cosh+b*cosine*sinh)/denominator
    imag = (a*cosine*sinh-b*sine*cosh)/denominator
    return real.square()-imag.square()


def defect(box):
    a, u, r = (I(*pair) for pair in box)
    v = (u*r).nonnegative()
    minus = (u*(1-r).nonnegative()).nonnegative()
    plus = (u*(1+r)).nonnegative()
    sine, cosine = trig_range(a.lo, a.hi)
    return (2*(h_range((2*u).nonnegative())-1)
            +8*(h_range((2*v).nonnegative())-1)
            +8*(f_range(a, minus, sine, cosine)+f_range(a, plus, sine, cosine)))


def main():
    started = time.monotonic()
    # L614 (7) gives E >=16*(H(1/2)+F(a,1/2)) for u>=1/2:
    # AB >=cosh(pi*t), and the multiplier 1+cos(2*pi*a*t)>=0.
    high_accepted, high_failures = [], []
    high_grid = [0.5+3.5*k/256 for k in range(257)]
    for lo, hi in zip(high_grid, high_grid[1:]):
        sine, cosine = trig_range(lo, hi)
        bound = 16*(h_at(0.5)+f_range(I(lo,hi),I(0.5),sine,cosine))-20
        row = {'a':[lo,hi],'lower':bound.lo,'upper':bound.hi}
        (high_accepted if bound.lo > 0 else high_failures).append(row)
    root = ((0.5, 4.0), (3/64, 0.5), (0.0, 1.0))
    stack = [('', root)]
    accepted, splits, failures = [], [], []
    evaluated = 0
    max_boxes = 300000
    while stack and evaluated < max_boxes:
        address, box = stack.pop()
        bound = defect(box)
        evaluated += 1
        if bound.lo > 0:
            accepted.append({'address':address,'box':box,'lower':bound.lo,'upper':bound.hi})
            continue
        if len(address) >= 48 or bound.hi < 0:
            failures.append({'address':address,'box':box,'lower':bound.lo,'upper':bound.hi})
            break
        widths = [b-a for a,b in box]
        scores = [widths[0], widths[1]/(box[1][0]+0.1), widths[2]]
        axis = max(range(3), key=scores.__getitem__)
        lo, hi = box[axis]
        mid = (lo+hi)/2
        assert lo < mid < hi
        splits.append({'address':address,'axis':axis,'mid':mid})
        children = []
        for bit, pair in (('0',(lo,mid)),('1',(mid,hi))):
            child = list(box)
            child[axis] = pair
            children.append((address+bit, tuple(child)))
        stack.extend(reversed(children))
    # Verify the complete stored partition combinatorially, including bounds.
    leaves = {entry['address']:entry for entry in accepted}
    split_map = {entry['address']:entry for entry in splits}
    coverage_stack = [('',root)]
    seen_leaves, seen_splits, uncovered = set(), set(), []
    while coverage_stack:
        address, box = coverage_stack.pop()
        if address in leaves:
            assert tuple(map(tuple,leaves[address]['box'])) == box
            assert math.isfinite(leaves[address]['lower']) and leaves[address]['lower'] > 0
            seen_leaves.add(address)
        elif address in split_map:
            row = split_map[address]
            axis, mid = row['axis'], row['mid']
            lo, hi = box[axis]
            assert lo < mid < hi
            for bit, pair in (('0',(lo,mid)),('1',(mid,hi))):
                child = list(box); child[axis] = pair
                coverage_stack.append((address+bit,tuple(child)))
            seen_splits.add(address)
        else:
            uncovered.append({'address':address,'box':box})
    assert len(seen_leaves) == len(accepted)
    assert len(seen_splits) == len(splits)
    small_coefficient = (Fraction(8,3)*Fraction(157,50)**2-25
                         -Fraction(100,253)-Fraction(32,171))
    small_spacing_bound = (Fraction(2,5)
                           -(Fraction(80,3)+Fraction(32,171))/400)
    assert PI_RATIONAL[0] > Fraction(157,50)
    assert PI_RATIONAL[1]**2 < 10
    assert small_coefficient > Fraction(7,10)
    assert small_spacing_bound > Fraction(3,10)
    compact_floor = all(Fraction.from_float(x['lower']) > Fraction(1,100000)
                        for x in accepted)
    high_floor = all(Fraction.from_float(x['lower']) > 3 for x in high_accepted)
    complete = not failures and not uncovered and not stack and not high_failures
    summary = {'complete':complete,'evaluated_boxes':evaluated,
               'accepted_boxes':len(accepted),'split_boxes':len(splits),
               'uncovered_boxes':len(uncovered),'failures':len(failures),
               'high_depth_cells':len(high_accepted),'high_depth_failures':len(high_failures),
               'high_depth_minimum_lower':min((x['lower'] for x in high_accepted),default=None),
               'actual_minimum_certified_lower':min((x['lower'] for x in accepted),default=None),
               'required_lower':0,'seconds':time.monotonic()-started}
    report = {'kind':'directed interval cover; independent audit pending',
              'scope':'m=1,n=2,a in [1/2,4],u in [3/64,1/2],v=r*u,r in [0,1]; separate u>=1/2 bound',
              'root':root,'summary':summary,'arithmetic':{'type':'binary64 nextafter outward',
                'pi_interval':[PI.lo,PI.hi],'pi_rational_bounds':[str(x) for x in PI_RATIONAL],
                'exp_degree':24,'exp_scaling':32,'exp_tail_upper':1e-24,
                'trig_terms':30,'trig_tail_absolute_upper':1e-49},
              'runtime':{'python':sys.version,'platform':platform.platform(),
                         'float_radix':sys.float_info.radix,
                         'float_mantissa_bits':sys.float_info.mant_dig,
                         'float_rounds':sys.float_info.rounds},
              'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'verification':{'partition_checked_in_full':True,
                'small_depth_coefficient_lower':str(small_coefficient),
                'small_depth_coefficient_required':'7/10',
                'small_spacing_lower':str(small_spacing_bound),
                'small_spacing_required':'3/10',
                'all_compact_leaves_above_1_over_100000':compact_floor,
                'all_high_depth_cells_above_3':high_floor,
                'independent_audit':False},
              'accepted':accepted,'splits':splits,'failures':failures,'uncovered':uncovered,
              'high_depth':{'grid':high_grid,'accepted':high_accepted,'failures':high_failures}}
    path = Path(__file__).with_name('two-packet-cover.json')
    path.write_text(json.dumps(report,separators=(',',':'))+'\n')
    print(json.dumps(summary,indent=2))
    print('Full certificate:',path)
    if not complete:
        sys.exit(1)


if __name__ == '__main__':
    main()
