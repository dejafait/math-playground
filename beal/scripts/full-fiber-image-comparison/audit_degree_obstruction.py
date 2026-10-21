"""Independent exact arithmetic audit of L040; universal reasoning is in L040.

No construction modules are imported. Coprimality is certified by Bezout
identities, rather than by the construction's Sylvester determinants.
"""
import json
from math import comb
from pathlib import Path

BASE = Path(__file__).resolve().parent
old = json.loads((BASE / 'degree-obstruction-certificate.json').read_text())
source = json.loads((BASE.parent / 'five-isogeny-modular-norm/norm-certificate.json').read_text())['polynomials_ascending']


def clean(p, modulus=None):
    return {i: (v % modulus if modulus else v) for i, v in p.items()
            if (v % modulus if modulus else v)}


def poly(a):
    return clean(dict(enumerate(a)))


def add(p, q, scale=1, modulus=None):
    r = p.copy()
    for i, v in q.items():
        r[i] = r.get(i, 0) + scale * v
    return clean(r, modulus)


def mul(p, q, modulus=None):
    r = {}
    for i, v in p.items():
        for j, w in q.items():
            r[i+j] = r.get(i+j, 0) + v*w
    return clean(r, modulus)


def power(p, n, modulus=None):
    r = {0: 1}
    # Binary powering, independently of the construction's repeated product.
    while n:
        if n & 1:
            r = mul(r, p, modulus)
        p = mul(p, p, modulus)
        n //= 2
    return r


def vector(p, length=None):
    return [p.get(i, 0) for i in range(length or (max(p, default=0)+1))]


def ev(p, x):
    total = 0
    for i in range(max(p, default=0), -1, -1):
        total = total*x + p.get(i, 0)
    return total


def divide5(p, q):
    p, q = clean(p, 5), clean(q, 5)
    quotient = {}
    while p and max(p) >= max(q):
        degree = max(p) - max(q)
        term = {degree: p[max(p)] * pow(q[max(q)], -1, 5) % 5}
        quotient = add(quotient, term, modulus=5)
        p = add(p, mul(term, q, 5), -1, 5)
    return quotient, p


def bezout5(p, q):
    r0, r1 = clean(p, 5), clean(q, 5)
    u0, u1, v0, v1 = {0: 1}, {}, {}, {0: 1}
    while r1:
        quotient, remainder = divide5(r0, r1)
        r0, r1 = r1, remainder
        u0, u1 = u1, add(u0, mul(quotient, u1, 5), -1, 5)
        v0, v1 = v1, add(v0, mul(quotient, v1, 5), -1, 5)
    unit = {0: pow(r0[max(r0)], -1, 5)}
    return mul(r0, unit, 5), mul(u0, unit, 5), mul(v0, unit, 5)


# These literal source coefficients were previously audited in L034.
h = poly([9789217, 4971236, 1333262, -52820, 1])
d = {i: comb(11, i)*(-16)**(11-i) for i in range(12)}
a, b, g = (poly(source[key]) for key in ('a', 'b', 'g'))
J = add({i: 2*v for i, v in a.items()}, b, -1)
h3 = power(h, 3)
checks = {}
for label, candidate, key in [('h', h, 'h'), ('d', d, 'd'), ('J', J, 'jcoef')]:
    checks[label+'_source_match'] = candidate == poly(source[key])
    checks[label+'_L040_match'] = candidate == poly(old['polynomials_ascending'][label])
checks['J_degree_11'] = max(J) == 11
checks['h3_monic_degree_12'] = max(h3) == 12 and h3[12] == 1
elimination = add(add(add(mul(a, a), mul(a, b), -1), mul(mul(b, b), g), -1), mul(d, h3))
checks['necessary_relation_elimination'] = not elimination

