#!/usr/bin/env python3
"""Independent ordered-draw replay of every mathematical L130 certificate field."""
import hashlib
import json
from fractions import Fraction
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
source = HERE / 'threshold-retention-alteration.json'
raw = source.read_bytes()
saved = json.loads(raw)
failures = []
checks = {}


def check(name, condition):
    checks[name] = bool(condition)
    if not condition:
        failures.append(name)


def rat(x):
    x = Fraction(x)
    return dict(numerator=x.numerator, denominator=x.denominator)


def falling(n, k):
    result = 1
    for i in range(k):
        result *= n-i
    return result


# Ordered images of a fixed right block, without replacement. State j counts
# how many of the seven marked (left-block) labels have been drawn so far.
states = [1]
layers = [states]
for i in range(7):
    following = [0] * (i+2)
    for j, count in enumerate(states):
        following[j] += count * (955-(i-j))
        following[j+1] += count * (7-j)
    states = following
    layers.append(states)
    check(f'draw_partition_{i+1}', sum(states) == falling(962, i+1))
ordered_total = sum(states)
check('images_divisible_by_7_factorial', all(x % factorial(7) == 0 for x in states))
subset_counts = [x // factorial(7) for x in states]
denominator = ordered_total // factorial(7)
rows = [dict(intersection=j, subset_count=x, injection_count=states[j],
             probability=rat(Fraction(states[j], ordered_total)),
             ordered_image_probability=rat(Fraction(states[j], ordered_total)),
             forbidden=(j >= 4)) for j, x in enumerate(subset_counts)]
for j in range(8):
    check(f'full_saved_row_{j}', saved['intersection_distribution'][j] == rows[j])
check('exactly_eight_rows', len(saved['intersection_distribution']) == 8)

q = 137
total = q*q*q
star = q*q
left = total-star
tail = sum(subset_counts[4:])
p = Fraction(sum(states[4:]), ordered_total)
expected = left * total * p
cap = expected.numerator // expected.denominator
right = total-cap
# 35 four-subsets of the fixed seven labels; inclusion probability (7)_4/(962)_4.
union_p = 35 * Fraction(falling(7, 4), falling(962, 4))
check('strict_expected_edge_bracket', 225024 < expected < 225025)
check('canonical_probability', p == Fraction(317147681, 9250668537533852))
check('canonical_expectation', expected == Fraction(3798592669695986594, 16880782002799))
check('canonical_counts', (total, star, left, right, cap) ==
      (2571353, 18769, 2552584, 2346329, 225024))
check('left_strict_threshold', left > 1532496)
check('right_strict_threshold', right > 1532496)
check('loss_within_budget', cap <= total-1532496)
check('union_bound_comparison', p <= union_p)
check('conditional_extension_count', denominator * factorial(7) * factorial(955) == factorial(962))
check('q_prime', all(q % d for d in range(2, 12)))
check('seven_distinct_T', len(set([16,64,70,102,112,118,121])) == 7)

expected_fields = {
    'parameters': {'q': 137, 'H': 1024, 'K': 60, 'Y': 962, 'residual_size': 7,
                   'total_blocks': total, 'left_star_deleted': star,
                   'retention_required_each': 1532496,
                   'overlap_required_for_proposed_bridge': 18632},
    'conditional_sample_space_size': factorial(962),
    'subset_denominator': denominator,
    'intersection_distribution': rows,
    'forbidden_subset_count': tail,
    'forbidden_pair_probability': rat(p),
    'expected_conflict_edges': rat(expected),
    'fourth_subset_union_probability': rat(union_p),
    'existence_edge_cap': cap,
    'retained_bounds': {'left': left, 'right': right, 'left_margin': left-1532496,
                        'right_margin': right-1532496,
                        'right_deletion_budget': total-1532496,
                        'ambient_common_star_overlap': 0},
    'checks': {name: True for name in [
        'ground_size', 'conditional_bijection_ground', 'hypergeometric_partition',
        'injection_partition', 'every_probability_agrees',
        'tail_below_independent_union_bound', 'floor_brackets_expectation',
        'left_threshold', 'right_threshold', 'deletion_budget',
        'ambient_overlap_below_required']},
    'failures': [],
}
for key, value in expected_fields.items():
    check('saved_field_'+key, saved[key] == value)
check('complete_saved_schema', set(saved) == set(expected_fields) |
      {'scope', 'conditional_probability_justification'})
check('ground_count', 1024-60-2 == 7*137+4-1 == 962)

output = HERE / 'l130-critical-audit.json'
report = {
    'scope': 'Exact L130 arithmetic audit; canonical lemma supplies the symbolic proof.',
    'input_sha256': hashlib.sha256(raw).hexdigest(),
    'method': 'Sequential ordered draws without replacement; all eight states and all saved mathematical fields compared.',
    'ordered_draw_layers': layers,
    'recomputed': expected_fields,
    'strict_expectation_floor_remainder': expected.numerator-cap*expected.denominator,
    'checks': checks, 'failures': failures,
    'symbolic_obligations': [
        'Nonempty conditional sample space of 962! bijections',
        'All sample-space labelings have zero right ambient star',
        'Cross supports are distinct; intersection is 60+j',
        'Polynomial blocks are distinct; expectation counts actual edges',
        'Finite averaging gives an integer edge count at most floor(expectation)',
        'Deleting right endpoints costs at most the number of edges',
        'L030 packing survives arbitrary bijections and deletion',
    ],
    'qualification': 'No sampled labeling or RS realization; symbolic obligations are reviewed in L130, not proved by these checks.',
}
output.write_text(json.dumps(report, indent=2)+'\n')
print(f'Independent ordered-draw audit: {len(checks)-len(failures)}/{len(checks)} checks; failures: {failures}')
print(f'Expected edges {expected}; cap {cap}; deletion budget {total-1532496}')
print(f'Retained left {left}, right >= {right}; required each 1532496; ambient overlap 0')
print(f'Certificate: scripts/finite-support/{output.name}')
if failures:
    raise SystemExit(1)
