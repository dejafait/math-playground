#!/usr/bin/env python3
"""Independent bounded L970 audit. Does not import the construction code.

Analytic justification and arithmetic contract: L970, audit step186.
All certificate records are consumed; full per-cell checks are saved.
"""
from decimal import (Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING,
                     Overflow, Underflow, Subnormal, Clamped,
                     InvalidOperation, DivisionByZero)
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
import math
import sys

# Exact sums of tiny positive tails have long power-of-ten denominators.
# This affects serialization only, never a mathematical bound.
sys.set_int_max_str_digits(0)

HERE = Path(__file__).parent
SOURCE = HERE / 'integrated-moment-certificate-184.json'
OUT = HERE / 'integrated-moment-audit-186.json'
LOW = Context(prec=90, rounding=ROUND_FLOOR, Emin=-999999, Emax=999999)
HIGH = Context(prec=90, rounding=ROUND_CEILING, Emin=-999999, Emax=999999)
bad_signals = [Overflow, Underflow, Subnormal, Clamped,
               InvalidOperation, DivisionByZero]
checks, failures, cell_records = [], [], []


def check(name, condition, evidence=None):
    row = {'check': name, 'passed': bool(condition)}
    if evidence is not None:
        row['evidence'] = evidence
    checks.append(row)
    if not condition:
        failures.append(row)
    return bool(condition)


class Box:
    def __init__(self, x, y=None):
        if isinstance(x, Box):
            self.l, self.r = x.l, x.r
        elif isinstance(x, F):
            self.l = LOW.divide(D(x.numerator), D(x.denominator))
            self.r = HIGH.divide(D(x.numerator), D(x.denominator))
        else:
            assert not isinstance(x, float) and not isinstance(y, float)
            self.l, self.r = D(x), D(x if y is None else y)
        assert self.l.is_finite() and self.r.is_finite() and self.l <= self.r

    def __neg__(self):
        return Box(self.r.copy_negate(), self.l.copy_negate())

    def __add__(self, x):
        x = Box(x)
        return Box(LOW.add(self.l, x.l), HIGH.add(self.r, x.r))

    __radd__ = __add__

    def __sub__(self, x):
        return self + -Box(x)

    def __rsub__(self, x):
        return Box(x) + -self

    def __mul__(self, x):
        x = Box(x)
        terms = [(a, b) for a in [self.l, self.r] for b in [x.l, x.r]]
        return Box(min(LOW.multiply(a, b) for a, b in terms),
                   max(HIGH.multiply(a, b) for a, b in terms))

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = Box(x)
        assert x.l > 0 or x.r < 0
        return self * Box(LOW.divide(D(1), x.r), HIGH.divide(D(1), x.l))

    def power(self, k):
        ans = Box(1)
        for _ in range(k):
            ans = ans * self
        return ans

    def record(self):
        return [str(self.l), str(self.r)]


@lru_cache(maxsize=100000)
def exponential_point(y):
    # Different parameters from construction: |z|<=1/16, degree 50.
    # Positive Taylor tail <= 2*z^51/51!, ratios <= 1/832.
    q = F(y.copy_abs())
    k = 0
    while q > F(1, 16):
        q /= 2
        k += 1
    z = Box(q)
    term, partial = Box(1), Box(1)
    for j in range(1, 51):
        term = term*z/j
        partial = partial+term
    tail = 2*z.power(51)/math.factorial(51)
    partial = Box(partial.l, HIGH.add(partial.r, tail.r))
    for _ in range(k):
        partial = partial*partial
    return Box(1)/partial if y < 0 else partial


def exponential(x):
    x = Box(x)
    return Box(exponential_point(x.l).l, exponential_point(x.r).r)


