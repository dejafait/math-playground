#!/usr/bin/env python3
"""Independent exact consumer of C499a's complete first-cell scalar evidence.

Imports no producer routines and does not rewrite the evidence being audited.
Audited L499 enclosures are inputs, not re-proved transcendental/mass facts.
"""
from dataclasses import dataclass
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'c499a-certificate-audit.json'
checks = []
result = {'scope': 'C499a interval application and complete scalar consumption; '
          'L494-L499 analytic qualifications retained; endpoint Y excluded.'}


@dataclass(frozen=True)
class Interval:
    lo: F
    hi: F

    def __post_init__(self):
        if self.lo > self.hi:
            raise ValueError('reversed interval')

    def __add__(self, other):
        b = interval(other)
        return Interval(self.lo + b.lo, self.hi + b.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-interval(other))

    def __mul__(self, other):
        b = interval(other)
        products = (self.lo*b.lo, self.lo*b.hi, self.hi*b.lo, self.hi*b.hi)
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = interval(other)
        if b.lo <= 0 <= b.hi:
            raise ValueError('zero in divisor')
        return self * Interval(1/b.hi, 1/b.lo)

    def contains(self, other):
        b = interval(other)
        return self.lo <= b.lo <= b.hi <= self.hi


def interval(a):
    return a if isinstance(a, Interval) else Interval(F(a), F(a))


def encode(a):
    if isinstance(a, F):
        return {'numerator': str(a.numerator), 'denominator': str(a.denominator)}
    if isinstance(a, Interval):
        return {'lower': encode(a.lo), 'upper': encode(a.hi)}
    if isinstance(a, dict):
        return {k: encode(v) for k, v in a.items()}
    if isinstance(a, (list, tuple)):
        return [encode(v) for v in a]
    return a


def decode(a):
    if isinstance(a, dict):
        if set(a) == {'numerator', 'denominator'}:
            n, d = int(a['numerator']), int(a['denominator'])
            if d <= 0:
                raise ValueError('nonpositive rational denominator')
            return F(n, d)
        if set(a) == {'lower', 'upper'}:
            return Interval(decode(a['lower']), decode(a['upper']))
        return {k: decode(v) for k, v in a.items()}
    if isinstance(a, list):
        return [decode(v) for v in a]
    return a


def digest(name):
    return sha256((ROOT/name).read_bytes()).hexdigest()


def check(name, predicate, actual, required):
    checks.append({'name': name, 'passed': bool(predicate),
                   'actual': encode(actual), 'required': encode(required)})
    if not predicate:
        raise ValueError(name)


def equal(name, actual, required):
    check(name, encode(actual) == encode(required), actual, required)


