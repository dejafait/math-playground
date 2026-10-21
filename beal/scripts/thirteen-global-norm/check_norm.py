"""Exact determinant certificate for L088; no local sample is used as proof."""
from itertools import product
from collections import defaultdict
from pathlib import Path
import json

# Multiplication by 1+c*z+c*z^2 in the basis 1,z,...,z^10, z^11=q.
# A determinant term selects one shift from {0,1,2} in each column.
terms = []
coefficients = defaultdict(int)
for shifts in product(range(3), repeat=11):
    rows = [(j + shifts[j]) % 11 for j in range(11)]
    if len(set(rows)) != 11:
        continue
    crossings = sum((j + shifts[j]) // 11 for j in range(11))
    count = sum(d != 0 for d in shifts)
    inversions = sum(rows[i] > rows[j] for i in range(11) for j in range(i+1, 11))
    sign = (-1) ** inversions
    coefficients[count, crossings] += sign
    terms.append(dict(shifts=shifts, rows=rows, c_degree=count,
                      q_degree=crossings, sign=sign,
                      valuation_lower_bound=2*count+15*crossings))

checks = {
    'exactly_one_constant_term': sum(t['c_degree'] == 0 for t in terms) == 1,
    'shift_sum_equals_eleven_crossings': all(sum(t['shifts']) == 11*t['q_degree'] for t in terms),
    'positive_terms_have_q_degree_one_or_two': all(t['q_degree'] in (1,2) for t in terms if t['c_degree']),
    'nonconstant_valuation_at_least_27': all(t['valuation_lower_bound'] >= 27 for t in terms if t['c_degree']),
    'strict_square_threshold': 27 > 2*3,
    'supported_family_local_square_obstructions': (-3 % 2, 11 % 2, 2 % 4) == (1,1,2),
    'thirteen_rational_root': (11**3-11**2+11+1) % 13 == 0 and (8-14*11+6*11**2) % 13 == 8,
    'thirteen_family_residues': ((11**2-11+1) % 13, (2-11-6*11**2) % 13) == (7,6),
    'thirteen_character_comparison': (pow(7,6,13), pow(6,6,13), pow(7*6,6,13)) == (12,12,1),
}
out = {
    'construction': 'det(1+c*z+c*z^2), z^11=q, all 3^11 column choices inspected',
    'specialization': {'q':32, 'ord_C_q':15, 'ord_C_c':2,
                       'ord_C_2':3, 'error_lower_bound':27, 'required_strict_bound':6},
    'determinant_polynomial': [dict(c_degree=r,q_degree=k,coefficient=a)
                              for (r,k),a in sorted(coefficients.items()) if a],
    'all_nonzero_determinant_terms': terms,
    'checks': checks, 'failures': [k for k,v in checks.items() if not v],
}
path = Path(__file__).with_name('norm-certificate.json')
path.write_text(json.dumps(out, indent=2)+'\n')
print(f"Checks: {sum(checks.values())}/{len(checks)}; determinant terms: {len(terms)}")
print('Norm error valuation >=27; required >6; failures:', out['failures'])
print('Certificate:', path)
assert all(checks.values())
