#!/usr/bin/env python3
"""Independent scalar replay of L499; no producer import or execution.

First reconstruct every stored row, bound and comparison on its grid.
Then reverse the prime traversal on a finer grid and require containment.
Previously audited transcendental and mass inputs remain explicit premises.
"""
from decimal import Decimal, localcontext, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'l499-certificate-audit.json'
records = []
report = {'scope': 'Fixed corner only; retained L494/L496 saddle/base-phase premises; '
                   'no transport or manuscript audit.'}


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def encode(v):
    if isinstance(v, F):
        return {'numerator': str(v.numerator), 'denominator': str(v.denominator)}
    if isinstance(v, tuple):
        return {'lower': encode(v[0]), 'upper': encode(v[1])}
    if isinstance(v, list):
        return [encode(x) for x in v]
    if isinstance(v, dict):
        return {k: encode(x) for k, x in v.items()}
    return v


def rat(v):
    if int(v['denominator']) <= 0:
        raise ValueError('nonpositive denominator')
    return F(int(v['numerator']), int(v['denominator']))


def interval(v):
    a, b = rat(v['lower']), rat(v['upper'])
    if a > b:
        raise ValueError('reversed input interval')
    return a, b


def require(name, condition, actual, required):
    records.append(dict(name=name, passed=bool(condition), actual=encode(actual),
                        required=encode(required)))
    if not condition:
        raise ValueError(name)


