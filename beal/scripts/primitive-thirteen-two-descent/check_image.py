"""Complete residue certificate for L087; uniform lifting is proved there.

Reuse pure F13 polynomial utilities, not the old membership computation.
All new image computations and every residue fiber are recomputed here.
"""
import ast
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
utility_source = ROOT / 'scripts/thirteen-adic-membership/check_membership.py'
syntax = ast.parse(utility_source.read_text())
namespace = {'P': 13}
exec(compile(ast.Module(body=[n for n in syntax.body
                             if isinstance(n, ast.FunctionDef)],
                        type_ignores=[]), str(utility_source), 'exec'), namespace)
trim, add, scale, mul, divide, gcd, power, derivative, factor, irred, inv, ev = (
    namespace[n] for n in ('trim', 'add', 'scale', 'mul', 'divide', 'gcd',
                          'power', 'derivative', 'factor', 'irreducibility',
                          'inv', 'evalpoly'))
data = json.loads((ROOT / 'scripts/five-isogeny-modular-norm/norm-certificate.json').read_text())['polynomials_ascending']
a, b, h, d = (scale(data[n], 1) for n in ('a', 'b', 'h', 'd'))
J = add(scale(a, 2), scale(b, -1))
checks = {}


def check(name, assertion):
    checks[name] = bool(assertion)


def mod(p, f):
    return divide(p, f)[1]


