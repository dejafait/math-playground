"""Exact L001 grid certificate; run from the active notebook directory."""
import json
from math import comb, factorial, prod
from pathlib import Path

n, k, Q, extension, threshold_denominator = 1024, 64, 65537, 28, 2**128
q = Q**extension
numerator = comb(n, k)
assert numerator * factorial(k) == prod(range(n-k+1, n+1))
rows = []
failures = []
for t in range(n-k+1):
    denominator = comb(n-t, k)
    assert denominator * factorial(k) == prod(range(n-t-k+1, n-t+1))
    bound, remainder = divmod(numerator, denominator)
    assert 0 <= remainder < denominator
    delta = q - bound * threshold_denominator
    rows.append(dict(t=t, agreements=n-t, denominator=denominator,
                     bound=bound, remainder=remainder,
                     threshold_comparison_difference=delta, safe=delta >= 0))
    if t and rows[-2]['bound'] > bound:
        failures.append(f'nonmonotone bound at {t}')
endpoint = max(row['t'] for row in rows if row['safe'])
if not all(row['safe'] == (row['t'] <= endpoint) for row in rows):
    failures.append('safe grid is not the expected initial segment')
if endpoint != 955:
    failures.append(f'unexpected endpoint {endpoint}')
assert rows[955]['bound'] < 2**318
assert rows[956]['bound'] > 2**321
# Independently reconstruct the pre-existing L019 averaging certificate.
unsafe_count = (comb(n,66) + Q*n - 1)//(Q*n)
if unsafe_count * threshold_denominator <= q:
    failures.append('L019 lower certificate does not exceed threshold')
if not 2**320 * threshold_denominator < q < 2**321 * threshold_denominator:
    failures.append('ambient threshold power-of-two bracket fails')
certificate = dict(parameters=dict(n=n,k=k,Q=Q,extension=extension,q=q,
    threshold_denominator=threshold_denominator), binomial_n_k=numerator,
    largest_certified_safe_index=endpoint, adjacent_comparisons=rows[endpoint:endpoint+2],
    grid=rows, unsafe_certificate=dict(error_index=958,lower_count=unsafe_count,
    threshold_excess=unsafe_count*threshold_denominator-q),
    pinned_boundary_bracket=[endpoint,957], failures=failures)
path = Path('scripts/finite-support/fixed-instance-bracket-results.json')
path.write_text(json.dumps(certificate, indent=2)+'\n')
print(f'Checked {len(rows)} indices; failures: {failures}')
for row in rows[endpoint:endpoint+2]:
    print(f"t={row['t']}, A={row['agreements']}, bound={row['bound']}; required bound*2^128 <= {q}: {row['safe']}")
print(f'Largest L001-certified index: {endpoint}; pinned boundary bracket: [{endpoint},957]')
print(f'Full certificate: {path}')
assert not failures
