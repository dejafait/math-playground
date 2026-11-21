#!/usr/bin/env python3
"""C999p conceptual-audit arithmetic: fixed data, full rows, exact H action.

The replay has distinct filenames. Independent 110-place integer intervals
and exact dyadic/rational products verify the complete load-bearing data.
The analytic/IEEE754/Decimal and inherited form contracts remain inputs.
"""
import hashlib
import importlib.util
import json
import math
import os
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
N, J, K = 512, 1024, 65536


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


helper = load('audit557_helpers', BASE/'fixed-block-metric-audit-557.py')
Q, SCALE = helper.Q, helper.SCALE
sq, norm, ln, dyadics = helper.sq, helper.norm, helper.ln, helper.dyadics
checks, failures = [], []


def check(ok, label):
    checks.append(dict(label=label, passed=bool(ok)))
    if not ok:
        failures.append(label)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def enclosed(q, saved, label):
    check(F(saved['lo']) <= F(q.lo, SCALE) <= F(q.hi, SCALE) <= F(saved['hi']), label)


def upper(q, saved, label):
    check(0 <= q.lo <= q.hi and F(q.hi, SCALE) <= F(saved['hi']), label)


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), Q())


def l1(x):
    return helper.arith.l1(x)


def exact_mv(a, v):
    an, ad = dyadics(a)
    vn, vd = dyadics(v)
    nums = an@vn
    den = ad*vd
    return [F(int(x), den) for x in nums]


