"""Independent exact audit: all recursion identities, heads and rational rows.

Imports no generator routine. Uses factorial binomials, polynomial pair
reconstruction, a bottom-up induction and explicit root reachability.
"""
import json
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial
from pathlib import Path

BASE = Path(__file__).parent
OUT = BASE / 'conditional-shell-audit-results.json'


@lru_cache(None)
def choose(n, k):
    return factorial(n)//(factorial(k)*factorial(n-k)) if 0 <= k <= n else 0


def enc(x):
    x = Q(x)
    return [x.numerator, x.denominator]


def canonical(blocks):
    result = []
    for b, n in blocks:
        if not (isinstance(b, int) and isinstance(n, int) and 0 <= b <= n):
            raise ValueError((b, n))
        weight = n-b if 2*b > n else b
        if weight:
            result.append((weight, n))
    return tuple(result)


def main():
    cert = json.loads((BASE/'conditional-shell-results.json').read_text())
    lp = json.loads((BASE/'delsarte-lp-results.json').read_text())
    old = json.loads((BASE/'selected-triple-sdp-results.json').read_text())
    failures = []

    def require(test, label):
        if not test:
            failures.append(label)

    require(cert['parameters'] == {'n':1024,'w':68,'v':956,'d':10,
                                   'delta':5,'Delta':63,'i':67,'j':68}, 'parameters')
    require(5 <= 67 < 68 <= 68 <= 1024//2 and 67+68 <= 1024-5,
            'Proposition 17 hypotheses and branch domain')
    x = [Q(z['numerator'], z['denominator']) for z in lp['exact']['primal']]
    require(len(x) == 64 and all(a > 0 for a in x), 'L021 vector')
    equations = []
    for j in range(1,65):
        polynomial = [0]*69
        for r in range(69-j):
            base = choose(68-j,r)*choose(956-j,r)
            for h in range(j+1):
                polynomial[r+h] += base*(-1)**h*choose(j,h)
        slack = 1+sum(Q(polynomial[i],choose(68,i)*choose(956,i))*x[i-5]
                      for i in range(5,69))
        require(slack == 0, 'defining pair equation '+str(j))
        equations.append(enc(slack))

    states, index = cert['recursion_states'], {}
    for sid, state in enumerate(states):
        blocks = tuple(map(tuple,state['blocks']))
        key = state['d'], blocks
        require(state['d'] in (8,10) and blocks == canonical(blocks), 'normalized state '+str(sid))
        require(key not in index and state['S'] == sum(u for u,n in blocks), 'unique weight '+str(sid))
        index[key] = sid
    rebuilt, links, depths = {}, {}, {}
    branch_count = 0
    counts = {8: {}, 10: {}}
    for key in sorted(index, key=lambda k:(sum(u for u,n in k[1]),k)):
        d, blocks = key
        S = sum(u for u,n in blocks)
        state = states[index[key]]
        branches, children = [], []
        if S < d//2:
            R, kind, depth = 1, 'below-distance', 0
        elif S == d//2:
            R, kind, depth = min(int(Q(n,u)) for u,n in blocks), 'disjoint-supports', 0
        else:
            kind = 'shorten'
            for a,(u,n) in enumerate(blocks):
                child = [(b-1,k-1) if t == a else (b,k)
                         for t,(b,k) in enumerate(blocks)]
                ck = d, canonical(child)
                require(sum(b for b,k in ck[1]) == S-1 and ck in rebuilt,
                        'strict descent and every child '+str(index[key]))
                candidate = int(Q(n*rebuilt[ck],u))
                branches.append({'block':a,'child':index[ck],'candidate':candidate})
                children.append(ck)
            R = min(b['candidate'] for b in branches)
            depth = 1+max(depths[ck] for ck in children)
        require(state['R'] == R and R >= 1 and state['kind'] == kind
                and state['branches'] == branches, 'complete recursion identity '+str(index[key]))
        rebuilt[key], links[key], depths[key] = R, children, depth
        branch_count += len(branches)
        counts[d][S] = counts[d].get(S,0)+1

    roots = []

    def check_root(d, blocks, record):
        key = d, canonical(blocks)
        roots.append(key)
        require(record['blocks'] == blocks and record['normalized'] == [list(z) for z in key[1]]
                and record['state'] == index[key], 'root input and normalization')
        return rebuilt[key]

    require(len(cert['pairs']) == 2, 'two pairs')
    occupancies, caps = [], []
    pair_evidence = []
    for a, record in zip((67,68),cert['pairs']):
        p = x[a-5]/(2*choose(68,a)*choose(956,a))
        B = choose(68,a)*choose(956,a)*p
        R = check_root(10,[[a,68],[a,956]],record)
        require(record['a'] == a and record['P'] == R and Q(*record['p']) == p
                and p == Q(*old['p'][a]) and Q(*record['B']) == B == x[a-5]/2,
                'unchanged shell '+str(a))
        occupancies.append(B)
        caps.append(R)
        pair_evidence.append({'a':a,'p':enc(p),'B':enc(B),'P':R})

    totals, partition_evidence = [], []
    require(len(cert['partitions']) == 2, 'two prescribed partitions')
    for data, record in zip(((63,68,4,888,8),(63,67,5,889,10)),cert['partitions']):
        w1,n1,w2,n2,d = data
        require(record['input'] == list(data) and len(record['summands']) == 64, 'partition input')
        hypotheses = []
        for cap in range(63,0,-1):
            tail = w1+w2-cap
            p_parameter = min(cap,n2-tail)
            require(p_parameter > 0, 'Theorem 26 e=0 prerequisite')
            hypotheses.append({'head_cap':cap,'tail_floor':tail,'p':p_parameter,'e':0})
        values = []
        for a, row in enumerate(record['summands']):
            b = w1+w2-a
            require(row['head'] == a and 0 <= a <= n1 and 0 <= b <= n2, 'all head weights')
            R = check_root(d,[[a,n1],[b,n2]],row)
            require(row['R'] == R, 'summand identity')
            values.append(R)
        total = sum(values)
        require(record['sum'] == total, 'full partition sum')
        totals.append(total)
        partition_evidence.append({'input':list(data),'summands':values,'sum':total,
                                   'Theorem_26_hypotheses':hypotheses,
                                   'terminal_weight':w1+w2})
    reachable, queue = set(), list(roots)
    while queue:
        key = queue.pop()
        if key not in reachable:
            reachable.add(key)
            queue.extend(links[key])
    require(reachable == set(index), 'exact reachable state closure')

    Pi,Pj = caps
    Pij,Pji = min(Pi,totals[0]),min(Pj,totals[1])
    coefficients = {'Pi':Pi,'Pj':Pj,'Pij':Pij,'Pji':Pji}
    require(Pi > 0 and Pj > 0 and 0 <= Pij <= Pi and 0 <= Pji <= Pj,
            'coefficient sign and clipping hypotheses')
    require(cert['coefficients'] == coefficients, 'all coefficient identities')
    sign = Pij*Pj+Pji*Pi-Pi*Pj
    ratio = Q(Pij,Pi)+Q(Pji,Pj)
    require(cert['branch_sign'] == sign and Q(*cert['ratio']) == ratio
            and (sign > 0) == (ratio > 1), 'exact ratio branch including equality')
    Bi,Bj = occupancies
    definitions = ([(62,Pji,Pi-Pij,Pi*Pji),(63,Pj-Pji,Pij,Pj*Pij)] if sign > 0
                   else [(64,Pj,Pi,Pi*Pj)])
    expected_rows = []
    for eq,a,b,rhs in definitions:
        lhs = a*Bi+b*Bj
        expected_rows.append({'equation':eq,'coefficients':[a,b],'rhs':rhs,
                              'lhs':enc(lhs),'slack':enc(rhs-lhs)})
    require(cert['rows'] == expected_rows, 'every polynomial row and rational slack')
    individual = [{'a':a,'slack':enc(P-B)} for a,P,B in zip((67,68),caps,occupancies)]
    require(cert['individual_caps'] == individual, 'independent individual-cap comparison')
    redundant = Pij == Pi and Pji == Pj
    if redundant:
        require(Q(*expected_rows[0]['slack']) == Pj*(Pi-Bi)
                and Q(*expected_rows[1]['slack']) == Pi*(Pj-Bj), 'source redundancy identities')
    U = Q(choose(1024,64),choose(68,64))
    objective,threshold = (U+1)/2,Q(65537**28,2**128)
    require(1+sum(x)/2 == objective == Q(*old['summary']['objective']), 'unchanged objective')
    require(cert['objective'] == enc(objective) and cert['threshold'] == enc(threshold)
            and cert['objective_ratio'] == enc(objective/threshold), 'threshold comparison identities')
    require(Q(1383,1000) < objective/threshold < Q(1384,1000)
            and objective.numerator//objective.denominator > threshold, 'above-threshold floor')
    violations = [r['equation'] for r in expected_rows if Q(*r['slack']) < 0]
    summary = {'state_count':len(states),'branch_count':branch_count,
               'conditional_equals_individual':redundant,'violated_rows':violations,'failures':[]}
    require(cert['summary'] == summary, 'generator summary recomputed')
    output = {'parameters':cert['parameters'],'pair_evidence':pair_evidence,
              'defining_equation_slacks':equations,'partition_evidence':partition_evidence,
              'coefficients':coefficients,'branch_sign':sign,'ratio':enc(ratio),
              'rows':expected_rows,'individual_caps':individual,
              'state_counts_by_distance_and_weight':counts,
              'maximum_shortening_depth':max(depths.values()),
              'state_count':len(states),'branch_count':branch_count,
              'reachable_state_count':len(reachable),'all_recursion_identities_checked':True,
              'objective':enc(objective),'threshold':enc(threshold),
              'objective_ratio':enc(objective/threshold),
              'floor_objective_excess':enc(objective.numerator//objective.denominator-threshold),
              'conditional_equals_individual':redundant,'violated_rows':violations,'failures':failures}
    OUT.write_text(json.dumps(output,separators=(',', ':'))+'\n')
    print('Audited coefficients:', coefficients)
    print('Partition sums:',totals)
    print('States / branches / reachable:',len(states),branch_count,len(reachable))
    print('Ratio:',ratio,'; required branch > 1:',sign > 0,'; both caps equal:',redundant)
    for r in expected_rows:
        print('Row',r['equation'],'actual slack',Q(*r['slack']),'; required >= 0')
    print('Individual cap slacks:',[Q(*r['slack']) for r in individual],'; required >= 0')
    print('Objective ratio strictly between 1.383 and 1.384:', Q(1383,1000)<objective/threshold<Q(1384,1000))
    print('Violations:',violations,'; audit failures:',failures)
    print('Audit:',OUT)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
