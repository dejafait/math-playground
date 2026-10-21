"""Independent full evidence audit for L056; never imports its producer.

Rebuild the group mathematically, check every binary-table entry against
permutation composition, then verify the entire finite completeness witness.
NumPy operations here are exact bounded integers; rank uses Fraction only.
"""
from fractions import Fraction
from itertools import product, permutations
from pathlib import Path
import hashlib
import json
import platform
import sys
import numpy as np

root = Path(__file__).resolve().parent
output = root / 'all-smaller-audit-certificate.json'
report = {'status': 'IN_PROGRESS', 'checks': [], 'failures': [],
          'inputs': {}, 'field_inputs': ['L051', 'L055'],
          'python': platform.python_version(), 'numpy': np.__version__}


def save():
    output.write_text(json.dumps(report, indent=2) + '\n')


def require(name, condition):
    report['checks'].append(name)
    if not bool(condition):
        report['failures'].append(name)
        report['status'] = 'FAILED'
        save()
        raise RuntimeError(name)


def read(name):
    data = (root / name).read_bytes()
    report['inputs'][name] = hashlib.sha256(data).hexdigest()
    return data


saved = json.loads(read('all-smaller-certificate.json'))
classes = [json.loads(x) for x in read('all-smaller-classes.jsonl').splitlines()]
conjugates = [json.loads(x) for x in read('all-smaller-conjugates.jsonl').splitlines()]
summary = json.loads(read('all-smaller-summary.json'))
require('entire class evidence equals main certificate', classes == saved['subgroup_classes'])
require('entire summary equals main certificate', summary == saved['enumeration'])
for name, digest in saved['backend']['sources'].items():
    require('source provenance ' + name, hashlib.sha256(read(name)).hexdigest() == digest)
for name, digest in saved['complete_conjugate_and_table_artifacts'].items():
    require('artifact provenance ' + name, hashlib.sha256(read(name)).hexdigest() == digest)


def parity(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p))) % 2


def mobius(m):
    a, b, c, d = m
    points = [(x, 1) for x in range(11)] + [(1, 0)]
    ans = []
    for x, y in points:
        num, den = (a*x+b*y) % 11, (c*x+d*y) % 11
        ans.append(11 if den == 0 else num*pow(den, -1, 11) % 11)
    return tuple(ans)


projective = {}
for m in product(range(11), repeat=4):
    determinant = (m[0]*m[3]-m[1]*m[2]) % 11
    if determinant == 0 or next(x for x in m if x) != 1:
        continue
    p = mobius(m)
    sign = 0 if pow(determinant, 5, 11) == 1 else 1
    require('matrix parity ' + str(m), parity(p) == sign)
    require('faithful projective matrix ' + str(m), p not in projective)
    projective[p] = m
require('all projective matrices', len(projective) == 1320)
expected = {p + tuple(12+x for x in s) for p in projective
            for s in permutations(range(3)) if parity(p) == parity(s)}
perms = [tuple(x) for x in saved['group']['all_disjoint_permutations']]
n = 3960
require('complete sign-compatible group and distinct entries',
        len(perms) == len(expected) == n and set(perms) == expected)
lookup = {p: i for i, p in enumerate(perms)}
ident = lookup[tuple(range(15))]
gens = [lookup[mobius(m)+tuple(12+x for x in s)] for m, s in [
    ((1, 1, 0, 1), (0, 1, 2)), ((1, 0, 1, 1), (0, 1, 2)),
    ((2, 0, 0, 1), (1, 0, 2)), ((1, 0, 0, 1), (1, 2, 0))]]
require('identity and all four generators',
        ident == saved['group']['identity'] == summary['identity'] and gens == saved['group']['generators'])
raw_group = list(map(int, read('all-smaller-group.txt').split()))
require('complete backend group input', raw_group == [n, ident]+gens+[x for p in perms for x in p])
target = [[3*p[a]+p[12+b]-12 for a, b in product(range(12), range(3))] for p in perms]
require('every target permutation', target == saved['group']['all_target_permutations'])
h = [i for i in range(n) if target[i][0] == 0]
require('actual target stabilizer and transitivity',
        h == saved['group']['target_stabilizer_elements'] and len(h) == 110 and
        {p[0] for p in target} == set(range(36)))
byteorder = saved['backend']['byteorder']
require('valid table byte order', byteorder in ('little', 'big'))
raw = read('all-smaller-multiplication.bin')
require('full table byte length', len(raw) == 2*n*n)
table = np.frombuffer(raw, dtype='<u2' if byteorder == 'little' else '>u2').reshape(n, n)
require('all table entries in group', np.all(table < n))
p_array = np.array(perms, dtype=np.uint8)
for a in range(n):
    require('all products in row ' + str(a), np.array_equal(p_array[table[a]], p_array[a][p_array]))
