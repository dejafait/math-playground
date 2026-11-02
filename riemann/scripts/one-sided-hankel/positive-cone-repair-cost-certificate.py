"""Exact constants for the strict-action repair cost; analytic proof in C673b.

All certificate decisions use Fraction arithmetic. The prior floating
screen is not an input. No finite cone feasibility is claimed.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

TERMS = 12
SERIES_TERMS = 100
SCALE = 10**12
logs, series, checks, failures = {}, {}, [], []


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def mul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def div(a, b):
    norm = b[0]**2+b[1]**2
    return ((a[0]*b[0]+a[1]*b[1])/norm,
            (a[1]*b[0]-a[0]*b[1])/norm)


def interval_add(a, b):
    return a[0]+b[0], a[1]+b[1]


def scale(c, a):
    vals = c*a[0], c*a[1]
    return min(vals), max(vals)


def log_unit(v):
    assert 1 <= v <= 2
    z = (v-1)/(v+1)
    terms = [2*z**(2*j+1)/(2*j+1) for j in range(TERMS)]
    lower = sum(terms, Q(0))
    tail = 2*z**(2*TERMS+1)/((2*TERMS+1)*(1-z*z))
    return (lower, lower+tail), dict(argument=str(v), z=str(z),
        terms=[str(t) for t in terms], tail=str(tail),
        lower=str(lower), upper=str(lower+tail))


log2, log2_record = log_unit(Q(2))
logs['2'] = log2_record


def logarithm(v):
    original, exponent = v, 0
    assert v > 0
    while v < 1:
        v *= 2
        exponent -= 1
    while v > 2:
        v /= 2
        exponent += 1
    reduced, record = log_unit(v)
    result = interval_add(reduced, scale(exponent, log2))
    logs[str(original)] = dict(power_of_two=exponent, reduced=record,
                               lower=str(result[0]), upper=str(result[1]))
    return result


def S(name, v):
    assert v[0]**2+v[1]**2 <= Q(4, 5)**2
    power = Q(1), Q(0)
    terms = []
    for k in range(1, SERIES_TERMS+1):
        power = mul(power, v)
        terms.append(power[0]/(k*(k+1)))
    partial = sum(terms, Q(0))
    tail = Q(4, 5)**101/(101*102*(1-Q(4, 5)))
    result = partial-tail, partial+tail
    series[name] = dict(argument=[str(c) for c in v],
        modulus_squared=str(v[0]**2+v[1]**2),
        terms=[str(t) for t in terms], partial=str(partial),
        tail=str(tail), lower=str(result[0]), upper=str(result[1]))
    return result


def outward(a):
    lo = (a[0]*SCALE).__floor__()
    hi = (a[1]*SCALE).__ceil__()
    return Q(lo, SCALE), Q(hi, SCALE)


def check(name, actual, relation, required):
    passed = {'<': actual < required, '>': actual > required,
              '=': actual == required}[relation]
    checks.append(dict(name=name, actual=str(actual), relation=relation,
                       required=str(required), passed=passed))
    if not passed:
        failures.append(name)


d, U, y, r = Q(5, 4), Q(121, 64), Q(1, 20), Q(9, 20)
x, a, u = (-d, Q(0)), (-d, y), (Q(-24, 25), Q(7, 25))
check('unit angular point', u[0]**2+u[1]**2, '=', Q(1))
F = scale(Q(1, 2), logarithm(d*d/(d*d+y*y)))
for sign, name, value in (
    (1, 'u/a', div(u, a)), (-1, 'u/x', div(u, x)),
    (1, 'x/(Uu)', div(x, (U*u[0], U*u[1]))),
    (-1, 'a/(Uu)', div(a, (U*u[0], U*u[1])))):
    F = interval_add(F, scale(sign, S(name, value)))
K = scale(2*r, logarithm(r))
K = interval_add(K, scale(-(r-y), logarithm(r-y)))
K = interval_add(K, scale(-(r+y), logarithm(r+y)))
K = scale(Q(10, 27), K)
beta = interval_add(K, (Q(3, 5)*y*y, Q(3, 5)*y*y))
rate = interval_add(interval_add(F, beta), (Q(1, 200), Q(1, 200)))
Fout, bout, rout = outward(F), outward(beta), outward(rate)
check('angular growth F lower', Fout[0], '>', Q(7, 1000))
check('coefficient rate beta lower', bout[0], '>', -Q(3, 5000))
check('combined correction rate lower', rout[0], '>', Q(57, 5000))
check('chosen correction exponent exceeds target', Q(11, 1000), '>', Q(1, 100))
annulus = []
for radius in (Q(9, 10), Q(11, 10)):
    A = scale(1/radius, logarithm(d/(d-radius)))
    A = interval_add(A, scale(U*radius/(d*d), logarithm(U*radius/(U*radius-d))))
    A = interval_add(A, (-1/d, -1/d))
    bounds = outward(A)
    check('annulus A upper at '+str(radius), bounds[1], '<', Q(3))
    annulus.append(dict(radius=str(radius), lower=str(bounds[0]), upper=str(bounds[1])))
check('outer logarithmic decay', outward(logarithm(Q(11, 10)))[0], '>', Q(19, 200))
check('inner logarithmic decay', outward(logarithm(Q(10, 9)))[0], '>', Q(1, 10))
check('outer tail exponent', 3*Q(3, 50)-2*Q(19, 200), '=', -Q(1, 100))
check('inner tail exponent', 3*Q(3, 50)-2*Q(1, 10), '=', -Q(1, 50))

report = dict(status='EXACT CONSTANT CERTIFICATE; ANALYTIC PROOF IN C673b',
    scope='L673 exact phase displacement; degree-2n zero-anchor strict correction only; no cone lower or upper bound',
    parameters=dict(y=str(y), u=[str(c) for c in u], log_terms=TERMS,
                    series_terms=SERIES_TERMS),
    logarithms=logs, series=series, annulus=annulus,
    summary=dict(F=[str(c) for c in Fout], beta=[str(c) for c in bout],
                 correction_rate=[str(c) for c in rout],
                 proved_eventual_exponent='11/1000', cone_budget_exponent='1/100',
                 exponent_gap='1/1000', projection_tail='<=19 exp(-n/100) for |y|<=3/50'),
    checks=checks, failures=failures)
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report, indent=2)+'\n')
print('Exact checks:', len(checks), '; failures:', failures)
print('F lower:', Fout[0], '> 7/1000; beta lower:', bout[0], '> -3/5000')
print('Correction rate lower:', rout[0], '> 57/5000; eventual exponent 11/1000 > required budget 1/100')
print('Full certificate:', out)
if failures:
    raise SystemExit(1)
