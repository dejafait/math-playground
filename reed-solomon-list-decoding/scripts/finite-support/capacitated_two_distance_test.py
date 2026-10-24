"""One full original-orbit pass and exact two-weight box support test.

No optimization solver, source-variable quotient or stopped solve is used.
The certificate losslessly factors every original coefficient and capacity.
"""
import hashlib
import itertools
import json
import resource
import sys
import time
from fractions import Fraction as Q
from math import comb, factorial, lcm
from pathlib import Path

sys.set_int_max_str_digits(0)
B = Path(__file__).parent
ROOT = B.parent.parent
OUT = B / 'capacitated-two-distance-results.json'
START = time.monotonic()
PERMS = list(itertools.permutations(range(3)))
CAPS = dict(original_entries=1500625, presentation_visits=9003750,
            seconds=900, output_bytes=64*2**20, live_bytes=2**30)


def enc(x):
    x = Q(x)
    return [x.numerator, x.denominator]


def main():
    state = dict(stage='in_progress', caps=CAPS, failures=[])
    OUT.write_text(json.dumps(state)+'\n')
    try:
        run(state)
    except Exception as exc:
        state.update(stage='obstruction', failures=[repr(exc)],
                     elapsed_seconds=time.monotonic()-START)
        OUT.write_text(json.dumps(state, separators=(',', ':'))+'\n')
        print('INCONCLUSIVE:', repr(exc), '; saved:', OUT, flush=True)
        raise


