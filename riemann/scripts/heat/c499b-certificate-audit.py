#!/usr/bin/env python3
"""Independent exact-rational consumer for C499b; never imports the producer.

Reuses accepted L496/L499 inputs, not their stored flags as new proofs.
Direct finite series and unrounded endpoint operations verify the new data.
The signed-support and analytic implications are audited in canonical C499b.
"""
from fractions import Fraction as Q
from decimal import Decimal, localcontext, ROUND_CEILING, ROUND_FLOOR
from hashlib import sha256
from math import factorial
from pathlib import Path
import json
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
OUT = HERE / 'c499b-certificate-audit.json'
checks, inputs, consumed = [], [], set()
report = {'scope': 'C499b only; accepted elementary/mass inputs retained. '
          'Saddle and base-phase manuscript proofs remain unaudited.',
          'method': 'Exact Fraction endpoint operations without grid rounding; '
          'direct powers/factorials independently reconstruct elementary sums.'}


class Interval:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = Q(lo), Q(lo if hi is None else hi)
        if self.lo > self.hi:
            raise ValueError('reversed interval')

    def __add__(self, b):
        b = interval(b)
        return Interval(self.lo+b.lo, self.hi+b.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, b):
        return self + -interval(b)

    def __rsub__(self, b):
        return interval(b) + -self

    def __mul__(self, b):
        b = interval(b)
        values = [x*y for x in (self.lo, self.hi) for y in (b.lo, b.hi)]
        return Interval(min(values), max(values))

    __rmul__ = __mul__

    def __truediv__(self, b):
        b = interval(b)
        if b.lo <= 0 <= b.hi:
            raise ValueError('zero denominator')
        return self * Interval(1/b.hi, 1/b.lo)

    def __rtruediv__(self, b):
        return interval(b)/self


def interval(a):
    return a if isinstance(a, Interval) else Interval(a)


def decode(a):
    if isinstance(a, float):
        raise ValueError('floating point certificate entry')
    if isinstance(a, dict):
        if set(a) == {'numerator', 'denominator'}:
            n, d = int(a['numerator']), int(a['denominator'])
            if d <= 0:
                raise ValueError('nonpositive rational denominator')
            return Q(n, d)
        if set(a) == {'lower', 'upper'}:
            return Interval(decode(a['lower']), decode(a['upper']))
        return {k: decode(v) for k, v in a.items()}
    if isinstance(a, list):
        return [decode(v) for v in a]
    return a


def encode(a):
    if isinstance(a, Q):
        return {'numerator': str(a.numerator), 'denominator': str(a.denominator)}
    if isinstance(a, Interval):
        return {'lower': encode(a.lo), 'upper': encode(a.hi)}
    if isinstance(a, dict):
        return {k: encode(v) for k, v in a.items()}
    if isinstance(a, (list, tuple)):
        return [encode(v) for v in a]
    return a


def covers(outer, inner):
    if isinstance(outer, Interval):
        inner = interval(inner)
        return outer.lo <= inner.lo <= inner.hi <= outer.hi
    if isinstance(outer, dict) and isinstance(inner, dict):
        return set(outer) == set(inner) and all(covers(outer[k], inner[k]) for k in outer)
    if isinstance(outer, list) and isinstance(inner, list):
        return len(outer) == len(inner) and all(covers(x, y) for x, y in zip(outer, inner))
    return outer == inner


def same(a, b):
    return covers(a, b) and covers(b, a)


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def load(name):
    p = HERE/name
    inputs.append({'path': name, 'sha256': digest(p)})
    return decode(json.loads(p.read_text()))


def check(name, passed, actual, required):
    checks.append({'name': name, 'passed': bool(passed), 'actual': actual,
                   'required': required})
    if not passed:
        raise ValueError(name)


def enclosure(name, stored, rebuilt):
    check(name, covers(stored, rebuilt), stored, rebuilt)
    return stored


def equal(name, stored, rebuilt):
    check(name, same(stored, rebuilt), stored, rebuilt)
    return stored


