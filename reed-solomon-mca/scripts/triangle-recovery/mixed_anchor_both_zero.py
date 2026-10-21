"""One complete fixed-assignment test of L066 attainment via L057.

All 715 disjoint-P supports, all full isolated-anchor weight points,
and every both-zero lift. No labeling sweep. Full evidence goes to disk.
"""
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import json

F = 97
H = tuple(x for x in range(1, F) if pow(x, 16, F) == 1)
P, Y, Z, W = (18, 22, 27), (1, 96), (8, 89), (12, 85)
U = set(P+Y+Z+W)


def prod(values):
    out = 1
    for value in values:
        out = out*value % F
    return out


def inv(x):
    return pow(x % F, -1, F)


def lagrange(x, nodes, t):
    return prod((t-u)*inv(x-u) for u in nodes if u != x)


CX = {x: prod(x-h for h in H if h not in U) for x in U}


def numerator(weights, mu):
    p, q, r = weights
    coeff = {x: -mu*CX[x] % F for x in Y}
    coeff.update({x: CX[x] for x in Z})
    coeff.update({P[0]: CX[P[0]]*(1-(1+mu)*p) % F,
                  P[1]: -mu*CX[P[1]]*q % F,
                  P[2]: CX[P[2]]*r % F})
    return coeff


def recover(K, weights, mu):
    coeff = numerator(weights, mu)
    omega = [inv(x)*sum(v*t*lagrange(x, K, t)
                       for t, v in coeff.items()) % F for x in K]
    residual = [(sum(v*pow(x,j,F) for x,v in zip(K,omega))
                 - sum(v*pow(x,j,F) for x,v in coeff.items())) % F
                for j in range(1,9)]
    assert not any(residual), (K, weights, mu, residual)
    return omega, residual


def run():
    assert len(H) == 16 and len(U) == 9 and U <= set(H)
    rows, groups = [], defaultdict(list)
    counts = Counter()
    for K in combinations([x for x in H if x not in P], 4):
        fk = {x: prod(x-k for k in K) for x in U}
        projected = [sum(CX[x]*x*fk[x]*prod(x-u for u in P)
                         for x in pair) % F for pair in (Y,Z)]
        beta = [[-sum(CX[t]*t*fk[t]*lagrange(x,P,t) for t in pair)
                 * inv(x*fk[x]) % F for x in P] for pair in (Y,Z)]
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
                row['gate'] = 'minus_one'
            else:
                by,bz = beta
                ca,cb,cc = (CX[x] for x in P)
                weights = ((1-(bz[0]-mu*by[0])*inv(ca))*inv(1+mu) % F,
                           (by[1]-bz[1]*inv(mu))*inv(cb) % F,
                           (bz[2]-mu*by[2])*inv(cc) % F)
                row['weights'] = weights
                if any(v in (0,1) for v in weights):
                    row['gate'] = 'base_weight'
                else:
                    omega,residual = recover(K,weights,mu)
                    row.update(omega=omega,residual8=residual,
                               gate='full' if all(omega) else 'zero_fourth_weight')
                    if all(omega):
                        groups[weights].append(len(rows))
        counts[row['kind']] += 1
        if 'gate' in row:
            counts[row['gate']] += 1
        rows.append(row)
    zero_ids = [i for i,row in enumerate(rows) if row['kind'] == 'both_zero']
    fibers = []
    for weights, anchor_ids in sorted(groups.items()):
        p,q,r = weights
        lifts = []
        for row_id in zero_ids:
            row = rows[row_id]
            by,bz = row['beta_Y_Z']
            ca,cb,cc = (CX[x] for x in P)
            A = [(ca*(1-p)-bz[0]) % F, -bz[1] % F, (cc*r-bz[2]) % F]
            B = [(-ca*p+by[0]) % F, (-cb*q+by[1]) % F, by[2]]
            assert any(A+B)
            lift = {'row_id': row_id, 'A': A, 'B': B}
            pivot = next((i for i,v in enumerate(B) if v),None)
            if pivot is None:
                lift['gate'] = 'no_pivot'
            else:
                mu = -A[pivot]*inv(B[pivot]) % F
                residual = [(a+mu*b) % F for a,b in zip(A,B)]
                lift.update(pivot=pivot,mu=mu,restored_residual=residual)
                if any(residual):
                    lift['gate'] = 'inconsistent'
                elif mu in (0,96):
                    lift['gate'] = 'base_scalar'
                else:
                    omega,residual8 = recover(row['K'],weights,mu)
                    lift.update(gate='eligible',omega=omega,residual8=residual8,
                                full=all(omega))
            lifts.append(lift)
        scalars = sorted({lift['mu'] for lift in lifts if lift['gate']=='eligible'})
        fibers.append({'weights':weights,'anchor_row_ids':anchor_ids,
                       'both_zero_lifts':lifts,'both_zero_scalars':scalars})
    maximum = max((len(f['both_zero_scalars']) for f in fibers),default=0)
    summary = {'support_rows_actual':len(rows),'support_rows_required':715,
               'kind_and_gate_counts':dict(counts),'full_anchor_weight_points':len(fibers),
               'both_zero_supports':len(zero_ids),
               'lift_tests_actual':len(fibers)*len(zero_ids),
               'lift_tests_required':len(fibers)*len(zero_ids),
               'mixed_count_histogram':dict(Counter(len(f['both_zero_scalars']) for f in fibers)),
               'both_zero_maximum':maximum,'attainment_threshold':3,
               'attaining_weight_points':sum(len(f['both_zero_scalars'])==3 for f in fibers),
               'failures_actual':0,'failures_required':0}
    result = {'scope':'One saved dependent-quadratic assignment; complete full-anchor weights and both-zero lifts',
              'H':H,'P':P,'Y':Y,'Z':Z,'W':W,'CX':CX,'rows':rows,
              'both_zero_row_ids':zero_ids,'fibers':fibers,'summary':summary,'failures':[]}
    path = Path(__file__).with_name('mixed-anchor-both-zero.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(summary,sort_keys=True))
    print(f'Full certificate: {path}')
    assert len(rows)==715


if __name__ == '__main__':
    run()
