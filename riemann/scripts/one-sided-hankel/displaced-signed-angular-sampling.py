"""Bounded floating-point diagnostic for the exact displaced rational family.

No interval/asymptotic certificate is asserted.  All original residues are one.
Output retains rational shift specifications and every rational-quadrature row.
Run from riemann: python3 scripts/one-sided-hankel/displaced-signed-angular-sampling.py
"""

import json
import math
from pathlib import Path

import numpy as np


OUT = Path(__file__).with_suffix('.json')
R = 11 / 8
U = R * R
X = -5 / 4
SHIFT_DENOMINATOR = 100_000_000


def family(n, shifts):
    q = (n - 3) // 12
    h0 = 27 / (10 * n)
    ordinates = h0 * (np.arange(-2 * q, 2 * q) + 0.5 + shifts)
    return np.r_[complex(X), X + 1j * ordinates]


def response(n, shifts, theta, gradient=False):
    a = family(n, shifts)[None, :]
    u = np.exp(1j * np.asarray(theta))[:, None]
    w = np.broadcast_to(X / a, (len(theta), a.shape[1])).copy()
    if gradient:
        log_derivative = np.broadcast_to(-1 / a, w.shape).copy()
    for j in range(1, n):
        t = j / n
        w *= ((X - t * u) / (a - t * u)) * ((U * u - t * a) / (U * u - t * X))
        if gradient:
            log_derivative -= 1 / (a - t * u) + t / (U * u - t * a)
    c0 = w.sum(axis=1) / R
    inv_clearance = 1 / (U - np.abs(a[0]) ** 2)
    diagonal = (np.abs(w) ** 2 * inv_clearance).sum(axis=1)
    if not gradient:
        return c0, diagonal
    dw = 1j * (27 / (10 * n)) * w[:, 1:] * log_derivative[:, 1:]
    e0 = np.mean(np.abs(c0) ** 2)
    diagonal_mean = np.mean(diagonal)
    de = (2 / R) * np.real(c0.conj()[:, None] * dw).mean(axis=0)
    d_diagonal = (
        2 * np.real(w[:, 1:].conj() * dw) * inv_clearance[1:]
        + np.abs(w[:, 1:]) ** 2
        * (2 * a[0, 1:].imag * (27 / (10 * n)) * inv_clearance[1:] ** 2)
    ).mean(axis=0)
    objective = math.log(e0) - math.log(diagonal_mean)
    return objective, de / e0 - d_diagonal / diagonal_mean


def descend(n, initial, theta, iterations=60):
    shifts = initial.copy()
    moment = np.zeros_like(shifts)
    variance = np.zeros_like(shifts)
    best = (math.inf, shifts.copy())
    trace = []
    for step in range(1, iterations + 1):
        value, grad = response(n, shifts, theta, gradient=True)
        trace.append({'iteration': step, 'log_e0_over_d': float(value)})
        if value < best[0]:
            best = (value, shifts.copy())
        moment = 0.9 * moment + 0.1 * grad
        variance = 0.999 * variance + 0.001 * grad * grad
        direction = (moment / (1 - 0.9 ** step)) / (np.sqrt(variance / (1 - 0.999 ** step)) + 1e-10)
        shifts = np.clip(shifts - 0.025 * direction, -0.125, 0.125)
    return best, trace


def pole_completion(n, shifts):
    a = family(n, shifts)
    t = np.arange(1, n) / n
    return np.r_[0j, t * X / U, (t[:, None] / a[None, 1:].conj()).ravel()]


def phase_and_derivative(theta, poles):
    phase = np.empty(len(theta))
    mu = np.empty(len(theta))
    count = len(poles)
    for begin in range(0, len(theta), 256):
        stop = min(begin + 256, len(theta))
        t = theta[begin:stop]
        z = np.exp(-1j * t[:, None]) * poles[None, :]
        phase[begin:stop] = count * t + 2 * np.angle(1 - z).sum(axis=1)
        mu[begin:stop] = ((1 - np.abs(poles) ** 2) / np.abs(1 - z) ** 2).sum(axis=1)
    return phase, mu