def linkage(label, rows):
    for row in rows:
        equal(label+' '+row['path'], digest(HERE/row['path']), row['sha256'])


def claim(name, passed, actual, required):
    """Independently test each producer comparison and its complete payload."""
    row = claims[name]
    consumed.add(name)
    check('claim: '+name, passed and row['passed'] is True
          and covers(row['actual'], actual) and same(row['required'], required),
          row, {'passed_by_consumer': bool(passed), 'actual': actual, 'required': required})


def audit_log(row, v):
    equal('log kind', row['kind'], 'log_unit')
    equal('log argument', row['v'], v)
    equal('log term count', row['terms'], 100)
    z = (v-1)/(v+1)
    equal('log transformed argument', row['z'], z)
    check('log positive range', 1 <= v <= 2 and 0 <= z <= Q(1, 3), [v, z], '[1,2], [0,1/3]')
    # Direct powers and exact sum, independent of the producer's rounded recurrence.
    partial = sum((z**(2*j+1)/Q(2*j+1) for j in range(100)), Q(0))
    power = z**201
    half = enclosure('log complete half sum', row['half_sum'], partial)
    omitted = enclosure('log first omitted power', row['first_omitted_power'], power)
    tail = 2*power/(201*(1-z*z))
    equal('log stored tail formula', row['tail_upper'], 2*omitted.hi/(201*(1-z*z)))
    check('log complete omitted tail', row['tail_upper'] >= tail,
          row['tail_upper'], tail)
    enclosure('log output rounding', row['enclosure'],
              Interval(2*half.lo, 2*half.hi+row['tail_upper']))
    enclosure('log direct series enclosure', row['enclosure'], Interval(2*partial, 2*partial+tail))
    return row['enclosure']


def audit_exp(row, arg):
    equal('exp kind', row['kind'], 'exp')
    equal('exp endpoint', row['argument'], arg)
    equal('exp degree', row['degree'], 180)
    u = abs(arg)
    check('exp negative endpoint and geometric ratio', arg < 0 and u < 182, arg, '-182<argument<0')
    terms = [u**j/Q(factorial(j)) for j in range(181)]
    partial, last = sum(terms, Q(0)), terms[-1]
    total = enclosure('exp complete Taylor sum', row['sum'], partial)
    final = enclosure('exp degree-180 term', row['last_term'], last)
    equal('exp subsequent ratio', row['subsequent_ratio_cap'], u/182)
    tail = (u**181/Q(factorial(181)))/(1-u/182)
    equal('exp stored tail formula', row['tail_upper'], final.hi*u/181/(1-u/182))
    check('exp full omitted tail', row['tail_upper'] >= tail, row['tail_upper'], tail)
    positive = enclosure('exp positive outward sum', row['positive_enclosure'],
                         Interval(total.lo, total.hi+row['tail_upper']))
    check('exp reciprocal positive denominator', positive.lo > 0, positive, '>0')
    answer = enclosure('exp reciprocal outwardness', row['enclosure'], 1/positive)
    enclosure('exp independent direct enclosure', answer,
              Interval(1/(partial+tail), 1/partial))
    return answer


