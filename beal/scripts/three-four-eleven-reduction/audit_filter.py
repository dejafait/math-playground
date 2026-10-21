"""Independent record-level audit of L032's finite filter, not a point search.

Source rows are encoded independently in compressed signed form from FNS
Tables 1--3, final author PDF printed pp. 9--10; symplectic signs are from
Lemma 5.2, pp. 18--19. No import or execution of check_filter.py is used.
"""
import json
from collections import Counter
from itertools import product
from pathlib import Path

root = Path(__file__).parent
original = json.loads((root / 'filter-certificate.json').read_text())
O = {-3, -1, 1, 3}
E = {-6, -2, 2, 6}
D = O | E
# (index, source a residues, source b residues, d values)
s2 = [
    (1, [1], [-1], {1, -3}), (1, [-1], [-1], {-1, 3}),
    (2, [0], [1, -3], O), (2, [0], [3, -1], E),
    (3, [2], [1, -3], O), (3, [2], [3, -1], E),
    (4, [1], [0], {-2, 6}), (4, [-1], [0], {2, -6}),
    (5, [1, -1], [2], E), (6, [1, -1], [-2], E),
    (7, [1], [4], {-2, 6}), (7, [-1], [4], {2, -6}),
]
s3 = [
    (1, [1], [-1], {-3, 6}), (1, [-1], [-1], {3, -6}),
    (2, [0], [1, -1], D), (3, [3, -3], [1], D),
    (4, [3, -3], [-1], D), (5, [1, -1, 2, -2], [0], D),
    (6, [4, -4], [0], D), (7, [1, -1, 4, -4], [1], D),
    (8, [2, -2], [1], D),
]

def expand(rows, mx, ma):
    return sorted((i, x % mx, a % ma, tuple(sorted(ds)))
                  for i, xs, aa, ds in rows for x, a in product(xs, aa))

r2, r3 = expand(s2, 4, 8), expand(s3, 9, 3)
checks = []
def check(name, ok, detail=None):
    checks.append({'name': name, 'passed': bool(ok), 'detail': detail})

for key, expected, index, xkey, akey, modulus in [
    ('rows2', r2, 'i2', 'X_mod4', 'A_mod8', 4),
    ('rows3', r3, 'i3', 'X_mod9', 'A_mod3', 9),
]:
    actual = original[key]
    normalized = sorted((r[index], r[xkey], r[akey], tuple(sorted(r['d']))) for r in actual)
    check(key + ' complete source transcription', normalized == expected,
          {'actual': len(actual), 'required': len(expected)})
    squares = {x*x % modulus for x in range(modulus)}
    check(key + ' every square flag', all(r['square_residue'] == (r[xkey] in squares) for r in actual))
check('every source impossible flag', all(r['source_impossible'] == (r['i2'] == 7) for r in original['rows2']))

# Table 3, four row groups and four column groups, including every empty cell.
rowgroups = [[1], [2, 6], [3, 5], [4]]
colgroups = [[1], [2, 6, 8], [3, 5], [4, 7]]
matrix = [[None, None, None, '54a1'],
          [None, '288a1', '864b1', '864a1'],
          ['96a1', None, '864c1', None],
          [None, None, '27a1', None]]
labels = {(i, j): matrix[r][c]
          for r, rr in enumerate(rowgroups) for c, cc in enumerate(colgroups)
          for i, j in product(rr, cc)}
expected = {'retained_residue_patterns': [], 'rejected_residue_patterns': []}
for i, x4, a8, ds2 in r2:
    for j, x9, a3, ds3 in r3:
        label = labels.get((i, j))
        ds = sorted(set(ds2) & set(ds3))
        if i == 7 or label is None or not ds:
            continue
        reason = None
        if label in {'27a1', '288a1'}:
            reason = 'cited unconditional CM exclusion'
        else:
            # Assign the Lemma 5.2 sign at each individual d, independently
            # of A-mod-8 tests in the original implementation.
            signs = []
            for d in ds:
                if label in {'864a1', '864b1'}:
                    b_symplectic = (i == 6 or (i == 2 and d in O))
                    signs.append(b_symplectic if label == '864b1' else not b_symplectic)
                elif label in {'96a1', '864c1'}:
                    signs.append(i == 5 or (i == 3 and d in O))
                else:
                    signs.append(True)  # Theorem 5.1's multiplicative case.
            check(f'uniform symplectic sign {i}/{j}/{a8}/{label}', len(set(signs)) == 1)
            if not all(signs):
                reason = 'anti-symplectic: FNS Lemma 5.2'
        for B in range(36):
            if (B*B % 4, B*B % 9) != (x4, x9):
                continue
            for A in range(24):
                if (A % 8, A % 3) != (a8, a3):
                    continue
                record = dict(B_mod36=B, A_mod24=A, i2=i, i3=j, label=label, d=ds)
                if reason:
                    record['reason'] = reason
                key = 'rejected_residue_patterns' if reason else 'retained_residue_patterns'
                expected[key].append(record)

# Counters detect duplicate, missing, altered, or extra full records.
def counter(records):
    return Counter(json.dumps(r, sort_keys=True) for r in records)
for key, records in expected.items():
    actual, required = counter(original[key]), counter(records)
    check(key + ' full multiset', actual == required,
          {'actual': len(original[key]), 'required': len(records),
           'missing': list((required - actual).elements()),
           'extra': list((actual - required).elements())})

# Compare each complete conclusion row, including residues and d, rather
# than only the four-column branch labels checked by check_filter.py.
conclusion = [
    ('54a1', 1, 7, 1, 7, 1, [1, 4], {1, -3}),
    ('96a1', 5, 1, 1, 2, 2, [1], {6}),
    ('864a1', 2, 7, 0, 3, 1, [1, 4], E),
    ('864a1', 2, 7, 0, 7, 1, [1, 4], E),
    ('864b1', 2, 5, 0, 1, 0, [1, 7], O),
    ('864b1', 2, 5, 0, 5, 0, [1, 7], O),
    ('864b1', 6, 5, 1, 6, 0, [1, 7], E),
    ('864c1', 5, 5, 1, 2, 0, [1, 7], E),
]
full_conclusion = {(label, i, j, parity, a8, a3, x9, tuple(sorted(ds)))
                   for label, i, j, parity, a8, a3, xs, ds in conclusion for x9 in xs}
full_actual = {(r['label'], r['i2'], r['i3'], r['B_mod36'] % 2,
                r['A_mod24'] % 8, r['A_mod24'] % 3,
                r['B_mod36']**2 % 9, tuple(sorted(r['d'])))
               for r in expected['retained_residue_patterns']}
check('complete eight conclusion branches', full_actual == full_conclusion)
check('Legendre signs at 11', {x*x % 11 for x in range(1, 11)} == {1, 3, 4, 5, 9})
failures = [c for c in checks if not c['passed']]
result = {
    'scope': 'Independent finite-record audit; source theorems and valuation proof remain cited/written inputs.',
    'checks': checks, 'expected_records': expected,
    'complete_branch_residue_tuples': sorted(full_actual),
    'summary': {'source_subrows': [len(r2), len(r3)],
                'retained_records_checked': len(expected['retained_residue_patterns']),
                'rejected_records_checked': len(expected['rejected_residue_patterns']),
                'actual_branches': len({(r[0], r[1], r[2], r[4]) for r in full_actual}), 'required_branches': 8,
                'actual_labels': len({r[0] for r in full_actual}),
                'required_labels_for_exclusion': 0, 'failures': failures},
}
output = root / 'audit-certificate.json'
output.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result['summary']))
print(f'Full audit certificate: {output}')
raise SystemExit(bool(failures))
