"""Independent exact arithmetic audit of L048; imports no construction code.

Existence of local factors, their descent and the image theorem are checked
in the canonical proof, not inferred from finite-precision computation.
"""
import json
from math import comb, gcd
from pathlib import Path

OUT = Path(__file__).with_name('audit-certificate.json')
original = json.loads(OUT.with_name('image-certificate.json').read_text())
# Transcribed independently from the displayed L033 defining polynomial.
h = [-380, -774, -1062, -456, 258, 468, 104, -126, -6, 6, -6, 0, 1]

# Integer polynomial long division by X^2+1, rather than evaluation by Horner.
r = h[:]
quotient = [0] * 11
for n in range(12, 1, -1):
    quotient[n-2] = r[n]
    r[n-2] -= r[n]
    r[n] = 0
reconstruction = [0] * 13
for n, a in enumerate(quotient):
    reconstruction[n] += a
    reconstruction[n+2] += a
for n in range(2):
    reconstruction[n] += r[n]

# F9 arithmetic, with coefficients stored in the basis (1, i).
def add(a, b):
    return ((a[0]+b[0]) % 3, (a[1]+b[1]) % 3)

def times(a, b):
    return ((a[0]*b[0]-a[1]*b[1]) % 3,
            (a[0]*b[1]+a[1]*b[0]) % 3)

def power(a, n):
    result = (1, 0)
    for _ in range(n):
        result = times(result, a)
    return result

