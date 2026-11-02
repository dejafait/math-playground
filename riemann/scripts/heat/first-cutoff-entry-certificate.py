#!/usr/bin/env python3
"""One full entering block, enlarged full support, and both resultant charges.

Exact rational interval arithmetic; prior audited corner inputs are reused.
No source transport decimal, partial-cell fall or coefficient replay is used.
Analytic qualifications and the signed comparison are stated in C499b.
"""
from decimal import Decimal, localcontext, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
OUT = HERE / 'first-cutoff-entry-certificate.json'
GRID, LOG_TERMS, EXP_DEGREE = 10**60, 100, 180
checks, evaluations = [], []
report = dict(scope='One point Y=4*pi*(691005^2-.16836/16), full entry '
                   '691004 -> 691005, constant ell0, no fall credit. '
                   'Imported saddle/base-phase proofs remain unaudited.',
              method='Outward rational grid intervals; range-reduced atanh '
                     'logarithms and positive Taylor/geometric exponential '
                     'tails. All squarefree channels bounded by finite Euler '
                     'expansion and a full-output logarithmic envelope.')


def down(a):
    return F(a.numerator*GRID//a.denominator, GRID)


def up(a):
    return -down(-a)


class Box:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        if self.lo > self.hi:
            raise ValueError('reversed interval')

    def __add__(self, other):
        other = box(other)
        return Box(down(self.lo+other.lo), up(self.hi+other.hi))

    __radd__ = __add__

    def __neg__(self):
        return Box(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -box(other)

    def __rsub__(self, other):
        return box(other) + -self

    def __mul__(self, other):
        other = box(other)
        v = [a*b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return Box(down(min(v)), up(max(v)))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = box(other)
        if other.lo*other.hi <= 0:
            raise ValueError('zero in denominator interval')
        return self * Box(down(1/other.hi), up(1/other.lo))

    def __rtruediv__(self, other):
        return box(other)/self


def box(a):
    return a if isinstance(a, Box) else Box(a)


def encode(a):
    if isinstance(a, F):
        return dict(numerator=str(a.numerator), denominator=str(a.denominator))
    if isinstance(a, Box):
        return dict(lower=encode(a.lo), upper=encode(a.hi))
    if isinstance(a, (list, tuple)):
        return [encode(v) for v in a]
    if isinstance(a, dict):
        return {k: encode(v) for k, v in a.items()}
    return a


def rat(a):
    n, d = int(a['numerator']), int(a['denominator'])
    if d <= 0:
        raise ValueError('nonpositive rational denominator')
    return F(n, d)


def read(a):
    return Box(rat(a['lower']), rat(a['upper']))


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def check(name, passed, actual, required):
    checks.append(dict(name=name, passed=bool(passed), actual=encode(actual),
                       required=encode(required)))
    if not passed:
        raise ValueError(name)


def log_unit(v):
    if not 1 <= v <= 2:
        raise ValueError('logarithm range reduction failed')
    z = (v-1)/(v+1)
    z2, power, total = z*z, box(z), Box(0)
    for j in range(LOG_TERMS):
        total = total + power/(2*j+1)
        power = power*z2
    tail = 2*power.hi/((2*LOG_TERMS+1)*(1-z2))
    ans = Box(down(2*total.lo), up(2*total.hi+tail))
    evaluations.append(dict(kind='log_unit', v=v, z=z, terms=LOG_TERMS,
                            half_sum=total, first_omitted_power=power,
                            tail_upper=tail, enclosure=ans))
    return ans


def exp_exact(a):
    u, term, total = abs(a), Box(1), Box(1)
    if not u < EXP_DEGREE+2:
        raise ValueError('exponential tail ratio invalid')
    for j in range(1, EXP_DEGREE+1):
        term = term*u/j
        total = total + term
    ratio = u/(EXP_DEGREE+2)
    tail = term.hi*u/(EXP_DEGREE+1)/(1-ratio)
    positive = Box(total.lo, up(total.hi+tail))
    ans = positive
    if a < 0:
        ans = Box(1)/positive
    evaluations.append(dict(kind='exp', argument=a, degree=EXP_DEGREE,
                            sum=total, last_term=term, subsequent_ratio_cap=ratio,
                            tail_upper=tail, positive_enclosure=positive,
                            enclosure=ans))
    return ans


def contains(outer, inner):
    return outer.lo <= inner.lo <= inner.hi <= outer.hi


def run():
    cp, ap = HERE/'fixed-corner-two-charge.json', HERE/'l499-certificate-audit.json'
    corner, audit = [json.loads(p.read_text()) for p in (cp, ap)]
    report['inputs'] = [dict(path=p.name, sha256=digest(p)) for p in (cp, ap)]
    check('prior independent audit completed',
          audit['result'] == 'PASS' and audit['failures'] == [],
          dict(result=audit['result'], failures=audit['failures']), 'PASS; no failures')
    for row in audit['inputs']:
        check('current audited input '+row['path'], digest(HERE/row['path']) == row['sha256'],
              digest(HERE/row['path']), row['sha256'])
    check('corner covered by prior audit',
          [r['sha256'] for r in audit['inputs'] if r['path'] == cp.name] == [digest(cp)],
          digest(cp), 'same corner certificate retained by audit')
    X, t, oldN, q = F('6000284561421.5'), F('.16836'), 691004, 691005
    ell0, cap, eps = F('24.18022820120389'), F('.500000000001'), F('.0000006')
    eps1 = (eps+F('.0000013'))*F('8.770232')/F('.14142')
    expected = dict(x=X, t=t, N=oldN, ell0=ell0, cap=cap, epsilon=eps,
                    epsilon_1=eps1, grid_denominator=str(10**50))
    check('exact inherited parameters', corner['parameters'] == encode(expected),
          corner['parameters'], expected)
    report['parameters'] = dict(X=X, t=t, old_N=oldN, new_N=q, ell0=ell0,
                                cap=cap, epsilon=eps, epsilon_1=eps1,
                                grid_denominator=str(GRID), channels=2**63,
                                first_cell_fall_credit=0)
    pi, LX, sigma = [read(corner['elementary_inputs'][k]) for k in ('pi', 'L', 'sigma')]
    report['elementary_inputs'] = dict(pi=pi, LX=LX, sigma_at_X=sigma)
    b = corner['bounds']
    R0, J0, D0 = [read(b[k]) for k in ('R', 'Jplus', 'product_derivative_cap')]
    primes = [p for p in range(2, 308) if all(p % d for d in range(2, isqrt(p)+1))]
    check('all 63 prime rows in full', len(primes) == 63
          and [r['p'] for r in corner['prime_rows']] == primes,
          [r['p'] for r in corner['prime_rows']], primes)
    sum_logs, R, J = Box(0), Box(1), Box(0)
    for row in corner['prime_rows']:
        h, r = read(row['log_p']), read(row['r'])
        check('positive prime data p='+str(row['p']), h.lo > 0 and 0 < r.lo <= r.hi < 1,
              [h, r], 'log>0 and 0<r<1')
        sum_logs, R, J = sum_logs+h, R*(1+r), J+h*r/(1-r)
    check('retained R0 contains full Euler product', contains(R0, R), R, R0)
    check('retained J0 contains full derivative sum', contains(J0, J), J, J0)
    check('retained D0 covers product derivative', contains(D0, R0*cap*J0), R0*cap*J0, D0)
    # Exact cancellation in the defining Y expression establishes equality.
    y_coefficient = F(q*q)-t/16
    boundary_square = y_coefficient+t/16
    check('one new primitive index', q == oldN+1, q, oldN+1)
    check('symbolic cutoff equality', boundary_square == q*q, boundary_square, q*q)
    check('canonical new integer cutoff', q >= 0 and q*q <= boundary_square < (q+1)**2,
          boundary_square, dict(lower=q*q, upper_excluded=(q+1)**2))
    Y = 4*pi*y_coefficient
    width = Y-X
    LY_upper = LX.hi+width.hi/X
    check('positive first displacement', width.lo > 0, width, '>0')
    check('closed time domain', F('.16836') <= t <= F('.1718'), t, '[.16836,.1718]')
    check('closed analytic boundary domain', t*LY_upper < F('5.17'), t*LY_upper, '<5.17')
    check('old anchor cutoff below entry', (X/(4*pi)+t/16).hi < q*q,
          X/(4*pi)+t/16, '<691005^2')
    report['domain'] = dict(Y=Y, width=width, LY_upper=LY_upper, tLY_upper=t*LY_upper,
                            Y_over_four_pi=y_coefficient, cutoff_square=boundary_square,
                            canonical_cutoff=q, derivative_frozen_at=q)
    # New elementary evaluation is only log(q) and w_q(X).
    k, v = 0, F(q)
    while v >= 2:
        v /= 2
        k += 1
    log2 = log_unit(F(2))
    logq = k*log2+log_unit(v)
    exponent = (t/4)*logq*logq-sigma*logq
    weight = Box(exp_exact(exponent.lo).lo, exp_exact(exponent.hi).hi)
    check('positive new logarithm', logq.lo > 0, logq, '>0')
    check('negative entering exponent', exponent.hi < 0, exponent, '<0')
    check('entering weight threshold', 0 < weight.lo <= weight.hi < F('.00000061'),
          weight, '0<w_q(X)<.00000061')
    support = logq+sum_logs
    h_cap = 1+2*support/ell0
    jump_cap = weight*R0*h_cap
    primitive_cap = F(53, 3)+weight
    Knew = R0*primitive_cap*support
    check('support cap enlarged from old cap',
          support.lo > read(b['log_support']).hi, support, '>old support cap')
    check('new log envelope enlarged', Knew.lo > read(b['Lhat_cap']).hi,
          Knew, '>old K0')
    check('primitive integral cap retained', rat(b['primitive_sum_cap']) == F(53, 3),
          rat(b['primitive_sum_cap']), F(53, 3))
    Q, C = X*(X*X+5)/(1+X*X)**2, (7*X*X-5)/(1+X*X)**2
    check('both rational corrections retained', Q == rat(b['Qalpha'])
          and C == rat(b['Calpha']) and Q > 0 and C > 0 and X >= 2,
          [Q, C, X], 'L499 Q,C positive and decreasing for x>=X>=2')
    Us = t*(Q+C)*Knew/ell0
    Ur = R0*eps/2+2*(D0*eps+R0*eps1)/ell0
    total = jump_cap+Us+Ur
    r0 = F(14176540015048665224252705167939023,
           33554432000000000000000000000000000000)
    check('exact old audited full-mass reserve', rat(b['reserve_lower']) == r0,
          rat(b['reserve_lower']), r0)
    margin = r0-total
    report['elementary_new'] = dict(log_range_reduction=dict(k=k, v=v), log_q=logq,
                                    exponent_at_X=exponent, weight_at_X=weight)
    report['envelopes'] = dict(sum_prime_logs=sum_logs, R0=R0, J0=J0, D0=D0,
                              full_output_log_cap=support, full_output_h_cap=h_cap,
                              entering_jump_cap=jump_cap, new_primitive_sum_cap=primitive_cap,
                              new_Lhat_cap=Knew, Q_at_X=Q, C_at_X=C,
                              charge_saddle_new=Us, charge_remainder_new=Ur,
                              combined_cost=total, reserve_lower=r0, remaining_margin=margin)
    check('full-entry strict reserve', total.hi < r0, total.hi, r0)
    check('reported conservative remaining margin', margin.lo > F('.000369'),
          margin, '>.000369')


try:
    run()
except Exception as exc:
    report['exception'] = f'{type(exc).__name__}: {exc}'
    if not checks or checks[-1]['passed']:
        checks.append(dict(name='execution completed', passed=False,
                           actual=report['exception'], required='no exception'))
failures = [r['name'] for r in checks if not r['passed']]
report.update(result='FAIL' if failures else 'PASS', checks=checks, failures=failures,
              elementary_evaluations=evaluations, script_sha256=digest(Path(__file__)))
OUT.write_text(json.dumps(encode(report), indent=2)+'\n')


def dec(a, upper=True):
    with localcontext() as ctx:
        ctx.prec = 26
        ctx.rounding = ROUND_CEILING if upper else ROUND_FLOOR
        return str(Decimal(a.numerator)/Decimal(a.denominator))


print(f"{report['result']}: {len(checks)} checks; failures={failures}")
if 'envelopes' in report:
    e = report['envelopes']
    for key in ('entering_jump_cap', 'new_Lhat_cap', 'charge_saddle_new',
                'charge_remainder_new', 'combined_cost'):
        print(f"{key} <= {dec(e[key].hi)}")
    print(f"required combined_cost < r0={dec(e['reserve_lower'], False)}")
    print(f"remaining_margin >= {dec(e['remaining_margin'].lo, False)}; required >.000369")
print(f'certificate={OUT.relative_to(HERE.parent.parent)}')
raise SystemExit(bool(failures))