def run():
    global claims
    original = load('first-cutoff-entry-certificate.json')
    corner = load('fixed-corner-two-charge.json')
    prior = load('l499-certificate-audit.json')
    phase = load('finite-euler-phase-floor-certificate.json')
    phase_audit = load('l496-certificate-audit.json')
    mass = load('mass-audit/audit.json')
    equal('current producer identity', original['script_sha256'],
          digest(HERE/'first-cutoff-entry-certificate.py'))
    equal('original report completed', [original['result'], original['failures']], ['PASS', []])
    equal('original exact input list', [r['path'] for r in original['inputs']],
          ['fixed-corner-two-charge.json', 'l499-certificate-audit.json'])
    linkage('original input identity', original['inputs'])
    linkage('corner input identity', corner['inputs'])
    linkage('prior accepted audit input identity', prior['inputs'])
    # These checks establish identity of already accepted mathematical inputs only.
    check('accepted phase audit retained', phase_audit['result'] == 'PASS'
          and phase_audit['failures'] == [],
          [phase_audit['result'], phase_audit['failures']], ['PASS', []])
    claims = {r['name']: r for r in original['checks']}
    equal('unique original comparisons', len(claims), len(original['checks']))
    claim('prior independent audit completed', prior['result'] == 'PASS' and prior['failures'] == [],
          {'result': prior['result'], 'failures': prior['failures']}, 'PASS; no failures')
    for row in prior['inputs']:
        claim('current audited input '+row['path'], digest(HERE/row['path']) == row['sha256'],
              digest(HERE/row['path']), row['sha256'])
    chash = digest(HERE/'fixed-corner-two-charge.json')
    claim('corner covered by prior audit',
          [r['sha256'] for r in prior['inputs'] if r['path'] == 'fixed-corner-two-charge.json'] == [chash],
          chash, 'same corner certificate retained by audit')
    X, t, n, q = Q('6000284561421.5'), Q('.16836'), 691004, 691005
    ell, c, eps = Q('24.18022820120389'), Q('.500000000001'), Q('.0000006')
    eps1 = (eps+Q('.0000013'))*Q('8.770232')/Q('.14142')
    old_parameters = dict(x=X, t=t, N=n, ell0=ell, cap=c, epsilon=eps,
                          epsilon_1=eps1, grid_denominator=str(10**50))
    claim('exact inherited parameters', same(corner['parameters'], old_parameters),
          corner['parameters'], old_parameters)
    equal('all new parameters', original['parameters'],
          dict(X=X, t=t, old_N=n, new_N=q, ell0=ell, cap=c, epsilon=eps,
               epsilon_1=eps1, grid_denominator=str(10**60), channels=2**63,
               first_cell_fall_credit=0))
    for key in ('pi', 'L', 'sigma'):
        equal('elementary input linkage '+key, corner['elementary_inputs'][key], phase['corner'][key])
    pi, lx, sigma = [corner['elementary_inputs'][k] for k in ('pi', 'L', 'sigma')]
    equal('new elementary input linkage', original['elementary_inputs'],
          dict(pi=pi, LX=lx, sigma_at_X=sigma))
    check('positive inherited domain data', min(pi.lo, lx.lo, sigma.lo) > 0,
          [pi, lx, sigma], '>0')
    # Sieve independently checks completeness, unlike producer trial division.
    flags = [True]*308
    flags[0] = flags[1] = False
    for p in range(2, 308):
        if flags[p]:
            for multiple in range(2*p, 308, p):
                flags[multiple] = False
    primes = [p for p in range(308) if flags[p]]
    equal('phase full prime set', [r['p'] for r in phase['prime_rows']], primes)
    claim('all 63 prime rows in full', len(primes) == 63
          and [r['p'] for r in corner['prime_rows']] == primes,
          [r['p'] for r in corner['prime_rows']], primes)
    logsum, product, derivative_sum = Interval(0), Interval(1), Interval(0)
    for row, source in zip(corner['prime_rows'], phase['prime_rows']):
        p, h, r = row['p'], row['log_p'], row['r']
        equal('accepted full prime row '+str(p), [h, r], [source['log_p'], source['r']])
        claim('positive prime data p='+str(p), h.lo > 0 and 0 < r.lo <= r.hi < 1,
              [h, r], 'log>0 and 0<r<1')
        enclosure('prime denominator '+str(p), row['denominator'], 1-r)
        enclosure('prime derivative summand '+str(p), row['J_term'], h*r/(1-r))
        logsum, product, derivative_sum = logsum+h, product*(1+r), derivative_sum+h*r/(1-r)
    b, env = corner['bounds'], original['envelopes']
    R, J, D = b['R'], b['Jplus'], b['product_derivative_cap']
    for name, exact, bound in [('retained R0 contains full Euler product', product, R),
                               ('retained J0 contains full derivative sum', derivative_sum, J),
                               ('retained D0 covers product derivative', R*c*J, D)]:
        claim(name, covers(bound, exact), exact, bound)
        enclosure('stored actual bounded: '+name, bound, claims[name]['actual'])
    for key, value in [('R0', R), ('J0', J), ('D0', D)]:
        equal('retained envelope '+key, env[key], value)
    logs = enclosure('complete sum of prime logs', env['sum_prime_logs'], logsum)
    coef = Q(q*q)-t/16
    square = coef+t/16
    claim('one new primitive index', q == n+1, q, n+1)
    claim('symbolic cutoff equality', square == q*q, square, q*q)
    claim('canonical new integer cutoff', q >= 0 and q*q <= square < (q+1)**2,
          square, dict(lower=q*q, upper_excluded=(q+1)**2))
    dom = original['domain']
    Y = enclosure('boundary interval', dom['Y'], 4*pi*coef)
    width = enclosure('boundary displacement', dom['width'], Y-X)
    equal('domain log bound', dom['LY_upper'], lx.hi+width.hi/X)
    equal('domain time times log bound', dom['tLY_upper'], t*dom['LY_upper'])
    for key, value in [('Y_over_four_pi', coef), ('cutoff_square', square),
                       ('canonical_cutoff', q), ('derivative_frozen_at', q)]:
        equal('domain '+key, dom[key], value)
    claim('positive first displacement', width.lo > 0, width, '>0')
    claim('closed time domain', Q('.16836') <= t <= Q('.1718'), t, '[.16836,.1718]')
    claim('closed analytic boundary domain', dom['tLY_upper'] < Q('5.17'), dom['tLY_upper'], '<5.17')
    anchor_cutoff = X/(4*pi)+t/16
    claim('old anchor cutoff below entry', anchor_cutoff.hi < q*q, anchor_cutoff, '<691005^2')
    check('old anchor lower cutoff', anchor_cutoff.lo >= n*n, anchor_cutoff, n*n)
    rows = original['elementary_evaluations']
    equal('complete elementary evaluation count', len(rows), 4)
    new = original['elementary_new']
    equal('range reduction', new['log_range_reduction'], dict(k=19, v=Q(q, 2**19)))
    l2, lv = audit_log(rows[0], Q(2)), audit_log(rows[1], Q(q, 2**19))
    logq = enclosure('range-reduced log q', new['log_q'], 19*l2+lv)
    exponent = enclosure('new weight exponent', new['exponent_at_X'], t/4*logq*logq-sigma*logq)
    elo, ehi = audit_exp(rows[2], exponent.lo), audit_exp(rows[3], exponent.hi)
    weight = equal('exp endpoint assembly', new['weight_at_X'], Interval(elo.lo, ehi.hi))
    claim('positive new logarithm', logq.lo > 0, logq, '>0')
    claim('negative entering exponent', exponent.hi < 0, exponent, '<0')
    claim('entering weight threshold', 0 < weight.lo <= weight.hi < Q('.00000061'),
          weight, '0<w_q(X)<.00000061')
    support = enclosure('full output support', env['full_output_log_cap'], logq+logs)
    hcap = enclosure('full output weight cap', env['full_output_h_cap'], 1+2*support/ell)
    jump = enclosure('all entering channels', env['entering_jump_cap'], weight*R*hcap)
    primitive = enclosure('new primitive cap', env['new_primitive_sum_cap'], Q(53, 3)+weight)
    K = enclosure('new logarithmic envelope', env['new_Lhat_cap'], R*primitive*support)
    claim('support cap enlarged from old cap', support.lo > b['log_support'].hi, support, '>old support cap')
    claim('new log envelope enlarged', K.lo > b['Lhat_cap'].hi, K, '>old K0')
    claim('primitive integral cap retained', b['primitive_sum_cap'] == Q(53, 3),
          b['primitive_sum_cap'], Q(53, 3))
    qa, ca = X*(X*X+5)/(1+X*X)**2, (7*X*X-5)/(1+X*X)**2
    claim('both rational corrections retained', qa == b['Qalpha'] and ca == b['Calpha']
          and qa > 0 and ca > 0 and X >= 2, [qa, ca, X],
          'L499 Q,C positive and decreasing for x>=X>=2')
    equal('saddle Q endpoint', env['Q_at_X'], qa)
    equal('saddle C endpoint', env['C_at_X'], ca)
    us = enclosure('complete saddle charge', env['charge_saddle_new'], t*(qa+ca)*K/ell)
    ur = enclosure('complete remainder charge', env['charge_remainder_new'],
                   R*eps/2+2*(D*eps+R*eps1)/ell)
    total = enclosure('complete comparison', env['combined_cost'], jump+us+ur)
    r0 = Q(14176540015048665224252705167939023, 33554432000000000000000000000000000000)
    equal('accepted mass replay completed', [mass['complete'], mass['failures']], [True, []])
    equal('mass reserve identity', Q(mass['reserve_lower']), r0)
    equal('mass full sum identity', Q(mass['full_upper']), Q(mass['prefix_upper'])+Q(mass['complement_upper']))
    equal('reserve complement identity', 1-Q(mass['full_upper']), r0)
    equal('new reserve linkage', env['reserve_lower'], r0)
    claim('exact old audited full-mass reserve', b['reserve_lower'] == r0, b['reserve_lower'], r0)
    margin = enclosure('complete remaining margin', env['remaining_margin'], r0-total)
    claim('full-entry strict reserve', total.hi < r0, total.hi, r0)
    claim('reported conservative remaining margin', margin.lo > Q('.000369'), margin, '>.000369')
    # Verify every stronger decimal actually printed in C499b, not just the coarse producer tests.
    for name, actual, printed in [
        ('domain', dom['tLY_upper'], '4.527504235458053'),
        ('weight', weight.hi, '.000000596314200997666'),
        ('support', support.hi, '296.197762161536'),
        ('log envelope', K.hi, '10814.174447541029'),
        ('jump', jump.hi, '.000031423761288557'),
        ('saddle charge', us.hi, '.000000000012548738'),
        ('remainder charge', ur.hi, '.000020830477230729'),
        ('combined cost', total.hi, '.000052254251068023')]:
        check('printed upper '+name, actual < Q(printed), actual, Q(printed))
    check('printed lower margin', margin.lo > Q('.000370239564802521'),
          margin.lo, Q('.000370239564802521'))
    equal('all producer comparisons consumed', sorted(consumed), sorted(claims))
    equal('producer comparison count', len(consumed), 91)
    report['bounds'] = dict(jump_upper=jump.hi, saddle_upper=us.hi,
                            remainder_upper=ur.hi, cost_upper=total.hi,
                            required_cost_strict_upper=r0, margin_lower=margin.lo,
                            required_margin_strict_lower=Q('.000370239564802521'))
    report['producer_checks_consumed'] = len(consumed)


try:
    run()
except Exception as exc:
    report['exception'] = f'{type(exc).__name__}: {exc}'
    if not checks or checks[-1]['passed']:
        checks.append(dict(name='consumer completed', passed=False,
                           actual=report['exception'], required='no exception'))
failures = [r['name'] for r in checks if not r['passed']]
report.update(result='FAIL' if failures else 'PASS', checks=checks, failures=failures,
              inputs=inputs, script_sha256=digest(Path(__file__)))
OUT.write_text(json.dumps(encode(report), indent=2)+'\n')


def display(x, upper):
    with localcontext() as ctx:
        ctx.prec = 26
        ctx.rounding = ROUND_CEILING if upper else ROUND_FLOOR
        return str(Decimal(x.numerator)/Decimal(x.denominator))


print(f"{report['result']}: {len(checks)} independent checks; failures={failures}")
if 'bounds' in report:
    for name, value in report['bounds'].items():
        # Display actual upper bounds upward, required upper thresholds downward;
        # reverse these directions for lower bounds. Exact fractions are saved.
        round_up = name.endswith('upper') != name.startswith('required_')
        print(f"{name}={display(value, round_up)}")
print(f'certificate={OUT.relative_to(HERE.parent.parent)}')
raise SystemExit(bool(failures))
