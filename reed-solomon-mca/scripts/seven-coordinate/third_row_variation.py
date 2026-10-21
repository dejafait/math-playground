"""Complete 29 new third-seed tests; reuse L110's audited thirtieth seed.

Run: python3 scripts/seven-coordinate/third_row_variation.py
All exact certificates stay on disk; rank deficiency is not feasibility.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json

import zero_anchor_support_filter as producer
import fixed_three_row_extensions as kernels
import verify_fixed_three_row_extensions as independent

P = 97
S, H, J = producer.S, producer.H, producer.J
FIRST = [([1, 8], [47, 50]), ([12, 18], [64, 70])]
OLD = ((22, 27), (75, 79))
HERE = Path(__file__).resolve().parent


def run():
    failures = []
    expected = list(product(combinations(S, 2), combinations(J, 2)))
    assert len(expected) == len(set(expected)) == 756
    assert H == independent.H and S == independent.S and J == independent.J
    assert len(H) == 16 and H == [x for x in range(1, P) if pow(x, 16, P) == 1]
    used = set(sum((i+k for i, k in FIRST), []))
    thirds = list(product(combinations(sorted(set(S)-used), 2),
                          combinations(sorted(set(J)-used), 2)))
    assert len(thirds) == len(set(thirds)) == 30 and OLD in thirds
    blocks, rebuilt, ratios = {}, {}, {}
    for i, k in expected:
        key = (i, k)
        blocks[key] = producer.block(i, k)['matrix']
        rebuilt[key] = independent.block(i, k)
        ratios[key] = kernels.ratio_block(i, k)
        assert blocks[key] == rebuilt[key]
    first_keys = [(tuple(i), tuple(k)) for i, k in FIRST]
    source_path = HERE/'fixed-three-row-extensions.json'
    audit_path = HERE/'fixed-three-row-critical-audit.json'
    old_bytes, audit_bytes = source_path.read_bytes(), audit_path.read_bytes()
    old, audit = json.loads(old_bytes), json.loads(audit_bytes)
    assert old['seed'] == [{'I': i, 'K': k} for i, k in FIRST]+[{'I': list(OLD[0]), 'K': list(OLD[1])}]
    assert old['summary'] == audit['summary'] and old['failures'] == audit['failures'] == []
    assert audit['producer_replay']['after_sha256'] == sha256(old_bytes).hexdigest()
    assert old['summary']['actual_cases'] == 756 and old['summary']['linear_survivor_count'] == 0

    seeds, residuals = [], []
    total, linear_total = Counter(), Counter()
    minors_checked = deficient_checked = vectors_checked = 0
    for third in thirds:
        keys = first_keys+[third]
        seed_sets = [set(i+k) for i, k in keys]
        assert all(not a & b for a, b in combinations(seed_sets, 2))
        if third == OLD:
            seeds.append({'third_I': list(third[0]), 'third_K': list(third[1]),
                          'reused_audited_L110': True, 'summary': old['summary'],
                          'source': source_path.name, 'audit': audit_path.name})
            continue
        stack = [row for key in keys for row in blocks[key]]
        rebuilt_stack = [row for key in keys for row in rebuilt[key]]
        ratio_stack = [row for key in keys for row in ratios[key]]
        seed_rank = producer.rank_and_rows(stack)[0]
        assert seed_rank == independent.column_rank(rebuilt_stack)[0]
        counts, linear_counts = Counter(), Counter()
        cases, survivors = [], []
        for i, k in expected:
            key = (i, k)
            matrix = stack+blocks[key]
            other_matrix = rebuilt_stack+rebuilt[key]
            rank, rows = producer.rank_and_rows(matrix)
            other_rank, pivot_columns = independent.column_rank(other_matrix)
            intersections = [len(set(i+k) & a) for a in seed_sets]
            linear = all(v <= 1 for v in intersections)
            local_failures = []
            if rank != other_rank:
                local_failures.append('independent ranks disagree')
            basis = []
            record = {'I': list(i), 'K': list(k), 'rank': rank,
                      'pivot_columns': pivot_columns,
                      'seed_intersections': intersections, 'pairwise_linear': linear,
                      'kernel_dimension': 21-rank, 'kernel_basis': basis}
            if rank == 21:
                modular_det = producer.determinant([matrix[r] for r in rows])
                integer_det = independent.integer_det([other_matrix[r] for r in rows])
                if modular_det == 0 or integer_det % P != modular_det:
                    local_failures.append('independent exact minor check failed')
                record.update(minor_row_indices=rows, minor_residue=modular_det,
                              integer_minor_determinant=integer_det)
                minors_checked += 1
            else:
                pivots, basis = kernels.rref_kernel(ratio_stack+ratios[key])
                if pivots != pivot_columns or len(basis) != 21-rank:
                    local_failures.append('independent complete kernel dimension/profile failed')
                free = sorted(set(range(21))-set(pivots))
                if [[v[c] for c in free] for v in basis] != [
                        [int(a == b) for b in range(len(free))] for a in range(len(free))]:
                    local_failures.append('kernel independence failed')
                kernel_residuals = [[sum(x*y for x, y in zip(row, v)) % P
                                     for row in other_matrix] for v in basis]
                if any(any(row) for row in kernel_residuals):
                    local_failures.append('complete kernel residual check failed')
                record.update(kernel_basis=basis, kernel_residuals=kernel_residuals)
                deficient_checked += 1
                vectors_checked += len(basis)
                if linear:
                    survivors.append({'I': list(i), 'K': list(k), 'rank': rank,
                                      'case_index': len(cases)})
            if local_failures:
                failures.append({'third': third, 'fourth': key, 'failures': local_failures})
            cases.append(record)
            counts[rank] += 1
            if linear:
                linear_counts[rank] += 1
        actual = [(tuple(c['I']), tuple(c['K'])) for c in cases]
        assert len(actual) == len(set(actual)) == 756 and set(actual) == set(expected)
        summary = {'actual_cases': len(cases), 'required_cases': 756,
                   'seed_rank': seed_rank, 'all_rank_histogram': dict(sorted(counts.items())),
                   'linear_cases': sum(linear_counts.values()),
                   'linear_rank_histogram': dict(sorted(linear_counts.items())),
                   'linear_survivor_count': len(survivors), 'required_exclusion_rank': 21}
        seeds.append({'third_I': list(third[0]), 'third_K': list(third[1]),
                      'reused_audited_L110': False, 'summary': summary,
                      'linear_survivors': survivors, 'cases': cases})
        if survivors:
            residuals.append({'third_I': list(third[0]), 'third_K': list(third[1]),
                              'survivors': survivors})
        total.update(counts)
        linear_total.update(linear_counts)
        print(f'Third {third}: linear ranks {dict(sorted(linear_counts.items()))}; '
              f'survivors {len(survivors)}; complete cases {len(cases)}/756', flush=True)

    summary = {'third_choices': len(seeds), 'required_third_choices': 30,
               'new_third_choices': 29, 'reused_audited_third_choices': 1,
               'new_cases': sum(total.values()), 'required_new_cases': 29*756,
               'new_all_rank_histogram': dict(sorted(total.items())),
               'new_linear_cases': sum(linear_total.values()),
               'new_linear_rank_histogram': dict(sorted(linear_total.items())),
               'new_linear_survivors': sum(v for r, v in linear_total.items() if r < 21),
               'third_choices_with_linear_survivors': len(residuals),
               'full_rank_minors_independently_checked': minors_checked,
               'complete_deficient_kernels_checked': deficient_checked,
               'kernel_vectors_checked': vectors_checked,
               'required_exclusion_rank': 21}
    output = {'modulus': P, 'H': H, 'S': S, 'J': J,
              'first_two': [{'I': i, 'K': k} for i, k in FIRST],
              'scope': '30 disjoint third choices for two fixed labeled supports; necessary rank filter only',
              'column_pairs': [[S[a], S[b]] for a, b in producer.PAIRS],
              'reused_source_sha256': sha256(old_bytes).hexdigest(),
              'reused_audit_sha256': sha256(audit_bytes).hexdigest(),
              'all_blocks_independently_equal': True, 'summary': summary,
              'unresolved_gates': ['nonzero decomposable kernel tensor over F_(97^20)',
                                  'each projected restriction has rank one',
                                  'lambda and both overlap weights nonzero',
                                  'prescribed original finite-chart gate',
                                  'remaining t=0 equality events and balance'],
              'residual_seeds': residuals, 'seeds': seeds, 'failures': failures}
    assert len(seeds) == 30 and sum(total.values()) == 29*756
    path = HERE/'third-row-variation.json'
    path.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Failures: {len(failures)}; certificate: {path}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
