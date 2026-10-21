#!/usr/bin/env python3
"""Independent exact replay of L066; imports no construction code.

Polynomial dictionaries use exponent pairs and integer coefficients.
Source coefficients are the previously source-audited L034 artifact.
Scheme coverage and the interpretation of orders are proved in L066.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
original = json.loads((ROOT / 'scripts/modular-map-thirteen/reduction-certificate.json').read_text())
source = json.loads((ROOT / 'scripts/five-isogeny-modular-norm/norm-certificate.json').read_text())['polynomials_ascending']
checks = {}


def check(name, condition):
    checks[name] = bool(condition)


def add(*polys):
    out = {}
    for poly in polys:
        for e, c in poly.items():
            out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c}


def scale(poly, c):
    return {e: c*v for e, v in poly.items() if c*v}


def mul(p, q):
    out = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            e = (i+k, j+l)
            out[e] = out.get(e, 0) + a*b
    return {e: c for e, c in out.items() if c}


def power(p, n):
    out = {(0, 0): 1}
    for _ in range(n):
        out = mul(out, p)
    return out


def evaluate(p, x, y):
    return sum(c*x**i*y**j for (i, j), c in p.items())


def listed(p):
    return [[i, j, c] for (i, j), c in sorted(p.items())]


def univariate(coeffs):
    return {(i, 0): c for i, c in enumerate(coeffs) if c}


def homogeneous(coeffs, degree):
    return {(i, degree-i): c for i, c in enumerate(coeffs) if c}


def substitute_w(p):
    # Substitution (t,w) -> (t,t^3 V), not division by t.
    return {(i+3*j, j): c for (i, j), c in p.items()}


one, t, w = {(0, 0): 1}, {(1, 0): 1}, {(0, 1): 1}
polys = {key: univariate(source[key]) for key in ('a', 'b', 'g', 'd', 'h')}
for key in polys:
    check('source_'+key, original['source_coefficients'][key] == source[key])
a, b, g, d, h = (polys[key] for key in ('a', 'b', 'g', 'd', 'h'))
check('g_model', g == univariate([-20, -10, -1, 1]))
check('d_model', d == power(add(t, scale(one, -16)), 11))
check('b_source_factors', b == mul(univariate(source['b1']), univariate(source['b2'])))
product_residual = add(mul(a, a), scale(mul(a, b), -1),
                       scale(mul(mul(b, b), g), -1), mul(d, power(h, 3)))
check('integer_product_identity', not product_residual)
check('original_product_residual', original['integer_product_residual'] == [] and not product_residual)

# Standard integral Weierstrass invariants, recomputed from a_i.
a1, a2, a3, a4, a6 = 0, -1, 1, -10, -20
b2 = a1*a1+4*a2
b4 = 2*a4+a1*a3
b6 = a3*a3+4*a6
b8 = a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
delta = -b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
discriminant = {'integer': delta, 'residue': delta % 13}
check('discriminant', discriminant == original['curve_discriminant'] and delta == -11**5)
check('smooth_at_13', delta % 13 != 0)

av, bv, gv, hv = [evaluate(p, 16, 0) for p in (a, b, g, h)]
charts = {}
for name, y in [('2T', -61), ('3T', 60)]:
    row = dict(x=16, y=y, numerator=av+bv*y,
               conjugate_numerator=av-bv-bv*y, curve_y_derivative=2*y+1)
    row['residues'] = {k: v % 13 for k, v in row.items()}
    charts[name] = row
    check(name+'_on_curve', y*y+y == gv)
    check(name+'_full_values', row == original['x16_charts'][name])
    check(name+'_parameter', (2*y+1) % 13 != 0)
check('2T_unit_conjugate', charts['2T']['conjugate_numerator'] == 11**22)
check('3T_unit_numerator', charts['3T']['numerator'] == 11**22)
factor_residual = add(mul(add(w, scale(one, 61)), add(w, scale(one, -60))),
                      scale(add(power(w, 2), w, scale(one, -gv)), -1))
factor_data = dict(y_polynomial=[-gv, 1, 1], linear_factors=[[61, 1], [-60, 1]],
                   root_difference=121, root_difference_residue=121 % 13)
check('x16_factorization', not factor_residual and factor_data == original['x16_curve_factorization'])
check('disjoint_sections', 121 % 13 != 0)
check('h16_and_cancelled_value', hv == 11**8 and
      original['h16'] == dict(integer=hv, residue=hv % 13, cancelled_j=-121, cancelled_j_residue=(-121) % 13)
      and -hv**3 == -121 * charts['2T']['conjugate_numerator'])

# Substitute X=-t, Y=1, Z=-w in the homogeneous Weierstrass equation.
X, Z = scale(t, -1), scale(w, -1)
projective = add(Z, scale(mul(X, Z), a1), scale(power(Z, 2), a3),
                 scale(power(X, 3), -1), scale(mul(power(X, 2), Z), -a2),
                 scale(mul(X, power(Z, 2)), -a4), scale(power(Z, 3), -a6))
U = add(one, power(t, 2), scale(w, -1), scale(mul(t, w), 10), scale(power(w, 2), 20))
equation_residual = add(projective, mul(w, U), scale(power(t, 3), -1))
check('projective_origin_equation', not equation_residual)
check('U_complete', listed(U) == original['origin_chart']['U'])
check('origin_implicit_derivative', projective.get((0, 1)) == -1 and evaluate(U, 0, 0) == 1)

R = add(homogeneous(source['a'], 11), scale(homogeneous(source['b'], 10), -1))
Rsub = substitute_w(R)
check('numerator_t_order_exact_10', min(i for i, j in Rsub) == 10)
Q = {(i-10, j): c for (i, j), c in Rsub.items()}
Dsub = substitute_w(homogeneous(source['d'], 11))
check('denominator_t_order_exact_11', min(i for i, j in Dsub) == 11)
H = {(i-11, j): c for (i, j), c in Dsub.items()}
qres = add(Rsub, scale(mul(power(t, 10), Q), -1))
hres = add(Dsub, scale(mul(power(t, 11), power(add(one, scale(mul(power(t, 2), w), -16)), 11)), -1))
check('Q_complete', listed(Q) == original['origin_chart']['Q'])
check('H_complete', listed(H) == original['origin_chart']['H'])
check('origin_factorizations', not qres and not hres)
check('original_origin_residuals', original['origin_chart']['numerator_residual'] == [] and
      original['origin_chart']['denominator_residual'] == [] and not qres and not hres)
check('origin_leading_units', evaluate(Q, 0, 1) == original['origin_chart']['Q_at_origin'] == -1 and
      evaluate(H, 0, 1) == original['origin_chart']['H_at_origin'] == 1)
check('source_degrees', len(source['a']) == 12 and len(source['b']) == 11 and
      source['a'][-1] == 743 and source['b'][-1] == 1)
orders = dict(origin_order=11-10, **{'3T_order': 11}, degree_actual=12, degree_required=12)
check('recorded_orders', all(original['pole_divisor'][k] == v for k, v in orders.items()))
check('degree_prime_to_characteristic', 12 % 13 != 0)
failures = [k for k, v in checks.items() if not v]
certificate = dict(
    provenance='L034 source-audited coefficient lists; no construction code imported or executed',
    source_coefficients={k: source[k] for k in polys},
    invariants=dict(b2=b2, b4=b4, b6=b6, b8=b8, **discriminant),
    x16_charts=charts, x16_factorization=factor_data,
    h16=dict(value=hv, residue=hv % 13, cancelled_j=-121),
    origin_polynomials=dict(U=listed(U), R=listed(R), Q=listed(Q), H=listed(H)),
    residuals=dict(conjugate_product=listed(product_residual), x16_factorization=listed(factor_residual),
                   projective_equation=listed(equation_residual), numerator=listed(qres), denominator=listed(hres)),
    leading_units=dict(U=1, Q=evaluate(Q, 0, 1), H=evaluate(H, 0, 1), reciprocal_j=-1),
    orders=orders,
    qualification='Orders require L066 scheme coverage and uniformizer proof; no finite-fiber sampling or rank bound',
    checks=checks, failures=failures)
output = ROOT / 'scripts/modular-map-thirteen/audit-certificate.json'
output.write_text(json.dumps(certificate, indent=2)+'\n')
print(f'Checks: {sum(checks.values())}/{len(checks)}; failures: {failures}')
print('With L066 coverage proof: pole orders actual/required 1,11 / 1,11; degree actual/required 12/12')
print('Certificate: '+str(output.relative_to(ROOT)))
raise SystemExit(bool(failures))