def convolution(a, b):
    result = [(0, 0)] * (len(a)+len(b)-1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            result[j+k] = add(result[j+k], times(x, y))
    return result

def at(p, z):
    result = (0, 0)
    for n, a in enumerate(p):
        result = add(result, times(a, power(z, n)))
    return result

def translate(p, z):
    result = [(0, 0)] * len(p)
    for n, a in enumerate(p):
        for k in range(n+1):
            result[k] = add(result[k], times(a, times((comb(n, k) % 3, 0), power(z, n-k))))
    return result

def vp3(n):
    if n == 0:
        return None
    v = 0
    while n % 3 == 0:
        v += 1
        n //= 3
    return v

factors = []
for sign in (1, -1):
    center = (0, sign % 3)
    p = [(1, 0)]
    for _ in range(6):
        p = convolution(p, [(0, -sign % 3), (1, 0)])
    value = [r[0], sign*r[1]]
    factors.append({'center': center, 'residue_coefficients': p,
                    'translated_residue_coefficients': translate(p, center),
                    'H_at_center': value,
                    'component_valuations': [vp3(v) for v in value],
                    'normalized_constant_residue': [v//3 % 3 for v in value]})
for index in (0, 1):
    factors[index]['opposite_factor_at_center'] = at(factors[1-index]['residue_coefficients'], factors[index]['center'])
product = convolution(*(entry['residue_coefficients'] for entry in factors))
# Every pair of roots, with multiplicity 6*6, has the same nonzero difference.
resultant = power((0, 2), 36)
models = []
for a4, a6 in ((-10, -20), (-7820, -263580)):
    b2, b4, b6 = -4, 2*a4, 1+4*a6
    c4 = b2*b2 - 24*b4
    c6 = -b2**3 + 36*b2*b4 - 216*b6
    numerator = c4**3 - c6**2
    delta, remainder = divmod(numerator, 1728)
    models.append({'a_invariants': [0, -1, 1, a4, a6], 'c4': c4, 'c6': c6,
                   'discriminant': delta, 'division_remainder': remainder,
                   'v3_discriminant': vp3(delta)})
residue_fifth_roots = [[a, b] for a in range(3) for b in range(3)
                       if power((a, b), 5) == (1, 0)]
zero = (0, 0)
expected_translation = [zero]*6 + [(1, 0)]
checks = {
    'all_thirteen_coefficients_match': h == original['polynomial']['ascending_coefficients'],
    'integer_division_reconstructs_all_coefficients': reconstruction == h,
    'both_exact_constant_values': [v['H_at_center'] for v in factors] == [[837, 282], [837, -282]] == [original['factor_certificate']['H_at_i'], original['factor_certificate']['H_at_minus_i']],
    'full_residue_factor_product': product == [(a % 3, 0) for a in h],
    'all_original_reductions_match': [a[0] for a in product] == original['polynomial']['mod_three'] == original['polynomial']['required_mod_three'],
    'quadratic_has_no_base_residue_root': [(a*a+1) % 3 for a in range(3)] == [1, 2, 2],
    'both_factors_monic_degree_six': all(len(v['residue_coefficients']) == 7 and v['residue_coefficients'][-1] == (1, 0) for v in factors),
    'both_full_translated_reductions': all(v['translated_residue_coefficients'] == expected_translation for v in factors),
    'both_constant_valuations_exactly_one': all(min(v['component_valuations']) == 1 for v in factors),
    'both_normalized_constants_nonzero': [v['normalized_constant_residue'] for v in factors] == [[0, 1], [0, 2]],
    'both_opposite_factors_are_units': all(v['opposite_factor_at_center'] == (2, 0) for v in factors),
    'residue_resultant_is_nonzero': list(resultant) == [1, 0] == original['factor_certificate']['residue_resultant'],
    'original_factor_arithmetic_matches': original['factor_certificate']['H_at_i_over_three_residue'] == [0, 1] and original['factor_certificate']['other_factor_at_i_residue'] == [2, 0] and original['factor_certificate']['actual_constant_valuation'] == original['factor_certificate']['required_constant_valuation'] == 1,
    'both_discriminants_exact': [m['discriminant'] for m in models] == [-11**5, -11] == original['image_application']['discriminants'] and all(m['division_remainder'] == 0 for m in models),
    'both_discriminants_are_units': [m['v3_discriminant'] for m in models] == [0, 0] == original['image_application']['three_adic_discriminant_valuations'],
    'all_residue_fifth_roots': residue_fifth_roots == [[1, 0]] and gcd(5, 9-1) == 1,
    'unit_derivative_at_one': 5 % 3 == 2,
    'degree_and_ef_accounting': 2*6 == 12 == len(h)-1,
}
certificate = {
    'method': 'Independent integer long division, full F9 polynomial multiplication and translation, c4/c6 discriminants. No construction code imported.',
    'polynomial': {'ascending_coefficients': h, 'division_quotient': quotient,
                   'division_remainder': r[:2], 'reconstruction': reconstruction,
                   'residue_factor_product': product},
    'factors_over_U': factors, 'residue_resultant': resultant,
    'models': models,
    'residue_kernel': {'all_fifth_roots': residue_fifth_roots, 'group_order': 8,
                       'kernel_exponent': 5, 'derivative_mod_three': 2},
    'bounds': {'constant_valuations_actual': [min(v['component_valuations']) for v in factors],
               'constant_valuations_required': [1, 1], 'total_degree_actual': 12,
               'total_degree_required': 12, 'residue_degree': 2, 'ramification_index': 6},
    'proof_obligations': 'Exact Hensel factor existence, Eisenstein irreducibility, Q3 root-field descent, actual residue field, good reduction and Schaefer-Stoll application are checked in L048; arithmetic flags alone do not prove these.',
    'checks': checks, 'failures': [name for name, ok in checks.items() if not ok],
}
OUT.write_text(json.dumps(certificate, indent=2)+'\n')
print(f'Independent arithmetic checks: {sum(checks.values())}/{len(checks)}; failures: {certificate["failures"]}')
print('Both constant valuations: actual=[1,1], required=[1,1]; complete degree actual=12, required=12.')
print('Both opposite-factor residues=(2,0), resultant=(1,0); discriminant valuations=[0,0]; residue fifth roots=[(1,0)].')
print(f'Certificate: {OUT.relative_to(Path.cwd())}')
if certificate['failures']:
    raise SystemExit(1)
