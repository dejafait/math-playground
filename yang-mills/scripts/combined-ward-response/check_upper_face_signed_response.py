"""L029 six-channel finite-mesh diagnostic; not the full Ward coefficient.

Deterministic low-mode traces have explicit (usually very large) norm
tail bounds. Full-mode randomized traces have empirical standard errors,
not confidence guarantees. Full evidence is saved, with bounded output.
"""
import argparse
import json
from pathlib import Path

import numpy as np

from haar_contraction import RelativeBox, PLANES, gradient
from check_axial_signed_response import tensor_sum

PIECES = ['HH', 'LL', 'dd', 'HL', 'Hd', 'Ld']


def bases(n):
    vertex = np.sqrt(2/n)*np.sin(np.pi*np.outer(np.arange(1, n), np.arange(1, n))/n)
    edge = np.sqrt(2/n)*np.cos(np.pi*np.outer(np.arange(n)+0.5, np.arange(n))/n)
    edge[:, 0] = 1/np.sqrt(n)
    return vertex, edge


def top_coordinates(fields, mu):
    axial = fields[0][-1]
    axis = mu-1
    pads = [(0, 0)]*3
    pads[axis] = (1, 1)
    extended = np.pad(axial, pads)
    low, high = [slice(None)]*3, [slice(None)]*3
    low[axis], high[axis] = slice(0, -1), slice(1, None)
    a, b = extended[tuple(low)], extended[tuple(high)]
    t = fields[mu][-1]
    return (a+b)/2, a-b, a-b-t


def covariances(n):
    vertex, edge = bases(n)
    padded = np.pad(vertex, ((1, 1), (0, 0)))
    lower, upper = padded[:-1], padded[1:]
    eig = 4*np.sin(np.pi*np.arange(1, n)/(2*n))**2
    inv3 = 1/(eig[:, None, None]+eig[None, :, None]+eig[None, None, :])
    result = {}
    for mu in (1, 2, 3):
        factors = [vertex**2 for _ in range(3)]
        greens = []
        for product in (lower**2, upper**2, lower*upper):
            factors[mu-1] = product
            greens.append(tensor_sum(inv3, factors))
        aa, bb, ab = (n*g for g in greens)
        h, l, b = (aa+bb+2*ab)/4, aa+bb-2*ab, (aa-bb)/2
        e = np.zeros_like(h)
        for component in (0, mu):
            modes = [np.arange(n) if r == component else np.arange(1, n) for r in range(4)]
            eigen = np.zeros(tuple(len(k) for k in modes))
            for axis, k in enumerate(modes):
                shape = [1]*4
                shape[axis] = len(k)
                eigen += (4*np.sin(np.pi*k/(2*n))**2).reshape(shape)
            factors = [vertex**2 for _ in range(4)]
            factors[0] = (edge[-1:]**2 if component == 0 else vertex[-1:]**2)
            factors[mu] = ((lower-upper)**2 if component == 0 else edge**2)
            e += tensor_sum(1/eigen, factors)[0]
        result[mu] = dict(h=h, l=l, b=b, e=e, c=b/n, f=l/n)
    return result


def coefficients(cov):
    h, l, b, e, c, f = (cov[key] for key in ('h', 'l', 'b', 'e', 'c', 'f'))
    return (l/4-f/3, h/4-e/12, -l/12,
            -b/2+c/3, b/3, f/6-h/3)


def contraction(left, right, covs):
    rows = []
    direct_defect = 0.0
    for mu, cov in covs.items():
        y, z = top_coordinates(left, mu), top_coordinates(right, mu)
        kh, kl, kd, khl, khd, kld = coefficients(cov)
        terms = [kh*y[0]*z[0], kl*y[1]*z[1], kd*y[2]*z[2],
                 khl*(y[0]*z[1]+y[1]*z[0])/2,
                 khd*(y[0]*z[2]+y[2]*z[0])/2,
                 kld*(y[1]*z[2]+y[2]*z[1])/2]
        row = -24*np.array([v.sum() for v in terms])
        # Assemble the symmetric M independently of the split summation.
        mz = [kh*z[0]+khl*z[1]/2+khd*z[2]/2,
              khl*z[0]/2+kl*z[1]+kld*z[2]/2,
              khd*z[0]/2+kld*z[1]/2+kd*z[2]]
        direct = -24*sum(np.sum(v*w) for v, w in zip(y, mz))
        direct_defect = max(direct_defect, abs(row.sum()-direct))
        rows.append(row)
    return np.array(rows), direct_defect


