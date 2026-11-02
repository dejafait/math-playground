"""Full signed spatial Mahler-mean screen; floating point, never a proof.

Run from riemann with python3 scripts/one-sided-hankel/displaced-angular-maximum-screen.py.
Every original residue, grid factor and prescribed spatial moment is retained.
"""
import json
import math
from pathlib import Path

import numpy as np

OUT = Path(__file__).with_suffix('.json')
X, R = -5 / 4, 11 / 8
U = R * R
DEN = 100_000_000


def coefficients(n, shifts, angles):
    q = (n - 3) // 12
    a = np.r_[complex(X), X + 1j * (27 / (10 * n)) *
              (np.arange(-2*q, 2*q) + .5 + shifts)]
    u = np.exp(1j * np.asarray(angles))[:, None]
    w = np.broadcast_to(X / a, (len(angles), len(a))).copy()
    for j in range(1, n):
        t = j / n
        w *= (X-t*u)/(a-t*u) * (U*u-t*a)/(U*u-t*X)
    # X/a is the j=0 factor. No prefix of the spatial moments is used.
    return w @ ((a[:, None]/R)**np.arange(len(a))[None, :]) / R


def spatial_mean(c, details=False):
    nonzero = np.flatnonzero(c != 0)
    if len(nonzero) == 0:
        raise ArithmeticError('Numerically zero full spatial slice')
    degree = int(nonzero[-1])
    c = c[:degree+1]
    scale = float(np.max(np.abs(c)))
    roots = np.polynomial.polynomial.polyroots(c / scale)
    value = math.log(abs(c[-1])) + float(np.log(np.maximum(1, np.abs(roots))).sum())
    if not details:
        return value
    residuals = []
    for root in roots:
        num = abs(np.polynomial.polynomial.polyval(root, c / scale))
        den = np.polynomial.polynomial.polyval(abs(root), np.abs(c / scale))
        residuals.append(float(num / den))
    return {
        'mean': value, 'actual_degree': degree,
        'leading_factor': [float(c[-1].real), float(c[-1].imag)],
        'coefficients': [[float(z.real), float(z.imag)] for z in c],
        'roots': [[float(z.real), float(z.imag)] for z in roots],
        'root_count': len(roots),
        'max_scaled_root_residual': max(residuals, default=0.),
        'min_root_unit_circle_distance': float(np.min(abs(abs(roots)-1))) if len(roots) else None,
        'log_constant_lower_bound': math.log(abs(c[0])) if c[0] != 0 else None,
    }


def means(n, shifts, angles):
    return np.array([spatial_mean(c) for c in coefficients(n, shifts, angles)])


