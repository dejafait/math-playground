#!/usr/bin/env python3
"""Independent exact audit of the complete finite L772 certificate.

Run from riemann. Infinite claims remain the canonical prose proof.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import prod
from pathlib import Path
import json


def q(value):
    return Q(value['numerator'], value['denominator'])


def bareiss(a):
    a = [list(row) for row in a]
    sign, previous = 1, 1
    for k in range(len(a) - 1):
        pivot_row = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, len(a)):
            for j in range(k + 1, len(a)):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
        for i in range(k + 1, len(a)):
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def det(a):
    scale = 10**12
    integer = [[x * scale for x in row] for row in a]
    assert all(x.denominator == 1 for row in integer for x in row)
    return Q(bareiss([[int(x) for x in row] for row in integer]), scale**len(a))


def matmul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


source = Path('scripts/coefficient-countermodel/strong-log-order-five-408.json')
raw = source.read_bytes()
c = json.loads(raw)
checks = {}
b = list(map(Q, ['1/1000000000000', '1/1000000', '1/100', '3/5', '1',
                 '3/5', '1/100', '1/1000000', '1/1000000000000']))
m = [[b[4 + j - i] for j in range(5)] for i in range(5)]
checks['complete_prefix_and_matrix'] = list(map(q, c['prefix'])) == b and [[q(x) for x in row] for row in c['matrix']] == m
ratios = [b[n]**2 / (b[n-1] * b[n+1]) for n in range(1, 8)]
checks['all_seven_ratios'] = ratios == list(map(q, c['prefix_ratios_n1_through_n7']))
checks['required_and_actual_bounds'] = q(c['required_ratio']) == Q(11, 4) < min(ratios)
b9 = b[8] * Q(1, 10**6) / 4
checks['junction'] = q(c['b9']) == b9 and q(c['junction_ratio_n8']) == b[8]**2/(b[7]*b9) == 4
checks['prefix_positive'] = all(x > 0 for x in b)
terms, permutations = [], set()
for entry in c['determinant_terms']:
    p = tuple(entry['permutation'])
    assert sorted(p) == list(range(5)) and p not in permutations
    permutations.add(p)
    # Parity from cycle count, independent of the generator's inversion count.
    visited, cycles = set(), 0
    for start in range(5):
        if start not in visited:
            cycles += 1
            i = start
            while i not in visited:
                visited.add(i)
                i = p[i]
    actual = (-1)**(5-cycles) * prod(m[i][p[i]] for i in range(5))
    assert actual == q(entry['term'])
    terms.append(actual)
value = det(m)
checks['all_120_terms_and_integer_elimination'] = len(permutations) == 120 and sum(terms) == value == q(c['determinant'])
checks['stated_determinant_and_sign'] = value == Q(-351560678441474525317585871, 10**28) < 0
checks['scaled_integer_determinant'] = value * 10**60 == c['scaled_integer_matrix_determinant']
blocks = c['reversal_blocks']
odd = [[q(x) for x in row] for row in blocks['odd']]
even = [[q(x) for x in row] for row in blocks['even']]
o = [[1, 0], [0, 1], [0, 0], [0, -1], [-1, 0]]
e = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]]
p = [o[i] + e[i] for i in range(5)]
checks['basis_and_exact_intertwining'] = bareiss(p) != 0 and matmul(m, o) == matmul(o, odd) and matmul(m, e) == matmul(e, even)
od, ed = det(odd), det(even)
checks['block_determinants'] = od == q(blocks['odd_determinant']) == Q(63000119999801, 10**14) and ed == q(blocks['even_determinant']) == Q(-5580317600071, 10**14)
checks['block_product_and_signs'] = od > 0 > ed and od * ed == value
reference = [[Q(1) if i == j else Q(3, 5) if abs(i-j) == 1 else Q(0) for j in range(5)] for i in range(5)]
checks['reference_determinant'] = det(reference) == q(c['reference_determinant']) == Q(-32, 625)
checks['r0_comparison'] = Q(5) < Q(25, 4) and Q(3, 2) + Q(5, 4) == Q(11, 4)
checks['source_report_has_no_failures'] = c['failures'] == [] and all(c['checks'].values())
output = Path(__file__).with_suffix('.json')
report = {'lemma': 'L772', 'source': str(source), 'source_sha256': sha256(raw).hexdigest(),
          'checks': checks, 'complete_terms_checked': len(terms),
          'determinant': str(value), 'required_ratio': '11/4', 'minimum_prefix_ratio': str(min(ratios)),
          'junction_ratio': '4', 'basis_determinant': bareiss(p),
          'odd_determinant': str(od), 'even_determinant': str(ed),
          'failures': [k for k, v in checks.items() if not v],
          'scope': 'Complete finite evidence only; universal tail, convergence and theorem application audited in L772 prose.'}
output.write_text(json.dumps(report, indent=2) + '\n')
print(f'Terms checked: {len(terms)}/120; D_(5,4)={value}; required <0: {value < 0}')
print(f'Minimum prefix ratio={min(ratios)}; junction=4; required >=11/4')
print(f'Checks: {sum(checks.values())}/{len(checks)}; failures: {report["failures"]}; certificate: {output}')
raise SystemExit(bool(report['failures']))
