"""One exact intersecting-singleton test; saves every scalar/r case.

Stops at the first fully gated witness. A stop is not exhaustive coverage.
Reuses L053's equations and its independently audited moment construction.
"""
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path
import json
from three_singleton import H, P, INV, ev, verify

OUT = Path(__file__).with_name('intersecting-singleton-result.json')


def main():
    stats = Counter()
    partitions, cases, triple_tests = [], [], []
    witness = None
    for z in H[1:]:
        groups = {}
        for s in combinations([x for x in H if x not in (1, z)], 3):
            values = {x: ev(s, x) for x in H if x not in s}
            ratio = values[z]*INV[values[1]] % P
            groups.setdefault(ratio, []).append((s, values))
        partitions.append(dict(z=z, groups=[dict(ratio=k, cubics=[s for s, _ in g])
                                            for k, g in sorted(groups.items())]))
        stats['cubics'] += 364
        for ratio, group in sorted(groups.items()):
            if len(group) < 4:
                continue
            for w, wv in group:
                available = [x for x in H if x not in (1, z) and x not in w]
                for y, d in permutations(available, 2):
                    records, r_groups = [], {}
                    for s, sv in group:
                        if s == w or y in s or d in s:
                            continue
                        u = sv[1]*INV[wv[1]] % P
                        mu = -u*wv[y]*INV[sv[y]] % P
                        row = dict(S=s, u=u, mu=mu)
                        stats['scalar_cases'] += 1
                        if mu == P-1:
                            row['status'] = 'excluded_mu'
                        else:
                            r = (1-u*wv[d]*INV[sv[d]])*INV[1+mu] % P
                            row['r'] = r
                            row['status'] = 'ungated_r' if r in (0, 1) else 'gated_r'
                            if r not in (0, 1):
                                r_groups.setdefault(r, []).append((s, sv, u, mu))
                        stats[row['status']] += 1
                        records.append(row)
                    case_index = len(cases)
                    cases.append(dict(z=z, ratio=ratio, W=w, y=y, d=d, candidates=records))
                    for r, members in sorted(r_groups.items()):
                        for triple in combinations(members, 3):
                            ss = [a[0] for a in triple]
                            mus = [a[3] for a in triple]
                            union = set().union(*map(set, ss))
                            if len(union) == 9:
                                continue  # The unchanged, audited disjoint scope.
                            item = dict(case=case_index, S=ss, mu=mus, r=r, h_tests=[])
                            stats['intersecting_r_triples'] += 1
                            if len(set(mus)) != 3:
                                item['status'] = 'colliding_mu'
                            else:
                                free = [x for x in H if x not in union | set(w) | {1, z, y, d}]
                                item['free_h_tag_labels'] = free
                                item['status'] = 'no_h_tag_room' if len(free) < 2 else 'h_rejected'
                                if len(free) >= 2:
                                    for h in free:
                                        responses = [u*wv[h]*INV[sv[h]] % P for _, sv, u, _ in triple]
                                        p = (responses[1]-responses[0])*INV[(mus[0]-mus[1]) % P] % P
                                        q = (responses[0]+p*mus[0]) % P
                                        residual = (q-p*mus[2]-responses[2]) % P
                                        gate = p*q*(1-p-q) % P
                                        item['h_tests'].append(dict(h=h, responses=responses, p=p, q=q,
                                                                    residual=residual, gate=gate))
                                        stats['h_tests'] += 1
                                        if residual or not gate:
                                            continue
                                        tag = next(x for x in free if x != h)
                                        witness = verify(h, d, tag, y, (1, z), w, ss, mus,
                                                         [a[2] for a in triple], p, q, r)
                                        # The reused helper's literal label describes its old scope.
                                        witness['pairwise_disjoint_outside'] = False
                                        witness['outside_union_size'] = len(union)
                                        witness['pairwise_intersections'] = [sorted(set(a) & set(b))
                                                                             for a, b in combinations(ss, 2)]
                                        item['status'] = 'gated_witness'
                                        stats['gated_witnesses'] += 1
                                        break
                            triple_tests.append(item)
                            if witness:
                                break
                        if witness:
                            break
                    if witness:
                        break
                if witness:
                    break
            if witness:
                break
        print(f'z={z}; scalar cases {stats["scalar_cases"]}; r triples {stats["intersecting_r_triples"]}; witness {bool(witness)}', flush=True)
        if witness:
            break
    result = dict(scope='intersecting same-y-tag triples; first-witness search; normalized z1=1',
                  complete=not bool(witness), statistics=dict(stats), cubic_groups=partitions,
                  scalar_r_cases=cases, triple_tests=triple_tests, witness=witness, failures=[])
    OUT.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print(f'gated witnesses {int(bool(witness))}; required to refute triple exclusion 1; eleven-refutation threshold 12')
    print(f'complete {result["complete"]}; failures 0; certificate {OUT}')


if __name__ == '__main__':
    main()
