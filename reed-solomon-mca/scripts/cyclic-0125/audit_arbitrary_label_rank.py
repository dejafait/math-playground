"""Independent complete certificate check; no imports from search scripts."""

from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from math import prod
from pathlib import Path

P = 97
HERE = Path(__file__).resolve().parent
PAIRS = list(combinations(range(8), 2))


def rref(matrix):
    a = [row[:] for row in matrix]
    pivots = []
    for col in range(len(a[0])):
        first = len(pivots)
        pivot = next((i for i in range(first, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[first], a[pivot] = a[pivot], a[first]
        scale = pow(a[first][col], P - 2, P)
        a[first] = [x * scale % P for x in a[first]]
        for i in range(len(a)):
            if i != first:
                factor = a[i][col]
                if factor:
                    a[i] = [(x - factor * y) % P for x, y in zip(a[i], a[first])]
        pivots.append(col)
    return a, pivots


def nullspace(matrix):
    a, pivots = rref(matrix)
    result = []
    for free in range(len(matrix[0])):
        if free not in pivots:
            v = [0] * len(matrix[0])
            v[free] = 1
            for i, col in enumerate(pivots):
                v[col] = -a[i][free] % P
            result.append(v)
    return result


def wedge(rows):
    return [[(a[j] * b[k] - a[k] * b[j]) % P for j, k in PAIRS]
            for a, b in combinations(rows, 2)]


def determinant_by_columns(matrix):
    """Column pivoting and successive Schur complements, no row swaps."""
    a = [row[:] for row in matrix]
    answer = 1
    while a:
        col = next((j for j, x in enumerate(a[0]) if x), None)
        if col is None:
            return 0
        if col != 0:
            for row in a:
                row[0], row[col] = row[col], row[0]
            answer = -answer
        pivot = a[0][0]
        answer = answer * pivot % P
        scale = pow(pivot, P - 2, P)
        a = [[(row[j] - row[0] * scale * a[0][j]) % P
              for j in range(1, len(a))] for row in a[1:]]
    return answer % P


def main():
    source = HERE / 'arbitrary-label-rank-result.json'
    data = json.loads(source.read_text())
    failures = []
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(message)

    H = [x for x in range(1, 97) if pow(x, 16, 97) == 1]
    check(len(H) == 16 and data['modulus'] == 97 and data['H'] == H, 'field and domain')
    check(data['column_pairs'] == [list(x) for x in PAIRS], 'column order')
    check(data['row_pairs'] == [list(x) for x in combinations(range(4), 2)], 'row pair order')
    cases = data['cases']
    check(0 < len(cases) <= 4096 and data['limit'] == 4096, 'bounded sample size')
    check(data['seed'] == 20261005042, 'recorded seed')
    check(len({tuple(c['labeling']) for c in cases}) == len(cases), 'distinct labelings')
    generators = [w for w in H if pow(w, 8, 97) != 1]
    check(len(cases) >= 8 and [c['labeling'] for c in cases[:8]] ==
          [[pow(w, t, P) for t in range(16)] for w in generators], 'all eight cyclic controls')

    independent_blocks = {}
    for key, block in data['support_blocks'].items():
        roots = block['support']
        check(len(roots) == 4 and len(set(roots)) == 4 and set(roots) <= set(H)
              and roots == sorted(roots) and key == ','.join(map(str, roots)), f'{key}: support')
        # Independent elementary symmetric sums, not factor multiplication.
        c = [(-1) ** (4 - j) * sum(prod(s) for s in combinations(roots, 4 - j)) % P
             for j in range(5)]
        polynomial_rows = [[0] * r + c + [0] * (3 - r) for r in range(4)]
        check(polynomial_rows == block['annihilator'], f'{key}: all polynomial coefficients')
        check(wedge(polynomial_rows) == block['matrix'], f'{key}: complete six-by-28 block')
        moment = [[pow(x, j + 1, P) for j in range(8)] for x in roots]
        basis = nullspace(moment)
        check(len(basis) == 4 and len(rref(polynomial_rows + basis)[1]) == 4,
              f'{key}: actual moment-nullspace agreement')
        independent_blocks[key] = wedge(basis)

    checked_minors = []
    control_ranks = []
    independent_exceptional = None
    used_keys = set()
    for index, case in enumerate(cases):
        label = case['labeling']
        check(sorted(label) == H, f'{index}: bijection')
        supports = [sorted(label[(t + a) % 16] for a in (0, 1, 2, 5)) for t in range(16)]
        keys = [','.join(map(str, support)) for support in supports]
        check(keys == case['support_keys'], f'{index}: all sixteen actual supports')
        used_keys.update(keys)
        check(set(supports[0]).isdisjoint(supports[6]), f'{index}: preserved disjoint pair')
        matrix = [row for key in keys for row in data['support_blocks'][key]['matrix']]
        selection = case['selected_rows']
        check(len(selection) == case['rank'] and len(set(selection)) == len(selection)
              and all(0 <= i < 96 for i in selection), f'{index}: row selection')
        if case['rank'] == 28:
            det = determinant_by_columns([matrix[i] for i in selection])
            check(det != 0 and det == case['minor_determinant'], f'{index}: exact maximal minor')
            checked_minors.append({'case_index': index, 'determinant': det})
        else:
            saved = data['exceptional']
            independent = [row for key in keys for row in independent_blocks[key]]
            reduced, pivots = rref(independent)
            kernel = nullspace(independent)
            check(index == len(cases) - 1 and saved['case_index'] == index,
                  f'{index}: stopped at first deficient case')
            check(matrix == saved['matrix'], f'{index}: complete saved matrix')
            original_reduced, original_pivots = rref(matrix)
            check(original_reduced == saved['reduced_matrix'] and original_pivots == saved['pivot_columns'],
                  f'{index}: complete saved reduction')
            check(len(pivots) == case['rank'] < 28 and len(original_pivots) == len(pivots),
                  f'{index}: independent exact rank')
            v = saved['kernel_vector']
            check(len(v) == 28 and any(v) and all(sum(x * y for x, y in zip(row, v)) % P == 0
                  for row in matrix + independent), f'{index}: nonzero kernel in both bases')
            check(bool(kernel), f'{index}: independently constructed kernel')
            independent_exceptional = {'case_index': index, 'labeling': label,
                                      'matrix': independent, 'reduced_matrix': reduced,
                                      'pivot_columns': pivots, 'kernel_basis': kernel}
        if index < 8:
            independent = [row for key in keys for row in independent_blocks[key]]
            actual = len(rref(independent)[1])
            check(actual == case['rank'] == 28, f'{index}: independent cyclic control rank')
            control_ranks.append(actual)
    check(used_keys == set(data['support_blocks']), 'every stored block used')
    summary = data['summary']
    check(summary['tested'] == len(cases) and summary['required_rank'] == 28,
          'actual and required counts')
    check(summary['rank_counts'] == {str(k): v for k, v in Counter(c['rank'] for c in cases).items()},
          'rank histogram')
    check(summary['origins'] == dict(Counter(c['origin'].split('-')[0] for c in cases)), 'origin histogram')
    check(summary['distinct_support_blocks'] == len(used_keys), 'support coverage count')
    deficient = [i for i, c in enumerate(cases) if c['rank'] < 28]
    check(deficient == ([] if summary['deficient_case'] is None else [summary['deficient_case']]),
          'deficiency summary')
    check(summary['universal_statement_decided'] == bool(deficient), 'no universality from sampling')
    check(summary['failures'] == [], 'search has no internal failures')
    if not deficient:
        check(len(cases) == 4096 and data['exceptional'] is None, 'full budget or first falsifier')
    report = {'source_sha256': sha256(source.read_bytes()).hexdigest(),
              'summary': {'tested': len(cases), 'required_rank': 28,
                          'verified_nonzero_maximal_minors': len(checked_minors),
                          'moment_nullspace_blocks_checked': len(used_keys),
                          'independent_control_ranks': control_ranks,
                          'independent_deficient_rank': None if independent_exceptional is None else
                          len(independent_exceptional['pivot_columns']),
                          'checks': checks, 'failures': failures,
                          'result': 'PASS' if not failures else 'FAIL'},
              'checked_minors': checked_minors, 'independent_support_blocks': independent_blocks,
              'independent_exceptional': independent_exceptional}
    output = HERE / 'arbitrary-label-rank-audit.json'
    output.write_text(json.dumps(report, separators=(',', ':')) + '\n')
    print(json.dumps(report['summary'], sort_keys=True))
    print(f'Full independent certificate: {output}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
