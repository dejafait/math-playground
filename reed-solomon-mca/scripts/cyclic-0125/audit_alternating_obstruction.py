"""Independent L026 audit: no imports from the certificate generator."""

from hashlib import sha256
from itertools import combinations
import json
from math import prod
from pathlib import Path

P = 97
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
PAIRS = list(combinations(range(8), 2))
ROW_PAIRS = list(combinations(range(4), 2))


def reduce_matrix(matrix):
    a = [[x % P for x in row] for row in matrix]
    pivots = []
    for col in range(len(a[0])):
        row = next((i for i in range(len(pivots), len(a)) if a[i][col]), None)
        if row is None:
            continue
        k = len(pivots)
        a[k], a[row] = a[row], a[k]
        scale = pow(a[k][col], P - 2, P)
        a[k] = [x * scale % P for x in a[k]]
        for i in range(len(a)):
            if i != k:
                factor = a[i][col]
                a[i] = [(x - factor * y) % P for x, y in zip(a[i], a[k])]
        pivots.append(col)
    return a, pivots


def nullspace(matrix):
    reduced, pivots = reduce_matrix(matrix)
    result = []
    for free in range(len(matrix[0])):
        if free not in pivots:
            v = [0] * len(matrix[0])
            v[free] = 1
            for i, pivot in enumerate(pivots):
                v[pivot] = -reduced[i][free] % P
            result.append(v)
    return result


def determinant(matrix):
    # Recursive cofactor expansion, distinct from the generator's permutations.
    if not matrix:
        return 1
    return sum((-1) ** j * x * determinant(
        [row[:j] + row[j + 1:] for row in matrix[1:]])
        for j, x in enumerate(matrix[0])) % P


def coefficients(roots):
    # Elementary symmetric functions, not repeated multiplication of factors.
    return [(-1) ** (4 - j) * sum(prod(s) for s in combinations(roots, 4 - j)) % P
            for j in range(5)]


def alternating(rows):
    return [[(a[j] * b[k] - a[k] * b[j]) % P for j, k in PAIRS]
            for a, b in combinations(rows, 2)]


