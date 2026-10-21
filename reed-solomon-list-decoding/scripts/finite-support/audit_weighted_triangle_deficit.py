"""Independent L107 arithmetic audit. Imports only L021's rational vector.

Does not import or execute the L107 constructor or overwrite its evidence.
The repetition and monotonicity arguments are audited in the manuscript.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT = BASE / 'weighted-triangle-deficit-critical-audit.json'


def choose(n, k):
    if not 0 <= k <= n:
        return 0
    k = min(k, n-k)
    value = 1
    for j in range(1, k+1):
        numerator = value * (n-j+1)
        assert numerator % j == 0
        value = numerator // j
    return value


def decode(value):
    return F(value['numerator'], value['denominator'])


def encode(value):
    value = F(value)
    return dict(numerator=value.numerator, denominator=value.denominator)


checks = {}


def check(name, condition):
    assert name not in checks
    checks[name] = bool(condition)


source = BASE / 'delsarte-lp-results.json'
original = BASE / 'weighted-triangle-deficit-results.json'
old = json.loads(original.read_text())
a = [decode(x) for x in json.loads(source.read_text())['exact']['primal']]
H = choose(1024, 68)
N = (65537**28 >> 128) + 1
U = F(choose(1024, 64), choose(68, 4))
alpha = F(N-1, (U-1)/2)
check('imported_vector_length', len(a) == 64)
check('imported_vector_sum', sum(a) == U-1)
check('imported_vector_positive', all(x > 0 for x in a))
check('threshold_floor', (N-1)*2**128 <= 65537**28 < N*2**128)
check('nontrivial_parameters', H >= 7 and N > 2 and 0 < alpha < 1)

# Reconstruct shell sizes by adjacent-shell recurrence, cross-checking
# the direct deleted/added-point products for every coordinate.
g = [1]
for i in range(68):
    numerator = g[-1]*(68-i)*(956-i)
    check(f'shell_recurrence_integral_{i+1}', numerator % (i+1)**2 == 0)
    g.append(numerator // (i+1)**2)
c = [F(1)] + [F(0)]*4
c += [F((N-1)*a[i-5], (U-1)*g[i]) for i in range(5, 69)]
check('source_coordinate_count', len(old['coordinates']) == 69)
rows = []
for i in range(69):
    check(f'shell_product_{i}', g[i] == choose(68, i)*choose(956, i))
    # These are counts in the contraction row, not edge counts.
    rep_a = choose(i, 0)*choose(68-i, 0)*choose(i, 0)*choose(956-i, 0)
    rep_b = choose(i, i)*choose(68-i, 0)*choose(i, i)*choose(956-i, 0)
    check(f'repeated_coefficients_{i}', rep_a == rep_b == 1)
    demand = None if i == 0 else N*c[i] - rep_a*c[i] - rep_b*c[i]
    if i:
        check(f'distinct_demand_{i}', demand == (N-2)*c[i])
        check(f'unordered_integrality_{i}', H*g[i] % 2 == 0)
    rows.append(dict(i=i, g=g[i], c=encode(c[i]),
                     demand=None if i == 0 else encode(demand),
                     unordered_edges=0 if i == 0 else H*g[i]//2))

cmax = c[5]
for i in range(1, 69):
    check(f'unique_maximum_comparison_{i}', c[i] == cmax if i == 5 else c[i] < cmax)
D = (N-2)*cmax
W = F(0)
for i, row in enumerate(rows):
    weight = None if i == 0 else c[i]/cmax
    row['phi'] = None if i == 0 else encode(weight)
    check(f'entire_saved_coordinate_{i}', row == old['coordinates'][i])
    if i:
        check(f'unit_weight_{i}', 0 <= weight <= 1)
        W += F(H*g[i], 2)*(1-weight)
check('complete_neighbor_partition', sum(g) == H)
check('complete_edge_partition', sum(r['unordered_edges'] for r in rows) == H*(H-1)//2)
check('objective_N', sum(g[i]*c[i] for i in range(69)) == N)
check('diagonal_not_edge', rows[0]['demand'] is None and rows[0]['unordered_edges'] == 0)
check('closed_deficit_identity', W == H*(H-1)/F(2) - F(H, 2)*(N-1)/cmax)
check('deficit_is_integer', W.denominator == 1)
forbidden = F(H, 2)*sum(g[1:5])
distance_one = F(H*g[1], 2)
check('forbidden_pairs_null', all(c[i] == 0 for i in range(1, 5)))
check('symbolic_bound', W >= forbidden >= distance_one == 32504*H)
check('strict_symbolic_gap', distance_one-(H-4) == 32503*H+4 > 0)
total_demand = sum(F(H*g[i], 2)*(N-2)*c[i] for i in range(1, 69))
check('positive_total_demand', total_demand == F((N-2)*H*(N-1), 2) > 0)
check('deficit_at_optimum', W == F(H*(H-1), 2)-total_demand/D)

expected = dict(
    input_path='scripts/finite-support/delsarte-lp-results.json',
    input_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
    H=H, N=N, U=encode(U), alpha=encode(alpha),
    maximizing_distances=[5], cmax=encode(cmax),
    optimal_common_divisor=encode(D), actual_deficit=encode(W),
    required_maximum=H-4, comparison_slack=encode(W-(H-4)),
    forbidden_deficit=int(forbidden), distance_one_deficit=int(distance_one))
for key, value in expected.items():
    check(f'saved_{key}', old[key] == value)
check('original_check_report', len(old['checks']) == 14 and all(old['checks'].values()) and old['failures'] == [])
check('all_original_fields_accounted_for', set(old) == set(expected) | {'coordinates', 'checks', 'failures'})
failures = [name for name, passed in checks.items() if not passed]
data = dict(
    scope='Independent arithmetic audit of L107; L021 vector imported, not re-proved.',
    original_sha256=hashlib.sha256(original.read_bytes()).hexdigest(),
    reconstructed=expected, coordinates=rows,
    maximum_gaps=[encode(cmax-c[i]) for i in range(1, 69)],
    total_unnormalized_demand=encode(total_demand),
    symbolic_strict_gap=32503*H+4,
    check_count=len(checks), checks=checks, failures=failures)
OUT.write_text(json.dumps(data, indent=2)+'\n')
print(f'Independent audit: {len(checks)} checks; failures: {failures}')
print('Actual missing weight >= 32504*H; required <= H-4; strict gap >= 32503*H+4.')
print('Unique maximizing distance: 5. Full exact deficit and all 69 coordinates compared.')
print(f'Full certificate: {OUT}')
assert not failures
