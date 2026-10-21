"""Independently recover the candidate fiber by seven-column moments.

Check all 715 disjoint-P supports; retain zero recovered weights and
both-zero diagnostics. Verify every claimed scalar in the original chart.
The arithmetic utility is shared with the earlier independent table replay;
neither the C++ interpolation evaluator nor its row classifier is imported.
"""
from itertools import combinations
from pathlib import Path
import hashlib
import json
from verify_fixed_union_table import invert, mul

ROOT = Path(__file__).parent
F = 97


def main():
    source = ROOT / 'two-antipodal-anchor-sweep.json'
    sweep = json.loads(source.read_text())
    candidate = sweep['maximum_witness']
    # Freeze the independently supplied candidate, rather than silently
    # accepting arbitrary labels or weights from a producer summary.
    P = (64, 75, 33)
    Y, Z, W = (1, 96), (18, 79), (8, 50)
    p, q, r = 71, 5, 17
    expected = [22, 30, 34, 50, 63]
    assert candidate == {'P': list(P), 'S_Y_Z_W': list(Y+Z+W),
                         'weights': [p,q,r], 'scalars': expected}
    H = tuple(x for x in range(1,F) if pow(x,16,F) == 1)
    U = set(P+Y+Z+W)
    assert len(U) == 9 and U <= set(H)
    assert sum(Y) % F == sum(Z) % F == 0 and sum(W) % F != 0
    assert all(v not in (0,1) for v in (p,q,r))
    cx = {}
    for x in U:
        value = 1
        for h in H:
            if h not in U:
                value = value*(x-h) % F
        assert value
        cx[x] = value

    def moment(error):
        return [sum(w*pow(x,j,F) for x,w in error.items()) % F
                for j in range(1,9)]

    normalized = ({**dict.fromkeys(Y,1), P[0]:p, P[1]:q},
                  {**dict.fromkeys(Z,1), P[0]:1-p, P[2]:r},
                  {**dict.fromkeys(W,1), P[1]:1-q, P[2]:1-r})
    alpha = (-1, 2, -1)  # gamma=(0,1,2), lambda=1.
    base = [{x: cx[x]*v*pow(a % F,-1,F) % F for x,v in n.items()}
            for n,a in zip(normalized,alpha)]
    assert all(all(e.values()) and len(e) == 4 for e in base)
    base_moments = [moment(e) for e in base]
    assert all((s2-2*s1+s0) % F == 0
               for s0,s1,s2 in zip(*base_moments))
    pair_moments = [moment({x:cx[x] for x in pair}) for pair in (Y,Z)]
    tests, positives = [], []
    for K in combinations([x for x in H if x not in P],4):
        matrix = [[pow(x,j,F) for x in (*K,*P)] for j in range(1,9)]
        inverse = invert(matrix[:7])
        solved = [mul(inverse, m[:7]) for m in pair_moments]
        residual = [(m[7]-mul(matrix[7:],v)[0]) % F
                    for m,v in zip(pair_moments,solved)]
        row = {'K':K, 'seven_column_residual_Y_Z':residual}
        if not any(residual):
            row['kind'] = 'both_zero_not_counted_as_isolated'
        elif not all(residual):
            row['kind'] = 'one_zero'
        else:
            mu = residual[1]*pow(residual[0],-1,F) % F
            row['mu'] = mu
            if mu == F-1:
                row['kind'] = 'excluded_minus_one'
            else:
                d = [(z-mu*y) % F for y,z in zip(solved[0][4:],solved[1][4:])]
                weights = ((1+d[0]*pow(cx[P[0]],-1,F))*pow(1+mu,-1,F) % F,
                           d[1]*pow(mu*cx[P[1]] % F,-1,F) % F,
                           -d[2]*pow(cx[P[2]],-1,F) % F)
                row['restored_weights'] = weights
                row['kind'] = 'different_weights'
                if weights == (p,q,r):
                    omega = [(z-mu*y) % F
                             for y,z in zip(solved[0][:4],solved[1][:4])]
                    coeff = {x:-mu*cx[x] % F for x in Y}
                    coeff.update({x:cx[x] for x in Z})
                    coeff.update({P[0]:cx[P[0]]*(1-(1+mu)*p) % F,
                                  P[1]:-mu*cx[P[1]]*q % F,
                                  P[2]:cx[P[2]]*r % F})
                    numerator_residual = [(a-b) % F for a,b in
                                          zip(moment(dict(zip(K,omega))),moment(coeff))]
                    assert not any(numerator_residual)
                    E = (2+mu) % F
                    assert E and mu not in (0,F-1)
                    T = 2*pow(E,-1,F) % F
                    assert T not in (0,1,2)
                    actual = [v*pow(E,-1,F) % F for v in omega]
                    direct = [(value-((1-T)*s0+T*s1)) % F
                              for value,s0,s1 in zip(moment(dict(zip(K,actual))),
                                                     base_moments[0],base_moments[1])]
                    assert not any(direct)
                    # Independently confirm L057's original quotient scalars.
                    projected = []
                    for pair in (Y,Z):
                        v = 0
                        for x in pair:
                            f = 1
                            for k in K:
                                f = f*(x-k) % F
                            gp = 1
                            for t in P:
                                gp = gp*(x-t) % F
                            v = (v+cx[x]*x*f*gp) % F
                        projected.append(v)
                    assert all(projected)
                    assert projected[1]*pow(projected[0],-1,F) % F == mu
                    row.update(kind='retained_isolated', omega=omega,
                               full_weight=all(omega), E=E, original_T=T,
                               actual_weights=actual, projected_Y_Z=projected,
                               actual_moments8=moment(dict(zip(K,actual))),
                               expected_pencil_moments8=[((1-T)*s0+T*s1) % F
                                                       for s0,s1 in zip(*base_moments[:2])],
                               numerator_residual8=numerator_residual,
                               original_moment_residual8=direct)
                    positives.append(dict(row))
        tests.append(row)
    assert len(tests) == 715
    scalars = sorted({row['mu'] for row in positives})
    assert scalars == expected and len(positives) == 5
    assert all(row['full_weight'] for row in positives)
    assert len({row['original_T'] for row in positives}) == 5
    packed = ROOT / 'two-antipodal-anchor-rows.bin'
    assert packed.stat().st_size == sweep['certificate_bytes'] == 354110900
    with packed.open('rb') as stream:
        digest = hashlib.file_digest(stream,'sha256').hexdigest()
    result = {'scope':'one fixed two-antipodal-pair triangle; five-scalar counterexample only',
              'H':H,'P':P,'Y':Y,'Z':Z,'W':W,'weights':[p,q,r],
              'CX':{str(x):cx[x] for x in sorted(cx)},
              'original_chart':{'gamma':[0,1,2],'lambda':1,'g':1,'rho':2},
              'base_errors':base,'base_moments':base_moments,
              'actual_support_tests':715,'required_support_tests':715,
              'actual_distinct_isolated_scalars':len(scalars),
              'proposed_upper_bound':3,'discriminating_threshold':4,
              'witness_rows':positives,'complete_fixed_assignment_tests':tests,
              'sweep_coverage_complete':sweep['coverage_complete'],
              'sweep_actual_required_rows':[sweep['actual_support_rows'],
                                             sweep['required_support_rows']],
              'packed_bytes':packed.stat().st_size,'packed_sha256':digest,
              'packed_rows_replayed':False,'failures':[],
              'actual_failures':0,'required_failures':0}
    path = ROOT / 'two-antipodal-witness-verification.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('Fixed-assignment support tests 715/715; isolated scalars 5; proposed bound 3; threshold 4')
    print('Five full-weight original eight-moment and finite-gate checks; failures 0/0')
    print('Global sweep incomplete: 70822180/237837600 rows; no global maximum asserted')
    print(f'Full witness certificate: {path}')


if __name__ == '__main__':
    main()
