"""Independent rational audit; no generator imports or trusted row signs.

Rebuilds recursive values in total-weight order, all children and scope,
source D via multinomial normalization, and original assignment values.
"""
import json
import sys
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).parent
OUT = BASE/'four-block-audit-results.json'


@lru_cache(None)
def choose(n,k):
    return 0 if not 0 <= k <= n else factorial(n)//(factorial(k)*factorial(n-k))


def multinomial(n,parts):
    assert min(parts) >= 0 and sum(parts) == n
    result = factorial(n)
    for k in parts:
        result //= factorial(k)
    return result


def enc(x):
    return [x.numerator,x.denominator]


def canonical(blocks):
    answer = []
    for weight,length in blocks:
        assert 0 <= weight <= length
        reduced = length-weight if 2*weight > length else weight
        if reduced > 0:
            answer.append((reduced,length))
    return tuple(answer)


def main():
    cert = json.loads((BASE/'four-block-results.json').read_text())
    lp = json.loads((BASE/'delsarte-lp-results.json').read_text())
    old = json.loads((BASE/'selected-triple-sdp-results.json').read_text())
    scalar = json.loads((BASE/'full-scalar-results.json').read_text())
    failures, violations = [], []

    def require(test,label):
        if not test:
            failures.append(label)

    require(cert['parameters']=={'n':1024,'w':68,'v':956,'d':10,'residual_cap':10},
            'exact approved parameters')
    x = [Q(r['numerator'],r['denominator']) for r in lp['exact']['primal']]
    require(len(x)==64,'64 L021 coordinates')
    defining_slacks = []
    for j in range(1,65):
        polynomial = [0]*69
        for r in range(69-j):
            base = choose(68-j,r)*choose(956-j,r)
            for h in range(j+1):
                polynomial[r+h] += base*(-1)**h*choose(j,h)
        slack = 1+sum(Q(polynomial[i],choose(68,i)*choose(956,i))*x[i-5]
                      for i in range(5,69))
        require(slack==0,'L021 defining equation '+str(j))
        defining_slacks.append(enc(slack))
    p = [Q(1)]+[Q(0)]*4+[x[i-5]/(2*choose(68,i)*choose(956,i)) for i in range(5,69)]
    require(p==[Q(*z) for z in cert['p']]==[Q(*z) for z in old['p']]
            ==[Q(*z) for z in scalar['p']],'all unchanged pair values')
    require(p[0]==1 and p[68]>0 and all(z>=0 for z in p),'pair sign hypotheses')
    H = cert['common_denominator']
    require(H>0 and [z*H for z in p]==cert['pair_scaled_numerators'],
            'positive lossless pair denominator')

    def value(i,j,h):
        if any(z in (1,2,3,4) for z in (i,j,h)):
            return Q(0),'forbidden'
        if 0 in (i,j,h):
            a,b,c = sorted((i,j,h))
            require(b==c,'repeated distances')
            return p[b],'repeated'
        return p[i]*p[j]*p[h]/p[68],'product'

    states = cert['recursion_states']
    index = {}
    for k,row in enumerate(states):
        key = tuple(map(tuple,row['blocks']))
        require(key==canonical(key) and key not in index,'unique normalized recursion state '+str(k))
        require(row['total_weight']==sum(u for u,n in key)<=10,'state weight '+str(k))
        index[key] = k
    rebuilt, children = {}, {}
    depth, state_counts = {}, [0]*11
    branch_count = 0
    # Independent induction order rather than generator call order.
    for key in sorted(index,key=lambda z:(sum(u for u,n in z),z)):
        total = sum(u for u,n in key)
        row = states[index[key]]
        expected_branches, child_keys = [], []
        if total < 5:
            R,kind,max_depth = 1,'below-distance',0
        elif total == 5:
            R,kind,max_depth = min(int(Q(n,u)) for u,n in key),'disjoint-supports',0
        else:
            kind = 'shorten'
            for a,(u,n) in enumerate(key):
                child = tuple((z-1,k-1) if b==a else (z,k)
                              for b,(z,k) in enumerate(key))
                ck = canonical(child)
                require(sum(z for z,k in ck)==total-1,'strict weight descent')
                require(ck in rebuilt,'complete lower-weight child')
                candidate = Q(n,u)*rebuilt[ck]
                floor_value = candidate.numerator//candidate.denominator
                expected_branches.append({'block':a,'child':index[ck],'candidate':floor_value})
                child_keys.append(ck)
            R = min(z['candidate'] for z in expected_branches)
            max_depth = 1+max(depth[z] for z in child_keys)
        require(row['kind']==kind and row['R']==R and row['branches']==expected_branches,
                'complete exact recursion '+str(index[key]))
        rebuilt[key],children[key],depth[key] = R,child_keys,max_depth
        state_counts[total] += 1
        branch_count += len(expected_branches)
    require(max(depth.values())<=5,'approved five-level bound')
    rows = {tuple(r['orbit']):r for r in cert['rows']}
    require(len(rows)==len(cert['rows']),'unique original ordered rows')
    scalar_entries = {(r['i'],r['j']):r for r in scalar['entries']}
    old_orbits = {tuple(o) for r in old['orbits'] for o in r['closure']}
    seen, roots = set(),set()
    counts = {k:0 for k in cert['counts']}
    weight_counts = [0]*11
    minimum, minimum_orbit = None,None
    for i in range(69):
        for j in range(69):
            ts = [t for t in range(69) if min(i-t,j-t,t,68-i-j+t)>=0]
            ss = [s for s in range(69) if min(i-s,j-s,s,956-i-j+s)>=0]
            for t in ts:
                for s in ss:
                    counts['all_actual_ordered_orbits'] += 1
                    lengths, weights = (i,68-i,i,956-i),(t,j-t,s,j-s)
                    complemented = [n-b if 2*b>n else b for b,n in zip(weights,lengths)]
                    total = sum(complemented)
                    if total > 10:
                        require((i,j,t,s) not in rows,'no unselected row')
                        continue
                    original = (i,j,t,s)
                    require(original in rows,'every selected actual orbit')
                    row = rows[original]
                    seen.add(original)
                    h = i+j-t-s
                    key = canonical(zip(weights,lengths))
                    roots.add(key)
                    require(key in index,'all row coefficients retained')
                    R = rebuilt[key]
                    # D is reconstructed by the source multinomial-to-pair ratio.
                    M1 = multinomial(68,(i-t,j-t,t,68-i-j+t))
                    M2 = multinomial(956,(i-s,j-s,s,956-i-j+s))
                    Dq = Q(M1*M2,choose(68,i)*choose(956,i))
                    require(Dq.denominator==1 and Dq>0,'positive integer source coefficient')
                    D = Dq.numerator
                    y,branch = value(i,j,h)
                    slack = R*p[i]-D*y  # Never divides by p_i.
                    require(row['h']==h and row['t_minus_s']==t-s and row['block_lengths']==list(lengths)
                            and row['block_weights']==list(weights) and row['complemented_weights']==complemented
                            and row['residual_weight']==total,'complete original source indices '+str(original))
                    require(row['recursion']==index[key] and row['R']==R and row['D']==D,
                            'independent coefficient '+str(original))
                    require(row['assignment_branch']==branch and Q(row['y_numerator'],H)==y
                            and Q(row['slack_numerator'],H)==slack,'exact rational row '+str(original))
                    sr = scalar_entries[i,j]
                    rec = scalar['evaluation_records'][sr['h_ids'][h-sr['h_min']]]
                    require(Q(rec['y'],scalar['scalar_denominator'])==y,'old scalar overlap')
                    counts['scalar_overlaps'] += 1
                    counts['selected_orbits'] += 1
                    counts[branch] += 1
                    counts['zero_length_orbits'] += (0 in lengths)
                    counts['zero_pair_orbits'] += (p[i]==0)
                    counts['old_closure_overlaps'] += (original in old_orbits)
                    weight_counts[total] += 1
                    sign = 'negative_slacks' if slack<0 else 'zero_slacks' if slack==0 else 'strict_positive_slacks'
                    counts[sign] += 1
                    if minimum is None or slack<minimum:
                        minimum,minimum_orbit = slack,list(original)
                    if slack<0:
                        violations.append({'orbit':list(original),'slack':enc(slack)})
        if i%16==0 or i==68:
            print('Independent four-block audit through i =',i,flush=True)
    require(seen==set(rows),'exact selected orbit domain, no extras')
    reached, pending = set(),list(roots)
    while pending:
        key = pending.pop()
        if key not in reached:
            reached.add(key)
            pending.extend(children[key])
    require(reached==set(index),'exact complete recursive closure, no extras')
    old_values = 0
    for row in old['orbits']:
        a,b,c,u = row['key']
        require(value(a,b,c)[0]==Q(*row['value']),'all 7093 old orbit-class values')
        old_values += 1
    require(counts==cert['counts'] and weight_counts==cert['residual_weight_counts'],'all regenerated counts')
    require(cert['minimum']=={'slack':enc(minimum),'orbit':minimum_orbit},'exact global minimum')
    stored_violations = [cert['rows'][k] for k in cert['violating_row_indices']]
    require([{'orbit':r['orbit'],'slack':enc(Q(r['slack_numerator'],H))} for r in stored_violations]
            ==violations,'all violating original rows')
    objective = sum(choose(68,i)*choose(956,i)*p[i] for i in range(69))
    threshold = Q(65537**28,2**128)
    require(objective==(Q(choose(1024,64),choose(68,64))+1)/2==Q(*cert['objective']),
            'unchanged objective')
    require(threshold==Q(*cert['required_threshold']) and Q(1383,1000)<objective/threshold<Q(1384,1000)
            and objective.__floor__()>threshold,'actual/required threshold comparison')
    require(not cert['failures'] and cert['stage']=='completed','complete generator')
    require(cert['selected_family_passes']==(not violations),'pass/violation agreement')
    result = {'verified':not failures,'selected_family_passes':not violations and not failures,
              'counts':counts,'residual_weight_counts':weight_counts,
              'recursive_states_verified':len(states),'recursive_branches_verified':branch_count,
              'state_weight_counts':state_counts,'maximum_shortening_depth':max(depth.values()),
              'all_old_orbit_values_checked':old_values,'L021_defining_slacks':defining_slacks,
              'minimum':{'slack':enc(minimum),'orbit':minimum_orbit},
              'violations':violations,'failures':failures,'objective':enc(objective),
              'required_threshold':enc(threshold),'scaled_floor_excess':2**128*objective.__floor__()-65537**28,
              'scope':'residual cap 10 with fixed recursive upper coefficients; no other row or full-SDP claim'}
    OUT.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print('Verified:',not failures,'; selected family passes:',result['selected_family_passes'])
    print('Counts:',counts,'; recursion states:',len(states),'; branches:',branch_count)
    print('Exact minimum:',minimum,'; orbit:',minimum_orbit)
    print('Actual objective:',objective,'; required <=',threshold)
    print('Violations:',len(violations),'; failures:',failures,'; audit certificate:',OUT)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
