#!/usr/bin/env python3
"""Inspect every counting record using independent CRT idempotents.

This is certificate verification, not a second choice of sieve. Its
complete work ledger is added to the producer's work before cap comparison.
"""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from math import prod
from pathlib import Path
import json

SRC = Path('scripts/pair-genus-two/seminvariant-workload-certificate.json')
OUT = Path('scripts/pair-genus-two/seminvariant-workload-verification.json')
c = json.loads(SRC.read_text())
I, J = 8624880, -46962471600
work = Counter()
checks = {}


def require(name, value):
    checks[name] = bool(value)
    assert value, name


require('exact_instance_and_fixed_moduli', c['invariants'] == dict(I=I, J=J)
        and c['fixed_sieve']['square_image_moduli'] == [64, 5, 7, 11, 13])
roots = [tuple(map(Q, r['interval'])) for r in c['roots']]
for i, (lo, hi) in enumerate(roots):
    values = [x**3-3*I*x+J for x in (lo, hi)]
    require(f'root_{i}_complete_endpoint_values',
            values == list(map(Q, c['roots'][i]['endpoint_values']))
            and lo < hi and values[0]*values[1] < 0)
require('ordered_roots', roots[0][1] < roots[1][0] and roots[1][1] < roots[2][0])
phi3, phi2, phi1 = roots

# Evaluate the combined quadratic directly rather than adding interval terms.
def source_endpoints(name, a):
    if name == 'type1_positive':
        return sorted(-4*a*x for x in phi1), sorted(-4*a*x for x in phi2)
    extreme = phi3 if a > 0 else phi1
    low = sorted(-4*a*x for x in extreme)
    # g'(t)=-(8/3)t-4a is strictly positive on the whole phi2 bracket.
    require(f'upper_quadratic_increasing_{name}_{a}', -Q(8, 3)*phi2[1]-4*a > 0)
    upper = [Q(4, 3)*(I-t*t)-4*a*t for t in phi2]
    return low, upper


expected_indices = [(name, sign*m) for name, sign, maximum in
                    [('type1_positive', 1, 1043), ('type2_positive', 1, 898),
                     ('type2_negative', -1, 144)] for m in range(1, maximum+1)]
require('all_region_indices', [(v['type'], v['a']) for v in c['region_intervals']]
        == expected_indices)
for row in c['region_intervals']:
    work['signed_region_interval_reviews'] += 1
    lower, upper = source_endpoints(row['type'], row['a'])
    inner = [lower[1].__ceil__(), upper[0].__floor__()]
    outer = [lower[0].__ceil__(), upper[1].__floor__()]
    require(f"interval_{row['type']}_{row['a']}",
            inner == outer == row['inner_integer_interval'] == row['outer_integer_interval'])

images = {}
for modulus in (64, 5, 7, 11, 13):
    table = []
    for r in range(modulus):
        work['square_image_residue_reviews'] += 1
        table.append(27*r*r % modulus)
    require(f'square_image_table_{modulus}',
            table == c['fixed_sieve']['square_image_tables'][str(modulus)])
    images[modulus] = set(table)
for p in range(27):
    work['div27_residue_reviews'] += 1
    require(f'div27_{p}', c['fixed_sieve']['mod27_predicate'][p]
            == (p**3 % 27 == 0) == (p % 3 == 0))
for p in range(64):
    work['mod64_residue_reviews'] += 1
    require(f'mod64_{p}', c['fixed_sieve']['mod64_predicate'][p]
            == (p**3 % 64 in images[64]) == (p % 8 in (0, 3, 4)))

moduli = [3, 8, 5, 7, 11, 13]
M = prod(moduli)
require('crt_product', M == c['fixed_sieve']['product'] == 120120)
basis = []
for m in moduli:
    work['crt_idempotent_preparations'] += 1
    Mi = M//m
    basis.append(Mi*pow(Mi, -1, m))