def rational_quadrature(n, shifts):
    poles = pole_completion(n, shifts)
    count = len(poles)
    origin_phase = phase_and_derivative(np.array([0.0]), poles)[0][0]
    levels = origin_phase + np.arange(2 * count) * math.pi
    theta = np.arange(2 * count) * math.pi / count
    residual_trace = []
    for _ in range(12):
        phase, mu = phase_and_derivative(theta, poles)
        error = phase - levels
        residual_trace.append(float(np.max(np.abs(error))))
        if residual_trace[-1] < 2e-10:
            break
        theta -= error / mu
    phase, mu = phase_and_derivative(theta, poles)
    c0, diagonal = response(n, shifts, theta)
    weights = 1 / (2 * mu)
    return {
        'interior_pole_count': count,
        'observation_count': 2 * count,
        'phase_residual_trace': residual_trace,
        'phase_residual_max': float(np.max(np.abs(phase - levels))),
        'weight_sum': float(weights.sum()),
        'theta_increasing': bool(np.all(np.diff(theta) > 0)),
        'weights_positive': bool(np.all(weights > 0)),
        'e0': float(np.sum(weights * np.abs(c0) ** 2)),
        'd': float(np.sum(weights * diagonal)),
        'sample_c0_max': float(np.max(np.abs(c0))),
        'rows': [
            {'theta': float(th), 'mu': float(m), 'weight': float(w),
             'c0_real': float(v.real), 'c0_imag': float(v.imag), 'diagonal': float(dg)}
            for th, m, w, v, dg in zip(theta, mu, weights, c0, diagonal)
        ],
    }


def metrics(n, e0, d, observed_max):
    norm_required_without_constant = n * math.exp(-n / 32) * math.sqrt(d)
    return {
        'e0': float(e0), 'd': float(d), 'sample_c0_max': float(observed_max),
        'norm_benchmark_without_unknown_constant': norm_required_without_constant,
        'l2_over_benchmark': math.sqrt(e0) / norm_required_without_constant,
        'sample_max_over_benchmark': observed_max / norm_required_without_constant,
        'log_e0_over_d_per_n': math.log(e0 / d) / n,
        'required_log_ratio_per_n_without_constant': 2 * math.log(n) / n - 1 / 16,
    }


