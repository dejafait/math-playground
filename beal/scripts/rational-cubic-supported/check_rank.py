"""Exact finite arithmetic supporting L077; theorem applications are in its proof."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c * x for x in a)


def mul(a, b, rel=(-1, -1, 1)):
    p = [Q(0)] * 5
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            p[i+j] += x*y
    for k in (4, 3):
        for j in range(3):
            p[k-3+j] += p[k] * rel[j]
    return tuple(p[:3])


ONE, T = (Q(1), Q(0), Q(0)), (Q(0), Q(1), Q(0))


def matrix(a):
    columns = [mul(a, e) for e in ((1, 0, 0), (0, 1, 0), (0, 0, 1))]
    return [[c[i] for c in columns] for i in range(3)]


def det(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


def norm(a):
    return det(matrix(a))


def inv(a):
    m = [row + [ONE[i]] for i, row in enumerate(matrix(a))]
    for j in range(3):
        pivot = next(i for i in range(j, 3) if m[i][j])
        m[j], m[pivot] = m[pivot], m[j]
        c = m[j][j]
        m[j] = [x/c for x in m[j]]
        for i in range(3):
            if i != j:
                c = m[i][j]
                m[i] = [x-c*y for x, y in zip(m[i], m[j])]
    return tuple(row[3] for row in m)


def eval_mod(a, t, modulus):
    return sum(int(c) * pow(t, i, modulus) for i, c in enumerate(a)) % modulus


def shift_to_s(a):
    return a[0]-a[1]+a[2], a[1]-2*a[2], a[2]


def residue(a, modulus=8):
    assert all(c.denominator == 1 for c in a)
    return tuple(int(c) % modulus for c in a)


s = add(T, ONE)
v, u = scale(-1, inv(T)), scale(-1, T)
derivative = (Q(1), Q(-2), Q(3))
a = mul(derivative, inv(mul(s, s)))
b = scale(11, inv(mul(a, a)))
w = mul(a, b)
h = (Q(-3), Q(14), Q(-6))  # 5-theta
generators = [scale(-1, ONE), v, s, a, b]
norms = [norm(x) for x in generators]

# Norm coordinates in Q*/Q*^2, ordered (-1,2,11).
norm_columns = [(1,0,0), (0,0,0), (0,1,0), (0,0,1), (0,0,1)]
kernel = [bits for bits in product(range(2), repeat=5)
          if all(sum(bits[j]*norm_columns[j][i] for j in range(5)) % 2 == 0
                 for i in range(3))]

# Full finite unit-square table in the proven maximal dyadic basis (1,s,s^2).
rs = (2, -6, 4)
unit_squares = [
    {"root": r, "square": residue(mul(r, r, rs))}
    for r in product(range(8), repeat=3) if r[0] % 2
]
targets = {name: {"exact_s": shift_to_s(z), "residue": residue(shift_to_s(z)),
                  "roots": [r["root"] for r in unit_squares
                            if r["square"] == residue(shift_to_s(z))]}
           for name, z in (("v", v), ("vh", mul(v,h)), ("w", w), ("wh", mul(w,h)),
                           ("vw", mul(v,w)), ("vwh", mul(mul(v,w),h)))}

# f discriminant for monic X^3 + A X^2 + B X + C.
A, B, C = -1, 1, 1
discriminant = A*A*B*B - 4*B**3 - 4*A**3*C - 27*C*C + 18*A*B*C
squares11 = sorted({i*i % 11 for i in range(1, 11)})
roots11 = [i for i in range(11) if (i**3-i*i+i+1) % 11 == 0]

checks = {
    "discriminant_minus_44": discriminant == -44,
    "minkowski_strict_bound": 44*16 < 27**2,  # sqrt(44)<27/4, pi>3
    "real_root_bounds": Q(-3,5)**3-Q(-3,5)**2+Q(-3,5)+1 < 0
                        < Q(-1,2)**3-Q(-1,2)**2+Q(-1,2)+1,
    "conrad_strict_bound": 2**3 < 3**2 and 4*3+24 < 44,
    "v_coordinates": v == (1,-1,1) and mul(v,u) == ONE,
    "a_coordinates": a == (9,-7,5),
    "integral_b": all(c.denominator == 1 for c in b),
    "a_s_squared_equals_derivative": mul(a,mul(s,s)) == derivative,
    "a_squared_b_equals_11": mul(mul(a,a),b) == scale(11,ONE),
    "w_equals_11_over_a": w == scale(11,inv(a)),
    "exact_generator_norms": norms == [-1,1,2,11,11],
    "w_norm_square": norm(w) == 121,
    "complete_norm_kernel_bits": kernel == [(0,i,0,j,j) for i,j in product(range(2),repeat=2)],
    "eleven_factorization": all((i**3-i*i+i+1-(i-6)*(i-3)**2) % 11 == 0 for i in range(11)),
    "eleven_roots": roots11 == [3,6],
    "eleven_generator_residues": eval_mod(a,3,11)==0 and eval_mod(a,6,11)!=0,
    "v_eleven_residues": [eval_mod(v,i,11) for i in (6,3)] == [9,7],
    "v_eleven_square_types": 9 in squares11 and 7 not in squares11 and 10 not in squares11,
    "entire_dyadic_unit_table": len(unit_squares)==256 and len({r['root'] for r in unit_squares})==256,
    "v_outside_full_H2": not targets['v']['roots'] and not targets['vh']['roots'],
    "w_outside_full_H2": not targets['w']['roots'] and not targets['wh']['roots'],
    "vw_in_full_H2": bool(targets['vw']['roots']) or bool(targets['vwh']['roots']),
}

# The theorem-certified generators and local images are justified in L077.
# Rows are quotient tests: dyadic H2 membership; rational 11 valuation.
dyadic_w = 1 if checks['w_outside_full_H2'] and checks['vw_in_full_H2'] else None
restriction_matrix = [[1, dyadic_w], [0,1], [0,1]]
rank = 2 if checks['v_outside_full_H2'] and dyadic_w == 1 else None
checks['combined_matrix_rank_two'] = rank == 2
failures = [key for key, ok in checks.items() if not ok]

def encode(obj):
    if isinstance(obj, Q):
        return int(obj) if obj.denominator == 1 else str(obj)
    raise TypeError(type(obj).__name__)

certificate = {
    'field': {'polynomial_ascending': [1,1,-1,1], 'discriminant': discriminant},
    'generators_t': dict(zip(['minus_one','v','s','a','b'], generators)),
    'norms': norms, 'w_t': w,
    'norm_columns_sign_two_eleven': norm_columns, 'full_norm_kernel_bits': kernel,
    'eleven': {'roots': roots11, 'squares': squares11,
               'v_residues_rational_ramified': [eval_mod(v,i,11) for i in (6,3)],
               'w_prime_valuations': [1,1],
               'valuation_note': 'Ideal valuations are proved from norms and prime factorization in L077.'},
    'dyadic': {'modulus': 8, 'basis': ['1','s','s^2'],
               'unit_square_table': unit_squares, 'targets': targets},
    'restriction': {'basis': ['v','w'], 'rows': ['dyadic','rational_11_first','rational_11_second'],
                    'matrix': restriction_matrix, 'rank': rank,
                    'note': 'Matrix represents the image using its two nonzero quotient coordinates; the repeated rows are not independent.'},
    'thresholds': {'combined_rank_actual': rank, 'second_direction_required': 2,
                   'supported_unit_dimension': 16, 'certified_removed_directions': rank,
                   'unit_kernel_upper_bound': 14, 'unit_kernel_required_upper_bound': 11,
                   'localized_class_kernel_computed': False},
    'checks': checks, 'failures': failures,
    'initial_probe': {'path': 'initial-rank-certificate.json',
                      'failed_expectation': 'w lies in H2',
                      'correction': 'w is outside H2; vw is inside H2. Rank two never required w in H2.'},
}
path = Path(__file__).with_name('rank-certificate.json')
path.write_text(json.dumps(certificate, default=encode, indent=2)+'\n')
print(f'Checks: {sum(checks.values())}/{len(checks)}; failures: {failures}')
print(f'Combined restriction rank actual/second-direction threshold: {rank}/2')
print('Certified supported-unit upper bound/required: 14/11; class kernel uncomputed')
print(f'Certificate: {path.relative_to(Path.cwd())}')
raise SystemExit(bool(failures))
