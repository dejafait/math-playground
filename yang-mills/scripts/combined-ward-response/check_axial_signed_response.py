"""L027's signed interior-axial loop for the actual two probes.

Full relative-mode covariance sums and an unbiased randomized trace
diagnostic. Numerical means/standard errors are not certified signs,
bounds, continuum asymptotics, or a computation of the full Gamma.
"""

import argparse
import json
from pathlib import Path

import numpy as np

from haar_contraction import RelativeBox, gradient


def tensor_sum(values, factors):
    for axis, factor in enumerate(factors):
        values = np.moveaxis(np.tensordot(factor, values, axes=(1, axis)), 0, axis)
    return values


def axial_covariances(n):
    """All vertices interior; axes are unchanged, mu is zero-based."""
    vertex = np.sqrt(2/n) * np.sin(np.pi*np.outer(np.arange(1, n), np.arange(1, n))/n)
    edge = np.sqrt(2/n) * np.cos(np.pi*np.outer(np.arange(n)+0.5, np.arange(n))/n)
    edge[:, 0] = 1/np.sqrt(n)
    padded = np.pad(vertex, ((1, 1), (0, 0)))
    difference = np.diff(padded, axis=0)[1:n-1]
    paths = np.cumsum(edge, axis=0)
    lower_path, upper_path = paths[:n-2], paths[1:n-1]
    lower_vertex, upper_vertex = vertex[:n-2], vertex[1:n-1]
    results = {}
    for mu in (1, 2, 3):
        inv = []
        for component in (mu, 0):
            modes = [np.arange(n) if r == component else np.arange(1, n) for r in range(4)]
            lam = np.zeros(tuple(len(k) for k in modes))
            for axis, k in enumerate(modes):
                shape = [1]*4
                shape[axis] = len(k)
                lam += (4*np.sin(np.pi*k/(2*n))**2).reshape(shape)
            inv.append(1/lam)
        coefficients = []
        for low, high, plow, phigh in ((upper_vertex, upper_vertex, upper_path, upper_path),
                                     (lower_vertex, lower_vertex, lower_path, lower_path),
                                     (upper_vertex, lower_vertex, upper_path, lower_path)):
            direct = [vertex**2 for _ in range(4)]
            direct[0], direct[mu] = low*high, edge[1:n-1]**2
            path = [vertex**2 for _ in range(4)]
            path[0], path[mu] = plow*phigh, difference**2
            coefficients.append(tensor_sum(inv[0], direct)+tensor_sum(inv[1], path))
        alpha, beta, cross = coefficients
        results[mu] = (alpha, beta, -cross)
    return results


def active_edges(field, mu, n):
    lower = [slice(None)]*4
    upper = [slice(None)]*4
    lower[0], upper[0] = slice(0, n-2), slice(1, n-1)
    lower[mu] = upper[mu] = slice(1, n-1)
    return field[tuple(upper)], -field[tuple(lower)]


def separated_contraction(left, right, covariances, n):
    result = np.zeros((3, 3))  # planes, path/mixed/curvature
    direct = np.zeros(3)
    for plane, mu in enumerate((1, 2, 3)):
        alpha, beta, rho = covariances[mu]
        yu, yv = active_edges(left[mu], mu, n)
        zu, zv = active_edges(right[mu], mu, n)
        ym, yd = (yu-yv)/2, yu+yv
        zm, zd = (zu-zv)/2, zu+zv
        e, h = alpha+beta+2*rho, alpha+beta-2*rho
        result[plane] = [2*np.sum(e*ym*zm),
                         np.sum((beta-alpha)*(ym*zd+yd*zm)),
                         np.sum(h*yd*zd)/2]
        direct[plane] = 2*np.sum(beta*yu*zu+alpha*yv*zv-rho*(yu*zv+yv*zu))
    return result, direct


