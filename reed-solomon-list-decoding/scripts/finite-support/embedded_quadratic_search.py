"""Exact approved embedded-graph search; no symbolic/random rank inference."""
from itertools import combinations
from pathlib import Path
import json

P = 65537
AUX = 137
G = 19139
T = [16, 64, 70, 102, 112, 118, 121]
OUT = Path(__file__).with_name('embedded-quadratic-search-results.json')


def product(left, right):
    if not left:
        return []
    return [[sum(a*b for a, b in zip(row, col)) % P
             for col in zip(*right)] for row in left]


def rref(matrix, columns):
    rows = [row[:] for row in matrix]
    n = len(rows)
    transform = [[int(i == j) for j in range(n)] for i in range(n)]
    operations, pivots = [], []
    for col in range(columns):
        at = len(pivots)
        pivot = next((i for i in range(at, n) if rows[i][col]), None)
        if pivot is None:
            continue
        if pivot != at:
            rows[pivot], rows[at] = rows[at], rows[pivot]
            transform[pivot], transform[at] = transform[at], transform[pivot]
            operations.append(['swap', pivot, at])
        scale = pow(rows[at][col], -1, P)
        rows[at] = [x*scale % P for x in rows[at]]
        transform[at] = [x*scale % P for x in transform[at]]
        operations.append(['scale', at, scale])
        for i in range(n):
            if i == at or not rows[i][col]:
                continue
            factor = rows[i][col]
            rows[i] = [(x-factor*y) % P for x, y in zip(rows[i], rows[at])]
            transform[i] = [(x-factor*y) % P
                            for x, y in zip(transform[i], transform[at])]
            operations.append(['subtract', i, at, factor])
        pivots.append(col)
    return rows, transform, operations, pivots


def pair_map(i, j, d):
    result = []
    for power in range(3):
        row = [0]*(3*(d-1))
        if i < d-1:
            row[3*i+power] = 1
        if j < d-1:
            row[3*j+power] = P-1
        result.append(row)
    return result


