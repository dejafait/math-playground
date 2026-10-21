"""Independent L071 audit: polynomial division, determinants and full residues.

Does not import or execute check_witness.py. The analytic local-ring,
Kummer-cardinality and base-change arguments are in L071, not this script.
"""
from fractions import Fraction as Q
from itertools import permutations, product
from pathlib import Path
import hashlib
import json


def trim(p):
    p = list(map(Q, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    r = [Q(0)] * max(len(p), len(q))
    for i, v in enumerate(p):
        r[i] += v
    for i, v in enumerate(q):
        r[i] += v
    return trim(r)


def scale(c, p):
    return trim([c * v for v in p])


def multiply(p, q):
    r = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return trim(r)


def remainder(p, modulus):
    r = trim(p)
    while len(r) >= len(modulus):
        r = add(r, [Q(0)] * (len(r) - len(modulus))
                + scale(-r[-1] / modulus[-1], modulus))
    return r


def compose(p, q):
    r = [Q(0)]
    for a in reversed(p):
        r = add(multiply(r, q), [a])
    return r


def coordinates(p, modulus):
    r = remainder(p, modulus)
    return r + [Q(0)] * (len(modulus) - 1 - len(r))


def determinant(matrix):
    n = len(matrix)
    total = Q(0)
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j]
                         for i in range(n) for j in range(i + 1, n))
        term = Q((-1) ** inversions)
        for i, j in enumerate(perm):
            term *= matrix[i][j]
        total += term
    return total


def multiplication_matrix(p, modulus):
    n = len(modulus) - 1
    columns = [coordinates([0] * j + list(p), modulus) for j in range(n)]
    return [list(row) for row in zip(*columns)]