def main():
    original = json.loads((BASE/'frozen-full-residual-590.json').read_text())
    energy = json.loads((BASE/'original-minimum-audit-588.json').read_text())
    names = set(original['input_hashes']) | {
        'frozen-full-residual-590.py', 'frozen-full-residual-590.json',
        'frozen-full-residual-590.npz', 'fixed-block-metric-audit-557.py',
        'fixed-trial-residual-audit-552.py', 'original-minimum-audit-588.py'}
    pins = {name: digest(BASE/name) for name in names}
    check(not original['failures'] and all(x['passed'] for x in original['checks']),
          'every original check and failure')
    check(original['script_sha256'] == pins['frozen-full-residual-590.py'], 'original generator pin')
    check(original['binary_artifact']['sha256'] == pins['frozen-full-residual-590.npz'],
          'original full array pin')
    for name, expected in original['input_hashes'].items():
        check(pins[name] == expected, 'original input pin '+name)
    check(original['parameters'] == dict(head=N, trial_support=J, K=K,
                                        reference='unchanged C999k'), 'frozen parameters')
    check(not energy['failures'] and all(x['passed'] for x in energy['checks']),
          'complete original-energy audit passes')
    check(energy['script_sha256'] == pins['original-minimum-audit-588.py'], 'energy audit script pin')
    for name, expected in energy['evidence']['input_hashes'].items():
        check(digest(BASE/name) == expected, 'energy source pin '+name)
    check(F(energy['bounds']['trial_energy']['lo']) > F('.42328427'),
          'audited full signed-U energy exceeds unchanged threshold')

    source = (BASE/'frozen-full-residual-590.py').read_text()
    check(source.count('prec=70') == 3, 'replay precision substitution count')
    source = source.replace('prec=70', 'prec=90')
    for ext in ['npz', 'json']:
        before = 'frozen-full-residual-590.'+ext
        check(source.count(before) == 1, 'replay output substitution '+ext)
        source = source.replace(before, 'frozen-full-residual-replay-592.'+ext)
    replay_path = BASE/'frozen-full-residual-replay-592.py'
    replay_path.write_text(source)
    with (BASE/'frozen-full-residual-replay-592.log').open('w') as log:
        subprocess.run([sys.executable, str(replay_path)], stdout=log,
                       stderr=subprocess.STDOUT, check=True, env=os.environ.copy())
    replay = json.loads((BASE/'frozen-full-residual-replay-592.json').read_text())
    check(not replay['failures'] and all(x['passed'] for x in replay['checks']),
          'all 90-digit replay checks')
    with np.load(BASE/'frozen-full-residual-590.npz') as data:
        arrays = {key: data[key].copy() for key in data.files}
    with np.load(BASE/'frozen-full-residual-replay-592.npz') as data:
        check(set(arrays) == set(data.files), 'all replay arrays covered')
        for key, values in arrays.items():
            check(np.isfinite(values).all() and np.array_equal(values, data[key]),
                  'full bitwise replay '+key)
    with np.load(BASE/'original-galerkin-586.npz') as data:
        trial = {key: data[key].copy() for key in data.files}
    with np.load(BASE/'endpoint-complement-locator-581.npz') as data:
        check(np.array_equal(trial['free_numerators'], data['free_numerators']),
              'every endpoint integer unchanged')
    check(np.array_equal(arrays['middle_free_dyadic'], trial['middle_free_dyadic']),
          'every middle dyadic unchanged')

    half = Q(F(1, 2))
    ell = sum((half**(2*j+1)/(2*j+1) for j in range(200)), Q())
    ell += Q.ends(0, (half**401/(401*(1-half*half))).hi)
    pi = 16*helper.arith.atan(5)-4*helper.arith.atan(239)
    enclosed(ell, original['constants']['ell'], 'independent atanh ell')
    enclosed(pi, original['constants']['pi'], 'independent Machin pi')
    k2 = [sq(n*pi/ell) for n in range(J)]

    def complete(free):
        v = [Q(), Q()]+[Q(x) for x in free]
        for n in range(2, J):
            ratio = (Q('.25')+k2[n % 2])/(Q('.25')+k2[n])
            if n % 2 == 0:
                ratio *= Q(2).sqrt()
            v[n % 2] -= ratio*v[n]
        return v

    integers = trial['free_numerators']
    check(integers.shape == (2*N,), 'endpoint integer shape')
    free_f = [F(0)]*(N-2)+[F(int(x), 2**40) for x in integers[:N]]
    free_h = [F(0)]*(N-2)+[F(int(x), 2**40) for x in integers[N:]]
    exact = dict(f=complete(free_f), h=complete(free_h),
                 g=complete([F(float(x)) for x in trial['middle_free_dyadic']]))
    centers = dict(f=trial['endpoint_f_center'], h=trial['endpoint_h_center'],
                   g=trial['middle_raw_center'])
    ones, norms, conversion = {}, {}, {}
    for name, values in exact.items():
        check(len(original['coefficients'][name]) == J, name+' all coefficients saved')
        for n, x in enumerate(values):
            enclosed(x, original['coefficients'][name][n], name+' exact coefficient '+str(n))
        ones[name], norms[name] = l1(values), norm(values)
        conversion[name] = l1([x-Q(F(float(y))) for x, y in zip(values, centers[name])])
        upper(ones[name], original['coefficient_L1'][name], name+' L1 upper')
        enclosed(norms[name], original['coefficient_L2'][name], name+' L2 enclosure')
        upper(conversion[name], original['coefficient_conversion'][name], name+' conversion upper')
        check(conversion[name].hi < Q('1e-14').lo, name+' conversion allowance')

    ratio = Q(J*J+(J-1)**2)/(J*J-(J-1)**2)
    rmax = Q(2).sqrt()/(6*Q('64.25')**2)
    offdiag = 2*rmax/pi
    c = Q('131072.5')
    diag = 1/c**2+2*k2[-1]*(1/(6*c**3)+1/c**4)
    local = rmax+offdiag+8*diag+Q('1e-7')
    ledger = dict(cancellation_ratio_upper=ratio, rmax=rmax,
                  offdiagonal_analytic_error=offdiag, diagonal_error=diag, local_derived=local)
    for key, value in ledger.items():
        enclosed(value, original['entry_ledger'][key], 'independent entry ledger '+key)
    check(ratio.hi < Q(1024).lo and local.hi < Q('.0001').lo, 'rectangular numerical caps')
    check((Q(K-1)*pi/ell*Q('.549307')).hi < Q(207000).lo, 'largest shift argument cap')
    u = Q(F(1, 2**53))
    gamma = 2048*u/(1-2048*u)
    check(gamma.hi < Q('2.3e-13').lo, '1024-input dot gamma cap')
    arith_row = Q('2.3e-13')*2400+400*sum(conversion.values(), Q())+Q('1e-11')
    check((256*arith_row).hi < Q('1e-6').lo, 'full finite arithmetic norm allowance')
    delta_p = Q(N).sqrt()*(Q('.0001')*ones['g']+Q('.000001')*(ones['f']+ones['h']))+Q('1e-6')
    delta_q = Q(K-N).sqrt()*(Q('.0001')*ones['g']+Q('.000001')*(ones['f']+ones['h']))+Q('1e-6')
    upper(delta_p, original['head']['rho_L2_error'], 'complete head error')
    upper(delta_q, original['middle']['rho_L2_error'], 'complete complementary error')

    rho = arrays['combined_residual']
    check(rho.shape == (K,), 'every finite residual row present')
    # M is the audited physical D+S matrix, not the reference diagonal.
    local_parts = [exact_mv(trial[key], centers[name]) for key, name in
                   [('t_entries', 'f'), ('ts_entries', 'h'), ('local_matrix', 'g')]]
    local_rational = [a+b-c for a, b, c in zip(*local_parts)]
    local_arithmetic = norm([Q(x-F(float(y))) for x, y in zip(local_rational, rho[:J])])
    check(local_arithmetic.hi < (Q(J).sqrt()*arith_row).hi,
          'all1024 exact local rows including Dg512:1023 obey arithmetic bound')

    with np.load(BASE/'complete-covariance-532.npz') as data:
        m0, cov = data['m0'], data['cov00']
    check(np.array_equal(m0, m0.T) and np.array_equal(cov, cov.T), 'reference dyadic symmetry')
    mn, md = dyadics(m0)
    cn, cd = dyadics(cov)
    common = max(md, cd)
    hn = mn*(common//md)*307*12500-cn*(common//cd)*100*12500
    for i in range(N):
        hn[i, i] -= 6671*common
    hd = common*307*12500
    yn, yd = dyadics(arrays['solution'])
    hyn, hyd = hn@yn, hd*yd
    hy = [Q(F(int(x), hyd)) for x in hyn]
    check(len(original['head']['exact_H_solution']) == N, 'complete saved H action')
    for n, x in enumerate(hy):
        enclosed(x, original['head']['exact_H_solution'][n], 'exact rational H action '+str(n))
    yi = [Q(F(float(x))) for x in arrays['solution']]
    bi = [Q(F(float(x))) for x in rho[:N]]
    sr, ynorm = norm([a-b for a, b in zip(bi, hy)]), norm(yi)
    upper(sr, original['head']['solve_residual'], 'exact solve residual')
    enclosed(ynorm, original['head']['solution_L2'], 'proposed solution norm')
    fn, fd = dyadics(arrays['factor'])
    ff = fn@fn.T
    rd = math.lcm(hd, 25, fd*fd)
    rn = hn*(rd//hd)-ff*(rd//(fd*fd))
    for i in range(N):
        rn[i, i] -= 6*(rd//25)
    rsq = sum(int(x)*int(x) for x in rn.flat)
    reconstruction = Q(F(rsq, rd*rd)).sqrt()
    check(reconstruction.hi < Q('1e-6').lo, 'exact full H-.24I-FFt verifies .239999 floor')
    center = 2*dot(yi, bi)-dot(yi, hy)
    enclosed(center, original['head']['center_energy'], 'head square-completion center')
    head = center+2*ynorm*delta_p+sq(sr+delta_p)/Q('.239999')
    upper(head, original['head']['upper'], 'full head inverse bound')

    blocks = original['middle']['row_blocks']
    check([(b['first'], b['last']) for b in blocks] ==
          [(s, s+N-1) for s in range(J, K, N)], 'every newly generated rectangular output once')
    check(all(0 <= b['maximum_entry'] < 400 for b in blocks), 'all rectangular entry magnitudes')
    saved_d = original['middle']['diagonal_lower_endpoints']
    check(len(saved_d) == K-N, 'every complementary denominator saved')
    weighted, lowers = Q(), []
    for n in range(N, K):
        dn = ln(n/(2*ell))-2*ell*ell/(9*n*n)
        check(F(dn.lo, SCALE) >= F(saved_d[n-N]) > F('6.14'), 'complete positive weight '+str(n))
        weighted += 2*sq(Q(F(float(rho[n]))))/dn
        lowers.append(str(F(dn.lo, SCALE)))
    upper(weighted, original['middle']['complete_weighted_center'], 'all weighted center rows')
    middle = sq(weighted.sqrt()+(2/Q('6.14')).sqrt()*delta_q)
    upper(middle, original['middle']['upper'], 'full complementary inverse bound')

    powers = []
    for p in range(2, 82):
        if any(p % d == 0 for d in range(2, math.isqrt(p)+1)):
            continue
        power = p
        while power < 81:
            if power > 27:
                powers.append((power, p))
            power *= p
    powers.sort()
    entries = load('entry_constants592', BASE/'residual-certificate-532.py')
    check(powers == entries.POWERS and len(powers) == 16, 'all nearest prime powers independently enumerated')
    a = sum((ln(Q(p))/Q(n).sqrt() for n, p in powers), Q())
    b = 4*ell*(1+Q('1.5')/Q(3).sqrt().sqrt())/(pi*pi)
    prime = 2*a/pi/Q(K-J).sqrt()*(ones['f']+ones['h'])
    response = (1+b/K)/Q(K-1).sqrt()*ones['g']
    kappa = 1/(2187*Q(3).sqrt()*Q('2.5')*(1-Q(1)/729))
    continuous = kappa*(norms['f']+norms['h'])
    full_tail = prime+response+continuous
    dk = ln(K/(2*ell))-2*ell*ell/(9*K*K)
    tail = 2*sq(full_tail)/dk
    tail_values = dict(weight_sum=a, response_b=b, prime_L2=prime, response_L2=response,
                       continuous_L2=continuous, full_rho_L2=full_tail, diagonal_lower=dk, upper=tail)
    for key, value in tail_values.items():
        enclosed(value, original['tail'][key], 'entire tail expression '+key)
    total = head+middle+tail
    check(F(total.hi, SCALE) <= F(original['summary']['reference_action_upper']),
          'independent total no larger than original full endpoint')
    check(total.hi < Q('.000760912').lo < Q('.42328427').lo, 'stated debt and energy thresholds')
    margin = Q('.42328427')-total
    check(margin.lo > Q('.42252335').hi, 'stated unrestricted-middle margin')
    check(all(digest(BASE/name) == expected for name, expected in pins.items()),
          'all preexisting pinned artifacts preserved')
    summary = dict(head_upper=helper.decimal(head), middle_upper=helper.decimal(middle),
        infinite_tail_upper=helper.decimal(tail), reference_action_upper=helper.decimal(total),
        required_strict_upper='.42328427', stated_debt_upper='.000760912',
        minimized_energy_lower=helper.decimal(margin, 'lo'),
        exact_reconstruction_upper=helper.decimal(reconstruction),
        solve_residual_upper=helper.decimal(sr), local_arithmetic_upper=helper.decimal(local_arithmetic),
        passed=not failures)
    result = dict(target="Critically audit C999p's full frozen-trial residual debt enclosure and unrestricted neutral-middle lower comparison, including the new1024-column ledger and complete unchanged-reference inverse action.",
        summary=summary, checks=checks, failures=failures, input_hashes=pins,
        script_sha256=digest(Path(__file__)), constants=dict(ell=ell.json(), pi=pi.json()),
        coefficients={name: [x.json() for x in values] for name, values in exact.items()},
        entry_ledger={key: value.json() for key, value in ledger.items()},
        local_rational_residual=[str(x) for x in local_rational],
        local_arithmetic_error=local_arithmetic.json(),
        exact_head=dict(H_denominator=str(hd), action_denominator=str(hyd),
            action_numerators=[str(int(x)) for x in hyn], action=[x.json() for x in hy],
            reconstruction_denominator=str(rd), reconstruction_squared_numerator=str(rsq),
            reconstruction_norm=reconstruction.json(), solve_residual=sr.json(),
            center_energy=center.json(), upper=head.json()),
        middle=dict(diagonal_lowers=lowers, weighted_center=weighted.json(), upper=middle.json()),
        tail={key: value.json() for key, value in tail_values.items()},
        total=total.json(), margin=margin.json(),
        qualification='REPRODUCTION under inherited analytic/IEEE754/Decimal, whole-core and unreplayed c_* contracts; one endpoint pair only.')
    out = BASE/'frozen-full-residual-audit-592.json'
    out.write_text(json.dumps(result, indent=2)+'\n')
    print('Complete residual audit:', json.dumps(summary))
    print('Checks:', len(checks), '; failures:', failures)
    print('Certificate:', out.relative_to(BASE.parent.parent))
    print('Full finite replay: scripts/separation-seven/frozen-full-residual-replay-592.json/.npz')
    assert not failures


if __name__ == '__main__':
    main()
