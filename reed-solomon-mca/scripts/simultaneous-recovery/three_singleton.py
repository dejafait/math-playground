"""Bounded exact search for three disjoint same-y-tag recoveries.

Stops at the first fully gated witness. Saves complete tested-case counts
and the selected eight-moment certificate; no all-labeling claim on a stop.
"""
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path
import json

P = 97
H = tuple(x for x in range(1, P) if pow(x, 16, P) == 1)
INV = {x: pow(x, -1, P) for x in range(1, P)}
V = {x: tuple(pow(x, j, P) for j in range(1, 9)) for x in H}
OUT = Path(__file__).with_name('three-singleton-result.json')


def ev(roots, x):
    a = 1
    for y in roots:
        a = a * (x-y) % P
    return a


def moments(word):
    return [sum(w * V[x][j] for x, w in word.items()) % P for j in range(8)]


def recover(k, n):
    a = [[V[x][j] for x in k] + [n[j]] for j in range(4)]
    for j in range(4):
        pivot = next(i for i in range(j, 4) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        a[j] = [z * INV[a[j][j]] % P for z in a[j]]
        for i in range(4):
            if i != j:
                t = a[i][j]
                a[i] = [(x-t*y) % P for x, y in zip(a[i], a[j])]
    omega = [a[j][4] for j in range(4)]
    assert moments(dict(zip(k, omega))) == n
    return omega


def verify(h, d, tag, y, zs, w, ss, mus, us, p, q, r):
    b = {h, d, tag, y, *zs}
    c = {x: ev([a for a in H if a not in b | set(w)], x) for x in b | set(w)}
    rho = next(x for x in range(2, P) if all((x-(1-x)*mu) % P for mu in mus))
    e0 = {h: c[h]*p*INV[(1-rho) % P] % P,
          d: c[d]*r*INV[(1-rho) % P] % P}
    e0.update({x: c[x]*INV[(1-rho) % P] % P for x in (tag, y)})
    e1 = {h: c[h]*q*INV[rho] % P, d: c[d]*(1-r)*INV[rho] % P}
    e1.update({x: c[x]*INV[rho] % P for x in zs})
    e2 = {h: -c[h]*(1-p-q) % P}
    e2.update({x: -c[x] % P for x in w})
    m0, m1 = moments(e0), moments(e1)
    slope = [(v-u) % P for u, v in zip(m0, m1)]
    pencil = lambda t: [(a+t*v) % P for a, v in zip(m0, slope)]
    assert moments(e2) == pencil(rho)
    assert all(all(e.values()) for e in (e0, e1, e2))
    assert p*q*(1-p-q)*r*(1-r) % P
    records = []
    for s, mu, u in zip(ss, mus, us):
        n = {x: -mu*c[x] % P for x in (tag, y)}
        n.update({x: c[x] for x in zs})
        n[h] = c[h]*(q-p*mu) % P
        n[d] = c[d]*(1-(1+mu)*r) % P
        k = tuple(sorted((tag, *s)))
        omega = recover(k, moments(n))
        e = (rho-(1-rho)*mu) % P
        t = rho*INV[e] % P
        error = {x: a*INV[e] % P for x, a in zip(k, omega)}
        assert moments(error) == pencil(t)
        assert t not in (0, 1, rho)
        records.append(dict(S=s, K=k, mu=mu, u=u, E=e, T=t,
                            N_moments=moments(n), omega=omega,
                            error=error, error_moments=moments(error),
                            full_weight=all(omega)))
    assert len({a['T'] for a in records}) == 3
    return dict(h=h, d=d, Y=[tag, y], Z=zs, W=w, p_q_r=[p, q, r],
                gamma=[0, 1, rho], lambda_value=1, c=c,
                original_errors=[e0, e1, e2], syndrome_intercept=m0,
                syndrome_slope=slope, records=records,
                triple_gates=True, all_eight_moments=True,
                pairwise_disjoint_outside=True)


def main():
    stats = Counter()
    per_z = []
    cubic_groups, triple_records, tests = [], [], []
    witness = None
    for z in H[1:]:
        groups = {}
        available = [x for x in H if x not in (1, z)]
        for s in combinations(available, 3):
            values = {x: ev(s, x) for x in H if x not in s}
            key = values[z]*INV[values[1]] % P
            groups.setdefault(key, []).append((s, values))
            stats['cubics'] += 1
        cubic_groups.append(dict(z=z, groups=[dict(ratio=key, cubics=[s for s, _ in group])
                                             for key, group in sorted(groups.items())]))
        local = Counter()
        for key, group in sorted(groups.items()):
            if len(group) < 4:
                continue  # Three candidates and distinct W (mu=-1 otherwise).
            for triple in combinations(group, 3):
                ss = [a[0] for a in triple]
                used = set().union(*map(set, ss))
                if len(used) != 9:
                    continue
                local['disjoint_triples'] += 1
                triple_records.append(dict(z=z, ratio=key, S=ss))
                complement = [x for x in available if x not in used]
                assert len(complement) == 5
                for y, d in permutations(complement, 2):
                    for w, wv in group:
                        if w in ss or y in w or d in w:
                            continue
                        us = [v[1]*INV[wv[1]] % P for _, v in triple]
                        mus = [-u*wv[y]*INV[v[y]] % P
                               for u, (_, v) in zip(us, triple)]
                        local['scalar_tests'] += 1
                        row = dict(z=z, ratio=key, S=ss, y=y, d=d, W=w, u=us, mu=mus)
                        if 96 in mus or len(set(mus)) != 3:
                            row['rejection'] = 'excluded_or_colliding_scalar'
                            tests.append(row)
                            continue
                        rs = [(1-u*wv[d]*INV[v[d]])*INV[1+m] % P
                              for u, m, (_, v) in zip(us, mus, triple)]
                        row['r'] = rs
                        if len(set(rs)) != 1 or rs[0] in (0, 1):
                            row['rejection'] = 'inconsistent_or_ungated_r'
                            tests.append(row)
                            continue
                        row['rejection'] = 'r_pass'
                        tests.append(row)
                        local['r_pass'] += 1
                        for h, tag in permutations([x for x in complement
                                                   if x not in (y, d) and x not in w], 2):
                            responses = [u*wv[h]*INV[v[h]] % P
                                         for u, (_, v) in zip(us, triple)]
                            p = (responses[1]-responses[0])*INV[(mus[0]-mus[1]) % P] % P
                            q = (responses[0]+p*mus[0]) % P
                            local['h_tests'] += 1
                            if (q-p*mus[2]-responses[2]) % P or not p*q*(1-p-q) % P:
                                continue
                            witness = verify(h, d, tag, y, (1, z), w, ss, mus, us,
                                             p, q, rs[0])
                            local['gated_witnesses'] += 1
                            break
                        if witness:
                            break
                    if witness:
                        break
                if witness:
                    break
            if witness:
                break
        stats.update(local)
        per_z.append(dict(z=z, counts=dict(local), complete=not bool(witness)))
        if witness:
            break
    result = dict(scope='normalized z1=1; bounded first-witness same-y search',
                  complete=not bool(witness), statistics=dict(stats),
                  per_z=per_z, cubic_groups=cubic_groups,
                  disjoint_triples=triple_records, recovery_tests=tests,
                  witness=witness, failures=[])
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(f"gated witnesses {int(bool(witness))}; required to refute at-most-two 1")
    print(f"full-weight selected recoveries {sum(r['full_weight'] for r in witness['records']) if witness else 0}; required 3")
    print(f"search complete {result['complete']}; failures 0; certificate {OUT}")


if __name__ == '__main__':
    main()