def integer_determinant(matrix):
    """Fraction-free elimination on integer lifts, independent of modular RREF."""
    B = [row[:] for row in matrix]
    n, previous, sign, trace = len(B), 1, 1, []
    for k in range(n-1):
        at = next((i for i in range(k, n) if B[i][k]), None)
        if at is None:
            return 0, trace
        if at != k:
            B[k], B[at] = B[at], B[k]
            sign = -sign
        pivot = B[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = pivot*B[i][j]-B[i][k]*B[k][j]
                quotient, remainder = divmod(numerator, previous)
                if remainder:
                    raise ArithmeticError('nonexact Bareiss division')
                B[i][j] = quotient
        for i in range(k+1, n):
            B[i][k] = 0
        trace.append({'column': k, 'swap_row': at, 'pivot': pivot,
                      'previous_divisor': previous, 'matrix': [row[:] for row in B]})
        previous = pivot
    return sign*B[-1][-1], trace


def main():
    failures, checks = [], []

    def check(name, condition):
        checks.append({'check': name, 'passed': bool(condition)})
        if not condition:
            failures.append(name)
            raise ArithmeticError(name)

    pool = set((a, b, c) for a in [0, 1, 136] for b in [0, 1, 136]
               for c in [0, 1, 136])
    for a in range(4):
        for lam in range(1, 5):
            for u, v in combinations(T, 2):
                pool.add(((a+lam*u*v) % AUX, -lam*(u+v) % AUX, lam))
    pool = sorted(pool)
    graphs = [[(a+b*t+c*t*t) % AUX for t in T] for a, b, c in pool]
    exponents = [[61+137*i+y for i, y in enumerate(values)] for values in graphs]
    labels = [[pow(G, e, P) for e in es] for es in exponents]
    core = [pow(G, e, P) for e in range(61)]
    check('generator exact order 1024', pow(G, 1024, P) == 1
          and pow(G, 512, P) == P-1)
    check('embedding is injective and disjoint from core',
          len({pow(G, e, P) for e in range(1020)}) == 1020)
    check('pool graphs distinct', len({tuple(v) for v in graphs}) == len(pool))
    state = 137061
    draws, trials = [], []
    obstruction = None
    result = {'parameters': {'prime': P, 'auxiliary_prime': AUX, 'generator': G,
              'T': T, 'core': core, 'trial_limit': 512, 'size_limit': 8,
              'seed': state}, 'pool': pool, 'draws': draws, 'trials': trials,
              'checks': checks, 'failures': failures}

    def draw(b, phase, tied):
        nonlocal state
        state = (1664525*state+1013904223) % (2**32)
        index = state % len(tied)
        selected = tied[index]
        draws.append({'trial': b, 'phase': phase, 'state': state,
                      'eligible': tied, 'residue': index, 'selected': selected})
        return selected

    try:
        for b in range(512):
            d = 2+b % 7
            chosen = [draw(b, 'initial', list(range(len(pool))))]
            points = {(i, y) for i, y in enumerate(graphs[chosen[0]])}
            growth = []
            while len(chosen) < d:
                scores = {q: sum((i, y) in points for i, y in enumerate(graphs[q]))
                          for q in range(len(pool)) if q not in chosen}
                best = max(scores.values())
                tied = [q for q, value in scores.items() if value == best]
                q = draw(b, 'growth-'+str(len(chosen)), tied)
                chosen.append(q)
                points.update((i, y) for i, y in enumerate(graphs[q]))
                growth.append({'increase': best, 'tied': tied, 'selected': q})
            supports = [sorted(core+labels[q]) for q in chosen]
            shared = {}
            for i, q in enumerate(chosen):
                for x in labels[q]:
                    shared.setdefault(x, []).append(i)
            matrix, row_labels = [], []
            for x, incident in sorted(shared.items()):
                anchor = min(incident)
                for j in incident[1:]:
                    D = pair_map(anchor, j, d)
                    matrix.append([sum(pow(x, power, P)*D[power][col]
                                       for power in range(3)) % P
                                   for col in range(3*(d-1))])
                    row_labels.append({'point': x, 'anchor': anchor, 'other': j,
                                       'incident': incident})
            ncols = 3*(d-1)
            R, U, ops, pivots = rref(matrix, ncols)
            rank = len(pivots)
            check(f'trial {b}: complete elimination identity', product(U, matrix) == R)
            check(f'trial {b}: reduced echelon and complete zero residual',
                  all(R[i][p] == int(i == j) for j, p in enumerate(pivots)
                      for i in range(len(R)))
                  and all(not any(row) for row in R[rank:]))
            # Independently rebuild every incidence row by direct graph values.
            rebuilt = []
            for x in sorted(shared):
                incident = [i for i, q in enumerate(chosen) if x in labels[q]]
                for j in incident[1:]:
                    row = [0]*ncols
                    for i, sign in [(incident[0], 1), (j, -1)]:
                        if i < d-1:
                            for power, value in enumerate([1, x, x*x % P]):
                                row[3*i+power] = sign*value % P
                    rebuilt.append(row)
            check(f'trial {b}: direct incidence reconstruction', rebuilt == matrix)
            intersections = []
            for size in range(2, d+1):
                for indices in combinations(range(d), size):
                    intersection = sorted(set.intersection(*(set(supports[i])
                                                              for i in indices)))
                    intersections.append({'indices': indices, 'points': intersection})
            trial = {'trial': b, 'd': d, 'pool_indices': chosen,
                     'polynomials': [pool[q] for q in chosen], 'growth': growth,
                     'graph_values': [graphs[q] for q in chosen],
                     'label_exponents': [exponents[q] for q in chosen],
                     'outside_labels': [labels[q] for q in chosen],
                     'supports': supports, 'all_intersections': intersections,
                     'outside_intersections': [{'indices': item['indices'],
                                               'points': sorted(set(item['points'])-set(core))}
                                              for item in intersections],
                     'w': sum(max(len(indices)-1, 0) for indices in shared.values()),
                     'matrix': matrix, 'row_labels': row_labels, 'rref': R,
                     'row_transform': U, 'operations': ops, 'pivots': pivots,
                     'rank': rank, 'columns': ncols, 'pair_tests': []}
            trials.append(trial)
            check(f'trial {b}: supports have 68 distinct points',
                  all(len(s) == len(set(s)) == 68 for s in supports))
            check(f'trial {b}: row count equals incidence weight', len(matrix) == trial['w'])
            # All higher intersections independently reconstructed by column values.
            check(f'trial {b}: complete higher-intersection reconstruction',
                  all(item['points'] == sorted(core+[pow(G, 61+137*col+graphs[chosen[item['indices'][0]]][col], P)
                      for col in range(7)
                      if len({graphs[chosen[i]][col] for i in item['indices']}) == 1])
                      for item in intersections))
            replay = [row[:] for row in matrix]
            for operation in ops:
                if operation[0] == 'swap':
                    _, i, j = operation
                    replay[i], replay[j] = replay[j], replay[i]
                elif operation[0] == 'scale':
                    _, i, scalar = operation
                    check(f'trial {b}: invertible scale', scalar != 0)
                    replay[i] = [scalar*x % P for x in replay[i]]
                else:
                    _, i, j, factor = operation
                    replay[i] = [(x-factor*y) % P for x, y in zip(replay[i], replay[j])]
            check(f'trial {b}: complete operation replay', replay == R)
            if len(matrix) == ncols == rank:
                identity = [[int(i == j) for j in range(ncols)] for i in range(ncols)]
                check(f'trial {b}: both inverse identities',
                      product(U, matrix) == identity and product(matrix, U) == identity)
                det, trace = integer_determinant(matrix)
                trial['integer_determinant'] = det
                trial['bareiss_trace'] = trace
                trial['determinant_mod_prime'] = det % P
                modular_det = 1
                for operation in ops:
                    if operation[0] == 'swap':
                        modular_det = -modular_det % P
                    elif operation[0] == 'scale':
                        modular_det = modular_det*pow(operation[2], -1, P) % P
                check(f'trial {b}: independent integer determinant',
                      det % P == modular_det != 0)
            for i, j in combinations(range(d), 2):
                D = pair_map(i, j, d)
                augmented = matrix+D
                AR, AU, aops, apivots = rref(augmented, ncols)
                check(f'trial {b}: pair {i},{j} augmented identity',
                      product(AU, augmented) == AR
                      and all(not any(row) for row in AR[len(apivots):])
                      and all(AR[r][p] == int(r == t) for t, p in enumerate(apivots)
                              for r in range(len(AR))))
                test = {'pair': [i, j], 'map': D, 'augmented_rank': len(apivots),
                        'augmented_matrix': augmented,
                        'augmented_rref': AR, 'augmented_transform': AU,
                        'augmented_operations': aops, 'augmented_pivots': apivots}
                trial['pair_tests'].append(test)
                if len(apivots) == rank:
                    W = [[sum(row[p]*U[t][c] for t, p in enumerate(pivots)) % P
                          for c in range(len(matrix))] for row in D]
                    check(f'trial {b}: pair {i},{j} exact row-space identity',
                          product(W, matrix) == D)
                    test['row_space_witness'] = W
                    if obstruction is None:
                        obstruction = {'trial': b, 'pair': [i, j],
                                       'rank': rank, 'columns': ncols,
                                       'row_space_witness': W, 'difference_map': D}
            if obstruction is not None:
                break
        result['obstruction'] = obstruction
        result['summary'] = {'trials': len(trials), 'pool_size': len(pool),
                             'draw_count': len(draws), 'checks': len(checks),
                             'failed_checks': len(failures),
                             'stop': 'verified obstruction' if obstruction else '512 trials exhausted',
                             'rank_rows_columns': [[t['rank'], len(t['matrix']), t['columns']]
                                                   for t in trials]}
    finally:
        OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result['summary'], sort_keys=True))
    print('actual required pair-rank increment: 0 / positive; obstruction:',
          None if obstruction is None else {k: obstruction[k]
                                           for k in ['trial', 'pair', 'rank', 'columns']})
    print('failures:', failures, '; full certificate:', OUT)


if __name__ == '__main__':
    main()