def one_column(box, x, covs):
    right = box.retract(box.spectral(box.residual(box.spectral(x, power=-1)), power=-1), box.n-1)
    rows, defect = [], 0.0
    for q in box.probe_matrices(x):
        left = box.retract(box.spectral(q, power=-1, time=box.tau), box.n-1)
        row, error = contraction(left, right, covs)
        rows.append(row)
        defect = max(defect, error)
    return np.array(rows), defect


def dense_check():
    n = 4
    box = RelativeBox(n, sample=True)
    covs = covariances(n)
    sizes = [int(np.prod(s)) for s in box.shapes]
    cuts = np.cumsum([0, *sizes])
    size = int(cuts[-1])
    def unpack(v):
        return [v[cuts[mu]:cuts[mu+1]].reshape(box.shapes[mu]) for mu in range(4)]
    def pack(v):
        return np.concatenate([x.ravel() for x in v])
    eye = np.eye(size)
    curl = np.column_stack([np.concatenate([v.ravel() for v in box.curl(unpack(e)).values()]) for e in eye])
    d0 = np.column_stack([pack([gradient(e.reshape(box.vertex_shape), mu) for mu in range(4)])
                          for e in np.eye((n-1)**4)])
    delta = curl.T@curl+d0@d0.T
    sigma = np.linalg.inv(delta)
    eig, waves = np.linalg.eigh(delta)
    heat = (waves*np.exp(-box.tau*eig/box.a**2))@waves.T
    half = (waves*np.exp(-box.tau*eig/(2*box.a**2)))@waves.T
    forest = np.column_stack([pack(box.retract(unpack(e), n-1)) for e in eye])
    a = np.column_stack([pack(box.residual(unpack(e))) for e in eye])
    cf = forest@sigma@forest.T
    m = np.zeros((size, size))
    cov_error = 0.0
    for mu, cov in covs.items():
        j = np.array([top_coordinates(unpack(e), mu) for e in eye]).transpose(1, 2, 3, 4, 0)
        cc = np.einsum('a...k,kl,b...l->ab...', j, cf, j)
        expected = ((cov['h'], cov['b'], cov['c']),
                    (cov['b'], cov['l'], cov['f']), (cov['c'], cov['f'], cov['e']))
        cov_error = max(cov_error, max(np.max(np.abs(cc[r, s]-expected[r][s])) for r in range(3) for s in range(3)))
        kh, kl, kd, khl, khd, kld = coefficients(cov)
        entries = ((kh, khl/2, khd/2), (khl/2, kl, kld/2), (khd/2, kld/2, kd))
        for r in range(3):
            for s in range(3):
                jr, js = j[r].reshape(-1, size), j[s].reshape(-1, size)
                m += jr.T @ (entries[r][s].reshape(-1, 1)*js)
    checks = [dict(type='complete_dense_incidence_vs_six_covariances', actual_maximum_error=float(cov_error),
                   required_maximum_error=1e-11, passed=bool(cov_error < 1e-11))]
    noise = np.random.default_rng(4104).normal(size=size)
    sigma_error = np.max(np.abs(pack(box.spectral(unpack(noise), power=-1))-sigma@noise))
    half_error = np.max(np.abs(pack(box.spectral(unpack(noise), time=box.tau/2))-half@noise))
    original_column, _ = one_column(box, unpack(half@noise), covs)
    checks.append(dict(type='matrix_free_sigma_and_half_heat_vs_dense_incidence',
                       actual_maximum_error=float(max(sigma_error, half_error)), required_maximum_error=1e-11,
                       passed=bool(max(sigma_error, half_error) < 1e-11)))
    for i in (0, 1):
        q = np.column_stack([pack(box.probe_matrices(unpack(e))[i]) for e in eye])
        w = forest@sigma@heat@q@heat@sigma@a@sigma@forest.T
        actual = -24*np.trace(m@w)
        left, right = forest@sigma@heat@q@half, forest@sigma@a@sigma@half
        rows = np.zeros((3, 6))
        split_defect = 0.0
        for k in range(size):
            row, defect = contraction(unpack(left[:, k]), unpack(right[:, k]), covs)
            rows += row
            split_defect = max(split_defect, defect)
        trace_error = abs(rows.sum()-actual)
        factor_error = np.max(np.abs(left@right.T-w))
        column, _ = contraction(unpack(left@noise), unpack(right@noise), covs)
        column_error = np.max(np.abs(column-original_column[i]))
        checks.append(dict(type='complete_dense_trace_order_sign_color_and_split', probe=(3, 6)[i],
                           actual_trace_error=float(trace_error), actual_factorization_error=float(factor_error),
                           actual_matrix_free_column_error=float(column_error),
                           actual_split_error=split_defect, signed_trace=float(actual),
                           required_maximum_error=1e-10, passed=bool(max(trace_error, factor_error, split_defect, column_error) < 1e-10)))
    return checks


