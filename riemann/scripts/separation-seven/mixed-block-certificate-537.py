#!/usr/bin/env python3
"""Fixed independent-profile Schur test; no scalar-phase inference.

Reuses all six audited raw covariance products from C744w. Analytic
entry, domain and infinite-tail allowances need the canonical proof.
Cholesky is only a factor proposer. This script never modifies inputs.
"""
import ctypes
import hashlib
import json
import math
import platform
import sys
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

import numpy as np

FOLDER = Path(__file__).resolve().parent
N, K, TAU = 512, 65536, 1.43
FLOOR = .2  # Frozen before this invocation; no parameter search.


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def exact_dyadic_rayleigh(matrix, vector):
    """Read every entry as a rational; integer accumulation is exact."""
    vector_ratios = [float(x).as_integer_ratio() for x in vector]
    vector_scale = max(d.bit_length()-1 for _, d in vector_ratios)
    integers = [n << (vector_scale-(d.bit_length()-1))
                for n, d in vector_ratios]
    matrix_scale = max(float(x).as_integer_ratio()[1].bit_length()-1
                       for x in matrix.flat)
    numerator = 0
    for i, row in enumerate(matrix):
        row_sum = 0
        for x, coefficient in zip(row, integers):
            n, d = float(x).as_integer_ratio()
            row_sum += (n << (matrix_scale-(d.bit_length()-1)))*coefficient
        numerator += integers[i]*row_sum
    norm_squared_integer = sum(x*x for x in integers)
    if norm_squared_integer == 0:
        raise ValueError('zero direction')
    rayleigh = Fraction(numerator, (1 << matrix_scale)*norm_squared_integer)
    return rayleigh, dict(
        matrix_binary_scale=matrix_scale, vector_binary_scale=vector_scale,
        exact_quadratic_integer=str(numerator),
        exact_vector_norm_squared_integer=str(norm_squared_integer),
        exact_rayleigh_numerator=str(rayleigh.numerator),
        exact_rayleigh_denominator=str(rayleigh.denominator),
        entries_accumulated=matrix.size,
        rational_upper='9/100', strict_upper_check=rayleigh < Fraction(9,100))


