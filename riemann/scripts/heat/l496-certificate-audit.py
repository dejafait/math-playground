#!/usr/bin/env python3
"""Independently consume every load-bearing L496 certificate field.

No producer import/execution; no floating-point mathematical comparisons.
Primitive sums use 10^-90 outward Horner arithmetic (the producer uses
10^-70 forward recurrences). All final graph operations use exact endpoints.
The analytic justification and retained source premise are in L496.
"""
from collections import Counter
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
import math
import traceback

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'finite-euler-phase-floor-certificate.json'
PRODUCER = HERE / 'finite-euler-phase-floor-certificate.py'
OUTPUT = HERE / 'l496-certificate-audit.json'
GRID = 10**90
checks = []
summary = {}


def rational(v):
    d = int(v['denominator'])
    if d <= 0:
        raise ValueError('Nonpositive rational denominator')
    return Q(int(v['numerator']), d)


def read_interval(v):
    a, b = rational(v['lower']), rational(v['upper'])
    if a > b:
        raise ValueError('Reversed interval')
    return a, b


def serial(v):
    if isinstance(v, Q):
        return {'numerator': str(v.numerator), 'denominator': str(v.denominator)}
    if isinstance(v, tuple):
        return {'lower': serial(v[0]), 'upper': serial(v[1])}
    if isinstance(v, list):
        return [serial(x) for x in v]
    if isinstance(v, dict):
        return {k: serial(x) for k, x in v.items()}
    return v


def record(name, passed, actual, required):
    checks.append({'name': name, 'passed': bool(passed),
                   'actual': serial(actual), 'required': serial(required)})


def equal(name, actual, required):
    record(name, actual == required, actual, required)


def contained(name, outer, inner):
    record(name, outer[0] <= inner[0] <= inner[1] <= outer[1], inner, outer)


def singleton(a):
    return Q(a), Q(a)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def subtract(a, b):
    return a[0] - b[1], a[1] - b[0]


def multiply(a, b):
    products = [x*y for x in a for y in b]
    return min(products), max(products)


def divide(a, b):
    if b[0]*b[1] <= 0:
        raise ValueError('Division interval meets zero')
    return multiply(a, (1/b[1], 1/b[0]))


def times(a, q):
    return multiply(a, singleton(q))


