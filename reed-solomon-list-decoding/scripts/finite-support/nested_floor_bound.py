"""Approved Johnson-Schonheim bound, with complete ordered-floor evidence."""
import json
from fractions import Fraction
from math import comb
from pathlib import Path

n, k, Q = 1024, 64, 65537
q, scale = Q**28, 2**128
failures, cases = [], []
for t in (956, 957):
    b, u, stages = n-t, 1, []
    for i in range(k-1, -1, -1):
        previous = u
        numerator, denominator = (n-i)*previous, b-i
        u, remainder = divmod(numerator, denominator)
        stages.append(dict(i=i, previous=previous, numerator=numerator,
                           denominator=denominator, quotient=u, remainder=remainder))
        if numerator != denominator*u+remainder or not 0 <= remainder < denominator:
            failures.append(f'bad division at t={t}, i={i}')
    # Independent exact-rational floor evaluation, in the same theorem order.
    rational_u = 1
    for i in reversed(range(k)):
        rational_u = Fraction((n-i)*rational_u, b-i).__floor__()
    if rational_u != u or len(stages) != k:
        failures.append(f'recurrence cross-check failed at t={t}')
    support_bound = comb(n,k)//comb(b,k)
    if u > support_bound:
        failures.append(f'nested bound exceeds unfloored support bound at t={t}')
    ratio = Fraction(scale*u, q)
    ratio_milli = (1000*ratio.numerator)//ratio.denominator
    cases.append(dict(error_index=t, agreements=b, stages=stages, bound=u,
        support_bound=support_bound, improvement=support_bound-u,
        scaled_bound=scale*u, required_maximum=q,
        threshold_excess=scale*u-q, certifies_safety=scale*u<=q,
        threshold_ratio_numerator=ratio.numerator,
        threshold_ratio_denominator=ratio.denominator,
        ratio_milli_lower=ratio_milli, ratio_milli_upper=ratio_milli+1))

certificate = dict(parameters=dict(n=n,k=k,Q=Q,extension=28,q=q,
    threshold_denominator=scale), cases=cases, failures=failures)
path = Path('scripts/finite-support/nested-floor-results.json')
path.write_text(json.dumps(certificate, indent=2)+'\n')
for case in cases:
    print(f"t={case['error_index']}, A={case['agreements']}, U={case['bound']}")
    print(f"Actual 2^128*U={case['scaled_bound']}; required <= {q}; safe certificate: {case['certifies_safety']}")
    print(f"Threshold ratio in [{case['ratio_milli_lower']}/1000,{case['ratio_milli_upper']}/1000)")
print(f'Checked 128 ordered floors; failures: {failures}; full certificate: {path}')
assert not failures
