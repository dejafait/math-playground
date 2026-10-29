#!/usr/bin/env python3
"""Independent finite audit for L107; symbolic proof remains in the lemma.

Read the entire construction certificate, independently transcribe the
literal table, walk all cyclic prefixes and compare every saved operand.
No allocation sampling, floating-point arithmetic or expanded large powers.
The already audited L104 enclosure is imported only after matching K,N.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import operator
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TABLE = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
ENCLOSURE = ROOT / 'lemmas/L104-d35-fixed-row0-unit-exclusion.md'
SOURCE = HERE / 'd35-positive-row0-max-term-certificate.json'
OUT = HERE / 'd35-positive-row0-max-term-audit-certificate.json'
source = json.loads(SOURCE.read_text())
checks = []


def equal(name, actual, required):
    checks.append(dict(name=name, actual=actual, required=required,
                       relation='=', passed=actual == required))


def compare(name, actual, relation, required):
    actual, required = F(actual), F(required)
    operations = {'=': operator.eq, '<': operator.lt, '>': operator.gt,
                  '>=': operator.ge}
    passed = operations[relation](actual, required)
    checks.append(dict(name=name, actual=actual, required=required,
                       relation=relation, difference=actual-required,
                       passed=passed))
    return passed


literal = [
    (8, 40), (15, 72), (28, 134), (52, 249), (98, 467),
    (184, 877), (347, 1650), (653, 3106), (1230, 5849),
    (2317, 11018), (4365, 20756), (8224, 39104),
    (15494, 73672), (29191, 138802), (54998, 261511),
    (103621, 492705), (195229, 928293), (367827, 1748976),
    (693015, 3295208), (1305695, 6208431), (2460032, 11697176),
    (4634896, 22038409), (8732512, 41522114),
    (16452748, 78230965), (30998279, 32670621),
]
parsed = [tuple(map(int, m)) for m in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', TABLE.read_text(), re.M)]
equal('literal table independent transcription', parsed,
      [(i, j, h) for i, (j, h) in enumerate(literal)])
rows = [(j, h-35 if i == 0 else h+35 if i == 24 else h)
        for i, (j, h) in enumerate(literal)]
B, kap = 9250245, F(23, 11)
p = [3*j+h for j, h in rows]
q = [4*j+h+2 for j, h in rows]
K, Nbase = sum(p), sum(q)
N = Nbase+18*B
equal('sum J', sum(j for j, h in rows), 66061058)
equal('sum H', sum(h for j, h in rows), 199390205)
equal('L104 K operand', K, 397573379)
equal('L104 N operand', N, 630138897)
equal('saved total exponents', source['total_exponents'],
      dict(K=K, N_base=Nbase, N=N))
equal('saved domain', source['domain'], dict(B=B, budget_variables=25,
      b0_lower=1, other_budget_lower=0, tails='2+18*b_i'))
expected_rows = [dict(i=i, J=j, H=h, p=p[i], q_base=q[i],
    q_budget_coefficient=18,
    eta=f'23/11-(16/27)^{j}*(12/11+(2/3)^{h})')
    for i, (j, h) in enumerate(rows)]
equal('all construction rows and offsets', source['rows'], expected_rows)
for i, (j, h) in enumerate(rows):
    compare(f'row{i} eta exponent premise', j, '>=', 8)
    compare(f'row{i} H positivity', h, '>', 0)
    if i > 0:
        compare(f'row{i} own J guard exponent', j, '>=', 15)
compare('eta factor strictly below one half', F(16, 27)**8, '<', F(1, 2))
compare('eta lower strictly exceeds one', kap/2, '>', 1)
compare('all guard shifts positive', F(4*2**32-23, 11), '>', 0)
c0_cap = F(3**p[0], 2**(q[0]+18))
compare('row0 excluded as cumulative-product minimum', c0_cap, '<', 1)

lm, lp = F(10584, 10**14), F(10585, 10**14)
equal('saved lower Lambda', F(source['imported_enclosure']['Lambda_lower']), lm)
equal('saved upper Lambda', F(source['imported_enclosure']['Lambda_upper']), lp)
compare('coarse D lower is valid', lm, '>', F(1, 10**10))
compare('exp upper comparison domain', lp, '<', 1)
delta, pinv = lp/(1-lp), 1/(1-lp)
compare('D upper less than one hundredth', delta, '<', F(1, 100))
compare('inverse P upper less than two', pinv, '<', 2)
compare('endpoint lower domains', 1/delta+kap, '>', F(540, 11))
g15 = F(4*2**60, 11)
max_cap, required = kap*pinv, lm*(g15-kap)/25
coarse_cap, coarse_required = 2*kap, F(1, 10**10)*(g15-kap)/25
bounds = dict(D_lower=lm, D_upper=delta, inverse_P_upper=pinv,
    eta_upper=kap, eta_lower=kap/2, g_nonzero_row_lower=g15,
    max_term_strict_upper=max_cap, necessary_max_term_strict_lower=required,
    exact_positive_margin=required-max_cap,
    coarse_max_term_strict_upper=coarse_cap,
    coarse_necessary_max_term_strict_lower=coarse_required,
    coarse_positive_margin=coarse_required-coarse_cap,
    all_s_strict_lower=1/delta+kap)
equal('complete decisive-bound field set', sorted(source['decisive_bounds']), sorted(bounds))
for name, expected in bounds.items():
    equal(f'decisive bound {name}', F(source['decisive_bounds'][name]), expected)
compare('sharp threshold exceeds cap', required, '>', max_cap)
compare('coarse threshold exceeds cap', coarse_required, '>', coarse_cap)
compare('weakest necessary maximum exceeds one million', coarse_required, '>', 10**6)
equal('displayed coarse threshold', coarse_required, F(2**62-23, 275*10**10))
equal('displayed coarse gap', coarse_required-coarse_cap,
      F(4611674518427387881, 2750000000000))

# Incrementally traverse the actual cycle. Each prefix has not yet
# traversed its input row; advance only after storing/comparing that term.
cuts, minimum_cases = [], []
equal('construction cut count', len(source['cuts']), 25)
for i in range(25):
    Pexp = Qexp = wraps = 0
    coeff, visited, terms = [0]*25, [], []
    j = i
    for k in range(25):
        record = dict(k=k, input_row=j, prefix_rows=visited.copy(), p=Pexp,
            q_base=Qexp, q_budget_coefficients=coeff.copy(), wrap=wraps,
            reciprocal_identity='C_i/(C_j*P^wrap)',
            log_term='log(eta_j)+(q_base+dot(q_budget_coefficients,b))*log2-p*log3')
        equal(f'cut{i} term{k} complete saved operands', source['cuts'][i]['terms'][k], record)
        # Independently compare the walked product to C_j*P^wrap/C_i,
        # including every symbolic budget coefficient.
        expected = (sum(p[:j])+wraps*K-sum(p[:i]),
                    sum(q[:j])+wraps*Nbase-sum(q[:i]),
                    [18*(int(h < j)+wraps-int(h < i)) for h in range(25)])
        equal(f'cut{i} term{k} product identity', (Pexp, Qexp, coeff.copy()), expected)
        equal(f'cut{i} term{k} distinct rows', len(set(visited)), k)
        terms.append(record)
        visited.append(j)
        Pexp += p[j]
        Qexp += q[j]
        coeff[j] += 18
        j += 1
        if j == 25:
            j = 0
            wraps += 1
    equal(f'cut{i} complete traversal', (j, Pexp, Qexp, coeff, wraps),
          (i, K, Nbase, [18]*25, 1))
    cut = dict(i=i, terms=terms, guard_exponent=4*rows[i][0],
        guard='g_i=(4/11)*2^guard_exponent',
        necessary_threshold='R_i=D*(g_i-23/11)/25',
        relaxation='max_k exp(log_term[i,k]) >= R_i')
    equal(f'cut{i} complete saved cut', source['cuts'][i], cut)
    cuts.append(cut)
    if i:
        expected_case = dict(r=i, J=rows[i][0], term_count=25,
            cases=[dict(k=t['k'], j=t['input_row'], wrap=t['wrap'],
                reciprocal_cap='1/P' if t['wrap'] else '1',
                term_strict_upper=str(max_cap)) for t in terms],
            necessary_strict_lower=str(required),
            contradiction_margin=str(required-max_cap))
        equal(f'possible minimum{i} complete saved case',
              source['minimum_argument']['cases'][i-1], expected_case)
        minimum_cases.append(expected_case)
equal('minimum case count', len(source['minimum_argument']['cases']), 24)
equal('saved c0 cap', F(source['minimum_argument']['c0_strict_upper_one']), c0_cap)

# Re-evaluate every saved finite comparison, its exact difference, and
# success flag. These checks supplement independent operands above.
original_count = len(source['checks'])
equal('construction finite-check count', original_count, 2699)
original_failures = []
for n, old in enumerate(source['checks']):
    actual, expected = F(old['actual']), F(old['required'])
    passed = compare(f'construction check{n}: {old["name"]}', actual, old['relation'], expected)
    equal(f'construction check{n} difference', F(old['difference']), actual-expected)
    equal(f'construction check{n} flag', old['passed'], passed)
    if not passed:
        original_failures.append(old['name'])
equal('construction failure list', source['summary']['failures'], original_failures)
equal('complete construction summary', source['summary'], dict(
    verdict='RELAXATION_INFEASIBLE', checks=2699, failures=[],
    numerator_terms_checked=625, possible_minimum_indices=24,
    minimum_case_terms=600, allocation_samples=0,
    floating_point_operations=0, independent_audit=False))
provenance = [dict(path=str(path.relative_to(ROOT)),
    sha256=hashlib.sha256(path.read_bytes()).hexdigest()) for path in (TABLE, ENCLOSURE)]
equal('construction input provenance', source['input_provenance'], provenance)
provenance.append(dict(path=str(SOURCE.relative_to(ROOT)),
    sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest()))
failures = [c['name'] for c in checks if not c['passed']]
result = dict(scope='L107 critical audit, literal d35 positive-row0 integer simplex only',
    input_provenance=provenance, rows=expected_rows,
    total_exponents=dict(K=K, N_base=Nbase, N=N),
    enclosure_import=dict(Lambda_lower=lm, Lambda_upper=lp,
        qualification='L104 audited proof reused after exact K,N matching; not recertified'),
    cuts=cuts, minimum_cases=minimum_cases, decisive_bounds=bounds,
    checks=checks, summary=dict(verdict='AUDIT_PASSED' if not failures else 'AUDIT_FAILED',
        checks=len(checks), failures=failures, original_checks_recomputed=original_count,
        symbolic_prefixes=625, minimum_case_terms=600, allocation_samples=0,
        floating_point_operations=0),
    limitations='Finite operands are audited here; universal common-tuple, minimum and necessary-guard logic are audited in L107. No assembly, actual-word transfer or Collatz resolution.')
OUT.write_text(json.dumps(result, default=str, indent=2)+'\n')
print(f'{result["summary"]["verdict"]}: checks={len(checks)}, failures={failures}')
print(f'K={K}; N={N}; complete prefixes=625; minimum-case terms=600; original checks={original_count}')
print(f'Actual M cap < {coarse_cap}; required M > {coarse_required}; positive gap > {coarse_required-coarse_cap}')
print(f'Certificate: {OUT.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)