def covariance_checks(covariances, n):
    checks = []
    for mu, (alpha, beta, rho) in covariances.items():
        jshape = [1]*4
        jshape[0] = n-2
        j = np.arange(1, n-1).reshape(jshape)
        e, h = alpha+beta+2*rho, alpha+beta-2*rho
        margins = {
            'alpha_lower_(j+1)/8': float(np.min(alpha-(j+1)/8)),
            'alpha_upper_j+9': float(np.min(j+9-alpha)),
            'beta_lower_j/8': float(np.min(beta-j/8)),
            'beta_upper_j+8': float(np.min(j+8-beta)),
            'curvature_variance_lower_0': float(np.min(e)),
            'curvature_variance_upper_1': float(np.min(1-e)),
            'covariance_determinant_lower_0': float(np.min(alpha*beta-rho*rho)),
            'curvature_coefficient_lower_(2j-3)/192': float(np.min(h/48-(2*j-3)/192)),
        }
        checks.append({'type': 'full_grid_covariance_bounds', 'N': n, 'plane_1based': [1, mu+1],
                       'plaquettes': int(alpha.size), 'required_minimum_margin': -1e-10,
                       'actual_minimum_margins': margins,
                       'e_range': [float(e.min()), float(e.max())],
                       'h_range': [float(h.min()), float(h.max())],
                       'passed': bool(min(margins.values()) >= -1e-10)})
    return checks


def dense_check():
    """Independent incidence inverse; one-site sample, not original u."""
    n = 4
    box = RelativeBox(n, sample=True)
    shapes, sizes = box.shapes, [int(np.prod(s)) for s in box.shapes]
    cuts = np.cumsum([0, *sizes])
    size = int(cuts[-1])

    def unpack(x):
        return [x[cuts[mu]:cuts[mu+1]].reshape(shapes[mu]) for mu in range(4)]

    def pack(x):
        return np.concatenate([v.ravel() for v in x])

    eye = np.eye(size)
    curl = np.column_stack([np.concatenate([v.ravel() for v in box.curl(unpack(e)).values()])
                            for e in eye])
    vertex_eye = np.eye((n-1)**4)
    d0 = np.column_stack([pack([gradient(e.reshape(box.vertex_shape), mu) for mu in range(4)])
                          for e in vertex_eye])
    delta = curl.T @ curl+d0 @ d0.T
    sigma = np.linalg.inv(delta)
    lam, waves = np.linalg.eigh(delta)
    heat = (waves*np.exp(-box.tau*lam/box.a**2)) @ waves.T
    half_heat = (waves*np.exp(-box.tau*lam/(2*box.a**2))) @ waves.T
    retract = np.column_stack([pack(box.retract(unpack(e), n-1)) for e in eye])
    a = np.column_stack([pack(box.residual(unpack(e))) for e in eye])
    qs = [np.column_stack([pack(box.probe_matrices(unpack(e))[i]) for e in eye]) for i in (0, 1)]
    covariances = axial_covariances(n)
    cf = retract @ sigma @ retract.T
    max_cov_error = 0.0
    m = np.zeros((size, size))
    for mu, (alpha, beta, rho) in covariances.items():
        for where in np.ndindex(alpha.shape):
            lo, hi = list(where), list(where)
            hi[0] += 1
            lo[mu] += 1
            hi[mu] += 1
            k, ell = cuts[mu]+np.ravel_multi_index(tuple(hi), shapes[mu]), cuts[mu]+np.ravel_multi_index(tuple(lo), shapes[mu])
            max_cov_error = max(max_cov_error, abs(cf[k, k]-alpha[where]),
                                abs(cf[ell, ell]-beta[where]), abs(-cf[k, ell]-rho[where]))
            # Local M is negative, and v=-x_lower. Three colors are
            # accounted for by -24 Tr(M W) on one-color full links.
            m[k, k] -= beta[where]/12
            m[ell, ell] -= alpha[where]/12
            m[k, ell] -= rho[where]/12
            m[ell, k] -= rho[where]/12
    checks = [{'type': 'dense_incidence_covariance_vs_all_mode_sum',
               'actual_maximum_error': max_cov_error, 'required_maximum_error': 1e-11,
               'passed': bool(max_cov_error < 1e-11)}]
    spectral_sigma = np.column_stack([pack(box.spectral(unpack(e), power=-1)) for e in eye])
    spectral_half = np.column_stack([pack(box.spectral(unpack(e), time=box.tau/2)) for e in eye])
    op_error = max(float(np.max(np.abs(spectral_sigma-sigma))),
                   float(np.max(np.abs(spectral_half-half_heat))))
    checks.append({'type': 'matrix_free_sigma_and_half_heat_vs_incidence',
                   'actual_maximum_error': op_error, 'required_maximum_error': 1e-11,
                   'passed': bool(op_error < 1e-11)})
    for i, q in enumerate(qs):
        left = retract @ sigma @ heat @ q @ half_heat
        right = retract @ sigma @ a @ sigma @ half_heat
        w = retract @ sigma @ heat @ q @ heat @ sigma @ a @ sigma @ retract.T
        expectation = -24*np.trace(m @ w)
        split = np.zeros((3, 3))
        direct = np.zeros(3)
        for k in range(size):
            row, drow = separated_contraction(unpack(left[:, k]), unpack(right[:, k]), covariances, n)
            split += row
            direct += drow
        factor_error = float(np.max(np.abs(left @ right.T-w)))
        trace_error = max(abs(float(split.sum())-expectation), abs(float(direct.sum())-expectation))
        checks.append({'type': 'dense_covariance_order_and_color_factor', 'probe': (3, 6)[i],
                       'actual_factorization_error': factor_error, 'actual_trace_error': trace_error,
                       'required_maximum_error': 1e-10, 'signed_loop_value': float(expectation),
                       'passed': bool(max(factor_error, trace_error) < 1e-10)})
    return checks


