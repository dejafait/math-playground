"""Exact rational enclosure replay for L831; standard library only.

All proof decisions use Fraction, never the decimal displays. Interval
endpoints are rounded outward to a rational grid of width 10^(-30).
Exp uses a positive Taylor sum and geometric tail; log uses atanh;
sqrt uses integer square roots; pi uses Machin's alternating series.
The analytic reduction and monotonicity arguments are in L831.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json


class I:
    def __init__(self, lo, hi=None):
        lower = F(lo)
        upper = lower if hi is None else F(hi)
        scale = 10**30
        self.lo = F((lower*scale).__floor__(), scale)
        self.hi = F((upper*scale).__ceil__(), scale)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = interval(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -interval(other)

    def __rsub__(self, other):
        return interval(other) + -self

    def __mul__(self, other):
        other = interval(other)
        values = [a*b for a in (self.lo, self.hi)
                  for b in (other.lo, other.hi)]
        return I(min(values), max(values))

    __rmul__ = __mul__

    def reciprocal(self):
        assert self.lo > 0 or self.hi < 0
        return I(1/self.hi, 1/self.lo)

    def __truediv__(self, other):
        return self * interval(other).reciprocal()

    def __rtruediv__(self, other):
        return interval(other) * self.reciprocal()

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        answer = I(1)
        for _ in range(n):
            answer = answer * self
        return answer


def interval(x):
    return x if isinstance(x, I) else I(x)


def sqrt(x):
    x = interval(x)
    assert x.lo >= 0
    scale = 10**24
    lower = isqrt((x.lo.numerator*scale**2)//x.lo.denominator)
    upper = isqrt((x.hi.numerator*scale**2)//x.hi.denominator) + 1
    return I(F(lower, scale), F(upper, scale))


def exp_point(x):
    x = F(x)
    if x < 0:
        return exp_point(-x).reciprocal()
    n = 120
    assert x < n + 2
    term = total = F(1)
    for k in range(1, n+1):
        term *= x/k
        total += term
    first = term*x/(n+1)
    tail = first/(1-x/(n+2))
    return I(total, total+tail)


def exp(x):
    x = interval(x)
    return I(exp_point(x.lo).lo, exp_point(x.hi).hi)


def log_point(x):
    x = F(x)
    assert x > 0
    if x < 1:
        return -log_point(1/x)
    t = (x-1)/(x+1)
    n = 160
    total = 2*sum((t**(2*k+1)/F(2*k+1) for k in range(n)), F(0))
    tail = 2*t**(2*n+1)/(F(2*n+1)*(1-t*t))
    return I(total, total+tail)


def atan_point(x):
    x = F(x)
    assert 0 < x < 1
    n = 80
    total = sum(((-1)**k*x**(2*k+1)/F(2*k+1)
                 for k in range(n)), F(0))
    next_term = (-1)**n*x**(2*n+1)/F(2*n+1)
    return I(min(total, total+next_term), max(total, total+next_term))


pi = 16*atan_point(F(1, 5))-4*atan_point(F(1, 239))
s2 = sqrt(2)
q = lambda value: F(str(value))
checks = []


def check(name, expression, relation, bound):
    value = interval(expression)
    bound = F(str(bound))
    passed = value.hi < bound if relation == '<' else value.lo > bound
    checks.append(dict(name=name, lower=str(value.lo), upper=str(value.hi),
                       relation=relation, required=str(bound), passed=passed,
                       display_lower=float(value.lo), display_upper=float(value.hi)))


check('sector_radius_at_a6', pi/2*exp(6)*sqrt(36+pi*pi/16), '<', 4000)
check('T_lower', pi/2*exp(6), '>', 630)
check('w_over_a', sqrt(1+pi*pi/576), '<', '1.009')
check('T_over_exp_a', pi*q('1.009')/2, '<', '1.585')
check('kappa_real', s2/q('1.009'), '>', '1.4')
check('gaussian_modulus', sqrt(6*pi/7), '>', '1.64')
check('gaussian_tail', I(2)/(q('.14')*q('1.64')), '<', '8.8')
check('cubic', F(19,54), '<', '.4')
check('fourth_derivative', I(72)/q('5.9')**4+2*exp('.1'), '<', '2.4')
check('local_exponential', exp(F(81,16)/(q('.2')*630)), '<', '1.2')
common = sqrt(F(7,6))
A4 = q('.1')*3*common/(4*q('.7')**2*sqrt('.7'))
A2 = q('.6')*3*F(81,16)*common/(2*q('.6')*sqrt('.6'))
A6 = q('.6')*q('.48')*15*common/(8*q('.6')**3*sqrt('.6'))
A8 = q('.6')*q('.03')*105*common/(16*q('.6')**4*sqrt('.6'))
check('local_T_coefficient', A4+A2+A6, '<', '14.4')
check('local_T2_coefficient', A8, '<', '1.3')
check('horizontal_curvature', s2*exp('-.1')/q('1.009'), '>', '1.26')
check('horizontal_tail', 2*exp('.225')/(q('1.64')*(q('.126')-q('2.25')/630)), '<', '12.6')
check('distant_left_radius', sqrt(F(1,4)+pi*pi/576), '<', '.52')
check('distant_left_action', s2*log_point('.52')+F(1,3), '<', '-.58')
check('distant_left_first_polynomial', (q('.08')*4000)**3/6/(20*4000), '>', 1)
check('distant_left_second_polynomial', F(4000**3,48)/(F(100*4000,6)), '>', 1)
check('vertical_action', s2*log_point(6)-s2*pi/24-F(1,3), '>', 2)
check('vertical_main_ratio', 72*sqrt(630), '>', 100)
check('theta_first_term', 81*exp(-5*pi/s2), '<', '.002')
check('theta_geometric_ratio', F(4,3)**4*exp(-7*pi/s2), '<', '.000001')
check('theta_geometric_sum', q('.002')/(1-q('.000001')), '<', 1)
check('theta_pointwise_factor', 17+15/(2*pi), '<', 20)
check('horizontal_exp_budget', q('12.6')*sqrt(630)*exp('-3.969'), '<', 9)
check('theta_absolute_main_integral', q('1.2')/q('1.64')*sqrt(pi/q('.6'))+F(9,630), '<', 2)
check('theta_exp3', exp(3), '>', 20)
check('theta_decay_coefficient', 3*pi/s2, '>', '6.6')
check('theta_far_polynomial', F(64*20**2*24,132**4), '<', '.01')
check('theta_vertical_integrand', (2*pi*pi+3*pi)*exp(-pi/s2)+(34*pi*pi+15*pi)*exp(-4*pi/s2), '<', 4)
check('theta_vertical_factor', 4/(2*pi*pi), '<', 1)
check('combined_exponential_budget', sqrt(630)*(q('8.8')*exp('-4.41')+q('12.6')*exp('-3.969')), '<', 9)
check('J_relative_budget', q('14.4')+q('1.3')/630+9+q('.02'), '<', 24)
check('lower_order_budget', F(3,4)*q('1.009')*(1+F(24,630)), '<', '.8')
check('H_relative_budget', 24+q('.8')+q('.03'), '<', 30)
check('H_log_coefficient', F(30)/(1-F(30,630)), '<', 32)
check('H_log_uniform', F(32,630), '<', '.051')

out = Path(__file__).with_name('audit_constants_657.json')
report = dict(method='exact Fraction interval arithmetic',
              precision=dict(outward_grid_digits=30, sqrt_digits=24, exp_terms=121, log_terms=160, atan_terms=80),
              checks=checks, passed=all(x['passed'] for x in checks),
              failures=[x['name'] for x in checks if not x['passed']])
out.write_text(json.dumps(report, indent=2)+'\n')
for item in checks:
    print(f"{item['name']}: [{item['display_lower']:.12g}, {item['display_upper']:.12g}] "
          f"{item['relation']} {item['required']}: {'PASS' if item['passed'] else 'FAIL'}")
print(f"{len(checks)} checks; failures={report['failures']}; certificate={out}")
raise SystemExit(0 if report['passed'] else 1)
