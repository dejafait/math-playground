#!/usr/bin/env python3
"""Independent exact arithmetic audit of L072; no construction code imported."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = HERE / 'earlier-recipient-certificate.json'
original_bytes = SOURCE.read_bytes()
old = json.loads(original_bytes)
# Independent transcription from the canonical L055 table.
J = [8, 15, 28, 52, 98, 184, 347, 653, 1230, 2317, 4365, 8224,
     15494, 29191, 54998, 103621, 195229, 367827, 693015, 1305695,
     2460032, 4634896, 8732512, 16452748, 30998279]
H = [40, 72, 134, 249, 467, 877, 1650, 3106, 5849, 11018, 20756,
     39104, 73672, 138802, 261511, 492705, 928293, 1748976, 3295208,
     6208431, 11697176, 22038409, 41522114, 78230965, 32670621]
S, ell, u, v = 10**12, 693147180559, 1098612288669, 1011600911679
lm, lp = F(10584, 10**14), F(10585, 10**14)
checks = []


def equal(name, actual, required):
    checks.append(dict(name=name, actual=actual, required=required,
                       passed=actual == required))


def lt(name, actual, required):
    actual, required = F(actual), F(required)
    checks.append(dict(name=name, actual=str(actual), required=str(required),
                       margin=str(required-actual), passed=actual < required))


canonical = (ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
parsed = [tuple(map(int, row)) for row in re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', canonical, re.M)]
table = [dict(i=i, J=J[i], H=H[i]) for i in range(25)]
equal('independent table vs L055', list(zip(range(25), J, H)), parsed)
equal('complete construction table', old['table'], table)
equal('J sum', sum(J), 66061058)
equal('H sum', sum(H), 199390205)
K = 3*sum(J)+sum(H)
N = 4*sum(J)+sum(H)+166504460
equal('total exponents', [K, N], [397573379, 630138897])
equal('strict J increase', all(a < b for a, b in zip(J, J[1:])), True)

# The assessed integrated geometric remainder, with unrounded rational terms.
logs = {}
for name, z in [('2', F(2)), ('3', F(3)), ('11/4', F(11, 4))]:
    x = (z-1)/(z+1)
    terms = [2*x**(2*k+1)/(2*k+1) for k in range(160)]
    lower = sum(terms)
    remainder = 2*x**321/(321*(1-x*x))
    logs[name] = dict(argument=str(z), x=str(x), terms=list(map(str, terms)),
                      lower=str(lower), remainder=str(remainder), upper=str(lower+remainder))
    lt('positive logarithm-series operand '+name, 0, x)
    equal('logarithm-series operand <=1/2 '+name, x <= F(1, 2), True)
lt('log2 grid lower', F(ell, S), F(logs['2']['lower']))
lt('log3 grid upper', F(logs['3']['upper']), F(u, S))
lt('log11/4 grid upper', F(logs['11/4']['upper']), F(v, S))
lambda_low = N*F(logs['2']['lower'])-K*F(logs['3']['upper'])
lambda_high = N*F(logs['2']['upper'])-K*F(logs['3']['lower'])
lt('Lambda strict lower', lm, lambda_low)
lt('Lambda strict upper', lambda_high, lp)
grid = 10**24
lambda_display = [str(F(lambda_low.numerator*grid//lambda_low.denominator, grid)),
                  str(F(lambda_high.numerator*grid//lambda_high.denominator+1, grid))]

minimum = F(575, 11)/lm+F(23, 11)
offset = F(12, 11)*F(3, 2)**40/2**20
bmax = F(23, 11)*(1+F(2**19, 10**8))
normalized = bmax/lm+bmax+F(23, 11)
exp_terms = {z: [F(z**k, factorial(k)) for k in range(41)] for z in [24, 27]}
expected_bounds = dict(minimum_shifted_upper=str(minimum),
                       prefix_offset_subtraction_lower=str(offset),
                       B_upper=str(bmax), normalized_shifted_upper=str(normalized))
equal('all construction exact bounds', old['exact_bounds'], expected_bounds)
equal('written minimum fraction', str(minimum), '7187500000030429/14553')
equal('written offset fraction', str(offset), '36472996377170786403/3170534137668829184')
equal('written B fraction', str(bmax), '9031479/4296875')
equal('written normalized fraction', str(normalized), '37631162507944991614/1894921875')

# Reconstruct each stored rational check with independently formed operands.
rational_expected = []


def rational(name, a, b):
    a, b = F(a), F(b)
    rational_expected.append(dict(name=name, actual=str(a), required=str(b),
                                  margin=str(b-a), passed=a < b))
    lt(name, a, b)


rational('minimum shifted upper below threshold', minimum, 500_000_000_000)
rational('exp27 finite positive sum above threshold', 500_000_000_000, sum(exp_terms[27]))
rational('negative shifted prefix offset', F(23, 11), offset)
rational('worst row0 multiplier exceeds weakened baseline', F(10**8, 2**18), F(3**64, 2**92))
rational('weakened row0 baseline exceeds two', 2, F(10**8, 2**18))
rational('rows1..23 tail20 baseline exceeds two', 2, F(3**117, 2**152))
rational('uniform normalized shifted upper below 20 billion', normalized, 20*10**9)
rational('exp24 finite positive sum above 20 billion', 20*10**9, sum(exp_terms[24]))
rational('log11over4 below two via exp2', F(11, 4), 5)
for z in [24, 27]:
    equal(f'all exp{z} terms', old[f'exp{z}_terms'], list(map(str, exp_terms[z])))
    equal(f'exp{z} sum', old[f'exp{z}_sum'], str(sum(exp_terms[z])))

supports = []
all_pairs = []
for j in range(22):
    # Direct prefix sums, not the construction program's incremental recurrence.
    ref_tail = [2]*25
    ref_tail[j], ref_tail[24] = 20, 166504394
    tail_coeff = [0]*25
    tail_coeff[23], tail_coeff[24] = 18, -18
    prefixes = [dict(i=k, three_exponent=sum(3*J[i]+H[i] for i in range(k)),
                     two_exponent_at_t0=sum(4*J[i]+H[i]+ref_tail[i] for i in range(k)),
                     two_exponent_t_coefficient=sum(tail_coeff[:k])) for k in range(26)]
    boundary = []
    for t in [1, 9250244]:
        tails = [ref_tail[i]+t*tail_coeff[i] for i in range(25)]
        boundary.append(dict(t=t, tails=tails, tail_sum=sum(tails),
                             bounds_and_congruences=all(a >= 2 and (a-2) % 18 == 0 for a in tails)))
    pairs = []
    for k in range(24):
        A = prefixes[k]['three_exponent']
        D = prefixes[k]['two_exponent_at_t0']
        old_D = sum(4*J[i]+H[i]+2 for i in range(k))+(18 if k == 23 else 0)
        delta = D-old_D
        for r in range(k+1, 25):
            lhs, rhs = 4*J[r]*ell, 29*S+A*u-D*ell
            record = dict(recipient=j, position=k, displaced_row=r, A=A, D=D,
                          row22_support_D=old_D, D_difference=delta,
                          difference_formula=18*((j < k)-(22 < k)),
                          lhs_lower_scaled=lhs, rhs_upper_scaled=rhs, margin_scaled=lhs-rhs,
                          passed=lhs > rhs and delta >= 0 and delta == 18*((j < k)-(22 < k)))
            pairs.append(record)
    all_pairs.extend(pairs)
    p = sum(3*J[i]+H[i] for i in range(24))
    t1 = boundary[0]['tails']
    q = sum(4*J[i]+H[i]+t1[i] for i in range(24))
    guard_q = q+4*J[24]
    operands = [24*S, p*u, -guard_q*ell, v]
    guard_upper = F(sum(operands), S)
    guard = dict(p=p, q=q, combined_two_exponent=guard_q,
                 operands=operands, upper=str(guard_upper), required='>=0')
    rational(f'recipient {j} boundary row24 upper below -3.79', guard_upper, F(-379, 100))
    properties = dict(
        boundaries_valid=all(b['tail_sum'] == 166504460 and b['bounds_and_congruences'] for b in boundary),
        first24_boundary_tails_at_most20=all(a <= 20 for a in t1[:24]),
        fixed_prefix_offsets=all(H[i] >= 40 and ref_tail[i] <= 20 for i in range(23)),
        row0_baseline=J[0] == 8 and H[0] == 40 and t1[0] <= 20,
        other_boundary_growth=all(J[i] >= 15 and H[i] >= 72 and t1[i] <= 20 for i in range(1, 24)),
        prefix_t_coefficients=[p['two_exponent_t_coefficient'] for p in prefixes] == [0]*24+[18, 0],
        closing_exponents=(prefixes[25]['three_exponent'], prefixes[25]['two_exponent_at_t0'],
                           prefixes[25]['two_exponent_t_coefficient']) == (397573379, 630138897, 0),
        boundary_guard_exponents=(p, q, guard_q) == (271907921, 306970784, 430963900),
        complete_first_displacement_pairs=len(pairs) == 300,
        all_prefix_improvements=all(pair['passed'] for pair in pairs))
    support = dict(recipient=j, boundaries=boundary, reference_prefixes=prefixes,
                   pairs=pairs, table_checks=properties, boundary_guard=guard)
    supports.append(support)
    equal(f'recipient {j}: complete original arithmetic records', old['supports'][j], support)
    equal(f'recipient {j}: all ten independently evaluated properties', all(properties.values()), True)

global_checks = dict(increasing_J=all(J[i] < J[i+1] for i in range(24)),
                     J_H_bounds=all(J[i] >= 8 and H[i] >= 40 for i in range(25)),
                     sum_J=sum(J) == 66061058, sum_H=sum(H) == 199390205,
                     complete_supports=[s['recipient'] for s in supports] == list(range(22)),
                     complete_pair_count=len(all_pairs) == 6600)
equal('all construction rational comparisons', old['checks'], rational_expected)
equal('complete construction global checks', old['global_checks'], global_checks)
equal('independently evaluated global checks', all(global_checks.values()), True)
equal('complete supports count', len(old['supports']), 22)
equal('all 6600 independently evaluated comparisons', all(p['passed'] for p in all_pairs), True)
weakest = min(all_pairs, key=lambda pair: pair['margin_scaled'])
equal('construction summary', old['summary'], dict(support_count=22, pair_count=6600,
      weakest_pair=weakest, rational_checks=31, table_checks=226, failures=[]))
equal('written weakest margin', str(F(weakest['margin_scaled'], S)), '629441541677/50000000000')
equal('written boundary upper', supports[0]['boundary_guard']['upper'], '-474883782659/125000000000')
lt('weakest rejection >12.58', F(1258, 100), F(weakest['margin_scaled'], S))

# Independently check the imported L071 full numerical comparison as used in L072.
old_support_pairs = []
for k in range(24):
    A = sum(3*J[i]+H[i] for i in range(k))
    D = sum(4*J[i]+H[i]+2 for i in range(k))+(18 if k == 23 else 0)
    for r in range(k+1, 25):
        old_support_pairs.append(dict(k=k, r=r, A=A, D=D,
                                      margin=4*J[r]*ell-29*S-A*u+D*ell))
equal('imported 300-pair minimum', min(p['margin'] for p in old_support_pairs), 12588830833540)
adjacent = [(p['k'], p['margin']) for p in old_support_pairs if p['r'] == p['k']+1]
L071 = (ROOT / 'lemmas/L071-permuted-two-recipient-j-infeasibility.md').read_text()
printed = [tuple(map(int, row)) for row in re.findall(r'^\|(\d+)\|(\d+)\|$', L071, re.M)]
equal('all 24 printed L071 weakest margins', adjacent, printed)

failures = [c['name'] for c in checks if not c['passed']]
# Avoid duplicating multi-megabyte evidence in comparison diagnostics.
for c in checks:
    if 'complete original arithmetic records' in c['name'] and c['passed']:
        c['actual'] = c['required'] = 'Full structure equality verified; independent record stored in supports.'
result = dict(target=old['target'], source_sha256=hashlib.sha256(original_bytes).hexdigest(),
              table=table, logarithms=logs,
              Lambda=dict(lower=str(lambda_low), upper=str(lambda_high),
                          outward_grid_enclosure=lambda_display, required=[str(lm), str(lp)]),
              exact_bounds=expected_bounds,
              exponential={str(z): dict(terms=list(map(str, exp_terms[z])), total=str(sum(exp_terms[z]))) for z in [24, 27]},
              supports=supports, imported_L071_pairs=old_support_pairs, checks=checks,
              summary=dict(check_count=len(checks), support_count=22, pair_count=6600,
                           weakest_pair=weakest, boundary_upper=supports[0]['boundary_guard']['upper'],
                           normalized_upper=str(normalized), Lambda_grid=lambda_display, failures=failures),
              limitation='Finite exact audit; full interval/order and coefficient positivity are proved in L072, not by sampling.')
path = HERE / 'earlier-recipient-audit-certificate.json'
path.write_text(json.dumps(result, indent=2)+'\n')
print(f'{len(checks)} audit checks; all 22 supports / 6600 pairs compared completely; failures: {failures}')
print(f'Weakest margin {F(weakest["margin_scaled"], S)} > required 12.58; boundary upper {supports[0]["boundary_guard"]["upper"]} < -3.79 (guard requires >=0)')
print(f'Normalized upper {normalized} < required 20000000000; Lambda enclosure {lambda_display}, required ({lm}, {lp})')
print(f'Certificate: {path}')
assert not failures
