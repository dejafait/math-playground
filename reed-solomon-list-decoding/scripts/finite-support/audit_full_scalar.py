"""Independent full scalar audit; imports no generator routines.

Reconstructs source multinomial scope and each rational cached value,
then verifies every ordered orbit, sign and distance permutation.
"""
import json
import sys
from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations
from math import factorial, lcm
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).parent
OUT = BASE / 'full-scalar-audit-results.json'


@lru_cache(None)
def choose(n,k):
    return 0 if k < 0 or k > n else factorial(n)//(factorial(k)*factorial(n-k))


def enc(x):
    return [x.numerator,x.denominator]


def main():
    cert = json.loads((BASE/'full-scalar-results.json').read_text())
    old = json.loads((BASE/'selected-triple-sdp-results.json').read_text())
    lp = json.loads((BASE/'delsarte-lp-results.json').read_text())
    failures, violations = [], []

    def require(test,label):
        if not test:
            failures.append(label)

    def valid(i,j,t,s):
        return min(i-t,j-t,t,68-i-j+t,i-s,j-s,s,956-i-j+s) >= 0

    require(cert['parameters']=={'n':1024,'w':68,'v':956,'d':10}, 'exact source instance')
    x = [Q(r['numerator'],r['denominator']) for r in lp['exact']['primal']]
    require(len(x)==64, '64 L021 pair coordinates')
    # Independently check the defining Ax=1 equations using convolution.
    # L021 establishes nonsingularity, so these equations fix its witness.
    defining_slacks = []
    for j in range(1,65):
        polynomial = [0]*69
        for r in range(69-j):
            base = choose(68-j,r)*choose(956-j,r)
            for h in range(j+1):
                polynomial[r+h] += base*((-1)**h)*choose(j,h)
        slack = 1+sum(Q(polynomial[i],choose(68,i)*choose(956,i))*x[i-5]
                      for i in range(5,69))
        defining_slacks.append(enc(slack))
        require(slack==0, 'L021 defining equation '+str(j))
    p = [Q(1)]+[Q(0)]*4+[x[i-5]/(2*choose(68,i)*choose(956,i)) for i in range(5,69)]
    require(p==[Q(*v) for v in cert['p']]==[Q(*v) for v in old['p']], 'unchanged all pair values')
    require(p[0]==1 and all(v>=0 for v in p) and p[68]>0, 'normalization and positive lambda')
    D = lcm(*(v.denominator for v in p))
    A = [int(v*D) for v in p]
    H = D*D*A[68]
    P = [a*D*A[68] for a in A]
    require(D>0 and H>0, 'positive common denominators')
    require((D,A,H)==(cert['pair_denominator'],cert['pair_numerators'],cert['scalar_denominator']),
            'positive lossless denominator clearing')

    def value(i,j,h):
        if any(z in (1,2,3,4) for z in (i,j,h)):
            return Q(0)
        if 0 in (i,j,h):
            _,b,c = sorted((i,j,h))
            require(b==c, 'repeated distances')
            return p[b]
        return p[i]*p[j]*p[h]/p[68]

    records = cert['evaluation_records']
    by_key = {}
    for index,row in enumerate(records):
        a,b,c = row['distances']
        require([a,b,c]==sorted((a,b,c)) and (a,b,c) not in by_key, 'unique numerical cache '+str(index))
        y = value(a,b,c)
        actual = y*H
        require(actual.denominator==1 and row['y']==actual.numerator, 'exact cache value '+str(index))
        upper = [p[z]-y for z in (a,b,c)]
        lower = [1+y-p[z]-p[k] for z,k in ((a,b),(a,c),(b,c))]
        require([v*H for v in upper]==row['upper'] and [v*H for v in lower]==row['lower'],
                'all six exact cached slacks '+str(index))
        by_key[a,b,c] = index
    entries = {(r['i'],r['j']):r for r in cert['entries']}
    require(len(entries)==len(cert['entries'])==69**2, 'all ordered entries, unique')
    old_orbits = {tuple(o) for row in old['orbits'] for o in row['closure']}
    visited_old, used_records = set(),set()
    counts = {'ordered_entries':len(entries),'actual_ordered_orbits':0,'expanded_scalar_rows':0,
              'permutation_checks':0,'forbidden_orbits':0,'repeated_orbits':0,
              'numerical_cache_records':len(records),'old_closure_orbits':0,'new_ordered_orbits':0}
    minima = [None]*3
    witnesses = [None]*3
    for i in range(69):
        for j in range(69):
            # Independent admissibility from the four parts, not source ranges.
            ts = [t for t in range(69) if min(i-t,j-t,t,68-i-j+t)>=0]
            ss = [s for s in range(69) if min(i-s,j-s,s,956-i-j+s)>=0]
            hs = sorted({i+j-t-s for t in ts for s in ss})
            row = entries[i,j]
            require(row['t_range']==[min(ts),max(ts)] and row['s_range']==[min(ss),max(ss)],
                    'complete source ranges '+str((i,j)))
            require(hs==list(range(min(hs),max(hs)+1)), 'contiguous h mapping')
            ids = [by_key[tuple(sorted((i,j,h)))] for h in hs]
            require(row['h_min']==min(hs) and row['h_ids']==ids, 'all lossless h maps '+str((i,j)))
            for t in ts:
                for s in ss:
                    h,u = i+j-t-s,t-s
                    require(valid(i,j,t,s) and 0<=h<=68, 'actual orbit')
                    idx = row['h_ids'][h-row['h_min']]
                    used_records.add(idx)
                    rec = records[idx]
                    require(rec['distances']==sorted((i,j,h)), 'original-orbit cache map')
                    y = rec['y']
                    slacks = [y,P[i]-y,H+y-P[i]-P[j]]
                    # The stored cached rows really represent these three rows.
                    key = rec['distances']
                    require(rec['upper'][key.index(i)]==slacks[1], 'mapped upper scalar row')
                    pair_positions = [(key[0],key[1]),(key[0],key[2]),(key[1],key[2])]
                    require(rec['lower'][pair_positions.index(tuple(sorted((i,j))))]==slacks[2],
                            'mapped lower scalar row')
                    for kind,slack in enumerate(slacks):
                        if minima[kind] is None or slack<minima[kind]:
                            minima[kind],witnesses[kind] = slack,[i,j,t,s]
                        if slack<0:
                            violations.append({'orbit':[i,j,t,s],
                                'kind':('nonnegative','upper','lower')[kind],
                                'slack':enc(Q(slack,H)),'value':enc(Q(y,H))})
                    if any(1<=z<=4 for z in (i,j,h)):
                        counts['forbidden_orbits']+=1
                        require(y==0, 'required distance zero')
                    if min(i,j,h)==0:
                        counts['repeated_orbits']+=1
                        require(u==0 and Q(y,H)==p[sorted((i,j,h))[1]], 'all repeated words')
                    for a,b,c in permutations((i,j,h)):
                        nn,mm = a+b-c+u,a+b-c-u
                        require(nn%2==0 and mm%2==0, 'permutation integrality')
                        tt,ss0 = nn//2,mm//2
                        require(valid(a,b,tt,ss0) and tt-ss0==u and a+b-tt-ss0==c,
                                'permutation actual original orbit and invariant')
                        other = entries[a,b]
                        oi = other['h_ids'][c-other['h_min']]
                        require(records[oi]['y']==y and records[oi]['distances']==sorted((a,b,c)),
                                'required source permutation equality')
                        counts['permutation_checks']+=1
                    counts['actual_ordered_orbits']+=1
                    counts['expanded_scalar_rows']+=3
                    if (i,j,t,s) in old_orbits:
                        visited_old.add((i,j,t,s))
        if i%16==0 or i==68:
            print('Independent ordered scalar audit through i =',i,flush=True)
    require(used_records==set(range(len(records))), 'no extraneous numerical records')
    require(visited_old==old_orbits, 'every old original orbit retained')
    counts['old_closure_orbits']=len(visited_old)
    counts['new_ordered_orbits']=counts['actual_ordered_orbits']-len(visited_old)
    require(counts==cert['counts'], 'all regenerated scope counts')

    old_values = 0
    for row in old['orbits']:
        a,b,c,u = row['key']
        require(value(a,b,c)==Q(*row['value']), 'old rational orbit value')
        old_values+=1
    for row in old['scalar_rows']:
        a,b,c,u = row['key']
        y = value(a,b,c)
        expected = y if row['kind']=='nonnegative' else p[row['i']]-y if row['kind']=='upper' else 1+y-p[row['i']]-p[row['j']]
        require(expected==Q(*row['slack']), 'old exact scalar row')
    old_pair_certificates = []
    for name in ('full-zero-block-results.json','mixed-zero-one-results.json'):
        other = json.loads((BASE/name).read_text())
        require(p==[Q(*v) for v in other['p']], 'unchanged pairs '+name)
        old_pair_certificates.append(name)
    objective = sum(choose(68,i)*choose(956,i)*p[i] for i in range(69))
    threshold = Q(65537**28,2**128)
    require(objective==(Q(choose(1024,64),choose(68,64))+1)/2==Q(*cert['objective']), 'objective exact')
    require(threshold==Q(*cert['required_threshold']), 'required threshold')
    require(Q(1383,1000)<objective/threshold<Q(1384,1000), 'ratio comparison')
    require(objective.__floor__()>threshold, 'integer-floor excess')
    require(violations==cert['violations'], 'every violating original row and exact residual')
    require(not cert['failures'] and cert['stage']=='completed', 'completed generator')
    scalar_feasible = not violations and not failures
    require(scalar_feasible==cert['scalar_feasible'], 'feasibility conclusion')
    result = {'verified':not failures,'scalar_feasible':scalar_feasible,
              'counts':counts,'old_orbit_values_checked':old_values,
              'old_reduced_scalar_rows_checked':len(old['scalar_rows']),
              'old_expanded_scalar_rows':3*len(visited_old),
              'new_expanded_scalar_rows':3*counts['new_ordered_orbits'],
              'old_pair_certificates_checked':old_pair_certificates,
              'L021_defining_slacks':defining_slacks,
              'minima':[{'kind':kind,'slack':enc(Q(v,H)),'orbit':o}
                        for kind,v,o in zip(('nonnegative','upper','lower'),minima,witnesses)],
              'violations':violations,'failures':failures,
              'objective':enc(objective),'required_threshold':enc(threshold),
              'scaled_floor_excess':2**128*objective.__floor__()-65537**28,
              'scope':'scalar only; no full-SDP, packing or RS-list claim'}
    OUT.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print('Independent verified:',not failures,'; scalar feasible:',scalar_feasible,'; counts:',counts)
    print('Actual objective:',objective,'; required <=',threshold)
    print('Scalar violations:',len(violations),'; audit failures:',failures,'; certificate:',OUT)
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()
