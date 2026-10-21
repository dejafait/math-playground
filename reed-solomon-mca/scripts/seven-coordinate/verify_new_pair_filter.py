"""Independent complete replay; imports neither producer nor its row solver.

Run: python3 scripts/seven-coordinate/verify_new_pair_filter.py
Derivative-based original blocks; column elimination tracks null relations.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
import traceback

import verify_fixed_three_row_extensions as derivative

P = 97
HERE = Path(__file__).resolve().parent


def column_kernel(matrix):
    """Eliminate columns, tracking exact relations among original columns."""
    echelon, pivots, basis = {}, [], []
    for c, column in enumerate(zip(*matrix)):
        v, relation = list(column), [int(i == c) for i in range(21)]
        for r in sorted(echelon):
            scale = v[r]
            if scale:
                saved, coefficients = echelon[r]
                v = [(a-scale*b) % P for a, b in zip(v, saved)]
                relation = [(a-scale*b) % P for a, b in zip(relation, coefficients)]
        r = next((i for i, x in enumerate(v) if x), None)
        if r is None:
            basis.append(relation)
        else:
            inverse = pow(v[r], -1, P)
            echelon[r] = ([inverse*x % P for x in v],
                          [inverse*x % P for x in relation])
            pivots.append(c)
    return pivots, basis


def determinant(matrix):
    """Column-pivoted determinant of a selected original square submatrix."""
    a = [row[:] for row in matrix]
    out = 1
    for r in range(len(a)):
        c = next((c for c in range(len(a)-1, r-1, -1) if a[r][c]), None)
        if c is None:
            return 0
        if c != r:
            for row in a:
                row[r], row[c] = row[c], row[r]
            out = -out
        out = out*a[r][r] % P
        inverse = pow(a[r][r], -1, P)
        for c in range(r+1, len(a)):
            scale = a[r][c]*inverse % P
            if scale:
                for k in range(r+1, len(a)):
                    a[k][c] = (a[k][c]-scale*a[k][r]) % P
            a[r][c] = 0
    return out % P


def run():
    path = HERE/'new-pair-filter.json'
    source_bytes = path.read_bytes()
    master = json.loads(source_bytes)
    s = [1, 8, 12, 18, 22, 27, 33]
    h = sorted({pow(8, j, P) for j in range(16)})
    j = sorted(set(h)-set(s))
    pairs = list(combinations(range(7), 2))
    universe = list(product(combinations(s, 2), combinations(j, 2)))
    sets = [set(i+k) for i, k in universe]
    first = [((1, 8), (47, 50)), ((12, 18), (64, 75))]
    fi = [universe.index(key) for key in first]
    assert len(h) == 16 and h == [x for x in range(1, P) if pow(x, 16, P) == 1]
    assert len(universe) == len(set(universe)) == 756
    assert not sets[fi[0]] & sets[fi[1]]
    assert master['modulus'] == P and master['S'] == s and master['H'] == h and master['J'] == j
    assert master['universe'] == [[list(i), list(k)] for i, k in universe]
    assert master['first_two'] == [[list(i), list(k)] for i, k in first]
    assert master['first_indices'] == fi and master['failures'] == []
    assert master['column_pairs'] == [[s[a], s[b]] for a, b in pairs]
    assert sha256((HERE/'new_pair_filter.py').read_bytes()).hexdigest() == master['code_sha256']
    assert sha256((HERE/'zero_anchor_support_filter.py').read_bytes()).hexdigest() == master['direct_helper_sha256']
    blocks = [derivative.block(*key) for key in universe]
    assert len(master['blocks']) == len(master['factor_gate_coefficients']) == 756
    gate_count = 0
    for u, (i, k) in enumerate(universe):
        saved = master['blocks'][u]
        assert saved['I'] == list(i) and saved['K'] == list(k) and saved['matrix'] == blocks[u]
        values = {}
        for x in s+list(k):
            denominator = 1
            for y in s+list(k):
                if y != x:
                    denominator = denominator*(x-y) % P
            assert denominator
            values[x] = 16*pow(x, 15, P)*pow(denominator, -1, P) % P
            assert values[x]
        observed = sorted(set(s)-set(i))
        z = observed[0]
        q = [[(int(y == x)*values[z]-int(y == z)*values[x]) % P for y in s]
             for x in observed[1:]]
        assert saved['pivot'] == z and saved['covectors'] == q
        assert len(master['factor_gate_coefficients'][u]) == 2
        for c, g in zip(i, master['factor_gate_coefficients'][u]):
            plane_vector = [int(x == c) for x in s]
            projection = [sum(a*b for a, b in zip(row, plane_vector)) % P for row in q]
            lam = plane_vector[s.index(z)]*pow(values[z], -1, P) % P
            error = [(int(x == c)-lam*values[x]) % P for x in i]
            error += [-lam*values[x] % P for x in k]
            moments = [(pow(c, d, P)-sum(a*pow(x, d, P) for x, a in zip(i+k, error))) % P
                       for d in range(1, 9)]
            assert g == dict(coordinate=c, pivot=z, g_pivot=values[z], projection=projection,
                             lambda_value=lam, error=error, moment_residuals=moments)
            assert not any(projection) and lam == 0 and error.count(0) == 3 and not any(moments)
            gate_count += 1
    thirds = []
    assert len(master['third_screen']) == 756
    for u, a in enumerate(sets):
        intersections = [len(a & sets[v]) for v in fi]
        eligible = u not in fi and max(intersections) <= 1
        assert master['third_screen'][u] == dict(index=u, intersections=intersections,
                                               distinct=u not in fi, eligible=eligible)
        if eligible:
            thirds.append(u)
    assert master['third_indices'] == thirds
    assert [v['third_index'] for v in master['thirds']] == thirds
    ranks, statuses, residuals, manifests = Counter(), Counter(), [], []
    factor_occ = omission_occ = factor_tests = omission_tests = vectors = 0
    eligible_count = 0
    first_residual = None
    for number, (c, meta) in enumerate(zip(thirds, master['thirds'])):
        shard_path = HERE/'new-pair-filter'/f'third-{c:03d}.json'
        data = shard_path.read_bytes()
        assert meta['certificate'] == str(shard_path.relative_to(HERE))
        assert sha256(data).hexdigest() == meta['sha256']
        shard = json.loads(data)
        assert shard['third_index'] == c and shard['failures'] == []
        selected = fi+[c]
        expected = []
        assert len(shard['fourth_screen']) == 756
        for d, a in enumerate(sets):
            intersections = [len(a & sets[v]) for v in selected]
            distinct = d not in selected
            eligible = distinct and all(v <= 1 for v in intersections)
            assert shard['fourth_screen'][d] == dict(index=d, intersections=intersections,
                                                    distinct=distinct, eligible=eligible)
            if eligible:
                # Recheck all six intersections on these four distinct original supports.
                assert all(len(sets[x] & sets[y]) <= 1 for x, y in combinations(selected+[d], 2))
                expected.append(d)
        assert [v['fourth_index'] for v in shard['cases']] == expected
        eligible_count += len(expected)
        local_ranks, local_status, remaining = Counter(), Counter(), []
        for d, record in zip(expected, shard['cases']):
            indices = selected+[d]
            matrix = [r for v in indices for r in blocks[v]]
            columns, basis = column_kernel(matrix)
            rank = len(columns)
            assert columns == record['pivot_columns'] and rank == record['rank']
            assert basis == record['kernel_basis'] and len(basis) == 21-rank
            free = sorted(set(range(21))-set(columns))
            assert [[v[j] for j in free] for v in basis] == [
                [int(a == b) for b in range(len(free))] for a in range(len(free))]
            residual = [[sum(a*b for a, b in zip(v, row)) % P for row in matrix] for v in basis]
            assert residual == record['kernel_residuals'] and not any(map(any, residual))
            rows = record['minor_rows']
            assert len(rows) == len(set(rows)) == rank and all(0 <= r < 24 for r in rows)
            minor = [[matrix[r][col] for col in columns] for r in rows]
            assert determinant(minor) == record['minor_residue'] != 0
            vectors += len(basis)
            if rank == 21:
                assert record['factor_tests'] == record['omission_tests'] == []
                status = 'rank'
            else:
                # Full antisymmetric tensors give a different path to each linear test.
                tensors = []
                for v in basis:
                    tensor = [[0]*7 for _ in s]
                    for value, (a, b) in zip(v, pairs):
                        tensor[a][b], tensor[b][a] = value, -value % P
                    tensors.append(tensor)
                factors = [(row, x) for row, u in enumerate(indices) for x in universe[u][0]]
                assert len(record['factor_tests']) == 8 and len(record['omission_tests']) == 7
                fp, op = False, False
                for (row, x), test in zip(factors, record['factor_tests']):
                    pos = s.index(x)
                    passes = all(t[a][b] == 0 for t in tensors
                                 for a, b in combinations(range(7), 2) if pos not in (a, b))
                    assert test['row'] == row and test['coordinate'] == x and test['passes'] == passes
                    witness = test['failure_witness']
                    if passes:
                        assert witness is None
                    else:
                        b, col, value = witness
                        assert 0 <= b < len(basis) and 0 <= col < 21
                        assert pos not in pairs[col] and basis[b][col] == value != 0
                    factor_tests += passes
                    fp |= passes
                for pos, test in enumerate(record['omission_tests']):
                    passes = all(not any(t[pos]) for t in tensors)
                    assert test['coordinate'] == s[pos] and test['passes'] == passes
                    witness = test['failure_witness']
                    if passes:
                        assert witness is None
                    else:
                        b, col, value = witness
                        assert 0 <= b < len(basis) and 0 <= col < 21
                        assert pos in pairs[col] and basis[b][col] == value != 0
                    omission_tests += passes
                    op |= passes
                factor_occ += fp
                omission_occ += op
                status = 'factor' if fp else 'omission' if op else 'residual'
            assert status == record['status']
            ranks[rank] += 1
            statuses[status] += 1
            local_ranks[rank] += 1
            local_status[status] += 1
            if status == 'residual':
                remaining.append(d)
                residuals.append([c, d])
                if first_residual is None:
                    first_residual = dict(third_index=c, fourth_index=d,
                                          supports=[universe[u] for u in indices],
                                          rank=rank, kernel_basis=basis)
        assert remaining == shard['residual_indices']
        actual_meta = dict(third_index=c, certificate=str(shard_path.relative_to(HERE)),
                           sha256=sha256(data).hexdigest(), cases=len(expected),
                           ranks={str(k): v for k, v in sorted(local_ranks.items())},
                           statuses=dict(sorted(local_status.items())))
        assert actual_meta == meta
        manifests.append(actual_meta)
        if (number+1) % 25 == 0 or number+1 == len(thirds):
            print(f'Replayed thirds {number+1}/{len(thirds)}; original stacks {eligible_count}; '
                  f'residuals {len(residuals)}; failures 0', flush=True)
    required = sum(c != d and len(sets[c] & sets[d]) <= 1 for c in thirds for d in thirds)
    assert eligible_count == required == sum(ranks.values())
    summary = dict(actual_thirds=len(thirds), actual_cases=eligible_count, required_cases=required,
                   rank_histogram={str(k): v for k, v in sorted(ranks.items())},
                   statuses=dict(sorted(statuses.items())), factor_passing_occurrences=factor_occ,
                   omission_passing_occurrences=omission_occ, factor_passing_tests=factor_tests,
                   omission_passing_tests=omission_tests, complete_kernel_vectors=vectors,
                   original_residual_entries=24*vectors, residual_thirds=len(set(c for c, d in residuals)),
                   required_exclusion_rank=21)
    assert master['summary'] == summary and master['residual_occurrences'] == residuals
    assert path.read_bytes() == source_bytes
    output = dict(source_sha256=sha256(source_bytes).hexdigest(), summary=summary,
                  derivative_helper_sha256=sha256(Path(derivative.__file__).read_bytes()).hexdigest(),
                  code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                  gate_coefficient_checks=gate_count, thirds=manifests,
                  first_residual=first_residual, failures=[],
                  scope='complete same-step independent replay, not separate critical audit')
    replay_path = HERE/'new-pair-filter-replay.json'
    replay_path.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Failures: 0; required/actual cases {required}/{eligible_count}; replay {replay_path}', flush=True)


if __name__ == '__main__':
    try:
        run()
    except Exception:
        (HERE/'new-pair-filter-replay-failure.txt').write_text(traceback.format_exc())
        raise
