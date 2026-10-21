"""Reproduce finite-spectrum rule diagnostics and compare saved M=112 sums.

Binary64 only: observed agreement is not an enclosure or sign proof.
Run check_continuum_tensor.py at the degrees named in the working record first.
"""
import json
from pathlib import Path

import numpy as np

from check_continuum_tensor import inverse_checks, time_rule


def main():
    base = Path(__file__).parent
    rules_path = base / 'continuum-tensor112-rule-diagnostic.json'
    result = dict(scope='Cutoff-112 inverse-weight diagnostics only; binary64, no enclosure.',
                  rows=[], failures=[])
    configurations = [(0.5, 8, 0), (0.5, 12, 0), (0.5, 24, 0),
                      (0.25, 24, 0), (0.25, 32, 0),
                      (0.5, 8, 8), (0.5, 12, 8), (0.5, 16, 8)]
    for width, degree, levels in configurations:
        times, ds, dr, rule = time_rule(degree, width, 80, levels)
        check = inverse_checks(112, times, ds, dr)
        result['rows'].append(dict(panel_width=width, endpoint_levels=levels,
                                   rule=rule, inverse_checks=check))
        if not check['passed']:
            result['failures'].append(dict(panel_width=width, degree=degree,
                                           endpoint_levels=levels,
                                           errors=check['actual_max_relative_inverse_weight_errors']))
    rules_path.write_text(json.dumps(result, indent=2) + '\n')

    paths = [base / f'continuum-tensor112-degree{d}-certificate.json' for d in (96, 144)]
    data = [json.loads(path.read_text()) for path in paths]
    comparison = dict(qualification='Binary64 refinement only, not a quadrature or rounding enclosure.',
                      input_certificates=[str(path.relative_to(base.parent.parent)) for path in paths],
                      rigorous_sign_certified=False, actual_error_bound=None, checks=[], failures=[])
    for item, degree in zip(data, (96, 144)):
        if item['coefficient_degree'] != degree or item['failures']:
            raise ValueError('Unexpected coefficient degree or failed input diagnostics')
        if any(row['cutoff'] != 112 or not row['inverse_checks']['passed'] for row in item['rows']):
            raise ValueError('Comparison requires passing rules at the same cutoff 112')
    tests = [('time degree 8 to 12, coefficient degree 96', data[0]['rows'][0], data[0]['rows'][1]),
             ('time degree 12 to 16, coefficient degree 144', data[1]['rows'][0], data[1]['rows'][1]),
             ('coefficient degree 96 to 144, time degree 12', data[0]['rows'][1], data[1]['rows'][0])]
    for name, old, new in tests:
        a, b = [np.array(row['pure_sector_axial_parts']) for row in (old, new)]
        differences = np.abs(a - b)
        required = 1e-8 + 1e-9 * np.abs(b)
        passed = bool(np.all(differences < required))
        check = dict(check=name, old_parts=a.tolist(), refined_parts=b.tolist(),
                     actual_absolute_differences=differences.tolist(),
                     required_absolute_differences=required.tolist(),
                     actual_max_absolute_difference=float(differences.max()),
                     actual_max_fraction_of_tolerance=float((differences / required).max()),
                     total_absolute_differences=np.abs(a.sum(axis=(1, 2)) - b.sum(axis=(1, 2))).tolist(),
                     passed=passed)
        comparison['checks'].append(check)
        if not passed:
            comparison['failures'].append(name)
    comparison['refined_totals'] = data[1]['rows'][1]['pure_values']
    output = base / 'continuum-tensor112-refinement-certificate.json'
    output.write_text(json.dumps(comparison, indent=2) + '\n')
    print(json.dumps(dict(rule_failures=result['failures'], rules_path=str(rules_path),
                          checks=[{key: c[key] for key in ('check', 'actual_max_absolute_difference',
                                  'actual_max_fraction_of_tolerance', 'passed')} for c in comparison['checks']],
                          refined_totals=comparison['refined_totals'], failures=comparison['failures'],
                          actual_error_bound=None, required_error_bound='Certified retained error plus L033 tail < retained absolute value.',
                          rigorous_sign_certified=False, path=str(output))))


if __name__ == '__main__':
    main()
