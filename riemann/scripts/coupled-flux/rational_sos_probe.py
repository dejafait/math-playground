"""Bounded floating SOS feasibility probe; never an exact certificate.

Run from riemann: python3 scripts/coupled-flux/rational_sos_probe.py
Only NumPy and the standard library are used. Full iterates, coefficient
maps and residuals are saved locally. Exact rational polynomial maps are
constructed before conversion to floating point.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import json
import math
import time
import numpy as np

ROOT = Path(__file__).resolve().parent


def monomials(n, d):
    if n == 1:
        return [(d,)]
    return [(k,) + a for k in range(d + 1) for a in monomials(n - 1, d - k)]


def add(a, b, scale=F(1)):
    c = a.copy()
    for m, x in b.items():
        c[m] = c.get(m, F(0)) + scale * x
    return {m: x for m, x in c.items() if x}


def mul(a, b):
    c = {}
    for m, x in a.items():
        for n, y in b.items():
            k = tuple(i + j for i, j in zip(m, n))
            c[k] = c.get(k, F(0)) + x * y
    return {m: x for m, x in c.items() if x}


def var(i):
    m = [0] * 6
    m[i] = 1
    return {tuple(m): F(1)}


def derivative(p):
    c = {}
    # t=(x,4y,8z,X,4Y,8Z); dot state=(t1/4,t2/2,t4/4,t5/2).
    for i, j, scale in [(0, 1, F(1, 4)), (1, 2, F(1, 2)),
                        (3, 4, F(1, 4)), (4, 5, F(1, 2))]:
        for m, x in p.items():
            if m[i]:
                n = list(m)
                n[i] -= 1
                n[j] += 1
                n = tuple(n)
                c[n] = c.get(n, F(0)) + x * m[i] * scale
    return {m: x for m, x in c.items() if x}


def spectral_matrix():
    # Integral Taylor polynomial, exact rational before floating conversion.
    scales = [1, 4, 8, 1, 4, 8]
    k = []
    errs = []
    for a in range(6):
        r, j = divmod(a, 3)
        row, erow = [], []
        for b in range(6):
            s, l = divmod(b, 3)
            value = F(0)
            for n in range(25):
                d = j + l + n
                if d % 2 == 0:
                    sign = -1 if ((j - l + n) // 2) % 2 else 1
                    value += F(sign * (r - s) ** n,
                               math.factorial(n) * 2 ** d * (d + 1))
            value *= scales[a] * scales[b]
            err = F(0) if r == s else F(2 * scales[a] * scales[b],
                       math.factorial(25) * 2 ** (j + l + 25) * (j + l + 26))
            row.append(value)
            erow.append(err)
        k.append(row)
        errs.append(erow)
    return k, errs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--iterations', type=int, default=12000)
    parser.add_argument('--suffix', default='')
    parser.add_argument('--warm-start', action='store_true')
    args = parser.parse_args()
    started = time.monotonic()
    vs = [var(i) for i in range(6)]
    q = {}
    for i, c in [(0, F(1, 2)), (1, F(3, 8)), (3, F(1, 2)), (4, F(3, 8))]:
        q = add(q, mul(vs[i], vs[i]), c)
    q2 = mul(q, q)
    dq = derivative(q)
    observable = add(mul(vs[0], vs[2]), mul(vs[1], vs[1]), -F(1, 2))
    observable = {m: x / 8 for m, x in observable.items()}
    basis = [m for m in monomials(6, 3) if m[2] + m[5] <= 1]
    forms = [m for m in monomials(6, 6) if m[2] + m[5] <= 2]
    p_basis = [m for m in monomials(6, 4) if m[2] == m[5] == 0]
    h_basis = [(i, j) for i in range(6) for j in range(i, 6)]
    pairs = [(i, j) for i in range(len(basis)) for j in range(i, len(basis))]
    index = {m: i for i, m in enumerate(forms)}
    ng, nh, np_ = len(pairs), len(h_basis), len(p_basis)
    nf = len(forms)
    nvars = 2 * ng + nh + np_ + 1
    a = np.zeros((2 * nf + 1, nvars))
    b = np.zeros(2 * nf + 1)
    sqrt2 = math.sqrt(2)
    for branch in range(2):
        off = branch * nf
        for t, (i, j) in enumerate(pairs):
            m = tuple(x + y for x, y in zip(basis[i], basis[j]))
            a[off + index[m], branch * ng + t] = 1 if i == j else sqrt2
        for t, (i, j) in enumerate(h_basis):
            poly = mul(q2, mul(vs[i], vs[j]))
            for m, val in poly.items():
                a[off + index[m], 2 * ng + t] = -float(val) * (1 if i == j else 2)
        for t, m in enumerate(p_basis):
            p = {m: F(1)}
            # Gram - q^2 tHt + q DP - P Dq = -branch*q^2 Q.
            poly = add(mul(q, derivative(p)), mul(p, dq), -F(1))
            for n, val in poly.items():
                a[off + index[n], 2 * ng + nh + t] = float(val)
        for m, val in mul(q2, observable).items():
            b[off + index[m]] = -branch * float(val)
    k_exact, k_error = spectral_matrix()
    k = np.array([[float(x) for x in row] for row in k_exact])
    target = F(1, 300)  # A successful exact recovery here would beat 1/288.
    for t, (i, j) in enumerate(h_basis):
        a[-1, 2 * ng + t] = k[i, j] * (1 if i == j else 2)
    a[-1, -1] = 1
    b[-1] = float(target)
    # Invertible scaling of unrestricted variables and constraint rows.
    columns = np.ones(nvars)
    for j in range(2 * ng, nvars - 1):
        norm = np.linalg.norm(a[:, j])
        if norm:
            columns[j] = 1 / norm
    a *= columns[None, :]
    rows = 1 / np.linalg.norm(a, axis=1)
    a *= rows[:, None]
    b *= rows
    vals, vecs = np.linalg.eigh(a @ a.T)
    keep = vals > 1e-11 * vals[-1]
    inverse = (vecs[:, keep] / vals[keep]) @ vecs[:, keep].T
    projector = a.T @ inverse
    discarded_rhs = float(np.linalg.norm(vecs[:, ~keep].T @ b))
    pair_i = np.array([i for i, j in pairs])
    pair_j = np.array([j for i, j in pairs])
    weights = np.array([1 if i == j else sqrt2 for i, j in pairs])

    def unpack(g):
        matrix = np.zeros((len(basis), len(basis)))
        matrix[pair_i, pair_j] = g / weights
        matrix[pair_j, pair_i] = g / weights
        return matrix

    def cone(x):
        z = x.copy()
        for branch in range(2):
            off = branch * ng
            ev, evec = np.linalg.eigh(unpack(x[off:off + ng]))
            mat = (evec * np.maximum(ev, 0)) @ evec.T
            z[off:off + ng] = mat[pair_i, pair_j] * weights
        z[-1] = max(z[-1], 0)
        return z

    x = np.zeros(nvars)
    if args.warm_start:
        x = np.load(ROOT / 'rational_sos_probe_maps.npz')['best_affine'].copy()
    logs = []
    best = None
    for iteration in range(1, args.iterations + 1):
        z = cone(x)
        reflected = 2 * z - x
        affine = reflected + projector @ (b - a @ reflected)
        x += affine - z
        if iteration == 1 or iteration % 250 == 0:
            residual = float(np.linalg.norm(a @ z - b))
            minimum = min(float(np.linalg.eigvalsh(unpack(affine[j*ng:(j+1)*ng]))[0]) for j in range(2))
            gap = float(np.linalg.norm(affine - z))
            rec = dict(iteration=iteration, scaled_constraint_l2=residual,
                       affine_min_eigenvalue=minimum, projection_gap=gap,
                       elapsed_seconds=time.monotonic() - started)
            logs.append(rec)
            if best is None or residual < best[0]:
                best = (residual, z.copy(), affine.copy(), rec.copy())
            if residual < 1e-9 or time.monotonic() - started > 160:
                break
    residual, best_cone, best_affine, best_record = best
    decoded = best_cone * columns
    h = np.zeros((6, 6))
    for val, (i, j) in zip(decoded[2 * ng:2 * ng + nh], h_basis):
        h[i, j] = h[j, i] = val
    output = dict(
        kind='floating_sos_feasibility_probe_not_a_proof',
        target_cost=str(target), required_cost='strictly below 1/288',
        coordinates='t=(x,4y,8z,X,4Y,8Z)',
        q={str(m): str(c) for m, c in q.items()},
        basis=basis, polynomial_basis=p_basis, coefficient_basis=forms,
        spectral_matrix=[[str(x) for x in row] for row in k_exact],
        spectral_entry_error=[[str(x) for x in row] for row in k_error],
        affine_rank=int(sum(keep)), affine_rows=len(b),
        discarded_rhs_norm=discarded_rhs, map_largest_eigenvalue=float(vals[-1]),
        best_record=best_record, log=logs, H=h.tolist(),
        P_coefficients=decoded[2 * ng + nh:-1].tolist(),
        cost_float=float(np.sum(h * k)), slack_float=float(decoded[-1]),
        gram_0=unpack(best_cone[:ng]).tolist(),
        gram_1=unpack(best_cone[ng:2*ng]).tolist(),
        affine_candidate=(best_affine * columns).tolist(),
        failures=['No exact PSD or coefficient identity certificate.',
                  'A nonzero residual does not exclude the SOS subclass or the full rational family.',
                  'All calculations after rational map construction use binary floating point.'],
        iterations=iteration, elapsed_seconds=time.monotonic() - started)
    stem = 'rational_sos_probe' + args.suffix
    path = ROOT / (stem + '.json')
    path.write_text(json.dumps(output, indent=2) + '\n')
    np.savez_compressed(ROOT / (stem + '_maps.npz'), A=a, b=b,
                        columns=columns, rows=rows, best_cone=best_cone,
                        best_affine=best_affine)
    print(json.dumps({k: output[k] for k in ['kind','target_cost','required_cost',
        'affine_rank','affine_rows','discarded_rhs_norm','best_record',
        'cost_float','slack_float','iterations','elapsed_seconds','failures']}, indent=2))
    print('Full evidence:', path.relative_to(ROOT.parent.parent))
    print('Full maps:', (ROOT / (stem + '_maps.npz')).relative_to(ROOT.parent.parent))


if __name__ == '__main__':
    main()
