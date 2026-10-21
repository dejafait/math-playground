#!/usr/bin/env python3
"""Bounded exact witness search on the approved fixed T; no exclusion claim."""
from itertools import combinations, product
from pathlib import Path
import json
import random

OUT = Path(__file__).with_name('nonprime-cubic-results.json')
T = (0, 1, 2, 3, 4, 5, 6, 11)  # integer a+11*b encodes a+b*u
EDGES = tuple(combinations(range(4), 2))
PAIRS = tuple(combinations(T, 2))
LIMIT = 10000
SEED = 20261008101


def add(a, b):
    return (a % 11 + b % 11) % 11 + 11 * ((a // 11 + b // 11) % 11)


def neg(a):
    return (-(a % 11)) % 11 + 11 * ((-(a // 11)) % 11)


def mul(a, b):
    x, y, z, w = a % 11, a // 11, b % 11, b // 11
    return (x*z + 2*y*w) % 11 + 11 * ((x*w + y*z) % 11)


ADD = [[add(a, b) for b in range(121)] for a in range(121)]
MUL = [[mul(a, b) for b in range(121)] for a in range(121)]
NEG = [neg(a) for a in range(121)]
INV = [0] + [next(b for b in range(1, 121) if MUL[a][b] == 1) for a in range(1, 121)]


def total(xs):
    s = 0
    for x in xs:
        s = ADD[s][x]
    return s


def evaluate(cs, x):
    y = 0
    for c in reversed(cs):
        y = ADD[MUL[y][x]][c]
    return y


def polynomial_product(f, g):
    out = [0]*(len(f)+len(g)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(g):
            out[i+j] = ADD[out[i+j]][MUL[a][b]]
    return out


POWERS = {x: [1, x, MUL[x][x], MUL[MUL[x][x]][x]] for x in T}


def reduce_matrix(matrix):
    a = [row[:] for row in matrix]
    n, m = len(a), len(a[0])
    transform = [[int(i == j) for j in range(n)] for i in range(n)]
    pivots = []
    for col in range(m):
        r = len(pivots)
        pivot = next((i for i in range(r, n) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        transform[r], transform[pivot] = transform[pivot], transform[r]
        scale = INV[a[r][col]]
        a[r] = [MUL[v][scale] for v in a[r]]
        transform[r] = [MUL[v][scale] for v in transform[r]]
        for i in range(n):
            if i == r or not a[i][col]:
                continue
            scale = a[i][col]
            a[i] = [ADD[v][NEG[MUL[scale][w]]] for v, w in zip(a[i], a[r])]
            transform[i] = [ADD[v][NEG[MUL[scale][w]]] for v, w in zip(transform[i], transform[r])]
        pivots.append(col)
    basis = []
    for free in (i for i in range(m) if i not in pivots):
        v = [0] * m
        v[free] = 1
        for r, col in enumerate(pivots):
            v[col] = NEG[a[r][free]]
        basis.append(v)
    return a, transform, pivots, basis


def incidence(cs):
    values = [[evaluate(p, x) for x in T] for p in cs]
    blocks = [{(x, y) for x, y in zip(T, row)} for row in values]
    intersections = [blocks[i] & blocks[j] for i, j in EDGES]
    private = [blocks[i] - set().union(*(blocks[j] for j in range(4) if i != j)) for i in range(4)]
    deleted = {(0, a) for a in range(4)}
    return {'coefficients': cs, 'values': values, 'blocks': [sorted(b) for b in blocks],
            'intersections': {f'{i+1}{j+1}': sorted(s) for (i,j), s in zip(EDGES, intersections)},
            'private_parts': [sorted(s) for s in private],
            'pair_sizes': [len(s) for s in intersections],
            'pair_sets_mutually_disjoint': all(not a & b for a,b in combinations(intersections, 2)),
            'private_sizes': [len(s) for s in private],
            'distinct_blocks': len({frozenset(b) for b in blocks}) == 4,
            'deleted_points_avoided': all(not b & deleted for b in blocks),
            'union_size': len(set.union(*blocks))}


def valid(w, shortening=True):
    return (w['pair_sizes'] == [2]*6 and w['pair_sets_mutually_disjoint']
            and w['private_sizes'] == [2]*4 and w['distinct_blocks']
            and (w['deleted_points_avoided'] or not shortening))


def shifted(cs):
    for h in range(121):
        candidate = [[ADD[p[0]][h]] + p[1:] for p in cs]
        w = incidence(candidate)
        if valid(w):
            w['common_constant_shift'] = h
            return w
    return None


def kernel_candidates(basis, rng):
    # Every basis vector, then at most 32 combinations. A miss is inconclusive.
    for b in basis:
        yield b
    if len(basis) > 1:
        for _ in range(32):
            weights = [rng.randrange(121) for _ in basis]
            yield [total(MUL[w][b[j]] for w,b in zip(weights, basis)) for j in range(len(basis[0]))]


def search(rng):
    records = []
    # A disjoint four-pair partition tests only the parallelogram subclass.
    for fp in PAIRS:
        rem1 = tuple(x for x in T if x not in fp)
        for gp in combinations(rem1, 2):
            rem2 = tuple(x for x in rem1 if x not in gp)
            for mp in combinations(rem2, 2):
                pp = tuple(x for x in rem2 if x not in mp)
                pairs = (fp, gp, mp, pp)
                matrix = []
                for pair, (sf, sg) in zip(pairs, ((1,0),(0,1),(1,10),(1,1))):
                    for x in pair:
                        matrix.append([MUL[sf][v] for v in POWERS[x]] + [MUL[sg][v] for v in POWERS[x]])
                reduced, transform, pivots, basis = reduce_matrix(matrix)
                records.append({'scope': 'parallelogram', 'pairs': pairs, 'rank': len(pivots)})
                for v in kernel_candidates(basis, rng):
                    f, g = v[:4], v[4:]
                    cs = [[0]*4, f, g, [ADD[a][b] for a,b in zip(f,g)]]
                    if valid(incidence(cs), shortening=False):
                        w = shifted(cs)
                        if w:
                            return records, w, {'matrix': matrix, 'rref': reduced, 'transform': transform,
                                                'pivots': pivots, 'basis': basis, 'vector': v, 'pairs': pairs}
    # General K4 assignments: incident pairs disjoint; opposite pairs may reuse x.
    for trial in range(LIMIT):
        occupied = [set() for _ in range(4)]
        pairs = []
        for i,j in EDGES:
            choices = [pair for pair in PAIRS if not set(pair) & (occupied[i] | occupied[j])]
            if not choices:
                break
            pair = rng.choice(choices)
            pairs.append(pair)
            occupied[i].update(pair)
            occupied[j].update(pair)
        if len(pairs) != 6:
            records.append({'scope': 'general', 'trial': trial, 'pairs': pairs, 'incomplete': True})
            continue
        matrix = []
        for (i,j), pair in zip(EDGES, pairs):
            for x in pair:
                row = [0]*12
                for vertex, sign in ((i,1),(j,10)):
                    if vertex < 3:
                        row[4*vertex:4*vertex+4] = [MUL[sign][v] for v in POWERS[x]]
                matrix.append(row)
        reduced, transform, pivots, basis = reduce_matrix(matrix)
        records.append({'scope': 'general', 'trial': trial, 'pairs': pairs, 'rank': len(pivots)})
        for v in kernel_candidates(basis, rng):
            cs = [v[4*i:4*i+4] for i in range(3)] + [[0]*4]
            if valid(incidence(cs), shortening=False):
                w = shifted(cs)
                if w:
                    return records, w, {'matrix': matrix, 'rref': reduced, 'transform': transform,
                                        'pivots': pivots, 'basis': basis, 'vector': v, 'pairs': pairs}
    return records, None, None


def main():
    old = incidence([[11,0,0,0],[11,2,9,0],[12,4,4,1],[12,6,2,1]])
    records, witness, linear = search(random.Random(SEED))
    checks = []
    def check(name, result):
        checks.append({'name': name, 'pass': bool(result)})
    check('2 nonsquare in F_11', 2 not in {a*a % 11 for a in range(11)})
    check('eight distinct evaluation points', len(set(T)) == 8)
    for a in range(1,121):
        check(f'field inverse {a}', MUL[a][INV[a]] == 1)
    if witness:
        check('all whole-pattern and shortening requirements', valid(witness))
        check('union has twenty graph points', witness['union_size'] == 20)
        matrix, transform = linear['matrix'], linear['transform']
        reproduced = [[total(MUL[transform[i][k]][matrix[k][j]] for k in range(len(matrix)))
                       for j in range(len(matrix[0]))] for i in range(len(matrix))]
        check('complete transformation identity', reproduced == linear['rref'])
        for k, v in enumerate(linear['basis'] + [linear['vector']]):
            check(f'complete kernel identity {k}', all(total(MUL[a][b] for a,b in zip(row,v)) == 0 for row in matrix))
        for i,j in EDGES:
            check(f'complete intersection {i+1}{j+1}', len(witness['intersections'][f'{i+1}{j+1}']) == 2)
        for e1,e2 in combinations(witness['intersections'], 2):
            part1 = {tuple(point) for point in witness['intersections'][e1]}
            part2 = {tuple(point) for point in witness['intersections'][e2]}
            check(f'disjoint complete edge sets {e1},{e2}', not part1 & part2)
        for i,part in enumerate(witness['private_parts']):
            check(f'private part {i+1}', len(part) == 2)
        for i,cs in enumerate(witness['coefficients']):
            check(f'block {i+1} avoids deletion at zero', cs[0] not in range(4))
            for j,x in enumerate(T):
                check(f'independent direct evaluation {i+1},{j}', total(MUL[c][p] for c,p in zip(cs,POWERS[x])) == witness['values'][i][j])
        f, g = linear['vector'][:4], linear['vector'][4:]
        factors = {'f': polynomial_product(polynomial_product([0,1],[10,1]),[1,1]),
                   'g': polynomial_product(polynomial_product([9,1],[8,1]),[4,1]),
                   'f_minus_g': polynomial_product([7,1],[6,1]),
                   'f_plus_g': [MUL[2][c] for c in polynomial_product([5,1],[9,0,1])]}
        check('factorization f', factors['f'] == f)
        check('factorization g', factors['g'] == g)
        check('factorization f-g', factors['f_minus_g'] + [0] == [ADD[a][NEG[b]] for a,b in zip(f,g)])
        check('factorization f+g', factors['f_plus_g'] == [ADD[a][b] for a,b in zip(f,g)])
        witness['factorization_coefficients'] = factors
    failures = [c['name'] for c in checks if not c['pass']]
    result = {'encoding': 'integer a+11*b represents a+b*u; all entries reduced in F_11[u]/(u^2-2)',
              'evaluation_positions': T, 'deleted_points': [[0,a] for a in range(4)],
              'field_inverses': [{'element': a, 'inverse': INV[a]} for a in range(1,121)],
              'old_coefficients_diagnostic': old,
              'search': {'seed': SEED, 'general_trial_limit': LIMIT, 'records': records,
                         'scope': 'bounded parallelogram and sampled general K4 assignments; no complete exclusion'},
              'linear_certificate': linear, 'witness': witness, 'checks': checks, 'failures': failures,
              'conclusion': 'whole-pattern avoidance refuted' if witness and not failures else 'inconclusive',
              'cap_comparison': 'not performed'}
    OUT.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'conclusion': result['conclusion'], 'assignments_tested': len(records),
                      'actual_pair_sizes': witness['pair_sizes'] if witness else None, 'required_pair_sizes': [2]*6,
                      'actual_private_sizes': witness['private_sizes'] if witness else None, 'required_private_sizes': [2]*4,
                      'checks': len(checks), 'failures': failures, 'certificate': str(OUT)}, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
