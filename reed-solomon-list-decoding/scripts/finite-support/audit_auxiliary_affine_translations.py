"""Independent complete audit of L049; no producer/helper imports.

Input shards remain untouched. Rebuild labels using successive powers,
intersections as full supports, and stars from column incidence partitions.
Independent rank/determinant: transpose, reverse coordinate order, forward
eliminate using the LAST available pivot (not the producer's Gauss-Jordan).
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
SRC = HERE / 'embedded-quadratic-affine-translations'
OUT = HERE / 'auxiliary-affine-translation-audit-results.json'
P, A, G, N = 65537, 137, 19139, 12
T = [16, 64, 70, 102, 112, 118, 121]
Q = [[33, 27, 3], [106, 120, 2], [0, 0, 0], [64, 44, 1], [34, 47, 2]]
IDENTITY = [[int(i == j) for j in range(N)] for i in range(N)]
REPORT = {'required_parameters': A*A, 'required_rank': N, 'completed_parameters': 0,
          'checks': 0, 'failures': [], 'shards': [], 'cases': [], 'operation_count': 0,
          'full_intersections_checked': 0, 'rank_distribution': {}, 'singular_parameters': []}
CONTEXT = 'startup'


def save_report():
    # Preserve complete set/path-valued mismatch evidence as JSON too.
    OUT.write_text(json.dumps(REPORT, separators=(',', ':'),
        default=lambda value: sorted(value) if isinstance(value, set) else str(value))+'\n')


def check(name, actual, expected=True):
    REPORT['checks'] += 1
    if actual != expected:
        REPORT['failures'].append({'context': CONTEXT, 'check': name,
                                   'actual': actual, 'expected': expected})
        raise ValueError(f'{CONTEXT}: {name}')


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def independent_elimination(mat, rational=False):
    # Transpose and reverse BOTH row/column orders; their determinant signs
    # cancel. Hence this matrix has exactly det(mat), not merely its rank.
    rows = [list(col)[::-1] for col in zip(*mat)][::-1]
    if rational:
        rows = [[Fraction(x) for x in row] for row in rows]
    rank, det, pivots = 0, 1, []
    for column in range(N):
        at = next((i for i in range(N-1, rank-1, -1) if rows[i][column]), None)
        if at is None:
            continue
        if at != rank:
            rows[rank], rows[at] = rows[at], rows[rank]
            det = -det
        pivot = rows[rank][column]
        det *= pivot
        if not rational:
            det %= P
        pivots.append({'column': column, 'swap_row': at,
                       'pivot': str(pivot) if rational else pivot})
        for i in range(rank+1, N):
            multiplier = rows[i][column]/pivot if rational else rows[i][column]*pow(pivot, -1, P) % P
            for j in range(column, N):
                value = rows[i][j]-multiplier*rows[rank][j]
                rows[i][j] = value if rational else value % P
        rank += 1
    if rank != N:
        det = 0
    return rank, det if rational else det % P, pivots


def verify_product(left, right, target):
    return all(sum(left[i][k]*right[k][j] for k in range(N)) % P == target[i][j]
               for i in range(N) for j in range(N))


def reconstruct(a, b, powers, core):
    coeff = [[(q[0]+b) % A, (q[1]+a) % A, q[2]] for q in Q]
    values = [[((q[2]*t+q[1])*t+q[0]) % A for t in T] for q in coeff]
    exponents = [[61+A*j+v for j, v in enumerate(row)] for row in values]
    labels = [[powers[e] for e in row] for row in exponents]
    supports = [set(core) | set(row) for row in labels]
    check('five distinct graph supports of size 68',
          len(set(map(frozenset, supports))) == 5 and all(len(s) == 68 for s in supports))
    intersections = []
    for size in range(1, 6):
        for indices in combinations(range(5), size):
            full = supports[indices[0]].copy()
            for i in indices[1:]:
                full.intersection_update(supports[i])
            equal_columns = {powers[61+A*j+values[indices[0]][j]] for j in range(7)
                             if len({values[i][j] for i in indices}) == 1}
            check('full intersection versus column equality', full, set(core) | equal_columns)
            intersections.append({'indices': list(indices), 'outside': sorted(full-set(core))})
    check('five-way intersection is precisely core', intersections[-1]['outside'], [])
    # Build full incident sets by auxiliary column partition, including singleton
    # points. Their actual-label sorted order determines the required row order.
    incident_by_label = {}
    for j in range(7):
        for v in set(row[j] for row in values):
            incident_by_label[powers[61+A*j+v]] = [i for i in range(5) if values[i][j] == v]
    stars, matrix = [], []
    for x, indices in sorted(incident_by_label.items()):
        for other in indices[1:]:
            anchor = indices[0]
            stars.append({'point': x, 'anchor': anchor, 'other': other, 'incident': indices})
            row = [0]*15
            for d, term in enumerate([1, x, x*x % P]):
                row[3*anchor+d] = term
                row[3*other+d] = -term % P
            matrix.append(row[:12])
    check('complete matrix dimensions', len(matrix) == N and all(len(row) == N for row in matrix))
    return {'parameter': [a, b], 'polynomials': coeff, 'graph_values': values,
            'label_exponents': exponents, 'outside_labels': labels,
            'supports': [sorted(s) for s in supports], 'subset_intersections': intersections,
            'stars': stars, 'matrix': matrix}


def audit_case(saved, expected):
    for key, value in expected.items():
        check('reconstructed '+key, saved[key], value)
    matrix = expected['matrix']
    # Replay on one augmented matrix, so every operation is applied to BOTH
    # original columns and the identity columns by a single loop.
    augmented = [matrix[i][:]+IDENTITY[i][:] for i in range(N)]
    inverse_det = 1
    for op in saved['operations']:
        check('operation arity/type', len(op) in (3, 4) and op[0] in ('swap', 'scale', 'subtract'))
        kind, i = op[:2]
        check('target row index', type(i) is int and 0 <= i < N)
        if kind == 'swap':
            check('swap arity', len(op), 3)
            j = op[2]
            check('swap source index', type(j) is int and 0 <= j < N and i != j)
            augmented[i], augmented[j] = augmented[j], augmented[i]
            inverse_det = -inverse_det % P
        elif kind == 'scale':
            check('scale arity', len(op), 3)
            scalar = op[2]
            check('scale is nonzero residue', type(scalar) is int and 0 < scalar < P)
            augmented[i] = [(x*scalar) % P for x in augmented[i]]
            inverse_det = inverse_det*scalar % P
        else:
            check('subtract arity', len(op), 4)
            j, scalar = op[2:]
            check('subtract operands', type(j) is int and 0 <= j < N and i != j
                  and type(scalar) is int and 0 <= scalar < P)
            augmented[i] = [(augmented[i][k]-scalar*augmented[j][k]) % P for k in range(2*N)]
    reduced = [row[:N] for row in augmented]
    transform = [row[N:] for row in augmented]
    check('complete replay RREF', saved['rref'], reduced)
    check('complete replay transform', saved['row_transform'], transform)
    leading = [next((j for j, x in enumerate(row) if x), None) for row in reduced]
    pivots = [x for x in leading if x is not None]
    rank = len(pivots)
    check('RREF leading/zero-row order', leading, sorted(set(pivots))+[None]*(N-rank))
    check('RREF pivot columns', all(reduced[i][c] == int(i == r)
                                   for r, c in enumerate(pivots) for i in range(N)))
    check('saved pivots', saved['pivots'], pivots)
    check('saved rank', saved['rank'], rank)
    check('saved required rank', saved['required_full_rank'], N)
    check('whole transformation identity', verify_product(transform, matrix, reduced))
    independent_rank, independent_det, rank_trace = independent_elimination(matrix)
    check('independent rank agreement', independent_rank, rank)
    determinant = pow(inverse_det, -1, P) if rank == N else 0
    check('independent determinant agreement', independent_det, determinant)
    check('saved determinant', saved['determinant_mod_P'], determinant)
    check('full rank', rank, N)
    check('reduced identity', reduced, IDENTITY)
    check('left inverse all entries', verify_product(transform, matrix, IDENTITY))
    check('right inverse all entries', verify_product(matrix, transform, IDENTITY))
    check('no saved kernel', saved['nonzero_kernel'], None)
    check('verification flags agree with independent checks', saved['verification'], {
        'support_and_incidence': True, 'complete_operation_replay': True,
        'full_transformation_identity': True, 'rref_including_zero_rows': True,
        'both_inverse_identities': True, 'nonzero_kernel_checked': False})
    REPORT['operation_count'] += len(saved['operations'])
    REPORT['full_intersections_checked'] += 31
    return {'parameter': expected['parameter'], 'rank': independent_rank,
            'determinant_mod_P': independent_det, 'independent_column_trace': rank_trace,
            'operations_replayed': len(saved['operations']), 'all_checks_passed': True}


def audit_integer_trace(matrix, saved):
    old = [r[:] for r in matrix]
    previous, sign, divisions = 1, 1, 0
    trace = saved['bareiss_trace']
    check('integer trace length', len(trace), N-1)
    for k, step in enumerate(trace):
        check('integer trace column', step['column'], k)
        row = next((i for i in range(k, N) if old[i][k]), None)
        check('integer trace pivot selection', step['swap_row'], row)
        if row != k:
            old[k], old[row] = old[row], old[k]
            sign = -sign
        check('integer trace previous divisor', step['previous_divisor'], previous)
        pivot = old[k][k]
        check('integer trace pivot value', step['pivot'], pivot)
        check('integer trace nonzero divisors', pivot != 0 and previous != 0)
        new = [r[:] for r in old]
        for i in range(k+1, N):
            new[i][k] = 0
            for j in range(k+1, N):
                numerator = old[i][j]*pivot-old[i][k]*old[k][j]
                quotient, remainder = divmod(numerator, previous)
                check('integer trace exact division', remainder, 0)
                new[i][j] = quotient
                divisions += 1
        check('complete integer trace state', step['matrix'], new)
        old, previous = new, pivot
    det = sign*old[-1][-1]
    rank, rational_det, rational_trace = independent_elimination(matrix, rational=True)
    check('rational determinant denominator', rational_det.denominator, 1)
    check('rational determinant equals integer trace', int(rational_det), det)
    check('saved integer determinant', saved['integer_determinant'], det)
    check('saved base residue', saved['determinant_mod_P'], det % P)
    check('base expected residue', det % P, 26669)
    check('base match flags', saved['matrix_matches'] and saved['inverse_matches'])
    return {'integer_determinant': det, 'determinant_mod_P': det % P,
            'rank': rank, 'exact_divisions_checked': divisions,
            'complete_saved_states_checked': len(trace), 'rational_column_trace': rational_trace}


def main():
    global CONTEXT
    summary = json.loads((SRC/'summary.json').read_text())
    REPORT['source_summary_sha256'] = digest(SRC/'summary.json')
    REPORT['audit_script_sha256'] = digest(Path(__file__))
    powers = [1]
    for _ in range(1023):
        powers.append(powers[-1]*G % P)
    core = powers[:61]
    check('field prime', all(P % d for d in range(2, 257)))
    check('auxiliary field prime', all(A % d for d in range(2, 12)))
    check('generator and exact order', G == pow(3, 64, P) and powers[-1]*G % P == 1
          and powers[512] == P-1 and len(set(powers)) == 1024)
    check('full label and dummy bijection', len(set(powers[61:1020])) == 959
          and len(set(powers[1020:])) == 4 and set(powers[:61]).isdisjoint(powers[61:]))
    check('summary parameters', summary['parameters'], {'prime': P, 'auxiliary_prime': A,
          'generator': G, 'T': T, 'polynomials': Q, 'core': core, 'count': A*A,
          'order': 'lexicographic (a,b)'})
    original_path = HERE/'embedded-quadratic-search-results.json'
    check('original hash', digest(original_path), summary['original_certificate_sha256'])
    check('original audited hash', digest(original_path),
          '40157ba7440ef639ec238405c7c25f5b03ec1b07b6d5d69b10abb2974a985b49')
    original = json.loads(original_path.read_text())['trials'][10]
    check('exact shard filenames', sorted(p.name for p in SRC.glob('a-*.json')),
          [f'a-{a:03d}.json' for a in range(A)])
    check('summary shard count', len(summary['certificates']), A)
    counts = Counter()
    for a in range(A):
        CONTEXT = f'shard {a}'
        path = SRC/f'a-{a:03d}.json'
        raw_hash = digest(path)
        check('shard metadata/hash', summary['certificates'][a],
              {'path': str(path.relative_to(HERE)), 'a': a, 'cases': A, 'sha256': raw_hash})
        shard = json.loads(path.read_text())
        check('shard shared core', shard['core'], core)
        check('shard cases count', len(shard['cases']), A)
        for b, case in enumerate(shard['cases']):
            CONTEXT = [a, b]
            start_checks = REPORT['checks']
            expected = reconstruct(a, b, powers, core)
            record = audit_case(case, expected)
            if a == b == 0:
                check('base original matrix', expected['matrix'], original['matrix'])
                check('base original stars', expected['stars'], original['row_labels'])
                check('base original inverse', case['row_transform'], original['row_transform'])
                REPORT['base_integer_audit'] = audit_integer_trace(expected['matrix'], summary['unshifted_check'])
            record['checks_passed'] = REPORT['checks']-start_checks
            REPORT['cases'].append(record)
            REPORT['completed_parameters'] += 1
            counts[record['rank']] += 1
        REPORT['shards'].append({'a': a, 'sha256': raw_hash, 'cases_audited': A})
        REPORT['rank_distribution'] = dict(sorted(counts.items()))
        if a % 20 == 0 or a == A-1:
            save_report()
            print(f'a={a}: cases {REPORT["completed_parameters"]}/{A*A}, rank {N}/{N}, failures 0', flush=True)
    CONTEXT = 'aggregate'
    check('aggregate parameter coverage', REPORT['completed_parameters'], A*A)
    check('original completion count', summary['completed_parameters'], A*A)
    check('original operation count', summary['operation_count'], REPORT['operation_count'])
    check('original rank distribution', summary['rank_distribution'], {str(k): v for k, v in counts.items()})
    check('no original singular parameters', summary['singular_parameters'], [])
    check('no original failure records', summary['failures'], [])
    check('no saved singular cases', list(SRC.glob('singular-*.json')), [])
    check('all intersections audited', REPORT['full_intersections_checked'], 31*A*A)
    REPORT['completed'] = True


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        if not REPORT['failures']:
            REPORT['failures'].append({'context': CONTEXT, 'error': repr(exc)})
        raise
    finally:
        save_report()
        print(json.dumps({k: REPORT.get(k) for k in ('completed', 'completed_parameters',
            'required_parameters', 'rank_distribution', 'required_rank', 'checks',
            'operation_count', 'full_intersections_checked', 'failures')}, sort_keys=True))
        print('Certificate:', OUT.relative_to(HERE.parent.parent))
