"""Critical audit of the immutable L116 application, with preserved originals.

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
OUT = B / 'l116-critical-audit.json'


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

    names = ['fixed-product-coupled.json', 'fixed-product-coupled-verification.json',
             'fixed_product_coupled.py', 'verify_fixed_product_coupled.py',
             'l112-l113-critical-audit.json', 'l114-critical-audit.json',
             'l115-critical-audit.json', 'positive-factor-enclosure.json.gz',
             'fixed-product-five-shell.json']
    report['input_sha256'] = {str((B/p).relative_to(ROOT)): sha(B/p) for p in names}
    save()
    spec = importlib.util.spec_from_file_location('l116_replay', B/'verify_fixed_product_coupled.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.OUT = B/'l116-critical-reverification.json'
    mod.main()
    replay = read('l116-critical-reverification.json')
    ck('complete_replay_equality', replay == read('fixed-product-coupled-verification.json'))
    source = read('fixed-product-coupled.json')
    c = [F(*v) for v in source['c']]
    g = [comb(68, i)*comb(956, i) for i in range(69)]
    ck('positive_homogeneous_normalization',
       source['N'] == 65537**28//2**128+1 and source['H'] == comb(1024,68) and
       F(*source['rho']) == F(source['N'],source['H']) > 0)

    # Every retained audit binding and the repaired string replay case.
    for name, code in [('l112-l113-critical-audit.json','critical_audit_l112_l113.py'),
                       ('l114-critical-audit.json','critical_audit_l114.py'),
                       ('l115-critical-audit.json','critical_audit_l115.py')]:
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

    endpoint_types = Counter()
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
                ck('Boolean_value_and_D', row['interval'] == [enc(c[max(i,j,h)])]*2 and
                   D == (g[j] if i == 0 else 1), [l,m,t,s,p['order']])
            elif min(i,j,h) < 5:
                ck('null_value_capacity', row['interval'] == [[0,1],[0,1]] and
                   min(c[i],c[j],c[h]) == 0, [l,m,t,s,p['order']])
        ck('unpermuted_entry_class', row['h'] == l+m-t-s and
           (F(*row['interval'][0]) > 0 if row['h'] >= 5 or row['h'] == 0 else
            row['interval'] == [[0,1],[0,1]]), [l,m,t,s])
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

    modes = replay['modes']
    ck('complete_mode_order', [(m['a'],m['b']) for m in modes] == list(product(range(7),repeat=2)))
    dimension = 1
    bounds = []
    old_bounds = []
    constant = modes[0]
    # All eight corners of the unnormalized constant 3-by-3 block.
    # This checks the algebraic cross correction, not box positivity by corners.
    cs = {key:F(*v) for key,v in constant['anchor_correction'].items()}
    ck('full_constant_corrections', cs == {'55':c[5]**2*g[5]**2,
       '56':c[5]*c[6]*g[5]*g[6], '66':c[6]**2*g[6]**2})
    anchor = [c[5]*g[5],c[6]*g[6]]
    T = [[F(1),-anchor[0],-anchor[1]],[F(0),F(1),F(0)],[F(0),F(0),F(1)]]
    for bits in product((0,1),repeat=3):
        A,Bb,C = [F(*constant['blocks'][key][e]) for key,e in zip(('55','56','66'),bits)]
        K = [[F(1),*anchor],[anchor[0],A+cs['55'],Bb+cs['56']],
             [anchor[1],Bb+cs['56'],C+cs['66']]]
        ck('whole_anchor_congruence', congruence(K,T) ==
           [[F(1),F(0),F(0)],[F(0),A,Bb],[F(0),Bb,C]], list(bits))
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
        scale = c[6]*D[6]
        lower,upper = C[0]/scale,C[1]/scale
        if 5 in layers:
            A = [F(*v) for v in mode['blocks']['55']]
            Bb = [F(*v) for v in mode['blocks']['56']]
            ck('positive_old_pivot', 0 < A[0] <= A[1] and
               mode['five_normalized'] == [enc(v/(c[5]*D[5])) for v in A], [a,b])
            old_bounds.append(A[0]/(c[5]*D[5]))
            square_hi = max(v*v for v in Bb)
            square_lo = 0 if Bb[0] <= 0 <= Bb[1] else min(v*v for v in Bb)
            lower = (C[0]-square_hi/A[0])/scale
            upper = (C[1]-square_lo/A[1])/scale
            # Cross-multiplied exact certificate: no floating or midpoint test.
            ck('division_free_pivot_threshold',
               C[0]*A[0]-square_hi >= F(638632,10**6)*scale*A[0] > 0,[a,b])
        ck('every_final_interval_and_bound', mode['remainder_normalized'] == [enc(lower),enc(upper)] and
           F(638632,10**6) <= lower <= upper and mode['verdict'] == 'positive',[a,b])
        if a or b:
            ck('all_nonconstant_anchor_zeros', all(F(*v) == 0 for v in mode['anchor_correction'].values()),[a,b])
        bounds.append(lower)
    ck('full_source_dimension', dimension == 1+g[5]+g[6])
    minimum = min(bounds)
    ck('manuscript_final_minimum', [(m['a'],m['b']) for m,v in zip(modes,bounds) if v == minimum] == [(4,0)] and
       F(638632,10**6) <= minimum < F(638633,10**6) and
       replay['minimum_normalized_remainder'] == dict(mode=[4,0],value=enc(minimum),
          bracket=[enc(F(638632,10**6)),enc(F(638633,10**6))]))
    ck('manuscript_old_minimum', len(old_bounds) == 36 and
       F(630869,10**6) <= min(old_bounds) < F(630870,10**6) and
       min(old_bounds) == F(*read('l115-critical-audit.json')['minimum_normalized_lower']))
    for p,h in report['input_sha256'].items():
        ck('unchanged_inputs', sha(ROOT/p) == h,p)
    report.update(stage='verified',replay_checks=replay['checks'],
                  replay_sha256={'l116-critical-reverification.json':sha(B/'l116-critical-reverification.json')},
                  relations=121,presentations=726,modes=49,dimension=dimension,
                  endpoint_presentations=dict(endpoint_types),
                  normalized_final_lower_endpoints=list(map(enc,bounds)),
                  normalized_old_lower_endpoints=list(map(enc,old_bounds)),
                  minimum_normalized_remainder=enc(minimum),
                  required_final_lower_bound=enc(F(638632,10**6)),
                  scope='L116 immutable included-anchor five/six application only; no full PSD claim.')
    save()
    print('L116 audit:',sum(counts.values()),'additional checks; replay:',replay['checks'],'; failures:',report['failures'])
    print('Actual/required relations 121/121, presentations 726/726, modes 49/49.')
    print('All final lower endpoints >= 638632/1000000 > 0; minimum < 638633/1000000 at (4,0).')
    print('All 36 old lower endpoints >= 630869/1000000 > 0; full anchor and both rectangular actions pass.')
    print('Full certificate:',OUT.relative_to(ROOT))


if __name__ == '__main__':
    main()
