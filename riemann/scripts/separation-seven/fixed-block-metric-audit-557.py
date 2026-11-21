#!/usr/bin/env python3
"""Audit C999k without changing its trial or reference allocation.

Replay all rows at 90 Decimal digits into separate artifacts. Independently
use integer outward intervals, exact dyadic matrix products for H*y and
F*F^t, and a complete weighted residual sum. Decimal ln retains the stated
correct-rounding contract; entry formula/IEEE754 contracts remain inputs.
"""
import hashlib
import importlib.util
import json
import math
import os
import subprocess
import sys
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
N, K = 512, 65536


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


arith = load('audit552_integer_intervals', BASE/'fixed-trial-residual-audit-552.py')
Q, SCALE = arith.Q, arith.SCALE
checks, failures = [], []


def check(ok, label):
    checks.append(dict(label=label, passed=bool(ok)))
    if not ok:
        failures.append(label)


def enclosed(q, saved, label):
    check(Fr(saved['lo']) <= Fr(q.lo, SCALE) <= Fr(q.hi, SCALE)
          <= Fr(saved['hi']), label)


def upper(q, saved, label):
    check(0 <= q.lo <= q.hi and Fr(q.hi, SCALE) <= Fr(saved['hi']), label)


def sq(q):
    if q.lo <= 0 <= q.hi:
        return Q.ends(0, -(-max(q.lo*q.lo, q.hi*q.hi)//SCALE))
    return q*q


def norm(v):
    return sum((sq(x) for x in v), Q()).sqrt()


def ln(q):
    # Correctly rounded Decimal logarithms, widened at 130 digits before
    # conversion to the independent 110-place integer grid.
    assert q.lo > 0
    with localcontext() as ctx:
        ctx.prec = 130
        a = ctx.next_minus((Decimal(q.lo)/Decimal(SCALE)).ln())
        b = ctx.next_plus((Decimal(q.hi)/Decimal(SCALE)).ln())
    return Q.ends(Q(Fr(a)).lo, Q(Fr(b)).hi)


def dyadics(a):
    ratios = [float(x).as_integer_ratio() for x in a.flat]
    den = max(d for _, d in ratios)
    assert all(den % d == 0 for _, d in ratios)
    return np.array([n*(den//d) for n, d in ratios], dtype=object).reshape(a.shape), den


def decimal(q, endpoint='hi'):
    with localcontext() as ctx:
        ctx.prec = 24
        ctx.rounding = ROUND_CEILING if endpoint == 'hi' else ROUND_FLOOR
        return str(Decimal(getattr(q, endpoint))/Decimal(SCALE))


def main():
    original = json.loads((BASE/'fixed-block-metric-555.json').read_text())
    names = ['fixed-block-metric-555.py', 'fixed-block-metric-555.json',
             'fixed-block-metric-555.npz', 'fixed-trial-residual-audit-552.py']
    names += list(original['input_hashes'])
    pins = {name: digest(BASE/name) for name in set(names)}
    check(not original['failures'] and all(x['passed'] for x in original['checks']),
          'all original checks and failures')
    check(original['source_script_sha256'] == pins['fixed-block-metric-555.py'], '555 script pin')
    check(original['binary_artifact']['sha256'] == pins['fixed-block-metric-555.npz'],
          '555 complete binary pin')
    for name, expected in original['input_hashes'].items():
        check(pins[name] == expected, 'source pin '+name)
    check(original['parameters'] == dict(N=N, K=K, complement_fraction='1/2',
                                       penalty=256, d0='6.14'), 'fixed allocation')

    source = (BASE/'fixed-block-metric-555.py').read_text()
    check(source.count('prec=70') == 3, 'replay precision substitution count')
    source = source.replace('prec=70', 'prec=90')
    for ext in ['npz', 'json']:
        key = 'fixed-block-metric-555.'+ext
        check(source.count(key) == 1, 'replay output substitution '+ext)
        source = source.replace(key, 'fixed-block-metric-replay-557.'+ext)
    replay_script = BASE/'fixed-block-metric-replay-557.py'
    replay_script.write_text(source)
    with (BASE/'fixed-block-metric-replay-557.log').open('w') as log:
        subprocess.run([sys.executable, str(replay_script)], stdout=log,
                       stderr=subprocess.STDOUT, check=True, env=os.environ.copy())
    replay = json.loads((BASE/'fixed-block-metric-replay-557.json').read_text())
    check(not replay['failures'] and all(x['passed'] for x in replay['checks']),
          'all 90-digit replay checks and failures')
    with np.load(BASE/'fixed-block-metric-555.npz') as data:
        arrays = {k: data[k] for k in data.files}
    with np.load(BASE/'fixed-block-metric-replay-557.npz') as data:
        check(set(data.files) == set(arrays), 'complete binary field coverage')
        for name, a in arrays.items():
            check(np.array_equal(a, data[name]), 'full binary replay '+name)
            check(np.isfinite(a).all(), 'finite binary values '+name)

    half = Q(Fr(1, 2))
    ell = sum((half**(2*j+1)/(2*j+1) for j in range(200)), Q())
    ell += Q.ends(0, (half**401/(401*(1-half*half))).hi)
    pi = 16*arith.atan(5)-4*arith.atan(239)
    enclosed(ell, original['constants']['ell'], 'independent atanh ell')
    enclosed(pi, original['constants']['pi'], 'independent Machin pi')
    direction = json.loads((BASE/'response-prefix-direction-546.json').read_text())
    check(direction['modes'] == N and direction['denominator'] == 2**40, 'direction parameters')
    k2 = [sq(n*pi/ell) for n in range(N)]

    def neutral(key):
        ints = direction[key]
        check(len(ints) == N-2 and all(type(x) is int for x in ints), key+' exact data')
        v = [Q(), Q()]+[Q(Fr(x, 2**40)) for x in ints]
        for n in range(2, N):
            p = n % 2
            ratio = (Q('.25')+k2[p])/(Q('.25')+k2[n])
            if p == 0:
                ratio *= Q(2).sqrt()
            v[p] -= ratio*v[n]
        return v

    f, g = [neutral(key) for key in ['f_free_numerators', 'g_free_numerators']]
    h = [(-1)**n*x for n, x in enumerate(f)]
    exact = dict(f=f, g=g, h=h)
    ones = {name: arith.l1(v) for name, v in exact.items()}
    norms = {name: norm(v) for name, v in exact.items()}
    conversion = {}
    for name, v in exact.items():
        check(len(original['coefficients'][name]) == N, name+' coefficient coverage')
        for n, x in enumerate(v):
            enclosed(x, original['coefficients'][name][n], name+' coefficient '+str(n))
        # These are the actual 70-digit midpoint-to-float conversions.
        with localcontext() as ctx:
            ctx.prec = 70
            fv = [float((Decimal(x['lo'])+Decimal(x['hi']))/2)
                  for x in original['coefficients'][name]]
        conversion[name] = arith.l1([x-Q(Fr(y)) for x, y in zip(v, fv)])
        check(conversion[name].hi < Q('1e-14').lo, name+' complete conversion allowance')
        upper(ones[name], original['coefficient_L1'][name], name+' coefficient L1 upper')
        enclosed(norms[name], original['coefficient_L2'][name], name+' coefficient norm')
    check(all(g[n].lo == g[n].hi == 0 for n in range(1, N, 2)), 'middle exactly even')

    e0 = Q('.000000181')+Q((K-N)*N).sqrt()*Q('1e-7')
    debt = (2*Q('.586')+e0)*e0+Q('1e-6')+sq(Q('.062501906'))
    upper(debt, original['reference']['total_covariance_error'], 'complete covariance debt')
    check(debt.hi < Q('.0046').lo, 'covariance operator allowance')
    check((Q('.000184')+N*Q('1e-7')).hi < Q('.00024').lo, 'head operator allowance')

    with np.load(BASE/'complete-covariance-532.npz') as data:
        m0, cov = data['m0'], data['cov00']
    check(np.array_equal(m0, m0.T) and np.array_equal(cov, cov.T), 'exact head symmetry')
    mn, md = dyadics(m0)
    cn, cd = dyadics(cov)
    common = max(md, cd)
    # H=m0-(100/307)cov-[6671/(307*12500)]I, exactly.
    hn = mn*(common//md)*307*12500-cn*(common//cd)*100*12500
    for i in range(N):
        hn[i, i] -= 6671*common
    hd = common*307*12500
    yn, yd = dyadics(arrays['solution'])
    hyn = hn@yn
    hyd = hd*yd
    hy = [Q(Fr(int(x), hyd)) for x in hyn]
    check(len(original['head']['exact_H_solution']) == N, 'all exact H action rows saved')
    for n, x in enumerate(hy):
        enclosed(x, original['head']['exact_H_solution'][n], 'exact rational H*y row '+str(n))
    rho = arrays['combined_residual']
    check(rho.shape == (K,), 'all residual outputs present')
    yi = [Q(Fr(float(x))) for x in arrays['solution']]
    bi = [Q(Fr(float(x))) for x in rho[:N]]
    sr = norm([x-y for x, y in zip(bi, hy)])
    upper(sr, original['head']['solve_residual'], 'exact rational solve residual')

    # Every factor product is an exact integer dot product. No Cholesky
    # success flag or floating product residual certifies positivity here.
    fn, fd = dyadics(arrays['factor'])
    ff = fn@fn.T
    rd = math.lcm(hd, 25, fd*fd)
    rn = hn*(rd//hd)-ff*(rd//(fd*fd))
    for i in range(N):
        rn[i, i] -= 6*(rd//25)
    reconstruction_squared = sum(int(x)*int(x) for x in rn.flat)
    reconstruction = Q(Fr(reconstruction_squared, rd*rd)).sqrt()
    check(reconstruction.hi < Q('1e-6').lo, 'exact full factor reconstruction <1e-6')
    check(reconstruction.hi < Q('1e-10').lo, 'exact reconstruction margin')
    factor_evidence = dict(denominator=str(rd), squared_numerator=str(reconstruction_squared),
        exact_frobenius=reconstruction.json(), H_denominator=str(hd),
        action_denominator=str(hyd), action_numerators=[str(int(x)) for x in hyn])

    delta_head = (Q('.00024')*norms['g']+Q(N).sqrt()*Q('2.1e-7')
                  *(ones['f']+ones['h'])+Q('1e-6'))
    delta_mid = (Q('.000000181')*norms['g']+Q(K-N).sqrt()
                 *(Q('1e-7')*ones['g']+Q('2.1e-7')*(ones['f']+ones['h']))+Q('1e-6'))
    upper(delta_head, original['head']['rho_L2_error'], 'head combined error')
    upper(delta_mid, original['middle']['rho_L2_error'], 'middle combined error')
    center = 2*sum((x*y for x, y in zip(yi, bi)), Q())-sum((x*y for x, y in zip(yi, hy)), Q())
    head = center+2*norm(yi)*delta_head+sq(sr+delta_head)/Q('.239999')
    upper(head, original['head']['upper'], 'complete head inverse upper')

    saved_lowers = original['middle']['diagonal_lower_endpoints']
    check(len(saved_lowers) == K-N, 'all positive denominators present')
    blocks = original['middle']['row_blocks']
    check([(x['first'], x['last']) for x in blocks] ==
          [(s, s+N-1) for s in range(N, K, N)], 'all output blocks exactly once')
    check(all(0 <= x['maximum_entry'] < 400 for x in blocks), 'every block magnitude ledger')
    weighted, lowers = Q(), []
    for n in range(N, K):
        d = ln(n/(2*ell))-2*ell*ell/(9*n*n)
        check(Fr(d.lo, SCALE) >= Fr(saved_lowers[n-N]) > Fr('6.14'),
              'independent diagonal lower '+str(n))
        weighted += 2*sq(Q(Fr(float(rho[n]))))/d
        lowers.append(str(Fr(d.lo, SCALE)))
    upper(weighted, original['middle']['complete_weighted_center'], 'complete weighted residual sum')
    middle = sq(weighted.sqrt()+(2/Q('6.14')).sqrt()*delta_mid)
    upper(middle, original['middle']['upper'], 'complete middle inverse upper')

    powers = []
    for p in range(2, 81):
        if any(p % j == 0 for j in range(2, math.isqrt(p)+1)):
            continue
        n = p
        while n < 81:
            if n > 27:
                powers.append((n, p))
            n *= p
    powers.sort()
    check(len(powers) == 16, 'complete separation-seven prime powers')
    a = sum((ln(Q(p))/Q(n).sqrt() for n, p in powers), Q())
    b = 4*ell*(1+Q('1.5')/Q(3).sqrt().sqrt())/(pi*pi)
    prime = 2*a/pi/Q(K-N).sqrt()*(ones['f']+ones['h'])
    response = (1+b/K)/Q(K-1).sqrt()*ones['g']
    kappa = 1/(Q(2187)*Q(3).sqrt()*Q('2.5')*(1-Q(1)/729))
    continuous = kappa*(norms['f']+norms['h'])
    tail_norm = prime+response+continuous
    dK = ln(K/(2*ell))-2*ell*ell/(9*K*K)
    tail = 2*sq(tail_norm)/dK
    for key, value in [('prime_weight_sum', a), ('response_b', b), ('prime_L2', prime),
                       ('response_L2', response), ('continuous_L2', continuous),
                       ('full_rho_L2', tail_norm), ('upper', tail)]:
        upper(value, original['tail'][key], 'full infinite tail '+key)
    enclosed(dK, original['tail']['diagonal_lower'], 'tail positive denominator')
    total = head+middle+tail
    check(Fr(total.hi, SCALE) <= Fr(original['summary']['reference_action_upper']),
          'original complete upper endpoint upheld')
    check(total.hi < Q('.023083550').lo < Q('.093538').lo, 'claimed and required thresholds')
    check((Q('.093538')-total).lo > Q('.070454450').hi, 'fixed minimized energy lower')
    for name, expected in pins.items():
        check(digest(BASE/name) == expected, 'original input preserved '+name)
    result = dict(scope=original['scope'], input_hashes=pins,
        coefficients={name: [x.json() for x in v] for name, v in exact.items()},
        coefficient_conversion={name: x.json() for name, x in conversion.items()},
        covariance_debt=debt.json(), exact_factor_and_action=factor_evidence,
        head=dict(solve_residual=sr.json(), center=center.json(), rho_error=delta_head.json(), upper=head.json()),
        middle=dict(first=N, last=K-1, lower_endpoints=lowers, weighted_center=weighted.json(),
                    rho_error=delta_mid.json(), upper=middle.json()),
        tail=dict(prime_powers=powers, prime=prime.json(), response=response.json(),
                  continuous=continuous.json(), full_norm=tail_norm.json(), diagonal=dK.json(), upper=tail.json()),
        summary=dict(reference_upper=total.json(), required='.093538', claimed='.023083550',
                     minimized_lower=(Q('.093538')-total).json(), passed=not failures),
        checks=checks, failures=failures,
        replay_paths=['fixed-block-metric-replay-557.py', 'fixed-block-metric-replay-557.json',
                      'fixed-block-metric-replay-557.npz', 'fixed-block-metric-replay-557.log'],
        qualifications=['Entry/response/IEEE754 and correctly rounded Decimal ln contracts retained.',
                        'Whole-core and unreplayed c_star qualifications retained.',
                        'Only fixed546 endpoints; no uniform triple, H2 or RH conclusion.'])
    out = BASE/'fixed-block-metric-audit-557.json'
    out.write_text(json.dumps(result, indent=2)+'\n')
    print('Head / middle / entire tail upper:', decimal(head), decimal(middle), decimal(tail))
    print('Complete correction upper:', decimal(total), '; claimed <.023083550; required <.093538')
    print('Exact full factor reconstruction:', decimal(reconstruction), '; required <1e-6')
    print('Checks:', len(checks), '; failures:', failures)
    print('Certificate:', out.relative_to(BASE.parent.parent))
    print('Preserved originals; full replay:', (BASE/'fixed-block-metric-replay-557.json').relative_to(BASE.parent.parent))
    assert not failures


if __name__ == '__main__':
    main()
