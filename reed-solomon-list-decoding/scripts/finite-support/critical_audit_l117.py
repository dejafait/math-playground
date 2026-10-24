"""Critical audit of the immutable L117 application, with preserved originals.

Replay the independent verifier and check its full evidence against the
manuscript. No constructor, solve, scan, retuning or refinement is run.
"""
from collections import Counter
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import permutations, product
import json
from math import comb, factorial
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B / 'l117-critical-audit.json'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(name):
    return json.loads((B / name).read_text())


def enc(x):
    return [x.numerator, x.denominator]


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def congruence(K, T):
    n = len(K)
    return [[sum(T[u][i]*K[u][v]*T[v][j]
                 for u in range(n) for v in range(n))
             for j in range(n)] for i in range(n)]


def main():
    counts = Counter()
    report = dict(stage='in_progress', failures=[], code_sha256=sha(Path(__file__)))

    def save():
        report.update(checks=sum(counts.values()), checks_by_kind=dict(counts))
        OUT.write_text(json.dumps(report, indent=2) + '\n')

    def ck(kind, ok, detail=None):
        counts[kind] += 1
        if not ok:
            report['failures'].append(dict(kind=kind, detail=detail))
            report['stage'] = 'failed'
            save()
            raise AssertionError((kind, detail))

    names = ['fixed-product-excluded.json', 'fixed-product-excluded-verification.json',
             'fixed_product_excluded.py', 'verify_fixed_product_excluded.py',
             'l112-l113-critical-audit.json', 'l114-critical-audit.json',
             'l115-critical-audit.json', 'positive-factor-enclosure.json.gz',
             'fixed-product-five-shell.json', 'fixed-product-coupled.json',
             'l116-critical-audit.json']
    report['input_sha256'] = {str((B/p).relative_to(ROOT)): sha(B/p) for p in names}
    save()
    spec = importlib.util.spec_from_file_location('l117_replay', B/'verify_fixed_product_excluded.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.OUT = B/'l117-critical-reverification.json'
    mod.main()
    replay = read('l117-critical-reverification.json')
    ck('complete_replay_equality', replay == read('fixed-product-excluded-verification.json'))
    source = read('fixed-product-excluded.json')
    c = [F(*v) for v in source['c']]
    g = [comb(68, i)*comb(956, i) for i in range(69)]
    ck('positive_homogeneous_normalization',
       source['N'] == 65537**28//2**128+1 and source['H'] == comb(1024,68) and
       F(*source['rho']) == F(source['N'],source['H']) > 0)

    # Every retained audit binding and the repaired string replay case.
    for name, code in [('l112-l113-critical-audit.json','critical_audit_l112_l113.py'),
                       ('l114-critical-audit.json','critical_audit_l114.py'),
                       ('l115-critical-audit.json','critical_audit_l115.py'),
                       ('l116-critical-audit.json','critical_audit_l116.py')]:
        audit = read(name)
        ck('retained_audit_status_code', audit['stage'] == 'verified' and
           not audit['failures'] and audit['code_sha256'] == sha(B/code), name)
        for p,h in audit['input_sha256'].items():
            ck('retained_audit_input', sha(ROOT/p) == h, p)
        replays = audit.get('replay_sha256', {})
        if isinstance(replays,str):
            ck('explicit_string_replay_schema', name == 'l115-critical-audit.json')
            replays = {'l115-critical-reverification.json': replays}
        for p,h in replays.items():
            ck('retained_audit_replay', sha(B/p) == h, p)

    box = {r['i']:tuple(F(*v) for v in r['interval']) for r in source['endpoints']}
    endpoint_types = Counter()
    null_types = Counter()
    dictionary = replay['dictionary']
    ck('complete_relation_order',
       [(r['layers'],r['intersections']) for r in dictionary] ==
       [([l,m],[t,s]) for l,m in [(5,5),(5,6),(6,6)]
        for t,s in product(range(min(l,m)+1),repeat=2)])
    for row in dictionary:
        l,m = row['layers']; t,s = row['intersections']
        # Full atom counts derived separately by splitting A and its complement.
        atoms = [956-l-m+s,t,l-s,m-t,m-s,l-t,s,68-l-m+t]
        ck('manuscript_complete_atoms', row['atoms'] == atoms and min(atoms) >= 0,
           [l,m,t,s])
        ck('six_distinct_orders', sorted(p['order'] for p in row['presentations']) ==
           [list(p) for p in permutations(range(3))], [l,m,t,s])
        for p in row['presentations']:
            # Transform all eight atoms, then derive each orbit without sets.
            permuted = [0]*8
            for mask, size in enumerate(atoms):
                newmask = sum(1<<j for j,old in enumerate(p['order']) if mask & (1<<old))
                permuted[newmask] = size
            i,j,tt,ss = permuted[1]+permuted[5],permuted[1]+permuted[3],permuted[1],permuted[6]
            h = permuted[2]+permuted[3]
            D = choose(i,tt)*choose(68-i,j-tt)*choose(i,ss)*choose(956-i,j-ss)
            head = factorial(68)//(factorial(i-tt)*factorial(j-tt)*factorial(tt)*factorial(68-i-j+tt))
            tail = factorial(956)//(factorial(i-ss)*factorial(j-ss)*factorial(ss)*factorial(956-i-j+ss))
            ck('complete_atom_presentation', p['orbit'] == [i,j,tt,ss] and p['h'] == h and
               h == i+j-tt-ss and tt-ss == t-s and
               p['D'] == D > 0 and p['full_count'] == head*tail == g[i]*D == g[l]*row['D'],
               [l,m,t,s,p['order']])
            if min(i,j,h) == 0:
                kind = 'coincident' if i == 0 else 'first' if j == 0 else 'second'
                endpoint_types[kind] += 1
                y = (c[max(i,j,h)],)*2
                ck('Boolean_value_and_D', D == (g[j] if i == 0 else 1),
                   [l,m,t,s,p['order']])
            elif min(i,j,h) < 5:
                y = (F(0),)*2
                null_types['opposite_forbidden' if h < 5 else 'anchored_forbidden'] += 1
                ck('null_value_capacity', min(c[i],c[j],c[h]) == 0, [l,m,t,s,p['order']])
            else:
                y = tuple(box[i][e]*box[j][e]*box[h][e] for e in (0,1))
            affine = (c[h]-y[1],c[h]-y[0])
            ck('each_own_opposite_pair_and_affine', p['pair'] == enc(c[h]) and
               p['y_interval'] == [enc(v) for v in y] == row['y_interval'] and
               p['affine_interval'] == [enc(v) for v in affine] and affine[0] >= 0,
               [l,m,t,s,p['order']])
            if h == 0:
                ck('Boolean_diagonal_one_minus_pair', affine == (1-c[i],)*2,
                   [l,m,t,s,p['order']])
            if 0 < h < 5:
                ck('opposite_forbidden_affine_zero', affine == (F(0),)*2,
                   [l,m,t,s,p['order']])
        ck('unpermuted_affine_entry', row['h'] == l+m-t-s and
           row['interval'] == row['presentations'][0]['affine_interval'], [l,m,t,s])
    ck('all_repetitions', endpoint_types == replay['repetitions'] ==
       dict(first=4,second=4,coincident=4))

    # Consume the complete signed-action evidence, including zero terms.
    action_map = {}
    expected_keys = [(n,l,m,k) for n in (68,956)
                     for l,m in [(5,5),(5,6),(6,5),(6,6)]
                     for k in range(min(l,m)+1)]
    ck('all_signed_action_records', [(r['n'],r['l'],r['m'],r['k'])
       for r in replay['signed_actions']] == expected_keys)
    for row in replay['signed_actions']:
        n,l,m,k = row['n'],row['l'],row['m'],row['k']
        D = choose(n-2*k,l-k)
        expected_terms = [dict(negative_choices=z,ordinary_intersection=b,t=k-z+b,
                              signed_count=(-1)**z*choose(k,z)*choose(l-k,b)*choose(n-l-k,m-k-b))
                          for z in range(k+1) for b in range(l-k+1)]
        ck('all_signed_terms', row['terms'] == expected_terms, [n,l,m,k])
        action = [sum(r['signed_count'] for r in expected_terms if r['t'] == t)
                  for t in range(min(l,m)+1)]
        ck('norm_and_signed_beta', row['D'] == D > 0 and row['norm'] == 2**k*D and
           row['action'] == action and row['beta'] == [D*v for v in action], [n,l,m,k])
        action_map[n,l,m,k] = action
    for n,k,t in product((68,956),range(6),range(6)):
        ck('coherent_signed_rectangular_actions',
           choose(n-2*k,5-k)*action_map[n,5,6,k][t] ==
           choose(n-2*k,6-k)*action_map[n,6,5,k][t], [n,k,t])

    # All anchor coordinates vanish before any reduction. No inverse of
    # that coordinate, and no included-anchor correction, belongs here.
    for row,(l,m) in zip(replay['anchor_cases'],[(0,0),(0,5),(5,0),(0,6),(6,0)]):
        ck('whole_zero_anchor', row == dict(layers=[l,m],orbit=[l,m,0,0],h=l+m,
           pair=enc(c[l+m]),y=enc(c[l+m]),affine=[0,1],D=g[m] if l==0 else 1))
    ck('anchor_exhaustion', len(replay['anchor_cases']) == 5)
    modes = replay['modes']
    ck('complete_mode_order', [(m['a'],m['b']) for m in modes] == list(product(range(7),repeat=2)))
    dimension = 1
    bounds = []
    old_bounds = []
    pivots = []
    comparisons = []
    required = F(638512,10**6)
    for mode in modes:
        a,b = mode['a'],mode['b']
        layers = [5,6] if max(a,b) <= 5 else [6]
        multiplicity = (choose(68,a)-choose(68,a-1))*(choose(956,b)-choose(956,b-1))
        D = {l:choose(68-2*a,l-a)*choose(956-2*b,l-b) for l in layers}
        ck('complete_mode_norm_dimension', mode['layers'] == layers and
           mode['multiplicity'] == multiplicity > 0 and
           mode['scaling'] == {str(l):v for l,v in D.items()} and min(D.values()) > 0,[a,b])
        dimension += len(layers)*multiplicity
        C = [F(*v) for v in mode['blocks']['66']]
        scale = D[6]
        lower,upper = C[0]/scale,C[1]/scale
        comparison = dict(mode=[a,b],scaling=D[6])
        if 5 in layers:
            A = [F(*v) for v in mode['blocks']['55']]
            Bb = [F(*v) for v in mode['blocks']['56']]
            ck('positive_old_pivot', 0 < A[0] <= A[1] and
               mode['five_normalized'] == [enc(v/D[5]) for v in A], [a,b])
            old_bounds.append(A[0]/D[5])
            ck('each_old_threshold', A[0] >= required*D[5] > 0, [a,b])
            pivots.append(dict(mode=[a,b],layer=5,interval=mode['five_normalized']))
            square_hi = max(v*v for v in Bb)
            square_lo = 0 if Bb[0] <= 0 <= Bb[1] else min(v*v for v in Bb)
            lower = (C[0]-square_hi/A[0])/scale
            upper = (C[1]-square_lo/A[1])/scale
            lhs,rhs = C[0]*A[0]-square_hi,required*scale*A[0]
            ck('division_free_pivot_threshold', lhs >= rhs > 0,[a,b])
            comparison.update(lhs=enc(lhs),rhs=enc(rhs),slack=enc(lhs-rhs),
                              square_interval=[enc(F(square_lo)),enc(square_hi)])
            # Exact algebraic congruence at all endpoint triples is an
            # additional identity check; whole-box signs follow from the
            # enclosing inequalities above, never corner sampling.
            for av,bv,cv in product(A,Bb,C):
                K = [[F(0),F(0),F(0)],[F(0),av,bv],[F(0),bv,cv]]
                T = [[F(1),F(0),F(0)],[F(0),F(1),-bv/av],[F(0),F(0),F(1)]]
                ck('zero_anchor_shell_congruence',congruence(K,T) ==
                   [[F(0),F(0),F(0)],[F(0),av,F(0)],[F(0),F(0),cv-bv*bv/av]],[a,b])
        else:
            lhs,rhs = C[0],required*scale
            ck('new_only_threshold',lhs >= rhs > 0,[a,b])
            comparison.update(lhs=enc(lhs),rhs=enc(F(rhs)),slack=enc(lhs-rhs))
        ck('every_final_interval_and_bound', mode['remainder_normalized'] == [enc(lower),enc(upper)] and
           required <= lower <= upper and mode['verdict'] == 'positive',[a,b])
        # This is the affine pair-minus-union block, without a Schur term.
        for key,interval in mode['blocks'].items():
            pair = F(*mode['pair_blocks'][key])
            ylo,yhi = [F(*v) for v in mode['y_blocks'][key]]
            ck('every_affine_block_no_anchor_subtraction',
               interval == [enc(pair-yhi),enc(pair-ylo)],[a,b,key])
        bounds.append(lower)
        comparisons.append(comparison)
    pivots += [dict(mode=[m['a'],m['b']],layer=6,interval=m['remainder_normalized']) for m in modes]
    ck('all_pivots_complete',pivots == replay['pivots'] and len(pivots)==85)
    ck('full_source_dimension', dimension == 1+g[5]+g[6])
    minimum = min(bounds)
    minimum_pivot = min(F(*p['interval'][0]) for p in pivots)
    ck('manuscript_final_minimum', [(m['a'],m['b']) for m,v in zip(modes,bounds) if v == minimum] == [(4,0)] and
       required <= minimum < F(638513,10**6) and
       replay['minimum_normalized_remainder'] == dict(mode=[4,0],value=enc(minimum),
          bracket=[enc(required),enc(F(638513,10**6))]))
    ck('manuscript_all_pivot_minimum', [(p['mode'],p['layer']) for p in pivots
       if F(*p['interval'][0])==minimum_pivot] == [([4,0],5)] and
       required <= minimum_pivot < F(638513,10**6) and len(old_bounds)==36 and
       replay['minimum_normalized_pivot'] == dict(mode=[4,0],layer=5,value=enc(minimum_pivot),
          bracket=[enc(required),enc(F(638513,10**6))]))
    for p,h in report['input_sha256'].items():
        ck('unchanged_inputs', sha(ROOT/p) == h,p)
    report.update(stage='verified',replay_checks=replay['checks'],
                  replay_sha256={'l117-critical-reverification.json':sha(B/'l117-critical-reverification.json')},
                  relations=121,presentations=726,modes=49,dimension=dimension,
                  endpoint_presentations=dict(endpoint_types),null_presentations=dict(null_types),
                  pivot_comparisons=comparisons,pivots=pivots,
                  normalized_final_lower_endpoints=list(map(enc,bounds)),
                  normalized_old_lower_endpoints=list(map(enc,old_bounds)),
                  minimum_normalized_remainder=enc(minimum),minimum_normalized_pivot=enc(minimum_pivot),
                  required_final_lower_bound=enc(F(638512,10**6)),
                  scope='L117 immutable excluded-anchor five/six application only; no full PSD claim.')
    save()
    print('L117 audit:',sum(counts.values()),'additional checks; replay:',replay['checks'],'; failures:',report['failures'])
    print('Actual/required relations 121/121, presentations 726/726, modes 49/49.')
    print('All final lower endpoints >= 638512/1000000 > 0; minimum < 638513/1000000 at (4,0).')
    print('All 85 lower endpoints >= 638512/1000000; required >0. Zero anchor and both rectangles pass.')
    print('Full certificate:',OUT.relative_to(ROOT))


if __name__ == '__main__':
    main()
