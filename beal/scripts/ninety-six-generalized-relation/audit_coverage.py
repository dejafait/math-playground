"""Independent audit of every load-bearing finite value in L055's certificate.

Does not import coverage.py. Group and orbital completeness are checked by
generator closure; discriminants are recomputed from the actual polynomials.
The field interpretation remains the canonical proof in L055.
"""
from fractions import Fraction as Q
from itertools import product, permutations
from math import isqrt
from pathlib import Path
import json

folder = Path(__file__).resolve().parent
saved = json.loads((folder / 'coverage-certificate.json').read_text())
failures = []
checks = []


def check(label, actual, expected):
    checks.append(label)
    if actual != expected:
        failures.append({'check': label, 'actual': actual, 'expected': expected})


def determinant(rows):
    a = [[Q(x) for x in row] for row in rows]
    d = Q(1)
    for k in range(len(a)):
        j = next((j for j in range(k, len(a)) if a[j][k]), None)
        if j is None:
            return 0
        if j != k:
            a[j], a[k] = a[k], a[j]
            d = -d
        pivot = a[k][k]
        d *= pivot
        for j in range(k + 1, len(a)):
            factor = a[j][k] / pivot
            a[j] = [x - factor*y for x, y in zip(a[j], a[k])]
    assert d.denominator == 1
    return int(d)


