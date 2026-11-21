#!/usr/bin/env python3
"""Bounded atomic convex candidates, followed by rational interval certificates.

Floating iteration is a proposal only. No optimality, continuum upper bound,
or asymptotic rate is asserted. Kernel arithmetic is reused from step371.
"""
import argparse
import importlib.util
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location('atomic371', HERE/'direct-kernel-atomic-371.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def save(path, data):
    path.write_text(json.dumps(data, indent=2)+'\n')


def matrix(n):
    slopes = [F(7, 4)+F(l, 8*n) for l in range(4*n+1)]
    gammas = [F(15, 8)+F(j, 4*n) for j in range(n+1)]
    columns = []
    for j, g in enumerate(gammas):
        columns.append([v.json() for v in m.kernel_column(n, slopes, g, F(0))])
        if j % 8 == 0:
            print(f'n={n}: enclosed band column {j}/{n}', flush=True)
    target = m.kernel_column(n, slopes, F(1), F(1, 8))
    data = {'n': n, 'slopes': list(map(str, slopes)),
            'gammas': list(map(str, gammas)), 'kernel_columns': columns,
            'target_column': [v.json() for v in target],
            'precision': m.PREC, 'status': 'ENCLOSURES_NOT_A_BOUND'}
    path = HERE/f'direct-kernel-paid-leakage-matrix-{n}-372.json'
    save(path, data)
    m.exact_exp.cache_clear()
    print('Full matrix:', path, flush=True)


def decode(v):
    return m.C(m.R(*v['re']), m.R(*v['im']))


def rationalize(weights):
    # Integer Euclidean lengths rounded UP bound complex TV rigorously.
    scale = max(abs(w) for w in weights)
    if not scale:
        return [(F(0), F(0)) for _ in weights]
    integers = [(int((w/scale).real*10**30), int((w/scale).imag*10**30))
                for w in weights]
    denominator = sum(isqrt(x*x+y*y)+1 for x, y in integers)
    return [(F(x, denominator), F(y, denominator)) for x, y in integers]


def proposals(n, iterations):
    import numpy as np
    row = json.loads((HERE/f'direct-kernel-paid-leakage-matrix-{n}-372.json').read_text())

    def midpoint(v):
        z = decode(v)
        return complex(float(z.re.midpoint()), float(z.im.midpoint()))

    mat = np.array([[midpoint(v) for v in col] for col in row['kernel_columns']]).T
    target = np.array([midpoint(v) for v in row['target_column']])
    # Frobenius bound suffices for stable heuristic step sizes. No SVD,
    # spectral truncation, Taylor ansatz or scalar representer is used.
    common_scale = np.linalg.norm(mat)
    mat, target = mat/common_scale, target/common_scale
    budget = float(np.exp(np.sqrt(n)))

    def project(v, radius):
        absolute = np.abs(v)
        if absolute.sum() <= radius:
            return v
        ordered = np.sort(absolute)[::-1]
        partial = np.cumsum(ordered)
        active = np.nonzero(ordered > (partial-radius)/np.arange(1, len(v)+1))[0][-1]
        level = (partial[active]-radius)/(active+1)
        return v*np.maximum(0, 1-level/np.maximum(absolute, 1e-300))

    candidates, diagnostics = [], []

    def record(v, method, count):
        # v uses the Hermitian pairing; stored atomic weights use sum w*k.
        action = np.vdot(v, target)
        leakage = np.max(np.abs(mat.conj().T@v))
        score = (abs(action)-budget*leakage)*common_scale
        weights = rationalize(np.conjugate(v))
        candidates.append({'method': method, 'iterations': count,
                           'rational_weights': [[str(r), str(i)] for r, i in weights],
                           'floating_score_NOT_CERTIFIED': float(score)})
        diagnostics.append({'method': method, 'iterations': count,
                            'floating_score_NOT_CERTIFIED': float(score),
                            'floating_tv': float(np.abs(v).sum())})
        print(f'n={n}: {method} iteration={count}, proposed score={score:.8e} (UNVERIFIED)', flush=True)

    # Convex saddle heuristic for Re(v*t)-B||M*v||_infinity, ||v||_1<=1.
    # The dual projection is onto the COMPLEX l1 ball of radius B.
    v = np.zeros(len(target), dtype=complex)
    extrapolated = v.copy()
    y = np.zeros(n+1, dtype=complex)
    for step in range(1, iterations+1):
        y = project(y+0.95*(mat.conj().T@extrapolated), budget)
        previous = v
        v = project(v+0.95*(target-mat@y), 1)
        extrapolated = 2*v-previous
        if step in [1000, 10000, iterations]:
            record(v, 'projected_complex_saddle', step)

    # Independent candidate generator: constrained least squares in the
    # primal coefficients, then normalize its residual as an atomic test.
    # It proposes tests only; no sampled upper fit is claimed as a bound.
    coeff = np.zeros(n+1, dtype=complex)
    extrapolated = coeff.copy()
    momentum = 1.0
    for step in range(1, iterations+1):
        residual = mat@extrapolated-target
        newer = project(extrapolated-mat.conj().T@residual, budget)
        next_momentum = (1+np.sqrt(1+4*momentum**2))/2
        extrapolated = newer+(momentum-1)/next_momentum*(newer-coeff)
        coeff, momentum = newer, next_momentum
        if step in [1000, 10000, iterations]:
            test = target-mat@coeff
            test = test/max(np.abs(test).sum(), 1e-300)
            record(test, 'projected_least_squares_residual', step)
    path = HERE/f'direct-kernel-paid-leakage-candidates-{n}-372.json'
    save(path, {'n': n, 'common_scale': float(common_scale),
                'candidates': candidates, 'diagnostics_NOT_CERTIFICATES': diagnostics,
                'status': 'PROPOSALS_ONLY'})
    print('All proposals, including failures:', path, flush=True)


def sqrt_bounds(x):
    """Exact integer-root enclosure; does not rely on Decimal.sqrt rounding."""
    if x < 0:
        raise ArithmeticError('negative square root input')
    value = F(x)
    den = 10**100
    root = isqrt(value.numerator*den*den//value.denominator)
    return m.R(m.R(F(root, den)).lo, m.R(F(root+1, den)).hi)


def modulus(z):
    squared = z.re*z.re+z.im*z.im
    # Generic interval multiplication can cross zero; square lower bound
    # is instead the exact sum of squared coordinate distance bounds.
    lower = m.LO.add(m.LO.multiply(z.re.lower_abs(), z.re.lower_abs()),
                     m.LO.multiply(z.im.lower_abs(), z.im.lower_abs()))
    return m.R(sqrt_bounds(lower).lo, sqrt_bounds(squared.hi).hi)


def verify(n):
    row = json.loads((HERE/f'direct-kernel-paid-leakage-matrix-{n}-372.json').read_text())
    candidates = json.loads((HERE/f'direct-kernel-paid-leakage-candidates-{n}-372.json').read_text())
    columns = [[decode(v) for v in col] for col in row['kernel_columns']]
    target = [decode(v) for v in row['target_column']]
    budget = m.exp_ball(m.C(sqrt_bounds(m.D(n)))).re
    results = []
    for candidate in candidates['candidates']:
        weights = [(F(r), F(i)) for r, i in candidate['rational_weights']]
        assert len(weights) == 4*n+1
        tv = m.R(0)
        for r, i in weights:
            tv = tv+sqrt_bounds(m.R(r*r+i*i).hi)
        assert tv.hi <= 1
        tp = m.pairing(weights, target)
        bp = [m.pairing(weights, col) for col in columns]
        leakage = max(modulus(p).hi for p in bp)
        action = modulus(tp)
        raw_score = m.LO.subtract(action.lo, m.HI.multiply(budget.hi, leakage))
        lower = max(m.D(0), raw_score)
        result = {**candidate, 'tv_upper': str(tv.hi), 'target_pairing': tp.json(),
                  'band_pairings': [p.json() for p in bp],
                  'target_modulus': action.json(), 'band_modulus_upper': str(leakage),
                  'budget': budget.json(), 'raw_score_lower': str(raw_score),
                  'E_n_lower': str(lower),
                  'scaled_lower': str(m.LO.multiply(lower, m.exact_exp(F(n, 64)).re.lo))}
        results.append(result)
        print(f"n={n}: {candidate['method']}({candidate['iterations']}): verified lower={lower:.8E}; leakage<={leakage:.4E}; TV<={tv.hi:.8f}", flush=True)
    best = max(range(len(results)), key=lambda i: m.D(results[i]['E_n_lower']))
    out = HERE/f'direct-kernel-paid-leakage-{n}-372.json'
    save(out, {'n': n, 'status': 'FINITE_LOWER_CERTIFICATES_ONLY',
               'matrix': f'scripts/adaptive-slope/direct-kernel-paid-leakage-matrix-{n}-372.json',
               'results': results, 'best_index': best,
               'best_lower': results[best]['E_n_lower'],
               'best_scaled_lower': results[best]['scaled_lower'],
               'asymptotic_rate': 'UNPROVED', 'failures_omitted': False})
    print('Full certificate:', out, flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--stage', choices=['matrix', 'propose', 'verify', 'all'], default='all')
    parser.add_argument('--n', nargs='+', type=int, default=[16, 32])
    parser.add_argument('--iterations', type=int, default=100000)
    args = parser.parse_args()
    for n in args.n:
        assert n in [16, 32]
        if args.stage in ['matrix', 'all']:
            matrix(n)
        if args.stage in ['propose', 'all']:
            proposals(n, args.iterations)
        if args.stage in ['verify', 'all']:
            verify(n)