inv = np.array([lookup[tuple(p.index(i) for i in range(15))] for p in perms])
require('all two-sided inverses and identity rows',
        np.all(table[np.arange(n), inv] == ident) and np.all(table[inv, np.arange(n)] == ident)
        and np.array_equal(table[ident], np.arange(n)) and np.array_equal(table[:, ident], np.arange(n)))
# All subsequent table uses now refer to independently verified composition.
conj = table[table, inv[:, None]]


def generated(gs):
    # Fixed-point set expansion rather than the producer's queue traversal.
    current = np.array([ident], dtype=int)
    while gs:
        expanded = np.unique(np.concatenate((current, table[np.array(gs)[:, None], current].ravel())))
        if len(expanded) == len(current):
            return frozenset(map(int, expanded))
        current = expanded
    return frozenset([ident])


require('four generators exhaust group', len(generated(gens)) == n)
report['group'] = {'order': n, 'identity': ident, 'generators': gens,
                   'verified_products': n*n, 'target_stabilizer': h,
                   'all_permutations': perms, 'all_target_permutations': target}
print('Independent group and all 15,681,600 products verified.', flush=True)
save()
sets = [frozenset(c['elements']) for c in classes]
require('trivial initial representative', sets[0] == frozenset([ident]) and classes[0]['generators'] == [])
for k, c in enumerate(classes):
    require(f'subgroup {k}: complete generated set', c['class'] == k and
            len(c['elements']) == len(sets[k]) == c['order'] and generated(c['generators']) == sets[k])

audit_rows = []
for k, c in enumerate(classes):
    members = np.array(sorted(sets[k]), dtype=int)
    mask = np.zeros(n, dtype=bool)
    mask[members] = True
    # Test conjugation of EVERY subgroup member, not just its generators.
    normalizer = np.flatnonzero(np.all(mask[conj[:, members]], axis=1)).tolist()
    require(f'subgroup {k}: full normalizer', normalizer == c['normalizer_elements'] and
            generated(c['normalizer_generators']) == frozenset(normalizer))
    # Undirected connected components of all generating reduction edges.
    # Each edge is a bijection on a finite set, so these equal its full orbits.
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    edges = [table[g] for g in c['generators']] + [table[:, g] for g in c['generators']]
    edges += [conj[g] for g in c['normalizer_generators']]
    for edge in edges:
        for x, y in enumerate(edge):
            rx, ry = find(x), find(int(y))
            if rx != ry:
                parent[ry] = rx
    components = {}
    for x in range(n):
        components.setdefault(find(x), []).append(x)
    orbit_list = sorted(components.values(), key=lambda v: v[0])
    ext = c['extensions']
    require(f'subgroup {k}: every reducing orbit represented', len(ext) == len(orbit_list))
    ids = [-1]*n
    for i, orbit in enumerate(orbit_list):
        for x in orbit:
            ids[x] = i
        e = ext[i]
        require(f'subgroup {k} orbit {i}: representative and fusion range',
                e['element'] in orbit and 0 <= e['class'] < len(classes) and 0 <= e['conjugator'] < n)
        actual_extension = generated(c['generators']+[e['element']])
        rhs = frozenset(map(int, conj[e['conjugator'], sorted(sets[e['class']])]))
        require(f'subgroup {k} orbit {i}: entire generated extension and witness', actual_extension == rhs)
    require(f'subgroup {k}: complete orbit partition', ids == c['element_orbit_ids'])
    audit_rows.append({'class': k, 'elements': sorted(sets[k]), 'normalizer': normalizer,
                       'reducing_orbits': orbit_list, 'checked_extensions': ext})
    if k % 10 == 0:
        print(f'Full subgroup/frontier verification {k+1}/{len(classes)}.', flush=True)

all_sets = {}
by_class = [[] for _ in classes]
for i, c in enumerate(conjugates):
    k, w = c['class'], c['conjugator']
    s = frozenset(c['elements'])
    require(f'conjugate {i}: range and distinct complete set',
            0 <= k < len(classes) and 0 <= w < n and len(s) == len(c['elements']) and s not in all_sets)
    require(f'conjugate {i}: every element of witness', s == frozenset(map(int, conj[w, sorted(sets[k])])))
    all_sets[s] = k
    by_class[k].append(i)
for k, s in enumerate(sets):
    require(f'class {k}: representative included', all_sets.get(s) == k)
    require(f'class {k}: full orbit-stabilizer count',
            len(by_class[k])*len(audit_rows[k]['normalizer']) == n)