def discriminant(f):
    n = len(f)-1
    derivative = [(n-i)*f[i] for i in range(n)]
    rows = [[0]*i + f + [0]*(n-2-i) for i in range(n-1)]
    rows += [[0]*i + derivative + [0]*(n-1-i) for i in range(n)]
    return (-1)**(n*(n-1)//2)*determinant(rows)


m = [1, -4, 0, 0, 0, -264, 66, -132, -2112, -1320, -660, -6240, -8007]
h = [1, -4, -160, -1264]
discs = [discriminant(m), discriminant(h)]
roots = [isqrt(-d//11) for d in discs]
check('actual polynomial discriminants', discs,
      [saved['discriminants']['m'], saved['discriminants']['h']])
check('nonsquare classes', discs, [-11*r*r for r in roots])
check('saved discriminant square roots', roots, saved['discriminants']['square_roots'])


def mobius(matrix):
    a, b, c, d = matrix
    vectors = [(x, 1) for x in range(11)] + [(1, 0)]
    answer = []
    for x, y in vectors:
        num, den = (a*x+b*y) % 11, (c*x+d*y) % 11
        answer.append(11 if not den else num*pow(den, 9, 11) % 11)
    return tuple(answer)


def sign(p):
    # Cycle parity, independently of the source inversion count.
    unseen, cycles = set(range(len(p))), 0
    while unseen:
        x = min(unseen)
        cycles += 1
        while x in unseen:
            unseen.remove(x)
            x = p[x]
    return (len(p)-cycles) % 2


def compose(p, q):
    return tuple(p[x] for x in q)


def closure(gens):
    identity = tuple(range(len(gens[0])))
    queue, seen = [identity], {identity}
    for p in queue:
        for g in gens:
            q = compose(p, g)
            if q not in seen:
                seen.add(q)
                queue.append(q)
    return seen


normalized = set()
for matrix in product(range(11), repeat=4):
    a, b, c, d = matrix
    if (a*d-b*c) % 11:
        inverse = pow(next(x for x in matrix if x), 9, 11)
        normalized.add(tuple(x*inverse % 11 for x in matrix))
rows = []
for matrix in normalized:
    p = mobius(matrix)
    a, b, c, d = matrix
    determinant_sign = int(pow((a*d-b*c) % 11, 5, 11) != 1)
    check('cycle sign for '+str(matrix), sign(p), determinant_sign)
    rows.append({'matrix': list(matrix), 'permutation': list(p), 'parity': sign(p)})
rows.sort(key=lambda r: r['permutation'])
check('every normalized matrix and permutation', rows,
      saved['projective_group']['all_normalized_matrices_and_permutations'])
u, v, odd, diagonal = [mobius(a) for a in
                       [(1, 1, 0, 1), (1, 0, 1, 1), (2, 0, 0, 1), (2, 0, 0, 6)]]
psl = closure([u, v])
pgl = closure([u, v, odd])
check('generated PSL equals full even matrix set', sorted(psl),
      sorted(tuple(r['permutation']) for r in rows if r['parity'] == 0))
check('generated PGL equals full matrix set', sorted(pgl),
      sorted(tuple(r['permutation']) for r in rows))


def inverse(p):
    return tuple(p.index(x) for x in range(len(p)))


commutators = [compose(compose(compose(diagonal, g), inverse(diagonal)), inverse(g))
               for g in [u, v]]
check('commutators', commutators, [mobius((1, 3, 0, 1)), mobius((1, 0, 2, 1))])
check('commutators generate PSL', sorted(closure(commutators)), sorted(psl))


def joint_action(a, b):
    return tuple(3*a[i]+b[j] for i in range(12) for j in range(3))


id12, id3 = tuple(range(12)), (0, 1, 2)
generator_pairs = [(u, id3), (v, id3), (odd, (1, 0, 2)), (id12, (1, 2, 0))]
generators = [joint_action(a, b) for a, b in generator_pairs]
joint = closure(generators)
s3 = list(permutations(range(3)))
indices = [[i, j] for i, r in enumerate(rows) for j, b in enumerate(s3)
           if r['parity'] == sign(b)]
check('all joint index pairs', indices, saved['joint_group']['all_index_pairs'])
check('saved S3 order', [list(b) for b in s3], saved['joint_group']['S3_permutations'])
check('joint closure equals entire fiber product', sorted(joint),
      sorted(joint_action(rows[i]['permutation'], s3[j]) for i, j in indices))
check('group orders', [len(psl), len(pgl), len(joint)], [660, 1320, 3960])
check('saved group orders', [saved['projective_group'][k] for k in
      ['PSL_order', 'PGL_order', 'elementary_generated_order', 'commutator_generated_order']]
      + [saved['joint_group']['order']], [660, 1320, 660, 660, 3960])
check('target points', saved['joint_group']['target_points'],
      [[a, b] for a in range(12) for b in range(3)])
orbits = {}
for name, n, coordinate in [('K96', 12, 0), ('F', 3, 1)]:
    remaining, records = set(product(range(36), range(n))), []
    while remaining:
        seed = min(remaining)
        queue, orbit = [seed], {seed}
        for x, y in queue:
            for g, pair in zip(generators, generator_pairs):
                point = (g[x], pair[coordinate][y])
                if point not in orbit:
                    orbit.add(point)
                    queue.append(point)
        remaining -= orbit
        records.append({'representative': list(seed), 'size': len(orbit),
                        'pairs': [list(z) for z in sorted(orbit)],
                        'map_matrix': [[int((x, y) in orbit) for y in range(n)] for x in range(36)]})
    check('complete '+name+' orbits and maps', records, saved['all_composita'][name])
    check(name+' coordinate incidence', [r['map_matrix'] for r in records],
          [[[int((x//3 if coordinate == 0 else x % 3) == y) ^ unequal
             for y in range(n)] for x in range(36)] for unequal in [0, 1]])
    orbits[name] = records
for key, divisor in [('factor_degrees_over_L96', 36), ('factor_degrees_over_Q', 1)]:
    check(key, {k: [r['size']//divisor for r in rs] for k, rs in orbits.items()},
          saved['all_composita'][key])
maps = orbits['K96']+orbits['F']
matrix = [sum((r['map_matrix'][x] for r in maps), []) for x in range(36)]
check('full concatenated matrix', matrix, saved['coverage']['complete_map_matrix'])
a, pivots = [[Q(x) for x in row] for row in matrix], []
for column in range(30):
    row = len(pivots)
    pivot = next((i for i in range(row, 36) if a[i][column]), None)
    if pivot is None:
        continue
    a[row], a[pivot] = a[pivot], a[row]
    scale = a[row][column]
    a[row] = [x/scale for x in a[row]]
    for i in range(36):
        if i != row:
            scale = a[i][column]
            a[i] = [x-scale*y for x, y in zip(a[i], a[row])]
    pivots.append(column)
rref = [[str(x) for x in row] for row in a]
check('full exact rref', rref, saved['coverage']['exact_rref'])
check('pivot columns', pivots, saved['coverage']['pivot_columns'])
check('actual rank', len(pivots), 14)
check('saved dimensions', [saved['coverage'][k] for k in
      ['actual_rank', 'required_rank', 'missing_dimension']], [14, 36, 22])
witness = [1, -1, 0, -1, 1]+[0]*31
check('saved annihilator', saved['coverage']['annihilator'], witness)
check('annihilator on all columns', [sum(witness[i]*matrix[i][j] for i in range(36))
      for j in range(30)], [0]*30)
check('separated target basis', saved['coverage']['basis_vector_separated'], 0)
check('original failures', saved['failures'], [])
result = {'polynomials_descending': [m, h], 'discriminants': discs,
          'square_roots': roots, 'all_matrix_rows': rows,
          'all_generated_joint_permutations': [list(p) for p in sorted(joint)],
          'orbits': orbits, 'complete_matrix': matrix, 'rref': rref,
          'actual_rank': len(pivots), 'required_rank': 36, 'annihilator': witness,
          'checks': checks, 'failures': failures,
          'qualification': 'Finite evidence only; actual field identification is proved in L055.'}
path = folder / 'audit-certificate.json'
path.write_text(json.dumps(result, indent=2)+'\n')
print('Independent complete finite audit:', 'FAIL' if failures else 'PASS')
print('Discriminants:', discs)
print('PSL/PGL/joint orders:', len(psl), len(pgl), len(joint))
print('Actual/required map rank:', len(pivots), '/ 36; missing:', 36-len(pivots))
print('Failures:', len(failures), '; certificate:', path.relative_to(Path.cwd()))
if failures:
    raise SystemExit(1)
