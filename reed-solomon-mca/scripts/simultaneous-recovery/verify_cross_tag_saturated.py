"""Independent complete coverage replay and all-support normalized recovery.

No producer imports. Verifies all scalar/r and h cases by cross multiplication;
classifies all 1820 supports for each survivor from eight moments alone.
"""
from itertools import combinations, permutations
from pathlib import Path
from collections import Counter
import json

ROOT = Path(__file__).parent
P = 97
H = tuple(x for x in range(1,P) if pow(x,16,P) == 1)


def value(s,x):
    v = 1
    for a in s:
        v = v*(x-a) % P
    return v


def moments(e):
    return [sum(a*pow(x,j,P) for x,a in e.items()) % P for j in range(1,9)]


def solve(k,m):
    a = [[pow(x,j,P) for x in k]+[m[j-1]] for j in range(1,5)]
    for j in range(4):
        i = next(i for i in range(j,4) if a[i][j])
        a[j],a[i] = a[i],a[j]
        a[j] = [v*pow(a[j][j],-1,P) % P for v in a[j]]
        for i in range(4):
            if i != j:
                t = a[i][j]
                a[i] = [(x-t*y) % P for x,y in zip(a[i],a[j])]
    return [a[j][-1] for j in range(4)]


def key(s):
    return (s['z'],tuple(s['W']),s['y2'],s['d'],s['h'],s['y1'],s['p'],s['q'],s['r'])


def verify_seed(seed):
    h,d = seed['h'],seed['d']
    ys,zs,w = (seed['y1'],seed['y2']),(1,seed['z']),seed['W']
    p,q,r = seed['p'],seed['q'],seed['r']
    b = {h,d,*ys,*zs}
    assert len(b | set(w)) == 9 and p*q*(1-p-q)*r*(1-r) % P
    c = {x:value([a for a in H if a not in b | set(w)],x) for x in b}
    n0 = {h:c[h]*q % P,d:c[d]*(1-r) % P, **{x:c[x] for x in zs}}
    n1 = {h:-c[h]*p % P,d:-c[d]*r % P, **{x:-c[x] % P for x in ys}}
    m0,m1 = moments(n0),moments(n1)
    excluded = [{h,d,*ys},{h,d,*zs},{h,*w},set(ys+zs)]
    records, admitted = [],[]
    for k in combinations(H,4):
        a,v = solve(k,m0),solve(k,m1)
        ma,mv = moments(dict(zip(k,a))),moments(dict(zip(k,v)))
        ra = [(x-y) % P for x,y in zip(ma[4:],m0[4:])]
        rv = [(x-y) % P for x,y in zip(mv[4:],m1[4:])]
        row = dict(K=k,intercept_weights=a,slope_weights=v,
                   residual_intercept=ra,residual_slope=rv)
        if not any(rv):
            assert any(ra), 'persistent full four-support normalized pencil'
            row['status'] = 'constant_inconsistent'
        else:
            j = next(j for j in range(4) if rv[j])
            mu = -ra[j]*pow(rv[j],-1,P) % P
            row['tested_mu'] = mu
            if any((x+mu*y) % P for x,y in zip(ra,rv)):
                row['status'] = 'inconsistent'
            elif mu in (0,96) or set(k) in excluded:
                row['status'] = 'base_or_universal_excluded'
            else:
                omega = [(x+mu*y) % P for x,y in zip(a,v)]
                n = [(x+mu*y) % P for x,y in zip(m0,m1)]
                assert moments(dict(zip(k,omega))) == n
                row.update(status='admitted',omega=omega,full_weight=all(omega))
                admitted.append(dict(K=k,mu=mu,omega=omega,moments=n,full_weight=all(omega)))
        records.append(row)
    assert len(records) == 1820
    singleton = [a for a in admitted if len(set(a['K']) & b) == 1
                 and next(iter(set(a['K']) & b)) in ys+zs]
    expected = {(tuple(a['K']),a['mu']):a for a in singleton}
    supplied = {(tuple(a['K']),a['mu']):a for a in seed['singleton_rows']}
    assert len(supplied) == len(seed['singleton_rows']) and expected.keys() == supplied.keys()
    for k,a in supplied.items():
        v = expected[k]
        assert a['omega'] == v['omega'] and a['moments'] == v['moments']
        tag = a['tag']
        assert set(a['K']) & b == {tag} and set(a['K']) == {tag,*a['S']}
        coeff = {x:-a['mu'] % P for x in ys}
        coeff.update({x:1 for x in zs})
        coeff[h],coeff[d] = (q-a['mu']*p) % P,(1-(1+a['mu'])*r) % P
        assert all((coeff[x]*value(a['S'],x)-a['u']*value(w,x)) % P == 0
                   for x in b if x != tag)
        assert a['full_weight'] == all(v['omega'])
    count = len({a['mu'] for a in admitted})
    assert count == 3 and len(admitted) == 3 and all(a['full_weight'] for a in admitted)
    assert {next(iter(set(a['K']) & b)) for a in singleton} == {seed['y1']}
    assert seed['distinct_singleton_mu'] == 3
    assert seed['tag_counts'] == {str(seed['y1']):3}
    return dict(key=key(seed),all_support_records=records,admitted=admitted,
                distinct_nonuniversal_mu=count,support_checks=1820)


