#!/usr/bin/env python3
"""L499: exact scalar comparison, reusing the audited L496/L498 inputs.

No transcendental evaluation, coefficient replay or sampled phase is used.
The imported intervals and their provenance are retained in the output.
"""
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
GRID = 10**50
checks = []


def down(a):
    return F(a.numerator * GRID // a.denominator, GRID)


def up(a):
    return -down(-a)


def serial(a):
    if isinstance(a, F):
        return {"numerator": str(a.numerator), "denominator": str(a.denominator)}
    if isinstance(a, Box):
        return {"lower": serial(a.lo), "upper": serial(a.hi)}
    if isinstance(a, dict):
        return {k: serial(v) for k, v in a.items()}
    if isinstance(a, (list, tuple)):
        return [serial(v) for v in a]
    return a


class Box:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        if self.lo > self.hi:
            raise ValueError("Reversed interval")

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
        ends = [a*b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return Box(down(min(ends)), up(max(ends)))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = box(other)
        if other.lo*other.hi <= 0:
            raise ValueError("Denominator interval contains zero")
        return self * Box(down(1/other.hi), up(1/other.lo))


def box(a):
    return a if isinstance(a, Box) else Box(a)


def rational(a):
    d = int(a['denominator'])
    if d <= 0:
        raise ValueError("Nonpositive rational denominator")
    return F(int(a['numerator']), d)


def read_box(a):
    return Box(rational(a['lower']), rational(a['upper']))


def check(name, passed, actual, required):
    checks.append(dict(name=name, passed=bool(passed), actual=serial(actual),
                       required=serial(required)))
    if not passed:
        raise ValueError(name)


def sha(path):
    return sha256(path.read_bytes()).hexdigest()


def decimal(a, lower=False):
    with localcontext() as ctx:
        ctx.prec = 24
        ctx.rounding = ROUND_FLOOR if lower else ROUND_CEILING
        return str(Decimal(a.numerator)/Decimal(a.denominator))


def run():
    source_path = ROOT/'finite-euler-phase-floor-certificate.json'
    phase_audit_path = ROOT/'l496-certificate-audit.json'
    mass_audit_path = ROOT/'mass-audit/audit.json'
    source = json.loads(source_path.read_text())
    phase_audit = json.loads(phase_audit_path.read_text())
    mass = json.loads(mass_audit_path.read_text())
    result['inputs'] = [dict(path=str(p.relative_to(ROOT)), sha256=sha(p))
                        for p in (source_path, phase_audit_path, mass_audit_path)]
    check('retained phase audit links the exact source',
          sha(source_path) == phase_audit['source_sha256'], sha(source_path), phase_audit['source_sha256'])
    check('retained phase audit complete', phase_audit['result'] == 'PASS'
          and phase_audit['failures'] == [], phase_audit['result'], 'PASS, zero failures')
    check('retained mass audit complete', mass['complete'] and mass['failures'] == [],
          dict(complete=mass['complete'], failures=mass['failures']), 'complete, zero failures')
    x, t, ell0, N = F('6000284561421.5'), F('.16836'), F('24.18022820120389'), 691004
    cap, eps = F('.500000000001'), F('0.0000006')
    eps1 = (eps+F('.0000013'))*F('8.770232')/F('.14142')
    check('corner parameters', rational(source['parameters']['X']) == x
          and rational(source['parameters']['t0']) == t,
          [rational(source['parameters']['X']), rational(source['parameters']['t0'])], [x, t])
    pi, L, sigma = (read_box(source['corner'][k]) for k in ('pi', 'L', 'sigma'))
    result['elementary_inputs'] = {k: source['corner'][k] for k in ('pi', 'L', 'Lstar', 'sigma')}
    result['parameters'] = dict(x=x, t=t, ell0=ell0, N=N, cap=cap, epsilon=eps,
                                epsilon_1=eps1, grid_denominator=str(GRID))
    check('corner in L494 closed domain', t*L.hi < F('5.17'), t*L.hi, '<5.17')
    floor_input = read_box(source['phase_floor'])
    check('imported phase lower exceeds ell0', floor_input.lo > ell0, floor_input.lo, ell0)
    check('imported nu derivative cap', rational(source['corner']['nu_derivative_cap']) < cap,
          rational(source['corner']['nu_derivative_cap']), cap)
    cutoff_square = Box(x)/(4*pi)+t/16
    check('cutoff lower endpoint', N*N <= cutoff_square.lo, cutoff_square.lo, N*N)
    check('cutoff upper endpoint', cutoff_square.hi < (N+1)**2, cutoff_square.hi, (N+1)**2)
    check('N squared below unmoved saddle', (4*pi*N*N).hi < x, (4*pi*N*N).hi, x)
    a = sigma-t*L/8
    a0, primitive_sum_cap = F(53, 50), F(53, 3)
    check('power-sum envelope exponent', a.lo > a0, a.lo, a0)
    check('power-sum integral arithmetic', 1+1/(a0-1) == primitive_sum_cap,
          1+1/(a0-1), primitive_sum_cap)
    primes = [p for p in range(2, 308) if all(p % d for d in range(2, isqrt(p)+1))]
    check('every prime row exactly once', source['primes'] == primes
          and [r['p'] for r in source['prime_rows']] == primes and len(primes) == 63,
          [r['p'] for r in source['prime_rows']], primes)
    R, Jplus, sum_logs = Box(1), Box(0), Box(0)
    rows = []
    for row in source['prime_rows']:
        p = row['p']
        h, r = read_box(row['log_p']), read_box(row['r'])
        check(f'positive log and radius p={p}', h.lo > 0 and r.lo > 0, [h.lo, r.lo], '>0')
        denominator = 1-r
        check(f'nonzero Euler denominator p={p}', denominator.lo > 0, denominator.lo, '>0')
        term = h*r/denominator
        R, Jplus, sum_logs = R*(1+r), Jplus+term, sum_logs+h
        rows.append(dict(p=p, log_p=h, r=r, denominator=denominator, J_term=term))
    log_support = L/2+sum_logs
    Lhat_cap = R*primitive_sum_cap*log_support
    product_derivative_cap = R*cap*Jplus
    Qalpha = x*(x*x+5)/(1+x*x)**2
    Calpha = (7*x*x-5)/(1+x*x)**2
    sigma_prime, eta_correction = t*Qalpha/4, t*Calpha/4
    check('both saddle corrections positive', sigma_prime > 0 and eta_correction > 0,
          [sigma_prime, eta_correction], '>0')
    charge_saddle = 4*(sigma_prime+eta_correction)*Lhat_cap/ell0
    charge_remainder = R*eps/2+2*(product_derivative_cap*eps+R*eps1)/ell0
    charge_total = charge_saddle+charge_remainder
    prefix = F('0.698591427320603743332620581311')
    complement = F(21688332681815698, 72057594037927936)
    reserve = 1-prefix-complement
    for name, actual in (('prefix_upper', prefix), ('complement_upper', complement),
                         ('full_upper', prefix+complement), ('reserve_lower', reserve)):
        check('mass exact linkage '+name, F(mass[name]) == actual, F(mass[name]), actual)
    margin = Box(reserve)-charge_total
    # These coarse thresholds are outputs checked against complete exact intervals.
    for name, actual, required in (
            ('positive product cap', R.hi, F(3)),
            ('full logarithmic moment cap', Lhat_cap.hi, F(23000)),
            ('saddle charge coarse bound', charge_saddle.hi, F('1e-10')),
            ('remainder charge coarse bound', charge_remainder.hi, F('.00003')),
            ('total charge coarse bound', charge_total.hi, F('.00003')),
            ('total charge reported bound', charge_total.hi, F('.000020830490')),
            ('decisive total charge below reserve', charge_total.hi, reserve)):
        check(name, actual < required, actual, required)
    check('remaining margin exceeds .00039', margin.lo > F('.00039'), margin.lo, F('.00039'))
    check('remaining margin exceeds .00040166', margin.lo > F('.00040166'), margin.lo, F('.00040166'))
    result.update(prime_rows=rows, bounds=dict(power_exponent=a, primitive_sum_cap=primitive_sum_cap,
                  R=R, Jplus=Jplus, log_support=log_support, Lhat_cap=Lhat_cap,
                  product_derivative_cap=product_derivative_cap, Qalpha=Qalpha, Calpha=Calpha,
                  sigma_prime=sigma_prime, eta_prime_minus_half=eta_correction,
                  charge_saddle=charge_saddle, charge_remainder=charge_remainder,
                  charge_total=charge_total, reserve_lower=reserve, margin=margin))


result = {'scope': 'Fixed corner only; source base-phase and saddle imports remain qualified. '
          'No transport, other-time, zero-time, global collision exclusion or RH claim.',
          'method': 'Exact Fraction intervals on a 10^-50 grid, using audited transcendental inputs; '
          'full positive Euler channels and source power-sum integral envelope.',
          'script_sha256': sha(Path(__file__))}
try:
    run()
except Exception as exc:
    result['exception'] = f'{type(exc).__name__}: {exc}'
    if not checks or checks[-1]['passed']:
        checks.append(dict(name='execution completed', passed=False, actual=result['exception'], required='no exception'))
failures = [r['name'] for r in checks if not r['passed']]
result.update(result='FAIL' if failures else 'PASS', checks=checks, failures=failures)
output = ROOT/'fixed-corner-two-charge.json'
output.write_text(json.dumps(serial(result), indent=2)+'\n')
print(f"{result['result']}: {len(checks)} checks; failures={failures}")
if 'bounds' in result:
    b = result['bounds']
    for name in ('R', 'Jplus', 'Lhat_cap', 'product_derivative_cap', 'charge_saddle', 'charge_remainder', 'charge_total'):
        print(f'{name} upper={decimal(b[name].hi)}')
    print(f"reserve lower={decimal(b['reserve_lower'], True)}; required charge_total upper < reserve lower")
    print(f"remaining margin lower={decimal(b['margin'].lo, True)}; required >.00039")
print(f'certificate={output.relative_to(ROOT.parent.parent)}')
raise SystemExit(bool(failures))