def main():
    rng = np.random.default_rng(20261102)
    doc = {
        'status': 'FLOATING_POINT_DIAGNOSTIC_NOT_PROOF',
        'scope': 'n=27,51,99; all unit residues; independent shifts |epsilon|<=H_0/8',
        'limitations': [
            'No interval enclosure of arithmetic, quadrature roots, or angular maxima.',
            'Finite nonconvex optimization does not give a global minimum.',
            'A finite benchmark ratio does not decide an unspecified uniform positive constant or onset.',
            'E_0 lower bound is sufficient via maximum and Jensen; its failure would not refute H.',
        ],
        'records': [], 'diagnostic_failures': [],
    }
    for n in (27, 51, 99):
        size = n // 3 - 1
        theta = 2 * math.pi * np.arange(256) / 256
        initial = rng.uniform(-0.1, 0.1, size)
        if n == 27:
            value, gradient = response(n, initial, theta, gradient=True)
            direction = rng.normal(size=size)
            direction /= np.linalg.norm(direction)
            epsilon = 1e-6
            plus = response(n, initial + epsilon * direction, theta, gradient=True)[0]
            minus = response(n, initial - epsilon * direction, theta, gradient=True)[0]
            actual = (plus - minus) / (2 * epsilon)
            predicted = float(gradient @ direction)
            doc['directional_derivative_check'] = {
                'finite_difference': actual, 'analytic_gradient': predicted,
                'absolute_discrepancy': abs(actual - predicted), 'diagnostic_tolerance': 1e-6,
            }
            if abs(actual - predicted) > 1e-6:
                doc['diagnostic_failures'].append('directional derivative discrepancy')
        candidates = []
        for label, start in (('zero', np.zeros(size)), ('independent_random', initial)):
            best, trace = descend(n, start, theta)
            candidates.append((best[0], best[1], label, trace))
        selected = min(candidates, key=lambda item: item[0])
        integers = np.rint(selected[1] * SHIFT_DENOMINATOR).astype(np.int64)
        shifts = integers / SHIFT_DENOMINATOR
        if np.max(np.abs(integers)) > SHIFT_DENOMINATOR // 8:
            raise ValueError('Stored rational family exceeds allowed shifts')
        dense_theta = 2 * math.pi * np.arange(4096) / 4096
        c0, diagonal = response(n, shifts, dense_theta)
        baseline_c0, baseline_diag = response(n, np.zeros(size), dense_theta)
        quadrature = rational_quadrature(n, shifts)
        quad_metrics = metrics(n, quadrature['e0'], quadrature['d'], quadrature['sample_c0_max'])
        dense_metrics = metrics(n, np.mean(np.abs(c0) ** 2), np.mean(diagonal), np.max(np.abs(c0)))
        relative_e = abs(quad_metrics['e0'] - dense_metrics['e0']) / max(quad_metrics['e0'], dense_metrics['e0'])
        relative_d = abs(quad_metrics['d'] - dense_metrics['d']) / max(quad_metrics['d'], dense_metrics['d'])
        consistency = {
            'e0_relative_discrepancy': relative_e,
            'd_relative_discrepancy': relative_d,
            'required_diagnostic_discrepancy_at_most': 1e-8,
            'required_phase_residual_at_most': 2e-9,
            'required_weight_sum_error_at_most': 1e-10,
        }
        if max(relative_e, relative_d) > 1e-8:
            doc['diagnostic_failures'].append(f'n={n}: dense grid/quadrature discrepancy')
        if quadrature['phase_residual_max'] > 2e-9 or abs(quadrature['weight_sum'] - 1) > 1e-10:
            doc['diagnostic_failures'].append(f'n={n}: quadrature convergence discrepancy')
        if not quadrature['theta_increasing'] or not quadrature['weights_positive']:
            doc['diagnostic_failures'].append(f'n={n}: quadrature ordering or weight failure')
        record = {
            'n': n, 'q': (n - 3) // 12, 'm': n // 3,
            'rational_shift_definition': 'epsilon_m=27/(10*n)*numerator_m/denominator',
            'shift_denominator': SHIFT_DENOMINATOR, 'shift_numerators': integers.tolist(),
            'ordinate_indices': list(range(-2 * ((n - 3) // 12), 2 * ((n - 3) // 12))),
            'selected_start': selected[2],
            'optimization_traces': {item[2]: item[3] for item in candidates},
            'baseline_dense': metrics(n, np.mean(np.abs(baseline_c0) ** 2), np.mean(baseline_diag), np.max(np.abs(baseline_c0))),
            'optimized_dense': dense_metrics, 'optimized_quadrature_metrics': quad_metrics,
            'diagnostic_consistency': consistency, 'quadrature': quadrature,
        }
        doc['records'].append(record)
        OUT.write_text(json.dumps(doc, indent=2) + '\n')
        print(f'n={n}: E0={quad_metrics["e0"]:.9g}, D={quad_metrics["d"]:.9g}, '
              f'L2/benchmark={quad_metrics["l2_over_benchmark"]:.9g}, '
              f'sampled-max/benchmark={quad_metrics["sample_max_over_benchmark"]:.9g}; '
              f'observations={quadrature["observation_count"]}', flush=True)
    doc['summary'] = {
        'uniform_bound_proved': False, 'countersequence_proved': False,
        'diagnostic_failure_count': len(doc['diagnostic_failures']),
        'n_values': [r['n'] for r in doc['records']],
        'optimized_l2_over_benchmark': [r['optimized_quadrature_metrics']['l2_over_benchmark'] for r in doc['records']],
        'optimized_sample_max_over_benchmark': [r['optimized_quadrature_metrics']['sample_max_over_benchmark'] for r in doc['records']],
        'baseline_l2_over_benchmark': [r['baseline_dense']['l2_over_benchmark'] for r in doc['records']],
    }
    OUT.write_text(json.dumps(doc, indent=2) + '\n')
    print(f'Diagnostic failures: {doc["diagnostic_failures"]}; no rigorous uniform bound or countersequence.', flush=True)
    print(f'Full diagnostic certificate: {OUT}', flush=True)


if __name__ == '__main__':
    main()
