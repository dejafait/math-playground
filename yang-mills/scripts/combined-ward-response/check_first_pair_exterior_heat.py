"""Full-spectrum sampling of a specified L070 exterior/axial diagnostic.

This is not the original pinned trace or its asymptotic coefficient.
The N=4 dense check uses a one-site displacement, not an admitted mesh.
Every actual-probe sample is retained. No statistical sign is certified.
"""
import argparse
import json
from pathlib import Path

import numpy as np
from haar_contraction import RelativeBox, average, gradient


def upper_rows(box, x):
    # Positive (1,mu) upper curvature, averaged to transverse vertices.
    curls = box.curl(x)
    return [average(curls[0, mu], mu)[-1] / box.a**2
            for mu in (1, 2, 3)]


def right_rows(box, x):
    lifted = box.retract(x, box.n-1)
    # Retain all interior axial levels and all pinned transverse end edges.
    return [average(lifted[mu], mu) / box.a for mu in (1, 2, 3)]


def pairing(box, x, y):
    top = upper_rows(box, x)
    right = right_rows(box, y)
    level = box.a * np.arange(1, box.n)[:, None, None, None]
    weight = box.u[0] * level
    return box.a**4 * sum(float(np.sum(weight * r[None] * v))
                          for r, v in zip(top, right))


def symmetric_pairing(box, x, y):
    return (pairing(box, x, y) + pairing(box, y, x)) / 2


def dense_check():
    box = RelativeBox(4, sample=True)
    sizes = [int(np.prod(s)) for s in box.shapes]
    cuts = np.cumsum([0, *sizes])
    size = int(cuts[-1])

    def unpack(v):
        return [v[cuts[j]:cuts[j+1]].reshape(box.shapes[j]) for j in range(4)]

    def pack(v):
        return np.concatenate([z.ravel() for z in v])

    eye = np.eye(size)
    curl = np.column_stack([np.concatenate([v.ravel() for v in box.curl(unpack(e)).values()])
                            for e in eye])
    vertices = np.eye((box.n-1)**4)
    d0 = np.column_stack([pack([gradient(e.reshape(box.vertex_shape), j) for j in range(4)])
                          for e in vertices])
    delta = curl.T @ curl + d0 @ d0.T
    lam, waves = np.linalg.eigh(delta)
    sigma = (waves/lam) @ waves.T
    heat = (waves*np.exp(-box.tau*lam/box.a**2)) @ waves.T
    half = (waves*np.exp(-box.tau*lam/(2*box.a**2))) @ waves.T
    q = [np.column_stack([pack(box.probe_matrices(unpack(e))[i]) for e in eye])
         for i in (0, 1)]
    # Assemble the diagnostic's bilinear matrix independently of trace sampling.
    upper = [np.column_stack([upper_rows(box, unpack(e))[j].ravel() for e in eye])
             for j in range(3)]
    right = [np.column_stack([right_rows(box, unpack(e))[j].ravel() for e in eye])
             for j in range(3)]
    level = box.a*np.arange(1, box.n)[:, None, None, None]
    weight = (box.u[0]*level).ravel()
    top_indices = np.tile(np.arange((box.n-1)**3), box.n-1)
    diagnostic = box.a**4 * sum(u[top_indices].T @ (weight[:, None]*v)
                                for u, v in zip(upper, right))
    diagnostic = (diagnostic+diagnostic.T)/2
    checks = []
    rng = np.random.default_rng(900004)
    x, y = rng.normal(size=(2, size))
    actual = symmetric_pairing(box, unpack(x), unpack(y))
    expected = float(x @ diagnostic @ y)
    error = abs(actual-expected)
    bound = 2e-11*max(1., abs(expected))
    checks.append(dict(type='centered_row_pairing_vs_dense_matrix', actual_error=error,
                       required_error=bound, passed=bool(error <= bound)))
    for i in (0, 1):
        covariance = sigma @ heat @ q[i] @ heat @ sigma
        expected = float(np.trace(diagnostic @ covariance))
        left = sigma @ heat @ q[i] @ half
        right_factor = sigma @ half
        # Sum every coordinate column, not a random trace, on this small geometry.
        total = sum(symmetric_pairing(box, unpack(left[:, j]), unpack(right_factor[:, j]))
                    for j in range(size))
        factor_error = float(np.max(np.abs(left @ right_factor.T-covariance)))
        trace_error = abs(total-expected)
        bound = 2e-11*max(1., abs(expected))
        half_fields = box.spectral(unpack(x), time=box.tau/2)
        actual_right = pack(box.spectral(half_fields, power=-1))
        actual_left = pack(box.spectral(box.probe_matrices(half_fields)[i],
                                        power=-1, time=box.tau))
        operator_error = max(float(np.max(np.abs(actual_right-right_factor @ x))),
                             float(np.max(np.abs(actual_left-left @ x))))
        checks.append(dict(type='all_column_trace_and_spectral_factorization', probe=(3, 6)[i],
                           actual_trace=total, required_trace=expected,
                           actual_trace_error=trace_error, actual_factor_error=factor_error,
                           actual_operator_error=operator_error, required_error=bound,
                           passed=bool(max(trace_error, factor_error, operator_error) <= bound)))
    return dict(scope='N=4 one-site displacement, algebra check only', checks=checks)


def sample_mesh(n, samples, seed):
    box = RelativeBox(n)
    rng = np.random.default_rng(seed)
    values = []
    for j in range(samples):
        xi = [rng.choice((-1., 1.), size=s) for s in box.shapes]
        half = box.spectral(xi, time=box.tau/2)
        right = box.spectral(half, power=-1)
        row = []
        for q in box.probe_matrices(half):
            left = box.spectral(q, power=-1, time=box.tau)
            row.append(symmetric_pairing(box, left, right))
        values.append(row)
        if (j+1) % 4 == 0:
            print(f'N={n}: retained {j+1}/{samples} paired samples', flush=True)
    data = np.asarray(values)
    return dict(N=n, a=box.a, samples=samples, seed=seed, probes=[3, 6],
                full_spectrum=True, levels=[1, n-1], support_indices=box.support_indices,
                values=data.tolist(), mean=data.mean(axis=0).tolist(),
                sample_standard_error=(data.std(axis=0, ddof=1)/np.sqrt(samples)).tolist(),
                sampling_qualification='Standard errors are estimates, not confidence or rigorous sign bounds')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--meshes', type=int, nargs='+', default=[24, 32])
    parser.add_argument('--samples', type=int, default=16)
    args = parser.parse_args()
    dense = dense_check()
    failures = [r for r in dense['checks'] if not r['passed']]
    path = Path(__file__).with_name('first-pair-exterior-heat-certificate.json')
    certificate = dict(scope='Centered exterior/axial diagnostic only; not a pinned-trace coefficient',
                       dense_check=dense, meshes=[], failures=failures,
                       required_bound='A rigorous sign or zero, and a separate pinned-trace reduction, remain required',
                       actual_bound='Floating algebra diagnostics and full-spectrum sample estimates only')
    path.write_text(json.dumps(certificate, indent=2)+'\n')
    if not failures:
        for n in args.meshes:
            mesh = sample_mesh(n, args.samples, 900000+n)
            certificate['meshes'].append(mesh)
            path.write_text(json.dumps(certificate, indent=2)+'\n')
            print(f"N={n}: mean={mesh['mean']}, sample SE={mesh['sample_standard_error']}", flush=True)
    print(f'Dense algebra failures: {len(failures)}; actual/required bounds: '
          'sample estimates / rigorous diagnostic decision plus trace reduction', flush=True)
    print('Full certificate:', path, flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
