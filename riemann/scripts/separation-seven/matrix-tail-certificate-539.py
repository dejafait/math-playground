#!/usr/bin/env python3
"""Frozen full mixed Schur certificate with a directional infinite tail.

Analytic proof and arithmetic qualifications are canonical in C744y.
No eigenvalue or library transcendental accuracy is presumed. Cholesky
only proposes a factor, checked against every reconstructed entry.
"""
import ctypes
import hashlib
import importlib.util
import json
import math
import platform
import sys
from decimal import Decimal
from pathlib import Path

import numpy as np

FOLDER = Path(__file__).resolve().parent
N, K = 512, 65536
TAU, PAID_FLOOR = 1.43, .04


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def scalar_certificate():
    spec = importlib.util.spec_from_file_location('scalar531', FOLDER/'complete-schur-531.py')
    scalar = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(scalar)
    I = scalar.I
    ell = I(3).ln()/2
    powers = scalar.prime_powers()
    weights = [I(p).ln()/I(n).sqrt() for n, p in powers]
    ratios = [(7*ell-I(n).ln())/ell for n, p in powers]
    groups = [[i for i, r in enumerate(ratios) if r.lo > 0],
              [i for i, r in enumerate(ratios) if r.hi < 0]]
    assert sum(map(len, groups)) == 16
    assert all(r.lo > -1 and r.hi < 1 for r in ratios)
    chord_checks = []
    for group in groups:
        for i in group:
            for j in group:
                for operation in ['sum', 'difference']:
                    if i == j and operation == 'difference':
                        continue
                    angle_ratio = ratios[i]+ratios[j] if operation == 'sum' else ratios[i]-ratios[j]
                    distances = []
                    for center in [-2, 0, 2]:
                        d = angle_ratio-center
                        if d.lo > 0:
                            distances.append(d)
                        elif d.hi < 0:
                            distances.append(-d)
                        else:
                            raise ValueError('unresolved resonance')
                    lower = min(d.lo for d in distances)
                    upper = min(d.hi for d in distances)
                    distance = I(lower, upper)
                    # |1-exp(i*pi*r)| >= 2 dist(r,2Z).
                    chord_lower = 2*distance
                    assert chord_lower.lo > Decimal('.01')
                    chord_checks.append(dict(n_i=powers[i][0], n_j=powers[j][0],
                                             operation=operation, ratio=angle_ratio.json(),
                                             distance_to_even_integer=distance.json(),
                                             chord_lower=chord_lower.json()))
    assert len(chord_checks) == 256
    a = sum(weights, I(0))
    squares = sum((w*w for w in weights), I(0))
    pi_lower = I('3.14')
    leading_hs_squared = 2*I(1)/(K-1)+(16/(pi_lower*pi_lower))*(
        squares/(2*(K-1))+200*a*a/(K*K))
    assert leading_hs_squared.hi < Decimal('.0001')
    exponential_sum = I('1.5')/I(3).sqrt().sqrt()
    response_constant = 4*ell/(pi_lower*pi_lower)*(2+exponential_sum)
    assert response_constant.hi < Decimal('.7')
    moment2 = sum(m*m for m in range(N))
    response2 = sum(((I(m)+I('.7'))*(I(m)+I('.7')) for m in range(N)), I(0))
    response_error = (response2/(3*(K-1)**3)).sqrt()
    prime_error = (2*a/pi_lower)/(1-I(N-1)/K)*(I(moment2)/(3*(K-1)**3)).sqrt()
    # Complete continuous and moment bounds, imported from audited C744w.
    continuous = I(1)/(I(2187)*I(3).sqrt()*I('2.5')*(1-I(1)/729))
    beta = (2/ell).sqrt()*(I(3).sqrt().sqrt()+1)*ell*ell/(2*pi_lower*pi_lower)
    moment = 256*(I(3).sqrt()-1/I(3).sqrt()).sqrt()*beta*(I(2)/(3*(K-1)**3)).sqrt()
    total_error = response_error+prime_error+continuous+moment
    assert response_error.hi < Decimal('.000231')
    assert prime_error.hi < Decimal('.001130')
    assert continuous.hi < Decimal('.000106')
    assert moment.hi < Decimal('.000001')
    assert total_error.hi < Decimal('.002')
    return dict(ell=ell.json(), powers=[dict(n=n, prime=p, weight=w.json(),
                                           delay_ratio=r.json())
                                      for (n,p),w,r in zip(powers,weights,ratios)],
                chord_checks=chord_checks,
                minimum_chord_lower=str(min(Decimal(r['chord_lower']['lo']) for r in chord_checks)),
                chord_required='.01', prime_weight_sum=a.json(),
                prime_weight_square_sum=squares.json(),
                leading_hilbert_schmidt_squared=leading_hs_squared.json(),
                required_leading_squared='.0001',
                response_constant=response_constant.json(),
                response_remainder=response_error.json(), prime_remainder=prime_error.json(),
                entire_continuous=continuous.json(), entire_moment=moment.json(),
                full_operator_remainder=total_error.json(), required_remainder='.002',
                matrix_U='(1/5000) Z*Z + (1/125000) I',
                covariance_upper_bound_proved_by='C744y exact formulas, integral comparison, Abel summation and combined-operator inequality')