def clean(value):
    if isinstance(value, Q):
        return int(value) if value.denominator == 1 else str(value)
    if isinstance(value, dict):
        return {k: clean(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [clean(v) for v in value]
    return value


directory = Path(__file__).resolve().parent
original_path = directory / 'witness-certificate.json'
original_bytes = original_path.read_bytes()
original = json.loads(original_bytes)
checks = {}


def check(name, assertion):
    checks[name] = bool(assertion)


f = [1, 1, -1, 1]
g = [-1264, -160, -4, 1]
shifted = [-2, 6, -4, 1]
theta = [8, -14, 6]
theta2 = coordinates(multiply(theta, theta), f)
t_from_theta = [Q(-92, 484), Q(-62, 484), Q(3, 484)]
u_t, inverse_t = [0, -1, 0], [1, -1, 1]
theta_s = coordinates(compose(theta, [-1, 1]), shifted)
u_s = coordinates(compose(u_t, [-1, 1]), shifted)
inverse_s = coordinates(compose(inverse_t, [-1, 1]), shifted)
h_s = coordinates(add([5], scale(-1, theta_s)), shifted)
uh_s = coordinates(multiply(u_s, h_s), shifted)
norm_u_t = determinant(multiplication_matrix(u_t, f))
norm_u_s = determinant(multiplication_matrix(u_s, shifted))
norm_h = determinant(multiplication_matrix(h_s, shifted))
check('original_inputs_match', original['inputs'] ==
      dict(f=f, g=g, shifted_f=shifted))
check('translated_polynomial', compose(f, [-1, 1]) == shifted)
check('eisenstein_at_two', all(a % 2 == 0 for a in shifted[:-1])
      and shifted[0] % 4 == 2 and shifted[-1] == 1)
check('theta_squared', theta2 == [196, -128, 124])
check('g_theta_zero', remainder(compose(g, theta), f) == [0])
check('inverse_recovers_t', remainder(compose(t_from_theta, theta), f) == [0, 1])
check('inverse_satisfies_f', remainder(compose(f, t_from_theta), g) == [0])
check('forward_recovers_theta', remainder(compose(theta, t_from_theta), g) == [0, 1])
check('original_coordinates_match', original['coordinates'] == clean({
    'theta_in_t': theta, 'theta_squared_in_t': theta2,
    'u_theta_numerator': [92, 62, -3], 'u_theta_denominator': 484}))
check('unit_inverse_t', remainder(multiply(u_t, inverse_t), f) == [1])
check('unit_norm_t', norm_u_t == 1)
check('original_unit_matches', original['unit'] == clean(
    dict(u_t=u_t, inverse_t=inverse_t, norm=norm_u_t)))
check('all_shifted_coordinates', [theta_s, u_s, inverse_s, h_s, uh_s] ==
      [[28, -26, 6], [1, -1, 0], [3, -3, 1], [-23, 26, -6], [-11, 13, -8]])
check('unit_inverse_s', remainder(multiply(u_s, inverse_s), shifted) == [1])
check('unit_norm_s', norm_u_s == 1)
point_value = compose(g, [5])[0]
check('point_value_and_norm', point_value == norm_h == -2039)
check('point_value_is_odd_square_mod_eight', point_value % 8 == 1)
check('original_point_matches', original['point'] == clean(
    dict(X=5, Y_squared=point_value, h_s=h_s, norm_h=norm_h)))

# Independently compare the printed arbitrary-coordinate square formula
# on a basis of all homogeneous quadratic monomials a^2,ab,ac,b^2,bc,c^2.
square_terms = []
for i in range(3):
    for j in range(i, 3):
        factor = 1 if i == j else 2
        square_terms.append(coordinates([0] * (i + j) + [factor], shifted))
check('arbitrary_square_formula', square_terms ==
      [[1, 0, 0], [0, 2, 0], [0, 0, 2], [0, 0, 1], [4, -12, 8], [8, -22, 10]])

records = []
for a in range(1, 8, 2):
    for b, c in product(range(8), repeat=2):
        root = [a, b, c]
        sq = coordinates(multiply(root, root), shifted)
        records.append(dict(root=root, square=[int(v % 8) for v in sq]))
expected_roots = set(product(range(1, 8, 2), range(8), range(8)))
check('complete_256_unit_roots', len(records) == 256 and
      {tuple(r['root']) for r in records} == expected_roots)
check('every_original_residue_record_matches', original['local']['enumeration'] == records)
square_residues = sorted({tuple(r['square']) for r in records})
check('sixteen_square_residues', len(square_residues) == 16)
check('every_original_square_residue_matches',
      original['local']['square_residues'] == clean(square_residues))
targets = {}
for name, elem in [('u', u_s), ('h', h_s), ('uh', uh_s)]:
    residue = [int(v % 8) for v in elem]
    targets[name] = clean(dict(exact=elem, residue=residue,
        matching_roots=[r['root'] for r in records if r['square'] == residue]))
check('every_original_target_matches', original['local']['targets'] == targets)
check('all_three_nonsquare_mod_eight', all(not v['matching_roots'] for v in targets.values()))
check('local_parameters_match', [original['local'][k] for k in
      ['modulus', 'ramification_index', 'residue_degree']] == [8, 3, 1])

# Only this rational factor of the K-completion is needed by the audit.
m = [-380, -774, -1062, -456, 258, 468, 104, -126, -6, 6, -6, 0, 1]
scaled_m = [Q(a * 2**i, 4) for i, a in enumerate(m)]
scaled_mod_two = [int(a % 2) for a in scaled_m]
check('rational_place_integral_scaled_polynomial', all(a.denominator == 1 for a in scaled_m))
check('rational_place_simple_root', scaled_mod_two == [1, 1] + [0] * 11)
g_mod_five_values = [int(compose(g, [r])[0] % 5) for r in range(5)]
check('cubic_no_roots_at_five', g_mod_five_values == [1, 3, 3, 2, 1])

thresholds = dict(actual_excluded_unit_witnesses=1,
    required_excluded_unit_witnesses=1, H_order_from_cited_theorem=2,
    full_unit_group_completeness_claimed=False)
check('original_thresholds_match', original['thresholds'] == thresholds)
# The mathematical reasons for |H|=2 and existence of the point are
# audited in L071. Numerical flags are not their proof.
check('original_reports_success', len(original['checks']) == 14 and
      all(original['checks'].values()) and original['failures'] == [])

failures = [name for name, passed in checks.items() if not passed]
data = clean(dict(
    scope='L071 exact certificate and input arithmetic; full theorem application is in L071',
    original_sha256=hashlib.sha256(original_bytes).hexdigest(),
    coordinate_checks=dict(theta_in_t=theta, theta_squared_in_t=theta2,
        t_in_theta=t_from_theta, theta_in_s=theta_s, inverse_in_s=inverse_s),
    multiplication_matrices=dict(u_t=multiplication_matrix(u_t, f),
        u_s=multiplication_matrix(u_s, shifted), h_s=multiplication_matrix(h_s, shifted)),
    norms=dict(u_t=norm_u_t, u_s=norm_u_s, h_s=norm_h),
    square_formula_monomials=['a^2', 'ab', 'ac', 'b^2', 'bc', 'c^2'],
    square_formula_columns=square_terms,
    rational_place=dict(m=m, scaled_m=scaled_m, scaled_mod_two=scaled_mod_two),
    g_mod_five_values=g_mod_five_values,
    local=dict(enumeration=records, square_residues=square_residues, targets=targets),
    thresholds=thresholds, checks=checks, failures=failures))
out = directory / 'audit-certificate.json'
out.write_text(json.dumps(data, indent=2) + '\n')
print(f'Independent checks: {sum(checks.values())}/{len(checks)}; failures: {failures}')
print('Full residue comparison: 256/256 unit roots; 16/16 square residues')
print(f'Corrected exact product: {clean(uh_s)}; excluded witnesses actual/required: 1/1')
print('Full Kummer image order: 2, conditional on the cited theorem application audited in L071')
print(f'Certificate: {out.relative_to(Path.cwd())}')
raise SystemExit(bool(failures))
