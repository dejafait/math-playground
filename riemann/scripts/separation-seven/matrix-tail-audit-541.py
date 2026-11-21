#!/usr/bin/env python3
"""Independent checks of the frozen C744y evidence; never replace originals.

The analytic argument and error bounds are in C744y Section 5. This
program checks every scalar interval and every matrix/factor entry,
under the inherited Decimal/IEEE754 contract, without new Cholesky.
"""
import ctypes
import hashlib
import importlib.util
import json
import math
import platform
import sys
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from fractions import Fraction
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
N, K = 512, 65536


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def main():
    original = json.loads((BASE/'matrix-tail-certificate-539.json').read_text())
    inherited = json.loads((BASE/'certificate-audit-534.json').read_text())
    failures, hashes, intervals = [], [], []

    def check(condition, label):
        if not condition:
            failures.append(label)

    def hash_check(name, expected):
        actual = digest(BASE/name)
        hashes.append(dict(path=name, actual=actual, expected=expected,
                           passed=actual == expected))
        check(actual == expected, 'hash: '+name)

    hash_check('certificate-audit-534.json', original['audit_sha256'])
    for record in original['input_checks']:
        check(record['sha256'] == record['expected'] ==
              inherited['original_sha256'][record['path']], 'inherited hash agreement')
        hash_check(record['path'], record['expected'])
    for record in original['artifacts']:
        hash_check(record['path'], record['sha256'])
    # Protect the audited generator and its elementary interval implementation.
    for name in ['complete-schur-531.py', 'residual-certificate-532.py']:
        hash_check(name, inherited['original_sha256'][name])
    check(not original['failures'] and not inherited['failures'], 'prior failures')
    check(original['parameters'] == dict(N=N, K=K, penalty=256, tau='143/100',
          separation=7, proposed_paid_floor='1/25'), 'frozen parameters')
    check(original['inherited_error_ledger'] == inherited['error_ledger'], 'ledger identity')

    # Use the already audited interval operations at 90 rather than 60 digits.
    # Rebuild all quantities below independently of the original539 function.
    spec = importlib.util.spec_from_file_location('interval531audit541', BASE/'complete-schur-531.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.DOWN = Context(prec=90, rounding=ROUND_FLOOR)
    mod.UP = Context(prec=90, rounding=ROUND_CEILING)
    mod.NEAR = Context(prec=90, rounding=ROUND_HALF_EVEN)
    I = mod.I
    scalar = original['scalar_certificate']

    def enclosed(label, value, stored):
        passed = Decimal(stored['lo']) <= value.lo <= value.hi <= Decimal(stored['hi'])
        intervals.append(dict(label=label, audit_interval=value.json(),
                              stored_interval=stored, contained=passed))
        check(passed, 'interval containment: '+label)

    ell = I(3).ln()/2
    enclosed('ell', ell, scalar['ell'])
    # Trial division directly finds every prime power in the exact open interval.
    powers = []
    for number in range(28, 81):
        factors, remaining = [], number
        for p in range(2, number+1):
            if remaining % p == 0:
                factors.append(p)
                while remaining % p == 0:
                    remaining //= p
        if len(factors) == 1:
            powers.append((number, factors[0]))
    check([(r['n'], r['prime']) for r in scalar['powers']] == powers, 'prime power list')
    ratios, weights = {}, {}
    for record in scalar['powers']:
        number, prime = record['n'], record['prime']
        weights[number] = I(prime).ln()/I(number).sqrt()
        ratios[number] = 7-I(number).ln()/ell
        enclosed(f'weight/{number}', weights[number], record['weight'])
        enclosed(f'ratio/{number}', ratios[number], record['delay_ratio'])
        check(-1 < ratios[number].lo <= ratios[number].hi < 1, 'delay support')
    plus = {n for n in ratios if ratios[n].lo > 0}
    minus = {n for n in ratios if ratios[n].hi < 0}
    check(len(plus) == 6 and len(minus) == 10 and plus | minus == set(ratios), 'sign groups')
    expected = {(a,b,op) for group in [plus,minus] for a in group for b in group
                for op in ['sum','difference'] if a != b or op == 'sum'}
    seen, chords = set(), []
    for record in scalar['chord_checks']:
        a,b,op = record['n_i'],record['n_j'],record['operation']
        key = a,b,op
        check(key in expected and key not in seen, 'chord key completeness')
        seen.add(key)
        r = ratios[a]+ratios[b] if op == 'sum' else ratios[a]-ratios[b]
        candidates = []
        for center in [-2,0,2]:
            difference = r-center
            check(difference.lo > 0 or difference.hi < 0, 'nonzero chord distance')
            candidates.append(difference if difference.lo > 0 else -difference)
        distance = I(min(t.lo for t in candidates), min(t.hi for t in candidates))
        chord = 2*distance
        for label,value,stored in [('ratio',r,record['ratio']),
                                   ('distance',distance,record['distance_to_even_integer']),
                                   ('chord',chord,record['chord_lower'])]:
            enclosed(f'{a}/{b}/{op}/{label}',value,stored)
        check(chord.lo > Decimal('.01'), 'chord threshold')
        chords.append(chord)
    check(seen == expected and len(seen) == 256, 'all 256 chords present')
    check(sum(op == 'sum' for a,b,op in seen) == 136, '136 sums')
    check(sum(op == 'difference' for a,b,op in seen) == 120, '120 differences')

    a = sum(weights.values(), I(0))
    a2 = sum((w*w for w in weights.values()), I(0))
    pi0 = I('3.14')
    e0 = 3/(2*I(3).sqrt().sqrt())
    b0 = 4*ell*(2+e0)/(pi0*pi0)
    response = (sum(((I(m)+I('.7'))*(I(m)+I('.7')) for m in range(N)), I(0))
                /(3*(K-1)**3)).sqrt()
    prime = 2*a/pi0/(1-I(511)/K)*(I(sum(m*m for m in range(N)))/(3*(K-1)**3)).sqrt()
    continuous = 1/(I(2187)*I(3).sqrt()*I('2.5')*(1-I(1)/729))
    beta = (2/ell).sqrt()*(I(3).sqrt().sqrt()+1)*ell*ell/(2*pi0*pi0)
    moment = 256*(I(3).sqrt()-1/I(3).sqrt()).sqrt()*beta*(I(2)/(3*(K-1)**3)).sqrt()
    remainder = response+prime+continuous+moment
    leading = 2*I(1)/(K-1)+16/(pi0*pi0)*(a2/(2*(K-1))+200*a*a/(K*K))
    for label,value in [('prime_weight_sum',a),('prime_weight_square_sum',a2),
                        ('response_constant',b0),('response_remainder',response),
                        ('prime_remainder',prime),('entire_continuous',continuous),
                        ('entire_moment',moment),('full_operator_remainder',remainder),
                        ('leading_hilbert_schmidt_squared',leading)]:
        enclosed(label,value,scalar[label])
    check(b0.hi < Decimal('.7'), 'response constant <.7')
    check(leading.hi < Decimal('.0001'), 'leading squared threshold')
    check(remainder.hi < Decimal('.002'), 'remainder threshold')

    # A conservative finite debt uses only rounded UP bounds from the audited
    # input; it does not rely on the last digits of an old floating ledger.
    ef = I('.000000181')+3*(I((K-N)*N)).sqrt()/10000000
    em = I('.000184')+I(3*N)/10000000
    finite_debt = em+((2*I('3.162')+ef)*ef+I('.000001'))/I('1.43')
    check(finite_debt.hi < Decimal('.008'), 'coarse finite debt <.008<.012')

    matrix_checks = []
    with np.load(BASE/'complete-covariance-532.npz') as archive:
        data = {key: archive[key] for key in archive.files}
    check(set(data) == {'m0','mc','mg','cov00','covcc','covgg','cov0c','cov0g','covcg'}, 'nine input keys')
    with np.load(BASE/'audit-replay-534/complete-covariance-532.npz') as replay:
        check(set(replay.files) == set(data), 'prior replay keys')
        for key,x in data.items():
            passed = x.shape == (N,N) and bool(np.all(np.isfinite(x))) and np.array_equal(x,replay[key])
            matrix_checks.append(dict(key=key, entries=int(x.size), full_input_replay_match=bool(passed)))
            check(passed,'complete input matrix '+key)
    # Assemble by separate block assignments; no saved mixed matrix is a premise.
    head, covariance = np.zeros((2*N,2*N)), np.zeros((2*N,2*N))
    head[:N,:N] = head[N:,N:] = data['m0']
    head[:N,N:] = data['mg']-data['mc']
    head[N:,:N] = -data['mc']-data['mg']
    for block in [covariance[:N,:N],covariance[N:,N:]]:
        block[:] = data['cov00']+data['covcc']+data['covgg']
    mixed = data['covcg']+data['covcg'].T
    covariance[:N,:N] += mixed
    covariance[N:,N:] -= mixed
    covariance[:N,N:] = -data['cov0c']-data['cov0c'].T+data['cov0g']-data['cov0g'].T
    covariance[N:,:N] = covariance[:N,N:].T
    residual = head-covariance/1.43
    residual = (residual+residual.T)/2
    z = np.zeros((4,2*N))
    for c in range(2):
        for m in range(N):
            z[2*c+m%2,c*N+m] = 1/np.sqrt(2.) if m == 0 else 1.
    u = (z.T@z)/5000+np.eye(2*N)/125000
    paid = residual-u/1.43
    rebuilt = dict(head=head,covariance=covariance,finite_residual=residual,z=z,u=u,paid=paid)
    with np.load(BASE/'matrix-tail-matrices-539.npz') as saved:
        check(set(saved.files) == set(rebuilt), 'six complete saved matrices')
        for key,x in rebuilt.items():
            old = saved[key]
            delta = x-old
            difference = math.sqrt(float(np.sum(delta*delta)))
            passed = old.shape == x.shape and bool(np.all(np.isfinite(old))) and difference < 1e-12
            matrix_checks.append(dict(key=key, entries=int(x.size),
                                      complete_difference_frobenius=difference,
                                      required_difference=1e-12, passed=bool(passed)))
            check(passed,'saved539 matrix '+key)
    q = Fraction.from_float(float(z[0,0]))
    zero_weight_square_error = abs(q*q-Fraction(1,2))
    check(q > Fraction(1,2) and zero_weight_square_error < Fraction(1,10**14), 'zero-mode exact dyadic enclosure')

    with np.load(BASE/'matrix-tail-factor-539.npz') as saved:
        factor = saved['factor']
    check(factor.shape == (2*N,2*N) and bool(np.all(np.isfinite(factor))), 'full stored factor')
    difference = paid-.04*np.eye(2*N)-factor@factor.T
    reconstruction = math.sqrt(float(np.sum(difference*difference)))
    normsq = float(np.sum(factor*factor))
    check(reconstruction < 1e-7 and normsq < 20000, 'reconstruction thresholds')
    check(float(np.max(np.abs(factor))) < 20 and float(np.max(np.abs(paid))) < 400, 'arithmetic magnitude thresholds')
    check(np.array_equal(paid,paid.T), 'Hermitian paid center')
    check(np.all(np.isfinite(paid)),'finite paid center')
    unit = Fraction(1,2**53)
    gamma = lambda n: n*unit/(1-n*unit)
    product_bound = gamma(2048)*20000
    # Factor/real-square norm sums are positive; use the sequential (worst case)
    # operation count, even if the runtime sums in a binary tree.
    norm_gamma = gamma(2*(2*N)**2+10)
    check(product_bound < Fraction(5,10**9), 'exact rational LL* error')
    check(norm_gamma < Fraction(1,10**9), 'real-square norm error multiplier')
    # Includes rational encodings and subtractions with ample independent slack.
    basic_arithmetic_bound = 100*unit*409600
    check(basic_arithmetic_bound < Fraction(5,10**9),'assembly basic-operation bound')
    total_reconstruction_upper = I(Decimal(reconstruction))/(1-I(norm_gamma.numerator)/norm_gamma.denominator)
    total_reconstruction_upper += I(product_bound.numerator)/product_bound.denominator+I('.00000001')
    check(total_reconstruction_upper.hi < Decimal('.000001'), 'full reconstruction debt')
    rounding = ctypes.CDLL(None).fegetround()
    check(rounding == 0 and sys.float_info.mant_dig == 53, 'binary64 nearest runtime')
    lower = Fraction(1,25)-Fraction(12,1000)-Fraction(2,1000000)
    check(lower == Fraction(13999,500000) and lower > 0,'rational final floor')

    output = dict(
        scope='Frozen C744y independent conceptual audit evidence; no new factor or parameter search',
        input_hashes=hashes, scalar_interval_checks=intervals,
        scalar_summary=dict(checked_interval_count=len(intervals),chord_count=len(seen),
                            minimum_chord_lower=str(min(c.lo for c in chords)),
                            leading_squared=leading.json(),required_leading_squared='.0001',
                            remainder=remainder.json(),required_remainder='.002',
                            coarse_finite_debt=finite_debt.json(),required_finite_debt='.012'),
        matrix_checks=matrix_checks,
        reconstruction=dict(entries=(2*N)**2,frobenius_residual=reconstruction,
                            required_residual=1e-7,factor_norm_squared=normsq,
                            required_factor_norm_squared=20000,
                            maximum_factor_entry=float(np.max(np.abs(factor))),
                            maximum_matrix_entry=float(np.max(np.abs(paid))),
                            zero_weight_squared_error=str(zero_weight_square_error),
                            exact_product_error_bound=str(product_bound),
                            exact_norm_gamma=str(norm_gamma),
                            exact_basic_arithmetic_bound=str(basic_arithmetic_bound),
                            total_reconstruction_upper=total_reconstruction_upper.json(),
                            required_reconstruction_debt='.000001',assembly_debt='.000001'),
        complete_lower_bound='0.027998' if not failures else None,
        required_complete_lower_bound='0',failures=failures,
        runtime=dict(python=sys.version,numpy=np.__version__,machine=platform.machine(),
                     fegetround=rounding,decimal_digits=90,
                     blas=np.__config__.CONFIG.get('Build Dependencies',{}).get('blas',{})),
        qualification='Analytic and arithmetic proof in C744y Section 5; explicit execution contracts remain hypotheses, not formal runtime verification. Composition and RH remain open.',
        original_certificate_sha256=digest(BASE/'matrix-tail-certificate-539.json'))
    path = BASE/'matrix-tail-audit-541.json'
    path.write_text(json.dumps(output,indent=2)+'\n')
    print('All scalar enclosures:',len(intervals),'chords:',len(seen),
          'minimum:',output['scalar_summary']['minimum_chord_lower'],'required >.01')
    print('Leading squared:',leading.hi,'required <.0001; remainder:',remainder.hi,'required <.002')
    print('Finite debt upper:',finite_debt.hi,'required <.012; reconstruction:',reconstruction,'required <1e-7')
    print('Complete entries reconstructed:',(2*N)**2,'paid lower:',output['complete_lower_bound'],'required >0; failures:',failures)
    print('Audit certificate:',path)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
