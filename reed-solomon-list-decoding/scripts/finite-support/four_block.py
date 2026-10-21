"""Fixed, gate-approved Theorem 12 test; exact integers, no optimization.

Every selected original ordered orbit is retained. Recursion evidence
records every branch, including those not attaining the minimum.
"""
import json
import sys
from fractions import Fraction as F
from math import comb, lcm
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).parent
OUT = BASE / 'four-block-results.json'
W, V, CAP = 68, 956, 10


def enc(x):
    return [x.numerator, x.denominator]


def normalize(blocks):
    result = []
    for u, n in blocks:
        assert 0 <= u <= n
        u = min(u, n-u)
        if u:
            result.append((u, n))
    return tuple(result)


def main():
    lp = json.loads((BASE/'delsarte-lp-results.json').read_text())
    old = json.loads((BASE/'selected-triple-sdp-results.json').read_text())
    scalar = json.loads((BASE/'full-scalar-results.json').read_text())
    p = [F(1)]+[F(0)]*4+[
        F(z['numerator'], z['denominator'])/(2*comb(W,i)*comb(V,i))
        for i,z in zip(range(5,69),lp['exact']['primal'])]
    assert p == [F(*z) for z in old['p']] == [F(*z) for z in scalar['p']]
    A_den = lcm(*(q.denominator for q in p))
    A = [int(q*A_den) for q in p]
    H = A_den*A_den*A[68]
    P = [a*A_den*A[68] for a in A]
    assert H > 0
    states, memo = [], {}

    def bound(blocks):
        key = normalize(blocks)
        if key in memo:
            return memo[key]
        total = sum(u for u,n in key)
        assert total <= CAP
        branches = []
        if total < 5:
            result, kind = 1, 'below-distance'
        elif total == 5:
            result, kind = min(n//u for u,n in key), 'disjoint-supports'
        else:
            kind = 'shorten'
            for a,(u,n) in enumerate(key):
                child = list(key)
                child[a] = (u-1,n-1)
                assert sum(z for z,k in normalize(child)) == total-1
                cid = bound(child)
                candidate = n*states[cid]['R']//u
                branches.append({'block':a, 'child':cid, 'candidate':candidate})
            result = min(b['candidate'] for b in branches)
        index = len(states)
        states.append({'blocks':list(map(list,key)), 'total_weight':total,
                       'kind':kind, 'R':result, 'branches':branches})
        memo[key] = index
        return index

    def numerator(i,j,h):
        if any(1 <= z <= 4 for z in (i,j,h)):
            return 0, 'forbidden'
        if min(i,j,h) == 0:
            a,b,c = sorted((i,j,h))
            assert b == c
            return P[b], 'repeated'
        return A[i]*A[j]*A[h], 'product'

    scalar_entries = {(r['i'],r['j']):r for r in scalar['entries']}
    old_orbits = {tuple(o) for r in old['orbits'] for o in r['closure']}
    rows, violations = [], []
    counts = {'all_actual_ordered_orbits':0, 'selected_orbits':0,
              'forbidden':0, 'repeated':0, 'product':0,
              'zero_length_orbits':0, 'zero_pair_orbits':0,
              'old_closure_overlaps':0, 'scalar_overlaps':0,
              'strict_positive_slacks':0, 'zero_slacks':0, 'negative_slacks':0}
    weight_counts = [0]*11
    minimum = None
    minimum_row = None
    for i in range(69):
        for j in range(69):
            for t in range(max(0,i+j-W),min(i,j)+1):
                for s in range(max(0,i+j-V),min(i,j)+1):
                    counts['all_actual_ordered_orbits'] += 1
                    lengths = (i,W-i,i,V-i)
                    weights = (t,j-t,s,j-s)
                    complemented = tuple(min(b,n-b) for b,n in zip(weights,lengths))
                    total = sum(complemented)
                    if total > CAP:
                        continue
                    h = i+j-t-s
                    rid = bound(tuple(zip(weights,lengths)))
                    R = states[rid]['R']
                    D = comb(i,t)*comb(W-i,j-t)*comb(i,s)*comb(V-i,j-s)
                    assert D > 0
                    Y, branch = numerator(i,j,h)
                    slack = R*P[i]-D*Y
                    original = [i,j,t,s]
                    row = {'orbit':original, 'h':h, 't_minus_s':t-s,
                           'block_lengths':list(lengths), 'block_weights':list(weights),
                           'complemented_weights':list(complemented),
                           'residual_weight':total, 'recursion':rid, 'R':R, 'D':D,
                           'assignment_branch':branch, 'y_numerator':Y,
                           'slack_numerator':slack}
                    rows.append(row)
                    if minimum is None or slack < minimum:
                        minimum, minimum_row = slack, original
                    if slack < 0:
                        violations.append(len(rows)-1)
                    sign = 'negative_slacks' if slack < 0 else 'zero_slacks' if slack == 0 else 'strict_positive_slacks'
                    counts[sign] += 1
                    counts['selected_orbits'] += 1
                    counts[branch] += 1
                    counts['zero_length_orbits'] += (0 in lengths)
                    counts['zero_pair_orbits'] += (p[i] == 0)
                    counts['old_closure_overlaps'] += (tuple(original) in old_orbits)
                    weight_counts[total] += 1
                    sr = scalar_entries[i,j]
                    rec = scalar['evaluation_records'][sr['h_ids'][h-sr['h_min']]]
                    assert F(Y,H) == F(rec['y'],scalar['scalar_denominator'])
                    counts['scalar_overlaps'] += 1
        if i%16 == 0 or i == 68:
            print('Four-block construction through i =',i,
                  '; selected =',len(rows),'; recursion states =',len(states),flush=True)
    objective = sum(comb(W,i)*comb(V,i)*p[i] for i in range(69))
    threshold = F(65537**28,2**128)
    result = {'stage':'completed', 'parameters':{'n':1024,'w':W,'v':V,'d':10,'residual_cap':CAP},
              'scope':'fixed recursive upper coefficients; selected original ordered orbits only',
              'p':list(map(enc,p)), 'common_denominator':H,
              'pair_scaled_numerators':P, 'recursion_states':states, 'rows':rows,
              'counts':counts, 'residual_weight_counts':weight_counts,
              'minimum':{'slack':enc(F(minimum,H)),'orbit':minimum_row},
              'violating_row_indices':violations, 'failures':[],
              'selected_family_passes':not violations,
              'objective':enc(objective),'required_threshold':enc(threshold)}
    OUT.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print('Counts:',counts,'; weight counts:',weight_counts)
    print('Exact minimum slack:',F(minimum,H),'; orbit:',minimum_row)
    print('Violations:',len(violations),'; failures: []; full certificate:',OUT)
    print('Actual objective:',objective,'; required <=',threshold)


if __name__ == '__main__':
    main()
