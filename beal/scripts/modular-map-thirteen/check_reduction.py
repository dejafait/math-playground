"""Exact full-chart arithmetic for L066; no finite-fiber sampling.

Reuse the audited L034 coefficient certificate, without executing its code.
Sparse bivariate monomials below are indexed by (t exponent, V exponent).
The open-cover and pole-order arguments are proved in the canonical lemma.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'five-isogeny-modular-norm' / 'norm-certificate.json'
DATA = json.loads(SOURCE.read_text())['polynomials_ascending']
a, b, h, g, d = (DATA[k] for k in ('a', 'b', 'h', 'g', 'd'))
checks = {}


def record(name, condition):
    checks[name] = bool(condition)


def clean(p):
    return {k: v for k, v in p.items() if v}


def plus(p, q):
    r = p.copy()
    for k, v in q.items():
        r[k] = r.get(k, 0) + v
    return clean(r)


def scale(p, c):
    return clean({k: c * v for k, v in p.items()})


def times(p, q):
    r = {}
    for (i, j), c in p.items():
        for (k, l), e in q.items():
            key = (i + k, j + l)
            r[key] = r.get(key, 0) + c * e
    return clean(r)


def power(p, n):
    r = {(0, 0): 1}
    for _ in range(n):
        r = times(r, p)
    return r


def poly(coefficients):
    return clean({(i, 0): c for i, c in enumerate(coefficients)})


def ev(coefficients, x):
    r = 0
    for c in reversed(coefficients):
        r = r * x + c
    return r


def serial(p):
    return [[i, j, c] for (i, j), c in sorted(p.items())]


ap, bp, hp, gp, dp = map(poly, (a, b, h, g, d))
# (a+by)(a-b-by) = a^2-ab-b^2*g on the curve.
product_residual = plus(
    plus(times(ap, ap), scale(times(ap, bp), -1)),
    plus(scale(times(times(bp, bp), gp), -1), times(dp, power(hp, 3))))
record('entire_integer_conjugate_product_identity', not product_residual)
record('source_denominator', dp == power({(0, 0): -16, (1, 0): 1}, 11))
record('source_degrees_and_leading_units',
       len(a) == 12 and len(b) == 11 and b[-1] == 1 and a[-1] == 743)

# Integral discriminant, independently recomputed from Weierstrass invariants.
b2, b4, b6, b8 = -4, -20, -79, -21
delta = -b2**2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6
record('curve_discriminant_unit', delta == -11**5 and delta % 13 != 0)

charts16 = {}
for label, y in [('2T', -61), ('3T', 60)]:
    n = ev(a, 16) + ev(b, 16) * y
    nc = ev(a, 16) - ev(b, 16) * (1 + y)
    derivative = 2*y + 1
    charts16[label] = {
        'x': 16, 'y': y, 'numerator': n, 'conjugate_numerator': nc,
        'curve_y_derivative': derivative,
        'residues': {'x': 16 % 13, 'y': y % 13, 'numerator': n % 13,
                     'conjugate_numerator': nc % 13,
                     'curve_y_derivative': derivative % 13}}
    record(label + '_on_integral_curve', y*y+y == ev(g, 16))
    record(label + '_relative_x_parameter', derivative % 13 != 0)
record('2T_regular_chart_unit', charts16['2T']['numerator'] == 0
       and charts16['2T']['conjugate_numerator'] == 11**22
       and charts16['2T']['conjugate_numerator'] % 13 != 0)
record('3T_reciprocal_chart_unit', charts16['3T']['numerator'] == 11**22
       and charts16['3T']['numerator'] % 13 != 0)
h16 = ev(h, 16)
record('h16_unit_and_cancelled_value', h16 == 11**8 and h16 % 13 != 0
       and -h16**3 == -121 * charts16['2T']['conjugate_numerator'])
record('complete_geometric_x16_factorization',
       [-ev(g, 16), 1, 1] == [-61*60, 61-60, 1]
       and (61+60) % 13 != 0)
record('complete_x16_special_fiber',
       sorted(y for y in range(13) if (y*y+y-ev(g, 16)) % 13 == 0)
       == sorted([(-61) % 13, 60 % 13]))

# At O: t=-x/y, w=-1/y. The exact projective equation is w*U=t^3.
# Its monomials here use (t,w); substituting w=t^3*V changes exponents.
U = {(0, 0): 1, (2, 0): 1, (1, 1): 10, (0, 1): -1, (0, 2): 20}
curve_in_tw = {(0, 1): 1, (0, 2): -1, (3, 0): -1,
               (2, 1): 1, (1, 2): 10, (0, 3): 20}
record('projective_origin_equation',
       curve_in_tw == plus(times({(0, 1): 1}, U), {(3, 0): -1}))
record('origin_U_unit_and_smooth_parameter', U[(0, 0)] == 1
       and curve_in_tw[(0, 1)] == 1)

R = plus({(i, 11-i): c for i, c in enumerate(a)},
         {(i, 10-i): -c for i, c in enumerate(b)})
R_sub = clean({(i+3*j, j): c for (i, j), c in R.items()})
Q = plus({(23-2*i, 11-i): c for i, c in enumerate(a)},
         {(20-2*i, 10-i): -c for i, c in enumerate(b)})
origin_numerator_residual = plus(R_sub, scale(times({(10, 0): 1}, Q), -1))
H = power({(0, 0): 1, (2, 1): -16}, 11)
den_tw = power({(1, 0): 1, (0, 1): -16}, 11)
den_sub = {(i+3*j, j): c for (i, j), c in den_tw.items()}
origin_denominator_residual = plus(den_sub, scale(times({(11, 0): 1}, H), -1))
record('origin_numerator_exact_factorization', not origin_numerator_residual)
record('origin_denominator_exact_factorization', not origin_denominator_residual)
record('origin_Q_is_integral', all(i >= 0 and j >= 0 for i, j in Q))
record('origin_Q_at_t0_V1_is_minus_one',
       sum(c for (i, j), c in Q.items() if i == 0) == -1)
record('origin_H_at_t0_V1_is_one',
       sum(c for (i, j), c in H.items() if i == 0) == 1)

failures = [k for k, ok in checks.items() if not ok]
certificate = {
    'source_coefficients': {k: DATA[k] for k in ('a', 'b', 'h', 'g', 'd')},
    'integer_product_residual': serial(product_residual),
    'curve_discriminant': {'integer': delta, 'residue': delta % 13},
    'x16_charts': charts16,
    'x16_curve_factorization': {'y_polynomial': [-ev(g, 16), 1, 1],
                               'linear_factors': [[61, 1], [-60, 1]],
                               'root_difference': 121, 'root_difference_residue': 121 % 13},
    'h16': {'integer': h16, 'residue': h16 % 13, 'cancelled_j': -121,
            'cancelled_j_residue': (-121) % 13},
    'origin_chart': {
        'monomial_convention': 'entries [i,j,c] denote c*t^i*V^j; U uses w instead of V',
        'U': serial(U), 'Q': serial(Q), 'H': serial(H),
        'numerator_residual': serial(origin_numerator_residual),
        'denominator_residual': serial(origin_denominator_residual),
        'Q_at_origin': -1, 'H_at_origin': 1,
        'reciprocal_j': 't*H/Q with w=t^3*V and V=1/U'},
    'pole_divisor': {'origin_order': 1, '3T_order': 11,
                    'degree_actual': 12, 'degree_required': 12,
                    'justification': 'Full open-cover and valuation proof in L066; not inferred from samples',
                    'separability': 'Simple pole at O, equivalently 13 does not divide degree 12'},
    'checks': checks, 'failures': failures}
path = HERE / 'reduction-certificate.json'
path.write_text(json.dumps(certificate, indent=2) + '\n')
print(f'Checks: {sum(checks.values())}/{len(checks)}; failures: {failures}')
print('Reduced pole orders at O/3T: 1/11; degree actual/required: 12/12')
print('Chart units: N(3T), conjugate N(2T), h(16), Q(O), H(O) all nonzero mod 13')
print(f'Certificate: {path}')
if failures:
    raise SystemExit(1)
