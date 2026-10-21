"""Replay all bounded-search rows through independent moment inversion.

No import from the row producer. Reuse the independently written
seven-column inversion from the existing table verifier. This validates
only the saved assignments, not a uniform triangle bound.
"""
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import json
from verify_fixed_union_table import invert, mul

ROOT = Path(__file__).parent
F = 97


def main():
    data = json.loads((ROOT/'three-row-search.json').read_text())
    H = tuple(x for x in range(1,F) if pow(x,16,F)==1)
    counts = {'assignments':0,'support_rows':0,'scalar_tests':0,
              'both_zero_tests':0,'gated_rows':0,'zero_fourth_weight_rows':0}
    maxima = []
    failures = []
    assert data['witness'] is None  # This replay checks the completed no-survivor run.
    assert len(data['cases'])==len(data['planned_assignments'])==256
    assignments = set()
    for case,plan in zip(data['cases'],data['planned_assignments']):
        P,Y,Z,W = (tuple(case[k]) for k in ('P','Y','Z','W'))
        assert [list(x) for x in (P,Y,Z,W)]==plan
        assert len(set(P+Y+Z+W))==9 and set(P+Y+Z+W)<=set(H)
        assert (P,Y,Z,W) not in assignments
        assignments.add((P,Y,Z,W))
        U = set(P+Y+Z+W)
        cx = {}
        for x in U:
            value = 1
            for h in H:
                if h not in U:
                    value = value*(x-h) % F
            cx[x] = value
        moments = [[sum(cx[x]*pow(x,j,F) for x in pair) % F for j in range(1,9)]
                   for pair in (Y,Z)]
        expected = list(combinations([x for x in H if x not in P],4))
        assert [tuple(row['K']) for row in case['rows']]==expected
        fibers = defaultdict(set)
        for row,K in zip(case['rows'],expected):
            matrix = [[pow(x,j,F) for x in (*K,*P)] for j in range(1,9)]
            inverse = invert(matrix[:7])
            sy,sz = (mul(inverse,v[:7]) for v in moments)
            ry,rz = [(v[7]-mul(matrix[7:],s)[0]) % F for v,s in zip(moments,(sy,sz))]
            if ry==rz==0:
                kind,tests = 'both_zero',list(range(1,96))
            elif ry==0 or rz==0:
                kind,tests = 'one_zero',[]
            else:
                mu = rz*pow(ry,-1,F) % F
                kind,tests = 'isolated',([mu] if mu!=96 else [])
            assert row['kind']==kind
            assert [entry[0] for entry in row['tests']]==tests
            for mu,entry in zip(tests,row['tests']):
                d = [(z-mu*y) % F for y,z in zip(sy[4:],sz[4:])]
                weight = ((1+d[0]*pow(cx[P[0]],-1,F))*pow(1+mu,-1,F) % F,
                          d[1]*pow(mu*cx[P[1]] % F,-1,F) % F,
                          -d[2]*pow(cx[P[2]],-1,F) % F)
                gated = all(x not in (0,1) for x in weight)
                assert entry==[mu,*weight,int(gated)]
                counts['scalar_tests']+=1
                counts['both_zero_tests']+=int(kind=='both_zero')
                if gated:
                    omega = [(z-mu*y) % F for y,z in zip(sy[:4],sz[:4])]
                    actual = {x:-mu*cx[x] % F for x in Y}
                    actual.update({x:cx[x] for x in Z})
                    p,q,r = weight
                    actual.update({P[0]:cx[P[0]]*(1-(1+mu)*p) % F,
                                   P[1]:-mu*cx[P[1]]*q % F,P[2]:cx[P[2]]*r % F})
                    residual = [(sum(o*pow(x,j,F) for x,o in zip(K,omega))-
                                 sum(v*pow(x,j,F) for x,v in actual.items())) % F
                                for j in range(1,9)]
                    if any(residual):
                        failures.append({'P':P,'Y':Y,'Z':Z,'K':K,'mu':mu,'residual8':residual})
                    counts['gated_rows']+=1
                    counts['zero_fourth_weight_rows']+=int(not all(omega))
                    fibers[weight].add(mu)
            counts['support_rows']+=1
        maximum = max(map(len,fibers.values()),default=0)
        assert maximum==case['maximum_D'] and maximum<3
        assert not case['three_scalar_fibers']
        maxima.append(maximum)
        counts['assignments']+=1
    assert counts['support_rows']==256*715
    result = {'scope':'All saved assignments only; no uniform bound',
              'counts':counts,'maximum_D_by_case':maxima,'maximum_D':max(maxima),
              'required_triple_threshold':3,'necessary_violation_threshold':7,
              'failures':failures,'actual_failures':len(failures),'required_failures':0}
    output = ROOT/'three-row-search-verification.json'
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(counts,sort_keys=True))
    print(f'Maximum D / triple threshold / necessary violation: {max(maxima)}/3/7; failures {len(failures)}/0')
    print(f'Certificate: {output}')
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()