branches = {}
for scalar, p0, q0, exponent in [(0, [1, 1, 1], [2, 4, 1], 3),
                                 (3, [2, 0, 3, 1], [4, 4, 4, 1], 2)]:
    F = clean(add(add(h3, J, scalar), d, -scalar*scalar), 5)
    p, q = power(poly(p0), exponent, 5), power(poly(q0), exponent, 5)
    gcd, u, v = bezout5(p, q)
    identity = add(mul(u, p, 5), mul(v, q, 5), modulus=5)
    recorded = old['integral_branch_cases'][str(scalar)]
    checks[f'branch_{scalar}_complete_coefficients'] = F == mul(p, q, 5)
    checks[f'branch_{scalar}_recorded_coefficients'] = vector(F) == recorded['F_mod5']
    checks[f'branch_{scalar}_recorded_blocks'] = [vector(p), vector(q)] == recorded['blocks']
    checks[f'branch_{scalar}_bezout_one'] = gcd == identity == {0: 1}
    checks[f'branch_{scalar}_monic_six_plus_six'] = max(p) == max(q) == 6 and p[6] == q[6] == 1
    branches[str(scalar)] = {'F': vector(F), 'blocks': [vector(p), vector(q)],
                             'bezout_u': vector(u), 'bezout_v': vector(v),
                             'bezout_identity': vector(identity),
                             'block_degree_actual': [max(p), max(q)], 'point_degree_required': 11}

# Exact coefficient rows of G(w,t), ordered by t-degree 0,1,2, then w-degree.
G = [{12-i: -v for i, v in d.items()},
     {12-i: v for i, v in J.items()},
     {12-i: v for i, v in h3.items()}]
Gbar = clean(G[0], 5)
checks['G_constant_t_row'] = G[0] == mul({1: -1}, power({0: 1, 1: -16}, 11))
checks['G_nonnegative_w_degrees'] = all(min(row) >= 0 for row in G)
checks['G_value_at_zero_is_t_squared'] = [row.get(0, 0) for row in G] == [0, 0, 1]
checks['G_derivative_mod5_is_minus_one'] = Gbar.get(1, 0) == 4
checks['G_reduction_recorded'] = vector(Gbar) == old['nonintegral_case']['G_mod5']
checks['integral_x_reduction'] = clean(d, 5) == power({0: -1, 1: 1}, 11, 5)
units = {'h16': ev(h, 16), 'J16': ev(J, 16)}
checks['unit_values_recorded'] = all(value == old['nonintegral_case'][key] for key, value in units.items())
checks['both_values_units'] = all(value % 5 == 1 for value in units.values())

# Exceptional charts: numerator at 2T, conjugate at 3T, removable limit.
num2, num3 = ev(a, 16)-61*ev(b, 16), ev(a, 16)+60*ev(b, 16)
checks['removable_chart'] = num2 == 0 and num3 != 0 and -ev(h, 16)**3 == -121*num3
checks['descent_exception_jT'] = ev(a, 5)+5*ev(b, 5) == -24729001*ev(d, 5)
checks['exceptional_scalar_residues'] = (-121) % 5 == (-24729001) % 5 == 4

certificate = {'source': 'scripts/five-isogeny-modular-norm/norm-certificate.json',
               'polynomials_ascending': {key: vector(p) for key, p in [('h', h), ('d', d), ('J', J)]},
               'elimination_residual': vector(elimination), 'branches': branches,
               'reciprocal_coefficients_by_t_degree': [vector(p, 13) for p in G],
               'reciprocal_origin_coefficients': [row.get(0, 0) for row in G],
               'reciprocal_derivative_coefficients': [row.get(1, 0) for row in G],
               'reciprocal_reduction': vector(Gbar), 'unit_values': units,
               'exceptional_charts': {'numerator_2T': num2, 'numerator_3T': num3,
                                       'j_2T': -121, 'j_T': -24729001},
               'bounds': {'block_max_actual': 6, 'point_degree_required': 11,
                          'total_actual': 12, 'total_required': 12,
                          'derivative_mod5_actual': 4, 'derivative_required': 'nonzero'},
               'checks': checks, 'failures': [key for key, ok in checks.items() if not ok]}
output = BASE / 'degree-obstruction-audit-certificate.json'
output.write_text(json.dumps(certificate, indent=2) + '\n')
print(f'Checks: {sum(checks.values())}/{len(checks)}; failures: {certificate["failures"]}')
print('Block max actual=6 < point degree required=11; total actual=12, required=12')
print('Hensel derivative actual=4 mod 5, required nonzero; origin=t^2 exactly')
print(f'Certificate: {output.relative_to(BASE.parent.parent)}')
if certificate['failures']:
    raise SystemExit(1)
