#!/usr/bin/env python3
"""Independent exact check of L031's saved certificate (no builder import).

The infinite analytic proof remains in L031. Run from the notebook root.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BASE = Path(__file__).resolve().parent
source = BASE / 'enlarged-basis.json'
data = json.loads(source.read_text())
checks = {}

def check(name, value):
    checks[name] = bool(value)

def val(x):
    x = F(x)
    if not x:
        return None
    a, b, v = abs(x.numerator), x.denominator, 0
    while a % 3 == 0:
        a //= 3
        v += 1
    while b % 3 == 0:
        b //= 3
        v -= 1
    return v

# Multiplication by theta using Phi_5, without a mod-5 power formula.
def theta_step(c):
    return [-c[3], c[0]-c[3], c[1]-c[3], c[2]-c[3]]

powers = [[1, 0, 0, 0]]
for i in range(726):
    powers.append(theta_step(powers[-1]))
check('theta_order_five', powers[5] == powers[0] and powers[1] != powers[0])

# Multiply successively by theta^a*pi^j, reducing pi^27=3 at each step.
def multiply_monomial(v, j, a):
    result = [F(0)] * 108
    for r in range(27):
        c = v[4*r:4*r+4]
        for _ in range(a):
            c = theta_step(c)
        q, s = divmod(r+j, 27)
        for b in range(4):
            result[4*s+b] += 3**q * c[b]
    return result

expected_cols = []
congruences = []
for j in range(1, 14):
    for a in range(4):
        idx = 4*(j-1)+a
        power = [F(1)] + [F(0)]*107
        series = [F(0)]*108
        for k in range(1, 243):
            power = multiply_monomial(power, j, a)
            for i in range(108):
                series[i] += F((-1)**(k+1), k)*power[i]
        check(f'finite_series_{j}_{a}', series == list(map(F, data['finite_sums'][idx])))
        col = []
        for i, x in enumerate(series):
            depth = int(i//4 < 14)
            scaled = 9*x
            modulus = 3**(depth+2)
            n = scaled.numerator*pow(scaled.denominator, -1, modulus) % modulus
            y = F(n, 9)
            actual = F(data['representatives'][idx][i])
            error = val(x-actual)
            ok = actual == y and (error is None or error >= depth)
            congruences.append(dict(j=j, a=a, coordinate=i, valuation=error,
                                    required=depth, passed=ok))
            check(f'coordinate_{idx}_{i}', ok and error == data['congruence_valuations'][idx][i])
            col.append(n)
        expected_cols.append(col)
for i in range(108):
    expected_cols.append([9*3**int(i//4 < 14) if k == i else 0 for k in range(108)])
expected_m = [list(row) for row in zip(*expected_cols)]
M = data['integer_generator_matrix']
B = data['integer_basis_matrix']
W = data['basis_in_generators']
C = data['generators_in_basis']
V = data['column_transform']
VI = data['inverse_column_transform']
for name, matrix, rows, cols in [('M', M, 108, 160), ('B', B, 108, 108),
                               ('W', W, 160, 108), ('C', C, 108, 160),
                               ('V', V, 160, 160), ('VI', VI, 160, 160)]:
    check('shape_and_integrality_'+name, len(matrix) == rows and
          all(len(row) == cols and all(type(x) is int for x in row) for row in matrix))
check('all_160_generator_columns', M == expected_m)

def matmul(A, B):
    columns = list(zip(*B))
    return [[sum(x*y for x, y in zip(row, col)) for col in columns] for row in A]

check('M_W_equals_B', matmul(M, W) == B)
check('B_C_equals_M', matmul(B, C) == M)
check('M_V_equals_zero_B', matmul(M, V) == [[0]*52+row for row in B])
identity = [[int(i == j) for j in range(160)] for i in range(160)]
check('V_VI_equals_identity', matmul(V, VI) == identity)
check('VI_V_equals_identity', matmul(VI, V) == identity)
check('W_last_columns', W == [row[52:] for row in V])
check('C_last_rows', C == VI[52:])
check('triangular_full_rank', all(B[i][j] == 0 for i in range(108) for j in range(i))
      and all(B[i][i] > 0 for i in range(108)))
diag = [val(B[i][i]) for i in range(108)]
histogram = {str(v): diag.count(v) for v in sorted(set(diag))}
det = sum(diag)-216
minimum = min(F(val(F(B[i][j], 9)))+F(i//4, 27)
              for i in range(108) for j in range(108) if B[i][j])
check('determinant_valuation_four', det == 4)
check('diagonal_histogram', histogram == {'0': 8, '1': 16, '2': 48, '3': 36})
check('every_basis_term_at_least_minus_two', minimum == -2)
witness = [(i, F(val(F(B[i][36], 9)))+F(i//4, 27)) for i in range(108) if B[i][36]]
check('b_9_0_unique_minimum', [i for i, v in witness if v == -2] == [0]
      and all(v >= -2 for i, v in witness))

# Parse all displayed expressions rather than regenerating their formatting.
lemma = ROOT / 'lemmas/L031-enlarged-complete-logarithm-lattice-basis.md'
rows = [line for line in lemma.read_text().splitlines() if re.match(r'^\| \d+ \|', line)]
check('table_rows', len(rows) == 27)
for r, line in enumerate(rows):
    cells = [s.strip() for s in line.split('|')[1:-1]]
    check(f'table_row_label_{r}', cells[0] == str(r) and len(cells) == 5)
    for a, expression in enumerate(cells[1:]):
        col = [F(0)]*108
        for term in expression.split(' + '):
            tokens = term.split()
            coefficient = F(tokens[0])
            rr, aa = 0, 0
            for token in tokens[1:]:
                base, _, exponent = token.partition('^')
                exponent = int(exponent) if exponent else 1
                if base == 'theta':
                    aa = exponent
                elif base == 'pi':
                    rr = exponent
                else:
                    raise ValueError(token)
            col[4*rr+aa] += coefficient
        check(f'canonical_table_column_{r}_{a}', col == [F(row[4*r+a], 9) for row in B])

failures = [name for name, ok in checks.items() if not ok]
report = dict(source=str(source.relative_to(ROOT)), checks=checks, failures=failures,
              coordinate_evidence=congruences, rank=108, required_rank=108,
              determinant_v3=det, diagonal_histogram=histogram,
              basis_term_minimum=str(minimum), witness_terms=[[i, str(v)] for i, v in witness],
              analytic_bounds=dict(tail_pi_valuation=108, required=14,
                                   deep_depth='14/27', required_strictly_above='1/2'),
              qualification='Infinite tails and unit completeness are proved in L031, not by this finite check.')
out = BASE / 'enlarged-basis-independent-audit.json'
out.write_text(json.dumps(report, indent=2)+'\n')
print('Independent audit: 52 series, 5616 congruences, 160 generators, 108 table columns; full matrix identities.')
print('Rank actual/required: 108/108; determinant v3:', det, '; minimum:', minimum)
print('Analytic bound recorded from proof: tail 108 >= 14; deep 14/27 > 1/2.')
print('Failures:', failures)
print('Certificate:', out.relative_to(ROOT))
raise SystemExit(bool(failures))