def rounded(a):
    lo, hi = a
    return (Q(lo.numerator*GRID//lo.denominator, GRID),
            Q(-((-hi.numerator*GRID)//hi.denominator), GRID))


def power_enclosure(q, n):
    # Binary powering, distinct from the producer's forward term recurrence.
    ans, base = singleton(1), singleton(q)
    while n:
        if n % 2:
            ans = rounded(multiply(ans, base))
        n //= 2
        if n:
            base = rounded(multiply(base, base))
    return ans


def log_partial(z, count):
    poly = singleton(Q(1, 2*count-1))
    for j in range(count-2, -1, -1):
        poly = rounded(add(singleton(Q(1, 2*j+1)), times(poly, z*z)))
    return rounded(times(poly, z))


def exp_partial(a, degree):
    poly = singleton(1)
    for k in range(degree, 0, -1):
        poly = rounded(add(singleton(1), times(poly, a/k)))
    return poly


def decimal(q, lower=False):
    with localcontext() as ctx:
        ctx.prec = 24
        ctx.rounding = ROUND_FLOOR if lower else ROUND_CEILING
        return str(Decimal(q.numerator)/Decimal(q.denominator))


def run():
    data = json.loads(SOURCE.read_text())
    logarithms, exponentials, arctangents = {}, {}, {}
    log_two = None
    previous = None
    kinds = Counter()
    for index, e in enumerate(data['evaluations']):
        kind = e['kind']
        kinds[kind] += 1
        label = f'evaluation {index} {kind}'
        box = read_interval(e['enclosure'])
        if kind == 'log_unit':
            v, z = rational(e['v']), rational(e['z'])
            n = e['count']
            equal(label+' term count', n, 100)
            record(label+' domain', 1 <= v <= 2, v, '[1,2]')
            equal(label+' transform', z, (v-1)/(v+1))
            if not (0 <= z <= Q(1, 3)):
                raise ValueError('Invalid logarithm transform')
            total = read_interval(e['sum'])
            omitted = read_interval(e['first_omitted_power'])
            contained(label+' partial sum', total, log_partial(z, n))
            contained(label+' omitted power', omitted, power_enclosure(z, 2*n+1))
            tail = rational(e['tail_upper'])
            equal(label+' tail formula', tail, 2*omitted[1]/((2*n+1)*(1-z*z)))
            contained(label+' final enclosure', box, (2*total[0], 2*total[1]+tail))
            if index == 0:
                equal(label+' log2 seed', v, Q(2))
                log_two = box
            previous = (v, box)
        elif kind == 'log_range_reduction':
            q, v, k = rational(e['q']), rational(e['v']), e['k']
            record(label+' reduced domain', 1 <= v < 2 and q > 0, v, '[1,2)')
            equal(label+' exact scaling', q, Q(2)**k*v)
            equal(label+' preceding unit argument', previous[0], v)
            contained(label+' signed recombination', box, add(times(log_two, k), previous[1]))
            if q in logarithms:
                equal(label+' repeated argument', box, logarithms[q])
            logarithms[q] = box
        elif kind == 'atan_reciprocal':
            n, count = e['n'], e['count']
            equal(label+' count', count, 100)
            record(label+' domain', n in (5, 239), n, [5, 239])
            total = sum((Q((-1)**j, (2*j+1)*n**(2*j+1)) for j in range(count)), Q(0))
            remainder = Q(1, (2*count+1)*n**(2*count+1))
            equal(label+' exact sum', rational(e['partial_sum']), total)
            equal(label+' alternating remainder', rational(e['remainder_upper']), remainder)
            contained(label+' enclosure', box, (total, total+remainder))
            arctangents[n] = box
        elif kind == 'exp':
            q, degree = rational(e['q']), e['degree']
            a = abs(q)
            equal(label+' degree', degree, 180)
            record(label+' tail ratio', a < degree+2, a, Q(degree+2))
            total, last = read_interval(e['sum']), read_interval(e['last_term'])
            contained(label+' Horner sum', total, exp_partial(a, degree))
            contained(label+' last term', last, times(power_enclosure(a, degree), Q(1, math.factorial(degree))))
            tail = rational(e['tail_upper'])
            equal(label+' geometric tail', tail, last[1]*a/(degree+1)/(1-a/(degree+2)))
            positive = total[0], total[1]+tail
            record(label+' positive denominator', positive[0] > 0, positive[0], Q(0))
            # The producer first rounds the positive upper endpoint to 10^-70.
            # Include that widening before checking its reciprocal enclosure.
            source_grid = 10**70
            upper = positive[1]
            upper = Q(-((-upper.numerator*source_grid)//upper.denominator), source_grid)
            positive = positive[0], upper
            inner = divide(singleton(1), positive) if q < 0 else positive
            contained(label+' signed exponential', box, inner)
            if q in exponentials:
                equal(label+' repeated argument', box, exponentials[q])
            exponentials[q] = box
        else:
            raise ValueError('Unknown primitive '+kind)
    equal('all evaluation kinds/counts', dict(kinds),
          {'log_unit': 133, 'log_range_reduction': 132, 'atan_reciprocal': 2, 'exp': 126})

    def log_interval(box):
        return logarithms[box[0]][0], logarithms[box[1]][1]

    def exp_interval(box):
        return exponentials[box[0]][0], exponentials[box[1]][1]

    X, t0, t1, cap = map(Q, ('6000284561421.5', '.16836', '.1718', '.500000000001'))
    for name, q in (('X', X), ('t0', t0), ('t1', t1), ('cap', cap)):
        equal('parameter '+name, rational(data['parameters'][name]), q)
    equal('producer grid', int(data['parameters']['grid_denominator']), 10**70)
    # Independently generate the complete prime list by the Eratosthenes sieve.
    flags = [True]*308
    flags[0] = flags[1] = False
    for p in range(2, 308):
        if flags[p]:
            for composite in range(p*p, 308, p):
                flags[composite] = False
    primes = [p for p in range(2, 308) if flags[p]]
    equal('complete prime list', data['primes'], primes)
    equal('prime count', len(primes), 63)
    equal('all prime rows exactly once', [r['p'] for r in data['prime_rows']], primes)
    corner = data['corner']
    pi = read_interval(corner['pi'])
    contained('Machin pi graph', pi, subtract(times(arctangents[5], 16), times(arctangents[239], 4)))
    log4pi = log_interval(times(pi, 4))
    L, Lstar, sigma = (read_interval(corner[k]) for k in ('L', 'Lstar', 'sigma'))
    contained('base logarithm graph', L, subtract(logarithms[X], log4pi))
    contained('Lstar graph', Lstar, subtract(times(logarithms[X*X+1], Q(1, 2)), log4pi))
    contained('sigma graph', sigma, add(singleton(Q('.5')-t0/(2*(1+X*X))), times(Lstar, t0/4)))
    nu_cap = Q(1, 2)+t1/(4*(X-6))
    equal('derivative cap graph', rational(corner['nu_derivative_cap']), nu_cap)
    expected_checks = [
        ('nu derivative cap', nu_cap, cap),
        ('time monotonicity for every prime', logarithms[Q(307)][1]+2/(1+X*X), Lstar[0]),
        ('base phase source lower height', Q('6000284561419.5'), X),
        ('base phase source upper time', t1, Q('.2')),
    ]
    sum_contributions = singleton(0)
    radius_uppers = []
    for row in data['prime_rows']:
        p = row['p']
        h, exponent, radius, denominator, contribution = (
            read_interval(row[k]) for k in ('log_p', 'exponent', 'r', 'denominator', 'loss_contribution'))
        equal(f'p={p} log linkage', h, logarithms[Q(p)])
        contained(f'p={p} exponent graph', exponent, subtract(times(multiply(h, h), t0/4), multiply(sigma, h)))
        equal(f'p={p} exp linkage', radius, exp_interval(exponent))
        record(f'p={p} positive radius', radius[0] > 0, radius[0], Q(0))
        contained(f'p={p} denominator graph', denominator, subtract(singleton(1), radius))
        record(f'p={p} positive denominator', denominator[0] > 0, denominator[0], Q(0))
        contained(f'p={p} loss graph', contribution, divide(multiply(h, radius), denominator))
        sum_contributions = add(sum_contributions, contribution)
        radius_uppers.append((radius[1], p))
        expected_checks.append((f'r_{p} < 1', radius[1], Q(1)))
    loss_sum = read_interval(data['loss_sum'])
    contained('complete loss sum graph', loss_sum, sum_contributions)
    floor = read_interval(data['phase_floor'])
    contained('phase floor graph', floor, subtract(L, times(loss_sum, 4*cap)))
    maximum, worst_prime = max(radius_uppers)
    equal('maximum radius graph', rational(data['max_radius_upper']), maximum)
    expected_checks += [
        ('uniform phase floor exceeds 24.18', Q('24.18'), floor[0]),
        ('maximum prime radius below .32926', maximum, Q('.32926')),
        ('displayed phase interval lower', Q('24.18022820120389189144'), floor[0]),
        ('displayed phase interval upper', floor[1], Q('24.18022820120389189145')),
    ]
    equal('complete source comparison names', [c['name'] for c in data['checks']], [c[0] for c in expected_checks])
    for c, (name, actual, required) in zip(data['checks'], expected_checks):
        equal(name+' actual linkage', rational(c['actual_upper']), actual)
        equal(name+' required linkage', rational(c['required_strict_upper']), required)
        record(name+' independent inequality', actual < required, actual, required)
        equal(name+' stored boolean', c['passed'], actual < required)
    equal('source failure list', data['failures'], [name for name, a, b in expected_checks if not a < b])
    equal('source result agrees with inequalities', data['result'], 'PASS' if all(a < b for _, a, b in expected_checks) else 'FAIL')
    record('source lower-time inclusion', t0 >= Q('.16836'), t0, Q('.16836'))
    summary.update({'primitive_evaluations': len(data['evaluations']), 'evaluation_kinds': dict(kinds),
                    'prime_rows': len(primes), 'source_comparisons': len(expected_checks),
                    'phase_floor': floor, 'required_floor': Q('24.18'),
                    'floor_margin': floor[0]-Q('24.18'), 'max_radius': maximum,
                    'worst_prime': worst_prime, 'required_radius': Q('.32926'),
                    'nu_cap': nu_cap, 'required_nu_cap': cap,
                    'time_monotonicity_margin': Lstar[0]-logarithms[Q(307)][1]-2/(1+X*X)})


try:
    run()
except Exception:
    record('audit completed without exception', False, traceback.format_exc(), 'no exception')

failures = [c['name'] for c in checks if not c['passed']]
report = {'result': 'FAIL' if failures else 'PASS',
          'method': 'Independent 10^-90 Horner/endpoint consumer; Eratosthenes prime sieve; no producer import or rerun.',
          'source_sha256': sha256(SOURCE.read_bytes()).hexdigest(),
          'producer_sha256': sha256(PRODUCER.read_bytes()).hexdigest(),
          'consumer_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
          'summary': serial(summary), 'checks': checks, 'failures': failures,
          'qualification': 'Arithmetic audit only; L496 supplies the analytic reduction and retains the imported Planat Lemma 6.3 premise.'}
OUTPUT.write_text(json.dumps(report, indent=2)+'\n')
print(f"{report['result']}: {len(checks)} independent checks; failures={failures}")
if summary:
    print(f"evaluations={summary['primitive_evaluations']}; primes={summary['prime_rows']}; source comparisons={summary['source_comparisons']}")
    print(f"phase lower={decimal(summary['phase_floor'][0], True)}; required >24.18; margin>{decimal(summary['floor_margin'], True)}")
    print(f"max radius upper={decimal(summary['max_radius'])}; required <.32926<1; worst prime={summary['worst_prime']}")
    print(f"nu cap upper={decimal(summary['nu_cap'])}; required <.500000000001")
print(f'certificate={OUTPUT.relative_to(HERE.parent.parent)}')
raise SystemExit(bool(failures))
