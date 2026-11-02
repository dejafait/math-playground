"""Exact real-crossing certificate for C673d; no bound on the cone distance.

All decisions use rational arithmetic. Analytic domain, derivative,
interpolation and nodal arguments are required separately in C673d.
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


def exponent(s):
    # At real z=s the conjugate angular pair has equal log moduli.
    result = add(F(s, Q(0), minus_one),
                 mul(add(F(s, Q(0), u0), F(-s, Q(0), u0)), -Q(1, 2)))
    return add(add(result, mul(C, -s)), K(s, Q(0)))


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


smax, step, end = Q(6, 25), Q(1, 500), Q(1, 4)
delta, gap = Q(20, 101), U-Q(3, 2)
strip_width = d-Q(99, 101)
check('unit circle angle', sum(v*v for v in u0), '=', Q(1))
check('pair pole strip width', strip_width, '>', Q(1, 4))
check('pair zero real part bound', d-U*Q(99, 101), '<', -Q(3, 5))
check('pair zero farther than strip', Q(3, 5), '>', strip_width)
check('real a modulus minimum', d-end, '=', Q(1))
check('real reflected a modulus maximum', d+end, '=', Q(3, 2))
check('U gap positive', gap, '>', Q(0))
check('rotated denominator distance', (d-end)*Q(20, 101), '=', delta)
check('pi upper', PI[1], '<', Q(22, 7))

pair_first = 1/delta+1/(2*gap)
pair_second = 1/delta**2+1/(3*gap**2)
minus_second = 1/(d-smax-1)+1/(3*(U-d)**2)
kernel_second = Q(20, 27)/r
second_bound = minus_second+pair_second+kernel_second
check('pair first derivative bound', pair_first, '=', Q(633, 100))
check('spatial second derivative bound on [0,6/25]', second_bound, '<', Q(132))
# Monotonicity of F(s,-1) follows from alpha,beta >=0, not this check alone.
check('single-angle beta denominator positive', U-d, '>', Q(0))

rows=[]
for j in range(121):
    s=j*step
    interval=exponent(s)
    rows.append(dict(index=j, s=str(s),
                     lower_numerator=floor_save(interval[0]),
                     upper_numerator=ceil_save(interval[1])))
check('last sample is tail start', 120*step, '=', smax)
sample_min=Q(min(row['lower_numerator'] for row in rows),SAVE_SCALE)
error=Q(132)*step**2/8
continuous_lower=sample_min-error
tail_start=Q(rows[-1]['lower_numerator'],SAVE_SCALE)
tail_cost=(end-smax)*(pair_first+Q(20,27)*Q(22,7))
tail_lower=tail_start-tail_cost
check('sample minimum', sample_min, '>', -Q(7,1000))
check('continuous compact lower', continuous_lower, '>', -Q(3,400))
check('tail starting value', tail_start, '>', Q(3,25))
check('tail lower', tail_lower, '>', Q(0))
check('barrier exceeds required upper exponent', -Q(3,400), '>', -Q(1,100))

report=dict(status='EXACT REAL-CROSSING CERTIFICATE; ANALYTIC ARGUMENT IN C673d',
            scope='Symmetric angular-pair factor; specified common strip and pole-free contours. '
                  'No cone-distance, signed-integral or finite-n integrand lower bound.',
            arithmetic=dict(log_terms=LOG_TERMS,atan_terms=ATAN_TERMS,
                            save_scale=SAVE_SCALE,pi_lower=str(PI[0]),pi_upper=str(PI[1])),
            domain=dict(s_min='0',s_compact_max=str(smax),s_end_excluded=str(end),
                        angle=[str(v) for v in u0],step=str(step),strip_width=str(strip_width)),
            summary=dict(sample_minimum_lower=str(sample_min),
                         spatial_second_derivative_upper=str(second_bound),
                         interpolation_error=str(error),compact_lower=str(continuous_lower),
                         tail_start_lower=str(tail_start),tail_cost=str(tail_cost),
                         tail_lower=str(tail_lower),claimed_lower='-3/400',
                         required_upper='-1/100',barrier_margin='1/400'),
            samples=rows,checks=checks,failures=failures)
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report,indent=2)+'\n')
print(f'Exact samples: {len(rows)}; checks: {len(checks)}; failures: {failures}')
print(f'Compact lower {continuous_lower}; tail lower {tail_lower}; global > -3/400.')
print('Required upper <= -1/100; strict barrier margin > 1/400.')
print(f'Full certificate: {out}')
if failures:
    raise SystemExit(1)
