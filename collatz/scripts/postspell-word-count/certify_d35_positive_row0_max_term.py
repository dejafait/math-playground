#!/usr/bin/env python3
"""Finite operands and symbolic prefix coverage for L107.

This is a construction certificate, not an independent proof audit. All
budget variables remain symbolic. The proof's finite-minimum argument
covers the whole simplex; no allocation or maximum branch is sampled.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TABLE = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
ENCLOSURE = ROOT / 'lemmas/L104-d35-fixed-row0-unit-exclusion.md'
OUT = HERE / 'd35-positive-row0-max-term-certificate.json'
checks = []


def check(name, actual, relation, required):
    a, b = F(actual), F(required)
    passed = {'=': a == b, '<': a < b, '>': a > b,
              '>=': a >= b}[relation]
    checks.append(dict(name=name, actual=a, relation=relation,
                       required=b, difference=a-b, passed=passed))


base = [tuple(map(int, row)) for row in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', TABLE.read_text(), re.M)]
assert [r[0] for r in base] == list(range(25)), 'Literal table index mismatch'
B, kap = 9250245, F(23, 11)
rows = []
for i, j, old_h in base:
    h = 5 if i == 0 else 32670656 if i == 24 else old_h
    rows.append(dict(i=i, J=j, H=h, p=3*j+h, q_base=4*j+h+2,
                     q_budget_coefficient=18,
                     eta=f'23/11-(16/27)^{j}*(12/11+(2/3)^{h})'))
    check(f'row{i} J>=8', j, '>=', 8)
    check(f'row{i} H>0', h, '>', 0)
    if i:
        check(f'possible minimum row{i} J>=15', j, '>=', 15)
check('H0 change', rows[0]['H']-base[0][2], '=', -35)
check('H24 change', rows[24]['H']-base[24][2], '=', 35)
check('sum J', sum(r['J'] for r in rows), '=', 66061058)
check('sum H', sum(r['H'] for r in rows), '=', 199390205)
K = sum(r['p'] for r in rows)
Nbase = sum(r['q_base'] for r in rows)
N = Nbase+18*B
check('K matches L104 enclosure', K, '=', 397573379)
check('N matches L104 enclosure for every allocation', N, '=', 630138897)
check('total tails', 50+18*B, '=', 166504460)
check('row0 p', rows[0]['p'], '=', 29)
check('row0 q base', rows[0]['q_base'], '=', 39)
c0_upper = F(3**29, 2**57)
check('row0 c upper for b0>=1', c0_upper, '<', 1)
check('eta subtraction factor', F(16, 27)**8, '<', F(1, 2))
check('eta lower exceeds1', kap/2, '>', 1)
check('smallest g minus shift positive', F(4*2**32-23, 11), '>', 0)

# These are imported audited bounds, after the exact totals match above.
# No floating-point logarithms or assumed numerical closure are used.
lm, lp = F(10584, 10**14), F(10585, 10**14)
delta = lp/(1-lp)
inverse_P_upper = 1/(1-lp)
check('Lambda lower exceeds coarse D lower', lm, '>', F(1, 10**10))
check('Lambda upper below1', lp, '<', 1)
check('D upper below1/100', delta, '<', F(1, 100))
check('inverse P upper below2', inverse_P_upper, '<', 2)
check('all endpoint lower domains', 1/delta+kap, '>', F(540, 11))

# C_i = 3^A_i / 2^(E_i + 18 sum_{h<i} b_h).
A, E = [0], [0]
for row in rows:
    A.append(A[-1]+row['p'])
    E.append(E[-1]+row['q_base'])
cuts = []
for i in range(25):
    terms = []
    for k in range(25):
        j = (i+k) % 25
        wrap = int(i+k >= 25)
        indices = [(i+h) % 25 for h in range(k)]
        p = sum(rows[h]['p'] for h in indices)
        q0 = sum(rows[h]['q_base'] for h in indices)
        coeff = [18*indices.count(h) for h in range(25)]
        expected_coeff = [18*(int(h < j)-int(h < i)+wrap)
                          for h in range(25)]
        check(f'cut{i} term{k} p identity', p, '=', A[j]-A[i]+wrap*K)
        check(f'cut{i} term{k} q base identity', q0, '=', E[j]-E[i]+wrap*Nbase)
        check(f'cut{i} term{k} budget identity discrepancies',
              sum(abs(a-b) for a, b in zip(coeff, expected_coeff)), '=', 0)
        check(f'cut{i} term{k} prefix cardinality', len(set(indices)), '=', k)
        terms.append(dict(k=k, input_row=j, prefix_rows=indices,
                          p=p, q_base=q0, q_budget_coefficients=coeff,
                          wrap=wrap,
                          reciprocal_identity='C_i/(C_j*P^wrap)',
                          log_term='log(eta_j)+(q_base+dot(q_budget_coefficients,b))*log2-p*log3'))
    check(f'cut{i} numerator term count', len(terms), '=', 25)
    full_rows = [(i+h) % 25 for h in range(25)]
    check(f'cut{i} full p', sum(rows[h]['p'] for h in full_rows), '=', K)
    check(f'cut{i} full q base', sum(rows[h]['q_base'] for h in full_rows), '=', Nbase)
    check(f'cut{i} complete budget coverage', len(set(full_rows)), '=', 25)
    cuts.append(dict(i=i, terms=terms,
                     guard_exponent=4*rows[i]['J'],
                     guard='g_i=(4/11)*2^guard_exponent',
                     necessary_threshold='R_i=D*(g_i-23/11)/25',
                     relaxation='max_k exp(log_term[i,k]) >= R_i'))

g15 = F(4*2**60, 11)
M_upper = kap*inverse_P_upper
R_lower = lm*(g15-kap)/25
M_coarse = 2*kap
R_coarse = F(1, 10**10)*(g15-kap)/25
check('minimum guard minus shift', g15-kap, '=', F(2**62-23, 11))
check('coarse necessary max lower', R_coarse, '=', F(2**62-23, 275*10**10))
check('coarse maximum cap', M_coarse, '=', F(46, 11))
check('certified max-term exclusion margin', R_lower, '>', M_upper)
check('coarse exclusion margin', R_coarse, '>', M_coarse)
check('coarse required maximum exceeds one million', R_coarse, '>', 10**6)
minimum_cases = []
for r in range(1, 25):
    # The conditional inequality C_r<=C_j is proved by selecting a
    # global minimum, not asserted numerically for unknown budgets.
    minimum_cases.append(dict(r=r, J=rows[r]['J'], term_count=25,
        cases=[dict(k=t['k'], j=t['input_row'], wrap=t['wrap'],
                    reciprocal_cap='1/P' if t['wrap'] else '1',
                    term_strict_upper=M_upper) for t in cuts[r]['terms']],
        necessary_strict_lower=R_lower, contradiction_margin=R_lower-M_upper))
check('possible minimum indices covered', len(minimum_cases), '=', 24)
failures = [c['name'] for c in checks if not c['passed']]
result = dict(
    scope='All integer b_i>=0, sum b_i=9250245, b0>=1; literal d35 order; J-only necessary relaxation',
    input_provenance=[dict(path=str(p.relative_to(ROOT)),
                           sha256=hashlib.sha256(p.read_bytes()).hexdigest())
                      for p in (TABLE, ENCLOSURE)],
    rows=rows,
    domain=dict(B=B, budget_variables=25, b0_lower=1,
                other_budget_lower=0, tails='2+18*b_i'),
    total_exponents=dict(K=K, N_base=Nbase, N=N),
    imported_enclosure=dict(Lambda_lower=lm, Lambda_upper=lp,
                            qualification='L104 audited enclosure, unchanged exact K,N'),
    exact_definitions=dict(P='3^K/2^N', D='P^-1-1',
                           C_i='product_{j<i} c_j',
                           n0='sum_{j=0}^24 eta_j/C_j / D',
                           n_i='C_i*(n0+sum_{j<i} eta_j/C_j)',
                           s_i='n_i+23/11'),
    cuts=cuts,
    minimum_argument=dict(selection='r minimizes C_0,...,C_24; ties allowed',
                          row0_excluded_by='C_1=c_0<C_0=1',
                          c0_strict_upper_one=c0_upper,
                          conditional_proof='C_r/C_j<=1; reciprocal prefix=C_r/(C_j*P^wrap)',
                          cases=minimum_cases),
    decisive_bounds=dict(D_lower=lm, D_upper=delta,
                         inverse_P_upper=inverse_P_upper,
                         eta_upper=kap, eta_lower=kap/2,
                         g_nonzero_row_lower=g15,
                         max_term_strict_upper=M_upper,
                         necessary_max_term_strict_lower=R_lower,
                         exact_positive_margin=R_lower-M_upper,
                         coarse_max_term_strict_upper=M_coarse,
                         coarse_necessary_max_term_strict_lower=R_coarse,
                         coarse_positive_margin=R_coarse-M_coarse,
                         all_s_strict_lower=1/delta+kap),
    checks=checks,
    summary=dict(verdict='RELAXATION_INFEASIBLE' if not failures else 'UNCERTIFIED',
                 checks=len(checks), failures=failures,
                 numerator_terms_checked=625, possible_minimum_indices=24,
                 minimum_case_terms=600, allocation_samples=0,
                 floating_point_operations=0, independent_audit=False),
    limitations='Symbolic affine/minimum proof is in L107. No actual-word transfer, arbitrary-order, entry, divergence, universal-descent or originality conclusion.')
OUT.write_text(json.dumps(result, default=str, indent=2)+'\n')
print(f'Verdict={result["summary"]["verdict"]}; checks={len(checks)}; failures={failures}')
print(f'K={K}; N={N}; symbolic prefixes=625; possible minima=24; allocation samples=0')
print(f'M_min < {M_coarse}; required M_min > {R_coarse}; gap > {R_coarse-M_coarse}')
print(f'c0 <= {c0_upper} < 1; denominator bounds imported after exact K,N match')
print(f'Certificate: {OUT.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)
