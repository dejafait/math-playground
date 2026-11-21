#!/usr/bin/env python3
"""Audit every L946 range by exact binomial expansion, without its producer.

All inherited audits are reused under complete flags and hashes. This is
not a new theta-node/library audit. Originals are never overwritten.
"""
import hashlib
import json
import re
import sys
from decimal import Decimal, localcontext
from fractions import Fraction as F
from math import comb, factorial, prod
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parent
OUT = BASE / 'l946-cover-audit-78.json'
S, J, K = 2**1024, 768, 128
report = {'status': 'IN_PROGRESS', 'checks': [], 'failures': [],
          'inputs_sha256': {}, 'ranges': [], 'python': sys.version,
          'method': 'Exact binomial derivative polynomials; one rounding per shifted coefficient; no rounded shifted-Horner recurrence.'}


def save():
    OUT.write_text(json.dumps(report, indent=2) + '\n')


def check(name, truth):
    report['checks'].append({'name': name, 'passed': bool(truth)})
    if not truth:
        report['status'] = 'FAILED'
        report['failures'].append(name)
        save()
        raise AssertionError(name)


def digest(name):
    h = hashlib.sha256((BASE / name).read_bytes()).hexdigest()
    report['inputs_sha256'][name] = h
    return h


def read(name):
    digest(name)
    return json.loads((BASE / name).read_text())


def ceil_ratio(a, b):
    q, r = divmod(a, b)
    return q + bool(r)


def upper(q):
    return ceil_ratio(q.numerator * S, q.denominator)


def display(q):
    with localcontext() as ctx:
        ctx.prec = 14
        return str(Decimal(q.numerator) / Decimal(q.denominator))


def exact_horner(coeffs, x):
    """Return numerator/denominator without any intermediate rounding.

    After descending to degree j, denominator is d^(m-j). Each new
    numerator is old*n + coefficient_j*d^(m-j+1).
    """
    acc, denominator = coeffs[-1], 1
    for coefficient in reversed(coeffs[:-1]):
        denominator *= x.denominator
        acc = acc * x.numerator + coefficient * denominator
    return acc, denominator


save()
cover = read('l938-direct-cover-76.json')
consistency = read('l938-direct-cover-check-76.json')
prior = read('l944-c944a-audit-75.json')
old = read('actual-h2-energy-cell-audit-50.json')
sharp = read('l938-two-bound-endpoint-73.json')
data = read('actual-h2-energy-cell-48.json')
poly = read('actual-h2-energy-cell-polynomial-48.json')
for label, obj, state, count in [
        ('step50', old, 'PASSED', 5101),
        ('step75', prior, 'PASSED', 15620),
        ('step76 checker', consistency, 'PASSED', 983),
        ('step76 producer', cover, 'CERTIFIED_COMPACT_COVER', None),
        ('C944a', sharp, 'SCOPED_ENDPOINT_PASS', 540)]:
    check(label + ' status/failures', obj['status'] == state and obj['failures'] == [])
    if count is not None:
        check(label + ' complete check count', len(obj['checks']) == count)
    for i, entry in enumerate(obj['checks']):
        check(label + ' flag ' + str(i) + ': ' + entry['name'], entry['passed'] is True)
for label, obj, key in [('step50', old, 'inputs_sha256'),
                        ('step75', prior, 'inputs_sha256'),
                        ('cover', cover, 'input_hashes')]:
    for name, expected in obj[key].items():
        check(label + ' inherited hash ' + name, digest(name) == expected)
for obj, script in [(cover, 'l938-direct-cover-76.py'),
                    (prior, 'audit-l944-c944a-75.py'),
                    (sharp, 'l938-two-bound-endpoint-73.py')]:
    check('producer hash ' + script, obj['producer_sha256'] == digest(script))
digest('check-l938-direct-cover-76.py')
identity = old['integer_identity']
check('reused exact identity', identity['residual'] == '0' and
      identity['difference_bound_lt_half_base'] is True and identity['degree'] == 3072)
check('same inherited identity', identity == prior['inherited_integer_identity'])

ap = data['approximation']
check('fixed budgets', (ap['degree'], ap['nodes'], ap['theta_terms'], ap['precision'],
      int(ap['chebyshev_denominator']), int(ap['power_denominator'])) ==
      (256, 257, 8, 200, 10**120, 10**120 * 4**256))
check('fixed cover arithmetic', cover['arithmetic'] == {
    'scale': str(S), 'retained_power_exponents': J, 'taylor_order': K,
    'maximum_depth': 12, 'maximum_intervals': 8191})
