"""Independent, exhaustive rational replay of L842; no new rank search.

Run from riemann: python3 scripts/dyadic-cubic/audit_second_ray_exact.py
Reads every original permutation term and compares a generator replay.
Coefficient route: finite-product Newton identities followed by geometric
power-sum limits; reciprocal coefficients by triangular inversion.
Determinant route: exact Gaussian elimination, independently of Leibniz.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import permutations
import json
from pathlib import Path
import subprocess
import sys

base = Path(__file__).resolve().parent
source = base / 'second-ray-exact-certificate.json'
original_bytes = source.read_bytes()
saved = json.loads(original_bytes)
checks = []


def check(name, condition):
    checks.append({'name': name, 'passed': bool(condition)})


def at(seq, n):
    return seq[n] if n >= 0 else Q(0)


def eliminate(matrix):
    b = [row[:] for row in matrix]
    value = Q(1)
    for k in range(len(b)):
        pivot_row = next((i for i in range(k, len(b)) if b[i][k]), None)
        if pivot_row is None:
            return Q(0)
        if pivot_row != k:
            b[k], b[pivot_row] = b[pivot_row], b[k]
            value = -value
        pivot = b[k][k]
        value *= pivot
        for i in range(k + 1, len(b)):
            ratio = b[i][k] / pivot
            for j in range(k, len(b)):
                b[i][j] -= ratio * b[k][j]
    return value


# The three unscaled variables are 1, exp(i*pi/3), exp(-i*pi/3).
# Their mth power sum is the integer cycle below, starting at m=0.
# Geometric summation over dyadic scales gives power[m].
cycle = [3, 2, 0, -1, 0, 2]
power = [Q(0)] + [Q(cycle[m % 6]) / (1 - Q(1, 2**m))
                       for m in range(1, 7)]
a = [Q(1)]
for n in range(1, 7):
    a.append(sum(((-1)**(m-1) * power[m] * a[n-m]
                  for m in range(1, n+1)), Q(0)) / n)
h = [Q(1)]
for n in range(1, 7):
    h.append(-sum(((-1)**k * a[k] * h[n-k]
                   for k in range(1, n+1)), Q(0)))

check('polynomial and scale', saved['polynomial_coefficients'] == [1, 2, 2, 1]
      and Q(saved['dyadic_ratio']) == Q(1, 2))
check('all seven elementary coefficients', list(map(Q, saved['a_0_through_6'])) == a)
check('all seven reciprocal coefficients', list(map(Q, saved['h_0_through_6'])) == h)
check('displayed elementary values', a == list(map(Q, [
    '1', '4', '8', '72/7', '64/7', '1280/217', '38848/13671'])))
check('displayed reciprocal values', h == list(map(Q, [
    '1', '4', '8', '72/7', '64/7', '1280/217', '52736/13671'])))
p = [1, 2, 2, 1]
a_residuals = [(1 - Q(1, 2**n))*a[n] - sum(
    (p[k]*Q(1, 2**(n-k))*a[n-k] for k in range(1, min(3, n)+1)), Q(0))
    for n in range(1, 7)]
h_residuals = [(1 - Q(1, 2**n))*h[n] - 2*at(h, n-1)
               + 2*at(h, n-2) - at(h, n-3) for n in range(1, 7)]
reciprocal_residuals = [sum(((-1)**k*a[k]*h[n-k]
                            for k in range(n+1)), Q(0)) - (n == 0)
                        for n in range(7)]
check('all six elementary recurrence equations', not any(a_residuals))
check('all six reciprocal recurrence equations', not any(h_residuals))
check('all seven inverse-series equations', not any(reciprocal_residuals))
check('ranks exactly 1 through 5', [r['rank'] for r in saved['rays']] == list(range(1, 6)))

rank_reports = []
for r, item in enumerate(saved['rays'], 1):
    matrix = [[at(a, 2+j-i) for j in range(r)] for i in range(r)]
    determinant = eliminate(matrix)
    rectangle = h[r]*h[r] - h[r-1]*h[r+1]
    check(f'rank {r} full matrix', [[Q(v) for v in row] for row in item['matrix']] == matrix)
    check(f'rank {r} independent elimination and rectangle', determinant == rectangle)
    check(f'rank {r} both reported values', Q(item['direct_determinant']) == determinant
          and Q(item['rectangular_expression']) == rectangle)
    check(f'rank {r} flags', item['methods_agree'] == (determinant == rectangle)
          and item['negative'] == (determinant < 0))
    expected = set(permutations(range(r)))
    observed = [tuple(term['permutation']) for term in item['leibniz_terms']]
    check(f'rank {r} exhaustive nonduplicated permutation set',
          len(observed) == len(expected) and set(observed) == expected)
    term_checks = []
    total = Q(0)
    for number, term in enumerate(item['leibniz_terms']):
        perm = tuple(term['permutation'])
        # Independent parity: number of cycles, rather than inversion count.
        seen = set()
        cycles = 0
        for i in range(r):
            if i not in seen:
                cycles += 1
                j = i
                while j not in seen:
                    seen.add(j)
                    j = perm[j]
        value = Q((-1)**(r-cycles))
        for i in range(r):
            value *= matrix[i][perm[i]]
        check(f'rank {r} term {number}', Q(term['signed_term']) == value)
        term_checks.append({'permutation': list(perm), 'recomputed_term': str(value),
                            'stored_term_matches': Q(term['signed_term']) == value})
        total += value
    check(f'rank {r} complete sum', total == determinant)
    rank_reports.append({'rank': r, 'matrix': [[str(v) for v in row] for row in matrix],
                         'elimination_determinant': str(determinant),
                         'rectangular_expression': str(rectangle),
                         'recomputed_leibniz_sum': str(total), 'terms': term_checks})

check('all displayed smaller-rank values',
      [r['elimination_determinant'] for r in rank_reports[:4]]
      == ['8', '160/7', '1600/49', '34816/1519'])
check('rank5 duplicate record', saved['rank5'] == {
    k: v for k, v in saved['rays'][4].items() if k != 'leibniz_terms'})
check('required lower bound', Q(saved['required_lower_bound']) == 0)
check('negative exact value', rank_reports[4]['elimination_determinant'] == '-1409024/2966607')
check('all original grouped checks true', len(saved['checks']) == 5 and all(saved['checks'].values()))
check('original failures empty', saved['failures'] == [])
replay = subprocess.run([sys.executable, str(base / 'second_ray_exact.py')],
                        capture_output=True, text=True)
check('generator exits successfully', replay.returncode == 0)
check('generator reproduces original bytes', source.read_bytes() == original_bytes)
failures = [item['name'] for item in checks if not item['passed']]
report = {
    'scope': 'L842 finite arithmetic audit only; analytic audit in canonical lemma.',
    'original_sha256': sha256(original_bytes).hexdigest(),
    'power_sums_1_through_6': list(map(str, power[1:])),
    'independent_a': list(map(str, a)), 'independent_h': list(map(str, h)),
    'elementary_recurrence_residuals': list(map(str, a_residuals)),
    'reciprocal_recurrence_residuals': list(map(str, h_residuals)),
    'reciprocity_residuals': list(map(str, reciprocal_residuals)),
    'ranks': rank_reports, 'checks': checks, 'failures': failures,
    'generator_replay': {'exit_code': replay.returncode,
                         'stdout': replay.stdout, 'stderr': replay.stderr},
    'actual_determinant': rank_reports[4]['elimination_determinant'],
    'required_lower_bound': '0', 'rank5_terms_inspected': len(rank_reports[4]['terms']),
    'total_terms_inspected': sum(len(r['terms']) for r in rank_reports),
}
destination = base / 'second-ray-independent-audit.json'
destination.write_text(json.dumps(report, indent=2) + '\n')
print(f'checks={len(checks)}; passed={len(checks)-len(failures)}; failures={failures}')
print('all 153 permutation terms inspected, including all 120 rank-five terms')
print(f'actual={report["actual_determinant"]}; required lower bound=0')
print(f'certificate={destination.relative_to(Path.cwd())}')
raise SystemExit(bool(failures))
