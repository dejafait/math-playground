"""Complete independent coefficient/orbit replay of the fixed-H pair test.

No producer imports. Enumerate all raw singleton partitions, normalize by
their six roots, and test quartic-net membership by five coefficients.
Save a rejecting coefficient or the full zero vector on every support.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json

PCHAR = 97
NODES = tuple(t for t in range(1,97) if pow(t,16,97)==1)


def product(values):
    ans = 1
    for v in values:
        ans = ans*v % PCHAR
    return ans


def polynomial(roots):
    p = [1]
    for x in roots:
        out = [0]*(len(p)+1)
        for j,c in enumerate(p):
            out[j] = (out[j]-x*c) % PCHAR
            out[j+1] = (out[j+1]+c) % PCHAR
        p = out
    return p


def times(a,b):
    out = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] = (out[i+j]+x*y) % PCHAR
    return out


def value(poly,t):
    ans = 0
    for c in reversed(poly):
        ans = (ans*t+c) % PCHAR
    return ans


def rank(mat):
    rows = [list(row) for row in mat]
    r = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(r,len(rows)) if rows[i][col]),None)
        if pivot is None:
            continue
        rows[pivot],rows[r] = rows[r],rows[pivot]
        scale = pow(rows[r][col],-1,PCHAR)
        rows[r] = [v*scale % PCHAR for v in rows[r]]
        for i in range(len(rows)):
            if i!=r:
                scale = rows[i][col]
                rows[i] = [(v-scale*w) % PCHAR for v,w in zip(rows[i],rows[r])]
        r += 1
    return r


def partitions(s):
    # A separate explicit six-root matching generator: choose the partner
    # of root zero, then the partner of the least remaining root.
    for i in range(1,6):
        tail = [s[j] for j in range(1,6) if j!=i]
        for j in range(1,4):
            last = [tail[k] for k in range(1,4) if k!=j]
            yield tuple(sorted(((s[0],s[i]),(tail[0],tail[j]),tuple(last))))


def normalize(pairs):
    roots = sum(pairs,())
    return min(tuple(sorted(tuple(sorted(x*pow(t,-1,97) % 97 for x in pair))
                            for pair in pairs)) for t in roots)


def main():
    here = Path(__file__).parent
    source = json.loads((here/'independent-net-pair.json').read_text())
    orbit_sizes = Counter()
    raw_count = 0
    for six in combinations(NODES,6):
        for pairs in partitions(six):
            raw_count += 1
            orbit_sizes[normalize(pairs)] += 1
    assert raw_count == 120120
    source_rows = {tuple(map(tuple,row['pairs'])):row for row in source['coverage']}
    assert len(source_rows)==len(source['coverage'])
    assert set(source_rows)==set(orbit_sizes), 'complete representative case-set mismatch'
    assert tuple(source['H'])==NODES
    quartics = {K:polynomial(K) for K in combinations(NODES,4)}
    replay, independent, support_tests, retained = [],0,0,0
    union_hist, candidate_hist = Counter(),Counter()
    coefficient_reject_hist = Counter()
    for pairs in sorted(orbit_sizes):
        row = source_rows[pairs]
        quadratics = [polynomial(pair) for pair in pairs]
        is_independent = rank(quadratics)==3
        assert is_independent==(row['quadratic_det']!=0)
        rec = {'pairs':pairs,'raw_orbit_size':orbit_sizes[pairs],
               'quadratic_rank':3 if is_independent else 2,
               'support_coefficient_checks':[],'surviving_supports':[],'pair_unions':[]}
        if not is_independent:
            assert not row['projected_residuals']
            replay.append(rec)
            continue
        independent += 1
        six = sum(pairs,())
        remaining = tuple(x for x in NODES if x not in six)
        net = [times(quadratics[1],quadratics[2]),
               times(quadratics[0],quadratics[2]),times(quadratics[0],quadratics[1])]
        pivots = [pair[0] for pair in pairs]
        denominators = [pow(value(f,x),-1,97) for f,x in zip(net,pivots)]
        barycentric = {x:pow(product(x-y for y in six if y!=x),-1,97) for x in six}
        assert len(row['projected_residuals'])==210
        for index,K in enumerate(combinations(remaining,4)):
            f = quartics[K]
            coeff = [value(f,x)*d % 97 for x,d in zip(pivots,denominators)]
            residual = [(f[j]-sum(c*n[j] for c,n in zip(coeff,net))) % 97
                        for j in range(5)]
            membership = not any(residual)
            sums = [sum(value(f,x)*barycentric[x] for x in pair) % 97 for pair in pairs]
            assert sums==row['projected_residuals'][index], (pairs,K,'row evidence')
            assert membership==(not any(sums)), (pairs,K,'coefficient/evaluation disagreement')
            # Save all coefficients and full residuals, not just a preview.
            # K is the indexed lexicographic four-subset of remaining.
            rec['support_coefficient_checks'].append([coeff,residual])
            support_tests += 1
            if membership:
                retained += 1
                rec['surviving_supports'].append(K)
            else:
                coefficient_reject_hist[next(j for j,v in enumerate(residual) if v)] += 1
        candidate_hist[len(rec['surviving_supports'])] += 1
        for K,L in combinations(rec['surviving_supports'],2):
            size = len(set(K+L))
            union_hist[size] += 1
            rec['pair_unions'].append({'K':K,'L':L,'union_size':size})
        replay.append(rec)
    projected = {tuple(map(tuple,row['pairs'])):tuple(map(tuple,row['candidates']))
                 for row in source['projected_records']}
    assert projected=={tuple(map(tuple,row['pairs'])):tuple(row['surviving_supports'])
                       for row in replay if row['surviving_supports']}
    required_tests = independent*210
    assert support_tests==required_tests
    forbidden = sum(count for size,count in union_hist.items() if size<=7)
    assert forbidden==0
    assert source['counts']['support_pairs']==0
    assert source['witness'] is None
    summary = {'raw_partitions_actual':raw_count,'raw_partitions_required':120120,
               'representatives_actual':len(replay),'representatives_required':len(source_rows),
               'orbit_size_histogram':dict(Counter(orbit_sizes.values())),
               'independent_representatives':independent,
               'support_tests_actual':support_tests,'support_tests_required':required_tests,
               'retained_support_occurrences':retained,'candidate_histogram':dict(candidate_hist),
               'pair_union_size_histogram':dict(union_hist),
               'forbidden_union_at_most_seven_actual':forbidden,
               'forbidden_union_at_most_seven_required':0,
               'first_nonzero_coefficient_histogram':dict(coefficient_reject_hist),
               'failures_actual':0,'failures_required':0}
    out = {'scope':'Complete fixed-H independent-net projected pair obstruction; no full-M bound',
           'support_row_encoding':'Lexicographic K in H minus the six singleton labels; each row is [net coefficients, five coefficient residuals]',
           'summary':summary,'coverage_replay':replay,'failures':[]}
    path = here/'independent-net-pair-verification.json'
    path.write_text(json.dumps(out,separators=(',',':'))+'\n')
    print(json.dumps(summary,sort_keys=True))
    print('Full replay certificate:',path)


if __name__=='__main__':
    main()
