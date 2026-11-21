#!/usr/bin/env python3
"""Independent exact replay of C031e; no branch solve or new quadrature.

Use the imaginary numerator z*conj(P), rather than differentiate the
quotient as in1322. Analytic existence/persistence are audited in C031e.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'conjugate-collision-audit-certificate-1324.json'


def bounds(x):
    return {'lower': str(x[0]), 'upper': str(x[1])}


def main():
    old_path = HERE / 'conjugate-collision-certificate-1322.json'
    old = json.loads(old_path.read_text())
    source = ROOT / 'lemmas/C030z-positive-diagonal-grunsky-finite-scalar-reduction.md'
    text = source.read_text()
    boxes = []
    for j in range(2, 7):
        hits = re.findall(r'\| S_' + str(j) + r' \| ([\de.\-]+) \| ([\de.\-]+) \|', text)
        assert len(hits) == 1, (j, hits)
        boxes.append(tuple(map(Q, hits[0])))
    A, B, C, D, E = boxes
    vl, vh = 160000-A[1]/C[0], 160000-A[0]/C[1]
    # z=r*w, w=exp(i*pi/3). The imaginary part of z*conj(P),
    # divided by sqrt(3), is N=r/2-sum b_j*r^(j+2)*sin(j*pi/3)/sqrt(3).
    sine = [Q(1, 2), Q(1, 2), Q(0), Q(-1, 2), Q(-1, 2)]
    # Store N=r/2+sum b_j*polynomial_j(r), with low-to-high coefficients.
    numerator_b_polynomials = []
    for j, sj in enumerate(sine, 1):
        poly = [Q(0)]*(j+3)
        poly[j+2] = -sj
        numerator_b_polynomials.append(poly)
    base_b = [1, 0, 0, 0, 0]
    base_N = [Q(0)]*8
    base_N[1] = Q(1, 2)
    for bj, poly in zip(base_b, numerator_b_polynomials):
        for degree, coefficient in enumerate(poly):
            base_N[degree] += bj*coefficient
    Nr = sum(degree*c for degree, c in enumerate(base_N))
    Na = [sum(poly) for poly in numerator_b_polynomials]
    # |P0(w)|^2=1 and N0(1)=0, so H_r=N_r and H_a=N_a at the base.
    qprime_a = [-2*x/Nr for x in Na]
    # Transpose the known C031c tangent explicitly in its stated basis.
    tangent_columns = [
        [Q(-1, 2), 0, 0, 0, Q(1, 2)],
        [0, -200, 0, 200, 0],
        [0, 0, Q(-1, 2), 0, Q(1, 2)],
        [0, 0, 0, -200, 0],
        [0, 0, 0, 0, Q(-1, 2)],
    ]
    reduced = [sum(x*y for x, y in zip(qprime_a, col)) for col in tangent_columns]
    components = [A, B, (vl*C[0], vh*C[1]),
                  (vl*D[0], vh*D[1]), (vl*vl*E[0], vh*vh*E[1])]
    low = A[0]+400*B[0]+vl*C[0]/2-200*vh*D[1]-vh*vh*E[1]/2
    high = A[1]+400*B[1]+vh*C[1]/2-200*vl*D[0]-vl*vl*E[0]/2
    printed_low = Q(-511270638434762842611272634477187,
                    21980550454735102084805000000000000000)
    printed_high = Q(-5112706164033352348297561245289,
                     219805504474417536020000000000000000)
    lo_threshold, hi_threshold = Q(-3, 125000), Q(-11, 500000)
    # Exact integer cross-products certify the two strict printed inequalities.
    lower_margin = low.numerator*lo_threshold.denominator-lo_threshold.numerator*low.denominator
    upper_margin = hi_threshold.numerator*high.denominator-high.numerator*hi_threshold.denominator
    current_hashes = {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                      for p in old['input_hashes']}
    saved_base = {'w': ['1/2', '1/2'], 'w_conjugate': ['1/2', '-1/2'],
                  'P': ['1/2', '1/2'], 'P_conjugate': ['1/2', '-1/2'],
                  'f': ['1', '0'], 'f_conjugate': ['1', '0'],
                  'f_radial_derivative': ['0', '-1']}
    partials = [['-1/2', '-1/2'], ['1/2', '-1/2'], ['1', '0'],
                ['1/2', '1/2'], ['-1/2', '1/2']]
    checks = {
        'original_source_hashes_unchanged': current_hashes == old['input_hashes'],
        'original_report_passed': old['status'] == 'passed' and not old['failures']
                                 and len(old['checks']) == 14 and all(old['checks'].values()),
        'complete_base_field_matches_hand_algebra': old['base'] == saved_base,
        'complete_parameter_partials_match_hand_algebra': old['derivatives']['f_tau_a_coefficients'] == partials,
        'five_fixed_boxes_match_canonical1307_and1322': old['bounds']['boxes'] ==
            {name: bounds(box) for name, box in zip('ABCDE', boxes)},
        'positive_ordered_boxes': all(0 < x[0] <= x[1] for x in boxes),
        'v_interval_and_positive_factors': Q(103935) < vl <= vh < Q(103936)
            and old['bounds']['v0'] == bounds((vl, vh)),
        'independent_numerator_base_zero': sum(base_N) == 0,
        'independent_numerator_radial_derivative': Nr == -1 and old['derivatives']['H_r'] == str(Nr),
        'independent_H_parameter_partials': list(map(str, Na)) == old['derivatives']['H_tau_a_coefficients'],
        'independent_squared_radius_tangent': list(map(str, qprime_a)) == old['derivatives']['squared_radius_a_coefficients'],
        'tangent_matrix_transpose_matches_C031c':
            [[str(col[j]) for col in tangent_columns] for j in range(5)] == old['derivatives']['tangent_matrix'],
        'reduced_tangent_and_basis': list(map(str, reduced)) == old['derivatives']['reduced_coefficients']
            and old['derivatives']['tangent_basis'] == ['A', 'B', 'v0*C', 'v0*D', 'v0^2*E'],
        'all_five_dependency_safe_product_intervals': list(map(bounds, components)) == old['bounds']['components'],
        'both_exact_printed_endpoints': low == printed_low and high == printed_high
            and old['bounds']['squared_radius_derivative'] == bounds((low, high)),
        'strict_integer_margins': lower_margin > 0 and upper_margin > 0
            and low <= high < hi_threshold < 0,
        'required_threshold_and_simple_enclosure': old['bounds']['required_upper_bound'] == '0'
            and old['bounds']['strict_simple_enclosure'] == bounds((lo_threshold, hi_threshold)),
    }
    failures = [key for key, ok in checks.items() if not ok]
    report = {
        'status': 'passed' if not failures else 'failed', 'checks': checks, 'failures': failures,
        'scope': 'Independent fixed-u=400, pi/3 C031e audit only; no parameter sweep or branch solve.',
        'numerator_replay': {
            'identity': 'H=N/|P(r*w)|^2; N=r/2+sum b_j*polynomial_j(r)',
            'convention': 'polynomial coefficients low to high; field pair x+y*i*sqrt(3)',
            'b_polynomials': [list(map(str, p)) for p in numerator_b_polynomials],
            'base_N': list(map(str, base_N)), 'N_base': str(sum(base_N)), 'N_r': str(Nr),
            'H_a': list(map(str, Na)), 'qprime_a': list(map(str, qprime_a)),
            'tangent_columns': [list(map(str, col)) for col in tangent_columns],
            'reduced': list(map(str, reduced)),
        },
        'boxes': {name: bounds(box) for name, box in zip('ABCDE', boxes)},
        'v0': bounds((vl, vh)), 'components': list(map(bounds, components)),
        'actual_derivative_interval': bounds((low, high)), 'required_upper_bound': '0',
        'simple_enclosure': bounds((lo_threshold, hi_threshold)),
        'integer_cross_product_margins': {'lower': str(lower_margin), 'upper': str(upper_margin)},
        'original_input_hashes': current_hashes,
        'audit_input_hashes': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in [Path(__file__), old_path, ROOT/'lemmas/C031e-quadratic-grunsky-interior-conjugate-collision.md']},
        'unresolved': 'C031c branch/tangent and fixed1307 actual inclusion/Decimal contracts inherited; no uniform/effective tau interval, other-branch exclusion or RH conclusion.',
    }
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print(f"{report['status']}: {len(checks)} checks; failures={failures}; {OUT.relative_to(ROOT)}")
    print(f'actual derivative interval: [{low}, {high}]; required upper bound <0')
    print(f'simple enclosure ({lo_threshold}, {hi_threshold}); both integer margins positive={lower_margin > 0 and upper_margin > 0}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
