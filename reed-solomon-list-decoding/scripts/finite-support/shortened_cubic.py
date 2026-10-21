#!/usr/bin/env python3
"""Bounded witness search and exact full graph verification; no avoidance claim."""
from itertools import combinations, product
from pathlib import Path
import json

P = 11
T = tuple(range(8))
OUT = Path(__file__).with_name('shortened-cubic-results.json')


def add(a, b):
    return ((a[0] + b[0]) % P, (a[1] + b[1]) % P)


def mul(a, b):
    return ((a[0]*b[0] + 2*a[1]*b[1]) % P,
            (a[0]*b[1] + a[1]*b[0]) % P)


def evaluate(cs, x):
    y = (0, 0)
    for c in reversed(cs):
        y = add(mul(y, (x, 0)), c)
    return y


def prime_eval(cs, x):
    return sum(c * pow(x, j, P) for j, c in enumerate(cs)) % P


def reduce_matrix(matrix):
    a = [row[:] for row in matrix]
    transform = [[int(i == j) for j in range(len(a))] for i in range(len(a))]
    pivots = []
    for col in range(len(a[0])):
        row = len(pivots)
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        transform[row], transform[pivot] = transform[pivot], transform[row]
        inverse = pow(a[row][col], -1, P)
        a[row] = [v * inverse % P for v in a[row]]
        transform[row] = [v * inverse % P for v in transform[row]]
        for i in range(len(a)):
            if i == row:
                continue
            scale = a[i][col]
            a[i] = [(v - scale*w) % P for v, w in zip(a[i], a[row])]
            transform[i] = [(v - scale*w) % P for v, w in zip(transform[i], transform[row])]
        pivots.append(col)
    basis = []
    for free in (i for i in range(len(a[0])) if i not in pivots):
        v = [0] * len(a[0])
        v[free] = 1
        for row, col in enumerate(pivots):
            v[col] = -a[row][free] % P
        basis.append(v)
    return a, transform, pivots, basis


def incidence_matrix(pairs):
    # Pair order: zeros of f, g, f-g, f+g. Signs retained in odd characteristic.
    matrix = []
    for (a, b), (sf, sg) in zip(pairs, ((1, 0), (0, 1), (1, -1), (1, 1))):
        for x in (a, b):
            powers = [pow(x, j, P) for j in range(4)]
            matrix.append([sf*v % P for v in powers] + [sg*v % P for v in powers])
    return matrix


def search():
    records = []
    for f_pair in combinations(T, 2):
        rem1 = tuple(x for x in T if x not in f_pair)
        for g_pair in combinations(rem1, 2):
            rem2 = tuple(x for x in rem1 if x not in g_pair)
            for minus_pair in combinations(rem2, 2):
                plus_pair = tuple(x for x in rem2 if x not in minus_pair)
                pairs = (f_pair, g_pair, minus_pair, plus_pair)
                matrix = incidence_matrix(pairs)
                reduced, transform, pivots, basis = reduce_matrix(matrix)
                records.append({'pairs': pairs, 'rank': len(pivots), 'tested_vectors': 0})
                if not basis:
                    continue
                # At most 11^3 vectors for any pattern; this is not exhaustive exclusion.
                for weights in product(range(P), repeat=min(len(basis), 3)):
                    if not any(weights):
                        continue
                    records[-1]['tested_vectors'] += 1
                    v = [sum(w*b[j] for w, b in zip(weights, basis)) % P for j in range(8)]
                    f, g = v[:4], v[4:]
                    polys = [f, g, [(a-b) % P for a,b in zip(f,g)],
                             [(a+b) % P for a,b in zip(f,g)]]
                    roots = [[x for x in T if prime_eval(cs, x) == 0] for cs in polys]
                    if roots == [list(pair) for pair in pairs]:
                        return records, {'pairs': pairs, 'matrix': matrix, 'rref': reduced,
                                         'transform': transform, 'pivots': pivots,
                                         'kernel_basis': basis, 'weights': weights, 'f': f, 'g': g,
                                         'root_sets': roots}
    return records, None