total = 0
row_summaries = []
expected_producer_crt = 0
expected_producer_counts = 0
expected_producer_work = 2085+27+100+64
for a, row in enumerate(c['completed_count_rows'], start=1):
    require(f'prefix_index_{a}', row['a'] == a and row['type'] == 'type1_positive'
            and row['complete'] and row['work_before'] == expected_producer_work)
    allowed = [[0], [0, 3, 4]]
    for m in moduli[2:]:
        valid = []
        for p in range(m):
            work['prime_predicate_residue_reviews'] += 1
            if (p**3-48*I*a*a*p-64*J*a**3) % m in images[m]:
                valid.append(p)
        allowed.append(valid)
    require(f'allowed_residues_{a}',
            row['allowed_residues'] == {str(m): v for m, v in zip(moduli, allowed)})
    # The direct CRT sum differs from the producer's incremental joining.
    residues = set()
    for choice in product(*allowed):
        work['crt_idempotent_combination_trials'] += 1
        residues.add(sum(x*e for x, e in zip(choice, basis)) % M)
    require(f'crt_complete_distinct_{a}', len(residues) == prod(map(len, allowed))
            == len(row['progressions']) and residues == {v[0] for v in row['progressions']})
    lo, hi = c['region_intervals'][a-1]['inner_integer_interval']
    require(f'count_interval_{a}', row['interval'] == [lo, hi])
    n = 0
    for residue, lower_floor, upper_floor, saved_count in row['progressions']:
        work['aggregate_progression_recounts'] += 1
        first = (lo-residue+M-1)//M
        last = (hi-residue)//M
        count = max(0, last-first+1)
        require(f'floor_record_{a}_{residue}',
                (first-1, last, count) == (lower_floor, upper_floor, saved_count))
        n += count
    total += n
    sizes = [prod(len(v) for v in allowed[:i+1]) for i in range(len(moduli))]
    require(f'crt_stage_cardinalities_{a}',
            row['crt_stage_sizes'] == [dict(modulus=prod(moduli[:i+1]), size=v)
                                      for i, v in enumerate(sizes)])
    expected_producer_crt += sum(sizes)
    expected_producer_counts += len(residues)
    expected_producer_work += 36+len(moduli)+sum(sizes)+len(residues)
    require(f'count_totals_{a}', n == row['pair_count']
            and total == row['cumulative_pair_count']
            and expected_producer_work == row['work_after'])
    row_summaries.append(dict(a=a, lower=lo, upper=hi, residue_count=len(residues),
                              pairs=n, cumulative_pairs=total))

expected_ledger = dict(signed_region_interval_preparations=2085,
                       divisibility_residue_cells=27, square_image_residue_cells=100,
                       mod64_predicate_cells=64,
                       prime_predicate_residue_cells=36*len(row_summaries),
                       crt_inverse_preparations=6*len(row_summaries),
                       crt_combination_trials=expected_producer_crt,
                       aggregate_progression_counts=expected_producer_counts)
require('producer_full_ledger', c['workload']['ledger'] == expected_ledger
        and c['workload']['actual_counting_work'] == sum(expected_ledger.values()))
require('prefix_total_and_stop', total == c['workload']['certified_sieve_pair_lower_bound']
        == 216116 and total > 200000 and len(row_summaries) == 34
        and c['partial_row'] is None
        and c['workload']['result'] == 'STOP_FIXED_SIEVE_PAIR_INSPECTIONS_OVER_CAP')
combined = sum(work.values())+c['workload']['actual_counting_work']
require('combined_counting_and_verification_within_cap', combined <= 200000)
require('no_producer_failures', not c['failures'] and all(c['checks'].values()))
verification = dict(source=str(SRC), sha256=sha256(SRC.read_bytes()).hexdigest(),
                    method='All table entries and all progression tuples checked; independent direct CRT idempotents.',
                    row_summaries=row_summaries,
                    verification_ledger=dict(work), verification_work=sum(work.values()),
                    producer_work=c['workload']['actual_counting_work'],
                    combined_work=combined, required_cap=200000,
                    verified_pair_lower_bound=total,
                    checks=checks, failures=[k for k, v in checks.items() if not v])
OUT.write_text(json.dumps(verification, indent=2)+'\n')
print('Full progression verification:', len(checks), 'checks; failures:', verification['failures'])
print('Verification work:', sum(work.values()), '; producer:', verification['producer_work'],
      '; combined:', combined, '/ 200000')
print('Certified pair lower bound:', total, '> 200000; full region count: incomplete')
print('Verification:', OUT)
