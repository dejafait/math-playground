"""Exact, bounded polynomial checks for L095; not a point search."""
import json
from pathlib import Path


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


q = [1, 1, 3]
power = [1]
for _ in range(5):
    power = mul(power, q)
phi = mul(power, [1, -5])
complement = [-x for x in phi]
complement[0] += 1
h = [55, 165, 594, 1100, 2145, 2475, 2970, 1782, 1215]
derivative = [(i + 1) * phi[i + 1] for i in range(11)]
q4 = [1]
for _ in range(4):
    q4 = mul(q4, q)
checks = {
    'homogeneous_complement_all_coefficients': complement == [0, 0, 0] + h,
    'derivative_all_coefficients': derivative == [0, 0] + [-165 * x for x in q4],
    'degree_eleven': len(phi) == 12 and phi[-1] == -1215,
    'H_constant_exactly_one_five': h[0] % 5 == 0 and h[0] % 25 != 0,
    'H_linear_divisible_by_five': h[1] % 5 == 0,
    'H_constant_exactly_one_eleven': h[0] % 11 == 0 and h[0] % 121 != 0,
    'H_all_lower_terms_divisible_by_eleven': all(x % 11 == 0 for x in h[:-1]),
    'three_k_one_negative_cases': all((5 * j - 11) < 0 and (5 * j - 11) % 11 != 0 for j in (1, 2)),
    'three_k_one_positive_residue': (-11) % 5 != 0,
    'three_k_ge_two_negative_residue': 5 % 11 != 0 and 5 - 11 * 2 < 0,
    'five_k_ge_two_negative_residue': 1 % 11 != 0 and 1 - 11 * 2 < 0,
    'five_k_one_negative_cases': all((j - 11) < 0 and (j - 11) % 11 != 0 for j in range(1, 11)),
    'case_two_linear_scale': 5**11 // 5 == 5**10,
}
result = {
    'purpose': 'Exact identities and finite residue checks only; valuation arguments and converses are proved in L095.',
    'H_ascending_m_degree': h,
    'phi_ascending_t_degree': phi,
    'checks': checks,
    'actual_passes': sum(checks.values()),
    'required_passes': len(checks),
    'failures': [k for k, v in checks.items() if not v],
    'required_denominator_cases': ['n=C', 'n=5C'],
    'exclusion_threshold': 'Zero positive solutions of both simultaneous systems; NOT established.',
}
path = Path(__file__).with_name('identity-certificate.json')
path.write_text(json.dumps(result, indent=2) + '\n')
print(f'Checks: {result["actual_passes"]}/{result["required_passes"]}; failures: {result["failures"]}')
print('Actual result: two exact power systems; required for branch exclusion: zero solutions (unproved).')
print(f'Full certificate: {path}')
assert all(checks.values())
