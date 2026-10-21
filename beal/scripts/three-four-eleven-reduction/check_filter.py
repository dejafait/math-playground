"""Check only the finite necessary-residue filter; no point classification."""
import json
from pathlib import Path

odd_d = [-3, -1, 1, 3]
even_d = [-6, -2, 2, 6]
all_d = sorted(odd_d + even_d)
rows2 = [
    (1, 1, 7, [1, -3]), (1, 3, 7, [-1, 3]),
    (2, 0, 1, odd_d), (2, 0, 5, odd_d),
    (2, 0, 3, even_d), (2, 0, 7, even_d),
    (3, 2, 1, odd_d), (3, 2, 5, odd_d),
    (3, 2, 3, even_d), (3, 2, 7, even_d),
    (4, 1, 0, [-2, 6]), (4, 3, 0, [2, -6]),
    (5, 1, 2, even_d), (5, 3, 2, even_d),
    (6, 1, 6, even_d), (6, 3, 6, even_d),
    (7, 1, 4, [-2, 6]), (7, 3, 4, [2, -6]),
]
rows3 = [
    (1, 1, 2, [-3, 6]), (1, 8, 2, [3, -6]),
    (2, 0, 1, all_d), (2, 0, 2, all_d),
    (3, 3, 1, all_d), (3, 6, 1, all_d),
    (4, 3, 2, all_d), (4, 6, 2, all_d),
    (5, 1, 0, all_d), (5, 8, 0, all_d),
    (5, 2, 0, all_d), (5, 7, 0, all_d),
    (6, 4, 0, all_d), (6, 5, 0, all_d),
    (7, 1, 1, all_d), (7, 8, 1, all_d),
    (7, 4, 1, all_d), (7, 5, 1, all_d),
    (8, 2, 1, all_d), (8, 7, 1, all_d),
]
table3 = {
    (1, 4): '54a1', (1, 7): '54a1',
    **{(i, j): '288a1' for i in [2, 6] for j in [2, 6, 8]},
    **{(i, j): '864b1' for i in [2, 6] for j in [3, 5]},
    **{(i, j): '864a1' for i in [2, 6] for j in [4, 7]},
    **{(i, 1): '96a1' for i in [3, 5]},
    **{(i, j): '864c1' for i in [3, 5] for j in [3, 5]},
    (4, 3): '27a1', (4, 5): '27a1',
}

def compatible2(row):
    i, x, a, ds = row
    return {'i2': i, 'X_mod4': x, 'A_mod8': a, 'd': ds,
            'square_residue': x in {0, 1},
            'source_impossible': i == 7}

def compatible3(row):
    i, x, a, ds = row
    return {'i3': i, 'X_mod9': x, 'A_mod3': a, 'd': ds,
            'square_residue': x in {0, 1, 4, 7}}

retained, rejected = [], []
for B in range(36):
    for A in range(24):
        for i, x4, a8, ds2 in rows2:
            if i == 7 or B*B % 4 != x4 or A % 8 != a8:
                continue
            for j, x9, a3, ds3 in rows3:
                if B*B % 9 != x9 or A % 3 != a3:
                    continue
                label = table3.get((i, j))
                ds = sorted(set(ds2) & set(ds3))
                if label is None or not ds:
                    continue
                record = {'B_mod36': B, 'A_mod24': A, 'i2': i,
                          'i3': j, 'label': label, 'd': ds}
                if label in {'27a1', '288a1'}:
                    record['reason'] = 'cited unconditional CM exclusion'
                    rejected.append(record)
                elif label == '864a1' and (i == 6 or a8 in {1, 5}):
                    record['reason'] = 'anti-symplectic: FNS Lemma 5.2'
                    rejected.append(record)
                elif label == '864b1' and i == 2 and a8 in {3, 7}:
                    record['reason'] = 'anti-symplectic: FNS Lemma 5.2'
                    rejected.append(record)
                else:
                    retained.append(record)
branches = sorted({(r['label'], r['i2'], r['i3'], r['A_mod24'] % 8)
                   for r in retained})
required_branches = sorted([
    ('54a1', 1, 7, 7), ('96a1', 5, 1, 2),
    ('864a1', 2, 7, 3), ('864a1', 2, 7, 7),
    ('864b1', 2, 5, 1), ('864b1', 2, 5, 5),
    ('864b1', 6, 5, 6), ('864c1', 5, 5, 2),
])
failures = []
if branches != required_branches:
    failures.append('branch list mismatch')
if any(r['B_mod36'] % 3 == 0 for r in retained):
    failures.append('a retained branch allows 3 dividing B')
if any(r['label'] == '96a1' and r['B_mod36']**2 % 9 != 1
       for r in retained):
    failures.append('96a1 square residue mismatch')
certificate = {
    'scope': 'finite necessary filters, not local points or integer solutions',
    'source': 'FNS author final PDF, Tables 1-3 and Lemma 5.2 at p=11',
    'rows2': [compatible2(r) for r in rows2],
    'rows3': [compatible3(r) for r in rows3],
    'retained_residue_patterns': retained,
    'rejected_residue_patterns': rejected,
    'branches': branches, 'required_branches': required_branches,
    'summary': {'labels': sorted({r['label'] for r in retained}),
                'actual_branch_count': len(branches), 'expected_branch_count': 8,
                'actual_label_count': len({r['label'] for r in retained}),
                'required_labels_for_exclusion': 0, 'failures': failures},
}
output = Path(__file__).with_name('filter-certificate.json')
output.write_text(json.dumps(certificate, indent=2) + '\n')
print(json.dumps(certificate['summary']))
print(f'Full finite-filter certificate: {output}')
raise SystemExit(bool(failures))
