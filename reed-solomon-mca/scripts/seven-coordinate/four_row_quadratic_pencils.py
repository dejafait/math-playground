"""Exact structural obstruction certificate, not an original-label census.

Enumerate 105 pencils from two unordered disjoint coordinate pairs in S.
Record every one of the 36 J-pair membership tests for every pencil.
Run from the active notebook: python3 scripts/seven-coordinate/four_row_quadratic_pencils.py
"""
from itertools import combinations
from pathlib import Path
import json

P = 97
H = [1, 8, 12, 18, 22, 27, 33, 47, 50, 64, 70, 75, 79, 85, 89, 96]
S = [1, 8, 12, 18, 22, 27, 33]
J = [x for x in H if x not in S]


def polynomial(pair):
    u, v = pair
    return [u * v % P, -(u + v) % P, 1]


def cross(a, b):
    return [(a[1]*b[2]-a[2]*b[1]) % P,
            (a[2]*b[0]-a[0]*b[2]) % P,
            (a[0]*b[1]-a[1]*b[0]) % P]


def run():
    records, failures = [], []
    for left, right in combinations(list(combinations(S, 2)), 2):
        if set(left) & set(right):
            continue
        a, b = polynomial(left), polynomial(right)
        normal = cross(a, b)
        if not any(normal):
            failures.append(f'dependent S pair polynomials: {left}, {right}')
        tests = []
        for pair in combinations(J, 2):
            d = polynomial(pair)
            residue = sum(x*y for x, y in zip(normal, d)) % P
            tests.append(dict(pair=list(pair), polynomial=d, determinant_residue=residue,
                              in_pencil=(residue == 0)))
        members = [test['pair'] for test in tests if test['in_pencil']]
        records.append(dict(S_pairs=[list(left), list(right)], generators=[a,b],
                            normal=normal, J_pair_tests=tests, J_members=members,
                            actual_J_member_count=len(members),
                            required_for_exception=4))
    if len(records) != 105:
        failures.append(f'coverage: {len(records)} pencils rather than 105')
    maximum = max(r['actual_J_member_count'] for r in records)
    distribution = {str(n): sum(r['actual_J_member_count'] == n for r in records)
                    for n in range(maximum + 1)}
    survivors = [i for i, r in enumerate(records) if r['actual_J_member_count'] >= 4]
    groups = {}
    for i in survivors:
        r = records[i]
        first = next(x for x in r['normal'] if x)
        key = tuple(x * pow(first, -1, P) % P for x in r['normal'])
        group = groups.setdefault(key, dict(normal=list(key), S_pair_choices=[],
                                             J_members=r['J_members']))
        group['S_pair_choices'].append(r['S_pairs'])
        if group['J_members'] != r['J_members']:
            failures.append(f'inconsistent equal-pencil membership at {i}')

    # Independent coverage: 35 four-sets, each with its three partitions.
    expected_pairs = set()
    for u, v, w, z in combinations(S, 4):
        for a, b in [((u,v),(w,z)), ((u,w),(v,z)), ((u,z),(v,w))]:
            expected_pairs.add(tuple(sorted((a,b))))
    actual_pairs = {tuple(tuple(p) for p in r['S_pairs']) for r in records}
    if expected_pairs != actual_pairs or len(actual_pairs) != len(records):
        failures.append('independent four-set/partition coverage failed')

    # Independent membership: every monic polynomial in span(a,b) is
    # a + lambda*(b-a); solve one nonzero coefficient and check all three.
    verified_tests = 0
    for i, r in enumerate(records):
        a, b = r['generators']
        diff = [(y-x) % P for x,y in zip(a,b)]
        pivot = next(j for j in range(3) if diff[j])
        for test in r['J_pair_tests']:
            u,v = test['pair']
            d = [(u*v) % P, (P-u-v) % P, 1]
            lam = (d[pivot]-a[pivot]) * pow(diff[pivot], -1, P) % P
            belongs = all((a[j]+lam*diff[j]-d[j]) % P == 0 for j in range(3))
            if belongs != test['in_pencil'] or d != test['polynomial']:
                failures.append(f'independent membership failed at record {i}, pair {u,v}')
            verified_tests += 1
    out = dict(modulus=P,H=H,S=S,J=J,
               scope='All 105 unordered disjoint S-pair quadratic pencils; all 36 J pairs per pencil',
               records=records, actual_pencils=len(records), required_pencils=105,
               actual_membership_tests=sum(len(r['J_pair_tests']) for r in records),
               required_membership_tests=105*36,
               maximum_J_member_count=maximum, required_exceptional_count=4,
               count_distribution=distribution, survivor_record_indices=survivors,
               surviving_pencil_groups=list(groups.values()),
               independent_coverage_pencils=len(expected_pairs),
               independently_verified_membership_tests=verified_tests,
               failures=failures)
    path = Path(__file__).with_name('four-row-quadratic-pencils.json')
    path.write_text(json.dumps(out, indent=2)+'\n')
    print(f'Pencils: actual {len(records)}, required 105; membership tests: '
          f'actual {out["actual_membership_tests"]}, required 3780')
    print(f'J-pair members: maximum {maximum}, required for exception 4; distribution {distribution}')
    print(f'Surviving record indices: {survivors}; failures: {failures}')
    print(f'Distinct surviving pencils: {len(groups)}; independent coverage '
          f'{len(expected_pairs)}/105, independently verified tests {verified_tests}/3780')
    print(f'Full certificate: {path.relative_to(Path.cwd())}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
