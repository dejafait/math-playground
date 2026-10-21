#!/usr/bin/env python3
"""Independent full L034 audit; no imports from the certificate builder.

Run from the notebook root. Exact evidence goes to the adjacent JSON file.
The analytic identification of the genuine logarithm lattice is audited L031.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from math import gcd
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'enlarged-basis.json'
CERT = ROOT / 'projected-container-homothety.json'
OUTPUT = ROOT / 'projected-container-independent-audit.json'
PIN = 'ad5ea1741a5cc54d5413ab679fd4fba387e8a2aafc8d9c7c2b6d31e799159102'
checks = {}


def check(name, condition):
    checks[name] = bool(condition)
    if not condition:
        raise ValueError(name)


def matrix(value, rows, cols, integral=False):
    if len(value) != rows or any(len(row) != cols for row in value):
        raise ValueError('matrix shape')
    if integral and any(type(x) is not int for row in value for x in row):
        raise ValueError('noninteger matrix entry')
    return [[Fraction(x) for x in row] for row in value]


def eye(n):
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def product(a, b):
    # Accumulate nonzero outer-product contributions, unlike builder dot products.
    if not a or not b or any(len(row) != len(b) for row in a):
        raise ValueError('product dimension')
    width = len(b[0])
    if any(len(row) != width for row in b):
        raise ValueError('ragged product')
    out = [[Fraction(0) for _ in range(width)] for _ in a]
    sparse = [[(j, x) for j, x in enumerate(row) if x] for row in b]
    for i, row in enumerate(a):
        for k, x in enumerate(row):
            if x:
                for j, y in sparse[k]:
                    out[i][j] += x * y
    return out


def v3(x):
    x = Fraction(x)
    if not x:
        raise ValueError('valuation of zero')
    powers = []
    for number in (abs(x.numerator), x.denominator):
        power = 0
        while number % 3 == 0:
            power += 1
            number //= 3
        powers.append(power)
    return powers[0] - powers[1]


def elementary(target, kind, i, j, coefficient, inverse=False):
    if inverse and coefficient is not None:
        coefficient = -coefficient
    if kind.endswith('row'):
        if kind.startswith('swap'):
            target[i], target[j] = target[j], target[i]
        else:
            for k in range(len(target[0])):
                target[i][k] += coefficient * target[j][k]
    else:
        for row in target:
            if kind.startswith('swap'):
                row[i], row[j] = row[j], row[i]
            else:
                row[i] += coefficient * row[j]


def encode(x):
    if isinstance(x, Fraction):
        return str(x)
    raise TypeError(type(x).__name__)


report = {'checks': checks, 'failures': [], 'analytic_input': 'Audited L031',
          'source_sha256': sha256(SOURCE.read_bytes()).hexdigest(),
          'certificate_sha256': sha256(CERT.read_bytes()).hexdigest()}
try:
    saved = json.loads(CERT.read_text())
    b = matrix(json.loads(SOURCE.read_text())['integer_basis_matrix'], 108, 108, True)
    check('pinned_complete_L031_input', report['source_sha256'] == PIN == saved['source_sha256'])
    check('B_full_rank_triangular', all(b[i][i] != 0 for i in range(108))
          and all(b[i][j] == 0 for i in range(108) for j in range(i)))
    check('B_over_9_determinant_valuation', sum(v3(b[i][i]) for i in range(108)) - 216 == 4)
    tau = [[Fraction(4), Fraction(-1), Fraction(-1), Fraction(-1)] + [Fraction(0)] * 104]
    check('complete_trace_row', saved['trace_row_divided_by_27'] == tau[0])
    t = product(tau, b)
    check('complete_trace_on_B', t[0] == saved['trace_on_integer_J_basis'])
    trace_gcd = 0
    for value in t[0]:
        check('trace_row_integer', value.denominator == 1)
        trace_gcd = gcd(trace_gcd, value.numerator)
    check('trace_gcd_is_one', trace_gcd == saved['trace_gcd'] == 1)
    a = matrix(saved['kernel_transform'], 108, 108, True)
    ai = matrix(saved['inverse_kernel_transform'], 108, 108, True)
    check('A_times_A_inverse_full', product(a, ai) == eye(108))
    check('A_inverse_times_A_full', product(ai, a) == eye(108))
    check('complete_transformed_trace', product(t, a) == [[Fraction(1)] + [Fraction(0)] * 107])
    c = matrix(saved['C_basis'], 108, 107, True)
    expected_c = [[Fraction(0)] * 107 for _ in range(108)]
    for j in range(107):
        if j < 3:
            expected_c[0][j] = 1
            expected_c[j+1][j] = 4
        else:
            expected_c[j+1][j] = 1
    check('full_C_basis_not_only_span', c == expected_c)
    check('C_trace_zero', product(tau, c) == [[0] * 107])
    mb9 = matrix(saved['M_basis_times_9'], 108, 107, True)
    check('full_M_basis_from_kernel', product(b, [row[1:] for row in a]) == mb9)
    check('M_trace_zero', product(tau, mb9) == [[0] * 107])
    r = matrix(saved['relative_C_in_M'], 107, 107)
    check('M_times_R_equals_C_all_coordinates', product(mb9, r) == [[9*x for x in row] for row in c])

    # Accumulate U and V separately, then check U R V = D globally.
    # Thus this check does not merely rerun the builder's evolving R matrix.
    left, right = eye(107), eye(107)
    operations = []
    operation_evidence = []
    for number, operation in enumerate(saved['smith_operations']):
        if not isinstance(operation, list) or len(operation) < 3:
            raise ValueError('malformed operation')
        kind, i, j = operation[:3]
        check(f'operation_{number}_indices', type(i) is int and type(j) is int
              and 0 <= i < 107 and 0 <= j < 107 and i != j)
        check(f'operation_{number}_syntax', kind in ('swap_row', 'swap_col', 'add_row', 'add_col')
              and len(operation) == (4 if kind.startswith('add') else 3))
        coefficient = Fraction(operation[3]) if kind.startswith('add') else None
        valuation = v3(coefficient) if coefficient else None
        check(f'operation_{number}_Z3_inverse', valuation is None or valuation >= 0)
        elementary(left if kind.endswith('row') else right, kind, i, j, coefficient)
        operations.append((kind, i, j, coefficient))
        operation_evidence.append({'number': number, 'operation': operation,
                                   'coefficient_v3': valuation, 'invertible_over_Z3': True})
    check('all_277_operations_read', len(operations) == 277)
    check('U_and_V_integral', all(not x or v3(x) >= 0 for m in (left, right) for row in m for x in row))
    d = [Fraction(x) for x in saved['smith_diagonal']]
    check('107_nonzero_diagonal_entries', len(d) == 107 and all(d))
    diagonal = [[d[i] if i == j else Fraction(0) for j in range(107)] for i in range(107)]
    check('global_U_R_V_equals_D', product(product(left, r), right) == diagonal)
    reverse = [row[:] for row in diagonal]
    for operation in reversed(operations):
        elementary(reverse, *operation, inverse=True)
    check('reverse_every_operation_D_to_R', reverse == r)
    exponents = [v3(x) for x in d]
    check('complete_exponent_list', exponents == sorted(exponents) == saved['smith_exponents'])
    multiplicities = {str(k): v for k, v in sorted(Counter(exponents).items())}
    check('all_multiplicities', multiplicities == saved['exponent_multiplicities']
          == {'-1': 36, '0': 48, '1': 16, '2': 7})
    unit_parts = [x / (Fraction(3) ** k) for x, k in zip(d, exponents)]
    check('all_diagonal_unit_parts', all(v3(x) == 0 for x in unit_parts))
    intervals = [[exponents[i], exponents[i+1]] for i in range(106)]
    lower, upper = max(x[0] for x in intervals), min(x[1] for x in intervals)
    check('all_106_interlacing_constraints', lower == 2 and upper == -1)
    check('saved_thresholds', saved['required_scalar_lower'] == lower
          and saved['required_scalar_upper'] == upper and saved['scalar_interval_empty'] is True)
    check('scalar_interval_empty', lower > upper)
    report.update(trace_gcd=trace_gcd, transformed_trace=product(t, a)[0],
                  left_smith_transform=left, right_smith_transform=right,
                  operation_evidence=operation_evidence, diagonal=d,
                  unit_parts=unit_parts, exponents=exponents,
                  exponent_multiplicities=multiplicities,
                  all_interlacing_intervals=intervals,
                  required_scalar_lower=lower, required_scalar_upper=upper)
except Exception as error:
    report['failures'].append(str(error))
finally:
    OUTPUT.write_text(json.dumps(report, default=encode, indent=2) + '\n')
    print(json.dumps({'checks': len(checks), 'failures': report['failures'],
                      'exponent_multiplicities': report.get('exponent_multiplicities'),
                      'required_scalar_lower': report.get('required_scalar_lower'),
                      'required_scalar_upper': report.get('required_scalar_upper'),
                      'certificate': str(OUTPUT.relative_to(ROOT.parents[1]))}))
if report['failures']:
    raise SystemExit(1)
