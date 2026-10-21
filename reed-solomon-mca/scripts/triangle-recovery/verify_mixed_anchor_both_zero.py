"""Replay all mixed-test cases using full moment linear algebra.

No producer imports or projected/Lagrange recovery formula is used.
Certificate failures and every load-bearing replay case are saved.
"""
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import hashlib
import json

F = 97


def product(xs):
    value = 1
    for x in xs:
        value = value*x % F
    return value


def solve(columns, rhs):
    """Exact reduced row echelon solve, with free variables set to zero."""
    n = len(columns)
    rows = [[col[i] % F for col in columns]+[rhs[i] % F] for i in range(len(rhs))]
    pivot_rows, rank = {}, 0
    for j in range(n):
        pivot = next((i for i in range(rank,len(rows)) if rows[i][j]),None)
        if pivot is None:
            continue
        rows[rank],rows[pivot] = rows[pivot],rows[rank]
        factor = pow(rows[rank][j],-1,F)
        rows[rank] = [x*factor % F for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank:
                factor = rows[i][j]
                rows[i] = [(a-factor*b) % F for a,b in zip(rows[i],rows[rank])]
        pivot_rows[j] = rank
        rank += 1
    inconsistent = any(not any(row[:n]) and row[-1] for row in rows)
    solution = None if inconsistent else [rows[pivot_rows[j]][-1] if j in pivot_rows else 0
                                         for j in range(n)]
    return rank,solution


def run():
    root = Path(__file__).parent
    source = root/'mixed-anchor-both-zero.json'
    cert = json.loads(source.read_text())
    H = tuple(x for x in range(1,F) if pow(x,16,F)==1)
    P,Y,Z,W = (18,22,27),(1,96),(8,89),(12,85)
    union = set(P+Y+Z+W)
    outside = tuple(x for x in H if x not in union)
    cx = {x:product(x-h for h in outside) for x in union}
    v = {x:[pow(x,j,F) for j in range(1,9)] for x in H}
    sy = [sum(cx[x]*v[x][j] for x in Y) % F for j in range(8)]
    sz = [sum(cx[x]*v[x][j] for x in Z) % F for j in range(8)]
    failures = []

    def check(condition, label, details=None):
        if not condition:
            failures.append({'check':label,'details':details})

    for name,value in [('H',H),('P',P),('Y',Y),('Z',Z),('W',W)]:
        check(cert[name]==list(value),'fixed_'+name)
    check(cert['CX']=={str(k):x for k,x in cx.items()},'cx')
    supports = list(combinations([x for x in H if x not in P],4))
    check([row['K'] for row in cert['rows']]==[list(K) for K in supports], 'complete_support_set')
    groups, zero_ids, replay = defaultdict(list),[],[]
    for row_id,K in enumerate(supports):
        row = cert['rows'][row_id]
        cols = [v[x] for x in K+P]
        rank_y, ysolution = solve(cols,sy)
        rank_z, zsolution = solve(cols,sz)
        check(rank_y==rank_z==7,'seven_column_independence',row_id)
        kind = ('both_zero' if ysolution is not None and zsolution is not None else
                'one_zero' if (ysolution is None)!=(zsolution is None) else 'isolated')
        check(row['kind']==kind,'support_kind',row_id)
        item = {'row_id':row_id,'rank_K_P':rank_y,'Y_in_span':ysolution is not None,
                'Z_in_span':zsolution is not None,'kind':kind}
        if kind=='both_zero':
            zero_ids.append(row_id)
        if kind=='isolated':
            rank,solution = solve(cols+[sy],sz)
            check(rank==8 and solution is not None,'isolated_unique_solution',row_id)
            mu = solution[7]
            check(mu==row['mu'] and mu!=0,'isolated_mu',row_id)
            item.update(mu=mu,moment_solution=solution)
            if mu==96:
                gate = 'minus_one'
            else:
                ca,cb,cc = [cx[x] for x in P]
                weights = ((1+solution[4]*pow(ca,-1,F))*pow(1+mu,-1,F) % F,
                           solution[5]*pow(mu*cb % F,-1,F) % F,
                           -solution[6]*pow(cc,-1,F) % F)
                check(row['weights']==list(weights),'anchor_weight_solution',row_id)
                item['weights'] = weights
                if any(x in (0,1) for x in weights):
                    gate = 'base_weight'
                else:
                    check(row['omega']==solution[:4], 'anchor_four_weights',row_id)
                    gate = 'full' if all(solution[:4]) else 'zero_fourth_weight'
                    if gate=='full':
                        groups[weights].append(row_id)
            check(gate==row['gate'],'anchor_gate',row_id)
            item['gate'] = gate
        replay.append(item)
    check(zero_ids==cert['both_zero_row_ids'],'complete_both_zero_set')

    # Independent L065 dependent-quadratic fiber description of all ten supports.
    quadratic = lambda pair: [pair[0]*pair[1] % F, -(pair[0]+pair[1]) % F,1]
    y2,z2,w2 = [quadratic(pair) for pair in (Y,Z,W)]
    rank,ab = solve([y2,z2],w2)
    check(rank==2 and ab is not None and all(ab) and sum(ab)%F==1,'dependent_quadratics')
    value = lambda pair,x: product(x-u for u in pair)
    fiber_map = defaultdict(list)
    for x in outside:
        fiber_map[value(Y,x)*pow(value(Z,x),-1,F) % F].append(x)
    doubles = [tuple(nodes) for nodes in fiber_map.values() if len(nodes)==2]
    family = {tuple(sorted(pair+B)) for pair in (Y,Z,W) for B in doubles}
    family.update(tuple(sorted(A+B)) for A,B in combinations(doubles,2))
    family.update(tuple(sorted(A+B)) for A,B in combinations((Y,Z,W),2))
    check(family=={supports[i] for i in zero_ids},'complete_split_net_family')
    expected_fibers = [(list(w),ids) for w,ids in sorted(groups.items())]
    check([(f['weights'],f['anchor_row_ids']) for f in cert['fibers']]==expected_fibers,
          'complete_full_anchor_weight_points')
    lift_replay,histogram = [],Counter()
    for weights,anchor_ids in sorted(groups.items()):
        fcert = next(f for f in cert['fibers'] if f['weights']==list(weights))
        p,q,r = weights
        n0 = [(sz[j]+cx[P[0]]*(1-p)*v[P[0]][j]+cx[P[2]]*r*v[P[2]][j]) % F
              for j in range(8)]
        n1 = [(-sy[j]-cx[P[0]]*p*v[P[0]][j]-cx[P[1]]*q*v[P[1]][j]) % F
              for j in range(8)]
        check([l['row_id'] for l in fcert['both_zero_lifts']]==zero_ids,'complete_lift_set',weights)
        scalars = set()
        for lift,row_id in zip(fcert['both_zero_lifts'],zero_ids):
            K = supports[row_id]
            cols = [v[x] for x in K]
            rank,w0 = solve([col[:4] for col in cols],n0[:4])
            rank1,w1 = solve([col[:4] for col in cols],n1[:4])
            check(rank==rank1==4,'four_column_recovery',(weights,row_id))
            residual0 = [(sum(col[j]*z for col,z in zip(cols,w0))-n0[j]) % F for j in range(8)]
            residual1 = [(sum(col[j]*z for col,z in zip(cols,w1))-n1[j]) % F for j in range(8)]
            pivot = next((j for j,x in enumerate(residual1) if x),None)
            item = {'weights':weights,'row_id':row_id,'omega_constant':w0,'omega_linear':w1,
                    'moment_residual_constant':residual0,'moment_residual_linear':residual1}
            if pivot is None:
                check(any(residual0),'exclude_entire_pencil',(weights,row_id))
                eligible = False
                item['gate'] = 'inconsistent_constant'
            else:
                mu = -residual0[pivot]*pow(residual1[pivot],-1,F) % F
                residual = [(a+mu*b) % F for a,b in zip(residual0,residual1)]
                eligible = not any(residual) and mu not in (0,96)
                item.update(mu=mu,residual8=residual,
                            gate='eligible' if eligible else 'inconsistent' if any(residual) else 'base_scalar')
            check(eligible==(lift['gate']=='eligible'),'exact_lift_agreement',(weights,row_id))
            if eligible:
                scalars.add(mu)
                omega = [(a+mu*b) % F for a,b in zip(w0,w1)]
                check(lift['mu']==mu and lift['omega']==omega,'lift_weights',(weights,row_id))
                item['omega'] = omega
            lift_replay.append(item)
        check(sorted(scalars)==fcert['both_zero_scalars'],'scalar_deduplication',weights)
        histogram[len(scalars)] += 1
    maximum = max(histogram,default=0)
    check(maximum==cert['summary']['both_zero_maximum'],'maximum')
    check(len(groups)==cert['summary']['full_anchor_weight_points'],'weight_point_count')
    summary = {'support_rows_actual':len(replay),'support_rows_required':715,
               'full_anchor_weight_points':len(groups),'both_zero_supports':len(zero_ids),
               'lift_tests_actual':len(lift_replay),'lift_tests_required':len(groups)*len(zero_ids),
               'both_zero_maximum':maximum,'attainment_threshold':3,
               'mixed_count_histogram':dict(histogram),'failures_actual':len(failures),'failures_required':0}
    result = {'producer_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
              'method':'Independent eight-moment RREF; first-four recovery followed by all-eight affine residuals',
              'quadratic_dependency_alpha_beta':ab,'outside_double_fibers':doubles,
              'split_net_supports':sorted(family),'anchor_replay':replay,
              'lift_replay':lift_replay,'summary':summary,'failures':failures}
    path = root/'mixed-anchor-both-zero-verification.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(summary,sort_keys=True))
    print(f'Full replay certificate: {path}')
    assert not failures


if __name__=='__main__':
    run()