def norm_tail_bounds(box, covs, selected):
    # Dimensionless operator bounds, explained in L029's diagnostic section.
    q3 = 16*max(float(np.max(np.abs(v))) for v in box.triplet_weights.values())
    rows = {p: np.zeros(box.vertex_shape) for p in PLANES}
    for mu, nu in PLANES:
        for alpha in range(4):
            if alpha not in (mu, nu):
                rows[tuple(sorted((mu, alpha)))] += np.abs(box.s[mu, nu])/2
                rows[tuple(sorted((nu, alpha)))] += np.abs(box.s[mu, nu])/2
    q6 = 16*max(float(np.max(v)) for v in rows.values())
    umax = np.sqrt(np.max(sum(v*v for v in box.u)))
    residual = 64*umax/box.a+q3+q6
    sigma = 1/min(float(v.min()) for v in box.lambdas)
    m = np.zeros(6)
    for cov in covs.values():
        m = np.maximum(m, [float(np.max(np.abs(v)))/(1 if j < 3 else 2)
                           for j, v in enumerate(coefficients(cov))])
    heat_trace = sum(float(np.exp(-box.tau*v/box.a**2).sum()) for v in box.lambdas)
    tail = heat_trace-sum(np.exp(-box.tau*value/box.a**2) for _, _, value in selected)
    bounds = [24*q*sigma**3*residual*(1+4*box.n)**2*33*m*tail for q in (q3, q6)]
    return dict(heat_trace=heat_trace, omitted_heat_trace=float(tail),
                retained_heat_trace_fraction=float(1-tail/heat_trace),
                Q_norm_upper_bounds=[q3, q6], residual_norm_upper_bound=float(residual),
                sigma_norm=float(sigma), forest_norm_upper_bound=1+4*box.n,
                local_piece_M_norm_upper_bounds=m.tolist(),
                channel_tail_bounds=np.array(bounds).tolist(),
                total_tail_bounds=np.array(bounds).sum(axis=1).tolist(),
                qualification='Analytic norm formulas; numerical evaluations use binary64, without interval rounding certificate.')


