"""Fixed AVZ Proposition 17 diagnostic; no coefficient or shell tuning."""
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path

BASE = Path(__file__).parent
OUT = BASE / 'conditional-shell-results.json'


def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]


def normalize(blocks):
    answer = []
    for weight, length in blocks:
        if not 0 <= weight <= length:
            raise ValueError((weight, length))
        u = min(weight, length-weight)
        if u:
            answer.append((u, length))
    return tuple(answer)


def main():
    lp = json.loads((BASE/'delsarte-lp-results.json').read_text())
    old = json.loads((BASE/'selected-triple-sdp-results.json').read_text())
    x = [F(r['numerator'], r['denominator']) for r in lp['exact']['primal']]
    states, memo = [], {}

    def bound(d, blocks):
        key = (d, normalize(blocks))
        if key in memo:
            return memo[key]
        d, blocks = key
        total = sum(u for u, n in blocks)
        branches = []
        if total < d//2:
            result, kind = 1, 'below-distance'
        elif total == d//2:
            result, kind = min(n//u for u, n in blocks), 'disjoint-supports'
        else:
            kind = 'shorten'
            for a, (u, n) in enumerate(blocks):
                child = list(blocks)
                child[a] = (u-1, n-1)
                assert sum(z for z, k in normalize(child)) == total-1
                cid = bound(d, child)
                candidate = n*states[cid]['R']//u
                branches.append({'block': a, 'child': cid, 'candidate': candidate})
            result = min(b['candidate'] for b in branches)
        index = len(states)
        states.append({'d': d, 'blocks': list(map(list, blocks)),
                       'S': total, 'kind': kind, 'R': result, 'branches': branches})
        memo[key] = index
        return index

    pairs = []
    for a in (67, 68):
        p = x[a-5]/(2*comb(68, a)*comb(956, a))
        assert p == F(*old['p'][a])
        occupancy = comb(68, a)*comb(956, a)*p
        assert occupancy == x[a-5]/2
        blocks = [[a, 68], [a, 956]]
        sid = bound(10, blocks)
        pairs.append({'a': a, 'blocks': blocks, 'normalized': list(map(list, normalize(blocks))),
                      'state': sid, 'p': enc(p), 'B': enc(occupancy), 'P': states[sid]['R']})

    partitions = []
    for data in ((63, 68, 4, 888, 8), (63, 67, 5, 889, 10)):
        w1, n1, w2, n2, d = data
        rows = []
        for a in range(64):
            blocks = [[a, n1], [w1+w2-a, n2]]
            sid = bound(d, blocks)
            rows.append({'head': a, 'blocks': blocks,
                         'normalized': list(map(list, normalize(blocks))),
                         'state': sid, 'R': states[sid]['R']})
        partitions.append({'input': list(data), 'summands': rows,
                           'sum': sum(r['R'] for r in rows)})
    Pi, Pj = [r['P'] for r in pairs]
    Pij, Pji = min(Pi, partitions[0]['sum']), min(Pj, partitions[1]['sum'])
    assert Pi > 0 and Pj > 0 and 0 <= Pij <= Pi and 0 <= Pji <= Pj
    Bi, Bj = [F(*r['B']) for r in pairs]
    sign = Pij*Pj + Pji*Pi - Pi*Pj
    definitions = ([(62, Pji, Pi-Pij, Pi*Pji), (63, Pj-Pji, Pij, Pj*Pij)]
                   if sign > 0 else [(64, Pj, Pi, Pi*Pj)])
    rows = []
    for eq, ci, cj, rhs in definitions:
        lhs = ci*Bi+cj*Bj
        rows.append({'equation': eq, 'coefficients': [ci, cj], 'rhs': rhs,
                     'lhs': enc(lhs), 'slack': enc(rhs-lhs)})
    individual = [{'a': r['a'], 'slack': enc(r['P']-F(*r['B']))} for r in pairs]
    U = F(comb(1024,64), comb(68,64))
    objective, threshold = (U+1)/2, F(65537**28,2**128)
    failures = []
    violations = [r['equation'] for r in rows if F(*r['slack']) < 0]
    result = {'parameters': {'n':1024, 'w':68, 'v':956, 'd':10, 'delta':5,
                             'Delta':63, 'i':67, 'j':68},
              'pairs': pairs, 'partitions': partitions, 'recursion_states': states,
              'coefficients': {'Pi':Pi, 'Pj':Pj, 'Pij':Pij, 'Pji':Pji},
              'branch_sign': sign, 'ratio': enc(F(Pij,Pi)+F(Pji,Pj)),
              'rows': rows, 'individual_caps': individual,
              'objective': enc(objective), 'threshold': enc(threshold),
              'objective_ratio': enc(objective/threshold),
              'summary': {'state_count':len(states),
                          'branch_count':sum(len(r['branches']) for r in states),
                          'conditional_equals_individual':Pij==Pi and Pji==Pj,
                          'violated_rows':violations, 'failures':failures}}
    OUT.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print('Coefficients:', result['coefficients'])
    print('Ratio:', F(*result['ratio']), '; branch sign:', sign)
    for r in rows:
        print('Row',r['equation'],'actual slack',F(*r['slack']),'; required >= 0')
    for r in individual:
        print('Individual',r['a'],'slack',F(*r['slack']),'; required >= 0')
    print('Objective/threshold:', objective/threshold, '; required <= 1')
    print('Summary:', result['summary'])
    print('Certificate:', OUT)


if __name__ == '__main__':
    main()
