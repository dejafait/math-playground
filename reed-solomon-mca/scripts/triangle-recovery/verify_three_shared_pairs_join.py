"""Independent complete row/pair replay for distinct saved seed/best assignments.

This verifies the selected assignments, not the full search prefix or a
uniform exclusion. Uses recurrence-column elimination and Gaussian recovery,
instead of the producer's G_J quotient and Lagrange numerator recovery.
"""
from itertools import combinations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
MOD = 97


def prod(xs):
    out = 1
    for x in xs:
        out = out*x % MOD
    return out


def solve(matrix, rhs):
    rows = [[v % MOD for v in row]+[b % MOD] for row, b in zip(matrix, rhs)]
    for j in range(len(rhs)):
        pivot = next(i for i in range(j, len(rhs)) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        scale = pow(rows[j][j], -1, MOD)
        rows[j] = [v*scale % MOD for v in rows[j]]
        for i in range(len(rhs)):
            if i != j:
                scale = rows[i][j]
                rows[i] = [(v-scale*w) % MOD for v, w in zip(rows[i], rows[j])]
    return [row[-1] for row in rows]


def moments(error):
    return [sum(v*pow(x, j, MOD) for x, v in error.items()) % MOD for j in range(1, 9)]


def recurrence(K, vector):
    coeff = [1]
    for x in K:
        out = [0]*(len(coeff)+1)
        for j, v in enumerate(coeff):
            out[j] = (out[j]-x*v) % MOD
            out[j+1] = (out[j+1]+v) % MOD
        coeff = out
    return [sum(v*vector[i+j] for j, v in enumerate(coeff)) % MOD for i in range(4)]


def row_key(row):
    return row['tag'], tuple(sorted(row['support'])), row['mu'], tuple(row['weights'])


def verify(path, saved=None):
    if saved is None:
        saved = json.loads(path.read_text())
    H = [x for x in range(1, MOD) if pow(x, 16, MOD) == 1]
    P = [saved[k] for k in ('a', 'b', 'c')]
    a, b, c = P
    Y, Z, W = [saved[k] for k in ('Y', 'Z', 'W')]
    U = P+Y+Z+W
    assert len(set(U)) == 9
    cx = {x: prod(x-h for h in H if h not in U) for x in U}
    bases = [set([a, b]+Y), set([a, c]+Z), set([b, c]+W)]
    rows, eligible_tests = [], 0
    for tag in range(3):
        for K in combinations(H, 4):
            if set(K) & set(P) != {P[tag]} or any(len(set(K) & B) > 1 for B in bases):
                continue
            eligible_tests += 1
            J = [x for x in P if x not in K]
            columns = [recurrence(K, moments({x: 1})) for x in J]
            raw = [recurrence(K, moments({x: cx[x] for x in pair})) for pair in (Y, Z)]
            betas, quotients = [], []
            for vector in raw:
                beta = solve([[col[j] for col in columns] for j in range(2)], [-v for v in vector[:2]])
                residual = [(vector[j]+sum(t*col[j] for t, col in zip(beta, columns))) % MOD for j in range(4)]
                assert residual[:2] == [0, 0]
                betas.append(beta)
                quotients.append(residual[2:])
            yy, zz = quotients
            if not any(yy) or not any(zz):
                continue
            pivot = next(i for i, v in enumerate(yy) if v)
            mu = zz[pivot]*pow(yy[pivot], -1, MOD) % MOD
            if mu in (0, 96) or any((z-mu*y) % MOD for y, z in zip(yy, zz)):
                continue
            weights = [-1]*3
            for j, x in enumerate(J):
                delta = (betas[1][j]-mu*betas[0][j])*pow(cx[x], -1, MOD) % MOD
                if x == a:
                    weights[0] = (1-delta)*pow(1+mu, -1, MOD) % MOD
                elif x == b:
                    weights[1] = -delta*pow(mu, -1, MOD) % MOD
                else:
                    weights[2] = delta
            if any(weights[j] in (0, 1) for j in range(3) if j != tag):
                continue
            rows.append({'tag': tag, 'support': list(K), 'mu': mu, 'weights': weights,
                         'recurrence_columns': columns, 'raw_YZ': raw,
                         'beta_YZ': betas, 'quotient_YZ': quotients})
    assert len(rows) == len(saved['rows'])
    assert {row_key(r) for r in rows} == {row_key(r) for r in saved['rows']}
    pairs = [[], [], []]
    for i, j in combinations(range(len(rows)), 2):
        x, y = rows[i], rows[j]
        if x['tag'] == y['tag'] and x['weights'] == y['weights'] and x['mu'] != y['mu'] and len(set(x['support']) & set(y['support'])) == 1:
            pairs[x['tag']].append([i, j])
    def pair_keys(rowlist, pairlist):
        return {tuple(sorted([row_key(rowlist[i]), row_key(rowlist[j])])) for i, j in pairlist}
    for tag in range(3):
        assert pair_keys(rows, pairs[tag]) == pair_keys(saved['rows'], saved['pairs'][tag])

    # Independently replay all three-tag joins at the common normalized weights.
    weight_joins, linear_distinct_joins = [], []
    for pa in pairs[0]:
        for pb in pairs[1]:
            wa, wb = rows[pa[0]]['weights'], rows[pb[0]]['weights']
            if wa[2] != wb[2]:
                continue
            weights = [wb[0], wa[1], wa[2]]
            for pc in pairs[2]:
                wc = rows[pc[0]]['weights']
                if wc[:2] != weights[:2]:
                    continue
                ids = pa+pb+pc
                weight_joins.append({'weights': weights, 'rows': ids})
                if len({rows[i]['mu'] for i in ids}) == 6 and all(len(set(rows[i]['support']) & set(rows[j]['support'])) <= 1 for i, j in combinations(ids, 2)):
                    linear_distinct_joins.append({'weights': weights, 'rows': ids})

    # Verify every saved tag pair as a full local pair if a free-weight choice
    # exists. Failure to find fullness is recorded, not silently discarded.
    full_pairs = []
    for tag in range(3):
        for ids in pairs[tag]:
            found = None
            for free in range(2, MOD):
                pqr = list(rows[ids[0]]['weights'])
                pqr[tag] = free
                p, q, r = pqr
                rho = next(t for t in range(2, MOD) if all((t-(1-t)*rows[i]['mu']) % MOD for i in ids))
                alpha = [(1-rho) % MOD, rho, 96]
                norm = [{a: p, b: q, **dict.fromkeys(Y, 1)},
                        {a: (1-p) % MOD, c: r, **dict.fromkeys(Z, 1)},
                        {b: (1-q) % MOD, c: (1-r) % MOD, **dict.fromkeys(W, 1)}]
                base_errors = [{x: cx[x]*v*pow(al, -1, MOD) % MOD for x, v in n.items()} for n, al in zip(norm, alpha)]
                bm = [moments(e) for e in base_errors]
                slope = [(v-u) % MOD for u, v in zip(bm[0], bm[1])]
                assert bm[2] == [(u+rho*v) % MOD for u, v in zip(bm[0], slope)]
                additional = []
                for i in ids:
                    K, mu = rows[i]['support'], rows[i]['mu']
                    E = (rho-(1-rho)*mu) % MOD
                    T = rho*pow(E, -1, MOD) % MOD
                    expected = [(u+T*v) % MOD for u, v in zip(bm[0], slope)]
                    values = solve([[pow(x, j, MOD) for x in K] for j in range(1, 5)], expected[:4])
                    error = dict(zip(K, values))
                    assert moments(error) == expected, 'restored row fails full moments'
                    if not all(values):
                        break
                    additional.append({'row': i, 'mu': mu, 'E': E, 'T': T,
                                       'error': error, 'moments8': expected})
                if len(additional) == 2:
                    times = [0, 1, rho]+[v['T'] for v in additional]
                    assert len(set(times)) == 5
                    errors = base_errors+[v['error'] for v in additional]
                    failures = []
                    for error in errors:
                        K = list(error)
                        values = solve([[pow(x, j, MOD) for x in K] for j in range(1, 5)], slope[:4])
                        residual = [(u-v) % MOD for u, v in zip(moments(dict(zip(K, values))), slope)]
                        assert any(residual)
                        failures.append(residual)
                    found = {'pqr': pqr, 'gamma': [0, 1, rho], 'errors': errors,
                             'base_moments8': bm, 'additional': additional,
                             'same_support_failure_residuals8': failures}
                    break
            full_pairs.append({'tag': tag, 'rows': ids, 'witness': found})
    return {'input': path.name, 'assignment': {k: saved[k] for k in ('a', 'b', 'c', 'Y', 'Z', 'W')},
            'support_tests': eligible_tests, 'rows': rows, 'pairs': pairs,
            'three_tag_weight_joins': weight_joins, 'linear_distinct_joins': linear_distinct_joins,
            'local_pair_replays': full_pairs,
            'checks': {'row_set_equal': True, 'pair_sets_equal': True, 'failures': []}}


def main():
    reports = []
    seen = {}
    for name in ('seed', 'best'):
        path = ROOT/f'three-shared-pairs-{name}.json'
        saved = json.loads(path.read_text())
        key = tuple(saved[k] if k in ('a', 'b', 'c') else tuple(saved[k])
                    for k in ('a', 'b', 'c', 'Y', 'Z', 'W'))
        if key in seen:
            original = json.loads((ROOT/seen[key]).read_text())
            assert saved == original
            continue
        seen[key] = path.name
        reports.append(verify(path))
    prefix = json.loads((ROOT/'three-shared-pairs-prefix.json').read_text())
    assert prefix['moment_failures'] == 0
    report = {'scope': 'Complete independent replay of distinct saved seed/best assignments only; prefix is not a uniform exclusion',
              'unique_selected_assignments': len(reports),
              'selected_assignments': reports, 'failures': []}
    path = ROOT/'three-shared-pairs-selected-verification.json'
    path.write_text(json.dumps(report, indent=2)+'\n')
    for r in reports:
        print(f"{r['input']}: rows {len(r['rows'])}/{len(r['rows'])}, pair counts {[len(p) for p in r['pairs']]}; three-tag weight joins {len(r['three_tag_weight_joins'])}/required 1.")
    print(f'Failures 0/0. Certificate: {path.relative_to(ROOT.parent.parent)}')


if __name__ == '__main__':
    main()
