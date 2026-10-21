"""Separate complete L111 audit. No producer imports; all cases, not a preview.

Run: python3 scripts/seven-coordinate/verify_third_row_variation.py
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
import subprocess
import sys

P = 97
H = sorted({pow(8, j, P) for j in range(16)})
S = [1, 8, 12, 18, 22, 27, 33]
J = sorted(set(H) - set(S))
PAIRS = list(combinations(range(7), 2))
FIRST = [((1, 8), (47, 50)), ((12, 18), (64, 70))]
OLD = ((22, 27), (75, 79))
HERE = Path(__file__).resolve().parent


def block(i, k):
    # Polynomial coefficient multiplication and Horner evaluation of g_K.
    coeff = [1]
    for y in sorted(set(J) - set(k)):
        coeff = [(-y*coeff[0]) % P] + [
            (coeff[d-1]-y*coeff[d]) % P for d in range(1, len(coeff))
        ] + [coeff[-1]]
    values = {}
    for x in S:
        value = 0
        for c in coeff[::-1]:
            value = (x*value+c) % P
        assert value
        values[x] = value
    observed = sorted(set(S) - set(i))
    z = observed[0]
    covectors = [[(values[z]*int(label == x)-values[x]*int(label == z)) % P
                  for label in S] for x in observed[1:]]
    return [[(a[x]*b[y]-a[y]*b[x]) % P for x, y in PAIRS]
            for a, b in combinations(covectors, 2)]


def pivots(matrix):
    # Ordinary forward Gaussian elimination, scanning columns and pivoting rows.
    a = [row[:] for row in matrix]
    chosen = []
    for c in range(21):
        r = len(chosen)
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inverse = pow(a[r][c], -1, P)
        for i in range(r+1, len(a)):
            factor = a[i][c]*inverse % P
            if factor:
                a[i][c:] = [(x-factor*y) % P for x, y in zip(a[i][c:], a[r][c:])]
        chosen.append(c)
    return chosen


def determinant(matrix):
    # Exact Bareiss elimination with ROW pivoting (producer uses column pivoting).
    a = [row[:] for row in matrix]
    n, sign, denominator = len(a), 1, 1
    for c in range(n-1):
        pivot = next((i for i in range(c, n) if a[i][c]), None)
        if pivot is None:
            return 0
        if pivot != c:
            a[c], a[pivot] = a[pivot], a[c]
            sign = -sign
        value = a[c][c]
        for i in range(c+1, n):
            for j in range(c+1, n):
                numerator = value*a[i][j]-a[i][c]*a[c][j]
                a[i][j], remainder = divmod(numerator, denominator)
                assert remainder == 0
            a[i][c] = 0
        denominator = value
    return sign*a[-1][-1]


def histogram(counter):
    return {str(k): v for k, v in sorted(counter.items())}


def run():
    path = HERE/'third-row-variation.json'
    before = path.read_bytes()
    source = json.loads(before)
    failures, checks, seeds = [], [], []

    def check(name, valid):
        checks.append({'check': name, 'passed': bool(valid)})
        if not valid:
            failures.append(name)

    check('full field-root domain', len(H) == 16 and H == [x for x in range(1, P) if pow(x, 16, P) == 1])
    check('field and label conventions', source['modulus'] == P and source['H'] == H
          and source['S'] == S and source['J'] == J
          and source['first_two'] == [{'I': list(i), 'K': list(k)} for i, k in FIRST]
          and source['column_pairs'] == [[S[a], S[b]] for a, b in PAIRS])
    expected = list(product(combinations(S, 2), combinations(J, 2)))
    used = set(x for i, k in FIRST for x in i+k)
    thirds = list(product(combinations(sorted(set(S)-used), 2), combinations(sorted(set(J)-used), 2)))
    actual_thirds = [(tuple(s['third_I']), tuple(s['third_K'])) for s in source['seeds']]
    check('all thirty third rows exactly once', len(thirds) == 30
          and len(actual_thirds) == len(set(actual_thirds)) == 30 and set(actual_thirds) == set(thirds))
    blocks = {key: block(*key) for key in expected}
    check('all 756 blocks have rank six', len(blocks) == 756 and all(len(pivots(b)) == 6 for b in blocks.values()))
    old_bytes = (HERE/'fixed-three-row-extensions.json').read_bytes()
    audit_bytes = (HERE/'fixed-three-row-critical-audit.json').read_bytes()
    old, audit = json.loads(old_bytes), json.loads(audit_bytes)
    check('reused source and audit hash identities', source['reused_source_sha256'] == sha256(old_bytes).hexdigest()
          and source['reused_audit_sha256'] == sha256(audit_bytes).hexdigest()
          and audit['producer_replay']['before_sha256'] == audit['producer_replay']['after_sha256'] == sha256(old_bytes).hexdigest()
          and audit['producer_replay']['returncode'] == 0)
    check('reused exact seed and complete successful audit', old['seed'] == [
        {'I': list(i), 'K': list(k)} for i, k in FIRST+[OLD]]
          and audit['summary'] == old['summary'] and old['failures'] == audit['failures'] == []
          and all(c['passed'] for c in audit['global_checks'])
          and len(audit['cases']) == len(old['cases']) == 756)
    for case, record in zip(old['cases'], audit['cases']):
        shared = ['I', 'K', 'rank', 'pivot_columns', 'seed_intersections', 'pairwise_linear', 'kernel_basis']
        check('reused audit case '+str(record['case']), all(case[k] == record[k] for k in shared)
              and all(c['passed'] for c in record['checks'])
              and not any(any(v) for v in record['kernel_residuals'])
              and (case['rank'] < 21 or (case['minor_row_indices'] == record['minor_row_indices']
                   and case['minor_residue'] == record['integer_determinant'] % P != 0)))
    totals, linears = Counter(), Counter()
    minor_count = kernel_count = vector_count = residual_count = 0
    residual_seeds, table = [], []
    explicit = None
    for seed_index, seed in enumerate(source['seeds']):
        third = tuple(seed['third_I']), tuple(seed['third_K'])
        keys = FIRST+[third]
        supports = [set(i+k) for i, k in keys]
        check(f'seed {seed_index} disjointness', all(not a & b for a, b in combinations(supports, 2)))
        check(f'seed {seed_index} reuse flag', seed['reused_audited_L110'] == (third == OLD))
        if third == OLD:
            check('reused seed summary and paths', seed['summary'] == old['summary']
                  and seed['source'] == 'fixed-three-row-extensions.json'
                  and seed['audit'] == 'fixed-three-row-critical-audit.json'
                  and old['summary']['linear_rank_histogram'] == {'21': 222})
            seeds.append({'third_I': list(third[0]), 'third_K': list(third[1]), 'reused_audited_L110': True})
            continue
        prefix = [row for key in keys for row in blocks[key]]
        seed_rank = len(pivots(prefix))
        cases = seed['cases']
        actual = [(tuple(c['I']), tuple(c['K'])) for c in cases]
        check(f'seed {seed_index} complete fourth case set', len(actual) == len(set(actual)) == 756 and set(actual) == set(expected))
        counts, linear_counts = Counter(), Counter()
        records, survivors = [], []
        for index, case in enumerate(cases):
            key = tuple(case['I']), tuple(case['K'])
            matrix = prefix+blocks[key]
            columns = pivots(matrix)
            rank = len(columns)
            intersections = [len(set(key[0]+key[1]) & a) for a in supports]
            linear = all(x <= 1 for x in intersections)
            basis = case['kernel_basis']
            local = []

            def test(name, valid):
                local.append({'check': name, 'passed': bool(valid)})
                if not valid:
                    failures.append(f'seed {seed_index} case {index}: {name}')

            test('rank and pivot profile', case['rank'] == rank and case['pivot_columns'] == columns)
            test('incidence and linearity', case['seed_intersections'] == intersections and case['pairwise_linear'] == linear)
            test('kernel dimensions and residues', len(basis) == case['kernel_dimension'] == 21-rank
                 and all(len(v) == 21 and all(type(x) is int and 0 <= x < P for x in v) for v in basis))
            free = sorted(set(range(21))-set(columns))
            test('complete free-coordinate identity', [[v[c] for c in free] for v in basis]
                 == [[int(a == b) for b in range(len(free))] for a in range(len(free))])
            residuals = [[sum(x*y for x, y in zip(row, v)) % P for row in matrix] for v in basis]
            test('all original matrix residuals', not any(any(v) for v in residuals))
            record = {'case_index': index, 'I': case['I'], 'K': case['K'], 'rank': rank,
                      'pivot_columns': columns, 'seed_intersections': intersections,
                      'pairwise_linear': linear, 'kernel_basis': basis,
                      'kernel_residuals': residuals, 'checks': local}
            if rank == 21:
                rows = case['minor_row_indices']
                valid = len(rows) == len(set(rows)) == 21 and all(type(r) is int and 0 <= r < 24 for r in rows)
                test('minor row selection', valid)
                det = determinant([matrix[r] for r in rows]) if valid else 0
                test('complete exact determinant and nonzero residue', det == case['integer_minor_determinant']
                     and det % P == case['minor_residue'] != 0)
                record.update(minor_row_indices=rows, integer_minor_determinant=det, minor_residue=det % P)
                minor_count += 1
            else:
                test('saved complete residuals', case['kernel_residuals'] == residuals)
                kernel_count += 1
                if linear:
                    survivors.append({'I': case['I'], 'K': case['K'], 'rank': rank, 'case_index': index})
            vector_count += len(basis)
            residual_count += sum(map(len, residuals))
            if third == ((22, 33), (79, 89)) and key == ((1, 12), (75, 79)):
                explicit = {'rank': rank, 'basis': basis, 'free_columns': free, 'intersections': intersections,
                            'residuals': residuals}
            counts[rank] += 1
            if linear:
                linear_counts[rank] += 1
            records.append(record)
        summary = {'actual_cases': len(records), 'required_cases': 756, 'seed_rank': seed_rank,
                   'all_rank_histogram': histogram(counts), 'linear_cases': sum(linear_counts.values()),
                   'linear_rank_histogram': histogram(linear_counts), 'linear_survivor_count': len(survivors),
                   'required_exclusion_rank': 21}
        check(f'seed {seed_index} entire summary and survivor list', summary == seed['summary'] and survivors == seed['linear_survivors'])
        check(f'seed {seed_index} linear case count', sum(linear_counts.values()) == 222)
        if survivors:
            residual_seeds.append({'third_I': list(third[0]), 'third_K': list(third[1]), 'survivors': survivors})
            table.append({'I': list(third[0]), 'K': list(third[1]), 'linear_ranks': histogram(linear_counts)})
        seeds.append({'third_I': list(third[0]), 'third_K': list(third[1]), 'summary': summary, 'cases': records})
        totals.update(counts)
        linears.update(linear_counts)
    summary = {'third_choices': len(seeds), 'required_third_choices': 30, 'new_third_choices': 29,
               'reused_audited_third_choices': 1, 'new_cases': sum(totals.values()), 'required_new_cases': 21924,
               'new_all_rank_histogram': histogram(totals), 'new_linear_cases': sum(linears.values()),
               'new_linear_rank_histogram': histogram(linears), 'new_linear_survivors': sum(v for r, v in linears.items() if r < 21),
               'third_choices_with_linear_survivors': len(residual_seeds),
               'full_rank_minors_independently_checked': minor_count, 'complete_deficient_kernels_checked': kernel_count,
               'kernel_vectors_checked': vector_count, 'required_exclusion_rank': 21}
    check('complete aggregate summary and residual lists', summary == source['summary'] and residual_seeds == source['residual_seeds'])
    check('claimed totals', totals == {18: 87, 19: 54, 20: 4683, 21: 17100}
          and linears == {19: 9, 20: 257, 21: 6172} and vector_count == 5052 and residual_count == 121248)
    check('all four asserted exceptional seeds and ranks', table == [
        {'I': [22, 33], 'K': [79, 89], 'linear_ranks': {'19': 9, '20': 92, '21': 121}},
        {'I': [22, 33], 'K': [85, 89], 'linear_ranks': {'20': 55, '21': 167}},
        {'I': [27, 33], 'K': [79, 96], 'linear_ranks': {'20': 55, '21': 167}},
        {'I': [27, 33], 'K': [85, 96], 'linear_ranks': {'20': 55, '21': 167}}])
    check('complete explicit residual example', explicit == {'rank': 20, 'basis': [[11, 35, 21, 53, 27, 1]+[0]*15],
          'free_columns': [5], 'intersections': [1, 1, 1], 'residuals': [[0]*24]})
    check('source reported no failures', source['failures'] == [] and source['all_blocks_independently_equal'] is True)
    replay = subprocess.run([sys.executable, str(HERE/'third_row_variation.py')], capture_output=True, text=True)
    after = path.read_bytes()
    if before != after:
        (HERE/'third-row-variation.before-audit.json').write_bytes(before)
    check('complete producer replay and byte identity', replay.returncode == 0 and before == after)
    check('reused artifacts unchanged', old_bytes == (HERE/'fixed-three-row-extensions.json').read_bytes()
          and audit_bytes == (HERE/'fixed-three-row-critical-audit.json').read_bytes())
    output = {'scope': 'complete separate L111 audit; no feasibility conclusions', 'summary': summary,
              'kernel_residual_entries_checked': residual_count, 'exceptional_seed_table': table,
              'explicit_residual_example': explicit, 'global_checks': checks, 'seeds': seeds,
              'reused_source_sha256': sha256(old_bytes).hexdigest(), 'reused_audit_sha256': sha256(audit_bytes).hexdigest(),
              'producer_replay': {'returncode': replay.returncode, 'stdout': replay.stdout, 'stderr': replay.stderr,
                                  'before_sha256': sha256(before).hexdigest(), 'after_sha256': sha256(after).hexdigest()},
              'failures': failures}
    destination = HERE/'third-row-critical-audit.json'
    destination.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Residual entries {residual_count}/121248; failures {len(failures)}; full certificate {destination}')
    if failures:
        print('Failures:', failures)
        raise SystemExit(1)


if __name__ == '__main__':
    run()
