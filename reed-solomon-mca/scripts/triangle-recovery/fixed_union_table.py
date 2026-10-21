"""Bounded exact L059 tables: fixed P and U, all 90 ordered pair partitions.

Not a uniform labeling certificate. All rows and rejected gates are saved.
Independent first-four inversion and eight-moment residuals check gated
rows; both-zero cases retain all 95 scalar tests. No original chart is
replaced: the table omits E, as in L059, whose nonprime-chart construction
realizes all its rational scalars.
"""
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import json
import argparse

F = 97
H = tuple(x for x in range(1, F) if pow(x, 16, F) == 1)
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--shared-labels', type=int, nargs=3, default=list(H[:3]),
                    help='Ordered labels a b c; no shared-label symmetry assumed')
parser.add_argument('--singleton-pool', type=int, nargs=6, default=list(H[3:9]))
parser.add_argument('--output', type=Path,
                    default=Path(__file__).with_name('fixed-union-table.json'))
ARGS = parser.parse_args()
P = tuple(ARGS.shared_labels)
assert len(set(P)) == 3 and set(P) <= set(H)
S = tuple(sorted(ARGS.singleton_pool))
assert len(set(S)) == 6 and set(S) <= set(H) - set(P)
U = tuple(sorted((*P, *S)))
M0 = tuple(range(1, 96))


def inv(x):
    return pow(x % F, -1, F)


def prod(xs):
    value = 1
    for x in xs:
        value = value * x % F
    return value


def lv(x, labels, t):
    return prod((t-u) * inv(x-u) for u in labels if u != x)


def invert(matrix):
    n = len(matrix)
    rows = [list(row) + [int(i == j) for j in range(n)]
            for i, row in enumerate(matrix)]
    for j in range(n):
        i = next(i for i in range(j, n) if rows[i][j] % F)
        rows[i], rows[j] = rows[j], rows[i]
        z = inv(rows[j][j])
        rows[j] = [v*z % F for v in rows[j]]
        for i in range(n):
            if i != j:
                z = rows[i][j]
                rows[i] = [(v-z*w) % F for v, w in zip(rows[i], rows[j])]
    return [row[n:] for row in rows]


CX = {x: prod(x-h for h in H if h not in U) for x in U}
VP = {x: tuple(pow(x, j, F) for j in range(1, 9)) for x in H}
SUPPORTS = tuple(combinations(H, 4))
DIRECT = {}
for K in SUPPORTS:
    matrix = [[VP[x][j] for x in K] for j in range(8)]
    DIRECT[K] = (matrix, invert(matrix[:4]))


def label_data(K, Y, Z):
    J = tuple(x for x in P if x not in K)
    fk = {x: prod(x-k for k in K) for x in H}
    vectors = [[sum(CX[x]*x*fk[x]*prod(x-u for u in J)*pow(x, j, F)
                    for x in pair) % F for j in range(4-len(J))]
               for pair in (Y, Z)]
    beta = [[-sum(CX[u]*u*fk[u]*lv(x, J, u) for u in pair)
             * inv(x*fk[x]) % F for x in J] for pair in (Y, Z)]
    vy, vz = vectors
    if not any(vy) and not any(vz):
        kind, mu = 'both_zero', None
        assert len(J) == 3
    elif not any(vy) or not any(vz):
        kind, mu = 'one_zero', None
    else:
        j = next(j for j, v in enumerate(vy) if v)
        mu = vz[j]*inv(vy[j]) % F
        kind = ('isolated' if all((z-mu*y) % F == 0
                                 for y, z in zip(vy, vz)) else 'independent')
    return J, vectors, beta, kind, mu


def point(beta, mu):
    by, bz = beta
    ca, cb, cc = (CX[x] for x in P)
    return ((1-(bz[0]-mu*by[0])*inv(ca))*inv(1+mu) % F,
            (by[1]-bz[1]*inv(mu))*inv(cb) % F,
            (bz[2]-mu*by[2])*inv(cc) % F)


def direct_residual(K, Y, Z, weight, mu):
    a, b, c = P
    p, q, r = weight
    coeff = {x: -mu*CX[x] % F for x in Y}
    coeff.update({x: CX[x] for x in Z})
    coeff.update({a: CX[a]*(1-(1+mu)*p) % F,
                  b: -mu*CX[b]*q % F, c: CX[c]*r % F})
    numerator = [sum(v*VP[x][j] for x, v in coeff.items()) % F
                 for j in range(8)]
    matrix, inverse = DIRECT[K]
    recovered = [sum(v*w for v, w in zip(row, numerator[:4])) % F
                 for row in inverse]
    residual = [(sum(v*w for v, w in zip(row, recovered))-n) % F
                for row, n in zip(matrix, numerator)]
    return recovered, residual