def atan_fixed(q, count):
    s = sum((F((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(count)), F(0))
    other = s+F((-1)**count, (2*count+1)*q**(2*count+1))
    return min(s, other), max(s, other)


al, ar = atan_fixed(5, 80)
bl, br = atan_fixed(239, 30)
pi_exact = [16*al-4*br, 16*ar-4*bl]
PI = Box(Box(pi_exact[0]).l, Box(pi_exact[1]).r)


def derivative_polynomial(p):
    # Ascending coefficients for (1/2-2v)P+2vP'.
    out = [F(0)]*(len(p)+1)
    for j, c in enumerate(p):
        out[j] += (F(1, 2)+2*j)*c
        out[j+1] -= 2*c
    return out


P0 = [F(0), F(-12), F(8)]
P1 = derivative_polynomial(P0)
P2 = derivative_polynomial(P1)


def polynomial(x, p):
    ans = Box(0)
    for c in reversed(p):
        ans = ans*x+Box(c)
    return ans


def evaluate(u):
    e2, ehalf = exponential(2*u), exponential(u/2)
    kernel = [Box(0), Box(0), Box(0)]
    for m in range(1, 5):
        v = PI*(m*m)*e2
        w = ehalf*exponential(-v)
        for j, p in enumerate([P0, P1, P2]):
            kernel[j] = kernel[j]+w*polynomial(v, p)
    omitted = 10000*PI.power(2)*exponential(Box(F(9, 2))*u-25*PI*e2)
    result = {}
    for label, a in [('b', Box(F(1, 2))), ('h', Box(72))]:
        ep, em = exponential(a*u), exponential(-a*u)
        c, s = (ep+em)/2, (ep-em)/2
        hs = [(c, a*s, a.power(2)*c),
              (u*s/(2*a), s/(2*a)+u*c/2, c+a*u*s/2)]
        for r, (f, df, ddf) in enumerate(hs):
            result[label+str(r)] = (kernel[0]*f,
                kernel[2]*f+2*kernel[1]*df+kernel[0]*ddf, omitted*f)
    return result


def rational_pair(pair):
    return [F(v) for v in pair]


def contains(outer, inner):
    a, b = rational_pair(outer)
    c, d = rational_pair(inner)
    return a <= c <= d <= b


source = json.loads(SOURCE.read_text())
keys = ['b0', 'b1', 'h0', 'h1']
check('parameters', source['parameters'] == {
    'N': 3072, 'u_interval': [0, 3], 'theta_N': 4, 'precision': 60,
    'exp_degree': 30, 'exp_reduced_argument_max': '1/8'})
check('derivative_polynomials', P1 == list(map(F, [0, -30, 60, -16]))
      and P2 == list(map(F, [0, -75, 330, -224, 32])))
check('pi_independent_enclosure', contains(source['pi']['interval'], PI.record()), PI.record())
check('pi_exact_saved_enclosure', contains(source['pi']['interval'],
      [source['pi']['exact_lower'], source['pi']['exact_upper']]))
check('pi_exact_bounds_enclose_independent', contains(
      [source['pi']['exact_lower'], source['pi']['exact_upper']],
      [str(v) for v in pi_exact]))
# Independently reproduce the declared exact alternating-series bounds.
original_bounds = [atan_fixed(q, n) for q, n in [(5, 49), (239, 14)]]
check('original_machin_exact', [16*original_bounds[0][0]-4*original_bounds[1][1],
      16*original_bounds[0][1]-4*original_bounds[1][0]] ==
      list(map(F, [source['pi']['exact_lower'], source['pi']['exact_upper']])))

trapezoid_sums = {key: Box(0) for key in keys}
for j in range(3073):
    node = evaluate(Box(F(j, 1024)))
    for key in keys:
        trapezoid_sums[key] += node[key][0]*Box(F(1, 2) if j in [0, 3072] else F(1))
    if j % 1024 == 0:
        print('independent nodes', j, '/3072', flush=True)

check('cell_count', len(source['cells']) == 3072)
derivative_sums = {key: F(0) for key in keys}
theta_sums = {key: F(0) for key in keys}
for j in range(3072):
    old = source['cells'][j]
    value = evaluate(Box(Box(F(j, 1024)).l, Box(F(j+1, 1024)).r))
    row = {'j': j, 'u': old['u'], 'bounds': {}, 'passed': True}
    row['passed'] &= old['j'] == j and rational_pair(old['u']) == [F(j, 1024), F(j+1, 1024)]
    for key in keys:
        saved = old['integrands'][key]
        derivative = value[key][1].record()
        omitted = value[key][2].r
        ok_derivative = contains(saved['f_second'], derivative)
        ok_omitted = F(saved['omitted_theta_upper']) >= max(F(0), F(omitted))
        row['bounds'][key] = {'second': derivative,
            'omitted_upper': str(omitted), 'second_contained': ok_derivative,
            'omitted_dominated': ok_omitted}
        row['passed'] &= ok_derivative and ok_omitted
        lo, hi = rational_pair(saved['f_second'])
        derivative_sums[key] += max(abs(lo), abs(hi))*F(1, 12*1024**3)
        theta_sums[key] += F(saved['omitted_theta_upper'])/1024
    if not row['passed']:
        failures.append({'cell': j, 'evidence': row})
    cell_records.append(row)
    if j % 1024 == 0:
        print('independent cells', j, '/3072', flush=True)
check('all_cell_bounds', all(row['passed'] for row in cell_records), {'count': len(cell_records)})

slope = 77-2*PI*exponential(Box(6))
tail = 16*PI.power(2)*exponential(231-PI*exponential(Box(6)))*Box(F(3, 2000)+F(1, 4000000))
check('improper_slope', contains(source['improper_tail']['phi_prime_at_3'], slope.record())
      and slope.r < -2000, slope.record())
check('improper_tail', contains(source['improper_tail']['bound'], tail.record())
      and tail.r < D('2e-451'), tail.record())
aggregate = {}
coarse_moments = {'b0': ['.4999992', '.5000008'],
    'b1': ['.01154780', '.01154791'], 'h0': ['6.22365e25', '6.22539e25'],
    'h1': ['5.37525e23', '5.37679e23']}
quad_caps = dict(zip(keys, map(F, ['8e-7', '5e-8', '8.63e21', '7.69e19'])))
theta_caps = dict(zip(keys, map(F, ['6e-32', '3e-36', '8e-32', '4e-36'])))
for key in keys:
    old = source['moments'][key]
    new_trap = (trapezoid_sums[key]/1024).record()
    check(key+'_node_trapezoid', contains(old['trapezoid'], new_trap), new_trap)
    check(key+'_exact_saved_cell_error_sum', contains(old['quadrature_error'],
          [str(derivative_sums[key])]*2))
    check(key+'_exact_saved_theta_sum', contains(old['theta_tail'], [str(theta_sums[key])]*2))
    tr, er, th, ut, moment = [rational_pair(old[field]) for field in
        ['trapezoid', 'quadrature_error', 'theta_tail', 'u_tail', 'integral']]
    required = [tr[0]-er[1], tr[1]+er[1]+th[1]+ut[1]]
    check(key+'_moment_propagation', moment[0] > 0 and
          moment[0] <= required[0] <= required[1] <= moment[1])
    check(key+'_same_u_tail', old['u_tail'] == source['improper_tail']['bound'])
    check(key+'_displayed_moment', contains(coarse_moments[key], old['integral']))
    check(key+'_displayed_error_caps', er[1] <= quad_caps[key] and th[1] <= theta_caps[key])
    aggregate[key] = {'node_trapezoid': new_trap,
        'exact_cell_error_sum': str(derivative_sums[key]),
        'exact_theta_sum': str(theta_sums[key]), 'required_moment': [str(v) for v in required]}

for key, label in [('b', 'b'), ('h', 'h')]:
    numerator = rational_pair(source['moments'][key+'1']['integral'])
    denominator = rational_pair(source['moments'][key+'0']['integral'])
    actual = [numerator[0]/denominator[1], numerator[1]/denominator[0]]
    check(label+'_ratio_propagation', contains(source['ratios'][label], [str(v) for v in actual]))
    coarse = ['.02309557', '.02309585'] if key == 'b' else ['.00863441', '.00863928']
    check(label+'_displayed_ratio', contains(coarse, source['ratios'][label]))
rlo, rhi = rational_pair(source['ratios']['b'])
tlo, thi = rational_pair(source['ratios']['h'])
check('required_ratio_boxes', F(1, 50) <= rlo <= rhi <= F(1, 40) and 0 < tlo <= thi <= F(1, 100))
h, gap = F(5184), F(20735, 4)
d1, d2 = 4*h*h/gap**2, h/gap
signed = source['signed_propagation']
check('complete_coefficients', F(signed['d1']) == d1 and F(signed['d2']) == d2)
box_lower = d1/F(50)-d2/F(1600)-d1/F(100)
check('exact_box_lower', F(signed['box_lower_exact']) == box_lower == F(423263556, 10748505625)
      and box_lower > F(39, 1000), str(box_lower))
direct = d1*rlo-d2*rhi*rhi-d1*thi
check('complete_signed_propagation', contains(signed['direct_lower'], [str(direct)]*2)
      and F(signed['direct_lower'][0]) > F('0.0572973163569718'), str(direct))
check('no_bad_decimal_signals', not any(ctx.flags[s] for ctx in [LOW, HIGH] for s in bad_signals))
check('original_checks', source['checks'] == {'b_box': True, 'h_box': True, 'positive_signed_lower': True}
      and source['failures'] == [] and source['status'] == 'PASS')
result = {'step': 186, 'status': 'PASS' if not failures else 'FAIL',
    'source': str(SOURCE), 'independent_precision': 90,
    'exp_degree': 50, 'exp_reduced_argument_max': '1/16',
    'checks': checks, 'failures': failures, 'pi': PI.record(),
    'improper_tail': {'slope': slope.record(), 'bound': tail.record()},
    'aggregate': aggregate, 'signed': {'box_lower': str(box_lower), 'direct_exact': str(direct)},
    'cells': cell_records}
OUT.write_text(json.dumps(result, indent=2)+'\n')
print('status:', result['status'], '; checks:', len(checks), '; cells:', len(cell_records))
print('box lower:', box_lower, '; required >', F(39, 1000))
print('failures:', len(failures), '; full evidence:', OUT)
assert not failures
