"""Exact seven-adic residue evidence; uniform lifting is proved in L090.

Reuse pure polynomial operations only. Do not execute an earlier calculation.
All coefficient lists are ascending. Full records go to image-certificate.json.
"""
import ast
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def functions(path, namespace):
    syntax = ast.parse(path.read_text())
    exec(compile(ast.Module(body=[n for n in syntax.body
                                 if isinstance(n, ast.FunctionDef)],
                            type_ignores=[]), str(path), 'exec'), namespace)
    return namespace


ops = functions(ROOT / 'scripts/thirteen-adic-membership/check_membership.py', {'P': 7})
add, scale, mul, divide, gcd, power, derivative, factor, irred, inv, ev = (
    ops[n] for n in ('add', 'scale', 'mul', 'divide', 'gcd', 'power',
                     'derivative', 'factor', 'irreducibility', 'inv', 'evalpoly'))
integer = functions(ROOT / 'scripts/five-isogeny-modular-norm/check_norm.py', {})
data = json.loads((ROOT / 'scripts/five-isogeny-modular-norm/norm-certificate.json').read_text())['polynomials_ascending']
a, b, h, d = (scale(data[n], 1) for n in ('a', 'b', 'h', 'd'))
J = add(scale(a, 2), scale(b, -1))
K = [-380, -774, -1062, -456, 258, 468, 104, -126, -6, 6, -6, 0, 1]
g = [-1264, -160, -4, 1]
checks = {}


def check(name, condition):
    checks[name] = bool(condition)


def mod(p, f):
    return divide(p, f)[1]


def polynomial(s):
    return add(add(power(h, 3), scale(J, s)), scale(d, -s*s))


def reconstruct(f, s):
    x = mod([0, 1], f)
    bv = ev(b, x, f)
    y = mod(mul(add(scale(ev(d, x, f), s), scale(ev(a, x, f), -1)), inv(bv, f)), f)
    curve = mod(add(add(mul(y, y), y), scale(ev([-20, -10, -1, 1], x, f), -1)), f)
    conjugate = add(ev(a, x, f), scale(mod(mul(bv, add(y, [1])), f), -1))
    chart = mod(mul(scale(ev(power(h, 3), x, f), -1), inv(conjugate, f)), f)
    assert curve == [0] and chart == [s % 7]
    return {'x': x, 'y': y, 'curve_residual': curve,
            'conjugate_numerator': conjugate, 'regular_j_value': chart,
            'd_value': ev(d, x, f)}