def main():
    source = HERE / 'alternating-obstruction-result.json'
    original = json.loads(source.read_text())
    lemma_path = ROOT / 'lemmas/L026-cyclic-0125-affine-support-exclusion.md'
    lemma = lemma_path.read_text()
    table_rows = [[cell.strip() for cell in line.strip('|').split('|')]
                  for line in lemma.splitlines() if line.startswith('| ')]
    coefficient_table = {int(row[0]): list(map(int, row[1:]))
                         for row in table_rows if len(row) == 6 and row[0].isdigit()}
    minor_table = {int(row[0]): (list(map(int, row[1].split(','))),
                               list(map(int, row[2:])))
                   for row in table_rows if len(row) == 10 and row[0].isdigit()}
    failures = []
    checks = 0

    def check(condition, label):
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(label)

    # Exact multiplicative order, rather than relying on the supplied list.
    generators = [w for w in range(1, P)
                  if next(d for d in range(1, P) if pow(w, d, P) == 1) == 16]
    check(len(generators) == 8, 'exactly eight generators')
    check(original['modulus'] == P and original['generators'] == generators,
          'base field and generator list')
    check(original['row_pairs'] == [list(p) for p in ROW_PAIRS], 'row pair order')
    compact = original['proof_certificate']
    check(compact['generators'] == generators and compact['row_pairs'] == original['row_pairs'],
          'compact generator and row data')
    check(len(original['blocks']) == len(compact['minors']) == 13, 'all thirteen blocks')
    check(set(coefficient_table) == set(generators) and set(minor_table) == set(range(1, 14)),
          'printed table coverage')
    reports = []
    for wi, w in enumerate(generators):
        roots = [pow(w, a, P) for a in (0, 1, 2, 5)]
        c = coefficients(roots)
        check(c == original['coefficients_ascending'][str(w)] == compact['coefficients'][str(w)]
              == coefficient_table[w], f'{w}: coefficient tables')
        base_rows = [[0] * r + c + [0] * (3 - r) for r in range(4)]
        base_wedges = alternating(base_rows)
        minors = []
        for h in range(1, 14):
            selected_columns = [i for i, pair in enumerate(PAIRS) if sum(pair) == h]
            block = [[row[i] for i in selected_columns] for row in base_wedges]
            recorded = original['blocks'][h - 1]
            small = compact['minors'][h - 1]
            rows, displayed_dets = minor_table[h]
            pairs = [list(PAIRS[i]) for i in selected_columns]
            minor = [block[i] for i in rows]
            det = determinant(minor)
            check(recorded['h'] == small['h'] == h and recorded['columns'] == small['columns'] == pairs
                  and recorded['selected_rows'] == small['rows'] == rows, f'{w}/{h}: block indices')
            saved = recorded['by_generator'][str(w)]
            check(saved['matrix'] == block and saved['minor'] == minor, f'{w}/{h}: full block and minor')
            check(det == saved['determinant'] == small['determinants'][wi] == displayed_dets[wi]
                  and det != 0, f'{w}/{h}: nonzero determinant and both tables')
            minors.append({'h': h, 'matrix': block, 'rows': rows, 'minor': minor, 'determinant': det})
        direct = []
        independent = []
        supports = []
        nullspaces = []
        for t in range(16):
            support = [pow(w, (a + t) % 16, P) for a in (0, 1, 2, 5)]
            supports.append(support)
            moment_transpose = [[pow(x, j + 1, P) for j in range(8)] for x in support]
            annihilator = nullspace(moment_transpose)
            nullspaces.append(annihilator)
            check(len(annihilator) == 4 and all(sum(x * y for x, y in zip(row, col)) % P == 0
                  for row in annihilator for col in moment_transpose), f'{w}/{t}: actual moment nullspace')
            independent.extend(alternating(annihilator))
            ct = coefficients(support)
            rt = [[0] * r + ct + [0] * (3 - r) for r in range(4)]
            check(len(reduce_matrix(rt + annihilator)[1]) == 4, f'{w}/{t}: annihilator row spaces agree')
            wedges = alternating(rt)
            direct.extend(wedges)
            check(all(wedges[ri][ci] == base_wedges[ri][ci] *
                      pow(w, ((8 + r + s - j - k) * t) % 16, P) % P
                      for ri, (r, s) in enumerate(ROW_PAIRS) for ci, (j, k) in enumerate(PAIRS)),
                  f'{w}/{t}: every coefficient in scaling identity')
        check(set(supports[0]).isdisjoint(supports[6]), f'{w}: disjoint pair')
        eight_columns = [[pow(x, j + 1, P) for j in range(8)]
                         for x in supports[0] + supports[6]]
        check(len(reduce_matrix(eight_columns)[1]) == 8, f'{w}: disjoint pair moment independence')
        direct_rank = len(reduce_matrix(direct)[1])
        reduced, pivots = reduce_matrix(independent)
        saved_direct = original['direct_checks'][str(w)]
        check(saved_direct['matrix'] == direct and saved_direct['rank'] == direct_rank == 28
              and saved_direct['required_rank'] == 28 and saved_direct['scaling_verified'] is True,
              f'{w}: complete original matrix and rank claims')
        check(len(pivots) == 28, f'{w}: independent nullspace rank')
        reports.append({'generator': w, 'coefficients': c, 'minors': minors,
                        'supports': supports, 'moment_nullspaces': nullspaces,
                        'independent_constraint_matrix': independent,
                        'independent_reduced_matrix': reduced, 'pivots': pivots,
                        'actual_rank': len(pivots), 'required_rank': 28})
    check(original['failures'] == [], 'original failures')
    summary = {'generators': generators, 'nonzero_minors_verified': sum(
        m['determinant'] != 0 for r in reports for m in r['minors']),
        'required_minors': 104, 'independent_ranks': [r['actual_rank'] for r in reports],
        'required_rank_each': 28, 'complete_original_matrices_compared': 8,
        'checks': checks, 'failures': failures,
        'result': 'PASS' if not failures else 'FAIL'}
    report = {'summary': summary, 'source_sha256': sha256(source.read_bytes()).hexdigest(),
              'lemma_at_audit_sha256': sha256(lemma_path.read_bytes()).hexdigest(), 'generators': reports}
    output = HERE / 'alternating-obstruction-audit.json'
    output.write_text(json.dumps(report, indent=2) + '\n')
    print(f"{summary['result']}: minors {summary['nonzero_minors_verified']}/104; "
          f"independent ranks {summary['independent_ranks']}, required 28 each; "
          f"checks {checks}; failures {failures}")
    print(f'Full certificate: {output}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
