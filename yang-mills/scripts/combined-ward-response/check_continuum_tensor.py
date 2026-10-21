"""L033 tensor/Laplace contraction; binary64 diagnostics, not sign certificates.

Reuse the existing exact weak expansion and coefficient-integral implementation.
Only O(M^2) mode tables are stored. No seven-index array is constructed here.
Full results, quadrature parameters and failures are saved to the output JSON.
"""
import argparse
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import numpy as np

from check_continuum_pure_sectors import (
    Integrals, assemble, operators,
)

TAU = 1 / 16
OMEGA2 = (np.pi / 8) ** 2
GAP = 3 * OMEGA2
PAIRS = [(0, 2), (1, 3)]


def product_terms(q, n, component):
    """Collect products exactly; each feature is an unordered monomial pair."""
    out = defaultdict(Fraction)
    left = [(d, a, b, v) for (d, cl, a, cr, b), v in q.items()
            if cl == 0 and cr == component and a[0] == 0]
    right = [(d, a, b, v) for (d, cl, a, cr, b), v in n.items()
             if cl == 0 and cr == component and a[0] == 0]
    for d, a, b, v in left:
        for e, f, g, w in right:
            keys = tuple(tuple(sorted(((d[j], a[j], b[j]),
                                      (e[j], f[j], g[j])))) for j in range(4))
            out[keys] += v * w
    return {key: value for key, value in out.items() if value}


class TensorKernel:
    def __init__(self, m, degree):
        self.m = m
        self.integrations = [Integrals(pair, m, degree) for pair in PAIRS]
        self.algebra = [operators(pair) for pair in PAIRS]
        self.products = {}
        for alpha in range(2):
            qs, n, _ = self.algebra[alpha]
            for i in range(2):
                for component in range(4):
                    self.products[alpha, i, component] = product_terms(
                        qs[i], n, component)
        self.stats = dict(
            combined_product_counts=[dict(potential=alpha, probe=[3, 6][i],
                                          component=component + 1, count=len(op))
                                     for (alpha, i, component), op in self.products.items()],
            maximum_mode_table_entries=(m + 1) ** 2,
            allocates_seven_index_array=False,
        )

    def evaluate(self, s, r):
        """Return H_i^alpha(s,r), split by zero/positive ell_1, without factor 8."""
        s, r = np.asarray(s), np.asarray(r)
        values = np.zeros((2, 2, 2, len(s), len(r)))
        for alpha in range(2):
            integ = self.integrations[alpha]
            for component in range(4):
                # Build only distinct one-dimensional pair-product tables.
                ops = [self.products[alpha, i, component] for i in range(2)]
                features = [sorted({key[j] for op in ops for key in op})
                            for j in range(4)]
                tables, positions = [], []
                for axis in range(4):
                    ks = np.array([0] if axis == 0 else range(1, self.m + 1))
                    ls = np.array(list(range(0 if axis == component else 1,
                                            self.m + 1)))
                    es = np.exp(-s[:, None] * OMEGA2 * ks[None, :] ** 2)
                    er = np.exp(-r[:, None] * OMEGA2 * ls[None, :] ** 2)
                    rows = []
                    for first, second in features[axis]:
                        product = (integ.matrix(axis, *first, component)
                                   * integ.matrix(axis, *second, component))
                        if axis == 0:
                            # Odd axial frequencies vanish by L032. Keep zero
                            # separately and all positive even frequencies.
                            zero = product * (ls == 0)[None, :]
                            positive = product * ((ls > 0) & (ls % 2 == 0))[None, :]
                            rows.append(np.stack([es @ zero @ er.T,
                                                  es @ positive @ er.T]))
                        else:
                            rows.append(es @ product @ er.T)
                    tables.append(np.asarray(rows))
                    positions.append({key: index for index, key in enumerate(features[axis])})
                for i, op in enumerate(ops):
                    keys = list(op)
                    # Bound temporary storage independently of polynomial count.
                    for start in range(0, len(keys), 32):
                        selected = keys[start:start + 32]
                        coeff = np.array([float(op[key]) for key in selected])
                        indices = [[positions[j][key[j]] for key in selected]
                                   for j in range(4)]
                        transverse = tables[1][indices[1]].copy()
                        for j in (2, 3):
                            transverse *= tables[j][indices[j]]
                        for part in range(2):
                            values[i, alpha, part] += np.einsum(
                                'p,psr,psr->sr', coeff, transverse,
                                tables[0][indices[0], part], optimize=False)
        return values


