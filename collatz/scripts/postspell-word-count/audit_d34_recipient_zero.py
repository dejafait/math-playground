#!/usr/bin/env python3
"""Independent finite audit of L098; analytic bounds remain cited imports.

Does not import or execute the construction program. The written audit
checks the quantified implication; this file checks its finite operands.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
source = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
construction = HERE / 'd34-recipient-zero-certificate.json'
old = json.loads(construction.read_text())

# Separate transcription from the canonical table, not the constructor.
base = [
    (8, 40), (15, 72), (28, 134), (52, 249), (98, 467),
    (184, 877), (347, 1650), (653, 3106), (1230, 5849),
    (2317, 11018), (4365, 20756), (8224, 39104), (15494, 73672),
    (29191, 138802), (54998, 261511), (103621, 492705),
    (195229, 928293), (367827, 1748976), (693015, 3295208),
    (1305695, 6208431), (2460032, 11697176), (4634896, 22038409),
    (8732512, 41522114), (16452748, 78230965), (30998279, 32670621),
]
rows = [[i, j, h] for i, (j, h) in enumerate(base)]
rows[0][2] = 6
rows[24][2] = 32670655
B = 9250245
J = sum(row[1] for row in rows)
H = sum(row[2] for row in rows)
tails = 18*B + 50
K = sum(3*j+h for _, j, h in rows)
N = sum(4*j+h for _, j, h in rows) + tails
kappa = Q(23, 11)
lam = Q(10584, 10**14)
guard_n1 = Q(2**62-23, 11)
E = 24*kappa/guard_n1
residual = lam-E
R = kappa*(1+1/residual)
U = Q(20_000_000_000)

# Rebuild row0 from its prime exponents and combined offset numerator.
G = Q(3**30, 2**38)
offset_Q = Q(12*3**6 + 11*2**6, 11*2**6)
signed_offset = Q(23*2**26-12*3**6-11*2**6, 11*2**26)
endpoint = Q(3**30*11*int(U) - (12*3**6+11*2**6)*2**32
             + 23*2**58, 11*2**58)
coefficient = Q(3**24, 2**32)*U-Q(12, 11)
factored = Q(3**6, 2**26)*coefficient+kappa-Q(1, 2**20)
threshold = Q(2**62, 11)
cap = dict(lambda_lower=lam, E=E, residual=residual, R=R, U=U)
signed = dict(G0=G, Q0=offset_Q, signed_offset=signed_offset,
              coefficient=coefficient, endpoint=endpoint,
              factored_endpoint=factored, endpoint_bound=15_000_000,
              endpoint_slack=15_000_000-endpoint, row1_threshold=threshold,
              strict_separation=threshold-endpoint)
checks = []


def check(name, actual, relation, required):
    passed = {'<': actual < required, '>': actual > required,
              '==': actual == required}[relation]
    checks.append(dict(name=name, actual=actual, relation=relation,
                       required=required, difference=actual-required,
                       passed=passed))


check('row count', len(rows), '==', 25)
check('changed H0', rows[0][2], '==', 6)
check('changed H24', rows[-1][2], '==', 32670655)
check('minimum H', min(h for _, _, h in rows), '>', 2)
check('first J', rows[0][1], '==', 8)
check('next J', rows[1][1], '==', 15)
check('minimum J increment', min(b[1]-a[1] for a, b in zip(rows, rows[1:])), '>', 0)
check('sum J invariant', J, '==', 66061058)
check('sum H invariant', H, '==', 199390205)
check('total tails', tails, '==', 166504460)
check('K invariant', K, '==', 397573379)
check('N invariant', N, '==', 630138897)
check('positive residual', residual, '>', 0)
check('guard-conditioned cap', R, '<', U)
check('failed old offset datum preserved', offset_Q, '<', kappa*2**20)
check('actual signed offset positive', signed_offset, '>', 0)
check('direct and factored endpoints agree', endpoint, '==', factored)
check('signed endpoint upper', endpoint, '<', Q(15_000_000))
check('row1 threshold lower', threshold, '>', Q(4*10**17))
check('strict signed rejection', endpoint, '<', threshold)

comparisons = []


def compare(path, actual, expected):
    if isinstance(expected, dict):
        comparisons.append(dict(path=path+'/keys', actual=sorted(actual),
                                expected=sorted(expected), passed=set(actual)==set(expected)))
        for key, value in expected.items():
            if key in actual:
                compare(path+'/'+key, actual[key], value)
        return
    if isinstance(expected, list):
        comparisons.append(dict(path=path+'/length', actual=len(actual),
                                expected=len(expected), passed=len(actual)==len(expected)))
        for i, (a, e) in enumerate(zip(actual, expected)):
            compare(path+'/'+str(i), a, e)
        return
    matches = Q(actual) == expected if isinstance(expected, Q) else actual == expected
    comparisons.append(dict(path=path, actual=actual, expected=expected, passed=matches))


canonical = [[int(i), int(j), int(h)] for i, j, h in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', source.read_text(), re.M)]
compare('/canonical_table', canonical, [[i, j, h] for i, (j, h) in enumerate(base)])
expected = dict(source=dict(path=str(source.relative_to(ROOT)),
                            sha256=hashlib.sha256(source.read_bytes()).hexdigest()),
                rows=rows, B=B, sum_J=J, sum_H=H, sum_a=tails, K=K, N=N,
                cap=cap, signed_comparison=signed, checks=checks,
                summary=dict(checks=20, failures=[], passed=True))
compare('/top_level_keys', sorted(old), sorted(list(expected)+[
    'scope', 'imported_analytic_input', 'limitations']))
for key, value in expected.items():
    compare('/construction/'+key, old[key], value)

# Exact displayed operands, in addition to certificate comparisons.
displayed = {
    'E': (E, Q(552, 4611686018427387881)),
    'residual': (residual, Q(6101253702379434166563, 57646075230342348512500000000000)),
    'R': (R, Q(1325859730438202850942226985830949, 67113790726173775832193)),
    'G0': (G, Q(205891132094649, 274877906944)),
    'Q0': (offset_Q, Q(2363, 176)),
    'offset': (signed_offset, Q(385873605, 184549376)),
    'endpoint': (endpoint, Q(22117214692422282938715, 1548112371908608)),
    'endpoint_slack': (15_000_000-endpoint, Q(1104470886206837061285, 1548112371908608)),
    'threshold': (threshold, Q(4611686018427387904, 11)),
}
for key, (actual, required) in displayed.items():
    compare('/displayed/'+key, actual, required)

failures = [c['name'] for c in checks if not c['passed']]
mismatches = [c['path'] for c in comparisons if not c['passed']]
result = dict(
    scope='Independent finite audit of L098 only; full-simplex proof checked in lemma audit.',
    construction_sha256=hashlib.sha256(construction.read_bytes()).hexdigest(),
    imported_analytic_input=old['imported_analytic_input'],
    provenance={k: old[k] for k in ['scope', 'limitations']},
    reconstruction=expected, comparisons=comparisons,
    summary=dict(mathematical_checks=len(checks), comparison_records=len(comparisons),
                 failures=failures, mismatches=mismatches, passed=not failures and not mismatches),
    limitations='No new analytic certification, allocation sampling, other recipients or downstream assembly.')
out = HERE / 'd34-recipient-zero-audit-certificate.json'
out.write_text(json.dumps(result, indent=2, default=str)+'\n')
print(f'Mathematical checks: {len(checks)}; comparison records: {len(comparisons)}')
print(f'Failures: {failures}; mismatches: {mismatches}')
print(f'Cap actual {R}; required < {U}')
print(f'Endpoint actual {endpoint}; required < 15000000')
print(f'Own-input threshold {threshold}; required > 400000000000000000')
print(f'Certificate: {out.relative_to(ROOT)}')
if failures or mismatches:
    raise SystemExit(1)
