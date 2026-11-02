"""Exact crossing certificate for C673c; no bound on the cone distance.

All decisions use rational arithmetic. Analytic domain, derivative,
interpolation and nodal arguments are required separately in C673c.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

LOG_TERMS, ATAN_TERMS, SAVE_SCALE = 24, 32, 10**12
checks, failures = [], []


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def mul(a, b):
    return (a[0]*b, a[1]*b) if b >= 0 else (a[1]*b, a[0]*b)


def neg(a):
    return -a[1], -a[0]


def log_unit(v):
    assert 1 <= v <= 2
    z = (v-1)/(v+1)
    total, term = Q(0), z
    for j in range(LOG_TERMS):
        total += 2*term/(2*j+1)
        term *= z*z
    tail = 2*term/((2*LOG_TERMS+1)*(1-z*z))
    return total, total+tail


LOG2 = log_unit(Q(2))


def logq(v):
    assert v > 0
    power = 0
    while v < 1:
        v *= 2
        power -= 1
    while v > 2:
        v /= 2
        power += 1
    return add(log_unit(v), mul(LOG2, power))


def atan_small(v):
    assert abs(v) <= Q(1, 2)
    total, term = Q(0), v
    for j in range(ATAN_TERMS):
        total += term/(2*j+1)
        term *= -v*v
    error = abs(term)/(2*ATAN_TERMS+1)
    return total-error, total+error


PI = add(mul(atan_small(Q(1, 5)), 16), mul(atan_small(Q(1, 239)), -4))
C = mul(PI, Q(10, 27))


def atanq(v):
    if v < 0:
        return neg(atanq(-v))
    if v > 1:
        return add(mul(PI, Q(1, 2)), neg(atanq(1/v)))
    if v > Q(1, 2):
        return add(mul(PI, Q(1, 4)), atan_small((v-1)/(v+1)))
    return atan_small(v)


def primitive(b, v):
    assert b >= 0 and b*b+v*v > 0
    result = add(mul(logq(b*b+v*v), v/2), (-v, -v))
    return add(result, mul(atanq(v/b), b)) if b else result


def cmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def cdiv(a, b):
    norm = b[0]*b[0]+b[1]*b[1]
    return cmul(a, (b[0]/norm, -b[1]/norm))


def integral_log(v):
    # Integral_0^1 log|v-t| dt; all endpoints here are nonsingular.
    a, b = v[0], abs(v[1])
    return add(primitive(b, 1-a), neg(primitive(b, -a)))


d, U, r = Q(5, 4), Q(121, 64), Q(9, 20)
u0, minus_one = (-Q(99, 101), Q(20, 101)), (-Q(1), Q(0))


def F(s, y, u):
    a, x = (-d+s, y), (-d, Q(0))
    Uu = (U*u[0], U*u[1])
    result = add(integral_log(cdiv(x, u)), neg(integral_log(cdiv(a, u))))
    result = add(result, mul(logq((a[0]*a[0]+a[1]*a[1])/(d*d)), Q(1, 2)))
    result = add(result, integral_log(cdiv(Uu, a)))
    return add(result, neg(integral_log(cdiv(Uu, x))))


BASE = mul(add(logq(r), (-Q(1), -Q(1))), 2*r)


def K(s, y):
    return mul(add(add(BASE, neg(primitive(abs(s), y+r))),
                   primitive(abs(s), y-r)), Q(10, 27))


def exponent(s, y):
    result = F(s, y, u0)
    result = add(result, mul(add(F(s, y, minus_one),
                                 F(-s, -y, minus_one)), -Q(1, 2)))
    return add(add(result, mul(C, -s)), K(s, y))


def floor_save(v):
    return (v.numerator*SAVE_SCALE)//v.denominator


def ceil_save(v):
    return -((-v.numerator*SAVE_SCALE)//v.denominator)


def check(name, actual, relation, required):
    passed = {'<': actual < required, '>': actual > required,
              '=': actual == required}[relation]
    checks.append(dict(name=name, actual=str(actual), relation=relation,
                       required=str(required), passed=passed))
    if not passed:
        failures.append(name)


y0, radius, smax, step = Q(3, 20), Q(1, 100000), Q(27, 100), Q(27, 10000)
ylo, yhi = y0-radius, y0+radius
delta, gap_a, gap_b = Q(47, 1000), Q(63, 100), Q(36, 100)
check('unit circle angle', sum(v*v for v in u0), '=', Q(1))
check('rotated denominator distance',
      (20*(d-smax)-99*yhi)/101, '>', delta)
check('a modulus bound squared', d*d+yhi*yhi, '<', Q(126, 100)**2)
check('reflected a modulus bound squared', (d+smax)**2+yhi*yhi, '<', Q(153, 100)**2)
check('a U gap', U-Q(126, 100), '>', gap_a)
check('reflected a U gap', U-Q(153, 100), '>', gap_b)
check('horizontal exit is in excluded disk', (d-smax)**2+yhi*yhi, '<', Q(1))
check('kernel y log ratio', ((r+yhi)/(r-yhi))**2, '<', Q(5))
check('log 5 upper', logq(Q(5))[1], '<', Q(2))

F0_second = 1/delta**2+1/(3*gap_a**2)
Fa_second = 1/ylo**2+1/(3*gap_a**2)
Fb_second = 1/ylo**2+1/(3*gap_b**2)
K_second = Q(10, 27)*(1/(r+ylo)+1/(r-yhi))
second_bound = F0_second+(Fa_second+Fb_second)/2+K_second
check('spatial second derivative bound', second_bound, '<', Q(600))

F0_first = 1/delta+1/(2*gap_a)
Fa_first = 1/ylo+1/(2*gap_a)
Fb_first = 1/ylo+1/(2*gap_b)
first_bound = F0_first+(Fa_first+Fb_first)/2+Q(10, 27)
check('height first derivative bound', first_bound, '<', Q(40))
check('phase node band radius at n>=180003', Q(5, 8)*Q(27, 10*180003), '<', radius)

rows = []
for j in range(101):
    s = j*step
    interval = exponent(s, y0)
    lo, hi = floor_save(interval[0]), ceil_save(interval[1])
    rows.append(dict(index=j, s=str(s), y=str(y0),
                     lower_numerator=lo, upper_numerator=hi))
sample_min = Q(min(row['lower_numerator'] for row in rows), SAVE_SCALE)
interpolation_error = Q(600)*step**2/8
height_error = Q(40)*radius
lower = sample_min-interpolation_error-height_error
check('sample minimum', sample_min, '>', -Q(1, 1000))
check('continuous exponent lower', lower, '>', -Q(1, 500))
check('barrier exceeds required upper exponent', -Q(1, 500), '>', -Q(1, 100))

report = dict(status='EXACT CROSSING CERTIFICATE; ANALYTIC ARGUMENT IN C673c',
              scope='Exact even rational gauge; common pole-free contours. '
                    'No cone-distance, signed-integral or finite-n integrand lower bound.',
              arithmetic=dict(log_terms=LOG_TERMS, atan_terms=ATAN_TERMS,
                              save_scale=SAVE_SCALE, pi_lower=str(PI[0]), pi_upper=str(PI[1])),
              domain=dict(s_min='0', s_max=str(smax), y_min=str(ylo), y_max=str(yhi),
                          angle=[str(v) for v in u0], step=str(step)),
              summary=dict(sample_minimum_lower=str(sample_min),
                           spatial_second_derivative_upper=str(second_bound),
                           height_first_derivative_upper=str(first_bound),
                           interpolation_error=str(interpolation_error), height_error=str(height_error),
                           continuous_lower=str(lower), claimed_lower='-1/500',
                           required_upper='-1/100', barrier_margin='1/125'),
              samples=rows, checks=checks, failures=failures)
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report, indent=2)+'\n')
print(f'Exact samples: {len(rows)}; checks: {len(checks)}; failures: {failures}')
print(f'Exponent >= {lower} > -1/500; required upper <= -1/100; strict gap > 1/125.')
print(f'Full certificate: {out}')
if failures:
    raise SystemExit(1)