def calculate(n, samples, cutoff, seed, path):
    box = RelativeBox(n)
    covs = covariances(n)
    archive = path.with_name(f'upper-face-signed-response-N{n}-covariances.npz')
    np.savez_compressed(archive, **{f'mu{mu+1}_{name}': array for mu, cov in covs.items() for name, array in cov.items()})
    checks = []
    for mu, cov in covs.items():
        h, l, b, e, c, f = (cov[key] for key in ('h', 'l', 'b', 'e', 'c', 'f'))
        matrices = np.empty((*h.shape, 3, 3))
        for r, row in enumerate(((h, b, c), (b, l, f), (c, f, e))):
            for s, v in enumerate(row):
                matrices[..., r, s] = v
        margins = dict(h_min=float(h.min()), h_upper=float((6*n-h).min()), l_min=float(l.min()),
                       l_upper=float((n-l).min()), e_min=float(e.min()), e_upper=float((1-e).min()),
                       interior_l_lower=float((np.take(l, np.arange(1, n-1), axis=mu-1)-n/6).min()),
                       covariance_minimum_eigenvalue=float(np.linalg.eigvalsh(matrices).min()))
        checks.append(dict(type='full_grid_covariance_bounds_and_positive_semidefiniteness', N=n, plane=[1, mu+1],
                           actual_minimum_margins=margins, required_minimum_margin=-1e-10,
                           passed=bool(min(margins.values()) >= -1e-10)))
    selected = [(mu, tuple(int(k) for k in index), float(eigen[index])) for mu, eigen in enumerate(box.lambdas)
                for index in zip(*np.nonzero(eigen/box.a**2 <= cutoff))]
    selected.sort(key=lambda item: (item[2], item[0], item[1]))
    vertex, edge = bases(n)
    deterministic, mode_rows, max_defect = np.zeros((2, 3, 6)), [], 0.0
    for count, (mu, index, eigen) in enumerate(selected, 1):
        x = box.zeros()
        value = np.ones(box.shapes[mu])*np.exp(-box.tau*eigen/(2*box.a**2))
        for axis, k in enumerate(index):
            vector = (edge if axis == mu else vertex)[:, k]
            shape = [1]*4
            shape[axis] = len(vector)
            value *= vector.reshape(shape)
        x[mu] = value
        row, defect = one_column(box, x, covs)
        deterministic += row
        mode_rows.append(dict(component=mu+1, physical_mode_indices=[k if axis == mu else k+1 for axis, k in enumerate(index)],
                              eigenvalue_physical=eigen/box.a**2, signed_channels=row.tolist()))
        max_defect = max(max_defect, defect)
        if count % 8 == 0 or count == len(selected):
            print(f'N={n}, deterministic modes={count}/{len(selected)}', flush=True)
    tail = norm_tail_bounds(box, covs, selected)
    tail['required_total_tail_bounds_for_sign'] = np.abs(deterministic.sum(axis=(1, 2))).tolist()
    tail['sign_tail_thresholds_met'] = [actual < required for actual, required in
                                      zip(tail['total_tail_bounds'], tail['required_total_tail_bounds_for_sign'])]
    rng, values = np.random.default_rng(seed+n), []
    for sample in range(samples):
        noise = [rng.normal(size=shape) for shape in box.shapes]
        x = box.spectral(noise, time=box.tau/2)
        row, defect = one_column(box, x, covs)
        values.append(row)
        max_defect = max(max_defect, defect)
        if (sample+1) % 16 == 0 or sample+1 == samples:
            print(f'N={n}, full-mode samples={sample+1}/{samples}', flush=True)
    data = np.array(values)
    pieces, totals = data.sum(axis=2), data.sum(axis=(2, 3))
    se = pieces.std(axis=0, ddof=1)/np.sqrt(samples)
    checks.append(dict(type='all_columns_split_and_finite', N=n, actual_maximum_split_error=max_defect,
                       required_maximum_error=1e-8, passed=bool(max_defect < 1e-8 and np.isfinite(data).all())))
    mesh = dict(N=n, a=box.a, tau=box.tau, samples=samples, seed=seed+n,
                admitted_support_vertex_ranges=box.support_indices,
                upper_face_plaquettes=sum(cov['h'].size for cov in covs.values()),
                full_covariance_coefficients=str(archive.resolve().relative_to(Path.cwd())), deterministic_cutoff_physical=cutoff,
                deterministic_modes=mode_rows, deterministic_piece_sums=deterministic.sum(axis=1).tolist(),
                deterministic_totals=deterministic.sum(axis=(1, 2)).tolist(), deterministic_tail=tail,
                piece_means=pieces.mean(axis=0).tolist(), piece_standard_errors=se.tolist(),
                total_means=totals.mean(axis=0).tolist(), total_standard_errors=(totals.std(axis=0, ddof=1)/np.sqrt(samples)).tolist(),
                a_squared_total_means=(box.a**2*totals.mean(axis=0)).tolist(),
                piece_sample_covariances=[np.cov(pieces[:, i], rowvar=False).tolist() for i in (0, 1)],
                individual_samples_by_probe_plane_piece=data.tolist(),
                qualification='Full-mode unbiased Gaussian trace diagnostic in exact arithmetic; binary64 implementation; empirical standard errors have no confidence guarantee. No cutoff fit.')
    return mesh, checks


