"""Complete L105 support-seed table for one fixed ordered split.

Every seed disposition and every distinct candidate's 324 row dispositions
are saved. Codes distinguish all first-failed gates; no sampling is used.
Run from the active notebook: python3 scripts/seven-coordinate/fixed_split_table.py
"""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import hashlib
import json

MOD = 97
P = (1, 8, 12)
Q = (18, 22, 27)
C = 33
H = tuple(x for x in range(1, MOD) if pow(x, 16, MOD) == 1)
J = tuple(x for x in H if x not in (*P, *Q, C))
KS = tuple(combinations(J, 2))
EDGES = tuple(product(P, Q))
ROWS = tuple((x, y, i) for x, y in EDGES for i in range(len(KS)))
INV = {x: pow(x, -1, MOD) for x in range(1, MOD)}
OUT = Path(__file__).with_name('fixed-split-table.json')


def g_value(k, x):
    value = 1
    for z in J:
        if z not in k:
            value = value * (x-z) % MOD
    return value


G = tuple({x: g_value(k, x) for x in H} for k in KS)


def tree_vector(triple, omitted, ki):
    """Solve the two tree edges by propagation from the fixed first label."""
    result = {triple[0]: 1}
    for _ in range(2):
        for x, k in zip(omitted, ki):
            z, zz = (t for t in triple if t != x)
            if z in result:
                result[zz] = result[z] * G[k][zz] * INV[G[k][z]] % MOD
            if zz in result:
                result[z] = result[zz] * G[k][z] * INV[G[k][zz]] % MOD
    assert len(result) == 3 and all(result.values())
    return result


def row_test(p, q, u, v, x, y, ki):
    z, zz = (t for t in P if t != x)
    aa = p[z] * INV[G[ki][z]] % MOD
    if p[zz] * INV[G[ki][zz]] % MOD != aa:
        return 'p', None
    z, zz = (t for t in Q if t != y)
    bb = q[z] * INV[G[ki][z]] % MOD
    if q[zz] * INV[G[ki][zz]] % MOD != bb:
        return 'q', None
    mu = bb * INV[aa] % MOD
    if (mu*u-v-bb*G[ki][C]) % MOD:
        return 'c', None
    if (mu*p[x]-bb*G[ki][x]) % MOD == 0:
        return 'x', None
    if (q[y]-bb*G[ki][y]) % MOD == 0:
        return 'y', None
    return 's', mu


def run():
    seeds, candidates, lookup = [], [], {}
    for e1, e2 in combinations(EDGES, 2):
        if e1[0] == e2[0] or e1[1] == e2[1]:
            continue
        for k1 in range(len(KS)):
            for k2 in range(len(KS)):
                if k1 == k2:
                    continue
                seed = [*e1, *e2, k1, k2]
                p = tree_vector(P, (e1[0], e2[0]), (k1, k2))
                q = tree_vector(Q, (e1[1], e2[1]), (k1, k2))
                mus, cs = [], []
                for (x, y), ki in zip((e1, e2), (k1, k2)):
                    z = next(t for t in P if t != x)
                    aa = p[z]*INV[G[ki][z]] % MOD
                    z = next(t for t in Q if t != y)
                    bb = q[z]*INV[G[ki][z]] % MOD
                    mus.append(bb*INV[aa] % MOD)
                    cs.append(bb*G[ki][C] % MOD)
                if mus[0] == mus[1]:
                    seeds.append([seed, 'mu', None])
                    continue
                u = (cs[0]-cs[1])*INV[(mus[0]-mus[1]) % MOD] % MOD
                v = (mus[0]*u-cs[0]) % MOD
                if u == 0 or v == 0:
                    seeds.append([seed, 'u' if u == 0 else 'v', None])
                    continue
                failures = []
                for (x, y), ki in zip((e1, e2), (k1, k2)):
                    code, _ = row_test(p, q, u, v, x, y, ki)
                    if code != 's':
                        failures.append(code)
                if failures:
                    seeds.append([seed, 'weight:' + ''.join(failures), None])
                    continue
                key = (*[p[z] for z in P], *[q[z] for z in Q], u, v)
                if key not in lookup:
                    lookup[key] = len(candidates)
                    codes, successes = [], []
                    for row_id, (x, y, ki) in enumerate(ROWS):
                        code, mu = row_test(p, q, u, v, x, y, ki)
                        codes.append(code)
                        if code == 's':
                            successes.append([row_id, mu])
                    scalars = sorted({mu for _, mu in successes})
                    assert len(scalars) == len(successes)
                    candidates.append({'key': key, 'codes': ''.join(codes),
                                       'successes': successes, 'scalars': scalars})
                seeds.append([seed, 'retained', lookup[key]])
    assert len(seeds) == 22680 and len(ROWS) == 324
    maximum = max(len(c['scalars']) for c in candidates)
    summary = {
        'seed_cases_actual': len(seeds), 'seed_cases_required': 22680,
        'seed_dispositions': dict(sorted(Counter(s[1] for s in seeds).items())),
        'distinct_candidates': len(candidates),
        'row_tests_actual': len(candidates)*len(ROWS),
        'row_tests_required_per_candidate': 324,
        'row_dispositions': dict(sorted(Counter(''.join(c['codes'] for c in candidates)).items())),
        'distinct_scalar_histogram': dict(sorted(Counter(len(c['scalars']) for c in candidates).items())),
        'maximum_distinct_scalars': maximum, 'equality_required_scalars': 6,
        'threshold_candidate_ids': [i for i, c in enumerate(candidates) if len(c['scalars']) >= 6],
        'maximum_candidate_ids': [i for i, c in enumerate(candidates) if len(c['scalars']) == maximum],
        'failures_actual': 0, 'failures_required': 0,
    }
    data = {'schema': 1, 'H': H, 'P': P, 'Q': Q, 'c': C, 'J': J,
            'K_order': KS, 'row_order': ROWS,
            'code_meanings': {'p': 'first failed P ratio', 'q': 'first failed Q ratio',
                             'c': 'failed c equation', 'x': 'zero P overlap weight',
                             'y': 'zero Q overlap weight', 's': 'full success'},
            'seeds': seeds, 'candidates': candidates, 'summary': summary}
    OUT.write_text(json.dumps(data, separators=(',', ':')) + '\n')
    print(json.dumps({**summary, 'maximum_candidate_ids': summary['maximum_candidate_ids'][:5],
                      'certificate': str(OUT),
                      'sha256': hashlib.sha256(OUT.read_bytes()).hexdigest()}, sort_keys=True))


if __name__ == '__main__':
    run()