def main():
    failures = []
    audit_path = FOLDER/'certificate-audit-534.json'
    audit = json.loads(audit_path.read_text())
    saved_path = FOLDER/'complete-residual-certificate-532.json'
    saved = json.loads(saved_path.read_text())
    input_checks = []
    for name in ['complete-covariance-532.npz',
                 'complete-residual-certificate-532.json']:
        actual = digest(FOLDER/name)
        expected = audit['original_sha256'][name]
        input_checks.append(dict(path=name, sha256=actual,
                                 expected=expected, passed=actual == expected))
        if actual != expected:
            failures.append('audited input hash mismatch: '+name)
    if audit['failures']:
        failures.append('prior covariance audit reports failures')
    if not all(row['finite'] and row['exact_match']
               for row in audit['covariance_checks']):
        failures.append('prior full covariance replay was not exact')
    if len(audit['covariance_checks']) != 9:
        failures.append('prior audit missing covariance records')
    if audit['error_ledger'] != saved['error_ledger']:
        failures.append('audited error ledger mismatch')

    ledger = audit['error_ledger']
    norms = ledger['factor_frobenius_norms']
    base_error = math.sqrt((K-N)*N)*1e-7
    e_f = ledger['analytic_response_q_error']+3*base_error
    e_m = ledger['analytic_head_error']+3*N*1e-7
    factor_norm_upper = sum(norms)
    # The product-space factor uses a diagonal B0 and off-diagonal
    # Bc+/-Bg. Their operator bounds are sum(norms), not sqrt(2)
    # times that sum. The same holds for their entry-error operators.
    debt = e_m+((2*factor_norm_upper+e_f)*e_f+1e-6)/TAU
    if not(debt < .012 and e_f < .001732 and e_m < .000337):
        failures.append('finite block arithmetic budget exceeded')
    tail = audit['scalar_tail_certificate']
    if tail != saved['scalar_tail_certificate']:
        failures.append('audited scalar tail mismatch')
    if not Decimal(tail['full_factor_tail']['hi']) < Decimal('.5'):
        failures.append('entire mixed factor tail exceeds one half')

    rounding_mode = ctypes.CDLL(None).fegetround()
    if rounding_mode != 0:
        failures.append('runtime is not in recorded nearest rounding mode')
    if failures:
        raise RuntimeError('; '.join(failures))

    with np.load(FOLDER/'complete-covariance-532.npz') as archive:
        data = {key: archive[key] for key in archive.files}
    if set(data) != {'m0','mc','mg','cov00','covcc','covgg',
                     'cov0c','cov0g','covcg'}:
        raise ValueError('wrong covariance keys')
    if not all(x.shape == (N,N) and np.all(np.isfinite(x))
               for x in data.values()):
        raise ValueError('nonfinite or wrong-size covariance input')
    t = data['mc']+data['mg']
    tt = data['mc']-data['mg']
    head = np.block([[data['m0'], -tt], [-t, data['m0']]])
    cg_symmetric = data['covcg']+data['covcg'].T
    common = data['cov00']+data['covcc']+data['covgg']
    top_right = (-data['cov0c']+data['cov0g']
                 -data['cov0c'].T-data['cov0g'].T)
    covariance = np.block([[common+cg_symmetric, top_right],
                           [top_right.T, common-cg_symmetric]])
    residual_raw = head-covariance/TAU
    symmetry_error = float(np.linalg.norm(residual_raw-residual_raw.T))
    residual = (residual_raw+residual_raw.T)/2
    matrix_path = FOLDER/'mixed-block-matrices-537.npz'
    np.savez_compressed(matrix_path, head=head, covariance=covariance,
                        residual=residual)
    reconstruction = None
    factor_path = FOLDER/'mixed-block-factor-537.npz'
    try:
        factor = np.linalg.cholesky(residual-FLOOR*np.eye(2*N))
        np.savez_compressed(factor_path, factor=factor)
        difference = residual-FLOOR*np.eye(2*N)-factor@factor.T
        error = math.sqrt(float(np.sum(difference*difference)))
        normsq = float(np.sum(factor*factor))
        reconstruction = dict(
            full_frobenius_residual=error, required_residual=1e-7,
            factor_frobenius_squared=normsq, required_norm_squared=20000,
            maximum_matrix_entry=float(np.max(abs(residual))),
            maximum_factor_entry=float(np.max(abs(factor))),
            exact_reconstruction_allowance='.000001')
        if not(error < 1e-7 and normsq < 20000
               and reconstruction['maximum_matrix_entry'] < 400
               and reconstruction['maximum_factor_entry'] < 20):
            failures.append('full factor reconstruction budget failed')
    except np.linalg.LinAlgError:
        failures.append('fixed finite floor .2 did not admit a proposed Cholesky factor')

    failure_direction = None
    if reconstruction is None:
        # Locate a direction only to diagnose the failed, frozen lower
        # certificate. The eigenvalue is never used as proof.
        eigenvalues, eigenvectors = np.linalg.eigh(residual)
        vector = eigenvectors[:, 0]
        vector_path = FOLDER/'mixed-block-failed-direction-537.npz'
        np.savez_compressed(vector_path, vector=vector)
        rayleigh, exact = exact_dyadic_rayleigh(residual, vector)
        failure_direction = dict(
            locator_eigenvalue=float(eigenvalues[0]),
            exact_dyadic_check=exact,
            finite_true_rayleigh_upper='51/500',
            frozen_tail_charge='7/40',
            frozen_lower_comparison_rayleigh_upper='-73/1000',
            frozen_lower_comparison_not_positive=exact['strict_upper_check'],
            qualification='The exact finite Schur form differs by <.012; .09+.012-.175=-.073. This refutes only the uniform-tail lower comparison, not the true Schur residual or the original mixed form.',
            vector_path=str(vector_path.relative_to(FOLDER.parent.parent)))

    lower = Decimal('.2')-Decimal('.000001')-Decimal('.012')-Decimal('.175')
    result = dict(
        target='d(f)+d(g)+2 Re H(f,tau_(7ell)g)>=0 for independent complex neutral smooth f,g',
        parameters=dict(N_per_profile=N, K=K, penalty=256,
                        tau='1.43', fixed_finite_floor='.2'),
        input_checks=input_checks, audit_sha256=digest(audit_path),
        input_replay_records=audit['covariance_checks'],
        inherited_error_ledger=ledger,
        mixed_error_ledger=dict(factor_norm_upper=factor_norm_upper,
                               factor_error=e_f, head_error=e_m,
                               covariance_arithmetic_allowance=1e-6,
                               actual_finite_debt=debt, required_finite_debt=.012),
        scalar_tail_certificate=tail,
        full_tail_norm_upper='.5', full_tail_debt_upper='.175',
        raw_matrix_symmetry_error=symmetry_error,
        reconstruction=reconstruction,
        failure_direction=failure_direction,
        full_residual_lower=str(lower) if not failures else None,
        required_full_residual_lower='0',
        full_inequality_certified_under_contract=not failures,
        independent_audit_complete=False, rh_candidate=False,
        arithmetic_contract='IEEE binary64 nearest basic operations and sqrt; standard dot-product gamma bounds; C744v/w analytic and arithmetic inputs',
        runtime=dict(python=sys.version, numpy=np.__version__,
                     machine=platform.machine(), fegetround=rounding_mode),
        failures=failures,
        qualification='A failed sufficient Schur certificate would not refute the form. No parameter retuning or negative smooth witness.',
        files=[str(matrix_path.relative_to(FOLDER.parent.parent))]
              +([str(factor_path.relative_to(FOLDER.parent.parent))]
                if reconstruction is not None else []))
    path = FOLDER/'mixed-block-certificate-537.json'
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('Fixed mixed block: finite debt', debt, 'required <.012;',
          'entire factor tail <.5; complete residual lower',
          result['full_residual_lower'], 'required >=0.', flush=True)
    print('Full reconstruction:', reconstruction, flush=True)
    if failure_direction:
        print('Exact failed-direction check:', exact['entries_accumulated'],
              'matrix entries; stored Rayleigh <.09:', exact['strict_upper_check'],
              '; true finite Rayleigh <.102; frozen lower comparison <-.073, required >=0.',
              flush=True)
    print('Failures:', failures, 'certificate:', path, flush=True)


if __name__ == '__main__':
    main()