etas, deriv_etas, deriv_coeffs = [], [], []
check('257 complete coefficient intervals', len(ap['chebyshev_coefficients']) == 257)
for ell, row in enumerate(ap['chebyshev_coefficients']):
    lo, hi = F(row['enclosure']['lower']), F(row['enclosure']['upper'])
    chosen = F(int(row['chosen_numerator']), 10**120)
    eta = max(chosen-lo, hi-chosen)
    check('complete coefficient radius ' + str(ell), row['k'] == ell and lo <= hi and
          eta >= 0 and eta == F(row['absolute_error']))
    etas.append(eta)
    deriv_etas.append(eta * F(ell**2, 4))
    deriv_coeffs.append(abs(chosen) * F(ell**2, 4))
r, n, N = F(2, 3), 257, 256
tail0 = r**n / (1-r)
tail2 = r**n * (n*n*(1-r)**2 + 2*n*r*(1-r) + r*(1+r)) / (1-r)**3
epsilon = 8*10**9*r**N + sum(etas, F(0))
delta = F(10**9, 2)*(tail2 + N*N*tail0) + sum(deriv_etas, F(0))
B = sum(deriv_coeffs, F(0)) + delta
H = 2+epsilon
A, D = 12*epsilon*H**11, delta*H**11 + 11*B*epsilon*H**10
check('full epsilon', epsilon == F(ap['epsilon']) and 0 < epsilon < F(1, 10**34))
check('complete coefficient error sum', sum(etas, F(0)) == F(ap['coefficient_error_sum']))
rows = data['algebra']['terms']
lemma = (BASE.parent.parent / 'lemmas/L938-actual-h2-fixed-energy-density-and-cell-test.md').read_text()
table = [(int(c), tuple(map(int, exponents.split(',')))) for c, exponents in
         re.findall(r'^\|\s*(-?\d+)\s*\|\s*\(([0-9,]+)\)\s*\|$', lemma, re.M)]
check('34 complete rows', len(rows) == len(table) == 34)
weights = []
for i, row in enumerate(rows):
    alpha, coefficient = row['exponents_A0_to_A6'], row['coefficient']
    check('row identity and degrees ' + str(i), (coefficient, tuple(alpha)) == table[i]
          and len(alpha) == 7 and all(isinstance(a, int) and a >= 0 for a in alpha)
          and sum(alpha) == sum(k*a for k, a in enumerate(alpha)) == 12)
    weight = F(abs(coefficient), prod(factorial(k)**a for k, a in enumerate(alpha)))
    direct = F(abs(coefficient), 2**12 * factorial(17))
    for k, a in enumerate(alpha):
        direct *= (F(factorial(2*k), 4**k*factorial(k)) / factorial(2*k))**a
    check('positive beta weight ' + str(i), direct == weight / (2**36 * factorial(17)))
    weights.append(weight)
check('absolute row weight', sum(weights, F(0)) == F(293, 540))
Z = sum(weights, F(0)) / (2**36 * factorial(17))
bounds = {'epsilon': epsilon, 'delta': delta, 'B': B, 'common_factor_bound': H,
          'product_error': A, 'product_derivative_error': D, 'beta_constant': Z}
for key, value in bounds.items():
    check('full constant ' + key, value > 0 and value == F(sharp['bounds'][key])
          and value == F(cover['bounds'][key]))
report['independent_bounds'] = {k: str(v) for k, v in bounds.items()}

rr, den = list(map(int, poly['numerators'])), int(poly['denominator'])
check('3073 R coefficients and C12', len(rr) == 3073 and
      den == (2*factorial(12)*int(ap['power_denominator'])*4**262)**12)
check('inherited full coefficient maximum', max(map(abs, rr)) == int(identity['saved_max_abs_coefficient']))
check('two full coefficient arrays', len(cover['coefficient_enclosures']) == 2)
polys = {}
for s, saved in zip([17, 16], cover['coefficient_enclosures']):
    check('coefficient offset/length ' + str(s), saved['offset'] == s and len(saved['intervals']) == s+3073)
    coefficients = []
    for j, pair in enumerate(saved['intervals']):
        lo, hi = map(int, pair)
        numerator = 0 if j < s else rr[j-s] * 4**j * S
        denominator = den * factorial(j)
        check('full signed coefficient ' + str((s, j)),
              lo*denominator <= numerator < (lo+1)*denominator and
              (hi-1)*denominator < numerator <= hi*denominator)
        coefficients.append((lo, hi))
    tail = sum(max(abs(lo), abs(hi)) for lo, hi in coefficients[J:])
    check('complete finite tail ' + str(s), tail == int(saved['uniform_discarded_tail_scaled']))
    polys[s] = (coefficients[:J], tail)
save()