def dense_heat(m, degree, s, r):
    """Small-cutoff independent contraction using the existing dense assembly."""
    algebra = [operators(pair) for pair in PAIRS]
    integrations = [Integrals(pair, m, degree) for pair in PAIRS]
    values = np.zeros((2, 2, 2, len(s), len(r)))
    for component in range(4):
        ls = [np.arange(0 if j == component else 1, m + 1) for j in range(4)]
        ks = np.arange(1, m + 1)
        shape = (m, len(ls[1]), m, len(ls[2]), m, len(ls[3]))
        lk = OMEGA2 * (ks[:, None, None, None, None, None] ** 2
                       + ks[None, None, :, None, None, None] ** 2
                       + ks[None, None, None, None, :, None] ** 2)
        ll0 = OMEGA2 * (ls[1][None, :, None, None, None, None] ** 2
                        + ls[2][None, None, None, :, None, None] ** 2
                        + ls[3][None, None, None, None, None, :] ** 2)
        for axial_position, ell1 in enumerate(ls[0]):
            if ell1 % 2:
                continue
            ll = ll0 + OMEGA2 * ell1 ** 2
            for alpha in range(2):
                n = assemble(algebra[alpha][1], component, axial_position,
                             integrations[alpha], shape)
                for i in range(2):
                    q = assemble(algebra[alpha][0][i], component, axial_position,
                                 integrations[alpha], shape)
                    for si, st in enumerate(s):
                        for ri, rt in enumerate(r):
                            values[i, alpha, int(ell1 != 0), si, ri] += np.sum(
                                q * n * np.exp(-st * lk - rt * ll))
    return values


def time_rule(degree, panel_width, window_exponents, endpoint_levels=0):
    """Finite log-time window; no certified truncation or quadrature bound."""
    end = TAU + window_exponents / GAP
    panels = int(np.ceil(np.log(end / TAU) / panel_width))
    edges = np.linspace(0, np.log(end / TAU), panels + 1)
    if endpoint_levels:
        # Resolve narrow inverse-weight peaks at the lower endpoint without
        # refining every panel. The original rule is preserved at levels=0.
        edges = np.concatenate(([0.0], edges[1] * 2.0 **
                                np.arange(-endpoint_levels, 1), edges[2:]))
        panels = len(edges) - 1
    points, weights = np.polynomial.legendre.leggauss(degree)
    zs, ws = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        zs.extend((a + b) / 2 + (b - a) * points / 2)
        ws.extend((b - a) * weights / 2)
    times = TAU * np.exp(zs)
    dr = np.array(ws) * times
    ds = dr * (times - TAU)
    return times, ds, dr, dict(degree_per_panel=degree, panels=panels,
                              nodes=len(times), time_window=[TAU, end],
                              endpoint_levels=endpoint_levels,
                              log_time_edges=edges.tolist(),
                              gap_window_exponents=window_exponents)


