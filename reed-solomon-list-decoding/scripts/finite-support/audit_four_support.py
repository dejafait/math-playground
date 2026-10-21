"""Independent complete audit of the existing L031 certificate (no imports from it).

Run from the active notebook. The original certificate is read-only.
All comparisons use whole arrays, never sampled entries.
"""
import hashlib
import json
from pathlib import Path

P = 65537
EDGES = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
SOURCE = Path(__file__).with_name('four-support-rank-results.json')
OUTPUT = Path(__file__).with_name('four-support-audit-results.json')
checks = []


def check(label, ok):
    checks.append({'check': label, 'passed': bool(ok)})


def product(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) % P
             for j in range(len(b[0]))] for i in range(len(a))]


def echelon(a):
    """Forward elimination, without normalizing pivots or clearing above them."""
    b = [row[:] for row in a]
    pivots = []
    for c in range(len(b[0])):
        r = len(pivots)
        choices = [i for i in range(r, len(b)) if b[i][c] != 0]
        if not choices:
            continue
        s = choices[-1]  # Deliberately different pivot choice from the generator.
        b[r], b[s] = b[s], b[r]
        for i in range(r + 1, len(b)):
            factor = b[i][c] * pow(b[r][c], P - 2, P) % P
            b[i] = [(b[i][j] - factor * b[r][j]) % P
                    for j in range(len(b[0]))]
        pivots.append(c)
    return {'rank': len(pivots), 'pivots': pivots, 'echelon': b}


def audit_reduction(a, saved, label):
    nr, nc = len(a), len(a[0])
    fresh = echelon(a)
    check(label + ': independently recomputed rank', fresh['rank'] == saved['rank'])
    r = saved['rref']
    check(label + ': dimensions', len(r) == nr and all(len(row) == nc for row in r))
    actual_pivots = [next(j for j, value in enumerate(row) if value)
                     for row in r if any(row)]
    pivots = saved['pivots']
    check(label + ': pivot positions and count',
          actual_pivots == pivots == sorted(set(pivots)) and len(pivots) == saved['rank'])
    check(label + ': all pivot columns and zero rows',
          all(r[i][c] == int(i == k) for k, c in enumerate(pivots) for i in range(nr))
          and all(not any(row) for row in r[len(pivots):]))
    identity = [[int(i == j) for j in range(nr)] for i in range(nr)]
    replay = [row[:] for row in a]
    transform = [row[:] for row in identity]
    operations_ok = True
    for operation in saved['operations']:
        kind, *args = operation
        if kind == 'swap':
            i, j = args
            operations_ok &= 0 <= i < nr and 0 <= j < nr and i != j
            for matrix in (replay, transform):
                matrix[i], matrix[j] = matrix[j], matrix[i]
        elif kind == 'scale':
            i, scalar = args
            operations_ok &= 0 <= i < nr and 0 < scalar < P
            for matrix in (replay, transform):
                matrix[i] = [scalar * value % P for value in matrix[i]]
        elif kind == 'add':
            i, j, scalar = args
            operations_ok &= 0 <= i < nr and 0 <= j < nr and i != j and 0 <= scalar < P
            for matrix in (replay, transform):
                matrix[i] = [(matrix[i][k] + scalar * matrix[j][k]) % P
                             for k in range(len(matrix[i]))]
        else:
            operations_ok = False
    check(label + ': every elementary operation invertible', operations_ok)
    check(label + ': replay on input and identity',
          replay == r and transform == saved['transform'])
    check(label + ': full transformation identity', product(transform, a) == r)
    free = [c for c in range(nc) if c not in pivots]
    basis = saved['kernel_basis']
    check(label + ': kernel dimensions', len(basis) == len(free)
          and all(len(v) == nc for v in basis))
    check(label + ': every kernel equation',
          all(sum(row[j] * v[j] for j in range(nc)) % P == 0 for row in a for v in basis))
    check(label + ': full free-coordinate identity',
          all(v[c] == int(i == j) for i, v in enumerate(basis) for j, c in enumerate(free)))
    check(label + ': all entries canonical residues',
          all(isinstance(x, int) and 0 <= x < P
              for matrix in (a, r, transform, basis) for row in matrix for x in row))
    fresh['operation_count'] = len(saved['operations'])
    return fresh


def root_product(points):
    coefficients = [1]
    for x in points:
        old = coefficients
        coefficients = [(-x * old[0]) % P]
        coefficients.extend((old[j-1] - x * old[j]) % P for j in range(1, len(old)))
        coefficients.append(old[-1])
    return coefficients


