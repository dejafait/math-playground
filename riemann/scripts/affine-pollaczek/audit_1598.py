#!/usr/bin/env python3
"""Full saved-certificate replay and independent top-coefficient check for C028k.

The all-degree argument and converse are audited in the canonical lemma.
Finite cases here are exact checks, never a substitute for that argument.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import contextlib
import io
import json
import runpy
import tempfile

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'feasibility_1596.py'
SAVED = HERE / 'feasibility-1596.json'
OUT = HERE / 'audit-1598.json'
saved_bytes = SAVED.read_bytes()
saved = json.loads(saved_bytes)

# Run the original unchanged program in an isolated directory, retaining
# the entire pre-existing certificate byte for byte.
with tempfile.TemporaryDirectory(prefix='c028k-audit1598-') as directory:
    replay_script = Path(directory) / SOURCE.name
    replay_script.write_bytes(SOURCE.read_bytes())
    with contextlib.redirect_stdout(io.StringIO()):
        runpy.run_path(str(replay_script), run_name='__main__')
    replay_bytes = (Path(directory) / SAVED.name).read_bytes()

independent = []

def record(label, actual, required):
    independent.append(dict(label=label, actual=str(actual),
                            required=str(required), passed=actual == required))

for d in (5, 6, 9, 17):
    for lam in (Q(1, 5), Q(1), Q(7, 2)):
        for c in (Q(-2), Q(0), Q(3, 2)):
            r, m = c*c/4+Q(1, 7), Q(2, 9)
            diagonal = [m-(i+lam)*c for i in range(d)]
            edges = [r*n*(n+2*lam-1) for n in range(1, d)]
            # Direct determinant expansion through order three: the only
            # nonidentity permutation possible at these orders is one
            # adjacent transposition. No polynomial recurrence is used.
            e1 = sum(diagonal, Q(0))
            e2 = sum((a*b for a, b in combinations(diagonal, 2)), Q(0))
            e2 -= sum(edges, Q(0))
            e3 = sum((a*b*z for a, b, z in combinations(diagonal, 3)), Q(0))
            e3 -= sum((beta*(e1-diagonal[n-1]-diagonal[n])
                       for n, beta in enumerate(edges, 1)), Q(0))
            power2, power3 = e1**2-2*e2, e1**3-3*e1*e2+3*e3
            mean = e1/d
            center2 = power2-d*mean**2
            center3 = power3-3*mean*power2+2*d*mean**3
            prefix = f'd={d},lambda={lam},c={c}'
            record(prefix+'/mean', mean, m-c*(lam+Q(d-1, 2)))
            record(prefix+'/central2', center2,
                   d*(d-1)*(c*c*Q(d+1, 12)+Q(2, 3)*r*(d+3*lam-2)))
            record(prefix+'/central3', center3,
                   -c*r*Q(d*(d-1)*(d-2), 2)*(d+2*lam-1))
            # This is tr(K^3)/(3*c*r) when c != 0; its sum is also
            # directly evaluated for c=0, where division would be invalid.
            edge_sum = sum((Q(n)*(n+2*lam-1)*(d-2*n)
                            for n in range(1, d)), Q(0))
            record(prefix+'/edge_sum', edge_sum,
                   -Q(d*(d-1)*(d-2), 6)*(d+2*lam-1))
    k0 = Q(d+1, 4*(d-2))
    V0 = Q(d+1, 12)+Q(2, 3)*k0*(d-2)
    ceiling = Q((d-1)**2, (d+1)*(d-2)**2)
    record(f'd={d}/supremum_identity', k0**2*(d-1)**2/(4*V0**3), ceiling)
    record(f'd={d}/ceiling_bound', ceiling <= Q(16, 9*(d+1)), True)
    for k in (Q(3, 10), Q(1), Q(5)):
        for lam in (Q(1, 5), Q(1), Q(7, 2)):
            V = Q(d+1, 12)+Q(2, 3)*k*(d+3*lam-2)
            D = d+2*lam-1
            # Independently differentiate log(k^2*D^2/(4*V^3)).
            log_derivative = Q(4)/D-Q(6)*k/V
            numerator = log_derivative*V*D
            record(f'd={d},k={k},lambda={lam}/lambda_derivative', numerator,
                   (d+1-2*k*(5*d+6*lam-1))/3)
            record(f'd={d},k={k},lambda={lam}/derivative_negative',
                   log_derivative < 0, True)

# Compare every complete record, including all actual/required rational
# values and labels. A bounded preview of the certificate is not used.
conditions = dict(
    exact_replay_byte_match=replay_bytes == saved_bytes,
    original_preserved=SAVED.read_bytes() == saved_bytes,
    saved_result_pass=saved.get('result') == 'PASS',
    saved_failures_empty=saved.get('failures') == [],
    exactly_224_records=len(saved.get('checks', [])) == len(independent) == 224,
    all_complete_records_match=saved.get('checks') == independent,
    independent_records_pass=all(row['passed'] for row in independent),
)
failures = [name for name, passed in conditions.items() if not passed]
failures.extend(row['label'] for row in independent if not row['passed'])
report = dict(
    summary=dict(result='PASS' if not failures else 'FAIL',
                 saved_sha256=sha256(saved_bytes).hexdigest(),
                 replayed_records=len(saved.get('checks', [])),
                 independent_records=len(independent), conditions=conditions,
                 failures=failures,
                 actual_bound='rho < M_d <= 16/(9*(d+1))',
                 required_condition='rho=tau^2/v^3>0 fixed; no unbounded feasible degrees',
                 limitations='Finite checks only; the all-degree strict bound and converse are audited in C028k.'),
    complete_independent_records=independent,
)
OUT.write_text(json.dumps(report, indent=2)+'\n')
print(f"{report['summary']['result']}: 224 saved records replayed and independently compared in full; failures={len(failures)}")
print('Actual ceiling: rho < M_d <= 16/(9*(d+1)); required rho>0 is fixed.')
print(f'Full audit certificate: {OUT}')
if failures:
    print(failures)
    raise SystemExit(1)