def inverse_checks(m, times, ds, dr):
    # Superset of all finite-cutoff eigenvalues, not a bound between samples.
    lambdas = OMEGA2 * np.arange(3, 4 * m * m + 1)
    shifted = np.exp(-(times[:, None] - TAU) * lambdas[None, :])
    errors = [float(np.max(np.abs(ds @ shifted * lambdas ** 2 - 1))),
              float(np.max(np.abs(dr @ shifted * lambdas - 1)))]
    return dict(eigenvalue_interval=[float(lambdas[0]), float(lambdas[-1])],
                tested_squared_frequency_sums=[3, 4 * m * m],
                actual_max_relative_inverse_weight_errors=errors,
                required_max_relative_inverse_weight_error=1e-11,
                passed=max(errors) < 1e-11,
                qualification='Binary64 diagnostic at every integer frequency sum in the finite range; no rounding enclosure.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cutoffs', type=int, nargs='+', default=[4, 12])
    parser.add_argument('--coefficient-degree', type=int, default=96)
    parser.add_argument('--time-degrees', type=int, nargs='+', default=[8, 12])
    parser.add_argument('--panel-width', type=float, default=0.5)
    parser.add_argument('--window-exponents', type=float, default=80)
    parser.add_argument('--endpoint-levels', type=int, default=0)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('continuum-tensor-certificate.json'))
    args = parser.parse_args()
    result = dict(scope='Implementation of L033 for all pure-sector monomials and second-index components at finite cutoffs.',
                  qualification='Binary64 diagnostics only. No certified coefficient or time quadrature, rounding or infinite-sum sign.',
                  rigorous_sign_certified=False, actual_error_bound=None,
                  required_error_bound='At the SAME cutoff, total enclosure error plus full spectral tail < certified retained absolute value.',
                  coefficient_degree=args.coefficient_degree, heat_checks=[], rows=[], failures=[])

    def save():
        args.output.write_text(json.dumps(result, indent=2) + '\n')

    # Save before the longer contractions; preserve any partial diagnostic.
    save()
    for m in args.cutoffs:
        kernel = TensorKernel(m, args.coefficient_degree)
        if m <= 4:
            s = np.array([TAU, 0.2, 1.0])
            r = np.array([TAU, 0.35, 1.5])
            tensor = kernel.evaluate(s, r)
            dense = dense_heat(m, args.coefficient_degree, s, r)
            scaled = float(np.max(np.abs(tensor - dense) / (1 + np.abs(dense))))
            check = dict(cutoff=m, s=s.tolist(), r=r.tolist(),
                         tensor_values=tensor.tolist(), dense_values=dense.tolist(),
                         actual_max_scaled_difference=scaled,
                         required_max_scaled_difference=1e-10, passed=scaled < 1e-10)
            result['heat_checks'].append(check)
            if not check['passed']:
                result['failures'].append(dict(check='pointwise heat contraction', cutoff=m))
            save()
            print(json.dumps(dict(check='pointwise heat contraction', cutoff=m,
                                  actual=scaled, required=1e-10, passed=check['passed'], path=str(args.output))), flush=True)
        reference_paths = ['continuum-pure-sectors-certificate.json',
                           'continuum-pure-sectors-higher-certificate.json']
        refs = []
        for filename in reference_paths:
            path = Path(__file__).with_name(filename)
            if path.exists():
                refs.extend([row for row in json.loads(path.read_text())['rows']
                             if row['cutoff'] == m and row['quadrature_degree'] == args.coefficient_degree])
        reference = refs[-1] if refs else None
        previous = None
        for degree in args.time_degrees:
            times, ds, dr, rule = time_rule(degree, args.panel_width, args.window_exponents,
                                           args.endpoint_levels)
            inverses = inverse_checks(m, times, ds, dr)
            if not inverses['passed']:
                result['failures'].append(dict(check='inverse-weight diagnostic', cutoff=m, degree=degree))
                result['rows'].append(dict(cutoff=m, time_rule=rule,
                                          inverse_checks=inverses,
                                          retained_sum_skipped=True))
                save()
                print(json.dumps(dict(cutoff=m, time_degree=degree,
                                      inverse_errors=inverses['actual_max_relative_inverse_weight_errors'],
                                      required=1e-11, retained_sum_skipped=True,
                                      path=str(args.output))), flush=True)
                continue
            heat = kernel.evaluate(times, times)
            values = 8 * np.einsum('iapst,s,t->iap', heat, ds, dr, optimize=True)
            row = dict(cutoff=m, time_rule=rule, inverse_checks=inverses,
                       pure_sector_axial_parts=values.tolist(),
                       pure_values=values.sum(axis=(1, 2)).tolist(), implementation=kernel.stats)
            if reference is not None:
                sectors = np.array(reference['sector_values'])
                expected = np.stack([sectors[:, 0, 0], sectors[:, 1, 1]], axis=1)
                differences = np.abs(values - expected)
                limits = 1e-8 + 1e-9 * np.abs(expected)
                row['reference_check'] = dict(reference_cutoff=m,
                    reference_coefficient_degree=args.coefficient_degree,
                    expected_parts=expected.tolist(), actual_absolute_differences=differences.tolist(),
                    required_absolute_differences=limits.tolist(),
                    passed=bool(np.all(differences < limits)),
                    qualification='Agreement with an existing finite-sum diagnostic, not an error enclosure.')
                if not row['reference_check']['passed']:
                    result['failures'].append(dict(check='retained-sum reference', cutoff=m, degree=degree))
            if previous is not None:
                row['time_refinement_max_absolute_change'] = float(np.max(np.abs(values - previous)))
            previous = values
            result['rows'].append(row)
            save()
            print(json.dumps(dict(cutoff=m, time_degree=degree, nodes=len(times),
                                  pure_values=row['pure_values'], inverse_errors=inverses['actual_max_relative_inverse_weight_errors'],
                                  reference_passed=row.get('reference_check', {}).get('passed'),
                                  path=str(args.output))), flush=True)
    print(json.dumps(dict(failures=result['failures'], actual_error_bound=None,
                          required_error_bound=result['required_error_bound'],
                          rigorous_sign_certified=False, path=str(args.output))))


if __name__ == '__main__':
    main()
