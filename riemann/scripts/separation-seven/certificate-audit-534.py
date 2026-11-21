#!/usr/bin/env python3
"""Replay the frozen certificate without overwriting its evidence.

This checks full arrays, not previews. Mathematical allowances and the
limits of the execution contract are discussed in the canonical audit.
"""
import hashlib
import importlib.util
import json
import math
import platform
import sys
import ctypes
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

import numpy as np

FOLDER = Path(__file__).resolve().parent


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path):
    with path.open('rb') as stream:
        digest = hashlib.file_digest(stream, 'sha256')
    return digest.hexdigest()


def contract_checks():
    """Finite exact checks for powers; record the platform rounding mode."""
    powers = []
    for exponent in range(64):
        computed = 3.**(-exponent)
        relative = abs(Fraction.from_float(computed)*3**exponent-1)
        bound = Fraction(1,2**52)
        powers.append(dict(exponent=exponent, actual_hex=computed.hex(),
                           exact_relative_error=str(relative),
                           required_error=str(bound), passed=relative<bound))
    library = ctypes.CDLL(None)
    rounding = library.fegetround()
    result = dict(float_power_checks=powers, fegetround=rounding,
                  python=sys.version, machine=platform.machine(),
                  numpy=np.__version__,
                  qualification='Runtime identification and finite exact power checks; the stated IEEE basic-operation/sqrt/dot-product execution contract remains an explicit computational hypothesis, not a formal verification of the platform',
                  failures=[f'power {row["exponent"]}' for row in powers if not row['passed']])
    path = FOLDER/'runtime-contract-534.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('Exact float-power tests:',len(powers),'required relative error <2^-52;',
          'rounding mode',rounding,'failures',result['failures'],'certificate',path)


