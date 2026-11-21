#!/usr/bin/env python3
"""Audit the fixed546 witness; preserve every original artifact.

Replay all intervals at90 digits and the entire remote matrix. Independently
check integer prime-power coverage and exact rational stored-matrix products.
Analytic/IEEE execution qualifications are in C744z Section9.
"""
import ctypes
import hashlib
import json
import platform
import sys
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from fractions import Fraction as F
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    original = json.loads((BASE/'response-prefix-stop-546.json').read_text())
    names = ['response-prefix-stop-546.py', 'response-prefix-stop-546.json',
             'response-prefix-direction-546.json', 'response-prefix-remote-546.npz',
             'complete-covariance-532.npz', 'complete-schur-531.py',
             'residual-certificate-532.py', 'matrix-tail-audit-541.json',
             'certificate-audit-534.json']
    hashes_before = {name: digest(BASE/name) for name in names}
    failures, interval_checks, rational_checks = [], [], []

    def check(ok, label):
        if not ok:
            failures.append(label)

    # Re-execute the whole frozen generator with more precision and new outputs.
    # The sole Decimal unary minus on a raw endpoint occurs in a support
    # assertion, not an enclosure. Use exact negation in this replay too.
    source = (BASE/'response-prefix-stop-546.py').read_text()
    source = source.replace('I = mod.I', '''mod.DOWN = Context(prec=90, rounding=ROUND_FLOOR)
mod.UP = Context(prec=90, rounding=ROUND_CEILING)
mod.NEAR = Context(prec=90, rounding=ROUND_HALF_EVEN)
I = mod.I''')
    source = source.replace('-ell.lo < delta.lo', 'ell.lo.copy_negate() < delta.lo')
    source = source.replace("BASE/'response-prefix-remote-546.npz'",
                            "BASE/'response-prefix-remote-replay-548.npz'")
    source = source.replace("BASE/'response-prefix-stop-546.json'",
                            "BASE/'response-prefix-replay-548.json'")
    namespace = dict(__file__=str(BASE/'response-prefix-stop-546.py'),
                     Context=Context, ROUND_FLOOR=ROUND_FLOOR,
                     ROUND_CEILING=ROUND_CEILING, ROUND_HALF_EVEN=ROUND_HALF_EVEN)
    exec(compile(source, str(BASE/'response-prefix-stop-546.py'), 'exec'), namespace)
    replay = namespace['result']

    def intervals(a, b, path=''):
        if isinstance(a, dict) and set(a) == {'lo', 'hi'}:
            ok = F(a['lo']) <= F(b['lo']) <= F(b['hi']) <= F(a['hi'])
            interval_checks.append(dict(path=path, contained=ok,
                                        original=a, audit=b))
            check(ok, 'interval containment '+path)
        elif isinstance(a, dict):
            for key in a.keys() & b.keys():
                intervals(a[key], b[key], path+'/'+key)
        elif isinstance(a, list):
            check(len(a) == len(b), 'list length '+path)
            for i, (x, y) in enumerate(zip(a, b)):
                intervals(x, y, path+'/'+str(i))

    intervals(original, replay)
    check(replay['direction'] == original['direction'], 'all exact direction data')
    check(original['direction']['sha256'] == hashes_before['response-prefix-direction-546.json'],
          'original direction hash')
    check(original['direction']['denominator'] == 2**40, 'dyadic denominator')
    check(original['remote']['matrices']['sha256'] == hashes_before['response-prefix-remote-546.npz'],
          'original remote matrix hash')
    prior541 = json.loads((BASE/'matrix-tail-audit-541.json').read_text())
    prior534 = json.loads((BASE/'certificate-audit-534.json').read_text())
    for row in original['input_hashes']:
        check(row['actual'] == row['expected'] == hashes_before[row['path']]
              == prior534['original_sha256'][row['path']], 'inherited534 hash '+row['path'])
    check(not prior541['failures'] and not prior534['failures'], 'inherited audit failures')

    # Independent sieve/exponent enumeration, rather than546 trial division.
    sieve = [True]*4000
    sieve[0] = sieve[1] = False
    for p in range(2, 64):
        if sieve[p]:
            for n in range(p*p, 4000, p):
                sieve[n] = False
    powers = []
    for p in range(2, 4000):
        if sieve[p]:
            n = p
            while n < 4000:
                if 3**13 < n*n < 3**15:
                    powers.append((n, p))
                n *= p
    powers.sort()
    rows = replay['remote']['primes']
    check(powers == [(r['n'], r['prime']) for r in rows], 'all remote prime powers')
    check(len(powers) == 334 and 4000**2 > 3**15, 'complete integer cutoff')
    for r in rows:
        check(F(r['weight_float_error']) < F(1, 10**16)
              and F(r['delay_float_error']) < F(1, 10**16), 'conversion '+str(r['n']))
        lo, hi = F(r['delta']['lo']), F(r['delta']['hi'])
        check((lo == hi == 0) if r['n'] == 2187 else (hi < 0 or lo > 0),
              'strict delay sign '+str(r['n']))
        check(-F(replay['constants']['ell']['lo']) < lo <= hi
              < F(replay['constants']['ell']['lo']), 'exact overlap '+str(r['n']))
    with np.load(BASE/'response-prefix-remote-546.npz') as archive:
        remote = archive['remote_prime'].copy()
    rebuilt = namespace['remote_matrix']
    check(np.array_equal(remote, rebuilt), 'all262144 remote entries replay')

    # Exact integer accumulation independently checks every stored-matrix
    # scalar product. Coefficient uncertainty comes from90-digit enclosures.
    scale = 10**110
    coeff = {}
    for name in ['f', 'g', 'h']:
        values, eps = [], F(0)
        for interval in replay['coefficients'][name]:
            lo, hi = F(interval['lo']), F(interval['hi'])
            integer = ((lo+hi)*scale/2).__floor__()
            point = F(integer, scale)
            values.append(integer)
            eps += max(abs(lo-point), abs(hi-point))
        coeff[name] = (values, eps)

    def exact_bilinear(label, matrix, xn, yn, stored):
        x, ex = coeff[xn]
        y, ey = coeff[yn]
        entries = [[float(v).as_integer_ratio() for v in row] for row in matrix]
        denominator = max(d for row in entries for _, d in row)
        integer = sum(y[i]*sum(x[j]*n*(denominator//d)
                      for j, (n, d) in enumerate(row)) for i, row in enumerate(entries))
        center = F(integer, denominator*scale*scale)
        maximum = max(abs(F(n, d)) for row in entries for n, d in row)
        lx, ly = F(sum(map(abs, x)), scale), F(sum(map(abs, y)), scale)
        error = maximum*(lx*ey+ly*ex+ex*ey)
        lo, hi = center-error, center+error
        ok = F(stored['lo']) <= lo <= hi <= F(stored['hi'])
        rational_checks.append(dict(label=label, integer_sum=str(integer),
            matrix_denominator=str(denominator), coefficient_denominator=str(scale),
            coefficient_uncertainty=str(error), exact_lower=str(lo), exact_upper=str(hi),
            required_enclosure=stored, passed=ok, matrix_entries=matrix.size))
        check(ok, 'exact rational product '+label)

    with np.load(BASE/'complete-covariance-532.npz') as archive:
        head = archive['m0']
        seven = archive['mc']+archive['mg']
    exact_bilinear('head f', head, 'f', 'f', original['heads']['f_center'])
    exact_bilinear('head g', head, 'g', 'g', original['heads']['g_center'])
    exact_bilinear('T f,g', seven, 'f', 'g', original['seven']['centers'][0])
    exact_bilinear('T g,h', seven, 'g', 'h', original['seven']['centers'][1])
    exact_bilinear('U f,h', remote, 'f', 'h', original['remote']['center'])

    # Independent explicit moment integration: this is a consistency check;
    # the exact identity in C744z(19)-(20) establishes neutrality.
    I, k2, nu = namespace['I'], namespace['k2'], namespace['nu']
    fourth = namespace['fourth']
    moments = []
    for name in ['f', 'g', 'h']:
        for sign in [-1, 1]:
            exponential = fourth if sign == 1 else 1/fourth
            value = sum((nu[n]*(I(sign)/2)*(((-1)**n)*exponential-1)
                         /(I('.25')+k2[n])*namespace[name][n]
                         for n in range(512)), I(0))
            ok = value.lo <= 0 <= value.hi
            moments.append(dict(profile=name, sign=sign, enclosure=value.json(), contains_zero=ok))
            check(ok, 'moment check '+name+str(sign))

    runtime = dict(python=sys.version, numpy=np.__version__, machine=platform.machine(),
        decimal_precision=namespace['mod'].NEAR.prec,
        fegetround=ctypes.CDLL(None).fegetround(),
        float_mantissa=sys.float_info.mant_dig, float_radix=sys.float_info.radix,
        qualification='Observed runtime only; IEEE754 basic operations/sqrt and Decimal contracts remain explicit hypotheses.')
    check(runtime['fegetround'] == 0 and runtime['float_mantissa'] == 53
          and runtime['float_radix'] == 2, 'runtime rounding and binary64')
    check(all(original['checks'].values()) and not original['failures'], 'original546 checks')
    check(all(replay['checks'].values()) and not replay['failures'], 'replay548 checks')
    hashes_after = {name: digest(BASE/name) for name in names}
    check(hashes_before == hashes_after, 'all original artifacts preserved')
    result = dict(scope='C744z Section8 fixed32 response comparison only',
        runtime=runtime, input_hashes=hashes_before, originals_unchanged=hashes_before == hashes_after,
        interval_checks=interval_checks, exact_rational_products=rational_checks,
        independent_prime_powers=powers, remote_entries_reproduced=int(remote.size),
        moments=moments, summary=replay['summary'], failures=failures,
        limitations=['Imported analytic identity and IEEE754/Decimal contracts remain.',
                    'Exact neutrality and form-core continuity also require the canonical analytic proof.',
                    'This does not sign the full residual, give an H2 witness, or resolve RH.'])
    path = BASE/'response-prefix-audit-548.json'
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('All interval checks:', len(interval_checks), 'exact matrix products:', len(rational_checks),
          'remote translations:', len(powers), 'remote entries:', remote.size)
    print('Failures:', failures, 'certificate:', path.relative_to(BASE.parent.parent))
    assert not failures


if __name__ == '__main__':
    main()