def run(state):
    paths = ['scripts/finite-support/delsarte-lp-results.json',
             'lemmas/L021-basic-delsarte-support-lp-optimum.md',
             'lemmas/L098-exact-cardinality-normalized-control-obstruction.md',
             'lemmas/L105-fixed-pair-independent-row-capacity-nonexclusion.md',
             'lemmas/L107-global-weighted-triangle-deficit-obstruction.md',
             'lemmas/L108-equilateral-triangles-stop-uncapacitated-distance-dual.md',
             'foundations/04-constant-weight-triple-sdp-source.md',
             'foundations/12-global-degree-three-moment-source.md',
             'foundations/13-fixed-cardinality-marginal-source.md',
             'drafts/literature/2026-10-22-two-distance-capacitated-triangle-test.md']
    state['input_sha256'] = {
        p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    lp = json.loads((B/'delsarte-lp-results.json').read_text())
    H = comb(1024, 68)
    N = 65537**28//2**128+1
    U = Q(comb(1024, 64), comb(68, 64))
    alpha = 2*(N-1)/(U-1)
    g = [comb(68, i)*comb(956, i) for i in range(69)]
    a = [Q(r['numerator'], r['denominator']) for r in lp['exact']['primal']]
    c = [Q(1)]+[Q(0)]*4+[alpha*x/(2*g[i])
                                  for i, x in zip(range(5, 69), a)]
    q = lcm(*(x.denominator for x in c))
    P = [int(x*q) for x in c]
    assert N > 2 and 0 < alpha < 1 and len(c) == 69
    assert sum(a) == U-1 and all(x > 0 for x in a)
    assert P[0] == q and P[1:5] == [0]*4
    assert all(0 < P[i] < q for i in range(5, 69))
    assert sum(g) == H and sum(g[i]*P[i] for i in range(69)) == N*q
    assert all(H*g[i] % 2 == 0 for i in range(1, 69))
    assert sum(H*g[i]//2 for i in range(1, 69)) == comb(H, 2)
    state.update(H=H, N=N, U=enc(U), alpha=enc(alpha), denominator=q,
                 pair_numerators=P, shell_sizes=g,
                 edge_demands=[None]+[enc((N-2)*x) for x in c[1:]])

    # Precompute each source multinomial by factorials, separately from D.
    facts = [factorial(k) for k in range(1025)]
    tables = {}
    entries = []
    for i in range(69):
        for j in range(69):
            ts = list(range(max(0, i+j-68), min(i, j)+1))
            ss = list(range(max(0, i+j-956), min(i, j)+1))
            A = {t: facts[68]//(facts[t]*facts[i-t]*facts[j-t]*facts[68-i-j+t])
                 for t in ts}
            B0 = {s: facts[956]//(facts[s]*facts[i-s]*facts[j-s]*facts[956-i-j+s])
                  for s in ss}
            da = {t: comb(i, t)*comb(68-i, j-t) for t in ts}
            db = {s: comb(i, s)*comb(956-i, j-s) for s in ss}
            assert all(A[t]*B0[s] == g[i]*da[t]*db[s]
                       for t, s in [(ts[0], ss[0]), (ts[-1], ss[-1])])
            tables[i, j] = (A, B0, da, db)
    buckets = {(m, k): [0, 0, 0] for m in range(4) for k in range(4-m)}
    # Each bucket: number of source entries, sum G, sum G*min(P).
    rows = []
    visits = [0]*6
    count = repeats = forbidden = distinct_entries = 0
    distinct_total = 0
    for i in range(69):
        full_sum = distinct_sum = 0
        rep = []
        for j in range(69):
            A, B0, da, db = tables[i, j]
            hs = {}
            for t in A:
                for s in B0:
                    h = i+j-t-s
                    atoms = (956-i-j+s, t, i-s, j-t,
                             j-s, i-t, s, 68-i-j+t)
                    assert min(atoms) >= 0 and sum(atoms) == 1024
                    assert sum(atoms[k] for k in (1, 3, 5, 7)) == 68
                    assert sum(atoms[k] for k in (2, 3, 6, 7)) == 68
                    assert sum(atoms[k] for k in (4, 5, 6, 7)) == 68
                    ds = ((0, i, j), (i, 0, h), (j, h, 0))
                    G = A[t]*B0[s]
                    D = da[t]*db[s]
                    assert G == g[i]*D  # every original entry, not samples
                    cap = min(P[i], P[j], P[h])
                    m, k = (i, j, h).count(5), (i, j, h).count(6)
                    distinct = min(i, j, h) > 0
                    # Derive each presentation from the actual eight atoms.
                    # t' is the anchor-only atom; s' is the other-pair-only atom.
                    for num, (aa, bb, cc) in enumerate(PERMS):
                        ip, jp = ds[aa][bb], ds[aa][cc]
                        tp, sp = atoms[1 << aa], atoms[(1 << bb) | (1 << cc)]
                        ap, bp, _, _ = tables[ip, jp]
                        assert tp in ap and sp in bp
                        assert tp-sp == t-s
                        assert ip+jp-tp-sp == ds[bb][cc]
                        assert ap[tp]*bp[sp] == G
                        assert min(P[ip], P[jp], P[ds[bb][cc]]) == cap
                        assert min(ip, jp, ds[bb][cc]) > 0 or not distinct
                        visits[num] += 1
                    rec = hs.setdefault(h, [0, 0])
                    rec[0] += 1
                    rec[1] += G
                    full_sum += G
                    count += 1
                    if any(0 < b < 5 for b in (i, j, h)):
                        forbidden += 1
                        assert cap == 0
                    if distinct:
                        distinct_entries += 1
                        distinct_sum += G
                        bucket = buckets[m, k]
                        bucket[0] += 1
                        bucket[1] += G
                        bucket[2] += G*cap
                    else:
                        repeats += 1
                        assert D == (g[j] if i == 0 else 1)
                        assert sorted((i, j, h))[1] == sorted((i, j, h))[2]
                        if i > 0:
                            rep.append([j, t, s, D])
            assert sum(x[1] for x in hs.values()) == g[i]*g[j]
            entries.append(dict(i=i, j=j, t=list(A), s=list(B0),
                source_inside=list(A.values()), source_outside=list(B0.values()),
                D_inside=list(da.values()), D_outside=list(db.values()),
                # h, original entries, sum G, capacity numerator, m5,m6,distinct
                h_records=[[h, z[0], z[1], min(P[i], P[j], P[h]),
                            (i,j,h).count(5), (i,j,h).count(6), min(i,j,h)>0]
                           for h, z in sorted(hs.items())]))
        assert full_sum == g[i]*H
        assert distinct_sum == (g[i]*(H-2) if i else 0)
        assert i == 0 or rep == [[0, 0, 0, 1], [i, i, i, 1]]
        distinct_total += distinct_sum
        rows.append(dict(i=i, full_source_sum=full_sum,
                         distinct_source_sum=distinct_sum, repetitions=rep))
        assert time.monotonic()-START < CAPS['seconds']
        print('Original rows checked:', i+1, '/69; entries:', count,
              flush=True) if i % 12 == 0 else None
    assert count == CAPS['original_entries']
    assert sum(visits) == CAPS['presentation_visits']
    assert repeats == 205 and forbidden == 10232
    assert distinct_total == (H-1)*(H-2)
    assert sum(b[1] for b in buckets.values()) == distinct_total
    assert H*distinct_total//6 == comb(H, 3)
    assert all(H*b[1] % 6 == 0 for b in buckets.values())

    # All actual nonzero-capacity break lines, canonically normalized.
    actual_lines = set()
    for (m, k), (_, _, K) in buckets.items():
        if K and (m or k):
            common = __import__('math').gcd(m, k)
            actual_lines.add((m//common, k//common))
    cover_lines = {(1,0), (0,1), (1,1), (2,1), (1,2)}
    assert actual_lines <= cover_lines
    # Include axes to split the diamond's four straight sides, even if
    # an axis is not a break line of any surviving contribution.
    candidates = {(1,0), (-1,0), (0,1), (0,-1)}
    for m, k in cover_lines:
        candidates.update({(k,-m), (-k,m)})
    assert len(candidates) == 10
    # Exact cyclic order on the diamond; no floating-point polar sorting.
    cyclic = [(1,0),(0,1),(-1,2),(-1,1),(-2,1),
              (-1,0),(0,-1),(1,-2),(1,-1),(2,-1)]
    assert set(cyclic) == candidates
    normalized = [tuple(Q(z,abs(x)+abs(y)) for z in (x,y)) for x,y in cyclic]
    pieces = []
    for pos, (left, right) in enumerate(zip(normalized, normalized[1:]+normalized[:1])):
        assert any(left[a] == right[a] == 0 or left[a]*right[a] >= 0 for a in (0,1))
        # Both endpoints lie on the same closed diamond side.
        assert all(left[a]*right[a] >= 0 for a in (0,1))
        signs = []
        for m, k in sorted(cover_lines):
            lv, rv = m*left[0]+k*left[1], m*right[0]+k*right[1]
            assert lv*rv >= 0  # no zero crossing inside this closed segment
            signs.append([m,k,(lv>0)-(lv<0),(rv>0)-(rv<0)])
        pieces.append(dict(left=pos, right=(pos+1)%10, line_endpoint_signs=signs))
    demand = (3*(N-2)*g[5]*P[5], 3*(N-2)*g[6]*P[6])
    evaluations = []
    for (x,y), (xx,yy) in zip(cyclic, normalized):
        support = sum(K*max(m*x+k*y,0) for (m,k),(_,_,K) in buckets.items())
        required = demand[0]*x+demand[1]*y
        margin = Q(support-required, abs(x)+abs(y))
        evaluations.append(dict(direction=[x,y], normalized=[enc(xx),enc(yy)],
            box_support_numerator=support, demand_pairing_numerator=required,
            normalized_scaled_margin=enc(margin),
            margin_over_positive_scale=enc(margin/sum(demand)),
            separates=margin<0))
    minimum = min(Q(*r['normalized_scaled_margin']) for r in evaluations)
    verdict = 'STRICT_SEPARATOR' if minimum < 0 else 'NO_TWO_DISTANCE_SEPARATOR'
    positive_scale = sum(demand)
    ratio = minimum/positive_scale
    state.update(stage='complete', coefficient_entries=entries, rows=rows,
        original_entries=count, presentation_visits=visits, repeated_entries=repeats,
        forbidden_entries=forbidden, distinct_entries=distinct_entries,
        distinct_source_total=distinct_total,
        buckets=[dict(m5=m,m6=k,source_entries=b[0],source_sum=b[1],
                      capacity_weighted_source_sum=b[2],unordered_triangles=H*b[1]//6)
                 for (m,k),b in sorted(buckets.items())],
        actual_break_lines=sorted(actual_lines), covering_break_lines=sorted(cover_lines),
        pieces=pieces, demand_coefficients=list(demand), evaluations=evaluations,
        verdict=verdict, minimum_normalized_scaled_margin=enc(minimum),
        minimum_over_positive_scale=enc(ratio), positive_scale=positive_scale,
        zero_vector_margin=0, all_nonzero_strictly_positive=minimum>0,
        elapsed_seconds=time.monotonic()-START,
        peak_live_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    assert state['peak_live_bytes'] < CAPS['live_bytes']
    OUT.write_text(json.dumps(state,separators=(',',':'))+'\n')
    assert OUT.stat().st_size < CAPS['output_bytes']
    lo = ratio.numerator*10**6//ratio.denominator
    print('Verdict:', verdict, '; exact candidates:', len(evaluations))
    print('Minimum / positive scale in [', lo, ',',lo+1, ')/10^6; required >= 0')
    print('Actual/required original entries:', count, '/', CAPS['original_entries'],
          '; presentations:', sum(visits), '/', CAPS['presentation_visits'])
    print('Failures:', state['failures'], '; certificate:', OUT)


if __name__ == '__main__':
    main()