def convolve(a, b):
    return [sum(a[j] * b[k-j] for j in range(len(a)) if 0 <= k-j < len(b)) % P
            for k in range(len(a) + len(b) - 1)]


def evaluate(coefficients, x):
    return sum(c * pow(x, i, P) for i, c in enumerate(coefficients)) % P


def degree(coefficients):
    return max((i for i, c in enumerate(coefficients) if c), default=-1)


def audit_case(kind, saved, domain, h):
    label = kind
    exponents = [(2*r, 2*r+1) if kind == 'consecutive' else (r, r+512) for r in range(6)]
    pairs = [[domain[a], domain[b]] for a, b in exponents]
    used = set(sum(pairs, []))
    remaining = [x for x in domain if x not in used]
    core = remaining[:60]
    private = [remaining[60+2*i:62+2*i] for i in range(4)]
    pieces = [core] + pairs + private
    check(label + ': mutually disjoint prescribed pieces',
          [len(piece) for piece in pieces] == [60] + [2]*10
          and len(set(sum(pieces, []))) == 80)
    supports = [sorted(core + private[i] + sum([pair for edge, pair in zip(EDGES, pairs)
                                             if i in edge], [])) for i in range(4)]
    for name, value in [('pairs', pairs), ('core', core), ('private', private), ('supports', supports)]:
        check(label + ': entire ' + name, saved[name] == value)
    check(label + ': all support sizes and intersections',
          all(len(set(s)) == 68 for s in supports)
          and all(set(supports[i]) & set(supports[j]) == set(core + pair)
                  for (i, j), pair in zip(EDGES, pairs)))
    maps = []
    matrix = []
    for (i, j), pair in zip(EDGES, pairs):
        d = [[((int(block == i) - int(block == j)) if power == c else 0) % P
              for block in range(3) for power in range(4)] for c in range(4)]
        maps.append(d)
        for x in pair:
            matrix.append([((int(block == i) - int(block == j)) * pow(x, power, P)) % P
                           for block in range(3) for power in range(4)])
    check(label + ': every signed matrix entry', saved['matrix'] == matrix)
    check(label + ': every difference-map entry', saved['difference_maps'] == maps)
    base = audit_reduction(matrix, saved['reduction'], label + '/M')
    augments = [audit_reduction(matrix + d, s, label + '/D' + str(edge))
                for edge, d, s in zip(EDGES, maps, saved['augmented_reductions'])]
    check(label + ': all six augmented reductions present', len(saved['augmented_reductions']) == 6)
    basis = saved['reduction']['kernel_basis']
    restrictions = []
    for i, j in EDGES:
        restrictions.append([[((v[4*i+c] if i < 3 else 0) - (v[4*j+c] if j < 3 else 0)) % P
                              for v in basis] for c in range(4)])
    good = [any(value for row in r for value in row) for r in restrictions]
    check(label + ': all restriction entries', saved['kernel_restrictions'] == restrictions)
    check(label + ': all six noncontainment/rank tests',
          saved['six_noncontainments'] == good
          == [a['rank'] > base['rank'] for a in augments])
    check(label + ': realizability flag', saved['realizable'] == all(good))
    expected_rank = 12 if kind == 'consecutive' else 10
    check(label + ': claimed ranks', base['rank'] == expected_rank and all(a['rank'] == 12 for a in augments))
    witness_evidence = None
    if kind == 'consecutive':
        check(label + ': zero kernel and absent witness', basis == [] and saved['witness'] is None)
        check(label + ': identity RREF', saved['reduction']['rref']
              == [[int(i == j) for j in range(12)] for i in range(12)])
    else:
        b0 = [53800, 0, 58839, 0, 32073, 0, 15029, 0, 46060, 0, 1, 0]
        b1 = [0, 53800, 0, 58839, 0, 32073, 0, 15029, 0, 46060, 0, 1]
        check(label + ': full printed basis', basis == [b0, b1])
        witness = saved['witness']
        reduced = [b0[4*i:4*i+4] for i in range(3)] + [[0]*4]
        core_polynomial = root_product(core)
        messages = [convolve(core_polynomial, g) for g in reduced]
        evaluations = [[evaluate(f, x) for x in domain] for f in messages]
        owners = [[i for i, s in enumerate(supports) if x in s] for x in domain]
        center = [evaluations[at[0]][a] if at else 0 for a, at in enumerate(owners)]
        check(label + ': every common-center prescription',
              all(evaluations[i][a] == center[a] for a, at in enumerate(owners) for i in at))
        agreements = [[x for a, x in enumerate(domain) if evaluations[i][a] == center[a]]
                      for i in range(4)]
        equalities = [[x for a, x in enumerate(domain) if evaluations[i][a] == evaluations[j][a]]
                      for i, j in EDGES]
        witness_evidence = dict(curve_parameter=0, excluded_parameter_bound=6, vector=b0,
                                reduced_messages=reduced, core_polynomial=core_polynomial,
                                messages=messages, evaluations=evaluations, center=center,
                                center_owners=owners, agreements=agreements, pair_equality_sets=equalities)
        for key, value in witness_evidence.items():
            check(label + ': entire witness/' + key, witness[key] == value)
        check(label + ': all strict degrees and nonzero degrees',
              [degree(f) for f in messages] == [62, 62, 62, -1])
        check(label + ': complete agreement counts', list(map(len, agreements)) == [68, 68, 68, 1012])
        check(label + ': every selected agreement',
              all(set(s) <= set(a) for s, a in zip(supports, agreements)))
        check(label + ': all six exact equality sets',
              all(set(eq) == set(core + pair) for eq, pair in zip(equalities, pairs)))
        differences = [[(reduced[i][c] - reduced[j][c]) % P for c in range(4)] for i, j in EDGES]
        check(label + ': printed difference coefficients',
              [[d[0], d[2]] for d in differences]
              == [[21727, 43810], [7740, 58838], [53800, 58839],
                  [51550, 15028], [32073, 15029], [46060, 1]])
        check(label + ': each difference a nonzero quadratic multiple',
              all(d[2] != 0 and d == [(d[2]*c) % P for c in root_product(pair)] + [0]
                  for d, pair in zip(differences, pairs)))
    summary = dict(rank=base['rank'], nullity=12-base['rank'], augmented_ranks=[a['rank'] for a in augments],
                   six_noncontainments=good, realizable=all(good),
                   agreement_counts=list(map(len, witness_evidence['agreements'])) if witness_evidence else None)
    return dict(summary=summary, pairs=pairs, core=core, private=private, supports=supports,
                matrix=matrix, difference_maps=maps, independent_reduction=base,
                independent_augmented_reductions=augments, restrictions=restrictions, witness=witness_evidence)


