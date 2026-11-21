"""Independent C020t replay: standard library only, no discovery calculations.

All saved rational boxes and symbolic expressions are read and checked in full.
The source certificate's truth flags are never used as mathematical premises.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial
from pathlib import Path
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
source = json.loads((HERE / 'sector-sextic-distinct-collision-1477.json').read_text())
checks, identities, replay = {}, {}, []
names = ('y', 't', 'b', 'c', 'd', 'x')
zero = (0,) * len(names)


def constant(c):
    return {zero: F(c)} if c else {}


def add(*ps):
    out = {}
    for p in ps:
        for e, c in p.items():
            out[e] = out.get(e, F(0)) + c
    return {e: c for e, c in out.items() if c}


def scale(p, c):
    return {e: c * v for e, v in p.items() if c * v}


def mul(*ps):
    out = constant(1)
    for p in ps:
        nxt = {}
        for e, c in out.items():
            for f, v in p.items():
                g = tuple(a + b for a, b in zip(e, f))
                nxt[g] = nxt.get(g, F(0)) + c * v
        out = {e: c for e, c in nxt.items() if c}
    return out


def power(p, n):
    return mul(*([p] * n))


def derivative(p, name):
    i = names.index(name)
    out = {}
    for e, c in p.items():
        if e[i]:
            f = list(e)
            f[i] -= 1
            out[tuple(f)] = c * e[i]
    return out


variables = {}
for i, name in enumerate(names):
    e = list(zero)
    e[i] = 1
    variables[name] = {tuple(e): F(1)}
y, t, b, c, d, x = (variables[n] for n in names)


def substitute(p, changes):
    return add(*(mul(constant(v), *(power(changes.get(n, variables[n]), k)
                                   for n, k in zip(names, e)))
                 for e, v in p.items()))


def encode(p):
    return [{'powers': list(e), 'coefficient': str(c)} for e, c in sorted(p.items())]


def identity(name, lhs, rhs):
    difference = add(lhs, scale(rhs, -1))
    checks[name] = not difference
    identities[name] = {'lhs': encode(lhs), 'rhs': encode(rhs),
                        'difference': encode(difference)}


def T(p):
    return add(p, derivative(p, 'y'), mul(t, derivative(derivative(p, 'y'), 'y')))


R = mul(add(power(y, 2), constant(-1)), add(power(y, 2), constant(-4)))
Q = add(power(y, 2), mul(b, y), c)
A, B, C = T(mul(y, R)), T(R), T(mul(y, y, R))
K = add(R, scale(mul(t, derivative(R, 'y')), 2))
out = T(mul(R, Q))
identity('product_rule', out,
         add(mul(Q, B), mul(derivative(Q, 'y'), K),
             mul(t, derivative(derivative(Q, 'y'), 'y'), R)))
at_d = lambda p: substitute(p, {'y': d})
ad, bd, cd = map(at_d, (A, B, C))
ap, bp, cp = (at_d(derivative(p, 'y')) for p in (A, B, C))
delta = add(mul(ad, bp), scale(mul(ap, bd), -1))
nb = add(mul(bd, cp), scale(mul(cd, bp), -1))
nc = add(mul(cd, ap), scale(mul(ad, cp), -1))
r0 = at_d(R)
r1 = at_d(derivative(R, 'y'))
r2 = scale(at_d(derivative(derivative(R, 'y'), 'y')), F(1, 2))
r3 = scale(at_d(derivative(derivative(derivative(R, 'y'), 'y'), 'y')), F(1, 6))
u = add(r0, scale(mul(t, r1), 2))
v = add(r0, r1, scale(mul(t, r2), 2))
w = add(r0, scale(r1, 2), scale(mul(t, r2), 6))
z = add(r1, scale(r2, 2), scale(mul(t, r3), 6))
h = scale(mul(t, r0), -2)
k = add(scale(r0, -2), scale(mul(t, r1), -6))
identity('shifted_first_column', add(ad, scale(mul(d, bd), -1)), u)
identity('shifted_second_row_first_column', add(ap, scale(mul(d, bp), -1)), w)
identity('shifted_first_row_second_column', bd, v)
identity('shifted_second_row_second_column', bp, z)
identity('shifted_first_rhs', add(scale(cd, -1), scale(mul(d, ad), 2),
                                scale(mul(d, d, bd), -1)), h)
identity('shifted_second_rhs', add(scale(cp, -1), scale(mul(d, ap), 2),
                                 scale(mul(d, d, bp), -1)), k)
identity('shifted_determinant', add(mul(u, z), scale(mul(w, v), -1)), delta)
N0 = add(mul(add(scale(t, 2), constant(-2)), r0, r0),
         scale(mul(t, r0, r1), -6), scale(mul(t, t, r1, r1), -12),
         scale(mul(t, t, r0, r2), 12))
E = add(scale(mul(r1, r1), 3), scale(mul(r0, r2), -8))
identity('elimination_without_division', add(mul(u, k), scale(mul(w, h), -1)), N0)
identity('shifted_cramer_numerator', add(nc, mul(d, nb), mul(d, d, delta)), N0)
identity('N0_square_completion', N0,
         add(scale(power(add(mul(t, r1), scale(r0, F(2, 5))), 2), -F(15, 2)),
             scale(mul(t, t, E), -F(3, 2)),
             mul(add(scale(t, 2), constant(-F(4, 5))), r0, r0)))
identity('E_square_completion', E,
         add(scale(power(add(power(d, 2), constant(-F(23, 20))), 2), 40),
             constant(F(1071, 10))))
identity('cramer_first', add(mul(ad, nb), mul(bd, nc), mul(cd, delta)), {})
identity('cramer_second', add(mul(ap, nb), mul(bp, nc), mul(cp, delta)), {})
M = add(scale(mul(nc, delta), 4), scale(mul(nb, nb), -1))
identity('pair_margin_numerator', M, add(scale(mul(nc, delta), 4), scale(power(nb, 2), -1)))
checks['uniform_N0_bound'] = (F(3, 2) * F(1, 4)**2 * F(1071, 10) == F(3213, 320)
                               and 2 * F(5, 18) - F(4, 5) == -F(11, 45))

# Compare every saved bivariate polynomial to an independently derived expression.
for key, expected in [('A', ad), ('B', bd), ('C', cd), ('delta', delta),
                      ('N_b', nb), ('N_c', nc), ('shifted_c_numerator', N0), ('E', E)]:
    loaded = {}
    for term in source['collision_algebra'][key]:
        e = list(zero)
        e[names.index('d')] = term['d_power']
        e[names.index('t')] = term['t_power']
        loaded[tuple(e)] = F(term['coefficient'])
    identity('saved_' + key, loaded, expected)

# Check the shifted residual coefficient formula identically for arbitrary b,c,d,t.
shift_input = substitute(mul(R, Q), {'y': add(d, x)})
shift_out = substitute(out, {'y': add(d, x)})


def coefficient(p, name, j):
    i = names.index(name)
    result = {}
    for e, value in p.items():
        if e[i] == j:
            f = list(e)
            f[i] = 0
            result[tuple(f)] = value
    return result


def rational_value(p, values):
    result = substitute(p, {name: constant(value) for name, value in values.items()})
    assert all(e == zero for e in result)
    return result.get(zero, F(0))


for n, saved in enumerate(source['zero_collisions']):
    tv, bv, cv = (F(saved[key]) for key in ('t', 'b', 'c'))
    values = {'d':F(0), 't':tv}
    dv = rational_value(delta, values)
    checks[f'zero_collision{n}_delta'] = dv == F(saved['delta']) != 0
    checks[f'zero_collision{n}_cramer'] = (
        rational_value(nb, values)/dv == bv and rational_value(nc, values)/dv == cv)
    checks[f'zero_collision{n}_margin'] = cv-bv*bv/4 == F(saved['pair_margin']) > 0
    numeric = {'t':constant(tv), 'b':constant(bv), 'c':constant(cv)}
    for key, polynomial in [('input_ascending', mul(R,Q)), ('output_ascending',out)]:
        actual = substitute(polynomial, numeric)
        coefficients = [rational_value(coefficient(actual, 'y', j), {}) for j in range(7)]
        checks[f'zero_collision{n}_{key}'] = [str(v) for v in coefficients] == saved[key]
        if key == 'output_ascending':
            checks[f'zero_collision{n}_residual'] = (
                coefficients[:2] == [0,0]
                and [str(v) for v in coefficients[2:]] == saved['residual_quartic_ascending'])


for j in range(7):
    identity('shifted_output_coefficient_' + str(j), coefficient(shift_out, 'x', j),
             add(coefficient(shift_input, 'x', j),
                 scale(coefficient(shift_input, 'x', j + 1), j + 1),
                 scale(mul(t, coefficient(shift_input, 'x', j + 2)), (j + 2) * (j + 1))))
identity('monic_residual', coefficient(shift_out, 'x', 6), constant(1))

# Independent interval operations on endpoint tuples, all rational.
def plus(a, b):
    return (a[0] + b[0], a[1] + b[1])


def times(a, b):
    endpoints = [u * v for u, v in product(a, b)]
    return (min(endpoints), max(endpoints))


def divide(a, b):
    assert not b[0] <= 0 <= b[1]
    return times(a, (1 / b[1], 1 / b[0]))


def horner(coeffs, interval):
    value = (F(0), F(0))
    for c in reversed(coeffs):
        value = plus(times(value, interval), (F(c), F(c)))
    return value


def exact_J(yv, tv):
    # Expanded formula (3), independent of the source's differential implementation.
    return yv**4 + 4*yv**3 + (12*tv-5)*yv**2 - 10*yv + 4 - 10*tv


def enc(interval):
    return [str(v) for v in interval]


cells = source['uniform_reference_certificate']['cells']
checks['32_cells'] = len(cells) == 32
checks['canonical_parameter_interval'] = source['parameter_interval'] == ['1/4', '5/18']
lemma = (ROOT / 'lemmas/C020t-sector-sextic-fixed-distinct-input-exclusion.md').read_text()
table = [[int(s) for s in line.split()] for line in lemma.splitlines()
         if re.fullmatch(r'\d+\s+-\d+\s+-\d+\s+-\d+\s+-\d+(?:\s+\d+){4}', line)]
checks['32_canonical_table_rows'] = len(table) == 32
coarse = [((-4,-3),(20,60),(5,7)), ((-2,-1),(-6,-4),(3,4)),
          ((0,1),(3,4),(-1,0)), ((1,2),(-4,-2),(-4,-3))]
margins, all_gaps, all_k = [], [], []
for j, cell in enumerate(cells):
    ti = tuple(map(F, cell['t_interval']))
    expected_t = (F(1,4) + F(j,1152), F(1,4) + F(j+1,1152))
    checks[f'cell{j}_coverage'] = ti == expected_t
    brackets, thresholds = [], []
    roots_out = []
    for i, saved in enumerate(cell['roots']):
        yi = tuple(map(F, saved['root_interval']))
        checks[f'cell{j}_root{i}_table'] = yi == tuple(F(v,10000) for v in table[j][1+2*i:3+2*i])
        brackets.append(yi)
        left = tuple(sorted(exact_J(yi[0], tv) for tv in ti))
        right = tuple(sorted(exact_J(yi[1], tv) for tv in ti))
        expected_signs = (1,-1) if i % 2 == 0 else (-1,1)
        signed = []
        for field, value, sign in [('J_left_interval', left, expected_signs[0]),
                                   ('J_right_interval', right, expected_signs[1])]:
            checks[f'cell{j}_root{i}_{field}_exact'] = enc(value) == saved[field]
            margin = value[0] if sign == 1 else -value[1]
            signed.append(margin)
            margins.append(margin)
        checks[f'cell{j}_root{i}_strict_endpoint_signs'] = min(signed) > 0
        ri = horner([4,0,-5,0,1], yi)
        rpi = horner([0,-10,0,4], yi)
        ki = plus(ri, times(times((F(2),F(2)), ti), rpi))
        checks[f'cell{j}_root{i}_K_nonzero'] = ki[0] > 0 if i%2==0 else ki[1] < 0
        threshold = times((F(-2),F(-2)), plus(yi, divide(times(ti,ri), ki)))
        thresholds.append(threshold)
        for field, value in [('K_interval',ki), ('threshold_interval',threshold)]:
            checks[f'cell{j}_root{i}_{field}_exact'] = enc(value) == saved[field]
        for field, value, bounds in zip(('root','K','threshold'), (yi,ki,threshold), coarse[i]):
            checks[f'cell{j}_root{i}_{field}_coarse'] = bounds[0] < value[0] <= value[1] < bounds[1]
        all_k.append(min(map(abs,ki)))
        roots_out.append({'root':enc(yi), 'J_left':enc(left), 'J_right':enc(right),
                          'K':enc(ki), 'threshold':enc(threshold)})
    gaps = [thresholds[i][0]-thresholds[i+1][1] for i in range(3)]
    all_gaps.extend(gaps)
    checks[f'cell{j}_root_order'] = all(brackets[i][1] < brackets[i+1][0] for i in range(3))
    checks[f'cell{j}_threshold_order'] = min(gaps) > 0
    checks[f'cell{j}_saved_gaps'] = [str(v) for v in gaps] == cell['threshold_gap_lower_bounds']
    replay.append({'t':enc(ti), 'roots':roots_out, 'gaps':[str(v) for v in gaps]})
checks['saved_endpoint_margin'] = str(min(margins)) == source['minimum_signed_endpoint_margin']
checks['saved_threshold_margin'] = str(min(all_gaps)) == source['uniform_reference_certificate']['minimum_threshold_gap_lower_bound']
checks['saved_K_margin'] = str(min(all_k)) == source['uniform_reference_certificate']['minimum_absolute_K_lower_bound']

# Ordered thresholds have nine order/equality cells. Test every one exactly.
# Only comparisons with thresholds enter the four-case sign rule.
thresholds = [F(6), F(7,2), -F(1,2), -F(7,2)]
bvalues = [F(7), F(6), F(5), F(7,2), F(1), -F(1,2), F(-2), -F(7,2), F(-5)]
sign_cases = []
for bv in bvalues:
    if bv > thresholds[1]:
        selected = (1,2,3)
    elif bv == thresholds[1]:
        selected = (0,2,3)
    elif bv >= thresholds[2]:
        selected = (0,1,3)
    else:
        selected = (0,1,2)
    values = [(1 if i%2==0 else -1)*(bv-thresholds[i]) for i in selected]
    checks['sign_case_' + str(bv)] = values[0] < 0 < values[1] and values[2] < 0
    sign_cases.append({'b':str(bv), 'selected_indices':[i+1 for i in selected],
                       'signed_values':[str(v) for v in values]})
checks['Walsh_factorial_coefficients'] = factorial(5)*6/F(factorial(6)) == 1 and factorial(4)*30/F(factorial(6)) == 1
checks['sextic_reference_discriminant_min'] = 36-120*F(5,18) == F(8,3) > 0
checks['symbol_sector_endpoints'] = 4*F(1,4)-1 == 0 and 4*F(5,18)-1 == F(1,9)
checks['table_matches_saved_table'] = table == source['root_box_table_10000']
failed = [name for name, ok in checks.items() if not ok]
certificate = {'status':'PASS' if not failed else 'FAIL', 'checks':checks,
               'failures':failed, 'identities':identities, 'full_interval_replay':replay,
               'sign_order_cases':sign_cases,
               'bounds':{'minimum_signed_endpoint_margin':str(min(margins)),
                         'minimum_threshold_gap':str(min(all_gaps)),
                         'minimum_K_absolute_bound':str(min(all_k)),
                         'N0_upper_bound':'-3213/320',
                         'required_endpoint_and_order_margin':'>0',
                         'actual_output_real_roots':'>=4 distinct',
                         'actual_collision_residual_real_roots':'4 simple',
                         'required_global_result':'(2,4) witness or whole-class impossibility; unresolved'},
               'limits':['Finite sign checks encode only order cases; IVT and multiplicity reasoning are in C020t.',
                         'No theorem about arbitrary spacings, general symbols or actual Xi is certified.',
                         'No source flags or discovery-only floating data are used as proof.']}
path = HERE / 'sector-sextic-distinct-audit-1478.json'
path.write_text(json.dumps(certificate, indent=2)+'\n')
print('C020t independent replay:',certificate['status'],sum(checks.values()),'/',len(checks))
print('Closed parameter cells:',len(cells),'; root boxes:',sum(len(c['roots']) for c in cells))
print('Endpoint margin:',min(margins),'; required >0')
print('Threshold gap:',min(all_gaps),'; required >0')
print('N0 <= -3213/320; required <0. Sign/equality cases:',len(sign_cases))
print('Actual: >=4 distinct real output roots; residual 4 simple real roots.')
print('Global target: (2,4) witness or full-class impossibility remains unresolved.')
print('Failures:',failed)
print('Full certificate:',path.relative_to(ROOT))
raise SystemExit(bool(failed))
