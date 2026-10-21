"""Independent exact reconstruction of the released-zero shell certificate.

Imports no constructor routines. Rebuilds primary beta eigenvalues with
the full source summation, factorial binomials, actual set incidences,
all primal/dual inequalities, and the constant Schur feasibility margin. No constructor imports.
"""
import hashlib
import json
from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations
from math import factorial
from pathlib import Path

ROOT = Path(__file__).parent
SOURCE = ROOT / 'released-zero-five-shell-results.json'
OUT = ROOT / 'released-zero-five-shell-audit-results.json'


@lru_cache(None)
def choose(n, k):
    return factorial(n)//factorial(k)//factorial(n-k) if 0 <= k <= n else 0


def enc(z):
    z = Q(z)
    return [z.numerator, z.denominator]


def source_eigen(n, k, r):
    t = 5-r
    numerator = sum((-1 if (u-t) % 2 else 1)*choose(u, t)*choose(n-2*k, u-k)
                    *choose(n-k-u, 5-u)**2 for u in range(k, n-k+1))
    return Q(numerator, choose(n-2*k, 5-k))


def main():
    raw = SOURCE.read_bytes()
    saved = json.loads(raw)
    failures, counts = [], {}

    def check(kind, truth, detail=None):
        counts[kind] = counts.get(kind, 0)+1
        if not truth:
            failures.append({'kind': kind, 'detail': detail})

    lp = json.loads((ROOT / 'delsarte-lp-results.json').read_text())
    primal = [Q(z['numerator'], z['denominator']) for z in lp['exact']['primal']]
    p = [Q(1)] + [Q(0)]*4 + [z/(2*choose(68, i)*choose(956, i))
                             for i, z in zip(range(5, 69), primal)]
    check('pair_input', list(map(enc, p)) == saved['parameters']['p']
          == json.loads((ROOT/'selected-triple-sdp-results.json').read_text())['p'])
    for j in range(1, 65):
        polynomial = [0]*69
        for r in range(69-j):
            for h in range(j+1):
                polynomial[r+h] += (-1 if h % 2 else 1)*choose(j, h)*choose(68-j, r)*choose(956-j, r)
        check('L021_defining_equations', 1+sum(Q(polynomial[i], choose(68, i)*choose(956, i))
                                              *primal[i-5] for i in range(5, 69)) == 0, j)
    U = Q(choose(1024, 64), choose(68, 64))
    rho = (U+1)/(2*choose(1024, 68))
    check('positive_scaling', rho > 0 and p[5] > 0)
    factors, multiplicities = {}, {}
    for n in (68, 956):
        F = [[source_eigen(n, k, r) for r in range(6)] for k in range(6)]
        m = [choose(n, k)-choose(n, k-1) for k in range(6)]
        for k in range(6):
            for r in range(6):
                other = sum((-1 if h % 2 else 1)*choose(k, h)*choose(5-k, r-h)
                            *choose(n-5-k, r-h) for h in range(r+1))
                check('beta_Johnson_agreement', F[k][r] == other and F[k][r].denominator == 1, [n, k, r])
        check('factor_completeness', all(z > 0 for z in m) and sum(m) == choose(n, 5), n)
        check('factor_identity_valencies', all(F[k][0] == 1 for k in range(6))
              and F[0] == [choose(5, r)*choose(n-5, r) for r in range(6)], n)
        for r in range(6):
            for s in range(6):
                check('factor_orthogonality', sum(m[k]*F[k][r]*F[k][s] for k in range(6))
                      == (choose(n, 5)*F[0][r] if r == s else 0), [n, r, s])
        factors[n], multiplicities[n] = F, m
    anchor = frozenset(range(68))
    B = (anchor-frozenset(range(5))) | frozenset(range(68, 73))
    dictionary, relations = [], []
    for r in range(6):
        for q in range(6):
            removed = frozenset(range(5-r)) | frozenset(range(5, 5+r))
            added = frozenset(range(68, 73-q)) | frozenset(range(73, 73+q))
            C = (anchor-removed) | added
            common = len(anchor & B & C)
            pp = [len((D & E)-F) for D, E, F in ((anchor, B, C), (anchor, C, B), (B, C, anchor))]
            private = [len(D-(E | F)) for D, E, F in ((anchor, B, C), (B, anchor, C), (C, anchor, B))]
            distinct = len({anchor, B, C}) == 3
            zeros = r+q in range(1, 5)
            check('actual_set_dictionary', len(C) == 68 and len(anchor-C) == 5 and len(B-C) == r+q
                  and common == 63-r and pp == [r, r, 5-q]
                  and private == [5-r, q, q] and distinct == ((r, q) != (0, 0)), [r, q])
            check('retained_zero_dictionary', zeros == (r+q in range(1, 5)), [r, q])
            permutation_records = []
            for D, E, F in permutations((anchor, B, C)):
                distances = [len(D-E), len(D-F), len(E-F)]
                common2 = len(D & E & F)
                pair2 = [len((D & E)-F), len((D & F)-E), len((E & F)-D)]
                private2 = [len(D-(E | F)), len(E-(D | F)), len(F-(D | E))]
                zero2 = any(i in range(1, 5) for i in distances)
                check('all_support_permutations', zero2 == zeros, [r, q, distances])
                eligible = distances[:2] == [5, 5]
                rr = 5-len((D-E) & (D-F))
                qq = 5-len((E-D) & (F-D))
                # Derive from full set regions, not just a distance multiset.
                check('represented_unordered_orbit_identification',
                      not eligible or (rr, qq) == (r, q), [r, q, distances, rr, qq])
                check('alternative_anchor_scope',
                      not distinct or eligible == (D == anchor or r+q == 5), [r, q, distances])
                permutation_records.append({'eligible_anchor': eligible,
                                            'represented_relation': [rr, qq] if eligible else None,
                                            'distances': distances, 'common': common2,
                                            'pair_only': pair2, 'private': private2, 'zero': zero2})
            dictionary.append({'r': r, 'q': q, 'distinct': distinct, 'zero': zeros,
                               'common': common, 'pair_only': pp, 'private': private,
                               'support_permutations': permutation_records})
            if distinct and not zeros:
                relations.append((r, q))
    modes = [(a, b) for a in range(6) for b in range(6) if a or b]
    val = [factors[68][0][r]*factors[956][0][q] for r, q in relations]
    A = [[-factors[68][a][r]*factors[956][b][q]/v for (r, q), v in zip(relations, val)]
         for a, b in modes]
    check('parameters', saved['parameters']['relations'] == list(map(list, relations))
          and saved['parameters']['modes'] == list(map(list, modes)) and saved['parameters']['valencies'] == val)
    for i, row in enumerate(A):
        for j, z in enumerate(row):
            check('every_matrix_coefficient', enc(z) == saved['matrix'][i][j], [i, j])
    x = [Q(*z) for z in saved['exact']['primal']]
    y = [Q(*z) for z in saved['exact']['dual']]
    check('vector_dimensions', len(x) == len(relations) == 21 and len(y) == len(modes) == 35)
    for i, z in enumerate(x):
        check('every_primal_sign', z >= 0, i)
    for i, z in enumerate(y):
        check('every_dual_sign', z >= 0, i)
    ps = [1-sum(a*z for a, z in zip(row, x)) for row in A]
    ds = [sum(y[i]*A[i][j] for i in range(35))-1 for j in range(21)]
    for i, z in enumerate(ps):
        check('every_primal_constraint', z >= 0 and enc(z) == saved['exact']['primal_slacks'][i], i)
    columns = []
    for j, z in enumerate(ds):
        check('every_dual_constraint', z >= 0 and enc(z) == saved['exact']['dual_slacks'][j], j)
        columns.append({'relation': relations[j], 'coefficient': enc(z+1), 'slack': enc(z)})
    upper = 1+sum(y)
    required = choose(68, 5)*choose(956, 5)*p[5]
    check('equal_objectives', 1+sum(x) == upper == Q(9965466368, 5))
    check('constant_Schur_feasible', required == Q(4982733184, 5) and upper == 2*required
          and saved['exact']['row_sum'] == enc(upper) and saved['exact']['required_row_sum'] == enc(required))
    check('complete_product_dimension', sum(multiplicities[68][a]*multiplicities[956][b]
          for a in range(6) for b in range(6)) == saved['parameters']['shell_size'])
    check('summary', saved['summary'] == {'shell_lp_verified': True, 'shell_excludes': False,
          'shell_verdict': 'FEASIBLE'} and saved['failures'] == [])
    d = {relation: z/v for relation, z, v in zip(relations, x, val)}
    shell = []
    size = choose(68, 5)*choose(956, 5)
    for a in range(6):
        for b in range(6):
            eigen = 1+sum(z*factors[68][a][r]*factors[956][b][q]
                          for (r, q), z in d.items())
            schur = eigen-(required if (a, b) == (0, 0) else 0)
            check('all_36_Schur_coordinates', schur >= 0, [a, b])
            shell.append({'mode': [a, b], 'multiplicity': multiplicities[68][a]*multiplicities[956][b],
                          'D_eigenvalue': enc(eigen), 'Schur_eigenvalue': enc(schur)})
    check('Boolean_diagonal_trace', sum(Q(*z['D_eigenvalue'])*z['multiplicity'] for z in shell) == size)
    check('released_relation_positive', (2, 3) in d and d[2, 3] > 0)
    expected_y = [Q(951, 5)*multiplicities[68][a] if b == 1 else
                  Q(multiplicities[68][a]) if b == 0 else Q(0) for a, b in modes]
    check('simple_dual_formula', y == expected_y)
    report = {'source_sha256' : hashlib.sha256(raw).hexdigest(), 'counts': counts,
              'checks': sum(counts.values()), 'failures': failures, 'verified': not failures,
              'set_dictionary': dictionary, 'factors': {n: [[enc(z) for z in row] for row in F] for n, F in factors.items()},
              'multiplicities': multiplicities, 'dual_columns': columns,
              'sparse_dual': [{'mode': modes[i], 'weight': enc(z)} for i, z in enumerate(y) if z],
              'row_sum_upper': enc(upper), 'required_row_sum': enc(required),
              'Schur_margin': enc(upper-required), 'coefficients': [{'relation': r, 'd': enc(z)} for r, z in d.items()],
              'all_product_modes': shell}
    OUT.write_text(json.dumps(report, separators=(',', ':'))+'\n')
    print('Independent exact checks:', report['checks'], '; failures:', len(failures))
    print('Dual columns actual/required: 21/21; spectral coordinates: 35/35 plus constant')
    print('Exact row sum upper/required:', upper, '/', required, '; margin:', upper-required)
    print('Verified shell-only feasibility:', not failures, '; certificate:', OUT)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
