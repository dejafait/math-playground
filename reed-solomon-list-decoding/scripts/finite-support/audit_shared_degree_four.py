"""Independent exact audit of L030; does not import the construction script."""
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt
from pathlib import Path
import json
import re

Q = 137
POINTS = (16, 64, 70, 102, 112, 118, 121)
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def elimination_det(pairs):
    # Rows of the coefficient matrix, reduced by field Gaussian elimination.
    a = [[u*v % Q for u, v in pairs],
         [(-u-v) % Q for u, v in pairs], [1, 1, 1]]
    det = 1
    pivots = []
    for k in range(3):
        p = next((i for i in range(k, 3) if a[i][k]), None)
        if p is None:
            return 0, pivots
        if p != k:
            a[k], a[p] = a[p], a[k]
            det = -det
        pivot = a[k][k]
        pivots.append(pivot)
        det = det*pivot % Q
        inv = pow(pivot, -1, Q)
        for i in range(k+1, 3):
            ratio = a[i][k]*inv % Q
            for j in range(k, 3):
                a[i][j] = (a[i][j] - ratio*a[k][j]) % Q
    return det % Q, pivots


def main():
    old = json.loads((HERE/'shared-degree-four-results.json').read_text())
    failures = []
    checks = {}

    def check(name, ok):
        checks[name] = bool(ok)
        if not ok:
            failures.append(name)

    check('prime', all(Q % d != 0 for d in range(2, isqrt(Q)+1)))
    check('fixed_points', old['q'] == Q and tuple(old['points']) == POINTS)
    rows = []
    # Independent enumeration: choose unordered triples from all 21 pairs,
    # retain those with six distinct endpoints. No recursive matching routine.
    for pairs in combinations(tuple(combinations(POINTS, 2)), 3):
        endpoints = {x for pair in pairs for x in pair}
        if len(endpoints) != 6:
            continue
        omitted, = set(POINTS)-endpoints
        det, pivots = elimination_det(pairs)
        rows.append({'omitted': omitted, 'pairs': [list(p) for p in pairs],
                     'det_mod_137': det, 'elimination_pivots': pivots})
    rows.sort(key=lambda r: (r['omitted'], r['pairs']))
    expected_keys = {(r['omitted'], tuple(map(tuple, r['pairs']))) for r in rows}
    saved_rows = old['matching_rows']
    saved_keys = [(r['omitted'], tuple(map(tuple, r['pairs']))) for r in saved_rows]
    check('complete_unique_matchings', len(rows) == len(expected_keys) == 105)
    check('saved_complete_unique_matchings', len(saved_keys) == len(set(saved_keys)) == 105
          and set(saved_keys) == expected_keys)
    regenerated = {(r['omitted'], tuple(map(tuple, r['pairs']))): r['det_mod_137'] for r in rows}
    check('all_saved_residues_equal', all(regenerated.get(key) == row['det_mod_137']
          for key, row in zip(saved_keys, saved_rows)))
    by_omitted = {str(x): [r['det_mod_137'] for r in rows if r['omitted'] == x]
                  for x in POINTS}
    check('all_nonzero', all(r['det_mod_137'] != 0 for r in rows))
    check('saved_table_equal', by_omitted == old['determinants_by_omitted'])
    proof = (ROOT/'lemmas/L030-all-core-shared-moment-extension.md').read_text()
    printed = {m[0]: [int(x) for x in m[1].split(',')]
               for m in re.findall(r'^\| (\d+) \| ([0-9,]+) \|$', proof, re.M)}
    check('canonical_table_equal', printed == by_omitted)

    # Enumerate ALL coefficient triples; no quotient by scalar multiples and
    # no root-incidence formula is used to generate this histogram.
    histogram = [0]*8
    xs_squared = tuple(x*x % Q for x in POINTS)
    for c in range(Q):
        for b in range(Q):
            offsets = tuple((b*x+c*x2) % Q for x, x2 in zip(POINTS, xs_squared))
            for a in range(Q):
                roots = sum((a+offset) % Q == 0 for offset in offsets)
                histogram[roots] += 1
    d = histogram[:3]
    check('all_polynomials_counted', sum(histogram) == Q**3)
    check('only_zero_has_more_than_two_roots', histogram[3:] == [0, 0, 0, 0, 1])
    check('prescribed_neighbor_counts', d == [2442832, 125664, 2856]
          and d == old['neighbor_counts'])
    check('saved_monic_histogram_consistent',
          histogram[:3] == [(Q-1)*h for h in old['monic_root_histogram'][:3]]
          and not any(old['monic_root_histogram'][3:]))
    check('pair_root_formula', d[2] == comb(7, 2)*(Q-1))
    check('root_incidence_formula', d[1]+2*d[2] == 7*(Q**2-1))
    check('total_nonzero_formula', sum(d) == Q**3-1)

    v = comb(963, 7)
    L = Q**3
    rho = Fraction(L, v)
    neighbors = [comb(7, i)*comb(956, 7-i) for i in range(3)]
    pair_moments = [rho*Fraction(d[i], neighbors[i]) for i in range(3)]
    check('ordered_pair_orbits', all(v*neighbors[i]*pair_moments[i] == L*d[i]
                                   for i in range(3)))
    check('row_sum_including_diagonal', rho + sum(neighbors[i]*pair_moments[i]
                                                for i in range(3)) == L*rho)
    check('moment_bounds', all(0 <= x <= rho <= 1 for x in pair_moments))
    check('ambient_size', 7*Q+4 == 963)
    N, D = comb(1024, 61), comb(68, 61)
    T = Fraction(65537**28, 2**128)
    M = T.numerator//T.denominator
    bstar = (D*(M+1)-1)//N
    check('exact_required_cap', bstar == 1532495)
    check('strict_adjacent_cap_test', N*bstar < D*(M+1) <= N*(bstar+1))
    check('exact_cap_obstruction', L > bstar and N*L >= D*(M+1)
          and N*L//D > M)
    result = {
        'target': "L030 independent audit: all 105 determinants, pair moments, local-cap scope",
        'method': 'Unordered disjoint pair triples; modular elimination; all coefficient triples',
        'q': Q, 'points': POINTS, 'matching_rows': rows,
        'determinants_by_omitted': by_omitted,
        'full_coefficient_histogram': histogram,
        'neighbor_counts': d,
        'pair_moments': {'v': v, 'rho': str(rho), 'N_i': neighbors,
                         'F_i': [str(x) for x in pair_moments]},
        'threshold': {'T': str(T), 'M': M, 'N': N, 'D': D,
                      'required_integer_cap': bstar, 'actual_local_family_size': L,
                      'all_core_transfer_floor': N*L//D,
                      'transfer_to_threshold_ratio': str(Fraction(N*L, D)/T)},
        'checks': checks, 'failures': failures,
        'scope': 'Symbolic proof, not this script, establishes every-core independence and all-order PSD. No cross-core consistency or RS realization verified.'}
    output = HERE/'shared-degree-four-audit-results.json'
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(f"Independent determinants: {len(rows)}/105, zero residues: {sum(r['det_mod_137']==0 for r in rows)}")
    print(f"All coefficient triples: {sum(histogram)}/{Q**3}; nonzero neighbor counts: {d}")
    print(f"Actual local size: {L}; required integer cap: <= {bstar}")
    print(f"Checks: {sum(checks.values())}/{len(checks)}; failures: {failures}; certificate: {output}")
    assert not failures


if __name__ == '__main__':
    main()