# Precomputed binomial weights are exact. For each k the separate polynomial
# sum_{j=k}^{J-1} endpoint_j * binom(j,k) * c^(j-k) is evaluated with a
# common dyadic denominator. No producer functions or Taylor arrays are used.
binomials = [[comb(j, k) for j in range(k, J)] for k in range(K)]
nodes = {(x['depth'], x['index']): x for x in cover['nodes']}
check('all99 unique nodes and root', len(nodes) == len(cover['nodes']) == 99 and (0, 0) in nodes)
leaves = []
for node_number, ((depth, index), node) in enumerate(nodes.items(), 1):
    tag = str((depth, index))
    left, right = map(F, node['E'])
    check('closed dyadic endpoints ' + tag, 0 <= depth <= 12 and 0 <= index < 2**depth
          and left == F(2**depth+15*index, 4*2**depth)
          and right == F(2**depth+15*(index+1), 4*2**depth) and left < right)
    a, b = left/4, right/4
    c, h = (a+b)/2, (b-a)/2
    check('nonnegative range hypotheses ' + tag, 0 < a <= c <= b <= 1 and h > 0)
    for key, s in [('value', 17), ('derivative', 16)]:
        if key not in node:
            continue
        obj, coefficients = node[key], polys[s][0]
        exact_rounded = []
        for k in range(K):
            lo_coeffs = [pair[0]*weight for pair, weight in zip(coefficients[k:], binomials[k])]
            hi_coeffs = [pair[1]*weight for pair, weight in zip(coefficients[k:], binomials[k])]
            low, denominator = exact_horner(lo_coeffs, c)
            high, other_denominator = exact_horner(hi_coeffs, c)
            check('exact binomial order ' + tag + key + str(k), denominator == other_denominator and low <= high)
            exact_rounded.append((low//denominator, ceil_ratio(high, denominator)))
        ev = obj['evidence']
        cl, ch = map(int, ev['center_coefficient'])
        check('independent center inclusion ' + key + tag,
              cl <= exact_rounded[0][0] <= exact_rounded[0][1] <= ch)
        magnitudes = [0] + [max(abs(lo), abs(hi)) for lo, hi in exact_rounded[1:]]
        var_num, var_den = exact_horner(magnitudes, h)
        var = ceil_ratio(var_num, var_den)
        check('complete independent variation ' + key + tag, 0 <= var <= int(ev['variation_scaled']))
        remainder_coeffs = [max(abs(lo), abs(hi))*comb(j, K)
                            for j, (lo, hi) in enumerate(coefficients) if j >= K]
        q_num, q_den = exact_horner(remainder_coeffs, b)
        Q = int(ev['taylor_derivative_bound_scaled'])
        check('independent full Kth derivative bound ' + key + tag, 0 <= q_num <= Q*q_den)
        hp = h**K
        W = ceil_ratio(Q*hp.numerator, hp.denominator)
        check('outward Kth remainder and complete tail ' + key + tag,
              W == int(ev['taylor_remainder_scaled']) and
              polys[s][1] == int(ev['discarded_tail_scaled']) and W >= 0)
        extra = int(ev['variation_scaled']) + W + polys[s][1]
        plo, phi = map(int, obj['polynomial_scaled'])
        check('complete full polynomial range ' + key + tag, (plo, phi) == (cl-extra, ch+extra))
        radius = upper(Z*right**17*A if s == 17 else Z*right**16*(17*A+right*D))
        check('complete actual radius and range ' + key + tag,
              radius > 0 and radius == int(obj['actual_radius_scaled']) and
              list(map(int, obj['actual_scaled'])) == [plo-radius, phi+radius])
        report['ranges'].append({'node': [depth, index], 'observable': key,
            'center': str(c), 'half_width': str(h), 'right_endpoint_y': str(b),
            'exact_binomial_outward_scaled': [[str(lo), str(hi)] for lo, hi in exact_rounded],
            'independent_variation_scaled': str(var),
            'exact_Kth_majorant_numerator': str(q_num), 'exact_Kth_majorant_denominator': str(q_den),
            'saved_polynomial_scaled': obj['polynomial_scaled'], 'actual_scaled': obj['actual_scaled'],
            'actual_radius_scaled': str(radius)})
    vlo, vhi = map(int, node['value']['actual_scaled'])
    decision = node['decision']
    check('derivative evaluated exactly when needed ' + tag, ('derivative' in node) == (vlo <= 0 <= vhi))
    if decision == 'VALUE_NEGATIVE':
        check('strict negative value ' + tag, vhi < 0)
    elif decision == 'VALUE_POSITIVE':
        check('strict positive value ' + tag, vlo > 0)
    elif decision == 'DERIVATIVE_POSITIVE':
        check('strict positive derivative at every possible zero ' + tag,
              vlo <= 0 <= vhi and int(node['derivative']['actual_scaled'][0]) > 0)
    else:
        check('only genuine unresolved internal nodes ' + tag, decision == 'BISECT' and depth < 12
              and vlo <= 0 <= vhi and int(node['derivative']['actual_scaled'][0]) <= 0)
    if decision == 'BISECT':
        check('both children ' + tag, (depth+1, 2*index) in nodes and (depth+1, 2*index+1) in nodes)
    else:
        leaves.append(node)
    if depth:
        check('valid parent ' + tag, nodes[(depth-1, index//2)]['decision'] == 'BISECT')
    if node_number % 10 == 0:
        report['progress'] = {'nodes': node_number, 'ranges': len(report['ranges'])}
        save()
        print('Independent exact audit:', node_number, '/99 nodes;', len(report['ranges']), 'ranges', flush=True)

leaves.sort(key=lambda node: F(node['E'][0]))
check('complete outer closed endpoints', F(leaves[0]['E'][0]) == F(1, 4) and F(leaves[-1]['E'][1]) == 4)
check('every shared endpoint covered', all(F(x['E'][1]) == F(y['E'][0]) for x, y in zip(leaves, leaves[1:])))
counts = {key: sum(x['decision'] == key for x in leaves) for key in
          ['VALUE_NEGATIVE', 'VALUE_POSITIVE', 'DERIVATIVE_POSITIVE', 'UNRESOLVED']}
check('all budgets and leaf counts', len(leaves) == 50 and counts == {
    'VALUE_NEGATIVE': 22, 'VALUE_POSITIVE': 24, 'DERIVATIVE_POSITIVE': 4, 'UNRESOLVED': 0}
    and max(d for d, i in nodes) == 9 and len(nodes) <= 8191)
ratios, derivative_margins = [], []
for node in leaves:
    decision = node['decision']
    obj = node['derivative'] if decision == 'DERIVATIVE_POSITIVE' else node['value']
    lo, hi = map(int, obj['polynomial_scaled'])
    radius = int(obj['actual_radius_scaled'])
    clearance = -hi if decision == 'VALUE_NEGATIVE' else lo
    check('strict full-kernel leaf margin ' + str((node['depth'], node['index'])), clearance > radius > 0)
    ratios.append((F(clearance, radius), node['depth'], node['index'], decision, clearance-radius))
    if decision == 'DERIVATIVE_POSITIVE':
        derivative_margins.append({'node': [node['depth'], node['index']], 'E': node['E'],
            'actual_derivative_lower_over_pi6': str(F(clearance-radius, S)),
            'display': display(F(clearance-radius, S)), 'required': '>0'})
ratio, depth, index, decision, gap = min(ratios)
saved = cover['summary']['minimum_clearance_over_radius']
check('complete minimum and strict bracket', 78557 < ratio < 78558 and ratio == F(saved['exact_ratio'])
      and [depth, index] == saved['node'] == [5, 31] and decision == saved['decision']
      and gap == int(saved['strict_gap_scaled']))
check('full saved summary counts', cover['summary']['intervals_examined'] == len(nodes)
      and cover['summary']['closed_leaves'] == len(leaves)
      and cover['summary']['maximum_depth_reached'] == 9 and cover['summary']['leaf_counts'] == counts
      and cover['summary']['unresolved_closed_intervals'] == [])
for name, expected in list(report['inputs_sha256'].items()):
    check('original unchanged ' + name, hashlib.sha256((BASE/name).read_bytes()).hexdigest() == expected)
report.pop('progress', None)
report['summary'] = {'nodes': len(nodes), 'ranges': len(report['ranges']), 'closed_leaves': len(leaves),
    'leaf_counts': counts, 'maximum_depth': 9, 'minimum_clearance_ratio': str(ratio),
    'ratio_display': display(ratio), 'required_clearance_ratio': '>1',
    'minimum_ratio_node': [depth, index], 'derivative_leaf_lower_bounds': derivative_margins,
    'conclusion': 'L946 compact crossing validated under inherited C944a/L938 execution contracts; no global crossing conclusion.'}
report['status'] = 'PASSED'
report['producer_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
save()
print('PASSED:', len(report['checks']), 'checks;', len(nodes), 'nodes;', len(report['ranges']), 'independent ranges;', len(leaves), 'closed leaves')
print('Minimum clearance/kernel radius:', display(ratio), '; required >1; derivative leaves:', len(derivative_margins), '; all lower bounds >0')
for entry in derivative_margins:
    print('E=', entry['E'], 'vprime/pi6 >=', entry['display'], '; required >0')
print('Failures:', report['failures'], '; full certificate:', OUT)