def labels(f):
    q = 7 ** (len(f)-1)
    for seed in range(1, 100):
        candidate = [seed % 7, seed // 7 + 1]
        if power(candidate, (q-1)//2, f) == [6]:
            root = power(candidate, (q-1)//4, f)
            break
    else:
        raise RuntimeError('No certified square root of minus one')
    assert power(root, 2, f) == [6]
    values = [add([0, 4], [-4]), add([0, 4], scale(root, -1)), add([0, 4], root)]
    characters = [power(v, (q-1)//2, f) for v in values]
    assert all(v in ([1], [6]) for v in characters)
    return {'nonsquare_seed': candidate, 'seed_character': power(candidate, (q-1)//2, f),
            'sqrt_minus_one': root, 'root_square': power(root, 2, f),
            'theta_residues': [[4], root, scale(root, -1)],
            'values_4x_minus_theta': values, 'characters': characters}


# Entire integral map: verify the integer identity, both x=16 charts,
# and the exact origin expressions used in the proof, at the new prime.
ia, ib, ih, iden, ig = (data[n] for n in ('a', 'b', 'h', 'd', 'g'))
iadd, imul, iscale, ipower, iev = (integer[n] for n in ('add', 'mul', 'scale', 'power', 'ev'))
residual = iadd(iadd(imul(ia, ia), iscale(imul(ia, ib), -1)),
                iadd(iscale(imul(imul(ib, ib), ig), -1), imul(iden, ipower(ih, 3))))
check('integer_conjugate_product_identity', residual == [0])
check('integer_denominator', iden == ipower([-16, 1], 11))
delta = -(-4)**2*(-21)-8*(-20)**3-27*(-79)**2+9*(-4)*(-20)*(-79)
check('curve_and_cubic_discriminants_units', delta == -11**5 and delta % 7 != 0 and (-256*11**5) % 7 != 0)
charts = []
for name, y in [('2T', -61), ('3T', 60)]:
    N, Nc = iev(ia, 16)+iev(ib, 16)*y, iev(ia, 16)-iev(ib, 16)*(1+y)
    charts.append({'point': name, 'y': y, 'N': N, 'N_conjugate': Nc,
                   'derivative': 2*y+1,
                   'residues': [N % 7, Nc % 7, (2*y+1) % 7]})
check('both_x16_charts_units', charts[0]['N'] == 0 and charts[0]['N_conjugate'] == 11**22
      and charts[1]['N'] == 11**22 and charts[1]['N_conjugate'] == 0
      and all(row['derivative'] % 7 != 0 for row in charts))
check('h16_cancelled_value', iev(ih, 16) == 11**8 and -11**24 == -121*11**22)
Q = [[23-2*i, 11-i, c] for i, c in enumerate(ia)] + [[20-2*i, 10-i, -c] for i, c in enumerate(ib)]
check('origin_integral_and_leading_units', len(ia) == 12 and len(ib) == 11
      and ib[-1] == 1 and all(t >= 0 and v >= 0 for t, v, c in Q)
      and sum(c for t, v, c in Q if t == 0) == -1)
map_record = {'integer_product_residual': residual, 'curve_discriminant': delta,
              'x16_charts': charts, 'h16': iev(ih, 16),
              'origin_Q_terms_t_V_coefficient': Q,
              'origin_H': '(1-16*t^2*V)^11', 'origin_reciprocal_linear_coefficient': -1,
              'polar_orders': [1, 11], 'degree_actual': 12, 'degree_required': 12}

kf = factor(K)
check('K_entire_irreducible_degree_twelve', len(kf) == 1 and len(kf[0]) == 13)
kc = [irred(f) for f in kf]
check('fixed_cubic_factorization', mul([3, 1], [1, 0, 1]) == scale(g, 1))
check('minus_one_nonsquare_over_F7', pow(6, 3, 7) == 6)
regular = []
for s in range(1, 6):
    F = polynomial(s)
    fs = factor(F)
    row = {'scalar_residue': s, 'polynomial': F,
           'degrees': [len(f)-1 for f in fs],
           'b_gcd': gcd(b, F), 'd_gcd': gcd(d, F),
           'derivative_gcd': gcd(F, derivative(F)),
           'factors': [{'irreducibility': irred(f), 'reconstruction': reconstruct(f, s)} for f in fs]}
    if row['degrees'] == [12]:
        row['two_descent'] = labels(fs[0])
    check(f'regular_{s}_entire_degree', sum(row['degrees']) == 12)
    check(f'regular_{s}_etale_and_b_unit', row['derivative_gcd'] == [1] and row['b_gcd'] == [1])
    regular.append(row)
check('regular_factor_degree_patterns', [r['degrees'] for r in regular] == [[1, 1, 10], [12], [12], [1, 1, 10], [1, 1, 10]])
check('compatible_regular_classes_identity', all(r['two_descent']['characters'] == [[1], [1], [1]] for r in regular if 'two_descent' in r))

G = gcd(polynomial(6), derivative(polynomial(6)))
gs = factor(G)
zero = {'factor': irred(h), 'polynomial': polynomial(0),
        'power_identity': polynomial(0) == power(h, 3),
        'b_gcd': gcd(b, h), 'd_gcd': gcd(d, h),
        'two_torsion_gcd': gcd(h, [-1264, -640, -64, 64]),
        'reconstruction': reconstruct(h, 0), 'two_descent': labels(h),
        'extension_degree_to_U12': 3,
        'quadratic_character_exponent_quotient': (7**12-1)//(7**4-1)}
branch = {'polynomial': polynomial(6), 'square_factor': G,
          'power_identity': polynomial(6) == power(G, 2),
          'b_gcd': gcd(b, G), 'd_gcd': gcd(d, G),
          'factors': [irred(f) for f in gs],
          'coprime_hensel_block_degrees': [2*(len(f)-1) for f in gs]}
check('zero_branch_complete_irreducible_four_cubed', len(h) == 5 and zero['power_identity'])
check('zero_branch_unit_differences', all(zero[k] == [1] for k in ('b_gcd', 'd_gcd', 'two_torsion_gcd')))
check('zero_branch_nontrivial_diagonal_class', zero['two_descent']['characters'] == [[1], [6], [6]] and zero['quadratic_character_exponent_quotient'] % 2 == 1)
check('1728_branch_complete_blocks', branch['power_identity'] and branch['coprime_hensel_block_degrees'] == [2, 2, 4, 4] and branch['b_gcd'] == [1])
check('1728_branch_no_degree_twelve_point', max(branch['coprime_hensel_block_degrees']) < 12)
check('removable_chart_in_residue_five', (-121) % 7 == 5 and regular[4]['d_gcd'] == [5, 1])

# Unit residues solve the normalized cube/fourth ratio for EVERY unit ratio.
ratio_choices = []
for eta in range(1, 7):
    aa, bb = next((a0, b0) for a0 in range(1, 7) for b0 in range(1, 7)
                  if (a0**3-eta*b0**4) % 7 == 0)
    ratio_choices.append({'ratio_unit': eta, 'a_start': aa, 'b_start': bb,
                          'cube_derivative': 3*aa*aa % 7})
check('primitive_unit_ratio_coverage', all(r['cube_derivative'] for r in ratio_choices) and len(ratio_choices) == 6)
check('eleventh_unit_power_bijective', sorted(pow(c, 11, 7) for c in range(1, 7)) == list(range(1, 7)))

unit_witness = {'scalar': [2, 1], 'b': 2, 'a_cubed': Fraction(32, 1726),
                'c_eleventh': Fraction(27648, 1726), 'a_start': 1, 'c_start': 5}
residue = lambda r: r.numerator*pow(r.denominator, -1, 7) % 7
check('regular_common_witness_roots', residue(unit_witness['a_cubed']) == 1
      and residue(unit_witness['c_eleventh']) == pow(5, 11, 7)
      and 3 % 7 != 0 and 11*pow(5, 10, 7) % 7 != 0)
check('regular_same_c_identities', unit_witness['a_cubed']+16 == unit_witness['c_eleventh']
      and 1728*unit_witness['a_cubed'] == 2*unit_witness['c_eleventh'])
canonical = {'scalar': [9261, 8], 'a': 7, 'b_fourth': 169, 'b_start': 1,
             'c_eleventh': 512, 'c_start': 1,
             'whole_fiber_input': 'L047: entire rational canonical fiber B_(9261/8) is K; tensor at seven'}
check('canonical_common_primitive_witness', (1-169) % 7 == 0 and 4 % 7 != 0
      and (1-512) % 7 == 0 and 11 % 7 != 0 and 7**3+169 == 512
      and Fraction(1728*7**3, 512) == Fraction(9261, 8))
check('canonical_scalar_in_zero_branch', 9261 % 7 == 0 and 8 % 7 != 0)
for key in ('a_cubed', 'c_eleventh'):
    r = unit_witness[key]
    unit_witness[key] = [r.numerator, r.denominator]

certificate = {'prime': 7, 'K_polynomial_mod7': scale(K, 1), 'K_factors': kc,
               'base_field_degrees': [len(f)-1 for f in kf],
               'fixed_cubic_mod7': scale(g, 1), 'integral_map': map_record,
               'regular_fibers': regular, 'branch_zero': zero, 'branch_1728': branch,
               'primitive_ratio_choices': ratio_choices,
               'primitive_realizations': [unit_witness, canonical],
               'restricted_image_size_actual': 2, 'unrestricted_image_size_comparison': 4,
               'checks': checks, 'failures': [n for n, ok in checks.items() if not ok],
               'qualification': 'Uniform lifting, branch exclusion, all identifications and exact realizations require L090. No global independence, dimension improvement or integer solution.'}
out = Path(__file__).with_name('image-certificate.json')
out.write_text(json.dumps(certificate, indent=2)+'\n')
print(f'Checks: {sum(checks.values())}/{len(checks)}; failures: {certificate["failures"]}')
print('Entire base degree actual=12 required=12; compatible regular residues=[2,3].')
print('Branch 1728 maximum lifted x-degree actual=4 required=12; incompatible.')
print('Restricted image actual=2; unrestricted comparison=4; global bounds unchanged.')
print('Certificate:', out.relative_to(ROOT))
if certificate['failures']:
    raise SystemExit(1)
