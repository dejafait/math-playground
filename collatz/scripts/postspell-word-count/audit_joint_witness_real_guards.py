#!/usr/bin/env python3
"""Independent exact audit of L062; do not import or run its generator."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
source = HERE / 'joint-witness-real-guard-certificate.json'
raw = source.read_bytes()
saved = json.loads(raw)
records = []


def encode(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [encode(v) for v in x]
    return x


def check(name, actual, required, relation='='):
    passed = actual == required if relation == '=' else actual < required
    records.append(dict(name=name, actual=encode(actual), required=encode(required),
                        relation=relation, passed=passed))


table_text = (ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
table = [tuple(map(int, m)) for m in re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', table_text, re.M)]
check('literal indices', [r[0] for r in table], list(range(25)))
literal = {i: (j, h, 2 if i != 24 else 166504412) for i, j, h in table}
order = [8, 1, 2, 3, 4, 5, 6, 12, 0, 9, 10, 11, 7, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
for lemma in ['L060-two-transposition-joint-prime-nonvanishing-stop.md',
              'L062-joint-witness-minimum-real-guard-failure.md']:
    text = (ROOT / 'lemmas' / lemma).read_text()
    written_order = list(map(int, re.search(r'```text\n([\d ]+)\n```', text)[1].split()))
    check(lemma + ' written chronology', written_order, order)
check('saved order', saved['order'], order)
check('intact permutation', sorted(order), list(range(25)))
check('saved row count', len(saved['rows']), 25)
check('saved prefix count', len(saved['prefixes']), 25)
pk = pn = even = 0
rows = []
prefixes = []
for position, index in enumerate(order):
    j, h, a = literal[index]
    row = dict(position=position, index=index, J=j, H=h, a=a)
    prefix = dict(position=position, index=index, three_exponent=pk, two_exponent=pn)
    rows.append(row)
    prefixes.append(prefix)
    check(f'row {position}', saved['rows'][position], row)
    check(f'prefix {position}', saved['prefixes'][position], prefix)
    check(f'parameters {position}', j >= 2 and h >= 3 and a >= 0 and a % 18 == 2, True)
    pk += 3*j+h
    pn += 4*j+h+a
    even += j+a
K, N, L = pk, pn, even
check('totals', [K, N, L], [397573379, 630138897, 232565518])
check('saved counts', saved['counts'], dict(K=K, L=L, N=N, d=1, K0=K, L0=L))
integer_checks = dict(
    fixed_order=saved['order'] == order,
    intact_permutation=sorted(order) == list(range(25)),
    large_tail_fixed=rows[-1]['index'] == 24 and rows[-1]['a'] == 166504412,
    first_24_tails_two=all(r['a'] == 2 for r in rows[:24]),
    parameter_hypotheses=all(r['J'] >= 2 and r['H'] >= 3 and r['a'] >= 0 and r['a'] % 18 == 2 for r in rows),
    odd_count=K == 397573379, even_count=L == 232565518, length=K+L == N,
    primitive_scaling_d1=K > 225640000 and L > 0,
    all_J_ge_8_H_ge_40=all(r['J'] >= 8 and r['H'] >= 40 for r in rows),
    first_J1230_H5849=literal[order[0]][:2] == (1230, 5849),
    complete_product_exponents=(pk, pn) == (397573379, 630138897))
check('integer check names', sorted(saved['integer_checks']), sorted(integer_checks))
for name, value in integer_checks.items():
    check('recomputed ' + name, value, True)
    check('saved ' + name, saved['integer_checks'][name], value)

# Direct atanh series for log 2 and log 3, without binary reduction or
# rounded terms. Integral remainder <= 2*x^(2m+1)/((2m+1)*(1-x*x)).
def log_bounds(t, m=96):
    x = F(t-1, t+1)
    terms = [2*x**(2*j+1)/(2*j+1) for j in range(m)]
    low = sum(terms, F(0))
    rem = 2*x**(2*m+1)/((2*m+1)*(1-x*x))
    return dict(argument=t, x=x, terms=terms, remainder_upper=rem,
                lower=low, upper=low+rem)


logs = [log_bounds(2), log_bounds(3)]
lambda_interval = (N*logs[0]['lower']-K*logs[1]['upper'],
                   N*logs[0]['upper']-K*logs[1]['lower'])
lo, hi = F(10584, 10**14), F(10585, 10**14)
check('independent Lambda lower', lo, lambda_interval[0], '<')
check('independent Lambda upper', lambda_interval[1], hi, '<')
check('saved Lambda lower', F(saved['lambda_input']['lower']), lo)
check('saved Lambda upper', F(saved['lambda_input']['upper']), hi)

baseline_c = F(27, 16)**8 * F(3, 2)**40 / 4
baseline_eta = F(23, 11) - (F(16, 27)**8)*(F(12, 11)+F(2, 3)**40)
minimum_c = F(19683, 8192)
B_upper = F(23, 11)*(1+F(1, 50000000))
n_lower = 2/hi-2
s_upper = B_upper/lo+F(23, 11)
check('written baseline eta', baseline_eta,
      F(7122556955297586891012225981605, 3433683820292512484657849089281))
check('written baseline c', baseline_c, F(3**64, 2**74))
for key, expected in [('B_lower', F(2)), ('B_upper', B_upper),
                      ('n0_lower', n_lower), ('s0_upper', s_upper)]:
    check('saved bound ' + key, F(saved['bounds'][key]), expected)
check('written n lower', n_lower, F(39999999995766, 2117))
check('written s upper', s_upper, F(95833335260143, 4851))
check('saved minimum position', saved['bounds']['minimum_position'], 0)
check('saved minimum row', saved['bounds']['minimum_original_index'], 8)

# Recurrence evaluation, independently of the generator's factorial form.
exp_terms = [F(1)]
for k in range(1, 41):
    exp_terms.append(exp_terms[-1]*24/k)
check('exponential term count', len(saved['exp24_terms']), 41)
for k, term in enumerate(exp_terms):
    check(f'exp24 term {k}', F(saved['exp24_terms'][k]), term)
exp_sum = sum(exp_terms)
check('written exponential sum', exp_sum,
      F(202750314819830504045671593478515759301, 7661655986496068058455078125))
lhs, rhs = F(4*literal[order[0]][0]*2, 3), F(26)
expected_checks = [
    ('first multiplier baseline exceeds 1e8', F(10**8), baseline_c),
    ('first eta baseline exceeds two', F(2), baseline_eta),
    ('each first-24 multiplier exceeds two', F(2), minimum_c),
    ('imported Lambda interval positive', F(0), lo),
    ('imported Lambda interval ordered', lo, hi),
    ('imported Lambda upper below one', hi, F(1)),
    ('n0 above 18 billion', F(18*10**9), n_lower),
    ('s0 below 20 billion', s_upper, F(20*10**9)),
    ('minimum lower-junction guard', F(540, 11), F(18*10**9)),
    ('length inequality', F(N), F(8*K, 5)+F(1725, 1034)),
    ('exp24 finite lower sum above 20 billion', F(20*10**9), exp_sum),
    ('exp2 finite lower sum above 11/4', F(11, 4), F(5)),
    ('log2 positive-series lower bound above 2/3', F(2, 3), F(56, 81)),
    ('violated J guard: RHS upper below LHS lower', rhs, lhs)]
check('original comparison names', [r['name'] for r in saved['checks']],
      [r[0] for r in expected_checks])
for old, (name, a, b) in zip(saved['checks'], expected_checks):
    check('independent ' + name, a, b, '<')
    check('original operands and margin: ' + name,
          [F(old['actual']), F(old['required']), F(old['margin'])], [a, b, b-a])
    check('original relation/flag: ' + name, [old['relation'], old['passed']], ['<', a < b])
for key, value in [('position', 0), ('original_index', 8), ('J', 1230)]:
    check('failed guard ' + key, saved['guard_failure'][key], value)
for key, value in [('lhs_strict_lower', lhs), ('rhs_strict_upper', rhs), ('separation', lhs-rhs)]:
    check('failed guard ' + key, F(saved['guard_failure'][key]), value)
check('original failures', saved['failures'], [])

failures = [r['name'] for r in records if not r['passed']]
result = dict(scope='Only L062 fixed order and its cyclic relabelings',
              source_sha256=hashlib.sha256(raw).hexdigest(),
              rows=rows, prefixes=prefixes, counts=dict(K=K, L=L, N=N),
              log_evidence=logs, independent_lambda_interval=lambda_interval,
              original_comparisons=[dict(name=n, actual=a, required=b, margin=b-a)
                                    for n, a, b in expected_checks],
              root_bounds=dict(B_upper=B_upper, n0_lower=n_lower, s0_upper=s_upper),
              guard=dict(lhs_strict_lower=lhs, rhs_strict_upper=rhs, separation=lhs-rhs),
              checks=records, check_count=len(records), failures=failures,
              qualifications='Symbolic positivity, closure, uniqueness, minimum and rotation arguments are in L062; no integer realization or other-order test.')
target = HERE / 'joint-witness-real-guard-audit-certificate.json'
target.write_text(json.dumps(encode(result), indent=2)+'\n')
print(f'Audit checks: {len(records)}; failures: {failures}')
print(f'Root bounds: n0>{n_lower}>18000000000; s0<{s_upper}<20000000000')
print(f'Required guard LHS<=RHS fails: LHS>{lhs}, RHS<{rhs}; separation>{lhs-rhs}')
print('Independent Lambda enclosure is strictly inside (10584/10^14,10585/10^14).')
print(f'Certificate: {target}')
assert not failures
