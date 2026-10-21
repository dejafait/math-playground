"""Bounded triple-fiber search, not a uniform count certificate.

Reuse L059's complete row producer, but check any positive witness by
direct eight-moment arithmetic in an explicit original finite chart.
Save every tested row, including rejected weights and both-zero tests.
"""
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import json
import random
import fixed_union_table as tab

OUT = Path(__file__).with_name('three-row-search.json')
F = 97


def assignments():
    rng = random.Random(145)
    seen = set()
    antipodes = [(x, F-x) for x in tab.H if x < F-x]
    plans = []
    for pairs in combinations(antipodes, 3):
        singleton = set(sum((list(pair) for pair in pairs), []))
        shared = tuple(rng.sample([x for x in tab.H if x not in singleton], 3))
        row = (shared, *pairs)
        seen.add(row)
        plans.append(row)
    while len(plans) < 256:
        labels = rng.sample(tab.H, 9)
        row = (tuple(labels[:3]), *(tuple(sorted(labels[i:i+2])) for i in (3,5,7)))
        if row not in seen:
            seen.add(row)
            plans.append(row)
    return plans


def witness_check(P, Y, Z, W, weights, selected):
    """Independent polynomial-evaluation chart and eight moment check.

    Input words are a*=e0 and b*=e1-e0 at gamma0=0, gamma1=1.
    Polynomial Q certifies the third base at gamma2=rho. Recovery
    uses first-four Vandermonde inversion, then checks all eight rows.
    """
    p,q,r = weights
    a,b,c = P
    mus = sorted(selected)
    rho = next(t for t in range(2,97)
               if all((t-(1-t)*mu) % F for mu in mus))
    alpha = ((1-rho) % F, rho, 96)
    normalized = ({a:p,b:q,**{x:1 for x in Y}},
                  {a:1-p,c:r,**{x:1 for x in Z}},
                  {b:1-q,c:1-r,**{x:1 for x in W}})
    # Recompute Q independently from the producer's coefficient table.
    union = set(P+Y+Z+W)
    coeff = {}
    for x in union:
        value = 1
        for h in tab.H:
            if h not in union:
                value = value*(x-h) % F
        coeff[x] = value
    base = [{x:coeff[x]*v*pow(ai,-1,F) % F for x,v in norm.items()}
            for norm,ai in zip(normalized,alpha)]
    def moment(word):
        return [sum(v*pow(x,j,F) for x,v in word.items()) % F for j in range(1,9)]
    sm = [moment(word) for word in base]
    failures = []
    third_residual = [(sm[2][j]-sm[0][j]-rho*(sm[1][j]-sm[0][j])) % F
                      for j in range(8)]
    if any(third_residual):
        failures.append('third base residual')
    if not all(all(word.values()) and len(word)==4 for word in base):
        failures.append('base fullness')
    output = []
    for mu in mus:
        K = selected[mu]
        E = (rho-(1-rho)*mu) % F
        T = rho*pow(E,-1,F) % F
        syndrome = [(x+T*(y-x)) % F for x,y in zip(sm[0],sm[1])]
        # Gaussian elimination implemented here independently of tab.invert.
        matrix = [[pow(x,j,F) for x in K]+[syndrome[j-1]] for j in range(1,5)]
        for col in range(4):
            pivot = next(i for i in range(col,4) if matrix[i][col])
            matrix[col],matrix[pivot] = matrix[pivot],matrix[col]
            scale = pow(matrix[col][col],-1,F)
            matrix[col] = [x*scale % F for x in matrix[col]]
            for i in range(4):
                if i != col:
                    scale = matrix[i][col]
                    matrix[i] = [(x-scale*y) % F for x,y in zip(matrix[i],matrix[col])]
        actual = {x:matrix[i][-1] for i,x in enumerate(K)}
        residual = [(x-y) % F for x,y in zip(moment(actual),syndrome)]
        if any(residual) or T in (0,1,rho):
            failures.append({'mu':mu,'residual':residual,'T':T})
        output.append({'K':K,'mu':mu,'E':E,'T':T,'weights':list(actual.values()),
                       'residual8':residual})
    if len({row['T'] for row in output}) != len(output):
        failures.append('duplicate parameters')
    return {'P':P,'Y':Y,'Z':Z,'W':W,'normalized_weights':weights,
            'gamma':[0,1,rho],'lambda':1,'Q_values':coeff,
            'base_errors':base,'third_base_residual8':third_residual,
            'recoveries':output,'failures':failures}


def main():
    plans = assignments()
    cases = []
    witness = None
    full = None
    for index,(P,Y,Z,W) in enumerate(plans):
        tab.P = P
        tab.U = tuple(sorted(P+Y+Z+W))
        tab.CX = {x:tab.prod(x-h for h in tab.H if h not in tab.U) for x in tab.U}
        fibers = defaultdict(dict)
        rows = []
        for K in combinations([x for x in tab.H if x not in P],4):
            J,vectors,beta,kind,mu = tab.label_data(K,Y,Z)
            tests = tab.M0 if kind=='both_zero' else ((mu,) if kind=='isolated' and mu in tab.M0 else ())
            entries = []
            for scalar in tests:
                weight = tab.point(beta,scalar)
                gated = all(x not in (0,1) for x in weight)
                entries.append([scalar,*weight,int(gated)])
                if gated:
                    fibers[weight].setdefault(scalar,K)
            rows.append({'K':K,'kind':kind,'projected':vectors,'beta':beta,'tests':entries})
        assert len(rows)==715
        maximum = max(map(len,fibers.values()),default=0)
        survivors = sorted(w for w,ms in fibers.items() if len(ms)>=3)
        cases.append({'P':P,'Y':Y,'Z':Z,'W':W,'maximum_D':maximum,
                      'three_scalar_fibers':[[list(w),sorted(fibers[w])] for w in survivors],
                      'rows':rows})
        if survivors:
            weight = survivors[0]
            witness = witness_check(P,Y,Z,W,weight,fibers[weight])
            if len(fibers[weight])>=7:
                full = tab.full_scalar_test(Y,Z,W,weight)
            break
    failures = witness['failures'] if witness else []
    result = {'scope':'Bounded search only; first triple survivor stops enumeration',
              'seed':145,'planned_assignments':plans,'cases':cases,'witness':witness,
              'full_M_if_seven':full,'failures':failures,
              'summary':{'tested_assignments':len(cases),'maximum_assignments':256,
                         'support_rows':len(cases)*715,'required_per_assignment':715,
                         'observed_maximum_D':max(c['maximum_D'] for c in cases),
                         'triple_test_threshold':3,'necessary_violation_threshold':7,
                         'actual_failures':len(failures),'required_failures':0}}
    OUT.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print(json.dumps(result['summary'],sort_keys=True))
    print(f'Certificate: {OUT}')
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()