def sqrt_two(f):
    """Tonelli-Shanks in the certified finite field; retain exact root."""
    q = 13 ** (len(f) - 1)
    odd, depth = q - 1, 0
    while odd % 2 == 0:
        odd //= 2
        depth += 1
    for seed in range(1, 1000):
        candidate = [seed % 13, seed // 13 + 1]
        if power(candidate, (q - 1) // 2, f) == [12]:
            break
    else:
        raise RuntimeError('No nonsquare found in bounded root calculation')
    c, r, residue, m = (power(candidate, odd, f),
                        power([2], (odd + 1) // 2, f),
                        power([2], odd, f), depth)
    while residue != [1]:
        z, i = residue, 0
        while z != [1]:
            z, i = power(z, 2, f), i + 1
        assert i < m
        correction = power(c, 2 ** (m - i - 1), f)
        r = mod(mul(r, correction), f)
        c = power(correction, 2, f)
        residue, m = mod(mul(residue, c), f), i
    assert power(r, 2, f) == [2]
    return {'root': r, 'square': power(r, 2, f),
            'nonsquare_seed': candidate,
            'seed_character': power(candidate, (q - 1) // 2, f)}


def labels(f):
    root = sqrt_two(f)
    r = root['root']
    values = [add([0, 4], [-8]), add([0, 4], add([2], scale(r, -1))),
              add([0, 4], add([2], r))]
    chars = [power(v, (13 ** (len(f) - 1) - 1) // 2, f) for v in values]
    assert all(c in ([1], [12]) for c in chars)
    return {'sqrt_two': root, 'theta_residues': [[8], add([-2], r),
                                               add([-2], scale(r, -1))],
            'values_4x_minus_theta': values, 'characters': chars}


def polynomial(s):
    return add(add(power(h, 3), scale(J, s)), scale(d, -s*s))


def reconstruct(f, s):
    x = mod([0, 1], f)
    bv = ev(b, x, f)
    y = mod(mul(add(scale(ev(d, x, f), s), scale(ev(a, x, f), -1)), inv(bv, f)), f)
    residual = mod(add(add(mul(y, y), y), scale(ev([-20, -10, -1, 1], x, f), -1)), f)
    conjugate = add(ev(a, x, f), scale(mod(mul(bv, add(y, [1])), f), -1))
    jchart = mod(mul(scale(ev(power(h, 3), x, f), -1), inv(conjugate, f)), f)
    assert residual == [0] and jchart == [s % 13]
    return {'x': x, 'y': y, 'curve_residual': residual,
            'regular_conjugate_numerator': conjugate, 'regular_j_value': jchart}


regular = []
for s in range(1, 12):
    F = polynomial(s)
    fs = factor(F)
    entries = []
    for f in fs:
        entry = {'irreducibility': irred(f), 'reconstruction': reconstruct(f, s)}
        if len(f) == 13:
            entry['two_descent'] = labels(f)
        entries.append(entry)
    row = {'scalar_residue': s, 'polynomial': F,
           'b_gcd': gcd(b, F), 'd_gcd': gcd(d, F),
           'derivative_gcd': gcd(F, derivative(F)),
           'degrees': [len(f)-1 for f in fs], 'factors': entries}
    check(f'regular_{s}_entire_degree', sum(row['degrees']) == 12)
    check(f'regular_{s}_etale_and_b_unit', row['b_gcd'] == [1] and row['derivative_gcd'] == [1])
    regular.append(row)

G = gcd(polynomial(12), derivative(polynomial(12)))
g4 = [-1264, -640, -64, 64]
branch_zero = {'factor': irred(h), 'power_identity': polynomial(0) == power(h, 3),
               'b_gcd': gcd(b, h), 'd_gcd': gcd(d, h),
               'two_torsion_gcd': gcd(g4, h),
               'reconstruction': reconstruct(h, 0), 'two_descent': labels(h)}
# At the other branch the degree-six subfield's units are squares in U12.
branch_1728 = {'factor': irred(G), 'power_identity': polynomial(12) == power(G, 2),
               'b_gcd': gcd(b, G), 'd_gcd': gcd(d, G),
               'two_torsion_gcd': gcd(g4, G),
               'reconstruction': reconstruct(G, 12),
               'extension_degree_to_U12': 2,
               'unit_square_exponent_quotient': (13**12-1)//(13**6-1)}
check('branch_zero_complete_four_cubed', len(h) == 5 and branch_zero['power_identity'])
check('branch_1728_complete_six_squared', len(G) == 7 and branch_1728['power_identity'])
check('branches_ordinary_unit_kummer_values', all(row[k] == [1] for row in (branch_zero, branch_1728) for k in ('b_gcd', 'd_gcd', 'two_torsion_gcd')))
check('branch_zero_all_squares_in_U4', branch_zero['two_descent']['characters'] == [[1], [1], [1]])
check('branch_1728_even_extension', branch_1728['unit_square_exponent_quotient'] % 2 == 0)
compatible = [r for r in regular if r['degrees'] == [12]]
check('compatible_regular_residues', [r['scalar_residue'] for r in compatible] == [1, 3, 7, 10])
check('regular_labels', [r['factors'][0]['two_descent']['characters'] for r in compatible] == [[[1], [1], [1]], [[1], [1], [1]], [[1], [12], [12]], [[1], [12], [12]]])
check('fixed_cubic_splitting', mul([-8, 1], [2, 4, 1]) == scale([-1264, -160, -4, 1], 1))
check('quadratic_discriminant_nonsquare', pow(2, 6, 13) == 12)
check('curve_and_cubic_good', (-11**5) % 13 != 0 and (-256*11**5) % 13 != 0)
check('x16_regular_scalar', (-121) % 13 == 9)

witnesses = []
for s, ar, cr in [(1, 7, 5), (7, 4, 7)]:
    acube, celeventh = Fraction(16*s, 1728-s), Fraction(16*1728, 1728-s)
    residue = lambda u: u.numerator * pow(u.denominator, -1, 13) % 13
    assertions = {'cube_root_residue': residue(acube) == ar**3 % 13,
                  'eleventh_root_residue': residue(celeventh) == cr**11 % 13,
                  'cube_derivative_unit': (3*ar*ar) % 13 != 0,
                  'eleventh_derivative_unit': (11*cr**10) % 13 != 0,
                  'same_c_sum': acube + 16 == celeventh,
                  'same_c_scalar': 1728*acube == s*celeventh}
    check(f'scalar_{s}_common_primitive_witness', all(assertions.values()))
    witnesses.append({'scalar': s, 'b': 2, 'a_cubed': [acube.numerator, acube.denominator],
                      'c_eleventh': [celeventh.numerator, celeventh.denominator],
                      'a_start': ar, 'c_start': cr, 'checks': assertions})
cert = {'prime': 13, 'base_field_degree': 12, 'fixed_cubic_mod13': scale([-1264, -160, -4, 1], 1),
        'regular_fibers': regular, 'branch_zero': branch_zero, 'branch_1728': branch_1728,
        'primitive_realizations': witnesses, 'checks': checks,
        'restricted_image_size_actual': 2, 'unrestricted_image_size_required_comparison': 4,
        'failures': [k for k, v in checks.items() if not v],
        'qualification': 'Arithmetic certificate; uniform branch, infinity, all-identification and Hensel arguments are in L087. No global independence or integer conclusion.'}
out = Path(__file__).with_name('image-certificate.json')
out.write_text(json.dumps(cert, indent=2) + '\n')
print(f'Checks: {sum(checks.values())}/{len(checks)}; failures: {cert["failures"]}')
print('Compatible regular residues:', [r['scalar_residue'] for r in compatible])
print('Restricted image actual=2; unrestricted comparison=4; global dimension bound unchanged.')
print('Certificate:', out.relative_to(ROOT))
if cert['failures']:
    raise SystemExit(1)