class Arithmetic:
    def __init__(self, digits):
        self.grid = 10**digits

    @staticmethod
    def pair(a):
        return a if isinstance(a, tuple) else (F(a), F(a))

    def round(self, a, b):
        q = self.grid
        return F(a.numerator*q//a.denominator, q), F(-((-b.numerator*q)//b.denominator), q)

    def add(self, a, b):
        a, b = self.pair(a), self.pair(b)
        return self.round(a[0]+b[0], a[1]+b[1])

    def sub(self, a, b):
        b = self.pair(b)
        return self.add(a, (-b[1], -b[0]))

    def mul(self, a, b):
        a, b = self.pair(a), self.pair(b)
        v = [a[i]*b[j] for i in (0, 1) for j in (0, 1)]
        return self.round(min(v), max(v))

    def div(self, a, b):
        b = self.pair(b)
        if b[0]*b[1] <= 0:
            raise ValueError('zero in divisor')
        return self.mul(a, self.round(1/b[1], 1/b[0]))


def replay(source, phase, mass, digits, reverse=False):
    a = Arithmetic(digits)
    tests = []

    def test(name, ok, actual, required):
        tests.append(dict(name=name, passed=bool(ok), actual=encode(actual), required=encode(required)))
        require(f'{digits}-grid: '+name, ok, actual, required)

    x, t, ell, n = F('6000284561421.5'), F('.16836'), F('24.18022820120389'), 691004
    cap, eps = F('.500000000001'), F('.0000006')
    eps1 = (eps+F('.0000013'))*F('8.770232')/F('.14142')
    source_hash = digest(ROOT/'finite-euler-phase-floor-certificate.json')
    test('retained phase audit links the exact source', source_hash == phase['source_sha256'],
         source_hash, phase['source_sha256'])
    test('retained phase audit complete', phase['result'] == 'PASS' and not phase['failures'],
         phase['result'], 'PASS, zero failures')
    test('retained mass audit complete', mass['complete'] and not mass['failures'],
         dict(complete=mass['complete'], failures=mass['failures']), 'complete, zero failures')
    parameters = [rat(source['parameters'][k]) for k in ('X', 't0')]
    test('corner parameters', parameters == [x, t], parameters, [x, t])
    pi, L, sigma = [interval(source['corner'][k]) for k in ('pi', 'L', 'sigma')]
    test('corner in L494 closed domain', t*L[1] < F('5.17'), t*L[1], '<5.17')
    floor = interval(source['phase_floor'])[0]
    test('imported phase lower exceeds ell0', floor > ell, floor, ell)
    derivative = rat(source['corner']['nu_derivative_cap'])
    test('imported nu derivative cap', derivative < cap, derivative, cap)
    cutoff = a.add(a.div(x, a.mul(4, pi)), t/16)
    test('cutoff lower endpoint', n*n <= cutoff[0], cutoff[0], n*n)
    test('cutoff upper endpoint', cutoff[1] < (n+1)**2, cutoff[1], (n+1)**2)
    moved = a.mul(a.mul(4, pi), n*n)[1]
    test('N squared below unmoved saddle', moved < x, moved, x)
    exponent = a.sub(sigma, a.div(a.mul(t, L), 8))
    test('power-sum envelope exponent', exponent[0] > F(53, 50), exponent[0], F(53, 50))
    primitive = 1+1/(F(53, 50)-1)
    test('power-sum integral arithmetic', primitive == F(53, 3), primitive, F(53, 3))
    # Eratosthenes, unlike the producer's trial-division prime list.
    sieve = [True]*308
    sieve[0] = sieve[1] = False
    for p in range(2, isqrt(307)+1):
        if sieve[p]:
            for k in range(p*p, 308, p):
                sieve[k] = False
    primes = [p for p in range(2, 308) if sieve[p]]
    row_primes = [r['p'] for r in source['prime_rows']]
    test('every prime row exactly once', source['primes'] == row_primes == primes and len(primes) == 63,
         row_primes, primes)
    R, J, logs = a.pair(1), a.pair(0), a.pair(0)
    rows = []
    for row in (reversed(source['prime_rows']) if reverse else source['prime_rows']):
        p, h, r = row['p'], interval(row['log_p']), interval(row['r'])
        test(f'positive log and radius p={p}', h[0] > 0 and r[0] > 0, [h[0], r[0]], '>0')
        den = a.sub(1, r)
        test(f'nonzero Euler denominator p={p}', den[0] > 0, den[0], '>0')
        term = a.div(a.mul(h, r), den)
        R, J, logs = a.mul(R, a.add(1, r)), a.add(J, term), a.add(logs, h)
        rows.append(dict(p=p, log_p=h, r=r, denominator=den, J_term=term))
    support = a.add(a.div(L, 2), logs)
    K = a.mul(a.mul(R, primitive), support)
    D = a.mul(a.mul(R, cap), J)
    Qalpha, Calpha = x*(x*x+5)/(1+x*x)**2, (7*x*x-5)/(1+x*x)**2
    sp, ec = t*Qalpha/4, t*Calpha/4
    test('both saddle corrections positive', sp > 0 and ec > 0, [sp, ec], '>0')
    Us = a.div(a.mul(4*(sp+ec), K), ell)
    Ur = a.add(a.div(a.mul(R, eps), 2),
               a.div(a.mul(2, a.add(a.mul(D, eps), a.mul(R, eps1))), ell))
    total = a.add(Us, Ur)
    prefix, complement = F('.698591427320603743332620581311'), F(21688332681815698, 72057594037927936)
    reserve = 1-prefix-complement
    for name, value in [('prefix_upper', prefix), ('complement_upper', complement),
                        ('full_upper', prefix+complement), ('reserve_lower', reserve)]:
        test('mass exact linkage '+name, F(mass[name]) == value, F(mass[name]), value)
    margin = a.sub(reserve, total)
    for name, actual, required in [
        ('positive product cap', R[1], F(3)),
        ('full logarithmic moment cap', K[1], F(23000)),
        ('saddle charge coarse bound', Us[1], F('1e-10')),
        ('remainder charge coarse bound', Ur[1], F('.00003')),
        ('total charge coarse bound', total[1], F('.00003')),
        ('total charge reported bound', total[1], F('.000020830490')),
        ('decisive total charge below reserve', total[1], reserve)]:
        test(name, actual < required, actual, required)
    for threshold in ('.00039', '.00040166'):
        test('remaining margin exceeds '+threshold, margin[0] > F(threshold), margin[0], F(threshold))
    bounds = dict(power_exponent=exponent, primitive_sum_cap=primitive, R=R, Jplus=J,
                  log_support=support, Lhat_cap=K, product_derivative_cap=D, Qalpha=Qalpha,
                  Calpha=Calpha, sigma_prime=sp, eta_prime_minus_half=ec,
                  charge_saddle=Us, charge_remainder=Ur, charge_total=total,
                  reserve_lower=reserve, margin=margin)
    return rows, bounds, tests


def run():
    names = ['finite-euler-phase-floor-certificate.json', 'l496-certificate-audit.json',
             'mass-audit/audit.json', 'fixed-corner-two-charge.json']
    source, phase, mass, old = [json.loads((ROOT/n).read_text()) for n in names]
    report['inputs'] = [dict(path=n, sha256=digest(ROOT/n)) for n in names]
    # Validate the producer's exact input linkage, separately from its flags.
    expected_inputs = [dict(path=n, sha256=digest(ROOT/n)) for n in names[:3]]
    require('all input hashes retained', old['inputs'] == expected_inputs, old['inputs'], expected_inputs)
    producer_hash = digest(ROOT/'fixed-corner-two-charge.py')
    require('producer hash retained', old['script_sha256'] == producer_hash,
            old['script_sha256'], producer_hash)
    require('elementary inputs identical', old['elementary_inputs'] ==
            {k: source['corner'][k] for k in ('pi', 'L', 'Lstar', 'sigma')},
            old['elementary_inputs'], 'all four exact source entries')
    expected_parameters = dict(x=F('6000284561421.5'), t=F('.16836'),
        ell0=F('24.18022820120389'), N=691004, cap=F('.500000000001'), epsilon=F('.0000006'),
        epsilon_1=F(20829301, 176775000000), grid_denominator=str(10**50))
    require('all exact parameters', old['parameters'] == encode(expected_parameters),
            old['parameters'], expected_parameters)
    rows, bounds, tests = replay(source, phase, mass, 50)
    require('all 63 complete prime rows exactly reconstructed', old['prime_rows'] == encode(rows),
            len(old['prime_rows']), len(rows))
    require('all 16 complete scalar fields exactly reconstructed', old['bounds'] == encode(bounds),
            old['bounds'], bounds)
    require('all 153 actual/required records exactly reconstructed', old['checks'] == tests and len(tests) == 153,
            len(old['checks']), len(tests))
    require('original final status consistent', old['result'] == 'PASS' and old['failures'] == [],
            dict(result=old['result'], failures=old['failures']), 'PASS with zero failures')
    fine_rows, fine, fine_tests = replay(source, phase, mass, 90, reverse=True)
    coarse_by_prime = {r['p']: r for r in rows}
    for row in fine_rows:
        for k in ('log_p', 'r', 'denominator', 'J_term'):
            outer, inner = coarse_by_prime[row['p']][k], row[k]
            require(f'finer row containment {row["p"]} {k}',
                    outer[0] <= inner[0] <= inner[1] <= outer[1], inner, outer)
    for k, inner in fine.items():
        outer = bounds[k]
        ok = (outer[0] <= inner[0] <= inner[1] <= outer[1]) if isinstance(inner, tuple) else outer == inner
        require('reverse finer-grid containment '+k, ok, inner, outer)
    report.update(reconstructed_source_comparisons=tests, finer_prime_rows=fine_rows,
                  finer_bounds=fine, finer_comparisons=fine_tests,
                  input_rows=63, source_comparisons=153, bound_fields=16)


try:
    run()
except Exception as exc:
    report['exception'] = f'{type(exc).__name__}: {exc}'
    if not records or records[-1]['passed']:
        records.append(dict(name='complete execution', passed=False, actual=report['exception'], required='no exception'))
failures = [r['name'] for r in records if not r['passed']]
report.update(result='FAIL' if failures else 'PASS', checks=records, failures=failures,
              audit_script_sha256=digest(Path(__file__)))
OUT.write_text(json.dumps(encode(report), indent=2)+'\n')
print(f"{report['result']}: {len(records)} audit checks; failures={failures}; certificate={OUT.relative_to(ROOT.parent.parent)}")
if 'finer_bounds' in report:
    b = report['finer_bounds']
    for name, v, rounding in [('total charge upper', b['charge_total'][1], ROUND_CEILING),
                              ('reserve lower', b['reserve_lower'], ROUND_FLOOR),
                              ('remaining margin lower', b['margin'][0], ROUND_FLOOR)]:
        with localcontext() as ctx:
            ctx.prec, ctx.rounding = 26, rounding
            print(f'{name}={Decimal(v.numerator)/Decimal(v.denominator)}')
    print('required: total charge upper < reserve lower; margin lower > .00040166')
raise SystemExit(bool(failures))
