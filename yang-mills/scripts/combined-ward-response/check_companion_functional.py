"""L045 companion diagnostic; finite spectral/time/quadrature refinements only.

Full evidence goes to disk. No rounding, spectral-tail or quadrature enclosure
is claimed. Integrate coefficient derivatives by parts using the exact weak
forms already implemented for L032; never differentiate the bump numerically.
"""
import argparse
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import numpy as np

from check_continuum_pure_sectors import Integrals, operators, ZERO
from check_continuum_tensor import time_rule, inverse_checks, OMEGA2


def scalar_weight():
    # S = kappa*(partial_2^3 partial_4 - partial_2 partial_4^3) Phi.
    # The axial integral in Integrals supplies kappa exactly as for Q_i^0.
    return {((0, 3, 0, 1), 0, ZERO, 0, ZERO): Fraction(1),
            ((0, 1, 0, 3), 0, ZERO, 0, ZERO): Fraction(-1)}


def products(left, right):
    out = defaultdict(Fraction)
    for (d, cl, a, cr, b), v in left.items():
        if cl != 0 or cr != 0 or a[0] or b[0]:
            continue
        for (e, fl, f, fr, g), w in right.items():
            if fl != 0 or fr != 0 or f[0] or g[0]:
                continue
            key = tuple(tuple(sorted(((d[j], a[j], b[j]),
                                      (e[j], f[j], g[j])))) for j in range(4))
            out[key] += v*w
    return {key: v for key, v in out.items() if v}


def compute(m, degree, time_degree, width, window):
    integ = Integrals((1, 3), m, degree)
    qs, _, _ = operators((1, 3))
    ops = [products(q, r) for q in qs for r in (scalar_weight(), qs[0])]
    ts, ds, dr, rule = time_rule(time_degree, width, window, 2)
    es = np.exp(-ts[:, None]*OMEGA2*np.arange(1, m+1)[None, :]**2)
    features = [sorted({key[j] for op in ops for key in op}) for j in range(4)]
    tables = [{} for _ in range(4)]
    for j in range(4):
        for first, second in features[j]:
            product = (integ.matrix(j, *first, 0)*integ.matrix(j, *second, 0))
            tables[j][first, second] = (float(product[0, 0]) if j == 0
                                        else es @ product @ es.T)
    sums = []
    for op in ops:
        value = np.zeros((len(ts), len(ts)))
        for key, c in op.items():
            term = float(c)*tables[0][key[0]]*tables[1][key[1]]
            term = term*tables[2][key[2]]*tables[3][key[3]]
            value += term
        sums.append(float(dr @ value @ dr))
    ab = np.array(sums).reshape(2, 2)
    # A rigorous analytic range is 0<c_*<=1/4, but A,B themselves
    # here are binary64 diagnostics. Endpoints are therefore diagnostics too.
    endpoints = np.stack([16*ab[:, 0], 16*ab[:, 0]+24*ab[:, 1]], axis=1)
    return dict(mode_cutoff=m, coefficient_degree=degree, time_rule=rule,
                term_counts=[len(op) for op in ops],
                inverse_weight_check=inverse_checks(m, ts, ds, dr),
                A=ab[:, 0].tolist(), B=ab[:, 1].tolist(),
                diagnostic_J_range_using_c_in_0_to_quarter=np.sort(endpoints).tolist(),
                failures=[], qualification="Diagnostic only: no certified arithmetic, coefficient/time quadrature or omitted-mode bounds.")


def dense_check(m, degree):
    from check_continuum_pure_sectors import assemble
    integ = Integrals((1, 3), m, degree)
    qs, _, _ = operators((1, 3))
    shape = (m,)*6
    ks = np.arange(1, m+1)
    lk = OMEGA2*(ks[:, None, None, None, None, None]**2
                +ks[None, None, :, None, None, None]**2
                +ks[None, None, None, None, :, None]**2)
    ll = OMEGA2*(ks[None, :, None, None, None, None]**2
                +ks[None, None, None, :, None, None]**2
                +ks[None, None, None, None, None, :]**2)
    weight = np.exp(-(lk+ll)/16)/(lk*ll)
    rs = [assemble(r, 0, 0, integ, shape) for r in (scalar_weight(), qs[0])]
    return np.array([[np.sum(assemble(q, 0, 0, integ, shape)*r*weight)
                      for r in rs] for q in qs])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='scripts/combined-ward-response/companion-functional-certificate.json')
    args = parser.parse_args()
    rows = [compute(4, 64, 10, .35, 40),
            compute(24, 96, 10, .35, 40),
            compute(40, 128, 12, .25, 48),
            compute(56, 160, 14, .20, 56)]
    dense = dense_check(4, 64)
    first = np.column_stack([rows[0]['A'], rows[0]['B']])
    error = float(np.max(np.abs(first-dense)))
    failures = []
    for row in rows:
        if not row['inverse_weight_check']['passed']:
            failures.append('Inverse-weight diagnostic failed at cutoff '+str(row['mode_cutoff']))
    if error > 1e-7:
        failures.append('Dense/tensor small-cutoff discrepancy exceeds diagnostic tolerance.')
    refinement = np.abs(np.column_stack([rows[-1]['A'], rows[-1]['B']])
                        -np.column_stack([rows[-2]['A'], rows[-2]['B']]))
    if float(np.max(refinement)) > 1e-4:
        failures.append('Final refinement difference exceeds diagnostic tolerance.')
    result = dict(probes=[3, 6], rows=rows, dense_check=dict(cutoff=4,
                  direct_values=dense.tolist(), maximum_difference=error,
                  required_maximum_difference=1e-7),
                  final_refinement_absolute_difference=refinement.tolist(),
                  required_final_refinement_difference=1e-4,
                  cancellation_required_J_intervals=[[21734.4, 21760.8],
                                                     [160876.8, 160972.32]],
                  failures=failures, verified_noncancellation=False,
                  qualification='No numerical entry is an enclosure; refinement and preview are not proof.')
    output = Path(args.output)
    output.write_text(json.dumps(result, indent=2)+'\n')
    print('Diagnostic A:', rows[-1]['A'], 'B:', rows[-1]['B'])
    print('Diagnostic J ranges:', rows[-1]['diagnostic_J_range_using_c_in_0_to_quarter'])
    print('Cancellation requires J in:', result['cancellation_required_J_intervals'])
    print('Dense/tensor difference:', error, 'required <=', 1e-7)
    print('Refinement difference:', float(np.max(refinement)), 'required <=', 1e-4)
    print('Failures:', failures, 'verified noncancellation:', False, 'path:', output)


if __name__ == '__main__':
    main()