def main():
    raw = SOURCE.read_bytes()
    saved = json.loads(raw)
    check('modulus prime by complete trial division', all(P % d for d in range(2, 257)))
    h = pow(3, 64, P)
    domain = [1]
    for _ in range(1023):
        domain.append(domain[-1] * h % P)
    check('full subgroup and generator data', saved['modulus'] == P and saved['generator'] == h == 19139
          and saved['domain'] == domain and saved['generator_half_power'] == domain[512] == P-1)
    check('exact order and subgroup membership', len(set(domain)) == 1024
          and domain[-1] * h % P == 1 and all(pow(x, 1024, P) == 1 for x in domain))
    check('ordered edges', saved['edges'] == [list(edge) for edge in EDGES])
    cases = {kind: audit_case(kind, saved['cases'][kind], domain, h)
             for kind in ('consecutive', 'antipodal')}
    summary = {kind: case['summary'] for kind, case in cases.items()}
    check('full original summary', saved['summary'] == summary)
    check('original failure list empty', saved['failures'] == [])
    expected_bounds = dict(realizable_requires_six_strict_rank_increases=True, field_size=P,
                           union_bound_requires_field_size_gt=6, unsafe_threshold_numerator=P**28,
                           unsafe_threshold_denominator=2**128, exhibited_distinct_messages=4,
                           list_upper_bound_claimed=False)
    check('all original bound qualifications', saved['bounds'] == expected_bounds)
    failures = [c['check'] for c in checks if not c['passed']]
    result = dict(source=str(SOURCE), source_sha256=hashlib.sha256(raw).hexdigest(),
                  modulus=P, generator=h, domain=domain, cases=cases, checks=checks,
                  summary=summary, bounds=expected_bounds, failures=failures)
    OUTPUT.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(summary=summary, checks=len(checks), failures=failures,
                          actual_field_size=P, required_field_size_gt=6,
                          actual_witness_degree=62, required_degree_lt=64,
                          actual_witness_size=4, unsafe_threshold_gt=2**320,
                          source=str(SOURCE), certificate=str(OUTPUT))))
    assert not failures, failures


if __name__ == '__main__':
    main()
