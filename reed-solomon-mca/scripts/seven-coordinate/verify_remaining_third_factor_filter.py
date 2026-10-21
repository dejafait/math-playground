"""Replay every saved remaining-third case using independent block formulas.

Run after the producer:
python3 scripts/seven-coordinate/verify_remaining_third_factor_filter.py
No producer imports; no Plucker, point sampling, or new gate solver.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json

import verify_fixed_three_row_extensions as independent

P = 97
HERE = Path(__file__).resolve().parent
S = [1, 8, 12, 18, 22, 27, 33]
H = [x for x in range(1, 97) if pow(x, 16, 97) == 1]
J = sorted(set(H)-set(S))
FIRST = [((1, 8), (47, 50)), ((12, 18), (64, 70))]
NAMED = ((1, 22), (75, 79))
PAIRS = list(combinations(range(7), 2))


def determinant_by_columns(matrix):
    """Modular determinant by column operations, independent of row path."""
    a = [row[:] for row in matrix]
    determinant = 1
    for r in range(len(a)):
        c = next((c for c in range(r, len(a)) if a[r][c]), None)
        if c is None:
            return 0
        if c != r:
            for row in a:
                row[r], row[c] = row[c], row[r]
            determinant = -determinant
        pivot = a[r][r]
        determinant = determinant*pivot % P
        inverse = pow(pivot, -1, P)
        for c in range(r+1, len(a)):
            factor = a[r][c]*inverse % P
            if factor:
                for k in range(r+1, len(a)):
                    a[k][c] = (a[k][c]-factor*a[k][r]) % P
            a[r][c] = 0
    return determinant % P


def hist(c):
    return {str(k): v for k, v in sorted(c.items())}


def run():
    source_path = HERE/'remaining-third-factor-filter.json'
    source_bytes = source_path.read_bytes()
    source = json.loads(source_bytes)
    assert source['failures'] == []
    assert source['modulus'] == P and source['H'] == H and source['S'] == S and source['J'] == J
    assert source['column_pairs'] == [[S[a], S[b]] for a, b in PAIRS]
    assert source['first_two'] == [[list(i), list(k)] for i, k in FIRST]
    universe = list(product(combinations(S, 2), combinations(J, 2)))
    support = {key: set(key[0]+key[1]) for key in universe}
    first_sets = [support[k] for k in FIRST]
    eligible_thirds = [k for k in universe if all(len(support[k]&a) <= 1 for a in first_sets)]
    disjoint = [k for k in eligible_thirds if not support[k] & set.union(*first_sets)]
    thirds = [k for k in eligible_thirds if k not in disjoint and k != NAMED]
    assert source['removed_disjoint_thirds'] == [[list(i), list(k)] for i, k in disjoint]
    assert source['removed_named_third'] == [list(NAMED[0]), list(NAMED[1])]
    assert len(universe) == 756 and len(eligible_thirds) == 382 and len(disjoint) == 30
    assert len(thirds) == 351 and len(source['thirds']) == 351
    assert [(tuple(s['third_I']), tuple(s['third_K'])) for s in source['thirds']] == thirds
    assert len(set(thirds)) == 351 and set(thirds) == set(eligible_thirds)-set(disjoint)-{NAMED}
    assert H == independent.H and S == independent.S and J == independent.J
    blocks = {key: independent.block(*key) for key in universe}
    forbidden = [j for j, (a, b) in enumerate(PAIRS) if S[a] != 1 and S[b] != 1]
    total, eligible_total, status_total = Counter(), Counter(), Counter()
    excluded, unresolved, audits = [], [], []
    minor_count = deficient_count = vector_count = eligible_deficient = factors = 0
    residual_entries = 0
    first_residual = None
    for number, (third, saved_summary) in enumerate(zip(thirds, source['thirds'])):
        path = HERE/saved_summary['certificate']
        assert path == HERE/'remaining-third-factor-filter'/f'third-{number:03d}.json'
        data = path.read_bytes()
        assert sha256(data).hexdigest() == saved_summary['sha256']
        shard = json.loads(data)
        assert shard['failures'] == [] and len(shard['cases']) == 756
        cases = shard['cases']
        assert [(tuple(c['I']), tuple(c['K'])) for c in cases] == universe
        keys = FIRST+[third]
        stack = [row for key in keys for row in blocks[key]]
        seed_sets = [support[key] for key in keys]
        counts, eligible_counts, statuses = Counter(), Counter(), Counter()
        indices = []
        for fourth_number, (fourth, c) in enumerate(zip(universe, cases)):
            matrix = stack+blocks[fourth]
            intersections = [len(support[fourth]&a) for a in seed_sets]
            eligible = fourth not in keys and all(x <= 1 for x in intersections)
            assert c['intersections'] == intersections and c['eligible'] == eligible
            rank = c['rank']
            assert type(rank) is int and 0 <= rank <= 21
            assert c['kernel_dimension'] == 21-rank
            if rank == 21:
                assert c['kernel_basis'] == []
                rows = c['minor_rows']
                assert len(rows) == len(set(rows)) == 21 and all(0 <= r < 24 for r in rows)
                determinant = determinant_by_columns([matrix[r] for r in rows])
                assert determinant == c['minor_residue'] != 0
                # Nonzero square minor proves rank exactly 21, without assuming saved rank.
                assert c['pivot_columns'] == list(range(21))
                status = 'excluded_rank' if eligible else 'ineligible'
                minor_count += 1
            else:
                other_rank, columns = independent.column_rank(matrix)
                assert other_rank == rank and c['pivot_columns'] == columns
                basis = c['kernel_basis']
                assert len(basis) == 21-rank
                assert all(len(v) == 21 and all(type(x) is int and 0 <= x < P for x in v) for v in basis)
                free = [j for j in range(21) if j not in columns]
                assert [[v[j] for j in free] for v in basis] == [
                    [int(a == b) for b in range(len(basis))] for a in range(len(basis))]
                residuals = [[sum(a*b for a, b in zip(v, row)) % P
                              for row in matrix] for v in basis]
                assert residuals == c['kernel_residuals'] and not any(map(any, residuals))
                containment = all(v[j] == 0 for v in basis for j in forbidden)
                assert containment == c['label_1_factor_containment']
                status = ('ineligible' if not eligible else 'excluded_label_1_factor'
                          if containment else 'unresolved')
                deficient_count += 1
                vector_count += len(basis)
                residual_entries += sum(map(len, residuals))
                if eligible:
                    eligible_deficient += 1
                    factors += int(containment)
                if status == 'unresolved':
                    indices.append(fourth_number)
                    if first_residual is None:
                        first_residual = {'third_index': number, 'third': [list(x) for x in third],
                                          'fourth_index': fourth_number, 'fourth': [list(x) for x in fourth],
                                          'rank': rank, 'kernel_basis': basis}
            assert c['status'] == status
            counts[rank] += 1
            if eligible:
                eligible_counts[rank] += 1
            statuses[status] += 1
        summary = {'third_index': number, 'third_I': list(third[0]), 'third_K': list(third[1]),
                   'actual_fourths': 756, 'required_fourths': 756,
                   'all_ranks': hist(counts), 'eligible_ranks': hist(eligible_counts),
                   'statuses': dict(sorted(statuses.items())), 'residual_fourths': len(indices),
                   'triple_excluded': not indices}
        assert summary == shard['summary']
        assert dict(summary, certificate=saved_summary['certificate'], sha256=sha256(data).hexdigest()) == saved_summary
        assert indices == shard['residual_case_indices']
        (unresolved if indices else excluded).append(number)
        audits.append(dict(summary, sha256=sha256(data).hexdigest()))
        total.update(counts)
        eligible_total.update(eligible_counts)
        status_total.update(statuses)
        if (number+1) % 50 == 0 or number+1 == 351:
            print(f'Replayed thirds {number+1}/351; cases {(number+1)*756}/265356', flush=True)
    summary = {'actual_thirds': 351, 'required_thirds': 351,
               'actual_fourth_cases': sum(total.values()), 'required_fourth_cases': 265356,
               'all_ranks': hist(total), 'eligible_ranks': hist(eligible_total),
               'statuses': dict(sorted(status_total.items())), 'excluded_triples': len(excluded),
               'residual_triples': len(unresolved), 'nonzero_minor_witnesses': minor_count,
               'complete_deficient_kernels': deficient_count, 'complete_kernel_vectors': vector_count,
               'eligible_deficient_kernels': eligible_deficient,
               'eligible_label_1_factor_kernels': factors, 'required_exclusion_rank': 21}
    assert summary == source['summary'] and first_residual == source['first_residual']
    assert excluded == source['excluded_triple_indices'] and unresolved == source['residual_triple_indices']
    output = {'source_sha256': sha256(source_bytes).hexdigest(), 'summary': summary,
              'kernel_residual_entries_checked': residual_entries, 'thirds': audits,
              'first_residual': first_residual, 'failures': [],
              'scope': 'same-step independent complete certificate replay, not a separate critical audit'}
    path = HERE/'remaining-third-factor-filter-replay.json'
    path.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Failures: 0; kernel residual entries: {residual_entries}; replay: {path}')


if __name__ == '__main__':
    run()