for i, c in enumerate(conjugates):
    for g in gens:
        s = frozenset(map(int, conj[g, c['elements']]))
        require(f'conjugate {i}: closure under generator {g}', all_sets.get(s) == c['class'])
require('full exhausted frontier and counts', summary['complete'] is True and
        len(classes) == summary['processed_classes'] == summary['discovered_classes'] == 67 and
        len(all_sets) == summary['actual_subgroups'] == 6906 and summary['group_order'] == n and summary['index_bound'] == 35)
report['enumeration'] = {'complete': True, 'class_count': len(classes),
                         'actual_subgroups': len(all_sets), 'classes': audit_rows,
                         'all_checked_conjugates': conjugates}
save()
print('All 67 classes, 6,906 conjugates and every extension verified.', flush=True)

qualifying = sorted((k for k, s in enumerate(sets) if n//len(s) < 36), key=lambda k: k)
require('exhaustive saved qualifying list', [q['class'] for q in saved['qualifying_subgroups']] == qualifying)
maps_report, columns = [], []
for q in saved['qualifying_subgroups']:
    k = q['class']
    js = sorted(sets[k])
    require(f'class {k}: nontrivial and index metadata', len(js) > 1 and n % len(js) == 0 and
            q['degree'] == n//len(js) and q['generators'] == classes[k]['generators'])
    cosets = sorted({tuple(sorted(map(int, table[g, js]))) for g in range(n)}, key=lambda v: v[0])
    require(f'class {k}: full distinct left cosets', len(cosets) == q['degree'] and
            sorted(x for s in cosets for x in s) == list(range(n)))
    reps = q['coset_representatives']
    reconstructed = [sorted(map(int, table[g, js])) for g in reps]
    require(f'class {k}: every saved coset and representative', reconstructed == q['cosets'] and
            len(reps) == len(cosets) and {tuple(s) for s in reconstructed} == set(cosets))
    orbits = sorted({tuple(sorted({target[j][x] for j in js})) for x in range(36)}, key=lambda v: v[0])
    require(f'class {k}: every J orbit on target', [list(o) for o in orbits] == q['target_subgroup_orbits'])
    matrices = []
    for orbit in orbits:
        images = [{target[g][x] for x in orbit} for g in reps]
        matrix = [[int(x in image) for image in images] for x in range(36)]
        matrices.append(matrix)
        columns.extend([list(col) for col in zip(*matrix)])
    require(f'class {k}: every entry of every orbital map', matrices == q['all_orbital_map_matrices'])
    maps_report.append({'class': k, 'degree': len(cosets), 'cosets': reconstructed,
                         'representatives': reps, 'orbits': orbits, 'maps': matrices})
require('complete seven classes and twelve maps with 121 columns',
        len(qualifying) == 7 and sum(len(q['maps']) for q in maps_report) == 12 and len(columns) == 121)
differences = [[v[3*a+b]-v[3*a]-v[b]+v[0] for a in range(12) for b in range(3)] for v in columns]
require('every mixed coordinate difference', all(x == 0 for row in differences for x in row))
# Independent exact elimination, with all rows and columns retained.
a = [[Fraction(x) for x in row] for row in zip(*columns)]
pivots, row = [], 0
for col in range(len(columns)):
    candidates = [i for i in range(row, 36) if a[i][col] != 0]
    if not candidates:
        continue
    i = candidates[-1]
    a[row], a[i] = a[i], a[row]
    p = a[row][col]
    a[row] = [v/p for v in a[row]]
    for i in range(36):
        if i != row:
            t = a[i][col]
            a[i] = [x-t*y for x, y in zip(a[i], a[row])]
    pivots.append(col)
    row += 1
rref = [[str(x) for x in r] for r in a]
require('entire exact reduced matrix and pivots', rref == saved['coverage']['exact_rref'] and
        pivots == saved['coverage']['pivot_columns'])
require('rank 14 against required 36 and complete metadata', row == saved['coverage']['actual_rank'] == 14 and
        saved['coverage']['required_rank'] == 36 and saved['coverage']['total_map_columns'] == 121 and
        saved['coverage']['complete'] is True and saved['coverage']['all_columns_have_zero_mixed_coordinate_differences'] is True)
report['qualifying_subgroups'] = maps_report
report['coverage'] = {'actual_rank': row, 'required_rank': 36, 'map_count': 12,
                       'column_count': len(columns), 'all_mixed_differences': differences,
                       'pivot_columns': pivots, 'exact_rref': rref}
report['verifier_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
report['status'] = 'VERIFIED'
save()
print(f'Independent audit: rank {row}, required 36; failures {len(report["failures"])}.')
print(f'Full certificate: {output.relative_to(root.parent.parent)}')