def full_scalar_test(Y, Z, W, weight):
    """Full M for a seven-scalar survivor, retaining relaxed zero weights."""
    a, b, c = P
    p, q, r = weight
    base = {frozenset((a,b,*Y)), frozenset((a,c,*Z)), frozenset((b,c,*W))}
    rows, union = [], set()
    for K in SUPPORTS:
        if frozenset(K) in base:
            continue
        J, vectors, beta, kind, mu = label_data(K, Y, Z)
        tests = M0 if kind == 'both_zero' else (
            (mu,) if kind == 'isolated' and mu in M0 else ())
        by, bz = (dict(zip(J, row)) for row in beta)
        accepted = []
        for mu in tests:
            actual = {a: CX[a]*(1-(1+mu)*p) % F,
                      b: -mu*CX[b]*q % F, c: CX[c]*r % F}
            if any((actual[x]-bz[x]+mu*by[x]) % F for x in J):
                continue
            recovered, residual = direct_residual(K, Y, Z, weight, mu)
            assert not any(residual), (K, weight, mu, residual)
            union.add(mu)
            accepted.append({'mu': mu, 'omega': recovered, 'residual8': residual})
        rows.append({'K': K, 'J': J, 'projected': vectors, 'beta_Y_Z': beta,
                     'kind': kind, 'isolated_mu': mu if kind == 'isolated' else None,
                     'accepted': accepted})
    assert len(rows) == 1817
    return {'weights': weight, 'M': sorted(union), 'count': len(union), 'rows': rows}


def run():
    disjoint = tuple(K for K in SUPPORTS if not set(K).intersection(P))
    assert len(disjoint) == 715
    cases, failures = [], []
    residual_tests, zero_weight_rows, both_zero_gated = 0, 0, 0
    for Y in combinations(S, 2):
        remaining = tuple(x for x in S if x not in Y)
        for Z in combinations(remaining, 2):
            W = tuple(x for x in remaining if x not in Z)
            rows, fibers = [], defaultdict(set)
            kinds, gates = Counter(), Counter()
            for K in disjoint:
                J, vectors, beta, kind, label_mu = label_data(K, Y, Z)
                assert J == P
                kinds[kind] += 1
                tests = M0 if kind == 'both_zero' else (
                    (label_mu,) if kind == 'isolated' and label_mu in M0 else ())
                entries = []
                for mu in tests:
                    weights = point(beta, mu)
                    gated = all(x not in (0, 1) for x in weights)
                    gates['gated' if gated else 'nongated'] += 1
                    entry = {'mu': mu, 'weights': weights, 'gated': gated}
                    if gated:
                        recovered, residual = direct_residual(K, Y, Z, weights, mu)
                        entry.update({'omega': recovered, 'residual8': residual})
                        residual_tests += 1
                        if any(residual):
                            failures.append({'Y': Y, 'Z': Z, 'K': K, **entry})
                        zero_weight_rows += int(not all(recovered))
                        both_zero_gated += int(kind == 'both_zero')
                        fibers[weights].add(mu)
                    entries.append(entry)
                rows.append({'K': K, 'projected': vectors, 'beta_Y_Z': beta,
                             'kind': kind, 'isolated_mu': label_mu,
                             'tested': entries})
            survivor_weights = sorted(w for w, scalars in fibers.items() if len(scalars) >= 7)
            full_tests = [full_scalar_test(Y,Z,W,w) for w in survivor_weights]
            maximum = max(map(len, fibers.values()), default=0)
            maxima = [{'weights': w, 'D': sorted(ms)}
                      for w, ms in sorted(fibers.items()) if len(ms) == maximum]
            cases.append({'Y': Y, 'Z': Z, 'W': W, 'support_count': len(rows),
                          'kind_counts': dict(kinds), 'gate_counts': dict(gates),
                          'fiber_histogram': dict(Counter(map(len, fibers.values()))),
                          'maximum_D': maximum, 'maximal_fibers': maxima,
                          'survivor_count': len(survivor_weights), 'full_tests': full_tests,
                          'rows': rows})
    assert len(cases) == 90
    summary = {'actual_cases': len(cases), 'required_cases': 90,
               'actual_support_rows': sum(c['support_count'] for c in cases),
               'required_support_rows': 90*715,
               'maximum_D': max(c['maximum_D'] for c in cases),
               'required_violation_D': 7,
               'seven_scalar_survivors': sum(c['survivor_count'] for c in cases),
               'direct_eight_moment_tests': residual_tests,
               'both_zero_gated_rows': both_zero_gated,
               'zero_fourth_weight_rows_retained': zero_weight_rows,
               'actual_failures': len(failures), 'required_failures': 0,
               'maximum_histogram': dict(Counter(c['maximum_D'] for c in cases))}
    result = {'scope': 'Fixed P and U only; all 90 ordered pair partitions; no uniform bound',
              'H': H, 'P': P, 'U': U, 'CX': CX, 'summary': summary,
              'cases': cases, 'failures': failures}
    path = ARGS.output
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('Cases actual/required: 90/90; disjoint support rows actual/required: '
          f"{summary['actual_support_rows']}/{summary['required_support_rows']}")
    print(f"Maximum D / necessary violation threshold: {summary['maximum_D']}/7; "
          f"seven-scalar survivors: {summary['seven_scalar_survivors']}")
    print(f'Eight-moment tests: {residual_tests}; both-zero gated rows: {both_zero_gated}; '
          f'zero fourth-weight rows retained: {zero_weight_rows}; failures actual/required: '
          f'{len(failures)}/0')
    print(f'Certificate: {path}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
