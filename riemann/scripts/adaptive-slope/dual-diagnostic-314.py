#!/usr/bin/env python3
"""Finite-grid diagnostic only: no certified quadrature or continuum claim."""
import json
from pathlib import Path
import numpy as np

A, B = 7 / 4, 9 / 4
OUT = Path(__file__).with_name('dual-diagnostic-314.json')


def scaled_kernel(n, t):
    p0 = np.exp(-t / 2)
    p1 = (3 - t) * p0
    for j in range(1, n + 1):
        p0, p1 = p1, ((2 * j + 3 - t) * p1 - (j + 2) * p0) / (j + 1)
    return (p1 - np.exp(-t / 2)) / (n + 1)


def response(n, c, beta, gamma, order=64):
    x, w = np.polynomial.legendre.leggauss(order)
    u, w = (x + 1) / 2, w / 2
    t = c[:, None] * (n + 2 * u[None, :])
    d = beta - 0.5
    upper = scaled_kernel(n, t) * (
        np.exp(d * t - c[:, None] * n / 4)
        + np.exp(-d * t - c[:, None] * n / 4))
    # Every quartet term is retained via the exact cosh/cos identity.
    upper *= (2 * c[:, None]) * w[None, :]
    result = -2 * np.einsum('cq,gcq->cg', upper,
                            np.cos(gamma[:, None, None] * t[None, :, :]))
    tlo = n + 2 * u
    lower = scaled_kernel(n, tlo) * (np.exp(d * tlo) + np.exp(-d * tlo)) * 2 * w
    result += 2 * np.exp(-c[:, None] * n / 4) * (
        np.cos(gamma[:, None] * tlo[None, :]) @ lower)[None, :]
    return result


report = {
    'status': 'UNCERTIFIED_DIAGNOSTIC',
    'target': 'All-measure dual obstruction for the unchanged review312 assay',
    'required': {
        'dual': 'Uniform c error O(exp(-kappa*n)), kappa>0, and coefficient l1 exp(o(n)); neither finite samples nor floating arithmetic proves this.',
        'primal': 'Selected response one, uniform gamma leakage O(exp(-delta*n)), delta>0, TV exp(o(n)).',
    },
    'method': 'Real exact quartet kernels; numerical Gauss-Legendre quadrature; truncated SVD least squares on the full normalized competing matrix. Candidate finite dual combinations are tested at extra c points.',
    'failures': ['No interval arithmetic', 'No proof of uniformity between points', 'No all-n estimate', 'SVD small singular values have floating-point uncertainty'],
    'runs': [],
}

for n in [8, 16, 24, 32, 48, 64]:
    c = np.linspace(A, B, 4 * n + 1)
    check_c = np.linspace(A, B, 8 * n + 2)
    gamma = np.linspace(A, B, 2 * n + 1)
    selected = response(n, c, 3 / 4, np.array([1.0]))[:, 0]
    competing = response(n, c, 7 / 8, gamma)
    selected_check = response(n, check_c, 3 / 4, np.array([1.0]), 96)[:, 0]
    competing_check = response(n, check_c, 7 / 8, gamma, 96)
    scale = np.exp(B * n / 8)
    u, sv, vh = np.linalg.svd(competing / scale, full_matrices=False)
    candidates = []
    for tol in [1e-5, 1e-7, 1e-9, 1e-11, 1e-13]:
        keep = sv > tol * sv[0]
        coeff = vh[keep, :].T @ ((u[:, keep].T @ (selected / scale)) / sv[keep])
        residual = selected_check - competing_check @ coeff
        max_error = float(np.max(np.abs(residual)))
        l1 = float(np.sum(np.abs(coeff)))
        candidates.append({
            'svd_relative_cutoff': tol,
            'retained_rank': int(np.sum(keep)),
            'coeff_l1': l1,
            'log_coeff_l1_per_n': float(np.log(max(l1, 1e-300)) / n),
            'check_grid_max_error': max_error,
            'error_relative_to_selected_max': max_error / float(np.max(np.abs(selected_check))),
            'negative_log_error_per_n': float(-np.log(max(max_error, 1e-300)) / n),
            'coefficients': coeff.tolist(),
            'check_grid_residuals': residual.tolist(),
        })
    quad_difference = float(np.max(np.abs(competing - response(n, c, 7 / 8, gamma, 96))))
    run = {
        'n': n, 'c': c.tolist(), 'check_c': check_c.tolist(), 'gamma': gamma.tolist(),
        'singular_values_scaled': sv.tolist(),
        'selected_check_max': float(np.max(np.abs(selected_check))),
        'competing_quadrature_64_96_max_difference': quad_difference,
        'candidates': candidates,
    }
    report['runs'].append(run)
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    best = min(candidates, key=lambda item: item['check_grid_max_error'])
    print(json.dumps({'n': n, 'best_grid_error': best['check_grid_max_error'],
                      'relative_error': best['error_relative_to_selected_max'],
                      'coefficient_l1': best['coeff_l1'],
                      'retained_rank': best['retained_rank'],
                      'quadrature_difference': quad_difference}), flush=True)

print('UNCERTIFIED_DIAGNOSTIC: required all-n uniform dual bounds remain unproved.')
print('Full certificate path:', OUT)
