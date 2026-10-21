"""Independent multinomial reconstruction of all finite L095 evidence."""
import hashlib
import json
from math import factorial
from pathlib import Path


def coefficient(power, degree):
    # In (1+t+3t^2)^power choose j copies of t and k copies of 3t^2.
    return sum(
        factorial(power) // (factorial(i) * factorial(j) * factorial(k)) * 3**k
        for k in range(power + 1)
        for j in range(power - k + 1)
        for i in [power - j - k]
        if j + 2*k == degree
    )


directory = Path(__file__).resolve().parent
original_path = directory / 'identity-certificate.json'
raw = original_path.read_bytes()
original = json.loads(raw)
phi = [coefficient(5, k) - 5*coefficient(5, k-1) for k in range(12)]
h = [-phi[k] for k in range(3, 12)]
replayed = {
    'homogeneous_complement_all_coefficients': phi[:3] == [1, 0, 0] and h == original['H_ascending_m_degree'],
    'derivative_all_coefficients': all(k*phi[k] == -165*coefficient(4, k-3) for k in range(1, 12)),
    'degree_eleven': phi[11] == -1215,
    'H_constant_exactly_one_five': h[0] % 5 == 0 and h[0] % 25 != 0,
    'H_linear_divisible_by_five': h[1] % 5 == 0,
    'H_constant_exactly_one_eleven': h[0] % 11 == 0 and h[0] % 121 != 0,
    'H_all_lower_terms_divisible_by_eleven': all(c % 11 == 0 for c in h[:8]),
    'three_k_one_negative_cases': [5*j-11 for j in [1, 2]] == [-6, -1],
    'three_k_one_positive_residue': (-11) % 5 == 4,
    'three_k_ge_two_negative_residue': 5 % 11 == 5 and 5-22 < 0,
    'five_k_ge_two_negative_residue': 1 % 11 == 1 and 1-22 < 0,
    'five_k_one_negative_cases': [j-11 for j in range(1, 11)] == list(range(-10, 0)),
    'case_two_linear_scale': 5*5**10 == 5**11,
}
checks = {
    'all_original_check_names_and_values_match': replayed == original['checks'],
    'all_thirteen_replayed_checks_true': len(replayed) == 13 and all(replayed.values()),
    'complete_phi_coefficients_match': phi == original['phi_ascending_t_degree'],
    'complete_H_coefficients_match': h == original['H_ascending_m_degree'],
    'original_counts_and_failures_match': original['actual_passes'] == original['required_passes'] == 13 and original['failures'] == [],
    'denominator_cases_match': original['required_denominator_cases'] == ['n=C', 'n=5C'],
}
certificate = {
    'scope': 'Finite polynomial and residue evidence only; unbounded valuations and converses are audited in L095.',
    'original_sha256': hashlib.sha256(raw).hexdigest(),
    'original_purpose': original['purpose'],
    'original_exclusion_threshold': original['exclusion_threshold'],
    'independent_method': 'Multinomial coefficients, without the original convolution routine.',
    'phi_ascending_t_degree': phi,
    'H_ascending_m_degree': h,
    'replayed_checks': replayed,
    'audit_checks': checks,
    'actual_passes': sum(checks.values()),
    'required_passes': len(checks),
    'failures': [name for name, ok in checks.items() if not ok],
}
path = directory / 'audit-certificate.json'
path.write_text(json.dumps(certificate, indent=2) + '\n')
print(f'Original checks independently replayed: {sum(replayed.values())}/13.')
print(f'Audit checks: {sum(checks.values())}/{len(checks)}; failures: {certificate["failures"]}.')
print('Actual: exact identity evidence agrees. Required for exclusion: zero solutions; not established.')
print(f'Full certificate: {path.relative_to(directory.parent.parent)}')
assert all(checks.values()) and all(replayed.values())