def main():
    checks = []
    def check(name, condition):
        checks.append({'name': name, 'pass': bool(condition)})

    squares = sorted({a*a % P for a in range(P)})
    check('11 is prime', all(P % d for d in range(2, P)))
    check('2 is nonsquare; u^2-2 irreducible', 2 not in squares)
    check('u^2=2 in quotient multiplication', mul((0,1), (0,1)) == (2,0))
    inverses = []
    for a, b in product(range(P), repeat=2):
        if (a,b) == (0,0):
            continue
        norm = (a*a - 2*b*b) % P
        check(f'nonzero norm {a},{b}', norm != 0)
        scale = pow(norm, -1, P)
        inv = (a*scale % P, -b*scale % P)
        inverses.append({'element': [a,b], 'norm': norm, 'inverse': inv})
        check(f'inverse {a},{b}', mul((a,b), inv) == (1,0))
    ground = {(x,(a,b)) for x in T for a,b in product(range(P), repeat=2)}
    deleted = {(0,(a,0)) for a in range(4)}
    omega = ground - deleted
    check('ground size 964', len(omega) == 964)
    family_size = (121 - 4) * 121**3
    check('family size 207272637', family_size == 207272637)

    search_records, witness = search()
    check('bounded search found a witness', witness is not None)
    if witness is not None:
        matrix = witness['matrix']
        transform = witness['transform']
        reproduced = [[sum(transform[i][k]*matrix[k][j] for k in range(8)) % P
                       for j in range(8)] for i in range(8)]
        check('entire transform times matrix is RREF', reproduced == witness['rref'])
        f, g = witness['f'], witness['g']
        prime_polys = [[0]*4, f, g, [(a+b) % P for a,b in zip(f,g)]]
        coefficients = [[(cs[0],1)] + [(c,0) for c in cs[1:]] for cs in prime_polys]
        values = [[evaluate(cs, x) for x in T] for cs in coefficients]
        blocks = [{(x,y) for x,y in zip(T,row)} for row in values]
        check('four distinct polynomials', len({tuple(cs) for cs in prime_polys}) == 4)
        check('four distinct blocks', len({frozenset(b) for b in blocks}) == 4)
        for i, block in enumerate(blocks):
            check(f'block {i+1} has eight points in Omega', len(block) == 8 and block <= omega)
            check(f'block {i+1} avoids four deleted points', not block & deleted)
        intersections = {}
        for i,j in combinations(range(4), 2):
            key = f'{i+1}{j+1}'
            intersections[key] = blocks[i] & blocks[j]
            check(f'edge {key} exactly two graph points', len(intersections[key]) == 2)
        for e1,e2 in combinations(intersections, 2):
            check(f'edge sets {e1},{e2} disjoint', not intersections[e1] & intersections[e2])
        private = [blocks[i] - set().union(*(blocks[j] for j in range(4) if j != i)) for i in range(4)]
        for i, part in enumerate(private):
            check(f'private part {i+1} exactly two', len(part) == 2)
        for indices in combinations(range(4), 3):
            check(f'triple intersection {indices} empty', not set.intersection(*(blocks[i] for i in indices)))
        check('union size 20', len(set.union(*blocks)) == 20)
        witness.update({'coefficient_order': 'ascending; each element [a,b] means a+b*u',
                        'coefficients': coefficients, 'evaluation_positions': T, 'values': values,
                        'blocks': [sorted(b) for b in blocks],
                        'intersections': {key: sorted(part) for key,part in intersections.items()},
                        'private_parts': [sorted(part) for part in private]})
    failures = [c['name'] for c in checks if not c['pass']]
    result = {'field': {'prime': P, 'modulus': 'u^2-2', 'squares': squares,
                        'inverse_certificates': inverses},
              'ground_size': len(omega), 'family_size': family_size,
              'pattern_requirement': {'pair_intersection_size': 2, 'private_part_size': 2,
                                      'pair_sets_mutually_disjoint': True},
              'search': {'scope': 'prescribed parallelogram subset only; no exhaustive exclusion',
                         'patterns_tested': len(search_records), 'records': search_records},
              'witness': witness, 'checks': checks, 'failures': failures,
              'conclusion': 'whole-pattern avoidance refuted' if witness is not None and not failures else 'inconclusive',
              'cap_comparison': 'not performed: avoidance prerequisite fails'}
    OUT.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'conclusion': result['conclusion'], 'patterns_tested': len(search_records),
                      'actual_ground_size': len(omega), 'required_ground_size': 964,
                      'actual_family_size': family_size, 'checks': len(checks),
                      'failures': failures, 'certificate': str(OUT)}, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
