#!/usr/bin/env python3
"""Finite L077 benchmark tests; the quantified proof is in the lemma.

Reuse audited L055/L064/L068 analytic enclosures, rather than claim to
recertify their cancellation-sensitive logarithms. No new table is searched.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE.parent.parent
TABLE_PATH = NOTEBOOK / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
text = TABLE_PATH.read_text()
table = [tuple(map(int, row)) for row in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', text, re.M)]
if len(table) != 25 or [i for i, _, _ in table] != list(range(25)):
    raise ValueError('Canonical L055 table must contain exactly the indexed 25 rows')

checks = []

def check(name, actual, relation, required):
    actual, required = Q(actual), Q(required)
    ok = {'<': actual < required, '<=': actual <= required,
          '=': actual == required, '>': actual > required,
          '>=': actual >= required}[relation]
    checks.append(dict(name=name, actual=str(actual), relation=relation,
                       required=str(required), actual_minus_required=str(actual-required),
                       passed=ok))

r, p, q, budget, cutoff = 25, 23, 24, 9250245, 2
kappa = Q(23, 11)
lam_lo, lam_hi = Q(10584, 10**14), Q(10585, 10**14)
e = Q(2)
eta0 = kappa-Q(12, 11)*Q(16, 27)**8-Q(16, 27)**8*Q(2, 3)**40
check('positive imported Lambda lower', lam_lo, '>', 0)
check('ordered imported Lambda bounds', lam_lo, '<', lam_hi)
check('Lambda upper below one', lam_hi, '<', 1)
check('eta0 lower e (all eta >= eta0 by table comparison)', eta0, '>', e)
check('unchanged tail2 multiplier lower bound above two', Q(3**9, 2**13), '>', 2)
check('boundary row0 multiplier above 1e8', Q(3**64, 2**74), '>', 10**8)
check('boundary other prefix rows baseline above two', Q(3**117, 2**170), '>', 2)
domain_lower = e*(1-lam_hi)/lam_hi
check('criterion all-input unshifted lower bound', domain_lower, '>=', 47)
check('imported stronger benchmark lower bound', domain_lower, '>', 18*10**9)

L = [Q(1)] + [Q(10**8 * 2**(i-1)) for i in range(1, r)]
prefix_records = [dict(i=i, incoming_lower=str(value),
                       reciprocal=str(1/value)) for i, value in enumerate(L)]
reciprocal_sum = sum(1/value for value in L)
q_bound = kappa*(1+Q(2, 10**8))
normalized_required = q_bound/lam_lo+q_bound+kappa/L[q]
u_bound = q_bound/lam_lo+q_bound+kappa
check('Q bounds complete incoming inverse-prefix sum', kappa*reciprocal_sum, '<=', q_bound)
check('U bounds normalized shifted input', normalized_required, '<=', u_bound)
check('U matches L068 bound', u_bound, '=', Q(435606069410390910013, 22050000000))
check('U below 20 billion', u_bound, '<', 20*10**9)
exp_terms = [Q(24**j, factorial(j)) for j in range(41)]
exp_lower = sum(exp_terms)
check('exp24 positive finite sum above 20 billion', exp_lower, '>', 20*10**9)

rows = [dict(i=i, J=j, H=h,
             a=2+18*cutoff if i == p else
               (2+18*(budget-cutoff) if i == q else 2))
        for i, j, h in table]
K = sum(3*j+h for _, j, h in table)
N = sum(4*j+h for _, j, h in table)+2*r+18*budget
prefix_k = sum(3*row['J']+row['H'] for row in rows[:q])
prefix_d = sum(4*row['J']+row['H']+row['a'] for row in rows[:q])
S = 10**12
ell, upper_log3, upper_log_guard = (Q(value, S) for value in
                                   (693147180559, 1098612288669, 1011600911679))
margin = 24+prefix_k*upper_log3-(prefix_d+4*rows[q]['J'])*ell+upper_log_guard
check('criterion final-row boundary margin', margin, '<', 0)
check('same complete margin as L068', margin, '=', Q(-474883782659, 125000000000))
check('required benchmark margin below -3.79', margin, '<', Q(-379, 100))

integer_checks = dict(
    literal_increasing_J=all(table[i][1] < table[i+1][1] for i in range(q)),
    eta_monotonicity_hypotheses=all(j >= 8 and h >= 40 for _, j, h in table),
    boundary_row0_exact_pair=table[0] == (0, 8, 40),
    boundary_other_prefix_baseline=all(row['J'] >= 15 and row['H'] >= 72
                                      and row['a'] <= 38 for row in rows[1:q]),
    all_early_tails_two=all(row['a'] == 2 for row in rows[:p]),
    boundary_changed_tails=(rows[p]['a'], rows[q]['a']) == (38, 166504376),
    full_exponents=(K, N) == (397573379, 630138897),
    incoming_exponents=(prefix_k, prefix_d) == (271907921, 306970784),
    full_tail_sum=sum(row['a'] for row in rows) == 2*r+18*budget,
    last_parameter_final_tail_two=2+18*(budget-budget) == 2,
    cutoff_admitted=0 <= cutoff <= budget,
)
small_budgets = [dict(B=b, cutoff=2, rejected_interval_empty=2 > b,
                     boundary_tests_required=False,
                     qualification='Endpoint/domain assertion still requires test (3)')
                 for b in (0, 1)]
failures = [c['name'] for c in checks if not c['passed']]
failures += [name for name, passed in integer_checks.items() if not passed]
old_path = HERE/'uniform-last-pair-certificate.json'
old = json.loads(old_path.read_text())
# Preserve the old probe by reference and full record; it is not a required test.
old_probes = old['diagnostic_probes']
result = dict(
    target='L077 finite L068 benchmark: literal last-pair cutoff tau=2',
    imports=dict(
        Lambda='Audited L055 enclosure; not freshly recertified here',
        logarithms='Audited L064/L068 outward bounds; not freshly recertified here',
        affine='L051 coordinate; L068 mechanism; H-H (1997) Lemma 2',
        survivors='Audited L055 t=0 and L064 j=23 t=1, assembled in L068'),
    constants=dict(r=r, p=p, q=q, B=budget, tau=cutoff, e=str(e),
                   lambda_lower=str(lam_lo), lambda_upper=str(lam_hi),
                   Q=str(q_bound), U=str(u_bound), T=24,
                   ell=str(ell), upper_log3=str(upper_log3),
                   upper_log11over4=str(upper_log_guard)),
    eta0=str(eta0), domain_lower=str(domain_lower),
    prefixes=prefix_records, reciprocal_sum=str(reciprocal_sum),
    normalized_required=str(normalized_required),
    boundary=dict(rows=rows, incoming_k=prefix_k, incoming_d=prefix_d,
                  J_last=rows[q]['J'], negative_log2_coefficient=prefix_d+4*rows[q]['J'],
                  margin_upper=str(margin)),
    exp24_terms=[str(value) for value in exp_terms], exp24_partial_sum=str(exp_lower),
    checks=checks, integer_checks=integer_checks,
    symbolic_coverage=dict(first_rejected=cutoff, last_rejected=budget,
        number_rejected=budget-cutoff+1,
        reason='Positive-coefficient exact final-input formula decreases throughout closed interval',
        survivors='t=0,1 imported only; no arbitrary-table survivor verdict'),
    small_budgets=small_budgets, preserved_optional_probes=old_probes,
    preserved_original_certificate_sha256=hashlib.sha256(old_path.read_bytes()).hexdigest(),
    failures=failures,
    limitations='No new analytic enclosures, new table, integer/order/support assembly or actual-cycle result')
path = HERE/'variable-table-last-pair-certificate.json'
path.write_text(json.dumps(result, indent=2)+'\n')
print(f'Rational checks: {len(checks)}; integer checks: {len(integer_checks)}; failures: {failures}')
print(f'All unshifted inputs > {domain_lower}; required >=47')
print(f'Boundary margin < {margin}; required <0; benchmark <-3.79')
print(f'Symbolic rejection coverage: 2..{budget}, including final tail 2')
print('Old optional <-4 probe preserved as failed; analytic bounds imported, not recertified')
print(f'Certificate: {path}')
assert not failures
