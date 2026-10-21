"""Exact integer checks for L143; the proof is in the canonical lemma."""
import json
from pathlib import Path


def mat(rows):
    return tuple(tuple(row) for row in rows)


def mm(a, b):
    return mat([[sum(x * y for x, y in zip(row, col))
                 for col in zip(*b)] for row in a])


def ms(c, a):
    return mat([[c * x for x in row] for row in a])


def ma(a, b):
    return mat([[x + y for x, y in zip(r, s)] for r, s in zip(a, b)])


def tr(a):
    return mat(zip(*a))


def va(a, b):
    return tuple(x + y for x, y in zip(a, b))


def vs(c, a):
    return tuple(c * x for x in a)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def bracket(a, b):
    return (2 * (a[1]*b[2] - a[2]*b[1]),
            2 * (a[2]*b[0] - a[0]*b[2]),
            2 * (a[0]*b[1] - a[1]*b[0]))


zero = (0, 0, 0)
identity = mat([[int(i == j) for j in range(4)] for i in range(4)])
m1 = mat([[0, 1, 0, 0], [-1, 0, 0, 0],
          [0, 0, 0, -1], [0, 0, 1, 0]])
m2 = mat([[0, 0, 1, 0], [0, 0, 0, 1],
          [-1, 0, 0, 0], [0, -1, 0, 0]])
m3 = mm(m1, m2)
mixed = (identity, m1, m2, m3)
pure = mixed[1:]
left_i = mat([[0, -1, 0, 0], [1, 0, 0, 0],
              [0, 0, 0, -1], [0, 0, 1, 0]])
left_j = mat([[0, 0, -1, 0], [0, 0, 0, 1],
              [1, 0, 0, 0], [0, -1, 0, 0]])
left_k = mm(left_i, left_j)
left = (left_i, left_j, left_k)
cyclic = ((1, 2, 3), (2, 3, 1), (3, 1, 2))


def tensor(coeff, basis):
    return [[tuple(sum(c[k] * m[a][b] for c, m in zip(coeff, basis))
                   for k in range(3)) for b in range(4)] for a in range(4)]


def calculate(p, q, coeff):
    P, Q, K = tensor(p, pure), tensor(q, pure), tensor(coeff, mixed)
    curvature = [[zero for _ in range(8)] for _ in range(8)]
    for a in range(4):
        for b in range(4):
            curvature[a][b] = P[a][b]
            curvature[a+4][b+4] = Q[a][b]
            curvature[a][b+4] = K[a][b]
            curvature[b+4][a] = vs(-1, K[a][b])
    full, projected = [], []
    b1, b2 = [], []
    for a in range(4):
        for mu in range(4):
            f = zero
            c = zero
            for k in range(8):
                f = va(f, vs(-1, bracket(curvature[a][k], curvature[k][mu+4])))
                f = va(f, bracket(curvature[mu+4][k], curvature[k][a]))
            for b in range(4):
                c = va(c, vs(-2, bracket(P[a][b], K[b][mu])))
                c = va(c, vs(-2, bracket(K[a][b], Q[b][mu])))
            full.append(f)
            projected.append(c)
    energy = sum(dot(c, K[a][mu]) for (a, mu), c in
                 zip(((a, mu) for a in range(4) for mu in range(4)), full))
    reduced = 0
    for k, i, j in cyclic:
        u, v = bracket(coeff[0], coeff[k]), bracket(coeff[i], coeff[j])
        reduced += 16 * (dot(q[k-1], va(u, vs(-1, v)))
                         - dot(p[k-1], va(u, v)))
    for a in range(4):
        for b in range(4):
            row, col = zero, zero
            for mu in range(4):
                row = va(row, bracket(K[a][mu], K[b][mu]))
                col = va(col, bracket(K[mu][a], K[mu][b]))
            expected_row, expected_col = zero, zero
            for k, i, j in cyclic:
                u, v = bracket(coeff[0], coeff[k]), bracket(coeff[i], coeff[j])
                expected_row = va(expected_row, vs(-2 * pure[k-1][a][b], va(u, v)))
                expected_col = va(expected_col, vs(2 * pure[k-1][a][b], va(u, vs(-1, v))))
            b1.append(row == expected_row)
            b2.append(col == expected_col)
    return {'full_equals_projection': full == projected,
            'energy_equals_reduction': energy == reduced,
            'row_moment_formula': all(b1), 'column_moment_formula': all(b2),
            'energy': energy, 'mixed_norm_squared': sum(dot(v, v) for row in K for v in row),
            'pure_first': p, 'pure_second': q, 'mixed_coefficients': coeff}