def original_check(n, samples, seed, destination):
    box = RelativeBox(n)
    covariances = axial_covariances(n)
    coefficient_path = destination.with_name(f'axial-signed-response-N{n}-covariances.npz')
    np.savez_compressed(coefficient_path, **{f'mu{mu+1}_{name}': array
                         for mu, values in covariances.items()
                         for name, array in zip(('alpha', 'beta', 'rho'), values)})
    checks = covariance_checks(covariances, n)
    rng = np.random.default_rng(seed)
    values, max_split_error, max_forest_entry = [], 0.0, 0.0
    for sample in range(samples):
        noise = [rng.normal(size=shape) for shape in box.shapes]
        x = box.spectral(noise, time=box.tau/2)
        right = box.retract(box.spectral(box.residual(box.spectral(x, power=-1)), power=-1), n-1)
        row = []
        for q in box.probe_matrices(x):
            left = box.retract(box.spectral(q, power=-1, time=box.tau), n-1)
            split, direct = separated_contraction(left, right, covariances, n)
            max_split_error = max(max_split_error, float(np.max(np.abs(split.sum(axis=1)-direct))))
            max_forest_entry = max(max_forest_entry, float(np.max(np.abs(left[0][:-1]))),
                                   float(np.max(np.abs(right[0][:-1]))))
            row.append(split)
        values.append(row)
        if (sample+1) % 16 == 0 or sample+1 == samples:
            print(f'N={n}, samples={sample+1}/{samples}, loop means={np.array(values).sum(axis=(2, 3)).mean(axis=0).tolist()}', flush=True)
    data = np.array(values)  # sample, probe, plane, contribution
    pieces = data.sum(axis=2)
    totals = pieces.sum(axis=2)
    checks.append({'type': 'every_sample_split_and_frozen_axial_entries', 'N': n,
                   'actual_maximum_split_error': max_split_error,
                   'actual_maximum_frozen_entry': max_forest_entry, 'required_maximum_error': 1e-9,
                   'passed': bool(max(max_split_error, max_forest_entry) < 1e-9)})
    checks.append({'type': 'all_samples_finite', 'N': n,
                   'passed': bool(np.isfinite(data).all())})
    summary = {'N': n, 'a': box.a, 'tau': box.tau, 'samples': samples, 'seed': seed,
               'admitted_support_vertex_ranges': box.support_indices,
               'number_of_interior_axial_plaquettes': sum(v[0].size for v in covariances.values()),
               'probes': [3, 6], 'pieces': ['common_path', 'mixed', 'curvature'],
               'loop_means': totals.mean(axis=0).tolist(),
               'loop_standard_errors': (totals.std(axis=0, ddof=1)/np.sqrt(samples)).tolist(),
               'piece_means': pieces.mean(axis=0).tolist(),
               'piece_standard_errors': (pieces.std(axis=0, ddof=1)/np.sqrt(samples)).tolist(),
               'piece_sample_covariances': [np.cov(pieces[:, i], rowvar=False).tolist() for i in (0, 1)],
               'full_covariance_coefficients': str(coefficient_path),
               'individual_samples_by_probe_plane_piece': data.tolist(),
               'qualification': 'Unbiased finite-mesh trace samples in exact arithmetic; floating-point implementation; standard errors have no confidence guarantee; no certified sign, bound or asymptotic.'}
    return summary, checks


