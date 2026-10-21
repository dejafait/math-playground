"""Independent full certificate replay using seven-column moment inversion.

No imports from the producer and no support polynomials, beta equations,
projected quotient formula, or L059 point formula. Read every support,
scalar test, rejected gate and retained row; reconstruct complete fibers.
"""
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import json
import argparse

F = 97


def invert(matrix):
    n = len(matrix)
    rows = [list(row)+[int(i==j) for j in range(n)] for i,row in enumerate(matrix)]
    for j in range(n):
        i = next(i for i in range(j,n) if rows[i][j] % F)
        rows[j], rows[i] = rows[i], rows[j]
        pivot = pow(rows[j][j] % F, -1, F)
        rows[j] = [x*pivot % F for x in rows[j]]
        for i in range(n):
            if i != j:
                pivot = rows[i][j]
                rows[i] = [(x-pivot*y) % F for x,y in zip(rows[i],rows[j])]
    return [row[n:] for row in rows]


def mul(matrix, vector):
    return [sum(x*y for x,y in zip(row,vector)) % F for row in matrix]


def run():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--shared-labels', type=int, nargs=3, default=[1,8,12],
                        help='Ordered labels a b c, supplied independently of certificate')
    parser.add_argument('--singleton-pool', type=int, nargs=6,
                        default=[18,22,27,33,47,50])
    parser.add_argument('--certificate', type=Path,
                        default=Path(__file__).with_name('fixed-union-table.json'))
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('fixed-union-table-verification.json'))
    args = parser.parse_args()
    path = args.certificate.resolve()
    data = json.loads(path.read_text())
    H = tuple(x for x in range(1,F) if pow(x,16,F)==1)
    P = tuple(args.shared_labels)
    assert len(set(P)) == 3 and set(P) <= set(H)
    S = tuple(sorted(args.singleton_pool))
    assert len(set(S)) == 6 and set(S) <= set(H) - set(P)
    U = tuple(sorted((*P,*S)))
    assert tuple(data['H']) == H and tuple(data['P']) == P and tuple(data['U']) == U
    cx = {}
    for x in U:
        value = 1
        for h in H:
            if h not in U:
                value = value*(x-h) % F
        cx[x] = value
    assert data['CX'] == {str(x):v for x,v in cx.items()}
    expected_cases = set()
    for Y in combinations(S,2):
        rest = tuple(x for x in S if x not in Y)
        for Z in combinations(rest,2):
            expected_cases.add((Y,Z,tuple(x for x in rest if x not in Z)))
    observed_cases = [(tuple(case['Y']),tuple(case['Z']),tuple(case['W']))
                      for case in data['cases']]
    assert len(observed_cases)==len(set(observed_cases))==90
    assert set(observed_cases)==expected_cases
    supports = tuple(combinations(tuple(x for x in H if x not in P),4))
    blocks = {}
    for K in supports:
        matrix = [[pow(x,j,F) for x in (*K,*P)] for j in range(1,9)]
        blocks[K] = (matrix, invert(matrix[:7]))
    failures, counts, maxima = [], Counter(), Counter()
    for case in data['cases']:
        Y, Z = tuple(case['Y']),tuple(case['Z'])
        observed_supports = [tuple(row['K']) for row in case['rows']]
        assert len(observed_supports)==len(set(observed_supports))==715
        assert set(observed_supports)==set(supports)
        moments = [[sum(cx[x]*pow(x,j,F) for x in pair) % F for j in range(1,9)]
                   for pair in (Y,Z)]
        fibers, kinds, gates = defaultdict(set), Counter(), Counter()
        for row in case['rows']:
            K = tuple(row['K'])
            matrix,inverse = blocks[K]
            solved = [mul(inverse, v[:7]) for v in moments]
            residual = [(v[7]-mul(matrix[7:], s)[0]) % F
                        for v,s in zip(moments,solved)]
            ry,rz = residual
            if ry==rz==0:
                kind,tests = 'both_zero',tuple(range(1,96))
            elif ry==0 or rz==0:
                kind,tests = 'one_zero',()
            else:
                mu = rz*pow(ry,-1,F) % F
                kind,tests = 'isolated', ((mu,) if mu !=96 else ())
                assert row['isolated_mu']==mu
            assert row['kind']==kind
            kinds[kind]+=1
            assert tuple(e['mu'] for e in row['tested'])==tests
            for mu,entry in zip(tests,row['tested']):
                sY,sZ = solved
                # Cancel the three P coefficients of Z-mu Y by adding
                # ca*(1-(1+mu)p), -mu*cb*q, cc*r respectively.
                d = [(z-mu*y) % F for y,z in zip(sY[4:],sZ[4:])]
                weight = ((1+d[0]*pow(cx[P[0]],-1,F))*pow(1+mu,-1,F) % F,
                          d[1]*pow(mu*cx[P[1]] % F,-1,F) % F,
                          -d[2]*pow(cx[P[2]],-1,F) % F)
                assert tuple(entry['weights'])==weight
                gated = all(x not in (0,1) for x in weight)
                assert entry['gated']==gated
                gates['gated' if gated else 'nongated']+=1
                counts['scalar_tests']+=1
                if gated:
                    omega = [(z-mu*y) % F for y,z in zip(sY[:4],sZ[:4])]
                    assert entry['omega']==omega
                    assert entry['residual8']==[0]*8
                    if (rz-mu*ry) % F:
                        failures.append({'Y':Y,'Z':Z,'K':K,'mu':mu})
                    counts['gated']+=1
                    counts['both_zero_gated']+=int(kind=='both_zero')
                    counts['zero_weights']+=int(not all(omega))
                    fibers[weight].add(mu)
            counts['supports']+=1
        maximum = max(map(len,fibers.values()),default=0)
        maxima[maximum]+=1
        assert case['maximum_D']==maximum
        assert case['kind_counts']==dict(kinds) and case['gate_counts']==dict(gates)
        assert case['fiber_histogram']=={str(k):v for k,v in Counter(map(len,fibers.values())).items()}
        expected_max = [{'weights':list(w),'D':sorted(ms)} for w,ms in sorted(fibers.items())
                        if len(ms)==maximum]
        assert case['maximal_fibers']==expected_max
        survivors = sum(len(ms)>=7 for ms in fibers.values())
        assert case['survivor_count']==survivors==0 and case['full_tests']==[]
    summary=data['summary']
    assert summary['maximum_D']==max(maxima)
    assert summary['actual_support_rows']==counts['supports']==64350
    assert summary['direct_eight_moment_tests']==counts['gated']
    assert summary['both_zero_gated_rows']==counts['both_zero_gated']
    assert summary['zero_fourth_weight_rows_retained']==counts['zero_weights']
    assert summary['seven_scalar_survivors']==0
    assert summary['required_cases']==90 and summary['required_support_rows']==64350
    assert summary['required_violation_D']==7 and summary['required_failures']==0
    assert summary['maximum_histogram']=={str(k):v for k,v in maxima.items()}
    assert data['failures']==[] and summary['actual_failures']==0
    result={'scope':'Complete independent replay of fixed-P/fixed-U 90-case tables only',
            'P':P,'U':U,
            'certificate':str(path.relative_to(Path(__file__).parents[2])),
            'actual_cases':len(observed_cases),'required_cases':90,
            'counts':dict(counts),'maximum_D':max(maxima),'required_violation_D':7,
            'maximum_histogram':dict(maxima),'actual_failures':len(failures),
            'required_failures':0,'failures':failures}
    output=args.output
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(f"Cases actual/required: {len(observed_cases)}/90; rows: {counts['supports']}/64350; "
          f"all scalar tests replayed: {counts['scalar_tests']}; maximum D/threshold: {max(maxima)}/7")
    print(f'Failures actual/required: {len(failures)}/0; verification: {output}')
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    run()
