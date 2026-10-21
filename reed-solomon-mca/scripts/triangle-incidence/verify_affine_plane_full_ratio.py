"""Replay every full-system rejection against L077's original incidence.

Uses homogeneous first-slot recovery instead of the producer's explicit
vertical formulas. Full input rows are verified, not sampled previews.
"""
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent
P = 97
GROUPS = [
    ['y_1', 'z_2', 'w_1', 'd_1'],
    ['y_2', 'c', 'd_6', 'd_5'],
    ['b', 'z_1', 'd_2', 'd_7'],
    ['a', 'd_4', 'd_3', 'w_2'],
]
NAMES = ['a', 'b', 'y_1', 'y_2', 'c', 'd_1', 'd_2', 'd_3',
         'z_1', 'd_4', 'd_5', 'w_1', 'z_2', 'd_6', 'w_2', 'd_7']
BLOCKS = [f'V{i}' for i in range(4)] + [f'M{m}D{i}' for m in range(3) for i in range(4)]
INV = [0] + [pow(x, -1, P) for x in range(1, P)]


def det(a, b):
    return (a[0]*b[1]-a[1]*b[0]) % P


def cross_parts(ps):
    a, b, c, d = ps
    return det(a, c)*det(b, d) % P, det(a, d)*det(b, c) % P


old = json.loads((ROOT/'affine-plane-quadrilaterals.json').read_text())['quadrilaterals']
new = json.loads((ROOT/'affine-plane-full-ratio-incidence.json').read_text())['quadruples']
failures = []
quads = []
for source, claim in zip(old, new):
    group = next((i for i, names in enumerate(GROUPS)
                  if set(names) == set(source['singleton_labels'])), None)
    if group is None:
        failures.append('singleton group missing')
        continue
    ids = [BLOCKS.index(b) for b in source['blocks']]
    positions = [GROUPS[group].index(n) for n in source['singleton_labels']]
    if (ids != claim['blocks'] or group != claim['ratio_group']
            or positions != claim['permutation']
            or [NAMES.index(n) for n in source['singleton_labels']] != claim['singletons']):
        failures.append('incidence mismatch')
    quads.append((ids, group, positions))
if len(old) != 48 or len(new) != 48 or len(quads) != 48:
    failures.append('complete incidence coverage')
recovery_quad = []
for v, e in [(1, 1), (2, 2), (3, 3)]:
    recovery_quad.append(next(q for q in quads if q[0] == [v, 4, 8, 12+e]))


def label_cross(ratios, quad):
    _, group, positions = quad
    canonical = [(0, 1), (1, 0), (1, 1), (1, ratios[group])]
    return cross_parts([canonical[i] for i in positions])


def build_points(ratios, ds):
    a, b, c, _ = ratios
    d1, d2, d3 = ds
    h = [0, (1-(1-b)*c*d3)*INV[b] % P,
         (1-(1-c)*a*d1)*INV[c] % P, (1-(1-a)*b*d2)*INV[a] % P]
    d = [1, d1, d2, d3]
    e = [(h[1]+(a-1)*d3)*INV[a] % P, b*d2 % P, c*d3 % P, a*d1 % P]
    points = [(0, 1), None, None, None] + [(1, x) for x in h+d+e]
    for quad in recovery_quad:
        (v, hi, di, ei), _, _ = quad
        hp, dp, ep = points[hi], points[di], points[ei]
        num, den = label_cross(ratios, quad)
        # Solve chi(p,h,d,e)=num/den as a homogeneous linear equation.
        c0 = (dp[1]*det(hp, ep)*den-num*ep[1]*det(hp, dp)) % P
        c1 = (-dp[0]*det(hp, ep)*den+num*ep[0]*det(hp, dp)) % P
        points[v] = (-c1 % P, c0)
    return points


with (ROOT/'affine-plane-affine-rank-rows.csv').open() as first, \
        (ROOT/'affine-plane-full-ratio-rows.csv').open() as second:
    source = (r for r in csv.DictReader(first) if r['status'] == 'unique_distinct')
    rejection = iter(csv.DictReader(second))
    counts = Counter()
    failed_quads = Counter()
    selected = None
    cases = 0
    for row in source:
        claim = next(rejection, None)
        if claim is None:
            failures.append('missing rejection row')
            break
        ratios = [int(row[x]) for x in ['A', 'B', 'C', 'D']]
        if ratios != [int(claim[x]) for x in ['A', 'B', 'C', 'D']]:
            failures.append('ratio order/coverage mismatch')
            break
        points = build_points(ratios, [int(row[x]) for x in ['d1', 'd2', 'd3']])
        if any(p == (0, 0) for p in points):
            failures.append('zero recovered projective vector')
        status = claim['status']
        if status == 'sixteen_direction_collision':
            i, j = int(claim['first_collision_i']), int(claim['first_collision_j'])
            if not 0 <= j < i < 16 or det(points[i], points[j]) != 0:
                failures.append('invalid collision witness')
        elif status == 'equation_rejected':
            n = int(claim['first_failed_quad'])
            quad = quads[n]
            left, right = cross_parts([points[i] for i in quad[0]])
            num, den = label_cross(ratios, quad)
            difference = (left*den-right*num) % P
            if den == 0 or difference == 0:
                failures.append('invalid equation witness')
            failed_quads[n] += 1
            if n == 16:
                selected = {'ratios': ratios, 'directions': points,
                            'quad_index': n, 'blocks': [BLOCKS[i] for i in quad[0]],
                            'singleton_labels': old[n]['singleton_labels'],
                            'label_numerator_denominator': [num, den],
                            'direction_numerator_denominator': [left, right],
                            'nonzero_difference': difference}
        else:
            failures.append('unrejected candidate')
        counts[status] += 1
        cases += 1
    if next(rejection, None) is not None:
        failures.append('extra rejection rows')

expected = {'sixteen_direction_collision': 209214, 'equation_rejected': 462810}
if cases != 672024 or dict(counts) != expected:
    failures.append('rejection totals')
cert = {'scope': 'All 672024 rejection witnesses; original L077 incidence and homogeneous recovery',
        'actual': {'incidence_rows': len(quads), 'rejection_witnesses': cases,
                   'counts': dict(counts), 'first_failed_quad_histogram': dict(failed_quads)},
        'required': {'incidence_rows': 48, 'rejection_witnesses': 672024, 'counts': expected},
        'selected_last_branch_witness': selected, 'failures': failures}
path = ROOT/'affine-plane-full-ratio-replay.json'
path.write_text(json.dumps(cert, indent=2)+'\n')
print(f'{"FAIL" if failures else "PASS"}: complete incidence {len(quads)}/48; '
      f'rejection witnesses {cases}/672024; counts {dict(counts)}/{expected}; '
      f'failures {len(failures)}/0.')
print('Certificate:', path)
raise SystemExit(bool(failures))
