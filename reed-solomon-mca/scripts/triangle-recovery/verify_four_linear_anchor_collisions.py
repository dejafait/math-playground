"""Replay every fixed-label row by seven-column moments, then graph cliques.

Imports only established modular Gaussian arithmetic, not the producer,
support-polynomial/beta equations, or L059's restored-point formula.
"""
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import hashlib
import json
from verify_fixed_union_table import invert, mul

F = 97


def run():
    path = Path(__file__).with_name('four-linear-anchor-collisions.json')
    data = json.loads(path.read_text())
    H = tuple(x for x in range(1,F) if pow(x,16,F) == 1)
    P, Y, Z, W = (64,75,33), (1,96), (18,79), (8,50)
    assert (data['H'], data['P'], data['Y'], data['Z'], data['W']) == tuple(
        list(t) for t in (H,P,Y,Z,W))
    U = set(P+Y+Z+W)
    cx = {}
    for x in U:
        value = 1
        for h in H:
            if h not in U:
                value = value*(x-h) % F
        cx[x] = value
    assert data['CX'] == {str(x): cx[x] for x in U}
    expected_supports = list(combinations([x for x in H if x not in P],4))
    assert [tuple(row['K']) for row in data['rows']] == expected_supports
    moments = [[sum(cx[x]*pow(x,j,F) for x in pair) % F
                for j in range(1,9)] for pair in (Y,Z)]
    replay, fibers = [], defaultdict(list)
    counts = Counter()
    complete_residuals = []
    for row_id, (K, row) in enumerate(zip(expected_supports, data['rows'])):
        matrix = [[pow(x,j,F) for x in (*K,*P)] for j in range(1,9)]
        inverse = invert(matrix[:7])
        solved = [mul(inverse,m[:7]) for m in moments]
        residual = [(m[7]-mul(matrix[7:],v)[0]) % F
                    for m,v in zip(moments,solved)]
        assert row['projected_Y_Z'] == residual
        test = {'row_id': row_id, 'K': K, 'residual_Y_Z': residual}
        ry, rz = residual
        if ry == rz == 0:
            kind = 'both_zero'
        elif not ry or not rz:
            kind = 'one_zero'
        else:
            kind = 'isolated'
            mu = rz*pow(ry,-1,F) % F
            assert row['mu'] == mu
            if mu == 96:
                gate = 'excluded_minus_one'
            else:
                diff = [(z-mu*y) % F for y,z in zip(*solved)]
                da,db,dc = diff[4:]
                weights = ((1+da*pow(cx[P[0]],-1,F))*pow(1+mu,-1,F) % F,
                           db*pow(mu*cx[P[1]] % F,-1,F) % F,
                           -dc*pow(cx[P[2]],-1,F) % F)
                assert row['weights'] == list(weights)
                if any(w in (0,1) for w in weights):
                    gate = 'excluded_base_weight'
                else:
                    omega = diff[:4]
                    assert row['omega'] == omega
                    p,q,r = weights
                    coeff = {x: -mu*cx[x] % F for x in Y}
                    coeff.update({x: cx[x] for x in Z})
                    coeff.update({P[0]: cx[P[0]]*(1-(1+mu)*p) % F,
                                  P[1]: -mu*cx[P[1]]*q % F,
                                  P[2]: cx[P[2]]*r % F})
                    numerator8 = [sum(v*pow(x,j,F) for x,v in coeff.items()) % F
                                  for j in range(1,9)]
                    recovered8 = mul(matrix,omega+[0,0,0])
                    residual8 = [(u-v) % F for u,v in zip(recovered8,numerator8)]
                    assert row['residual8'] == residual8 == [0]*8
                    complete_residuals.append({'row_id':row_id, 'numerator8':numerator8,
                                              'recovered8':recovered8,'residual8':residual8})
                    gate = 'full' if all(omega) else 'zero_fourth_weight'
                    if all(omega):
                        fibers[weights].append(row_id)
                test.update(mu=mu, weights=weights)
            assert row['gate'] == gate
            counts[gate] += 1
            test['gate'] = gate
        assert row['kind'] == kind
        counts[kind] += 1
        test['kind'] = kind
        replay.append(test)
    expected_fibers = [{'weights':list(w), 'row_ids':ids,
                        'scalars':[data['rows'][i]['mu'] for i in ids]}
                       for w,ids in sorted(fibers.items())]
    assert data['fibers'] == expected_fibers
    pair_replay, clique4 = [], []
    # Different traversal from producer: form adjacency, then enumerate
    # all increasing graph cliques. Distinct-scalar gates precede edges.
    for weights, ids in sorted(fibers.items()):
        assert len({data['rows'][i]['mu'] for i in ids}) == len(ids)
        adjacency = {i: set() for i in ids}
        for i in ids:
            for j in ids:
                if i >= j:
                    continue
                common = sorted(x for x in expected_supports[i] if x in expected_supports[j])
                linear = len(common) <= 1
                pair_replay.append({'row_ids':[i,j], 'intersection':common,'linear':linear})
                if linear:
                    adjacency[i].add(j)
                    adjacency[j].add(i)

        def extend(chosen, candidates):
            if len(chosen) == 4:
                clique4.append({'weights':weights, 'row_ids':chosen})
                return
            for i in sorted(candidates):
                extend(chosen+[i], {j for j in candidates & adjacency[i] if j > i})

        extend([], set(ids))
    assert data['same_weight_pairs'] == pair_replay
    # Inspect all producer four-subsets as well, including failed ones.
    expected_quartets = []
    for weights,ids in sorted(fibers.items()):
        for choice in combinations(ids,4):
            sizes = [sum(x in expected_supports[j] for x in expected_supports[i])
                     for i,j in combinations(choice,2)]
            expected_quartets.append({'weights':list(weights),'row_ids':list(choice),
                                      'intersection_sizes':sizes,'qualifies':max(sizes)<=1})
    assert data['quartets'] == expected_quartets
    expected_summary = {'support_rows_actual':len(replay),'support_rows_required':715,
                        'kind_and_gate_counts':dict(counts),'full_weight_fibers':len(fibers),
                        'full_scalar_maximum':max(map(len,fibers.values())),
                        'fiber_size_histogram':{str(k):v for k,v in Counter(map(len,fibers.values())).items()},
                        'same_weight_pairs':len(pair_replay),
                        'linear_same_weight_pairs':sum(r['linear'] for r in pair_replay),
                        'distinct_scalar_quartets':len(expected_quartets),
                        'qualifying_quartets':len(clique4),'failures_actual':0,'failures_required':0}
    assert data['summary'] == expected_summary and data['failures'] == []
    result = {'certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
              'summary':expected_summary, 'required_quartet_size':4,
              'complete_row_replay':replay, 'gated_eight_moment_checks':complete_residuals,
              'fibers':expected_fibers, 'pair_replay':pair_replay,
              'quartet_replay':expected_quartets,'qualifying_cliques4':clique4,'failures':[]}
    out = path.with_name('four-linear-anchor-collisions-verification.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Support replay {len(replay)}/715; gated eight-moment checks {len(complete_residuals)}/492')
    print(f'All same-weight pairs {len(pair_replay)}/10; linear pairs {sum(r["linear"] for r in pair_replay)}; qualifying quartets {len(clique4)}/threshold 1')
    print(f'Quartet replay {len(expected_quartets)}/5; failures 0/0; full certificate: {out}')


if __name__ == '__main__':
    run()
