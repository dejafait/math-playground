"""Independent moment-nullspace and determinant checks; imports no search code."""
from itertools import combinations
import json
from pathlib import Path

P = 97
HERE = Path(__file__).resolve().parent
CP = list(combinations(range(8), 2))
RP = list(combinations(range(4), 2))


def reduce_rows(rows):
    a = [[v % P for v in row] for row in rows]
    pivot_cols = []
    for col in range(len(a[0])):
        start = len(pivot_cols)
        choices = [i for i in range(start, len(a)) if a[i][col] != 0]
        if not choices:
            continue
        chosen = choices[-1]
        a[start], a[chosen] = a[chosen], a[start]
        divisor = a[start][col]
        for j in range(len(a[start])):
            a[start][j] = a[start][j] * pow(divisor, P - 2, P) % P
        for i in range(len(a)):
            if i == start:
                continue
            scale = a[i][col]
            for j in range(len(a[i])):
                a[i][j] = (a[i][j] - scale * a[start][j]) % P
        pivot_cols.append(col)
    return a[:len(pivot_cols)], pivot_cols


def moment_annihilator(labels):
    moment_transpose = [[pow(x, j + 1, P) for j in range(8)] for x in labels]
    reduced, pivots = reduce_rows(moment_transpose)
    assert len(pivots) == 4
    nullspace = []
    for free in range(8):
        if free in pivots:
            continue
        vector = [0] * 8
        vector[free] = 1
        for i, col in enumerate(pivots):
            vector[col] = -reduced[i][free] % P
        nullspace.append(vector)
    assert len(nullspace) == 4
    return nullspace


def wedge(rows):
    return [[(rows[r][j] * rows[s][k] - rows[r][k] * rows[s][j]) % P
             for j, k in CP] for r, s in RP]


def exact_polynomial_rows(labels):
    # Elementary symmetric coefficients, independent of search multiplication.
    elementary = []
    for size in range(5):
        total = 0
        for subset in combinations(labels, size):
            product = 1
            for x in subset:
                product *= x
            total += product
        elementary.append(total % P)
    coefficients = [(-1) ** (4 - j) * elementary[4 - j] % P for j in range(5)]
    return [[coefficients[j - r] if 0 <= j - r <= 4 else 0
             for j in range(8)] for r in range(4)]


def column_determinant(rows):
    # Column operations, unlike search's row elimination.
    a = [row[:] for row in rows]
    n = len(a)
    sign, product = 1, 1
    for i in range(n):
        candidates = [j for j in range(i, n) if a[i][j]]
        if not candidates:
            return 0
        j = candidates[-1]
        if j != i:
            for row in a:
                row[i], row[j] = row[j], row[i]
            sign = -sign
        pivot = a[i][i]
        product = product * pivot % P
        for j in range(i + 1, n):
            factor = a[i][j] * pow(pivot, P - 2, P) % P
            for k in range(i, n):
                a[k][j] = (a[k][j] - factor * a[k][i]) % P
    return sign * product % P


def main():
    plan = json.loads((HERE / 'plan.json').read_text())
    result = json.loads((HERE / 'result.json').read_text())
    failures, checked = [], []
    families = {f['id']: f for f in plan['families']}
    assert plan['column_pairs'] == [list(p) for p in CP]
    assert plan['row_pairs'] == [list(p) for p in RP]
    assert plan['H'] == [x for x in range(1, P) if pow(x, 16, P) == 1]
    assert pow(8, 16, P) == 1 and pow(8, 8, P) != 1
    assert len(plan['cases']) == 252 <= plan['limit'] == 256
    assert len({(c['family_id'], tuple(c['labeling'])) for c in plan['cases']}) == 252
    for f in families.values():
        edges = [set(e) for e in f['edges']]
        assert len(edges) == len({frozenset(e) for e in edges}) == 16
        assert all(len(e) == 4 and e <= set(range(16)) for e in edges)
        assert [sum(v in e for e in edges) for v in range(16)] == [4] * 16
        pairs = [list(c) for c in combinations(range(16), 2) if edges[c[0]].isdisjoint(edges[c[1]])]
        triples = [list(c) for c in combinations(range(16), 3)
                   if all(edges[i].isdisjoint(edges[j]) for i, j in combinations(c, 2))]
        assert pairs and not triples
        assert pairs == f['incidence']['disjoint_pairs']
        assert triples == f['incidence']['disjoint_triples']
        assert f['incidence']['admissible']
    # Reconstruct every saved block and compare every entry, not a preview.
    independent_blocks = {}
    for key, saved in result['support_blocks'].items():
        labels = list(map(int, key.split(',')))
        assert saved['labels'] == labels and len(labels) == len(set(labels)) == 4
        rows = exact_polynomial_rows(labels)
        assert rows == saved['annihilator']
        full_matrix = wedge(rows)
        assert full_matrix == saved['matrix']
        moment_rows = moment_annihilator(labels)
        pol_space, _ = reduce_rows(rows)
        moment_space, _ = reduce_rows(moment_rows)
        assert pol_space == moment_space
        independent_blocks[key] = wedge(moment_rows)
        polynomial_wedges, _ = reduce_rows(full_matrix)
        moment_wedges, _ = reduce_rows(independent_blocks[key])
        assert polynomial_wedges == moment_wedges and len(polynomial_wedges) == 6
    for expected_index, saved in enumerate(result['cases']):
        assert saved['plan_index'] == expected_index
        planned = plan['cases'][expected_index]
        label = planned['labeling']
        assert sorted(label) == plan['H']
        keys = [','.join(map(str, sorted(label[v] for v in e)))
                for e in families[planned['family_id']]['edges']]
        assert keys == saved['support_keys']
        matrix = [row for key in keys for row in result['support_blocks'][key]['matrix']]
        independent = [row for key in keys for row in independent_blocks[key]]
        assert len(matrix) == len(independent) == 96
        rank = len(reduce_rows(independent)[1])
        assert rank == saved['rank']
        indices, columns = saved['selected_rows'], saved['minor_columns']
        assert len(indices) == len(set(indices)) == len(columns) == len(set(columns)) == rank
        assert all(0 <= i < 96 for i in indices) and all(0 <= j < 28 for j in columns)
        determinant = column_determinant([[matrix[i][j] for j in columns] for i in indices])
        assert determinant == saved['minor_determinant'] != 0
        if planned['control']:
            assert rank == 28
        if rank < 28:
            defect = result['defect']
            assert defect['plan_index'] == expected_index and defect['matrix'] == matrix
            kernel = defect['kernel_basis']
            assert len(kernel) == 28 - rank == len(reduce_rows(kernel)[1])
            assert all(sum(a * b for a, b in zip(row, vector)) % P == 0
                       for row in matrix + independent for vector in kernel)
        checked.append({"plan_index": expected_index, "rank": rank,
                        "minor_determinant": determinant, "independent_moment_rank": rank})
    assert not result['summary']['failures']
    summary = {"families_checked": len(families), "pairs_checked": len(checked),
               "blocks_checked": len(independent_blocks),
               "all_saved_entries_checked": True,
               "matrix_entries_checked": 96 * 28 * len(checked),
               "required_rank": 28, "actual_ranks": sorted({c['rank'] for c in checked}),
               "failures": failures, "universal_theorem_proved": False}
    (HERE / 'verification.json').write_text(json.dumps({"summary": summary, "cases": checked}, separators=(',', ':')) + '\n')
    print(json.dumps(summary, sort_keys=True))
    print('Independent verification: scripts/matching-two-rank/verification.json')


if __name__ == '__main__':
    main()
