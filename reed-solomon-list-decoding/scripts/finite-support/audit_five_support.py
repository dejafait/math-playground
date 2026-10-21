"""Independent, exhaustive audit of L040's fixed certificate; no imports from it."""
import hashlib
import itertools
import json
from pathlib import Path

P = 65537
ROOT = Path(__file__).parent
SOURCE = ROOT / 'five-support-rank-results.json'
OUT = ROOT / 'five-support-audit-results.json'


def eye(n):
    return [[int(r == c) for c in range(n)] for r in range(n)]


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) % P
             for j in range(len(b[0]))] for i in range(len(a))]


def main():
    original_bytes = SOURCE.read_bytes()
    saved = json.loads(original_bytes)
    checks = {}

    def check(name, value):
        checks[name] = bool(value)

    # Repeated multiplication, rather than the original pow-per-entry generator.
    h = pow(3, 64, P)
    domain = [1]
    for _ in range(1023):
        domain.append(domain[-1] * h % P)
    check('field_prime', all(P % d for d in range(2, 257)))
    check('generator', h == 19139 == saved['generator'])
    check('modulus', saved['modulus'] == P)
    check('order', domain[512] == P-1 and domain[-1]*h % P == 1)
    check('domain', domain == saved['domain'] and len(set(domain)) == 1024
          and 0 not in domain)
    check('generator_checks', saved['generator_checks'] ==
          {'power_1024': 1, 'power_512': P-1})
    edges = [(i, j) for i in range(1, 6) for j in range(i+1, 6)]
    core = domain[20:79]
    overlaps = [[domain[2*r], domain[2*r+1]] for r in range(10)]
    private = [[domain[79+i]] for i in range(5)]
    check('edges', saved['edges'] == [list(e) for e in edges])
    check('core', saved['core'] == core and len(core) == 59)
    check('overlaps', saved['overlaps'] == overlaps)
    check('private', saved['private'] == private)
    pieces = core + sum(overlaps, []) + sum(private, [])
    check('all_84_points', len(pieces) == len(set(pieces)) == 84)
    # Assign membership point by point, rather than unioning incident pieces.
    owners = {x: set(range(1, 6)) for x in core}
    for e, pair in zip(edges, overlaps):
        for x in pair:
            owners[x] = set(e)
    for i, point in enumerate(private, 1):
        owners[point[0]] = {i}
    supports = [sorted(x for x, members in owners.items() if i in members)
                for i in range(1, 6)]
    for i in range(5):
        check(f'support_{i+1}', supports[i] == saved['supports'][i]
              and len(supports[i]) == 68)
    pairs, higher = [], []
    for size in range(2, 6):
        for indices in itertools.combinations(range(1, 6), size):
            actual = sorted(x for x in domain
                            if all(x in supports[i-1] for i in indices))
            expected = sorted(core + (overlaps[edges.index(indices)] if size == 2 else []))
            check('intersection_' + ''.join(map(str, indices)), actual == expected)
            if size == 2:
                pairs.append({'edge': list(indices), 'points': actual})
            else:
                higher.append({'indices': list(indices), 'points': actual})
    check('saved_pair_intersections', pairs == saved['pair_intersections'])
    check('saved_higher_intersections', higher == saved['higher_intersections'])

    # A column is the elementary monomial in one nonreference message.
    columns = [(message, degree) for message in range(1, 5) for degree in range(5)]
    maps, matrix, labels = [], [], []
    for edge, pair in zip(edges, overlaps):
        i, j = edge
        d = [[((message == i) - (message == j)) % P if deg == degree else 0
              for message, deg in columns] for degree in range(5)]
        maps.append({'edge': list(edge), 'coefficient_map': d})
        check(f'map_{i}{j}', maps[-1] == saved['difference_maps'][len(maps)-1])
        for x in pair:
            row = [((message == i) - (message == j)) * pow(x, degree, P) % P
                   for message, degree in columns]
            matrix.append(row)
            labels.append({'edge': list(edge), 'point': x})
            check(f'row_{len(matrix)-1}', row == saved['matrix'][len(matrix)-1])
    check('complete_matrix', matrix == saved['matrix'])
    check('row_labels', labels == saved['row_labels'])
    check('complete_maps', maps == saved['difference_maps'])

    # Every saved operation is validated and applied to [M | I].
    red = saved['reduction']
    augmented = [row[:] + unit for row, unit in zip(matrix, eye(20))]
    replay = []
    raw, swaps, operation_det = [], 0, 1
    for index, op in enumerate(red['operations']):
        kind, i, j, c = op
        valid = (0 <= i < 20 and 0 <= j < 20 and 0 <= c < P)
        valid = valid and ((kind == 'swap' and i != j and c == 0)
                          or (kind == 'scale' and i == j and c != 0)
                          or (kind == 'add' and i != j))
        check(f'operation_{index}_invertible', valid)
        if not valid:
            raise ValueError(f'Invalid operation {index}: {op}')
        pivot = None
        if kind == 'swap':
            augmented[i], augmented[j] = augmented[j], augmented[i]
            swaps += 1
            operation_det = -operation_det % P
        elif kind == 'scale':
            pivot = augmented[i][i]
            check(f'scale_{len(raw)}_pivot', i == len(raw) and pivot != 0
                  and pivot*c % P == 1)
            raw.append(pivot)
            augmented[i] = [c*x % P for x in augmented[i]]
            operation_det = operation_det*c % P
        else:
            augmented[i] = [(x+c*y) % P for x, y in zip(augmented[i], augmented[j])]
        replay.append({'index': index, 'operation': op, 'raw_pivot': pivot,
                       'state': [row[:] for row in augmented]})
    final, transform = [r[:20] for r in augmented], [r[20:] for r in augmented]
    check('rref_complete', final == red['rref'] == eye(20))
    check('transform_complete', transform == red['transform'])
    check('left_inverse_every_entry', multiply(transform, matrix) == eye(20))
    check('right_inverse_every_entry', multiply(matrix, transform) == eye(20))
    check('pivots', red['pivots'] == list(range(20)))
    check('raw_pivots', raw == red['raw_pivots'] and len(raw) == 20)
    check('swap_count_and_sign', swaps == red['swap_count'] == 3
          and red['determinant_sign'] == (-1)**swaps)
    det_replay = pow(operation_det, -1, P)
    check('determinant_from_operations', det_replay == red['determinant'] == 52987)

    # Exact integer Bareiss elimination uses neither modular inversion nor
    # the saved pivot strategy. Exact divisions certify the recurrence.
    b = [row[:] for row in matrix]
    previous, sign = 1, 1
    bareiss = []
    for k in range(19):
        pivot_row = next(i for i in range(19, k-1, -1) if b[i][k])
        if pivot_row != k:
            b[k], b[pivot_row] = b[pivot_row], b[k]
            sign = -sign
        pivot = b[k][k]
        divisions = []
        for i in range(k+1, 20):
            for j in range(k+1, 20):
                numerator = pivot*b[i][j] - b[i][k]*b[k][j]
                quotient, remainder = divmod(numerator, previous)
                divisions.append([i, j, numerator, previous, quotient, remainder])
                b[i][j] = quotient
        check(f'bareiss_{k}_exact_divisions', all(v[-1] == 0 for v in divisions))
        for i in range(k+1, 20):
            b[i][k] = 0
        bareiss.append({'column': k, 'pivot_row': pivot_row, 'pivot': pivot,
                        'divisions': divisions, 'matrix': [row[:] for row in b]})
        previous = pivot
    integer_det = sign*b[-1][-1]
    check('independent_integer_determinant', integer_det % P == 52987
          == saved['independent_determinant'])
    check('rank', red['rank'] == 20 and integer_det % P != 0)
    check('kernel', saved['kernel_basis'] == [])
    # Express every row of each difference map in the row span of M.
    distinctions = []
    for item in maps:
        d = item['coefficient_map']
        coefficients = multiply(d, transform)
        valid = multiply(coefficients, matrix) == d
        edge_name = ''.join(map(str, item['edge']))
        check('difference_row_span_' + edge_name, valid)
        distinctions.append({'edge': item['edge'], 'row_span_coefficients': coefficients,
                             'identity_verified': valid, 'augmented_rank': 20})
    expected_distinctions = [{'edge': list(e), 'restriction_to_kernel': 'zero',
                             'augmented_rank': 20, 'possible': False} for e in edges]
    check('saved_ten_distinctions', saved['distinctions'] == expected_distinctions)
    check('saved_bounds', saved['bounds'] == {'actual_rank': 20, 'required_full_rank': 20,
          'reduced_degree_max': 4, 'message_degree_max': 63, 'required_message_degree_lt': 64})
    check('original_report', len(saved['checks']) == 41 and all(saved['checks'].values())
          and saved['failures'] == [] and saved['conclusion'] == 'forbidden for every m>=1')
    check('generator_script_hash', saved['script_sha256'] == hashlib.sha256(
          (ROOT / 'five_support_rank.py').read_bytes()).hexdigest())
    check('source_unchanged', SOURCE.read_bytes() == original_bytes)
    failures = [key for key, value in checks.items() if not value]
    result = {'source_sha256': hashlib.sha256(original_bytes).hexdigest(),
              'audit_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'domain': domain, 'core': core, 'overlaps': overlaps, 'private': private,
              'point_owners': {str(x): sorted(v) for x, v in owners.items()},
              'supports': supports, 'pair_intersections': pairs, 'higher_intersections': higher,
              'matrix': matrix, 'difference_maps': maps, 'row_labels': labels,
              'operation_replay': replay, 'inverse': transform, 'bareiss': bareiss,
              'integer_determinant': integer_det, 'determinant_mod_p': integer_det % P,
              'distinctions': distinctions, 'checks': checks, 'failures': failures,
              'summary': {'actual_rank': 20 if integer_det % P else None, 'required_rank': 20,
                          'determinant': integer_det % P, 'required_determinant': 52987,
                          'operations': len(replay), 'inverse_entries_checked_each_order': 400,
                          'difference_maps': 10, 'intersections': len(pairs)+len(higher),
                          'checks': len(checks), 'failures': failures}}
    OUT.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'summary': result['summary'], 'certificate': str(OUT)}, indent=2))
    assert not failures


if __name__ == '__main__':
    main()
