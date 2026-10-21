"""Complete independent L110 audit; no producer imports.

Run from the notebook:
python3 scripts/seven-coordinate/verify_fixed_three_row_extensions.py
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
SEED = [([1, 8], [47, 50]), ([12, 18], [64, 70]),
        ([22, 27], [75, 79])]
PAIRS = list(combinations(range(7), 2))
HERE = Path(__file__).resolve().parent


def block(i, k):
    # At x in S, differentiate X^16-1 = g_K(X)*prod_{y in S union K}(X-y).
    # Thus g_K(x) = 16*x^15 / prod_{y in (S union K) minus {x}}(x-y).
    values = {}
    for x in S:
        denominator = 1
        for y in S + list(k):
            if y != x:
                denominator = denominator * (x-y) % P
        assert denominator
        values[x] = 16 * pow(x, 15, P) * pow(denominator, -1, P) % P
        assert values[x]
    observed = sorted(set(S)-set(i))
    z = observed[0]
    quotients = []
    for x in observed[1:]:
        quotients.append([(int(y == x)*pow(values[x], -1, P)
                           - int(y == z)*pow(values[z], -1, P)) % P for y in S])
    rows = []
    for a, b in combinations(range(4), 2):
        factor = values[z]**2 * values[observed[a+1]] * values[observed[b+1]] % P
        rows.append([factor * (quotients[a][x]*quotients[b][y]
                                - quotients[a][y]*quotients[b][x]) % P
                     for x, y in PAIRS])
    return rows


def column_rank(matrix):
    """Choose independent columns by eliminating their row coordinates."""
    echelon = {}
    chosen = []
    for column, values in enumerate(zip(*matrix)):
        v = list(values)
        for coordinate in sorted(echelon):
            multiple = v[coordinate]
            if multiple:
                v = [(x-multiple*y) % P for x, y in zip(v, echelon[coordinate])]
        pivot = next((r for r, value in enumerate(v) if value), None)
        if pivot is not None:
            inverse = pow(v[pivot], -1, P)
            echelon[pivot] = [inverse*x % P for x in v]
            chosen.append(column)
    return len(chosen), chosen


def integer_det(matrix):
    """Fraction-free integer determinant with COLUMN pivoting, no field reduction."""
    a = [row[:] for row in matrix]
    n = len(a)
    previous, sign = 1, 1
    for r in range(n-1):
        c = next((c for c in range(n-1, r-1, -1) if a[r][c]), None)
        if c is None:
            return 0
        if c != r:
            for row in a:
                row[r], row[c] = row[c], row[r]
            sign = -sign
        pivot = a[r][r]
        for x in range(r+1, n):
            for y in range(r+1, n):
                numerator = pivot*a[x][y] - a[x][r]*a[r][y]
                quotient, remainder = divmod(numerator, previous)
                assert remainder == 0
                a[x][y] = quotient
            a[x][r] = 0
        previous = pivot
    return sign*a[-1][-1]


def run():
    path = HERE / 'fixed-three-row-extensions.json'
    before = path.read_bytes()
    source = json.loads(before)
    failures, checks, records = [], [], []

    def check(name, value):
        checks.append({'check': name, 'passed': bool(value)})
        if not value:
            failures.append(name)

    check('H has sixteen elements and is the full root set',
          len(H) == 16 and H == [x for x in range(1, P) if pow(x, 16, P) == 1])
    check('field and all labeled metadata', source['modulus'] == P
          and source['H'] == H and source['S'] == S and source['J'] == J
          and source['seed'] == [{'I': i, 'K': k} for i, k in SEED]
          and source['column_pairs'] == [[S[a], S[b]] for a, b in PAIRS])
    seed = [row for i, k in SEED for row in block(i, k)]
    check('seed rank eighteen', column_rank(seed)[0] == source['seed_rank'] == 18)
    seed_sets = [set(i+k) for i, k in SEED]
    check('seed supports pairwise disjoint', all(not (a & b) for a, b in combinations(seed_sets, 2)))
    expected = set(product(combinations(S, 2), combinations(J, 2)))
    cases = source['cases']
    actual = [(tuple(c['I']), tuple(c['K'])) for c in cases]
    check('exact complete case set with no duplicates', len(cases) == len(set(actual)) == 756
          and set(actual) == expected)
    counts, linear_counts = Counter(), Counter()
    minors = kernels = vectors = residual_entries = 0
    for number, case in enumerate(cases):
        i, k = case['I'], case['K']
        local = []

        def test(name, valid):
            local.append({'check': name, 'passed': bool(valid)})
            if not valid:
                failures.append(f'case {number}: {name}')

        matrix = seed + block(i, k)
        rank, pivots = column_rank(matrix)
        intersections = [len(set(i+k) & a) for a in seed_sets]
        linear = all(v <= 1 for v in intersections)
        basis = case['kernel_basis']
        test('rank and independent-column profile', rank == case['rank'] and pivots == case['pivot_columns'])
        test('intersection counts and linear disposition', intersections == case['seed_intersections']
             and linear == case['pairwise_linear'])
        test('kernel dimensions', len(basis) == case['kernel_dimension'] == 21-rank
             and all(len(v) == 21 and all(type(x) is int and 0 <= x < P for x in v) for v in basis))
        free = sorted(set(range(21))-set(pivots))
        test('complete free-coordinate identity',
             [[v[c] for c in free] for v in basis]
             == [[int(a == b) for b in range(len(free))] for a in range(len(free))])
        residuals = [[sum(x*y for x, y in zip(row, v)) % P for row in matrix] for v in basis]
        test('all kernel residuals', not any(any(row) for row in residuals))
        record = {'case': number, 'I': i, 'K': k, 'rank': rank, 'pivot_columns': pivots,
                  'seed_intersections': intersections, 'pairwise_linear': linear,
                  'kernel_basis': basis, 'kernel_residuals': residuals, 'checks': local}
        if rank == 21:
            indices = case['minor_row_indices']
            valid = len(indices) == len(set(indices)) == 21 and all(0 <= r < 24 for r in indices)
            test('minor indices', valid)
            determinant = integer_det([matrix[r] for r in indices]) if valid else 0
            test('exact integer minor witness', determinant % P == case['minor_residue'] != 0)
            record.update(minor_row_indices=indices, integer_determinant=determinant,
                          minor_residue=determinant % P)
            minors += 1
        else:
            kernels += 1
            test('deficient case fails linearity', not linear)
        vectors += len(basis)
        residual_entries += sum(map(len, residuals))
        counts[rank] += 1
        if linear:
            linear_counts[rank] += 1
        records.append(record)
    summary = {'actual_cases': len(records), 'required_cases': 756,
               'all_rank_histogram': {str(k): v for k, v in sorted(counts.items())},
               'linear_cases': sum(linear_counts.values()),
               'linear_rank_histogram': {str(k): v for k, v in sorted(linear_counts.items())},
               'linear_survivor_count': sum(v for k, v in linear_counts.items() if k < 21),
               'required_exclusion_rank': 21}
    check('all summary fields independently reconstructed', summary == source['summary'])
    check('explicit asserted classification', counts == {18: 3, 20: 135, 21: 618}
          and linear_counts == {21: 222})
    check('all saved survivors and failures empty', source['linear_survivors'] == source['failures'] == [])
    replay = subprocess.run([sys.executable, str(HERE/'fixed_three_row_extensions.py')],
                            capture_output=True, text=True)
    after = path.read_bytes()
    check('producer replay exits successfully and preserves complete certificate', replay.returncode == 0 and before == after)
    out = {'scope': 'complete independent L110 proof-program audit; fixed seed only',
           'modulus': P, 'H': H, 'S': S, 'J': J, 'seed_matrix': seed,
           'summary': summary, 'minor_witnesses_checked': minors,
           'deficient_kernels_checked': kernels, 'kernel_vectors_checked': vectors,
           'kernel_residual_entries_checked': residual_entries,
           'global_checks': checks, 'cases': records,
           'producer_replay': {'returncode': replay.returncode, 'stdout': replay.stdout,
                               'stderr': replay.stderr, 'before_sha256': sha256(before).hexdigest(),
                               'after_sha256': sha256(after).hexdigest()},
           'failures': failures}
    output = HERE/'fixed-three-row-critical-audit.json'
    output.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Minors {minors}/618; deficient kernels {kernels}/138; vectors {vectors}; '
          f'residual entries {residual_entries}; failures {len(failures)}; certificate {output}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