def audit(mesh):
    data = np.array(mesh['individual_samples_by_probe_plane_piece'])
    pieces, totals, n = data.sum(axis=2), data.sum(axis=(2, 3)), mesh['samples']
    deterministic = np.array([mode['signed_channels'] for mode in mesh['deterministic_modes']]).sum(axis=0)
    defects = [np.max(np.abs(pieces.mean(axis=0)-mesh['piece_means'])),
               np.max(np.abs(pieces.std(axis=0, ddof=1)/np.sqrt(n)-mesh['piece_standard_errors'])),
               np.max(np.abs(totals.mean(axis=0)-mesh['total_means'])),
               np.max(np.abs(totals.std(axis=0, ddof=1)/np.sqrt(n)-mesh['total_standard_errors'])),
               np.max(np.abs(deterministic.sum(axis=1)-mesh['deterministic_piece_sums']))]
    with np.load(mesh['full_covariance_coefficients']) as archive:
        finite = all(np.isfinite(archive[key]).all() for key in archive.files)
        shapes = {key: list(archive[key].shape) for key in archive.files}
    return dict(type='complete_stored_samples_modes_and_covariances', N=mesh['N'], actual_maximum_summary_defect=float(max(defects)),
                required_maximum_error=1e-12, all_covariances_finite=bool(finite), covariance_shapes=shapes,
                passed=bool(max(defects) < 1e-12 and finite))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--N', type=int, nargs='+', default=[24, 32])
    parser.add_argument('--samples', type=int, default=64)
    parser.add_argument('--cutoff', type=float, default=1.1)
    parser.add_argument('--seed', type=int, default=4105)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('upper-face-signed-response-certificate.json'))
    args = parser.parse_args()
    assert args.samples >= 2
    result = dict(scope='L029 complete upper-face one-internal-action-pair class only', probes=[3, 6], pieces=PIECES,
                  full_Gamma_evaluated=False, logarithmic_coefficient_established=False,
                  required_threshold='A resolved full signed trace is needed before choosing cancellation/asymptotic work; no finite-mesh fit proves a logarithm.',
                  checks=dense_check(), meshes=[])
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    for n in args.N:
        mesh, checks = calculate(n, args.samples, args.cutoff, args.seed, args.output)
        result['meshes'].append(mesh)
        result['checks'].extend(checks)
        result['checks'].append(audit(mesh))
        args.output.write_text(json.dumps(result, indent=2)+'\n')
        print(f'N={n}: full-mode means={mesh["total_means"]}, empirical SE={mesh["total_standard_errors"]}; '
              f'deterministic={mesh["deterministic_totals"]}, required tail bounds < '
              f'{np.abs(mesh["deterministic_totals"]).tolist()} for a deterministic sign; '
              f'actual tail bounds={mesh["deterministic_tail"]["total_tail_bounds"]}', flush=True)
    result['failures'] = [check for check in result['checks'] if not check['passed']]
    result['diagnostic_threshold_failures'] = [
        dict(N=mesh['N'], probe=probe, threshold='omitted trace bound < absolute deterministic total',
             actual_tail_bound=actual, required_tail_bound_below=required)
        for mesh in result['meshes']
        for probe, actual, required, passed in zip((3, 6), mesh['deterministic_tail']['total_tail_bounds'],
            mesh['deterministic_tail']['required_total_tail_bounds_for_sign'], mesh['deterministic_tail']['sign_tail_thresholds_met'])
        if not passed]
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Checks={len(result["checks"])}, failures={len(result["failures"])}; certificate={args.output}', flush=True)
    print(f'Deterministic sign-tail threshold failures={len(result["diagnostic_threshold_failures"])}; '
          'consistency checks do not certify a signed response.', flush=True)
    if result['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