def main():
    source = json.loads((ROOT/'cross-tag-saturated-result.json').read_text())
    assert source['complete'] and source['stop_before'] is None and not source['failures']
    assert [a['z'] for a in source['cubic_groups']] == list(H[1:])
    stats = Counter()
    expected_seed_keys = set()
    ci,ti = 0,0
    for part in source['cubic_groups']:
        z = part['z']
        available = [x for x in H if x not in (1,z)]
        all_cubics = set(combinations(available,3))
        supplied_cubics = []
        ratios = []
        for group in part['groups']:
            ratio = group['ratio']
            ratios.append(ratio)
            for s in group['cubics']:
                assert tuple(s) in all_cubics
                assert (value(s,z)-ratio*value(s,1)) % P == 0
                supplied_cubics.append(tuple(s))
        assert ratios == sorted(set(ratios))
        assert len(supplied_cubics) == 364 and set(supplied_cubics) == all_cubics
        stats['cubic_memberships'] += 364
        for group in part['groups']:
            ratio,g = group['ratio'],group['cubics']
            if len(g) < 4:
                continue
            for wi,w in enumerate(g):
                labels = [x for x in H if x not in {1,z,*w}]
                for y,d in permutations(labels,2):
                    row = source['scalar_r_cases'][ci]
                    assert row[:5] == [z,ratio,wi,y,d]
                    expected_si = [i for i,s in enumerate(g) if s != w and y not in s and d not in s]
                    assert [a[0] for a in row[5]] == expected_si
                    rgroups = {}
                    for si,u,mu,r in row[5]:
                        s = g[si]
                        assert 0 < u < P and 0 < mu < P
                        assert (u*value(w,1)-value(s,1)) % P == 0
                        assert (mu*value(s,y)+u*value(w,y)) % P == 0
                        stats['scalar_cases'] += 1
                        if mu == 96:
                            assert r is None
                            stats['excluded_mu'] += 1
                        else:
                            assert r is not None and 0 <= r < P
                            assert ((1-(1+mu)*r)*value(s,d)-u*value(w,d)) % P == 0
                            if r not in (0,1):
                                rgroups.setdefault(r,[]).append((si,s,u,mu))
                    for r,members in sorted(rgroups.items()):
                        for triple in combinations(members,3):
                            item = source['triple_tests'][ti]
                            ss,mus = [a[1] for a in triple],[a[3] for a in triple]
                            assert item['case'] == ci and item['r'] == r
                            assert item['S_indices'] == [a[0] for a in triple] and item['mu'] == mus
                            union = set().union(*map(set,ss))
                            stats['common_r_triples'] += 1
                            if len(union) == 9:
                                assert item['status'] == 'audited_L053_disjoint'
                                assert False, 'audited disjoint exclusion unexpectedly violated'
                            elif len(set(mus)) != 3:
                                assert item['status'] == 'colliding_mu' and not item['h_tests']
                            else:
                                free = [x for x in H if x not in union | set(w) | {1,z,y,d}]
                                assert item['free'] == free
                                assert item['status'] == ('tested_h' if len(free) >= 2 else 'no_room')
                                assert [a[0] for a in item['h_tests']] == (free if len(free) >= 2 else [])
                                for h,responses,p,q,residual,gate in item['h_tests']:
                                    for response,(_,s,u,_) in zip(responses,triple):
                                        assert (response*value(s,h)-u*value(w,h)) % P == 0
                                    assert all((q-p*mu-response) % P == 0
                                               for mu,response in zip(mus[:2],responses[:2]))
                                    assert residual == (q-p*mus[2]-responses[2]) % P
                                    assert gate == p*q*(1-p-q) % P
                                    stats['h_tests'] += 1
                                    if residual == 0 and gate:
                                        for tag in free:
                                            if tag != h:
                                                expected_seed_keys.add((z,tuple(w),y,d,h,tag,p,q,r))
                            ti += 1
                    ci += 1
    assert ci == len(source['scalar_r_cases']) and ti == len(source['triple_tests'])
    assert {k:stats[k] for k in source['statistics']} == source['statistics']
    assert len(source['seeds']) == len(expected_seed_keys) == 8
    assert {key(s) for s in source['seeds']} == expected_seed_keys
    evidence = [verify_seed(s) for s in source['seeds']]
    # L054's numerical construction is checked as a regression, not assumed.
    assert (33,(18,50,64),27,96,70,75,71,16,87) in expected_seed_keys
    result = dict(scope='complete normalized saturated-row replay; every rejection and all seed supports',
                  coverage=dict(cubic_memberships=stats['cubic_memberships'],required_cubic_memberships=5460,
                                scalar_case_groups=ci,scalar_cases=stats['scalar_cases'],
                                common_r_triples=ti,h_tests=stats['h_tests'],
                                seeds=len(evidence),support_checks=1820*len(evidence),
                                required_support_checks=14560),
                  seeds=evidence, summary=dict(complete=True,maximum_nonuniversal_mu=3,
                                              eleven_refutation_threshold=12,failures=[]))
    out = ROOT/'cross-tag-saturated-verification.json'
    out.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print(f'coverage cubics {stats["cubic_memberships"]}/5460; scalar cases {stats["scalar_cases"]}; '
          f'triples {ti}; h tests {stats["h_tests"]}; seeds {len(evidence)}/8')
    print(f'all-support checks {14560}/14560; saturated-row nonuniversal maximum 3; '
          f'eleven-refutation threshold 12; failures 0; certificate {out}')


if __name__ == '__main__':
    main()