def main():
    source = load_module('residual532', FOLDER/'residual-certificate-532.py')
    scalar = load_module('scalar531', FOLDER/'complete-schur-531.py')
    failures = []
    scalar_replay = scalar.scalar_certificate()
    scalar_original = json.loads((FOLDER/'scalar-certificate-531.json').read_text())
    scalar_equal = scalar_replay == scalar_original
    if not scalar_equal:
        failures.append('531 scalar certificate differs from complete replay')
    scalar_tail = source.scalar_tail()
    saved = json.loads((FOLDER/'complete-residual-certificate-532.json').read_text())
    if scalar_tail != saved['scalar_tail_certificate']:
        failures.append('532 scalar tail differs from complete replay')

    # Verify all otherwise-uncontracted float powers used by the generator.
    # Decimal here has >50 digits of slack against these rational tests.
    # Every compared float is converted exactly, not by its decimal display.
    power_checks = []
    with localcontext() as ctx:
        ctx.prec = 90
        unit = Decimal(2)**-53
        for exponent in sorted(set(range(64)) | {6*j for j in range(1, 8)}):
            exact = Decimal(1)/(Decimal(3)**exponent)
            actual = Decimal(3.**(-exponent))
            relative = abs(actual/exact-1)
            bound = 2*unit
            power_checks.append(dict(exponent=exponent,
                                     actual_hex=(3.**(-exponent)).hex(),
                                     relative_error=str(relative), required=str(bound),
                                     passed=relative<bound))
            if not relative<bound:
                failures.append(f'float power error at exponent {exponent}')

    replay_dir = FOLDER/'audit-replay-534'
    replay_dir.mkdir(exist_ok=True)
    source.FOLDER = replay_dir
    data, ledger = source.assemble()
    covariance_checks = []
    with np.load(FOLDER/'complete-covariance-532.npz') as original:
        if set(original.files) != set(data):
            failures.append('covariance key set differs')
        for key, matrix in data.items():
            old = original[key]
            difference = matrix-old
            exact_match = np.array_equal(matrix, old)
            record = dict(key=key, shape=list(matrix.shape),
                          finite=bool(np.all(np.isfinite(matrix))),
                          exact_match=bool(exact_match),
                          maximum_entry_difference=float(np.max(abs(difference))),
                          frobenius_difference=float(np.linalg.norm(difference)))
            covariance_checks.append(record)
            if not exact_match or not record['finite']:
                failures.append(f'covariance replay mismatch: {key}')
    identity = np.eye(512)
    phase_records = []
    # Reconstruct with the stored factors, never request new Cholesky factors.
    with np.load(FOLDER/'phase-cholesky-factors-532.npz') as archive:
        factors = archive['factors']
    if factors.shape != (65,512,512):
        raise ValueError('wrong factor dimensions')
    pi = float(source.PI_TEXT)
    for j, factor in enumerate(factors):
        s, c = source.sincos(np.array(j*pi/64), pi)
        covariance = (data['cov00'] + c*c*data['covcc'] + s*s*data['covgg']
                      + c*(data['cov0c']+data['cov0c'].T)
                      + 1j*s*(data['cov0g']-data['cov0g'].T)
                      + 1j*c*s*(data['covcg']-data['covcg'].T))
        matrix = data['m0'] + c*data['mc'] + 1j*s*data['mg'] - covariance/1.43
        matrix = (matrix + matrix.conj().T)/2
        difference = matrix - .24*identity - factor@factor.conj().T
        # Real squares avoid an unstated accuracy contract for complex abs/hypot.
        error = math.sqrt(float(np.sum(difference.real*difference.real
                                        + difference.imag*difference.imag)))
        normsq = float(np.sum(factor.real*factor.real + factor.imag*factor.imag))
        record = dict(index=j, finite=bool(np.all(np.isfinite(factor))),
                      full_reconstruction_frobenius=error,
                      factor_frobenius_squared=normsq,
                      maximum_matrix_entry=float(np.max(abs(matrix.real)+abs(matrix.imag))),
                      maximum_factor_entry=float(np.max(abs(factor.real)+abs(factor.imag))),
                      required_reconstruction=1e-7, required_norm_squared=10000)
        phase_records.append(record)
        if not(record['finite'] and error<1e-7 and normsq<10000
               and record['maximum_matrix_entry']<400):
            failures.append(f'factor reconstruction failure: {j}')
    result = dict(
        scope='Full frozen covariance replay, all stored-factor reconstructions and scalar ledgers; analytic allowances require canonical audit',
        runtime=dict(python=sys.version, machine=platform.machine(), system=platform.system(),
                     numpy=np.__version__, decimal_context='explicit 60 or 90 digits',
                     blas=np.__config__.CONFIG.get('Build Dependencies',{}).get('blas',{})),
        scalar_replay_exact=scalar_equal, scalar_certificate=scalar_replay,
        scalar_tail_certificate=scalar_tail, power_checks=power_checks,
        covariance_checks=covariance_checks, error_ledger=ledger,
        phases=phase_records,
        rounded_uniform_lower='0.030999', required_uniform_lower='0.025',
        mathematical_proof='See canonical C744v/w audit; replay alone is not an arithmetic or analytic proof',
        failures=failures,
        original_sha256={name:sha256(FOLDER/name) for name in [
            'complete-schur-531.py','residual-certificate-532.py',
            'scalar-certificate-531.json','complete-residual-certificate-532.json',
            'complete-covariance-532.npz','phase-cholesky-factors-532.npz']})
    path = FOLDER/'certificate-audit-534.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('Full replay: matrices', len(covariance_checks), 'phases', len(phase_records),
          'max reconstruction',max(x['full_reconstruction_frobenius'] for x in phase_records),
          'required <1e-7; error ledger',ledger['sampled_schur_error'],'required <.012;',
          'claimed lower .030999 required .025;',
          'failures',failures, 'certificate',path,flush=True)


if __name__ == '__main__':
    if '--contract-only' in sys.argv:
        contract_checks()
    else:
        main()