def audit_stored_evidence(path):
    result = json.loads(path.read_text())
    audit = []
    for mesh in result['meshes']:
        data = np.asarray(mesh['individual_samples_by_probe_plane_piece'])
        pieces, samples = data.sum(axis=2), mesh['samples']
        totals = pieces.sum(axis=2)
        defects = [np.max(np.abs(pieces.mean(axis=0)-mesh['piece_means'])),
                   np.max(np.abs(pieces.std(axis=0, ddof=1)/np.sqrt(samples)-mesh['piece_standard_errors'])),
                   np.max(np.abs(totals.mean(axis=0)-mesh['loop_means'])),
                   np.max(np.abs(totals.std(axis=0, ddof=1)/np.sqrt(samples)-mesh['loop_standard_errors']))]
        with np.load(mesh['full_covariance_coefficients']) as archive:
            shapes = {key: list(archive[key].shape) for key in archive.files}
            finite = all(np.isfinite(archive[key]).all() for key in archive.files)
        audit.append({'type': 'complete_stored_samples_and_coefficient_archive',
                      'N': mesh['N'], 'sample_shape': list(data.shape),
                      'actual_maximum_summary_defect': float(max(defects)),
                      'required_maximum_defect': 1e-12, 'finite_coefficients': bool(finite),
                      'coefficient_shapes': shapes,
                      'passed': bool(max(defects) <= 1e-12 and finite)})
        print(f'N={mesh["N"]}: all {data.size} stored sample components checked; '
              f'summary defect={max(defects)}, required<=1e-12; coefficients finite={finite}.', flush=True)
    result['stored_evidence_audit'] = audit
    path.write_text(json.dumps(result, indent=2)+'\n')
    assert all(item['passed'] for item in audit)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--N', type=int, nargs='+', default=[24, 32])
    parser.add_argument('--samples', type=int, default=128)
    parser.add_argument('--seed', type=int, default=3705)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('axial-signed-response-certificate.json'))
    args = parser.parse_args()
    assert args.samples >= 2
    result = {'scope': 'Only L027 interior-axial one-internal-action-pair class, actual probes at admitted meshes.',
              'full_Gamma_evaluated': False, 'logarithmic_coefficient_established': False,
              'required_asymptotic_threshold': 'A mesh-independent bound would exclude a logarithm in this selected class; no such bound is certified.',
              'checks': dense_check(), 'meshes': []}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    for n in args.N:
        mesh, checks = original_check(n, args.samples, args.seed+n, args.output)
        result['meshes'].append(mesh)
        result['checks'].extend(checks)
        args.output.write_text(json.dumps(result, indent=2)+'\n')
        print(f'N={n}: means={mesh["loop_means"]}, standard errors={mesh["loop_standard_errors"]}; target=uniform bound (unproved).', flush=True)
    failures = [check for check in result['checks'] if not check['passed']]
    result['failures'] = failures
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Checks={len(result["checks"])}, failures={len(failures)}; certificate={args.output}', flush=True)
    if failures:
        print(json.dumps(failures, indent=2), flush=True)
        raise SystemExit(1)
    audit_stored_evidence(args.output)


if __name__ == '__main__':
    main()
