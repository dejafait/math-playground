"""Independent full-record arithmetic audit for L096; exact integers only."""
import hashlib
import json
from pathlib import Path


def multiply(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def horner(coefficients, x):
    result = 0
    for c in reversed(coefficients):
        result = result * x + c
    return result


def v11(x):
    if not x:
        return None
    power = 0
    while x % 11 == 0:
        x //= 11
        power += 1
    return power


directory = Path(__file__).resolve().parent
source = directory / 'eleven-lifts-certificate.json'
raw = source.read_bytes()
original = json.loads(raw)
# Expand Q(1,N)^5(N-5); recover H(1,N) from the full complement.
qpower = [1]
for _ in range(5):
    qpower = multiply(qpower, [3, 1, 1])
product = multiply(qpower, [-5, 1])
complement = [-c for c in product]
complement[11] += 1
h = complement[:9]
audits = {
    'full_complement_coefficients': complement[9:] == [0, 0, 0]
    and h == [1215, 1782, 2970, 2475, 2145, 1100, 594, 165, 55],
    'uniform_H_residue': h[0] % 11 == 5
    and all(c % 11 == 0 for c in h[1:]),
}
records = []
replayed = []
for name, d, root in [('I', 1, 3), ('II', 5, 1)]:
    m = u = 1
    c = 5 * m + u**5 if name == 'I' else m + 5**10 * u**5
    n = d * c
    q = horner([3, 1, 1], n)
    hv = horner(h, n)
    scale = d**11
    error = scale * root**3 - hv
    derivative = 3 * scale * root**2
    residues = dict(a=root % 11, A=root % 11, B=q % 11, C=c % 11)
    checks = {
        'linear_equation': c == (6 if name == 'I' else 9765626),
        'complement_identity': n**11 - q**5 * (n - 5) == hv,
        'linear_numerator': n - 5 == scale,
        'H_residue': hv % 11 == 5,
        'error_divisible_by_11': error % 11 == 0,
        'derivative_unit': derivative % 11 != 0,
        'strict_hensel_bound': v11(error) is not None
        and v11(error) > 2 * v11(derivative),
        'all_coordinate_residues_nonzero': all(
            x % 11 != 0 for x in [m, u, root, root, q, c]),
    }
    reconstructed = dict(system=name, m=m, u=u, C=c, n=n, Q=q, H=hv,
                         scale=scale, a0=root, error=error, derivative=derivative,
                         error_valuation=v11(error), derivative_valuation=v11(derivative),
                         residues=residues, checks=checks)
    replayed.append(reconstructed)
    independent = {
        'error_exactly_one_eleven': error % 11 == 0 and error % 121 != 0,
        'hensel_n_one_k_zero': v11(error) == 1 and v11(derivative) == 0,
        'uniqueness_factor_unit': (scale * 3 * root**2) % 11 != 0,
        # For variable X and A=X, this is scale*(C^11-B^5-X^3)=-F(X).
        'reconstruction_constant_and_cubic': scale * (c**11 - q**5) == hv,
        'cancellation_scale_unit': scale % 11 != 0,
        'all_seven_coordinates_unit': all(
            x % 11 != 0 for x in [m, u, root, root, q, c, n]),
    }
    audits.update({f'{name}:{key}': value for key, value in independent.items()})
    records.append(dict(reconstructed_record=reconstructed,
                        error_divided_by_11_residue=(error // 11) % 11,
                        uniqueness_factor_residue=(3 * scale * root**2) % 11,
                        required_error_valuation_strictly_greater_than=2*v11(derivative),
                        independent_checks=independent))
expected = dict(records=replayed, checks=16, failures=[])
audits['entire_original_certificate_equal'] = expected == original
audits['all_sixteen_replayed_assertions_pass'] = all(
    all(r['checks'].values()) for r in replayed)
failures = [key for key, passed in audits.items() if not passed]
output = directory / 'eleven-lifts-audit-certificate.json'
certificate = dict(
    scope='Exact finite hypotheses and reconstruction; Hensel existence and disk uniqueness are justified in L096.',
    original_sha256=hashlib.sha256(raw).hexdigest(),
    independent_method='Polynomial convolution and Horner evaluation; no import or execution of the original script.',
    full_complement_ascending_N=complement, records=records, audit_checks=audits,
    actual_passes=sum(audits.values()), required_passes=len(audits), failures=failures)
output.write_text(json.dumps(certificate, indent=2) + '\n')
for r in records:
    v = r['reconstructed_record']
    print(f"{v['system']}: v11(error)={v['error_valuation']} > required "
          f"{r['required_error_valuation_strictly_greater_than']}; "
          f"v11(derivative)={v['derivative_valuation']}; residues={v['residues']}")
print(f"Replayed assertions: 16/16; audit: {sum(audits.values())}/{len(audits)}; failures: {failures}")
print('Conclusion: both exact local lifts certified using Hensel; integer exclusion not established.')
print(f'Full certificate: {output.relative_to(directory.parent.parent)}')
assert not failures
