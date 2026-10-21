"""Approved whole-kernel/selected-row factor filter, with complete certificates.

Run: python3 scripts/seven-coordinate/residual_coordinate_factors.py
No general Plucker solver, point sampling, or four-row converse is used.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json

import zero_anchor_support_filter as direct

P = 97
HERE = Path(__file__).resolve().parent
S, H, J, PAIRS = direct.S, direct.H, direct.J, direct.PAIRS
FIRST = [((1, 8), (47, 50)), ((12, 18), (64, 70))]
NAMED = ((1, 22), (75, 79))
OUT = HERE/'residual-coordinate-factors'


def save(path, value):
    data = (json.dumps(value, separators=(',', ':'))+'\n').encode()
    path.write_bytes(data)
    return sha256(data).hexdigest()


def run():
    OUT.mkdir(exist_ok=True)
    source_path = HERE/'remaining-third-factor-filter.json'
    source_data = source_path.read_bytes()
    source = json.loads(source_data)
    universe = list(product(combinations(S, 2), combinations(J, 2)))
    support = {key: set(key[0]+key[1]) for key in universe}
    first_sets = [support[key] for key in FIRST]
    eligible_thirds = [key for key in universe if all(
        len(support[key]&a) <= 1 for a in first_sets)]
    disjoint = [key for key in eligible_thirds if not support[key]&set.union(*first_sets)]
    thirds = [key for key in eligible_thirds if key not in disjoint and key != NAMED]
    assert len(universe) == 756 and len(thirds) == len(source['thirds']) == 351
    assert source['modulus'] == P and source['S'] == S and source['H'] == H and source['J'] == J
    assert source['column_pairs'] == [[S[a], S[b]] for a, b in PAIRS]
    assert source['first_two'] == [[list(i), list(k)] for i, k in FIRST]
    assert source['failures'] == []
    blocks = {key: direct.block(*key) for key in universe}
    stats, ranks, chosen, overlap = Counter(), Counter(), Counter(), Counter()
    old_excluded = {thirds[n] for n in source['excluded_triple_indices']}
    summaries, old_residual_thirds, remaining_thirds, newly_excluded_thirds = [], [], [], []
    regression = None
    for n, (third, meta) in enumerate(zip(thirds, source['thirds'])):
        assert meta['third_index'] == n
        assert (tuple(meta['third_I']), tuple(meta['third_K'])) == third
        source_shard = HERE/meta['certificate']
        assert source_shard == HERE/'remaining-third-factor-filter'/f'third-{n:03d}.json'
        data = source_shard.read_bytes()
        assert sha256(data).hexdigest() == meta['sha256']
        shard = json.loads(data)
        assert shard['failures'] == [] and len(shard['cases']) == 756
        assert [(tuple(c['I']), tuple(c['K'])) for c in shard['cases']] == universe
        indices = [u for u, case in enumerate(shard['cases']) if case['status'] == 'unresolved']
        assert indices == shard['residual_case_indices']
        assert len(indices) == meta['residual_fourths']
        if not indices:
            continue
        old_residual_thirds.append(n)
        rows3 = FIRST+[third]
        records, remaining = [], []
        for u in indices:
            case = shard['cases'][u]
            fourth = universe[u]
            rows = rows3+[fourth]
            intersections = [len(support[fourth]&support[key]) for key in rows3]
            assert max(intersections) <= 1 and case['eligible']
            assert intersections == case['intersections']
            assert all(len(support[a]&support[b]) <= 1 for a, b in combinations(rows, 2))
            matrix = [row for key in rows for row in blocks[key]['matrix']]
            rank, independent_rows = direct.rank_and_rows(matrix)
            basis = case['kernel_basis']
            assert rank == case['rank'] < 21 and len(basis) == 21-rank
            assert all(len(v) == 21 and all(type(x) is int and 0 <= x < P for x in v) for v in basis)
            free = [c for c in range(21) if c not in case['pivot_columns']]
            assert len(free) == len(basis)
            assert [[v[c] for c in free] for v in basis] == [
                [int(a == b) for b in range(len(basis))] for a in range(len(basis))]
            residuals = [[sum(a*b for a, b in zip(v, row)) % P for row in matrix] for v in basis]
            assert residuals == case['kernel_residuals'] and not any(map(any, residuals))
            factors = []
            for j, key in enumerate(rows):
                i, k = key
                block = blocks[key]
                for c in i:
                    forbidden = [t for t, (a, b) in enumerate(PAIRS) if c not in (S[a], S[b])]
                    coefficients = [[v[t] for t in forbidden] for v in basis]
                    contained = not any(map(any, coefficients))
                    record = {'row': j+1, 'coordinate': c, 'forbidden_columns': forbidden,
                              'complete_off_factor_coefficients': coefficients, 'contained': contained}
                    if contained:
                        h = [int(x == c) for x in S]
                        qh = [sum(a*b for a, b in zip(q, h)) % P for q in block['covectors']]
                        z = block['pivot']
                        gz = direct.g(k, z)
                        assert gz != 0 and c in i and c != z and not any(qh)
                        lam = h[S.index(z)]*pow(gz, -1, P) % P
                        error = {x: ((h[S.index(x)]-lam*direct.g(k, x)) if x in i
                                     else -lam*direct.g(k, x)) % P for x in i+k}
                        moments = [sum(((h[S.index(x)] if x in S else 0)-error.get(x, 0))
                                       *pow(x, d, P) for x in H) % P for d in range(1, 9)]
                        other = next(x for x in i if x != c)
                        assert lam == error[other] == 0 and not any(error[x] for x in k)
                        assert not any(moments)
                        record['gate'] = {'pivot': z, 'g_pivot': gz, 'Q_Ec': qh, 'h': h,
                            'lambda': lam, 'error': {str(x): e for x, e in error.items()},
                            'other_overlap': other, 'original_moment_residuals': moments,
                            'rank_zero': 'rejected_by_L109_nonpersistence',
                            'rank_one': 'unique_recovery_line_Ec_fails_full_weights',
                            'prescribed_chart': 'intrinsic_failure_before_finite_gate'}
                    factors.append(record)
            passes = [f for f in factors if f['contained']]
            status = 'excluded_coordinate_factor' if passes else 'unresolved'
            prior_class = ('L112_disjoint' if fourth in disjoint else 'L113_named' if fourth == NAMED
                           else 'L114_excluded' if fourth in old_excluded else 'historical_residual')
            overlap[f'{prior_class}:{status}'] += 1
            record = {'third_index': n, 'fourth_index': u, 'four_rows': rows,
                      'rank': rank, 'independent_original_rows': independent_rows,
                      'kernel_basis': basis, 'free_columns': free,
                      'original_stack_residuals': residuals, 'factor_tests': factors,
                      'status': status, 'selected_factor': (
                          {'row': passes[0]['row'], 'coordinate': passes[0]['coordinate']} if passes else None),
                      'already_excluded_by_L115': (n, u) == (0, 249)}
            record['fourth_historical_class'] = prior_class
            if passes:
                chosen[f"row{passes[0]['row']}_label{passes[0]['coordinate']}"] += 1
            else:
                remaining.append(u)
            if (n, u) == (0, 249):
                assert passes and any(f['row'] == 2 and f['coordinate'] == 12 for f in passes)
                regression = {'third_index': n, 'fourth_index': u, 'status': status,
                              'passing_factors': [[f['row'], f['coordinate']] for f in passes]}
            stats['occurrences'] += 1
            stats[status] += 1
            stats['basis_vectors'] += len(basis)
            stats['original_residual_entries'] += 24*len(basis)
            stats['factor_tests'] += len(factors)
            stats['passing_factor_tests'] += len(passes)
            ranks[rank] += 1
            records.append(record)
        if remaining:
            remaining_thirds.append(n)
        else:
            newly_excluded_thirds.append(n)
        local = {'third_index': n, 'source_shard': str(source_shard.relative_to(HERE)),
                 'source_sha256': sha256(data).hexdigest(), 'historical_residual_indices': indices,
                 'remaining_indices': remaining, 'cases': records, 'failures': []}
        path = OUT/f'third-{n:03d}.json'
        digest = save(path, local)
        summaries.append({'third_index': n, 'historical': len(indices), 'remaining': len(remaining),
                          'excluded': len(indices)-len(remaining), 'certificate': str(path.relative_to(HERE)),
                          'sha256': digest})
        if len(summaries) % 25 == 0:
            print(f"Residual thirds {len(summaries)}/230; occurrences {stats['occurrences']}/24866", flush=True)
    assert stats['occurrences'] == 24866 and len(old_residual_thirds) == 230
    assert old_residual_thirds == source['residual_triple_indices'] and regression
    summary = dict(stats, required_occurrences=24866, historical_residual_thirds=230,
                   remaining_thirds=len(remaining_thirds), newly_excluded_thirds=len(newly_excluded_thirds),
                   known_L115_occurrences=1, newly_excluded_occurrences=stats['excluded_coordinate_factor']-1,
                   rank_histogram={str(k): v for k, v in sorted(ranks.items())},
                   selected_factor_histogram=dict(sorted(chosen.items())),
                   fourth_historical_class_histogram=dict(sorted(overlap.items())))
    output = {'source': str(source_path.relative_to(HERE)), 'source_sha256': sha256(source_data).hexdigest(),
              'modulus': P, 'H': H, 'S': S, 'first_two': FIRST, 'summary': summary,
              'thirds': summaries, 'newly_excluded_third_indices': newly_excluded_thirds,
              'remaining_third_indices': remaining_thirds, 'L115_regression': regression,
              'failures': [], 'scope': 'whole-kernel sufficient filter only; no feasibility inference'}
    path = HERE/'residual-coordinate-factors.json'
    save(path, output)
    print(json.dumps(summary, sort_keys=True))
    print(f'Failures: 0; certificate: {path}; complete shards: {OUT}')


if __name__ == '__main__':
    run()
