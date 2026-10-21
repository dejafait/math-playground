#!/usr/bin/env python3
"""Independent L086 audit: no construction code imported or executed.

All finite operands are reconstructed; the quantified proof is in L086.
The logarithm remainder is the previously assessed DLMF specialization.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
source = HERE / 'd5-remaining-early-recipients-certificate.json'
raw = source.read_bytes()
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
rows[0][2], rows[24][2] = 35, 32670626
checks = []


def verify(name, passed):
    checks.append(dict(name=name, passed=bool(passed)))


def rational_dict_equal(a, b):
    return set(a) == set(b) and all(F(a[k]) == F(b[k]) for k in b)


canonical_raw = (ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_bytes()
canonical = [list(map(int, t)) for t in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', canonical_raw.decode(), re.M)]
verify('all 25 independently transcribed canonical pairs',
       canonical == [[i, j, h] for i, (j, h) in enumerate(base)])
verify('complete changed construction table', old['rows'] == rows)
verify('table domains and increasing own J',
       all(j >= 2 and h >= 3 for _, j, h in rows)
       and all(rows[i+1][1] > rows[i][1] for i in range(24)))
prior_raw = (HERE / 'h-transfer-family-certificate.json').read_bytes()
prior = json.loads(prior_raw)['tables'][4]
verify('source provenance', old['source_sha256'] == sha256(canonical_raw).hexdigest()
       and old['prior_certificate_sha256'] == sha256(prior_raw).hexdigest())
verify('complete prior d5 table', prior['d'] == 5 and prior['rows'] == rows)

kappa, U, T = F(23, 11), F(20_000_000_000), F(24)
ell, u, v = map(lambda n: F(n, 10**12),
                (693147180559, 1098612288669, 1011600911679))
E, lam = F(24*23, 4*2**60-23), F(10584, 10**14)
R = kappa/(lam-E)+kappa
constants = dict(U=U, T=T, ell=ell, u=u, v=v, E=E, lambda_lower=lam, R=R)
verify('all construction constants', rational_dict_equal(old['constants'], constants))
prefix_floor = min(h for _, _, h in rows[:22])
recipient_floor = min(h for _, _, h in rows[1:23])
offsets = dict(prefix_H_floor=prefix_floor,
               prefix_tail2_upper=kappa-(F(12, 11)*F(3, 2)**prefix_floor+1)/4,
               recipient_H_floor=recipient_floor,
               recipient_Q_lower=F(12, 11)*F(3, 2)**recipient_floor+1,
               required_Q=kappa*2**20,
               failed_row0_Q=F(12, 11)*F(3, 2)**35+1)
verify('every offset operand', rational_dict_equal(old['offsets'], offsets))
verify('lower domain and uniform eta positivity bound',
       F(540, 11)-kappa == 47 and
       0 < kappa-F(12, 11)*F(16, 27)**2-F(16, 27)**2*F(2, 3)**3 < kappa)
terms = [F(1)]
for k in range(1, 41):
    terms.append(terms[-1]*T/k)
verify('all 41 exponential terms', list(map(F, old['exponential_terms'])) == terms)

prefixes = [dict(i=i, A=sum(3*j+h for _, j, h in rows[:i]),
                 D=sum(4*j+h+2 for _, j, h in rows[:i])) for i in range(26)]
verify('all 25 stored incoming prefixes', old['prefixes'] == prefixes[:25])
margins = []
for j in range(1, 23):
    p = prefixes[j+1]
    A, D, next_J = p['A'], p['D'], rows[j+1][1]
    M = (D+18+4*next_J)*ell-T-v-A*u
    margins.append(dict(j=j, next_input=j+1, A=A, D=D, next_J=next_J, margin=M))
verify('complete 22 margin records including own inputs', len(old['margins']) == 22
       and all(rational_dict_equal(a, b) for a, b in zip(old['margins'], margins)))
lemma_text = (ROOT / 'lemmas/L086-d5-literal-early-support-exclusion.md').read_text()
printed = [tuple(map(int, t)) for t in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|$', lemma_text, re.M)]
verify('entire canonical 22-row table', printed == [
    (m['j'], m['A'], m['D'], m['margin']*10**12) for m in margins])

# Reconstruct all original comparisons from independent direct prefix sums.
specs = []


def spec(name, a, relation, b):
    specs.append((name, F(a), relation, F(b)))


K = sum(3*j+h for _, j, h in rows)
N = sum(4*j+h+2 for _, j, h in rows)+18*9250245
spec('prior table d', prior['d'], '=', 5)
spec('K', K, '=', 397573379)
spec('N', N, '=', 630138897)
spec('minimum prefix H', prefix_floor, '=', 35)
spec('minimum recipient H', recipient_floor, '=', 72)
spec('all prefix tail2 offsets negative', offsets['prefix_tail2_upper'], '<', 0)
spec('all recipient tail20 offsets negative', offsets['recipient_Q_lower'], '>', offsets['required_Q'])
spec('failed row0 tail20 datum preserved', offsets['failed_row0_Q'], '<', offsets['required_Q'])
spec('U below exp24 lower sum', U, '<', sum(terms))
spec('L085 cap residual', lam-E, '>', 0)
spec('L085 cap below U', R, '<', U)
for i in range(25):
    p = prefixes[i]
    spec(f'incoming{i} A matches L084', p['A'], '=', prior['prefixes'][i]['A'])
    spec(f'incoming{i} D matches L084', p['D'], '=', prior['prefixes'][i]['D_tail2'])
    if 1 <= i <= 22:
        m, previous = margins[i-1], prior['S']['margins'][i]
        spec(f'recipient{i} A', m['A'], '=', previous['A'])
        spec(f'recipient{i} D', m['D'], '=', previous['D'])
        spec(f'recipient{i} margin matches L084', m['margin'], '=', previous['margin'])
        spec(f'recipient{i} strict rejection', m['margin'], '>', F(1134, 100))
        spec(f'recipient{i} changed A shift', m['A']-sum(3*j+h for j, h in base[:i+1]), '=', -5)
        spec(f'recipient{i} changed D shift', m['D']-sum(4*j+h+2 for j, h in base[:i+1]), '=', -5)
spec('complete A', prefixes[25]['A'], '=', 397573379)
spec('complete D plus budget', prefixes[25]['D']+18*9250245, '=', 630138897)
verify('exact coverage of all original comparisons', len(specs) == len(old['checks']) == 195
       and [s[0] for s in specs] == [c['name'] for c in old['checks']])
comparisons = []
for record, (name, a, relation, b) in zip(old['checks'], specs):
    cross = a.numerator*b.denominator-b.numerator*a.denominator
    passed = {'=': cross == 0, '<': cross < 0, '>': cross > 0}[relation]
    same = (set(record) == {'name', 'actual', 'relation', 'required', 'difference', 'passed'}
            and record['name'] == name and F(record['actual']) == a
            and record['relation'] == relation and F(record['required']) == b
            and F(record['difference']) == a-b and record['passed'] is passed)
    verify('complete original comparison: '+name, same and passed)
    comparisons.append(dict(name=name, actual=a, relation=relation, required=b,
                            difference=a-b, cross_product_difference=cross,
                            passed=passed, matches_original=same))


def log_interval(t):
    z = (t-1)/(t+1)
    assert 0 < z < 1
    power, summands = z, []
    for m in range(100):
        summands.append(2*power/(2*m+1))
        power *= z*z
    remainder = 2*power/(201*(1-z*z))
    lower = sum(summands)
    return dict(argument=t, z=z, terms=summands, remainder=remainder,
                lower=lower, upper=lower+remainder)


logs = {name: log_interval(t) for name, t in
        [('log2', F(2)), ('log3', F(3)), ('log11over4', F(11, 4))]}
l2, l3, lc = (logs[name] for name in ('log2', 'log3', 'log11over4'))
verify('all three strict outward analytic operands',
       ell < l2['lower'] < l2['upper'] and l3['upper'] < u and lc['upper'] < v)
lambda_lo = N*l2['lower']-K*l3['upper']
lambda_hi = N*l2['upper']-K*l3['lower']
verify('complete amplified Lambda enclosure', lam < lambda_lo < lambda_hi < F(10585, 10**14))
error_records = []
for m in margins:
    A, C, M = m['A'], m['D']+18+4*m['next_J'], m['margin']
    exact_lo = C*l2['lower']-24-lc['upper']-A*l3['upper']
    exact_hi = C*l2['upper']-24-lc['lower']-A*l3['lower']
    error_lo = C*(l2['lower']-ell)+A*(u-l3['upper'])+v-lc['upper']
    error_hi = C*(l2['upper']-ell)+A*(u-l3['lower'])+v-lc['lower']
    verify(f'all amplified margin errors at recipient {m["j"]}',
           A > 0 and C > 0 and M > F(1134, 100)
           and 0 < error_lo < error_hi and exact_lo == M+error_lo
           and exact_hi == M+error_hi)
    error_records.append(dict(j=m['j'], coefficient_log3=A, coefficient_log2=C,
                              M=M, exact_margin_lower=exact_lo, exact_margin_upper=exact_hi,
                              error_lower=error_lo, error_upper=error_hi))
minimum = min(m['margin'] for m in margins)
min_row = next(m['j'] for m in margins if m['margin'] == minimum)
verify('full original summary', old['summary'] == dict(
    checks=195, recipients=22, minimum_margin=str(minimum), minimum_row=min_row,
    required_margin=str(F(1134, 100)), failures=[], passed=True))
verify('all top-level construction fields accounted for', set(old) == {
    'scope', 'imports', 'source_sha256', 'prior_certificate_sha256', 'rows',
    'constants', 'offsets', 'exponential_terms', 'prefixes', 'margins',
    'checks', 'summary', 'limitations'})
verify('construction unchanged', source.read_bytes() == raw)
failures = [c['name'] for c in checks if not c['passed']]
scale = 10**12
max_error_upper = F((max(e['error_upper'] for e in error_records)*scale).__ceil__(), scale)
result = dict(construction_sha256=sha256(raw).hexdigest(),
              original_scope=old['scope'], original_imports=old['imports'],
              original_limitations=old['limitations'], rows=rows, constants=constants,
              offsets=offsets, exponential_terms=terms, prefixes=prefixes,
              margins=margins, comparisons=comparisons, logs=logs,
              lambda_interval=dict(lower=lambda_lo, upper=lambda_hi,
                                   required_lower=lam, required_upper=F(10585, 10**14)),
              analytic_margin_errors=error_records, audit_checks=checks,
              summary=dict(checks=len(checks), original_comparisons=len(comparisons),
                           recipients=len(margins), minimum_margin=minimum,
                           minimum_row=min_row, required_margin=F(1134, 100),
                           maximum_error_upper_grid=max_error_upper,
                           failures=failures, passed=not failures))
out = HERE / 'd5-early-support-audit-certificate.json'
out.write_text(json.dumps(result, indent=2, default=str)+'\n')
print(f'Independent checks: {len(checks)}; original comparisons: {len(comparisons)}/195; failures: {failures}')
print(f'Recipients: {len(margins)}/22; minimum M_{min_row}={minimum}; required >1134/100')
print(f'All positive amplified margin errors <{max_error_upper}; direction preserves rejection')
print(f'Cap={R}; required <{U}; exponential lower sum >{U}: {sum(terms)>U}')
print(f'Certificate: {out.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)
