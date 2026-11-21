#!/usr/bin/env python3
"""Independent 512-bit rational audit of the complete fixed certificate1326.

Uses reciprocal positive exponential series, not the producer's alternating
negative series. All endpoint comparisons are exact; displays are not inputs.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'scripts/theta-score/jensen-five-1326.json'
OUT = Path(__file__).with_suffix('.json')
BITS = 512
GRID = 2**BITS


def down(x):
    return F((x * GRID).__floor__(), GRID)


def up(x):
    return F((x * GRID).__ceil__(), GRID)


class Box:
    def __init__(self, lo, hi=None):
        self.lo = down(F(lo))
        self.hi = up(F(lo if hi is None else hi))
        assert self.lo <= self.hi

    def __add__(self, other):
        other = box(other)
        return Box(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Box(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-box(other))

    def __mul__(self, other):
        other = box(other)
        ends = [x*y for x in (self.lo, self.hi)
                for y in (other.lo, other.hi)]
        return Box(min(ends), max(ends))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = box(other)
        assert not other.lo <= 0 <= other.hi
        ends = [x/y for x in (self.lo, self.hi)
                for y in (other.lo, other.hi)]
        return Box(min(ends), max(ends))

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        answer = Box(1)
        for _ in range(n):
            answer = answer*self
        return answer

    def record(self):
        return {'lo': str(self.lo), 'hi': str(self.hi)}


def box(x):
    return x if isinstance(x, Box) else Box(x)


checks = []


def check(name, success, **evidence):
    checks.append({'name': name, 'passed': bool(success), **evidence})


def contains(record, independent, name):
    scale = 2**record['denominator_power_of_two']
    low, high = F(int(record['lo_integer']), scale), F(int(record['hi_integer']), scale)
    check(name, low <= independent.lo <= independent.hi <= high,
          stored=[str(low), str(high)], independent=independent.record())


def atan(q, count):
    value = sum((F((-1)**k, (2*k+1)*q**(2*k+1))
                 for k in range(count)), F(0))
    adjacent = value + F((-1)**count, (2*count+1)*q**(2*count+1))
    return Box(min(value, adjacent), max(value, adjacent))


def exp_negative_endpoint(x):
    # For t=x/512<1/2, exp(t) is bounded by its positive Taylor sum
    # through M=100 plus [0, first omitted term/(1-t/(M+2))].
    t = Box(x/512)
    assert 0 <= t.lo <= t.hi < F(1, 2)
    term, total = Box(1), Box(1)
    for k in range(1, 101):
        term = term*t/k
        total = total + term
    first = term*t/101
    remainder = first / (Box(1) - t/102)
    exponential = total + Box(0, remainder.hi)
    inverse = Box(1)/exponential
    # Nine squarings undo scaling by 512.
    for _ in range(9):
        inverse = inverse*inverse
    return inverse


def exp_negative(interval):
    return Box(exp_negative_endpoint(interval.hi).lo,
               exp_negative_endpoint(interval.lo).hi)


original_bytes = SOURCE.read_bytes()
cert = json.loads(original_bytes)
check('fixed_contract', cert['N'] == 8 and cert['precision_bits'] == 256)
pi = 16*atan(5, 140) - 4*atan(239, 50)
check('pi_3_4', 3 < pi.lo <= pi.hi < 4)
contains(cert['pi'], pi, 'pi')

# Differentiate v^d e^(-v) e^(u/2), with Dv=2v.
polys = [[F(0), F(-12), F(8)]]
for order in range(1, 7):
    prior = polys[-1]
    result = [F(0)]*(len(prior)+1)
    for degree in range(len(result)):
        if degree < len(prior):
            result[degree] += (F(1, 2) + 2*degree)*prior[degree]
        if degree:
            result[degree] -= 2*prior[degree-1]
    polys.append(result)
check('all_seven_polynomials', cert['polynomials_Q'] == [[str(c) for c in p] for p in polys])

derivatives = [Box(0) for _ in range(7)]
check('exact_retained_row_count', len(cert['term_intervals']) == 8)
for n, row in enumerate(cert['term_intervals'], 1):
    check('row_index_'+str(n), row['n'] == n)
    v = pi*n*n
    exponential = exp_negative(v)
    contains(row['v'], v, 'v_'+str(n))
    contains(row['exp_minus_v'], exponential, 'exp_'+str(n))
    check('row_derivative_count_'+str(n), len(row['derivative_terms']) == 7)
    for j, poly in enumerate(polys):
        # Direct monomial evaluation differs from producer's Horner scheme.
        value = sum((coefficient*v**degree for degree, coefficient
                     in enumerate(poly)), Box(0))*exponential
        contains(row['derivative_terms'][j], value, 'term_'+str(n)+'_'+str(j))
        derivatives[j] = derivatives[j] + value

check('tail_row_count', len(cert['tail_bounds']) == 7)
check('exp3_gt16', sum((F(3**k, factorial(k)) for k in range(5)), F(0)) == F(131, 8) > 16)
ratio = F(2**16, 2**(4*19))
check('tail_geometric_ratio', ratio == F(1, 2**60) < F(1, 2))
for j, poly in enumerate(polys):
    B = sum((abs(c)*4**d for d, c in enumerate(poly)), F(0))
    tail = 2*B*9**16/F(2**324)
    row = cert['tail_bounds'][j]
    check('tail_'+str(j), row['j'] == j and F(row['B']) == B
          and F(row['bound']) == tail and tail < F(1, 10**60),
          B=str(B), full_tail_bound=str(tail))
    derivatives[j] = derivatives[j] + Box(-tail, tail)
    contains(cert['kernel_derivatives'][j], derivatives[j], 'kernel_'+str(j))
for j in (1, 3, 5):
    check('odd_interval_zero_'+str(j), derivatives[j].lo <= 0 <= derivatives[j].hi)

check('K0_positive', derivatives[0].lo > 0)
r2, r4, r6 = [derivatives[j]/derivatives[0] for j in (2, 4, 6)]
a1 = -r2
a3 = r4 - 3*r2*r2
a5 = -(r6 - 15*r4*r2 + 30*r2*r2*r2)
for key, val in [('a1', a1), ('a3', a3), ('a5', a5)]:
    contains(cert['score_derivatives'][key], val, key)
A, B, C = a5, 10*a3, 5*a1
D, AC = B*B-4*A*C, A*C
for key, val in [('A', A), ('B', B), ('C', C), ('D', D), ('AC', AC)]:
    contains(cert['quadratic_in_y'][key], val, key)
for key, val in [('K0', derivatives[0]), ('a1', a1), ('a3', a3),
                 ('a5', a5), ('D', D), ('AC', AC)]:
    low, high = map(F, cert['published_enclosures'][key])
    check('published_'+key, low < val.lo <= val.hi < high,
          actual=val.record(), required=[str(low), str(high)])
check('strict_root_conditions', A.hi < 0 and C.lo > 0 and D.lo > 0 and AC.hi < 0)
check('original_no_failures', cert['outcome'] == 'NONREAL_PAIR_CERTIFIED'
      and cert['failures'] == [] and all(cert['checks'].values()))

# Replay only after independent comparisons have used the original saved data.
replay = subprocess.run([sys.executable, 'scripts/theta-score/jensen-five-1326.py'],
                        cwd=ROOT, capture_output=True, text=True)
check('producer_replay_exit', replay.returncode == 0,
      stdout=replay.stdout, stderr=replay.stderr)
check('producer_replay_byte_identical', SOURCE.read_bytes() == original_bytes)
failures = [c['name'] for c in checks if not c['passed']]
report = {'target': 'Fixed C019a full analytic-contract and rational-certificate audit',
          'arithmetic_precision_bits': BITS,
          'source_sha256': hashlib.sha256(original_bytes).hexdigest(),
          'method': 'Independent rational boxes; longer Machin series; reciprocal positive exponential Taylor series M100 scaled512; direct monomial derivative evaluation; all stored mathematical intervals compared',
          'checks': checks, 'failures': failures,
          'analytic_contracts': 'Human-reviewed in C019a audit1328; this script alone does not verify complex analysis or Jensen necessity.',
          'outcome': 'PASS' if not failures else 'FAIL'}
OUT.write_text(json.dumps(report, indent=2)+'\n')
print('Outcome:', report['outcome'], '; exact checks:', len(checks))
print('Required: all saved endpoint enclosures, seven tails<1e-60, A<0<C, D>0, AC<0; byte-identical replay.')
print('Actual certified outer bounds:', cert['published_enclosures'])
print('Failures:', failures)
print('Full audit certificate:', OUT.relative_to(ROOT))
if failures:
    raise SystemExit(1)