checks = {}
checks['quaternion_units'] = all(mm(m, m) == ms(-1, identity) for m in pure) and (
    mm(m1, m2) == m3 and mm(m2, m3) == m1 and mm(m3, m1) == m2)
checks['basis_invariant'] = all(mm(tr(l), mm(m, l)) == m for l in left for m in mixed)
checks['pure_skew'] = all(tr(m) == ms(-1, m) for m in pure)
checks['basis_orthogonal_norm_four'] = all(
    sum(m[a][b]*n[a][b] for a in range(4) for b in range(4)) == 4*int(i == j)
    for i, m in enumerate(mixed) for j, n in enumerate(mixed))
# ASD: (01,23), (02,13), (03,12) have signs (-,+,-).
checks['pure_ASD'] = all(m[0][1] == -m[2][3] and m[0][2] == m[1][3]
                         and m[0][3] == -m[1][2] for m in pure)
t1, t2, t3 = (1, 0, 0), (0, 1, 0), (0, 0, 1)
p, q, coeff = [t3, zero, zero], [zero]*3, [t1, t2, zero, zero]
witnesses = {
    'negative': calculate([vs(2, t3), zero, zero], p, coeff),
    'positive': calculate(p, [vs(2, t3), zero, zero], coeff),
    'noncommuting_zero': calculate(p, p, coeff),
    'zero_pure_blocks': calculate(q, q, coeff),
    'commuting_coefficients': calculate(p, q, [t1, t1, t1, t1]),
}
checks['negative_witness'] = witnesses['negative']['energy'] == -32
checks['positive_witness'] = witnesses['positive']['energy'] == 32
checks['zero_witnesses_nonzero_mixed'] = all(
    witnesses[name]['energy'] == 0 and witnesses[name]['mixed_norm_squared'] > 0
    for name in ('noncommuting_zero', 'zero_pure_blocks', 'commuting_coefficients'))
# Full quadratic projection checked on every coordinate vector and pair sum
# in the thirty-dimensional invariant module (polarization certificate).
basis = [[int(i == j) for i in range(30)] for j in range(30)]
vectors = basis + [[x+y for x, y in zip(a, b)]
                   for i, a in enumerate(basis) for b in basis[i+1:]]
vectors += [[((i+3)*(j+5) % 11)-5 for i in range(30)] for j in range(20)]
test_failures = []
for n, v in enumerate(vectors):
    v3 = [tuple(v[i:i+3]) for i in range(0, 30, 3)]
    result = calculate(v3[:3], v3[3:6], v3[6:])
    for field in ('full_equals_projection', 'energy_equals_reduction',
                  'row_moment_formula', 'column_moment_formula'):
        if not result[field]:
            test_failures.append({'test': n, 'field': field, 'data': result})
checks['all_exact_test_cases'] = not test_failures
certificate = {'checks': checks, 'failures': [k for k, v in checks.items() if not v],
               'test_failures': test_failures, 'exact_cases': len(vectors),
               'matrices': {'mixed': mixed, 'left': left}, 'witnesses': witnesses,
               'normalization': '-tr(XY)/2; [Ti,Tj]=2 epsilon_ijk Tk',
               'required_sign': 'energy >= 0 for a universal vanishing-forcing Bochner argument',
               'actual_negative_energy': witnesses['negative']['energy'],
               'zero_equation': '16 sum_cyclic (<q_k-p_k,[A0,Ak]>-<p_k+q_k,[Ai,Aj]>)=0'}
path = Path(__file__).with_name('product_coupling_certificate.json')
path.write_text(json.dumps(certificate, indent=2) + '\n')
print(f'Exact checks: {sum(checks.values())}/{len(checks)}; cases: {len(vectors)}; failures: {certificate["failures"]}')
print('Actual mixed energies: -32, +32, 0; required universal sign: >=0.')
print(f'Certificate: {path}')
if certificate['failures']:
    raise SystemExit(1)
