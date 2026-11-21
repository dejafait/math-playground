"""Independent exact algebra audit of C020r/s; no previous script is imported.

The uniform sign and multiplicity arguments are audited in the canonical
proofs. This certificate checks their polynomial identities and finite
order cases, and does not replace the analytic arguments.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

NAMES = ('y', 't', 'a', 'b', 'c', 'r', 'u', 'v', 'e')
ZERO = (0,) * len(NAMES)


def const(value):
    return {ZERO: F(value)} if value else {}


def add(*terms):
    out = {}
    for term in terms:
        for exponent, value in term.items():
            out[exponent] = out.get(exponent, F(0)) + value
    return {exponent: value for exponent, value in out.items() if value}


def scale(term, value):
    return {exponent: value * coefficient for exponent, coefficient in term.items()
            if value * coefficient}


def mul(*terms):
    out = const(1)
    for term in terms:
        nxt = {}
        for p, cp in out.items():
            for q, cq in term.items():
                exponent = tuple(i + j for i, j in zip(p, q))
                nxt[exponent] = nxt.get(exponent, F(0)) + cp * cq
        out = {exponent: value for exponent, value in nxt.items() if value}
    return out


def power(term, exponent):
    return mul(*([term] * exponent))


def derivative(term, variable):
    i = NAMES.index(variable)
    out = {}
    for exponent, coefficient in term.items():
        if exponent[i]:
            reduced = list(exponent)
            reduced[i] -= 1
            out[tuple(reduced)] = coefficient * exponent[i]
    return out


def sub(term, replacements):
    out = {}
    for exponent, coefficient in term.items():
        factors = [const(coefficient)]
        for name, degree in zip(NAMES, exponent):
            factors.append(power(replacements.get(name, variables[name]), degree))
        out = add(out, mul(*factors))
    return out


def encode(term):
    return [{'powers': list(exponent), 'coefficient': str(coefficient)}
            for exponent, coefficient in sorted(term.items())]


variables = {}
for i, name in enumerate(NAMES):
    exponent = list(ZERO)
    exponent[i] = 1
    variables[name] = {tuple(exponent): F(1)}
y, t, a, b, c, r, u, v, e = (variables[name] for name in NAMES)
checks, identities = {}, {}


def check(name, lhs, rhs):
    difference = add(lhs, scale(rhs, -1))
    checks[name] = not difference
    identities[name] = {'lhs': encode(lhs), 'rhs': encode(rhs),
                        'difference': encode(difference)}


def T(term):
    return add(term, derivative(term, 'y'), mul(t, derivative(derivative(term, 'y'), 'y')))


S = add(power(y, 2), scale(a, -1))
R = power(S, 2)
A = add(S, scale(mul(t, y), 8))
J = add(R, scale(mul(y, S), 4), scale(mul(t, add(scale(power(y, 2), 3), scale(a, -1))), 4))
K = mul(S, A)
Q = add(power(y, 2), mul(b, y), c)
check('J_direct_derivative', T(R), J)
check('K_direct_derivative', add(R, scale(mul(t, derivative(R, 'y')), 2)), K)
check('product_rule', T(mul(R, Q)),
      add(mul(Q, J), mul(derivative(Q, 'y'), K), mul(t, derivative(derivative(Q, 'y'), 'y'), R)))
eta_value = scale(mul(t, add(mul(add(scale(t, 16), const(-5)), power(y, 2)), scale(a, -1))), 4)
check('J_remainder_at_A_roots', add(J, scale(eta_value, -1)),
      mul(A, add(S, mul(add(const(4), scale(t, -8)), y))))
check('J_at_minus_h_cleared', add(J, scale(scale(mul(t, a), 8), -1)),
      mul(S, add(S, scale(y, 4), scale(t, 12))))
check('phi_derivative_numerator',
      add(mul(derivative(S, 'y'), A), scale(mul(S, derivative(A, 'y')), -1)),
      scale(mul(t, add(power(y, 2), a)), 8))
check('J_reflection', add(J, scale(sub(J, {'y': scale(y, -1)}), -1)), scale(mul(y, S), 8))

su, sv = sub(S, {'y': u}), sub(S, {'y': v})
au, av = sub(A, {'y': u}), sub(A, {'y': v})
w, z = add(u, v), mul(u, v)
P = add(z, a)
check('rational_difference_numerator', add(mul(sv, au), scale(mul(su, av), -1)),
      scale(mul(t, add(v, scale(u, -1)), P), 8))
check('A_product_symmetric', mul(au, av),
      add(power(P, 2), scale(mul(a, power(w, 2)), -1),
          scale(mul(t, w, add(z, scale(a, -1))), 8), scale(mul(power(t, 2), z), 64)))
check('E_symmetric', add(mul(au, av), scale(mul(power(t, 2), P), 8)),
      add(mul(P, add(P, scale(mul(t, w), 8), scale(power(t, 2), 72))),
          scale(mul(a, power(add(w, scale(t, 8)), 2)), -1)))

V = add(power(r, 2), scale(t, 12), const(-4))
U = add(power(r, 2), scale(t, 8), const(-4))
rm2, rp2 = add(r, const(-2)), add(r, const(2))
Nminus = add(mul(rp2, V), scale(mul(r, a), -2))
Nplus = add(mul(rm2, V), scale(mul(r, a), -2))
lowfactor = add(scale(mul(r, power(y, 2)), 2), scale(mul(r, rp2, y), 2), Nminus)
highfactor = add(scale(mul(r, power(y, 2)), 2), scale(mul(r, rm2, y), -2), Nplus)
relation = add(mul(add(power(r, 2), const(-4)), power(V, 2)), scale(mul(power(r, 2), a, U), -4))
check('entire_adjacent_pair_factorization_cleared',
      add(mul(lowfactor, highfactor), scale(mul(power(r, 2), J), -4)), relation)
check('pair_sum_products', add(Nminus, Nplus), scale(mul(r, add(V, scale(a, -2))), 2))
check('pair_difference_products', add(Nminus, scale(Nplus, -1)), scale(V, 4))
check('pair_linear_equation', add(scale(mul(rp2, Nplus), -1), mul(rm2, Nminus)), scale(mul(r, a), 8))

# Here r stands for W of either sign. No branch is chosen by this algebra.
B = add(mul(add(scale(t, 10), const(-3)), power(r, 3)),
        mul(add(const(6), scale(t, -24)), power(r, 2)),
        mul(add(scale(power(t, 2), 48), scale(t, -60), const(12)), r),
        scale(power(t, 2), -192), scale(t, 136), const(-24))
cleared_E = add(mul(power(rm2, 2), power(V, 2), U),
                scale(mul(r, rm2, V, add(scale(mul(t, rm2), 8), scale(power(t, 2), 72)), U), 2),
                scale(mul(add(power(r, 2), const(-4)), power(V, 2), power(add(rm2, scale(t, 8)), 2)), -1))
check('outer_E_factorization_cleared', cleared_E, scale(mul(t, rm2, V, B), 8))
upper = add(mul(add(scale(t, 10), const(-3)), power(e, 3)),
            scale(mul(add(const(1), scale(t, -3)), power(e, 2)), -12),
            scale(mul(t, add(const(3), scale(t, -4)), e), -12), scale(power(t, 2), -96))
lower = add(mul(add(const(3), scale(t, -10)), power(e, 3)),
            scale(mul(add(const(2), scale(t, -7)), power(e, 2)), 12),
            scale(mul(add(const(4), scale(t, -13), scale(power(t, 2), -4)), e), 12),
            scale(mul(t, add(const(5), scale(t, -18))), 16))
check('upper_branch_expansion', sub(B, {'r': add(e, const(2))}), upper)
check('lower_branch_expansion', sub(B, {'r': add(scale(e, -1), const(-2))}), lower)
decreasing = add(const(4), scale(t, -13), scale(power(t, 2), -4))
check('lower_linear_endpoint_difference', add(decreasing, const(-F(13, 162))),
      mul(add(const(F(5, 18)), scale(t, -1)), add(const(F(127, 9)), scale(t, 4))))

# Independent denominator-cleared translation; u=l, v=k, x=(2ky-l)/(2k).
xnum = add(scale(mul(v, y), 2), scale(u, -1))
check('centering_squared_factor', add(scale(v, 4), scale(mul(u, xnum), 2), power(xnum, 2)),
      add(scale(mul(power(v, 2), power(y, 2)), 4), scale(power(u, 2), -1), scale(v, 4)))
check('quadratic_discriminant_translation',
      add(scale(add(power(u, 2), mul(b, u), c), 4), scale(power(add(b, scale(u, 2)), 2), -1)),
      add(scale(c, 4), scale(power(b, 2), -1)))

endpoint_bounds = {
    '3-10t': {'minimum': str(3-10*F(5, 18)), 'required': '>=2/9'},
    '1-3t': {'minimum': str(1-3*F(5, 18)), 'required': '>=1/6'},
    '3-4t': {'minimum': str(3-4*F(5, 18)), 'required': '>=17/9'},
    '2-7t': {'minimum': str(2-7*F(5, 18)), 'required': '>=1/18'},
    '4-13t-4t^2': {'minimum': str(4-13*F(5, 18)-4*F(5, 18)**2), 'required': '>=13/162'},
    '5-18t': {'minimum': str(5-18*F(5, 18)), 'required': '>=0'},
    '96t^2': {'minimum': str(96*F(1, 4)**2), 'required': '>=6'},
}
checks['exact_endpoint_values'] = [item['minimum'] for item in endpoint_bounds.values()] == [
    '2/9', '1/6', '17/9', '1/18', '13/162', '0', '6']
checks['strict_lower_s_coefficient'] = 12*F(13, 162) == F(26, 27) > 0

# Exhaustive order cases, not samples of h,t or polynomial roots.
# Descending thresholds b_1>b_2>b_3>b_4: a cut k has k thresholds above b.
sign_table = []
for cut in range(5):
    comparison = [-1 if i < cut else 1 for i in range(4)]
    sign_table.append({'case': f'{cut} thresholds strictly above b', 'b_minus_thresholds': comparison})
for equal in range(4):
    comparison = [-1 if i < equal else 0 if i == equal else 1 for i in range(4)]
    sign_table.append({'case': f'b=b_{equal+1}', 'b_minus_thresholds': comparison})
for row in sign_table:
    signs = [sgn * k for sgn, k in zip(row['b_minus_thresholds'], [1, -1, 1, -1])]
    selected = [list(indices) for indices in combinations(range(4), 3)
                if [signs[i] for i in indices] == [-1, 1, -1]]
    row['F_signs'] = signs
    row['selected_indices'] = [[i+1 for i in indices] for indices in selected]
    checks['sign_order_' + row['case']] = bool(selected)

failures = [name for name, value in checks.items() if not value]
record = {
    'status': 'PASS' if not failures else 'FAIL',
    'scope': 'Independent C020r/s algebra and order-case audit, h>0, 1/4<=t<=5/18.',
    'variables': NAMES,
    'checks': checks, 'failures': failures, 'identities': identities,
    'endpoint_bounds': endpoint_bounds, 'sign_table': sign_table,
    'actual_bounds': 'B_t(r)<=-6; B_t(-r)>=(2/9)s^3+(2/3)s^2+(26/27)s>0, s=r-2>0.',
    'required_bounds': 'Both outer E<0, retaining h>0 and t endpoints; no uniform positive gap as h tends to zero is required.',
    'analytic_review': {
        'reference_roots': 'Four disjoint sign intervals, with J(eta)<0 and J(+/-h)>0, exhaust quartic degree and force simplicity.',
        'strict_branch': 'alpha_4>eta_+>0; if alpha_3<0 then J(-alpha_3)<0, forcing -alpha_3<alpha_4; hence r>2.',
        'denominators': 'A(alpha_i) nonzero by strict locations; |W|>2 and t>0 make W^2(W^2+8t-4)>0.',
        'endpoints': 'Each linear coefficient is minimized at 5/18; the quadratic decreasing coefficient has the saved exact nonnegative endpoint difference.',
        'counts': 'Every order row has three strict (-,+,-) values. Positive monic even-degree ends give four disjoint real-root intervals. Residual degree four forces simplicity.',
        'shared_roots': 'Strictly signed points cannot equal d; no division at other points or assumption H(d)!=0 is made.',
        'transfer': 'Centering has h^2=(l^2-4k)/(4k^2)>0; positive scaling k^2 and translation preserve all multiplicities; collision d=-m.',
    },
    'limitations': ['No full general-input or higher-symbol-degree count theorem.',
                    'No actual-Xi correspondence, divisor payment, RH candidate or originality certification.',
                    'Full matching Mathlib coverage not checked; polynomial checks alone do not prove analytic conclusions.'],
}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(record, indent=2) + '\n')
print(f'Independent exact checks: {sum(checks.values())}/{len(checks)}; order cases: {len(sign_table)}/9.')
print('Actual: B_t(r)<=-6; B_t(-r)>=(2/9)s^3+(2/3)s^2+(26/27)s>0 for s>0.')
print('Required: E<0 on both strict branches; full sextic target unresolved.')
print('Failures:', failures)
print('Full certificate:', path)
if failures:
    raise SystemExit(1)