def run():
    names = ['first-frozen-cell-certificate.json', 'fixed-corner-two-charge.json',
             'l499-certificate-audit.json']
    cell, corner, audit = [decode(json.loads((ROOT/n).read_text())) for n in names]
    result['inputs'] = [{'path': n, 'sha256': digest(n)} for n in names]
    expected_inputs = [{'path': n, 'sha256': digest(n)} for n in names[1:]]
    equal('complete C499a input provenance', cell['inputs'], expected_inputs)
    equal('C499a producer hash', cell['script_sha256'], digest('first-frozen-cell-certificate.py'))
    # Verify current identity of the retained audited files; do not replay them.
    for entry in audit['inputs']:
        equal('retained L499 audit input '+entry['path'], digest(entry['path']), entry['sha256'])
    equal('L499 producer hash', corner['script_sha256'], digest('fixed-corner-two-charge.py'))

    x, t, n = F('6000284561421.5'), F('.16836'), 691004
    ell, cap, eps = F('24.18022820120389'), F('.500000000001'), F('0.0000006')
    eps1 = F('0.0000019')*F('8.770232')/F('.14142')
    prior_params = dict(x=x, t=t, N=n, ell0=ell, cap=cap, epsilon=eps,
                        epsilon_1=eps1, grid_denominator=str(10**50))
    params = dict(X=x, t=t, N=n, ell0=ell, cap=cap, epsilon=eps,
                  epsilon_1=eps1, Y_definition='4*pi*((N+1)^2-t/16)',
                  right_endpoint_included=False)
    equal('complete interval parameters including open endpoint', cell['parameters'], params)
    pi, lx = corner['elementary_inputs']['pi'], corner['elementary_inputs']['L']
    equal('both inherited elementary intervals', cell['elementary_inputs'], dict(pi=pi, LX=lx))
    y = pi * (4*(n+1)**2-t/4)
    width = y-x
    relative = width/x
    cutoff = interval(x)/(pi*4)+t/16
    lower_edge = pi*(4*n*n)
    log_upper = lx.hi + relative.hi
    domain = dict(Y=y, width=width, relative_width=relative, cutoff_X=cutoff,
                  four_pi_N_squared=lower_edge, LY_upper=log_upper, tLY_upper=t*log_upper)
    equal('all seven interval-domain fields', cell['domain'], domain)

    b = corner['bounds']
    R, J, S, K, D = [b[k] for k in ('R', 'Jplus', 'log_support', 'Lhat_cap', 'product_derivative_cap')]
    us, ur, total = [b[k] for k in ('charge_saddle', 'charge_remainder', 'charge_total')]
    q = x*(x*x+5)/(x*x+1)**2
    c = (7*x*x-5)/(x*x+1)**2
    saddle = K*(t*(q+c)/ell)
    remainder = R*(eps/2)+(D*eps+R*eps1)*(2/ell)
    reserve = 1-F('.698591427320603743332620581311')-F(21688332681815698, 72057594037927936)
    margin = interval(reserve)-total
    envelopes = dict(R0=R, J0=J, S0=S, K0=K, D0=D, Q_at_X=q, C_at_X=c,
                     charge_saddle=us, charge_remainder=ur, charge_total=total,
                     reserve_lower=reserve, remaining_margin=margin)
    equal('all twelve uniform-envelope fields', cell['uniform_envelopes'], envelopes)

    # Recompute predicates and actual/required values before reading stored flags.
    reconstructed = []

    def comparison(name, predicate, actual, required):
        record = dict(name=name, passed=bool(predicate), actual=actual, required=required)
        check('recomputed comparison '+name, predicate, actual, required)
        reconstructed.append(record)

    links = [v['sha256'] for v in audit['inputs'] if v['path'] == names[1]]
    comparison('exact L499 certificate retained by prior audit', links == [digest(names[1])], links, [digest(names[1])])
    comparison('prior audit completion record', audit['result'] == 'PASS' and audit['failures'] == [],
               dict(result=audit['result'], failures=audit['failures']), 'PASS; no failures')
    comparison('all inherited exact parameters', corner['parameters'] == prior_params, corner['parameters'], prior_params)
    comparison('positive inherited elementary intervals', pi.lo > 0 and lx.lo > 0, [pi.lo, lx.lo], '>0')
    comparison('spatial derivative monotonicity range', x >= 2, x, '>=2')
    comparison('time in L494 and L496 closed domain', F('.16836') <= t <= F('.1718'), t, '[.16836,.1718]')
    comparison('nonempty open cell', width.lo > 0, width, '>0')
    comparison('anchor cutoff lower bound', cutoff.lo >= n*n, cutoff, '>=691004^2')
    comparison('anchor cutoff upper bound', cutoff.hi < (n+1)**2, cutoff, '<691005^2')
    comparison('fixed support log N below L(X)/2', lower_edge.hi < x, lower_edge, x)
    comparison('whole cell in uniform analytic domain', t*log_upper < F('5.17'), t*log_upper, '<5.17')
    for label, value in [('R', R), ('Jplus', J), ('S0', S), ('K0', K), ('D0', D)]:
        comparison('positive inherited '+label, value.lo > 0, value, '>0')
    comparison('exact inherited saddle corrections', b['Qalpha'] == q and b['Calpha'] == c and q > 0 and c > 0,
               [q, c], 'L499 values, both positive')
    comparison('retained enclosure for saddle charge', us.contains(saddle), saddle, us)
    comparison('retained enclosure for remainder charge', ur.contains(remainder), remainder, ur)
    comparison('retained total covers both charges', total.contains(us+ur), us+ur, total)
    comparison('exact complete mass reserve', b['reserve_lower'] == reserve, reserve, b['reserve_lower'])
    comparison('uniform total charge threshold', total.hi < F('.000020830490'), total, '<.000020830490')
    comparison('strict uniform reserve comparison', total.hi < reserve, total.hi, reserve)
    comparison('uniform remaining margin threshold', margin.lo > F('.00040166'), margin, '>.00040166')
    equal('exactly 24 producer comparisons', len(reconstructed), 24)
    for index, record in enumerate(reconstructed):
        equal('complete actual/required record '+str(index), cell['checks'][index], record)
    equal('no unconsumed producer comparisons', len(cell['checks']), len(reconstructed))
    equal('stored producer result', cell['result'], 'PASS')
    equal('stored producer failures', cell['failures'], [])

    # Additional checks not delegated to the stored cell comparisons.
    check('positive denominators and frozen derivative cap', ell > 0 and cap > 0, [ell, cap], '>0')
    check('K0 contains R0*(53/3)*S0', K.contains(R*S*F(53, 3)), R*S*F(53, 3), K)
    check('D0 contains R0*cap*J0', D.contains(R*J*cap), R*J*cap, D)
    check('canonical r0 exact fraction', reserve == F(14176540015048665224252705167939023,
          33554432000000000000000000000000000000), reserve, 'C499a exact fraction')
    for label, enclosed, low, high in [
        ('Y', y, '6000290041249.8045187868265', '6000290041249.8045187868266'),
        ('width', width, '5479828.3045187868265380786', '5479828.3045187868265380787')]:
        check('canonical strict decimal enclosure '+label,
              F(low) < enclosed.lo <= enclosed.hi < F(high), enclosed, [F(low), F(high)])
    check('canonical displayed log-domain upper bound', t*log_upper < F('4.5275042354580522005720508'),
          t*log_upper, F('4.5275042354580522005720508'))
    check('canonical displayed charge upper bound', total.hi <= F('.000020830489779465538884432261'),
          total.hi, F('.000020830489779465538884432261'))
    check('canonical displayed margin lower bound', margin.lo >= F('.00040166332609107773910199603'),
          margin.lo, F('.00040166332609107773910199603'))
    result.update(parameters=params, reconstructed_domain=domain,
                  reconstructed_envelopes=envelopes, producer_comparisons=reconstructed,
                  qualifications=['L499 finite inputs and audit retained, not re-proved.',
                  'L494 saddle and L496 base-phase manuscripts remain unaudited.',
                  'Rational consumer does not prove analytic transport; see C499a audit.',
                  'No claim for endpoint Y, other cells/times, H1, zero time or RH.'])


