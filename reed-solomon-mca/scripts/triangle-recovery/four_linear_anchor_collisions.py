"""Complete fixed-L068-label isolated row and quartet certificate (L057).

No label sweep; both-zero rows are classified but outside this target.
All original E gates can only remove rows from the chart-free table.
"""
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import json

F = 97
H = tuple(x for x in range(1, F) if pow(x, 16, F) == 1)
P, Y, Z, W = (64, 75, 33), (1, 96), (18, 79), (8, 50)


def prod(values):
    result = 1
    for value in values:
        result = result * value % F
    return result


def inv(value):
    return pow(value % F, -1, F)


def lagrange(x, labels, t):
    return prod((t-u)*inv(x-u) for u in labels if u != x)


def run():
    union = set(P+Y+Z+W)
    assert len(H) == 16 and len(union) == 9 and union <= set(H)
    cx = {x: prod(x-h for h in H if h not in union) for x in union}
    rows, groups = [], defaultdict(list)
    counts = Counter()
    failures = []
    for K in combinations([x for x in H if x not in P], 4):
        fk = {x: prod(x-k for k in K) for x in union}
        projected = [sum(cx[x]*x*fk[x]*prod(x-u for u in P)
                         for x in pair) % F for pair in (Y, Z)]
        beta = [[-sum(cx[t]*t*fk[t]*lagrange(x, P, t) for t in pair)
                 * inv(x*fk[x]) % F for x in P] for pair in (Y, Z)]
        ry, rz = projected
        row = {'K': K, 'projected_Y_Z': projected, 'beta_Y_Z': beta}
        if ry == rz == 0:
            row['kind'] = 'both_zero'
        elif not ry or not rz:
            row['kind'] = 'one_zero'
        else:
            mu = rz*inv(ry) % F
            row.update(kind='isolated', mu=mu)
            if mu == 96:
                row['gate'] = 'excluded_minus_one'
            else:
                by, bz = beta
                ca, cb, cc = (cx[x] for x in P)
                p = (1-(bz[0]-mu*by[0])*inv(ca))*inv(1+mu) % F
                q = (by[1]-bz[1]*inv(mu))*inv(cb) % F
                r = (bz[2]-mu*by[2])*inv(cc) % F
                weights = (p, q, r)
                row['weights'] = weights
                if any(value in (0, 1) for value in weights):
                    row['gate'] = 'excluded_base_weight'
                else:
                    coeff = {x: -mu*cx[x] % F for x in Y}
                    coeff.update({x: cx[x] for x in Z})
                    coeff.update({P[0]: ca*(1-(1+mu)*p) % F,
                                  P[1]: -mu*cb*q % F, P[2]: cc*r % F})
                    omega = [inv(x)*sum(v*t*lagrange(x, K, t)
                                       for t, v in coeff.items()) % F for x in K]
                    residual = [(sum(v*pow(x,j,F) for x,v in zip(K,omega))
                                 - sum(v*pow(x,j,F) for x,v in coeff.items())) % F
                                for j in range(1,9)]
                    if any(residual):
                        failures.append({'K': K, 'residual8': residual})
                    row.update(omega=omega, residual8=residual,
                               gate='full' if all(omega) else 'zero_fourth_weight')
                    if all(omega):
                        groups[weights].append(len(rows))
        counts[row['kind']] += 1
        if 'gate' in row:
            counts[row['gate']] += 1
        rows.append(row)
    fibers, quartets, pairs = [], [], []
    for weights, ids in sorted(groups.items()):
        scalars = [rows[i]['mu'] for i in ids]
        assert len(scalars) == len(set(scalars))
        fibers.append({'weights': weights, 'row_ids': ids, 'scalars': scalars})
        for i, j in combinations(ids, 2):
            intersection = sorted(set(rows[i]['K']) & set(rows[j]['K']))
            pairs.append({'row_ids': [i, j], 'intersection': intersection,
                          'linear': len(intersection) <= 1})
        for choice in combinations(ids, 4):
            intersections = [len(set(rows[i]['K']) & set(rows[j]['K']))
                             for i,j in combinations(choice, 2)]
            quartets.append({'weights': weights, 'row_ids': choice,
                             'intersection_sizes': intersections,
                             'qualifies': max(intersections) <= 1})
    summary = {'support_rows_actual': len(rows), 'support_rows_required': 715,
               'kind_and_gate_counts': dict(counts), 'full_weight_fibers': len(fibers),
               'full_scalar_maximum': max((len(f['row_ids']) for f in fibers), default=0),
               'fiber_size_histogram': dict(Counter(len(f['row_ids']) for f in fibers)),
               'same_weight_pairs': len(pairs), 'linear_same_weight_pairs': sum(p['linear'] for p in pairs),
               'distinct_scalar_quartets': len(quartets),
               'qualifying_quartets': sum(q['qualifies'] for q in quartets),
               'failures_actual': len(failures), 'failures_required': 0}
    result = {'scope': 'L068 fixed nine labels; all gated weights; isolated disjoint-P only',
              'H': H, 'P': P, 'Y': Y, 'Z': Z, 'W': W,
              'CX': {str(x): cx[x] for x in sorted(cx)}, 'rows': rows,
              'fibers': fibers, 'same_weight_pairs': pairs, 'quartets': quartets,
              'summary': summary, 'failures': failures}
    path = Path(__file__).with_name('four-linear-anchor-collisions.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Full certificate: {path}')
    assert len(rows) == 715 and not failures


if __name__ == '__main__':
    run()
