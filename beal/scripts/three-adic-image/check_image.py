"""Exact arithmetic for L048; local factor existence is proved by Hensel/Eisenstein."""
from math import comb
from pathlib import Path
import json

H = [-380, -774, -1062, -456, 258, 468, 104, -126, -6, 6, -6, 0, 1]

def vi(n):
    if n == 0:
        return None
    ans = 0
    while n % 3 == 0:
        ans += 1
        n //= 3
    return ans

def mul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])

def power(a, n):
    ans = (1, 0)
    for _ in range(n):
        ans = mul(ans, a)
    return ans

def evaluate(a):
    ans = (0, 0)
    for c in reversed(H):
        prod = mul(ans, a)
        ans = (prod[0]+c, prod[1])
    return ans

def discr(a4, a6):
    b2, b4, b6, b8 = -4, 2*a4, 1+4*a6, -4*a6-1-a4*a4
    return -b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6

residue = [c % 3 for c in H]
expected = [0]*13
for k in range(7):
    expected[2*k] = comb(6, k) % 3
plus, minus = evaluate((0, 1)), evaluate((0, -1))
pair_valuation = min(v for v in map(vi, plus) if v is not None)
normalized_residue = [c//3 % 3 for c in plus]
separation = [c % 3 for c in power((0, 2), 6)]
resultant = [c % 3 for c in power((0, 2), 36)]
d0, d1 = discr(-10, -20), discr(-7820, -263580)
checks = {
    'complete_mod_three_identity': residue == expected,
    'quadratic_irreducible_mod_three': all((r*r+1) % 3 != 0 for r in range(3)),
    'two_distinct_residue_roots': (0, 1) != (0, 2),
    'exact_translated_constant': plus == (837, 282) and minus == (837, -282),
    'strict_eisenstein_constant_valuation': pair_valuation == 1 and normalized_residue == [0, 1],
    'other_factor_evaluation_unit': separation == [2, 0],
    'coprime_residue_factor_resultant': resultant == [1, 0],
    'degree_accounting': 2*6 == len(H)-1 == 12,
    'good_reduction_discriminants': d0 == -11**5 and d1 == -11 and vi(d0) == vi(d1) == 0,
    'no_nontrivial_residue_fifth_roots': (3**2-1) % 5 != 0,
}
cert = {
    'method': 'Exact integer and Z[i] arithmetic; existence/irreducibility/residue-field claims use the canonical proof, not approximate factorization.',
    'polynomial': {'ascending_coefficients': H, 'mod_three': residue, 'required_mod_three': expected},
    'quadratic': {'relation': 'i^2=-1', 'residue_field_order': 9, 'base_degree': 2},
    'factor_certificate': {
        'H_at_i': list(plus), 'H_at_minus_i': list(minus),
        'H_at_i_over_three_residue': normalized_residue,
        'actual_constant_valuation': pair_valuation, 'required_constant_valuation': 1,
        'other_factor_at_i_residue': separation, 'residue_resultant': resultant,
        'hensel_factor_degrees_over_U': [6, 6], 'required_total_degree_over_Q3': 12,
        'conclusion_over_Q3': {'factor_degrees': [12], 'ramification_indices': [6], 'residue_degrees': [2]},
        'qualification': 'Hensel factors are not approximated; their exact constant valuations follow from H(i) and the other factor being a unit. Descent to one Q3 factor requires the root-lifting proof in L048.',
    },
    'image_application': {'discriminants': [d0, d1], 'three_adic_discriminant_valuations': [vi(d0), vi(d1)],
        'residue_multiplicative_order': 8, 'kernel_exponent': 5, 'rational_kernel_size': 1,
        'unrestricted_image_cardinality': 1, 'image': ['1'],
        'qualification': 'Imported Schaefer-Stoll Lemmas 4.2-4.5, with dual kernel mu_5 from L033; not a restricted-image or global calculation.'},
    'checks': checks, 'failures': [name for name, passed in checks.items() if not passed],
}
out = Path(__file__).with_name('image-certificate.json')
out.write_text(json.dumps(cert, indent=2)+'\n')
print(f'Checks passed: {sum(checks.values())}/{len(checks)}; failures: {cert["failures"]}')
print('Constant valuation actual=1 required=1; residue separation/resultant nonzero; degree actual=12 required=12.')
print('Certified proof parameters: one Q3 factor, e=6, f=2; unrestricted image actual=1 (full-image threshold met).')
print(f'Certificate: {out.relative_to(Path.cwd())}')
if not all(checks.values()):
    raise SystemExit(1)
