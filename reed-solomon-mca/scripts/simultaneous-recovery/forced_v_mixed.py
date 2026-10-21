"""Complete fixed-H forced-V branch test, with exact F_97 arithmetic.

Source partition is the already audited L049 certificate. Every admitted
record is independently checked against all eight moments. E is relaxed:
counts are upper bounds for every original finite chart, not witnesses.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import finite_count as fc

P, H, V = fc.P, fc.H, fc.V
INV = {x: pow(x, -1, P) for x in range(1, P)}
OUT = Path(__file__).with_name('forced-v-mixed-result.json')
SOURCE = Path(__file__).with_name('disjoint-d-pair-result.json')


def ev(roots, x):
    a = 1
    for root in roots:
        a = a * (x-root) % P
    return a


def recover(k, target):
    weights = tuple(sum(a*b for a, b in zip(row, target[:4])) % P
                    for row in fc.INVERSES[tuple(sorted(k))])
    assert fc.moment(dict(zip(sorted(k), weights))) == target
    return weights


def target(c, ys, zs, d, p, q, r, mu):
    word = {x: -mu*c[x] % P for x in ys}
    word.update({x: c[x] for x in zs})
    word[1] = c[1]*(q-mu*p) % P
    word[d] = c[d]*(1-(1+mu)*r) % P
    return fc.moment(word)


def forced_v(c, ys, zs, d, p, q, residual):
    cols = {x: tuple(ev(residual, x)*V[x][j] % P for j in range(4))
            for x in (1, d, *ys, *zs)}
    fy = tuple((sum(c[x]*cols[x][j] for x in ys) + c[1]*p*cols[1][j]) % P
               for j in range(4))
    rhs = tuple((sum(c[x]*cols[x][j] for x in zs) + c[1]*q*cols[1][j]) % P
                for j in range(4))
    rank, ok, solution = fc.solve([fy, tuple(-x % P for x in cols[d])], rhs)
    if not ok:
        return 'V_inconsistent', None
    assert rank == 2 and solution is not None
    mu, beta = solution
    if mu in (0, 96):
        return 'V_selected_scalar', None
    r = (1-beta*INV[c[d]]) * INV[1+mu] % P
    if r in (0, 1):
        return 'r_gate', None
    omega = recover(residual, target(c, ys, zs, d, p, q, r, mu))
    if not all(omega):
        return 'V_lower_weight', None
    return 'feasible', {'mu': mu, 'r': r, 'omega': omega}


def mixed(c, ys, zs, d, w, p, q, r, bprime, tail):
    bset = (1, d, *ys, *zs)
    records = []
    tested = 0
    for b in (1, *ys, *zs):
        z = next(x for x in zs if x != b)
        y = next(x for x in ys if x != b)
        for bp in bprime:
            for pair in combinations(tail, 2):
                tested += 1
                s = (bp, *pair)
                values = {x: ev(s, x) for x in bset if x != b}
                u = values[z] * INV[ev(w, z)] % P
                mu = -u*ev(w, y)*INV[values[y]] % P
                if mu in (0, 96):
                    continue
                ax = {1: (q-mu*p) % P, d: (1-(1+mu)*r) % P}
                ax.update({x: -mu % P for x in ys})
                ax.update({x: 1 for x in zs})
                if any((ax[x]*values[x]-u*ev(w, x)) % P
                       for x in bset if x != b):
                    continue
                k = tuple(sorted((b, *s)))
                n = target(c, ys, zs, d, p, q, r, mu)
                omega = recover(k, n)
                records.append({'K': k, 'mu': mu, 'u': u,
                                'omega': omega, 'N_moments': n,
                                'full_weight': all(omega)})
    assert tested == 250
    return records


def main():
    data = json.loads(SOURCE.read_text())
    assert len(data['complete_groups']) == 8190
    counts = Counter()
    cases = []
    seen = set()
    raw_pairs = 0
    for index, choice in enumerate(data['complete_groups'], 1):
        ys, zs = tuple(choice['Y']), tuple(choice['Z'])
        for key, gg in choice['groups']:
            if len(gg) < 3:
                continue
            group = [tuple(s) for s in gg]
            for w in group:
                wvals = {x: ev(w, x) for x in (1, *ys, *zs)}
                for s, ss in combinations([a for a in group if a != w], 2):
                    raw_pairs += 1
                    rows = []
                    for outside in (s, ss):
                        u = ev(outside, zs[0])*INV[wvals[zs[0]]] % P
                        mu = -u*wvals[ys[0]]*INV[ev(outside, ys[0])] % P
                        ah = u*wvals[1]*INV[ev(outside, 1)] % P
                        assert all(((-mu if x in ys else 1)*ev(outside, x)
                                    -u*wvals[x]) % P == 0 for x in (*ys, *zs))
                        rows.append((mu, ah))
                    (mu, ah), (nu, bh) = rows
                    if mu in (0, 96) or nu in (0, 96) or mu == nu:
                        counts['pair_scalar_gate'] += 1
                        continue
                    p = (ah-bh)*INV[(nu-mu) % P] % P
                    q = (ah+mu*p) % P
                    if p*q*(1-p-q) % P == 0:
                        counts['p_q_gate'] += 1
                        continue
                    common = set(s) & set(ss)
                    assert len(common) == 1 and common <= set(w)
                    shared = next(iter(common))
                    residual = tuple(sorted((set(s) | set(ss)) - common))
                    assert len(residual) == 4
                    assert not set(residual) & (set(w)-common)
                    used = {1, *ys, *zs, *w, *s, *ss}
                    for d in H:
                        if d in used:
                            continue
                        counts['d_pair_presentations'] += 1
                        identity = (ys, zs, d, w, p, q, residual)
                        if identity in seen:
                            counts['duplicate_presentations'] += 1
                            continue
                        seen.add(identity)
                        union = {1, d, *ys, *zs, *w}
                        c = {x: ev([a for a in H if a not in union], x) for x in union}
                        status, vrec = forced_v(c, ys, zs, d, p, q, residual)
                        counts[status] += 1
                        if vrec is None:
                            continue
                        r = vrec['r']
                        selected = []
                        lower = False
                        for outside, scalar in ((s, mu), (ss, nu)):
                            k = tuple(sorted((d, *outside)))
                            om = recover(k, target(c, ys, zs, d, p, q, r, scalar))
                            selected.append({'K': k, 'mu': scalar, 'omega': om})
                            lower |= not all(om)
                        if lower:
                            counts['selected_lower_weight'] += 1
                            continue
                        assert vrec['mu'] not in (mu, nu)
                        bprime = tuple(sorted({shared, *residual}))
                        tail = tuple(x for x in H if x not in {1, d, *ys, *zs, *bprime})
                        assert len(tail) == 5 and set(w)-common <= set(tail)
                        records = mixed(c, ys, zs, d, w, p, q, r, bprime, tail)
                        mus = sorted({rec['mu'] for rec in records})
                        assert not set(mus) & {mu, nu, vrec['mu']}
                        cases.append({'Y': ys, 'Z': zs, 'd': d, 'W': w,
                                      'S': s, 'SS': ss, 'p_q_r': [p, q, r],
                                      'c': c, 'V': residual, 'V_recovery': vrec,
                                      'selected_recoveries': selected,
                                      'Bprime_minus_d': bprime, 'T0': tail,
                                      'mixed_supports_tested': 250,
                                      'mixed_records': records, 'mixed_mus': mus})
        if index % 1000 == 0:
            OUT.write_text(json.dumps({'complete': False, 'choices_done': index,
                                       'counters': counts, 'cases': cases}, separators=(',', ':'))+'\n')
            print(f'choices {index}/8190; full forced-V cases {len(cases)}; '
                  f'maximum mixed count {max((len(c["mixed_mus"]) for c in cases), default=0)}', flush=True)
    assert raw_pairs == 75600
    histogram = Counter(len(c['mixed_mus']) for c in cases)
    maximum = max(histogram, default=0)
    result = {'complete': True, 'source': SOURCE.name,
              'scope': {'h': 1, 'prime': P, 'H': H, 'all_labelings': True,
                        'two_d_and_forced_V_branch_only': True,
                        'E_exclusion_relaxed': True, 'required_mixed_count': 9},
              'counters': counts, 'cases': cases,
              'summary': {'Y_Z_choices': 8190, 'W_pair_presentations': raw_pairs,
                          'unique_pair_configurations': len(seen),
                          'full_forced_V_configurations': len(cases),
                          'mixed_support_tests': 250*len(cases),
                          'mixed_count_histogram': dict(sorted(histogram.items())),
                          'maximum_distinct_mixed_scalars': maximum,
                          'required_for_twelve': 9,
                          'all_admitted_eight_moments_verified': True,
                          'independent_completeness_check_pending': True,
                          'proves_uniform_eleven': False, 'failures': []}}
    OUT.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print(json.dumps(result['summary'], sort_keys=True))
    print(f'actual mixed maximum {maximum}; required 9; certificate {OUT}')


if __name__ == '__main__':
    main()
