"""L067 audit: independent packed-row aggregation and original-chart witness.

The complete mathematical row replay is performed by the audited C++ replay.
This checker uses itertools and tuple/set keys instead of its nested index,
bit-mask and packed-weight/bitset utilities. It reads every certificate byte.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).parent
F = 97


def run():
    H = tuple(x for x in range(1, F) if pow(x, 16, F) == 1)
    assert H == (1, 8, 12, 18, 22, 27, 33, 47, 50, 64, 70, 75, 79, 85, 89, 96)
    pairs = tuple(sorted({tuple(sorted((x, -x % F))) for x in H}))
    assert len(pairs) == 8 and pairs[0] == (1, 96)
    all_supports = tuple(combinations(H, 4))
    assert len(set(all_supports)) == 1820
    # C++ support mask intersection agrees with independent tuple deletion.
    support_masks = [sum(1 << H.index(x) for x in K) for K in all_supports]
    support_coverage = {}
    for P in combinations(H, 3):
        pmask = sum(1 << H.index(x) for x in P)
        expected = tuple(combinations(tuple(x for x in H if x not in P), 4))
        actual = tuple(K for K, mask in zip(all_supports, support_masks) if not mask & pmask)
        assert actual == expected and len(expected) == 715
        support_coverage[P] = len(expected)
    producer = json.loads((ROOT / 'antipodal-anchor-sweep.json').read_text())
    old_replay = json.loads((ROOT / 'antipodal-anchor-verification.json').read_text())
    replay = json.loads((ROOT / 'antipodal-anchor-audit-replay.json').read_text())
    assert replay == old_replay
    for key in producer:
        if key not in ('mode', 'all_eight_moment_tests', 'zero_fourth_weight_rows_retained'):
            assert producer[key] == replay[key], key
    maxima, histogram, kinds = [], Counter(), Counter()
    assignments, pair_choices, digest = [], [], hashlib.sha256()
    packed = ROOT / 'antipodal-anchor-rows.bin'
    with packed.open('rb') as handle:
        for Z, W in permutations(pairs[1:], 2):
            S = pairs[0] + Z + W
            pair_choices.append((Z, W))
            outside = tuple(x for x in H if x not in S)
            for P in permutations(outside, 3):
                assignments.append((Z, W, P))
                n = support_coverage[tuple(sorted(P))]
                block = handle.read(5*n)
                assert len(block) == 5*n
                digest.update(block)
                fibers = defaultdict(set)
                for offset in range(0, len(block), 5):
                    kind, mu, p, q, r = block[offset:offset+5]
                    kinds[kind] += 1
                    assert kind in range(5)
                    if kind in (0, 1):
                        assert (mu,p,q,r) == (0,0,0,0)
                    elif kind == 2:
                        assert (mu,p,q,r) == (96,0,0,0)
                    else:
                        assert 1 <= mu <= 95 and all(0 <= x < F for x in (p,q,r))
                        gated = all(x not in (0,1) for x in (p,q,r))
                        assert gated == (kind == 4)
                        if gated:
                            fibers[(p,q,r)].add(mu)
                local = max(map(len, fibers.values()), default=0)
                maxima.append(local)
                histogram.update(map(len, fibers.values()))
        assert handle.read(1) == b''
    assert len(pair_choices) == len(set(pair_choices)) == 42
    assert len(assignments) == len(set(assignments)) == 30240
    assert sum(kinds.values()) == 21621600
    assert maxima == replay['maximum_by_assignment']
    assert [kinds[i] for i in range(5)] == replay['row_counts']
    assert {str(k):v for k,v in histogram.items()} == replay['fiber_histogram']
    assert max(maxima) == replay['maximum_isolated_disjoint_P'] == 3
    assert digest.hexdigest() == 'bf33edaa08cd2cafa51605f5b2f08e1ed70f9f7dafec11ed188f896bb6242e3c'
    assert packed.stat().st_size == 108108000
    assert replay['all_eight_moment_tests'] == kinds[4] == 15367752
    assert replay['zero_fourth_weight_rows_retained'] == 3568320
    assert replay['failures'] == [] and replay['actual_failures'] == 0

    # Build actual base errors from L057 (2), independently of numerator N.
    P, Y, Z, W = (27,79,22), (1,96), (8,89), (12,85)
    p,q,r = 58,3,35
    U = set(P+Y+Z+W)
    cx = {x:1 for x in U}
    for x in U:
        for h in H:
            if h not in U:
                cx[x] = cx[x]*(x-h) % F
    a,b,c = P
    normalized = ({a:p,b:q,**{x:1 for x in Y}},
                  {a:1-p,c:r,**{x:1 for x in Z}},
                  {b:1-q,c:1-r,**{x:1 for x in W}})
    alpha = (-1,2,-1)  # Original gamma=(0,1,2), lambda=1.
    base = [{x:cx[x]*t*pow(ai,-1,F)%F for x,t in e.items()}
            for e,ai in zip(normalized,alpha)]
    def moments(e):
        return [sum(v*pow(x,j,F) for x,v in e.items())%F for j in range(1,9)]
    base_moments = list(map(moments,base))
    affine2 = [(2*y-x)%F for x,y in zip(*base_moments[:2])]
    assert base_moments[2] == affine2
    assert all(len(e)==4 and all(e.values()) for e in base)
    specified = [((12,33,47,89),36,(55,94,44,12),46),
                 ((12,47,75,96),87,(53,23,18,96),24),
                 ((33,75,89,96),32,(31,10,70,21),40)]
    witness = []
    for K,mu,omega,T in specified:
        E = (2+mu)%F
        assert E and 2*pow(E,-1,F)%F == T and T not in (0,1,2)
        actual = {x:w*pow(E,-1,F)%F for x,w in zip(K,omega)}
        residual = [(v-(1-T)*v0-T*v1)%F
                    for v,v0,v1 in zip(moments(actual),*base_moments[:2])]
        assert not any(residual) and all(actual.values())
        witness.append({'K':K,'mu':mu,'omega':omega,'E':E,'T':T,
                        'actual_weights':list(actual.values()),'original_moment_residual8':residual})
    result = {'scope':'L067 critical audit; antipodal pairs only',
              'H':H,'antipodal_pairs':pairs,'support_order_checks':len(support_coverage),
              'actual_pair_cases':42,'required_pair_cases':42,
              'actual_assignments':30240,'required_assignments':30240,
              'actual_rows':21621600,'required_rows':21621600,
              'row_counts':[kinds[i] for i in range(5)],
              'fiber_histogram':dict(histogram),'maximum_by_assignment':maxima,
              'maximum_isolated_disjoint_P':3,'required_four_anchor_threshold':4,
              'packed_sha256':digest.hexdigest(),'packed_bytes':packed.stat().st_size,
              'all_eight_moment_tests':replay['all_eight_moment_tests'],
              'zero_weight_rows_retained':replay['zero_fourth_weight_rows_retained'],
              'original_base_errors':base,'original_base_moments':base_moments,
              'base_third_parameter_residual8':[(x-y)%F for x,y in zip(base_moments[2],affine2)],
              'original_witness_rows':witness,'failures':[],'actual_failures':0,'required_failures':0}
    path = ROOT / 'antipodal-anchor-critical-audit.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('Complete replay agrees; independent aggregation: 21621600/21621600 rows, 30240/30240 assignments')
    print('Isolated maximum 3; required anchors 4; support-order checks 560/560; failures 0/0')
    print('Three original-chart witness errors pass all eight moments; full weights retained')
    print(f'Certificate: {path}')


if __name__ == '__main__':
    run()
