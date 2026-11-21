#!/usr/bin/env python3
"""Independent finite audit of C998g; no quadrature nodes or integrals.

The analytic proof and source hypotheses are checked in C998g Section7.
All prior certificates are read completely and left unchanged.
"""
import json
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
checks, snapshots = [], {}
report = {'checks': checks, 'scope': 'C998g fixed exact-node ledger and direct work only'}


def check(label, ok):
    checks.append({'name': label, 'pass': bool(ok)})


def raw(name):
    if name not in snapshots:
        snapshots[name] = (BASE / name).read_bytes()
    return snapshots[name]


def read(name):
    return json.loads(raw(name))


def rat(value):
    return F(int(value['numerator']), int(value['denominator']))


def record(value):
    value = F(value)
    return {'numerator': str(value.numerator), 'denominator': str(value.denominator)}


def ceiling(value):
    return -((-value.numerator) // value.denominator)


try:
    old = read('duffy-square-ledger-672.json')
    initial = read('jump-log-h1-bounds-654.json')
    audited = read('jump-log-h1-audit-655.json')
    for name, cert, expected_count, pass_key in [
        ('654', initial, 12, 'passed'), ('655', audited, 41, 'pass'),
        ('672', old, 75, 'pass')
    ]:
        check(name + ' complete check list and no failures',
              len(cert['checks']) == expected_count and
              all(c[pass_key] is True for c in cert['checks']) and cert['failures'] == [])
        for filename, digest in cert['input_sha256'].items():
            check(name + ' input pin ' + filename, sha256(raw(filename)).hexdigest() == digest)
    for stem, cert in [('jump-log-h1-bounds-654', initial),
                       ('jump-log-h1-audit-655', audited),
                       ('duffy-square-ledger-672', old)]:
        check(stem + ' generator hash', sha256(raw(stem + '.py')).hexdigest() == cert['script_sha256'])

    archive = 'frozen-reference-proposal-652.npz'
    check('exact archive identity', sha256(raw(archive)).hexdigest() ==
          '2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6')
    with np.load(BASE / archive, allow_pickle=False) as data:
        matrix = data['free_middle_dyadics'].copy()
    check('all762 finite binary64 values', matrix.shape == (254, 3) and
          matrix.dtype == np.dtype('float64') and np.isfinite(matrix).all())
    witness = initial['exact_X_witness']
    rows = witness['integer_columns_by_row']
    check('complete witness shape, support and denominator', len(rows) == 32 and
          all(len(row) == 3 and all(type(v) is int for v in row) for row in rows) and
          witness['denominator'] == 2**24 and witness['ambient_dimension'] == 2044 and
          witness['support_indices_zero_based'] == list(range(16)) + list(range(1022, 1038)) and
          witness['omitted_coordinates'] == 'exactly zero')
    report['columns'] = []
    counts = []
    for col in range(3):
        q = [F.from_float(float(x)) for x in matrix[:, col]]
        check(f'column{col} all254 exact dyadics match654 and672',
              q == list(map(rat, initial['exact_free_middle_columns'][col])) ==
              list(map(rat, old['exact_free_columns'][col])))
        f = [F(row[col], 2**24) for row in rows[:16]]
        h = [F(row[col], 2**24) for row in rows[16:]]
        vals = {}
        for key, arr in [('F', f), ('H', h), ('V', q)]:
            vals[key] = 6 * sum(map(abs, arr), F(0))
            vals['L' + key] = 24 * sum(((i + 3) * abs(v) for i, v in enumerate(arr)), F(0))
        force, v = vals['F'] + vals['H'], vals['V']
        vals['unprojected_l2'] = 5 * force + 45 * v
        vals['total_absolute_jumps'] = 16 * force + 40 * v
        vals['remainder_l2'] = vals['unprojected_l2'] + v + vals['total_absolute_jumps']
        vals['remainder_derivative'] = (16 * (vals['LF'] + vals['LH']) + force +
                                       23 * vals['LV'] + 83 * v + 384 * vals['unprojected_l2'])
        vals['remainder_h1'] = vals['remainder_l2'] + vals['remainder_derivative']
        check(f'column{col} all11 rational ledger values', vals ==
              {k: rat(v) for k, v in initial['columns'][col]['bounds'].items()} ==
              {k: rat(v) for k, v in audited['columns'][col]['all_bounds'].items()})
        check(f'column{col} required envelope inequalities', force < 26 and v < 14 and
              vals['unprojected_l2'] < 760)
        counts.append({'column': col,
                       'even_nonzero': sum(v != 0 for v in q[::2]),
                       'odd_nonzero': sum(v != 0 for v in q[1::2])})
        report['columns'].append({'column': col, 'exact_free_dyadics': list(map(record, q)),
                                  'all_bounds': {k: record(v) for k, v in vals.items()}})
    check('all six parity coefficient inventories', counts == old['coefficient_counts'] and
          all(c['even_nonzero'] == c['odd_nonzero'] == 127 for c in counts))
    report['coefficient_counts'] = counts

    # Rational constants in the independently checked analytic inequalities.
    constants = {'A_majorant': F(3, 2) * (17 * 26 + 21 * 14) + F(43, 2) * 14,
                 'radial_prefactor': 196 * F(3, 10) * F(8, 7) * 49,
                 'angular_prefactor': 196 * F(3, 10) * 2,
                 'angular_gauss_prefactor': F(32, 45) * 118}
    check('absolute and ellipse prefactors', constants['A_majorant'] == 1405 < 1500 and
          constants['radial_prefactor'] < 3300 and constants['angular_prefactor'] < 118 and
          constants['angular_gauss_prefactor'] < 84)
    check('exponential comparisons using log2>2/3', F(765, 2) < F(574 * 2, 3) and
          F(765, 4) < F(288 * 2, 3))
    report['analytic_constants'] = {k: record(v) for k, v in constants.items()}
    panels = []
    for exponent in range(1, 49):
        left, right = F(1, 2**exponent), F(1, 2**(exponent - 1))
        order = 32 + ceiling(144 * left)
        row = {'j': exponent, 'left': record(left), 'right': record(right),
               'n_in_Trefethen_19_3': order, 'gauss_points': order + 1,
               'exact_node_error_upper': record(F(84, 2**64))}
        check(f'panel{exponent} full record and exponent', row == old['prescription']['panels'][exponent-1]
              and 2 * order >= 64 + 288 * left)
        panels.append(row)
    check('exact48-panel partition', len(old['prescription']['panels']) == 48 and
          rat(panels[0]['right']) == 1 and rat(panels[-1]['left']) == F(1, 2**48) and
          all(panels[k]['left'] == panels[k+1]['right'] for k in range(47)))
    p = old['prescription']
    check('fixed radial and angular prescription', rat(p['eta']) == F(1, 2**48) and
          (p['radial_n'], p['radial_gauss_points'], p['rho']) == (320, 321, 2) and
          p['proposed_fractional_bits_unverified'] == 256)
    error = {'corner': F(196 * 3 * 50, 10 * 2**48),
             'radial_exact_node': F(32 * 3300, 45 * 2**66),
             'angular_exact_node': F(48 * 84, 2**64)}
    error['total_analytic'] = sum(error.values(), F(0))
    error['required_total_including_finite_arithmetic'] = F(1, 10**10)
    check('every exact error component', all(rat(old['error'][k]) == v for k, v in error.items()))
    check('printed exact total and thresholds', error['total_analytic'] ==
          F(18063793, 1729382256910270464) < F(11, 10**12) < F(1, 10**10))
    points = sum(row['gauss_points'] for row in panels)
    keys = 321 * points
    coefficients = sum(c['even_nonzero'] + c['odd_nonzero'] for c in counts)
    work = keys * coefficients
    check('full node and coefficient count', points == p['angular_points'] == 1770 and
          keys == p['scaled_density_points'] == 568170 and coefficients == 762 and
          old['work']['nonzero_free_coefficients'] == coefficients)
    check('work lower bound and required cap', work == old['work']['mandatory_real_multiplications'] ==
          432945540 and old['work']['required_square_service_maximum'] == 20000000 and
          work > 20000000 and rat(old['work']['excess_ratio']) == F(work, 20000000))
    report['panels'] = panels
    report['error'] = {k: record(v) for k, v in error.items()}
    report['work'] = {'angular_points': points, 'scaled_node_keys': keys,
                      'nonzero_free_coefficients': coefficients,
                      'mandatory_real_multiplications': work, 'allowed_total_scalar_operations': 20000000}
    check('all loaded inputs preserved', all((BASE / name).read_bytes() == value
                                            for name, value in snapshots.items()))
except Exception as exc:
    check('exception: ' + type(exc).__name__ + ': ' + str(exc), False)

report['failures'] = [c['name'] for c in checks if not c['pass']]
report['input_sha256'] = {k: sha256(v).hexdigest() for k, v in snapshots.items()}
report['script_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
report['result'] = 'PASS_FINITE_AUDIT_PRESCRIBED_WORK_STOP_UPHELD' if not report['failures'] else 'FAIL'
report['not_verified'] = ['analytic proof by this script', 'nodes or finite arithmetic',
                          'actual Gram or residual size', 'inverse debt or S3 signs',
                          'original analytic/arithmetic/source-to-Xi/whole-core/c_* contracts']
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(report, indent=2) + '\n')
print(report['result'])
print('Checks:', len(checks), '; failures:', report['failures'])
if not report['failures']:
    print('Exact-node error:', str(error['total_analytic']), '< 1.1e-11; required total <= 1e-10; finite arithmetic unpaid.')
    print('Required direct multiplications:', work, '; allowed total scalar operations: 20000000.')
print('Full certificate:', output.relative_to(BASE.parent.parent))
raise SystemExit(bool(report['failures']))