def optimize(n, initial, angles, rng):
    shifts = initial.copy()
    best = float(np.max(means(n, shifts, angles)))
    trace = [{'iteration': 0, 'sample_max_mean': best}]
    # Explicit finite budget; full independent coordinates remain available.
    for step in range(80):
        direction = rng.normal(size=len(shifts))
        if step % 3 == 0:
            direction[:] = 0
            direction[step % len(shifts)] = 1
        direction /= max(np.max(abs(direction)), 1e-100)
        size = .08 * (.3 ** (step // 27))
        for sign in (1, -1):
            candidate = np.clip(shifts + sign*size*direction, -.125, .125)
            value = float(np.max(means(n, candidate, angles)))
            if value < best:
                shifts, best = candidate, value
        trace.append({'iteration': step+1, 'sample_max_mean': best})
    return shifts, trace


def refine_peak(n, shifts, center, width):
    lo, hi = center-width, center+width
    # Local refinement only; no claim that a missed peak is impossible.
    for _ in range(22):
        p, q = lo+(hi-lo)/3, hi-(hi-lo)/3
        fp, fq = means(n, shifts, [p, q])
        if fp < fq:
            lo = p
        else:
            hi = q
    theta = (lo+hi)/2
    return theta, float(means(n, shifts, [theta])[0])


def main():
    rng = np.random.default_rng(2026110231)
    doc = {
        'status': 'FLOATING_POINT_DIAGNOSTIC_NOT_PROOF',
        'target': 'H >= -n/100-C*log(n), absolute C and onset',
        'limitations': [
            'Finite nonconvex search is not minimization over the displacement cube.',
            'Angular mesh and local refinement do not certify the global maximum.',
            'Root computations and quadrature have no interval enclosures.',
            'No finite n range decides the unknown absolute constant or onset.',
        ],
        'records': [], 'failures': [],
    }
    for n in (15, 27, 51, 99):
        q = (n-3)//12
        coarse = np.arange(64)*2*math.pi/64
        for start in ('zero', 'independent_random'):
            initial = np.zeros(4*q) if start == 'zero' else rng.uniform(-.125, .125, 4*q)
            shifts, trace = optimize(n, initial, coarse, rng)
            numerators = np.rint(shifts*DEN).astype(int)
            shifts = numerators/DEN
            angles = np.arange(512)*2*math.pi/512
            rows = []
            for theta, c in zip(angles, coefficients(n, shifts, angles)):
                row = spatial_mean(c, details=True)
                row['theta'] = float(theta)
                rows.append(row)
            observed = np.array([r['mean'] for r in rows])
            refined = [refine_peak(n, shifts, angles[k], 2*math.pi/512)
                       for k in np.argsort(observed)[-4:]]
            peak_theta, peak_value = max(refined, key=lambda pair: pair[1])
            peak_c = coefficients(n, shifts, [peak_theta])[0]
            peak = spatial_mean(peak_c, details=True)
            peak['theta'] = peak_theta
            # Independent dense spatial quadrature at the observed peak.
            quadratures = []
            for count in (4096, 16384):
                z = np.exp(2j*math.pi*(np.arange(count)+.371)/count)
                quadratures.append({'count': count, 'mean': float(np.log(abs(
                    np.polynomial.polynomial.polyval(z, peak_c))).mean())})
            maxres = max(r['max_scaled_root_residual'] for r in rows+[peak])
            jensen_defect = min(r['mean']-r['log_constant_lower_bound']
                               for r in rows if r['log_constant_lower_bound'] is not None)
            failures = []
            if maxres > 1e-9:
                failures.append('large polynomial root residual')
            if jensen_defect < -1e-8:
                failures.append('numerical Jensen inequality failed')
            if any(r['root_count'] != n//3-1 for r in rows):
                failures.append('actual degree differed from prescribed maximum; see retained rows')
            if abs(quadratures[-1]['mean']-peak_value) > .002:
                failures.append('dense spatial quadrature differs by more than .002')
            record = {
                'n': n, 'M': n//3, 'start': start,
                'shift_numerators': numerators.tolist(), 'shift_denominator': DEN,
                'max_shift': float(max(abs(shifts))), 'optimization_trace': trace,
                'coarse_angle_count': 64, 'final_angle_count': 512,
                'sample_max_mean': float(max(observed)), 'refined_peak': peak,
                'sample_min_mean': float(min(observed)),
                'value_at_minus_one': rows[256]['mean'],
                'required_rate_without_unknown_log_constant': -n/100,
                'observed_rate_slack': peak_value+n/100,
                'observed_C_needed': (-peak_value-n/100)/math.log(n),
                'max_scaled_root_residual': maxres, 'min_jensen_defect': jensen_defect,
                'spatial_quadrature_at_peak': quadratures,
                'rows': rows, 'failures': failures,
            }
            doc['records'].append(record)
            doc['failures'].extend([{'n': n, 'start': start, 'failure': f} for f in failures])
            OUT.write_text(json.dumps(doc, indent=2, allow_nan=False)+'\n')
            print(f'n={n} start={start} observed H={peak_value:.9g} rate benchmark={-n/100:.3g} '
                  f'm(-1)={rows[256]["mean"]:.9g} root residual={maxres:.3g} failures={failures}', flush=True)
    doc['summary'] = [{
        'n': r['n'], 'start': r['start'], 'observed_H': r['refined_peak']['mean'],
        'peak_theta': r['refined_peak']['theta'],
        'm_minus_one': r['value_at_minus_one'], 'sample_min_mean': r['sample_min_mean'],
        'max_sample_log_c0': max(row['log_constant_lower_bound'] for row in r['rows']
                                 if row['log_constant_lower_bound'] is not None),
        'peak_spatial_gain_over_c0': r['refined_peak']['mean']-
                                   r['refined_peak']['log_constant_lower_bound'],
        'observed_C_needed': r['observed_C_needed'],
        'root_residual_max': r['max_scaled_root_residual'],
        'quadrature_minus_root': r['spatial_quadrature_at_peak'][-1]['mean']-
                                 r['refined_peak']['mean'],
        'coarse_refined_peak_difference': r['refined_peak']['mean']-
                                        r['optimization_trace'][-1]['sample_max_mean'],
        'failures': r['failures'],
    } for r in doc['records']]
    OUT.write_text(json.dumps(doc, indent=2, allow_nan=False)+'\n')
    print(f'Full diagnostic (not certificate): {OUT}')


if __name__ == '__main__':
    main()