def main():
    failures = []
    scalars = scalar_certificate()
    audit_path = FOLDER/'certificate-audit-534.json'
    audit = json.loads(audit_path.read_text())
    checks = []
    for name in ['complete-covariance-532.npz', 'complete-residual-certificate-532.json']:
        actual = digest(FOLDER/name)
        expected = audit['original_sha256'][name]
        checks.append(dict(path=name, sha256=actual, expected=expected, passed=actual == expected))
        if actual != expected:
            failures.append('input hash mismatch: '+name)
    if audit['failures'] or len(audit['covariance_checks']) != 9 or not all(
            r['finite'] and r['exact_match'] for r in audit['covariance_checks']):
        failures.append('inherited audit failed')
    if ctypes.CDLL(None).fegetround() != 0:
        failures.append('rounding mode is not nearest')
    if failures:
        raise RuntimeError('; '.join(failures))
    with np.load(FOLDER/'complete-covariance-532.npz') as saved:
        data = {key: saved[key] for key in saved.files}
    assert set(data) == {'m0','mc','mg','cov00','covcc','covgg','cov0c','cov0g','covcg'}
    assert all(x.shape == (N,N) and np.all(np.isfinite(x)) for x in data.values())
    # Rebuild the product block directly from audited inputs; C744x is not an input.
    t, tt = data['mc']+data['mg'], data['mc']-data['mg']
    head = np.block([[data['m0'], -tt], [-t, data['m0']]])
    common = data['cov00']+data['covcc']+data['covgg']
    cg = data['covcg']+data['covcg'].T
    tr = -data['cov0c']+data['cov0g']-data['cov0c'].T-data['cov0g'].T
    covariance = np.block([[common+cg, tr], [tr.T, common-cg]])
    residual_raw = head-covariance/TAU
    residual = (residual_raw+residual_raw.T)/2
    z = np.zeros((4, 2*N))
    weights = np.ones(N)
    weights[0] = 1/np.sqrt(2.)
    for component in range(2):
        for parity in range(2):
            indices = np.arange(parity, N, 2)
            z[2*component+parity,component*N+indices] = weights[indices]
    u = (z.T@z)/5000+np.eye(2*N)/125000
    paid = residual-u/TAU
    ledger = audit['error_ledger']
    e_f = ledger['analytic_response_q_error']+3*math.sqrt((K-N)*N)*1e-7
    e_m = ledger['analytic_head_error']+3*N*1e-7
    debt = e_m+((2*sum(ledger['factor_frobenius_norms'])+e_f)*e_f+1e-6)/TAU
    assert debt < .012
    reconstruction = None
    factor_path = FOLDER/'matrix-tail-factor-539.npz'
    try:
        factor = np.linalg.cholesky(paid-PAID_FLOOR*np.eye(2*N))
        difference = paid-PAID_FLOOR*np.eye(2*N)-factor@factor.T
        error = math.sqrt(float(np.sum(difference*difference)))
        norm_squared = float(np.sum(factor*factor))
        reconstruction = dict(full_frobenius_residual=error, required_residual=1e-7,
                              factor_frobenius_squared=norm_squared, required_norm_squared=20000,
                              maximum_matrix_entry=float(np.max(np.abs(paid))),
                              maximum_factor_entry=float(np.max(np.abs(factor))),
                              reconstruction_debt='.000001', matrix_U_arithmetic_debt='.000001')
        if not (np.all(np.isfinite(factor)) and error < 1e-7 and norm_squared < 20000
                and reconstruction['maximum_matrix_entry'] < 400
                and reconstruction['maximum_factor_entry'] < 20):
            failures.append('full reconstruction budget failed')
        np.savez_compressed(factor_path, factor=factor)
    except np.linalg.LinAlgError:
        failures.append('frozen paid floor .04 did not admit a factor; no retuning')
    matrices_path = FOLDER/'matrix-tail-matrices-539.npz'
    np.savez_compressed(matrices_path, head=head, covariance=covariance,
                        finite_residual=residual, z=z, u=u, paid=paid)
    final_lower = Decimal('.04')-Decimal('.012')-Decimal('.000002')
    result = dict(parameters=dict(N=N, K=K, penalty=256, tau='143/100',
                                  separation=7, proposed_paid_floor='1/25'),
                  scalar_certificate=scalars, input_checks=checks,
                  audit_sha256=digest(audit_path), input_replay_records=audit['covariance_checks'],
                  inherited_error_ledger=ledger, actual_finite_debt=debt, required_finite_debt='.012',
                  reconstruction=reconstruction, complete_lower_bound=str(final_lower) if not failures else None,
                  required_complete_lower_bound='0', failures=failures,
                  complete_covariance_paid_under_contract=not failures,
                  independent_audit_complete=False, rh_candidate=False,
                  qualification='Full fixed mixed Schur comparison only; strict H2 slack, composition, other separations, non-neutral coverage and RH remain open.',
                  arithmetic_contract='C744v/w IEEE754 binary64 nearest basic operations, sqrt, dot gamma bounds; directed Decimal for scalar certificate',
                  runtime=dict(python=sys.version, numpy=np.__version__, machine=platform.machine(),
                               fegetround=ctypes.CDLL(None).fegetround()),
                  artifacts=[dict(path=p.name,sha256=digest(p)) for p in [matrices_path]+([factor_path] if reconstruction else [])])
    path = FOLDER/'matrix-tail-certificate-539.json'
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('Leading HS squared:',scalars['leading_hilbert_schmidt_squared']['hi'],'required <.0001; remainder:',
          scalars['full_operator_remainder']['hi'],'required <.002.')
    print('All',len(scalars['chord_checks']),'chord checks: minimum',scalars['minimum_chord_lower'],'required >.01.')
    print('Finite debt:',debt,'required <.012; reconstruction:',reconstruction)
    print('Complete lower:',result['complete_lower_bound'],'required >=0; failures:',failures)
    print('Certificate:',path,'matrices:',matrices_path,'factor:',factor_path if reconstruction else None)


if __name__ == '__main__':
    main()
