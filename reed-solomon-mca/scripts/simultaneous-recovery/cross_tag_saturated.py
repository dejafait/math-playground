"""Bounded cross-tag test of saturated singleton rows; never claims coverage on timeout.

Audited L053 equations generate seeds. All visited scalar/r cases and
triple/h tests are saved; singleton recovery checks use all eight moments.
"""
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path
import json
import time
from three_singleton import H, P, INV, ev, moments, recover

ROOT = Path(__file__).parent
OUT = ROOT/'cross-tag-saturated-result.json'
SECONDS = 55


def singleton_rows(h, d, ys, zs, w, p, q, r):
    b = {h, d, *ys, *zs}
    o = [x for x in H if x not in b]
    c = {x: ev([a for a in H if a not in b | set(w)], x) for x in b}
    rows = []
    for tag in (*ys, *zs):
        for s in combinations(o, 3):
            sv = {x: ev(s, x) for x in b}
            wv = {x: ev(w, x) for x in b}
            zz = next(x for x in zs if x != tag)
            yy = next(x for x in ys if x != tag)
            u = sv[zz]*INV[wv[zz]] % P
            mu = -u*wv[yy]*INV[sv[yy]] % P
            if mu == P-1:
                continue
            coeff = {x: -mu % P for x in ys}
            coeff.update({x: 1 for x in zs})
            coeff[h] = (q-mu*p) % P
            coeff[d] = (1-(1+mu)*r) % P
            if any((coeff[x]*sv[x]-u*wv[x]) % P for x in b if x != tag):
                continue
            k = tuple(sorted((tag, *s)))
            n = moments({x: c[x]*coeff[x] % P for x in b})
            omega = recover(k, n)  # asserts all eight moments, permits zeros
            rows.append(dict(tag=tag, S=s, K=k, mu=mu, u=u, omega=omega,
                             moments=n, full_weight=all(omega)))
    return rows


def main():
    start = time.monotonic()
    stats = Counter()
    partitions, scalar_cases, triples, seeds = [], [], [], []
    seen = set()
    maximum = None
    complete = True
    stop_location = None
    for z in H[1:]:
        groups = {}
        for s in combinations([x for x in H if x not in (1, z)], 3):
            values = {x: ev(s, x) for x in H if x not in s}
            groups.setdefault(values[z]*INV[values[1]] % P, []).append((s, values))
        partitions.append(dict(z=z, groups=[dict(ratio=k, cubics=[s for s, _ in g])
                                            for k, g in sorted(groups.items())]))
        for ratio, group in sorted(groups.items()):
            if len(group) < 4:
                continue
            for wi, (w, wv) in enumerate(group):
                available = [x for x in H if x not in (1, z) and x not in w]
                for y, d in permutations(available, 2):
                    if time.monotonic()-start > SECONDS:
                        complete = False
                        stop_location = dict(z=z, ratio=ratio, W_index=wi, y=y, d=d)
                        break
                    records, r_groups = [], {}
                    for si, (s, sv) in enumerate(group):
                        if s == w or y in s or d in s:
                            continue
                        u = sv[1]*INV[wv[1]] % P
                        mu = -u*wv[y]*INV[sv[y]] % P
                        stats['scalar_cases'] += 1
                        if mu == P-1:
                            records.append([si, u, mu, None])
                            stats['excluded_mu'] += 1
                        else:
                            r = (1-u*wv[d]*INV[sv[d]])*INV[1+mu] % P
                            records.append([si, u, mu, r])
                            if r not in (0, 1):
                                r_groups.setdefault(r, []).append((si, s, sv, u, mu))
                    case = len(scalar_cases)
                    scalar_cases.append([z, ratio, wi, y, d, records])
                    for r, members in sorted(r_groups.items()):
                        for triple in combinations(members, 3):
                            ss = [a[1] for a in triple]
                            mus = [a[4] for a in triple]
                            union = set().union(*map(set, ss))
                            stats['common_r_triples'] += 1
                            item = dict(case=case, S_indices=[a[0] for a in triple],
                                        r=r, mu=mus, h_tests=[])
                            if len(union) == 9:
                                item['status'] = 'audited_L053_disjoint'
                            elif len(set(mus)) != 3:
                                item['status'] = 'colliding_mu'
                            else:
                                free = [x for x in H if x not in union | set(w) | {1,z,y,d}]
                                item['free'] = free
                                item['status'] = 'tested_h' if len(free) >= 2 else 'no_room'
                                if len(free) >= 2:
                                    for h in free:
                                        response = [a[3]*wv[h]*INV[a[2][h]] % P for a in triple]
                                        p = (response[1]-response[0])*INV[(mus[0]-mus[1]) % P] % P
                                        q = (response[0]+p*mus[0]) % P
                                        residual = (q-p*mus[2]-response[2]) % P
                                        gate = p*q*(1-p-q) % P
                                        item['h_tests'].append([h,response,p,q,residual,gate])
                                        stats['h_tests'] += 1
                                        if residual or not gate:
                                            continue
                                        for tag in free:
                                            if tag == h:
                                                continue
                                            key = (z,w,y,d,h,tag,p,q,r)
                                            if key in seen:
                                                continue
                                            seen.add(key)
                                            rows = singleton_rows(h,d,(tag,y),(1,z),w,p,q,r)
                                            seed = dict(z=z,W=w,y2=y,d=d,h=h,y1=tag,p=p,q=q,r=r,
                                                        generating_case=case, generating_S=ss,
                                                        singleton_rows=rows,
                                                        distinct_singleton_mu=len({a['mu'] for a in rows}),
                                                        tag_counts=dict(Counter(a['tag'] for a in rows)))
                                            assert seed['tag_counts'].get(tag, 0) >= 3
                                            seeds.append(seed)
                                            if maximum is None or seed['distinct_singleton_mu'] > maximum['distinct_singleton_mu']:
                                                maximum = seed
                            triples.append(item)
                    if not complete:
                        break
                if not complete:
                    break
            if not complete:
                break
        print(f'z={z}; scalar cases {stats["scalar_cases"]}; seeds {len(seeds)}; '
              f'max singleton parameters {maximum["distinct_singleton_mu"] if maximum else 0}; '
              f'complete so far {complete}', flush=True)
        if not complete:
            break
    result = dict(scope='normalized saturated y-singleton seeds; all four singleton tags; bounded 55-second run',
                  complete=complete, stop_before=stop_location, statistics=dict(stats),
                  cubic_groups=partitions, scalar_r_cases=scalar_cases, triple_tests=triples,
                  seeds=seeds, maximum=maximum, failures=[])
    OUT.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print(f'complete {complete}; singleton maximum {maximum["distinct_singleton_mu"] if maximum else 0}; '
          f'eleven-refutation threshold 12; failures 0; certificate {OUT}')


if __name__ == '__main__':
    main()
