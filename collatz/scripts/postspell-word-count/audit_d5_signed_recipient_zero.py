#!/usr/bin/env python3
"""Independent finite audit of L085; no constructor is imported or executed.

The quantified proof is in L085. Fractions and cross products certify
finite arithmetic only. The log remainder is the already assessed DLMF
4.6.4 specialization used in L055/L076's audits.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = HERE / 'd5-signed-recipient-zero-certificate.json'
raw = SOURCE.read_bytes()
old = json.loads(raw)
base = [
    (8, 40), (15, 72), (28, 134), (52, 249), (98, 467),
    (184, 877), (347, 1650), (653, 3106), (1230, 5849),
    (2317, 11018), (4365, 20756), (8224, 39104),
    (15494, 73672), (29191, 138802), (54998, 261511),
    (103621, 492705), (195229, 928293), (367827, 1748976),
    (693015, 3295208), (1305695, 6208431), (2460032, 11697176),
    (4634896, 22038409), (8732512, 41522114),
    (16452748, 78230965), (30998279, 32670621),
]
rows = [[i, j, h] for i, (j, h) in enumerate(base)]
rows[0][2] = 35
rows[24][2] = 32670626
B = 9250245
kappa = F(23, 11)
sum_j = sum(j for _, j, _ in rows)
sum_h = sum(h for _, _, h in rows)
tails = 2 * len(rows) + 18 * B
K = 3 * sum_j + sum_h
N = 4 * sum_j + sum_h + tails
lam = F(10584, 10**14)
E = F(24 * 23, 4 * (1 << 60) - 23)
residual = lam - E
cap = kappa / residual + kappa
U = F(20_000_000_000)
G = F(27, 16)**8 * F(3, 2)**35
Q = F(12, 11) * F(3, 2)**35 + 1
eta0 = kappa - Q/G
offset = kappa - Q/(1 << 20)
endpoint = (G*U - Q)/(1 << 20) + kappa
threshold = F(1 << 62, 11)

proof_checks = []
def verify(name, passed):
    proof_checks.append({'name': name, 'passed': bool(passed)})

canonical = [tuple(map(int, t)) for t in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$',
    (ROOT/'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text(),
    re.M)]
verify('independent transcription equals all canonical L055 rows',
       canonical == [(i, j, h) for i, (j, h) in enumerate(base)])
verify('changed rows equal complete stored table', old['rows'] == rows)
verify('only H0 and H24 changed, with opposite differences',
       [(i, h-base[i][1]) for i, _, h in rows if h != base[i][1]]
       == [(0, -5), (24, 5)])
verify('table domains and all 24 J lower comparisons',
       all(j >= 2 and h >= 3 for _, j, h in rows)
       and all(rows[i+1][1] > rows[i][1] for i in range(24))
       and all(j >= 15 for _, j, _ in rows[1:]))
verify('complete fixed sums including every tail',
       (sum_j, sum_h, tails, K, N) ==
       (66061058, 199390205, 166504460, 397573379, 630138897))
verify('lower domain shifts to n>=47', F(540, 11)-kappa == 47)
verify('row0 eta is strictly between zero and kappa', 0 < eta0 < kappa)
verify('positive row0 bracket at entire lower domain', G*F(540, 11)-Q > 0)
verify('independent row0 multiplier exponents', G == F(3**59, 2**67))
verify('shifted and unshifted endpoint evaluations agree',
       endpoint == G*F(1, 1 << 20)*(U-kappa+eta0)+kappa)

def log_interval(t):
    x = (t-1)/(t+1)
    assert 0 < x < 1
    terms = [2*x**(2*m+1)/(2*m+1) for m in range(96)]
    lower = sum(terms, F(0))
    remainder = 2*x**193/(193*(1-x*x))
    return dict(argument=t, x=x, terms=terms, remainder=remainder,
                lower=lower, upper=lower+remainder)

log2 = log_interval(F(2))
log3 = log_interval(F(3))
lambda_lo = N*log2['lower'] - K*log3['upper']
lambda_hi = N*log2['upper'] - K*log3['lower']
grid_scale = 10**18
grid_lo = F((lambda_lo*grid_scale).__floor__(), grid_scale)
grid_hi = F((lambda_hi*grid_scale).__ceil__(), grid_scale)
verify('independent Lambda interval strictly inside imported enclosure',
       lam < grid_lo <= lambda_lo < lambda_hi <= grid_hi < F(10585, 10**14))

expected = dict(B=B, K=K, N=N, lambda_lower=lam, E=E,
                residual=residual, cap=cap, U=U, G0=G, Q0=Q,
                signed_offset=offset, endpoint_upper=endpoint,
                row1_threshold=threshold, strict_separation=threshold-endpoint)
for key, value in expected.items():
    verify('stored numerical field '+key, F(old[key]) == value)

# Reconstruct each original comparison independently, including its operands,
# sign, exact difference and verdict. Evaluate signs using integer products.
specs = [
    ('row count', 25, '==', 25),
    ('minimum H', min(h for _, _, h in rows), '>', 2),
    ('minimum J increment', min(rows[i+1][1]-rows[i][1] for i in range(24)), '>', 0),
    ('K invariant', K, '==', 397573379),
    ('N invariant', N, '==', 630138897),
    ('positive residual', residual, '>', 0),
    ('guard-conditioned cap', cap, '<', U),
    ('failed old offset datum preserved', Q, '<', kappa*(1 << 20)),
    ('actual signed offset positive', offset, '>', 0),
    ('signed endpoint upper', endpoint, '<', 2*10**12),
    ('row-1 threshold lower', threshold, '>', 4*10**17),
    ('strict signed rejection', endpoint, '<', threshold),
]
verify('exact original check names and ordering',
       [c['name'] for c in old['checks']] == [s[0] for s in specs])
comparisons = []
for record, (name, a, relation, b) in zip(old['checks'], specs):
    a, b = F(a), F(b)
    delta = a.numerator*b.denominator-b.numerator*a.denominator
    passed = {'==': delta == 0, '<': delta < 0, '>': delta > 0}[relation]
    same = (set(record) == {'name', 'actual', 'relation', 'required', 'difference', 'passed'}
            and record['name'] == name and F(record['actual']) == a
            and record['relation'] == relation and F(record['required']) == b
            and F(record['difference']) == a-b and record['passed'] is passed)
    verify('reconstructed complete comparison '+name, same and passed)
    comparisons.append(dict(name=name, actual=a, relation=relation, required=b,
                            difference=a-b, cross_product_difference=delta,
                            passed=passed, matches_original=same))
verify('original summary matches reconstructed verdicts',
       old['summary'] == dict(checks=12, failures=[], passed=True))
verify('no unexamined construction fields', set(old) == set(expected) | {
    'scope', 'imported_analytic_input', 'rows', 'checks', 'summary', 'limitations'})
verify('construction certificate unchanged', SOURCE.read_bytes() == raw)
failures = [c['name'] for c in proof_checks if not c['passed']]
result = dict(
    construction_sha256=sha256(raw).hexdigest(),
    original_scope=old['scope'], original_analytic_status=old['imported_analytic_input'],
    original_limitations=old['limitations'], rows=rows, values=expected,
    row0_eta=eta0, original_comparisons=comparisons,
    analytic=dict(log2=log2, log3=log3, lambda_lower=lambda_lo,
                  lambda_upper=lambda_hi,
                  lambda_grid=dict(lower=grid_lo, upper=grid_hi,
                                   required_lower=lam, required_upper=F(10585, 10**14))),
    proof_checks=proof_checks,
    summary=dict(checks=len(proof_checks), original_comparisons=len(comparisons),
                 failures=failures, passed=not failures),
    limitations='Finite operands only; all-allocation implication and cap independence audited in L085. '
                'No new recipient, order, realization or universal-descent result.')
out = HERE/'d5-signed-recipient-zero-audit-certificate.json'
out.write_text(json.dumps(result, indent=2, default=str)+'\n')
print(f'Independent checks: {len(proof_checks)}; original comparisons: {len(comparisons)}; failures: {failures}')
print(f'Lambda: {grid_lo} <= enclosed value <= {grid_hi}; required ({lam}, {F(10585, 10**14)})')
print(f'Cap: {cap}; required < {U}')
print(f'Full signed endpoint: {endpoint}; required < {threshold}; certified < {2*10**12}')
print(f'Row1 requires >= {threshold} > {4*10**17}')
print(f'Certificate: {out.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)
