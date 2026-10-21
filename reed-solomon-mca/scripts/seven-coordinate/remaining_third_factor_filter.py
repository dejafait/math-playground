"""Approved remaining-third filter; no feasibility inference from residuals.

Run: python3 scripts/seven-coordinate/remaining_third_factor_filter.py
Complete per-third certificates are saved before proceeding to the next.
Only full rank and complete label-1 factor containment exclude cases.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json

import zero_anchor_support_filter as direct
import fixed_three_row_extensions as kernels
import verify_fixed_three_row_extensions as independent

P = 97
S, H, J = direct.S, direct.H, direct.J
FIRST = [((1, 8), (47, 50)), ((12, 18), (64, 70))]
NAMED = ((1, 22), (75, 79))
HERE = Path(__file__).resolve().parent
OUT = HERE / 'remaining-third-factor-filter'


def histogram(c):
    return {str(k): v for k, v in sorted(c.items())}


def run():
    OUT.mkdir(exist_ok=True)
    universe = list(product(combinations(S, 2), combinations(J, 2)))
    supports = {key: set(key[0]+key[1]) for key in universe}
    first_sets = [supports[key] for key in FIRST]
    eligible_thirds = [key for key in universe if all(
        len(supports[key] & a) <= 1 for a in first_sets)]
    disjoint = [key for key in eligible_thirds if not supports[key] & set.union(*first_sets)]
    thirds = [key for key in eligible_thirds if key not in disjoint and key != NAMED]
    assert H == independent.H and S == independent.S and J == independent.J
    assert len(universe) == len(set(universe)) == 756
    assert len(eligible_thirds) == 382 and len(disjoint) == 30
    assert NAMED in eligible_thirds and NAMED not in disjoint
    assert len(thirds) == len(set(thirds)) == 351
    assert set(eligible_thirds) == set(thirds) | set(disjoint) | {NAMED}
    assert not any(set(a) & set(b) for a, b in combinations([thirds, disjoint, [NAMED]], 2))
    blocks, rebuilt, ratios = {}, {}, {}
    for key in universe:
        blocks[key] = direct.block(*key)['matrix']
        rebuilt[key] = independent.block(*key)
        ratios[key] = kernels.ratio_block(*key)
        assert blocks[key] == rebuilt[key]
    forbidden = [n for n, (a, b) in enumerate(direct.PAIRS) if 1 not in (S[a], S[b])]
    totals, eligible_totals, status_totals = Counter(), Counter(), Counter()
    summaries, first_residual = [], None
    all_excluded, residual_thirds = [], []
    vectors = minors = deficient = eligible_deficient = factor_cases = 0
    for number, third in enumerate(thirds):
        keys = FIRST+[third]
        seed_sets = [supports[key] for key in keys]
        stack = [r for key in keys for r in blocks[key]]
        other_stack = [r for key in keys for r in rebuilt[key]]
        ratio_stack = [r for key in keys for r in ratios[key]]
        counts, eligible_counts, statuses = Counter(), Counter(), Counter()
        records, residual_indices = [], []
        for fourth in universe:
            matrix = stack+blocks[fourth]
            other_matrix = other_stack+rebuilt[fourth]
            rank, rows = direct.rank_and_rows(matrix)
            other_rank, columns = independent.column_rank(other_matrix)
            assert rank == other_rank
            intersections = [len(supports[fourth] & a) for a in seed_sets]
            eligible = fourth not in keys and max(intersections) <= 1
            assert eligible == (max(intersections) <= 1)
            record = {'I': fourth[0], 'K': fourth[1], 'intersections': intersections,
                      'eligible': eligible, 'rank': rank, 'pivot_columns': columns,
                      'kernel_dimension': 21-rank, 'kernel_basis': []}
            if rank == 21:
                minor = [matrix[r] for r in rows]
                determinant = direct.determinant(minor)
                assert determinant
                record.update(minor_rows=rows, minor_residue=determinant,
                              status='excluded_rank' if eligible else 'ineligible')
                minors += 1
            else:
                pivot_columns, basis = kernels.rref_kernel(ratio_stack+ratios[fourth])
                assert columns == pivot_columns and len(basis) == 21-rank
                free = [c for c in range(21) if c not in columns]
                assert [[v[c] for c in free] for v in basis] == [
                    [int(a == b) for b in range(len(basis))] for a in range(len(basis))]
                residuals = [[sum(a*b for a, b in zip(v, row)) % P
                              for row in other_matrix] for v in basis]
                assert not any(map(any, residuals))
                containment = all(v[c] == 0 for v in basis for c in forbidden)
                status = ('ineligible' if not eligible else 'excluded_label_1_factor'
                          if containment else 'unresolved')
                record.update(kernel_basis=basis, kernel_residuals=residuals,
                              label_1_factor_containment=containment, status=status)
                vectors += len(basis)
                deficient += 1
                if eligible:
                    eligible_deficient += 1
                    factor_cases += int(containment)
                if status == 'unresolved':
                    residual_indices.append(len(records))
                    if first_residual is None:
                        first_residual = {'third_index': number, 'third': third,
                                          'fourth_index': len(records), 'fourth': fourth,
                                          'rank': rank, 'kernel_basis': basis}
            counts[rank] += 1
            if eligible:
                eligible_counts[rank] += 1
            statuses[record['status']] += 1
            records.append(record)
        actual = [(tuple(c['I']), tuple(c['K'])) for c in records]
        assert actual == universe and len(set(actual)) == 756
        summary = {'third_index': number, 'third_I': third[0], 'third_K': third[1],
                   'actual_fourths': len(records), 'required_fourths': 756,
                   'all_ranks': histogram(counts), 'eligible_ranks': histogram(eligible_counts),
                   'statuses': dict(sorted(statuses.items())),
                   'residual_fourths': len(residual_indices),
                   'triple_excluded': not residual_indices}
        certificate = {'summary': summary, 'cases': records,
                       'residual_case_indices': residual_indices, 'failures': []}
        path = OUT / f'third-{number:03d}.json'
        data = (json.dumps(certificate, separators=(',', ':'))+'\n').encode()
        path.write_bytes(data)
        summaries.append(dict(summary, certificate=str(path.relative_to(HERE)),
                              sha256=sha256(data).hexdigest()))
        (residual_thirds if residual_indices else all_excluded).append(number)
        totals.update(counts)
        eligible_totals.update(eligible_counts)
        status_totals.update(statuses)
        if (number+1) % 25 == 0 or number+1 == len(thirds):
            print(f'Thirds {number+1}/351; cases {(number+1)*756}/265356; '
                  f'unresolved occurrences {status_totals["unresolved"]}', flush=True)
    summary = {'actual_thirds': len(summaries), 'required_thirds': 351,
               'actual_fourth_cases': sum(totals.values()), 'required_fourth_cases': 265356,
               'all_ranks': histogram(totals), 'eligible_ranks': histogram(eligible_totals),
               'statuses': dict(sorted(status_totals.items())),
               'excluded_triples': len(all_excluded), 'residual_triples': len(residual_thirds),
               'nonzero_minor_witnesses': minors, 'complete_deficient_kernels': deficient,
               'complete_kernel_vectors': vectors, 'eligible_deficient_kernels': eligible_deficient,
               'eligible_label_1_factor_kernels': factor_cases,
               'required_exclusion_rank': 21}
    output = {'modulus': P, 'H': H, 'S': S, 'J': J, 'first_two': FIRST,
              'column_pairs': [[S[a], S[b]] for a, b in direct.PAIRS],
              'removed_disjoint_thirds': disjoint, 'removed_named_third': NAMED,
              'summary': summary, 'thirds': summaries,
              'excluded_triple_indices': all_excluded, 'residual_triple_indices': residual_thirds,
              'first_residual': first_residual,
              'unresolved_gates': ['decomposability over F_(97^20)',
                  'rank-one projection at every row', 'nonzero lambda and overlap weights',
                  'prescribed original finite chart', 'remaining equality events and balance'],
              'failures': []}
    path = HERE / 'remaining-third-factor-filter.json'
    path.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Failures: 0; certificate: {path}; complete shards: {OUT}')


if __name__ == '__main__':
    run()