try:
    run()
except Exception as exc:
    result['exception'] = f'{type(exc).__name__}: {exc}'
    if not checks or checks[-1]['passed']:
        checks.append(dict(name='execution completed', passed=False,
                           actual=result['exception'], required='no exception'))
failures = [c['name'] for c in checks if not c['passed']]
result.update(result='FAIL' if failures else 'PASS', checks=checks, failures=failures,
              script_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
OUT.write_text(json.dumps(encode(result), indent=2)+'\n')


def decimal(q, upper):
    with localcontext() as ctx:
        ctx.prec = 26
        ctx.rounding = ROUND_CEILING if upper else ROUND_FLOOR
        return str(Decimal(q.numerator)/Decimal(q.denominator))


print(f"{result['result']}: {len(checks)} independent checks; failures={failures}")
if 'reconstructed_domain' in result:
    d, e = result['reconstructed_domain'], result['reconstructed_envelopes']
    print('Complete consumption: 24/24 comparison records, 7/7 domain fields, 12/12 envelope fields.')
    print(f"width >= {decimal(d['width'].lo, False)}; required >0; Y excluded")
    print(f"t*L(Y) <= {decimal(d['tLY_upper'], True)}; required <5.17")
    print(f"charge <= {decimal(e['charge_total'].hi, True)}; required <.000020830490")
    print(f"margin >= {decimal(e['remaining_margin'].lo, False)}; required >.00040166")
print(f'certificate={OUT.relative_to(ROOT.parent.parent)}')
raise SystemExit(bool(failures))
