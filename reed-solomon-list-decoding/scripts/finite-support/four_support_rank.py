"""Exact signed four-support diagnostic; run from the notebook directory."""
import json
from itertools import combinations
from pathlib import Path

P = 65537
EDGES = list(combinations(range(4), 2))
OUT = Path(__file__).with_name('four-support-rank-results.json')
failures = []


def check(ok, name):
    if not ok:
        failures.append(name)


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j] + x*y) % P
    return c


def roots_poly(points):
    a = [1]
    for x in points:
        a = mul(a, [-x % P, 1])
    return a


def ev(a, x):
    v = 0
    for c in reversed(a):
        v = (v*x+c) % P
    return v


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) % P
             for col in zip(*b)] for row in a]


def reduction(a):
    r = [row[:] for row in a]
    nr, nc = len(r), len(r[0])
    t = [[int(i == j) for j in range(nr)] for i in range(nr)]
    pivots, ops = [], []
    for c in range(nc):
        j = next((j for j in range(len(pivots), nr) if r[j][c]), None)
        if j is None:
            continue
        i = len(pivots)
        if i != j:
            r[i], r[j] = r[j], r[i]
            t[i], t[j] = t[j], t[i]
            ops.append(['swap', i, j])
        u = pow(r[i][c], -1, P)
        r[i] = [x*u % P for x in r[i]]
        t[i] = [x*u % P for x in t[i]]
        ops.append(['scale', i, u])
        for j in range(nr):
            if j != i and r[j][c]:
                v = -r[j][c] % P
                r[j] = [(x+v*y) % P for x, y in zip(r[j], r[i])]
                t[j] = [(x+v*y) % P for x, y in zip(t[j], t[i])]
                ops.append(['add', j, i, v])
        pivots.append(c)
    basis = []
    for c in range(nc):
        if c not in pivots:
            v = [0]*nc
            v[c] = 1
            for i, pc in enumerate(pivots):
                v[pc] = -r[i][c] % P
            basis.append(v)
    # Replay the invertible elementary operations separately on the input.
    replay = [row[:] for row in a]
    for op in ops:
        if op[0] == 'swap':
            _, i, j = op
            replay[i], replay[j] = replay[j], replay[i]
        elif op[0] == 'scale':
            _, i, u = op
            check(u != 0, 'noninvertible scale')
            replay[i] = [u*x % P for x in replay[i]]
        else:
            _, j, i, v = op
            replay[j] = [(x+v*y) % P for x, y in zip(replay[j], replay[i])]
    check(replay == r == mm(t, a), 'row-operation identity')
    check(all(r[i][c] == int(i == j) for j, c in enumerate(pivots)
              for i in range(nr)), 'pivot columns')
    check(all(not any(row) for row in r[len(pivots):]), 'zero tail')
    check(all(not any(sum(x*y for x, y in zip(row, v)) % P for row in a)
              for v in basis), 'kernel equality')
    check(len(basis) + len(pivots) == nc, 'rank nullity')
    return dict(rank=len(pivots), pivots=pivots, rref=r,
                transform=t, operations=ops, kernel_basis=basis)


def difference_matrix(i, j):
    d = [[0]*12 for _ in range(4)]
    for c in range(4):
        if i < 3:
            d[c][4*i+c] = 1
        if j < 3:
            d[c][4*j+c] = P-1
    return d


def run_case(kind, h, domain):
    pairs = [[pow(h, 2*r, P), pow(h, 2*r+1, P)] if kind == 'consecutive'
             else [pow(h, r, P), -pow(h, r, P) % P] for r in range(6)]
    used = {x for pair in pairs for x in pair}
    check(len(used) == 12 and used <= set(domain), kind+' pair points')
    remaining = [x for x in domain if x not in used]
    core = remaining[:60]
    private = [remaining[60+2*i:62+2*i] for i in range(4)]
    supports = [sorted(core + private[i] + [x for edge, pair in zip(EDGES, pairs)
                                           if i in edge for x in pair])
                for i in range(4)]
    check(all(len(set(s)) == 68 for s in supports), kind+' support sizes')
    for (i, j), pair in zip(EDGES, pairs):
        check(set(supports[i]) & set(supports[j]) == set(core+pair),
              kind+f' intersection {i}{j}')
    matrix = []
    maps = [difference_matrix(*edge) for edge in EDGES]
    for d, pair in zip(maps, pairs):
        for x in pair:
            matrix.append([sum(pow(x, c, P)*d[c][j] for c in range(4)) % P
                           for j in range(12)])
    red = reduction(matrix)
    basis = red['kernel_basis']
    augmented, restrictions = [], []
    for d in maps:
        augmented.append(reduction(matrix+d))
        restrictions.append([[sum(a*b for a, b in zip(row, v)) % P
                              for v in basis] for row in d])
    good = [any(any(row) for row in a) for a in restrictions]
    check(all(g == (r['rank'] > red['rank']) for g, r in zip(good, augmented)),
          kind+' six rank/noncontainment equivalences')
    result = dict(pairs=pairs, core=core, private=private, supports=supports,
                  matrix=matrix, reduction=red, difference_maps=maps,
                  augmented_reductions=augmented, kernel_restrictions=restrictions,
                  six_noncontainments=good, realizable=all(good), witness=None)
    if all(good):
        # A polynomial curve in kernel coordinates avoids six proper subspaces.
        bound = 6*(len(basis)-1)
        chosen = None
        for t in range(bound+1):
            v = [sum(pow(t, b, P)*basis[b][j] for b in range(len(basis))) % P
                 for j in range(12)]
            if all(any(sum(a*b for a, b in zip(row, v)) % P for row in d)
                   for d in maps):
                chosen = (t, v)
                break
        check(chosen is not None, kind+' scalar witness')
        t, v = chosen
        reduced = [v[4*i:4*i+4] for i in range(3)] + [[0]*4]
        g = roots_poly(core)
        messages = [mul(g, f) for f in reduced]
        check(all(len(f) <= 64 for f in messages), kind+' strict degree')
        vals = [[ev(f, x) for x in domain] for f in messages]
        center, owners = [], []
        for ix, x in enumerate(domain):
            at = [i for i in range(4) if x in supports[i]]
            y = vals[at[0]][ix] if at else 0
            check(all(vals[i][ix] == y for i in at), kind+' center overlap')
            center.append(y)
            owners.append(at)
        agreements = [[x for ix, x in enumerate(domain) if vals[i][ix] == center[ix]]
                      for i in range(4)]
        equality_sets = [[x for ix, x in enumerate(domain) if vals[i][ix] == vals[j][ix]]
                         for i, j in EDGES]
        check(all(set(s) <= set(a) for s, a in zip(supports, agreements)),
              kind+' selected agreements')
        check(all(len(a) <= 63 for a in equality_sets), kind+' six distinct messages')
        if kind == 'antipodal':
            check(all(set(a) == set(core+pair) for a, pair in zip(equality_sets, pairs)),
                  kind+' exact pair equality sets')
        result['witness'] = dict(curve_parameter=t, excluded_parameter_bound=bound,
                                 vector=v, reduced_messages=reduced, core_polynomial=g,
                                 messages=messages, evaluations=vals, center=center,
                                 center_owners=owners, agreements=agreements,
                                 pair_equality_sets=equality_sets)
    return result


def main():
    h = pow(3, 64, P)
    domain = [pow(h, i, P) for i in range(1024)]
    check(pow(h, 1024, P) == 1 and pow(h, 512, P) == P-1, 'generator order')
    check(len(set(domain)) == 1024, 'domain distinctness')
    cases = {kind: run_case(kind, h, domain) for kind in ['consecutive', 'antipodal']}
    summary = {kind: dict(rank=c['reduction']['rank'],
                          nullity=len(c['reduction']['kernel_basis']),
                          augmented_ranks=[r['rank'] for r in c['augmented_reductions']],
                          six_noncontainments=c['six_noncontainments'],
                          realizable=c['realizable'],
                          agreement_counts=([len(a) for a in c['witness']['agreements']]
                                            if c['witness'] else None))
               for kind, c in cases.items()}
    cert = dict(modulus=P, generator=h, generator_half_power=pow(h, 512, P),
                domain=domain, edges=EDGES, cases=cases, summary=summary,
                bounds=dict(realizable_requires_six_strict_rank_increases=True,
                            field_size=P, union_bound_requires_field_size_gt=6,
                            unsafe_threshold_numerator=P**28,
                            unsafe_threshold_denominator=2**128,
                            exhibited_distinct_messages=4,
                            list_upper_bound_claimed=False), failures=failures)
    OUT.write_text(json.dumps(cert, indent=2)+'\n')
    print(json.dumps(dict(summary=summary, failures=failures, certificate=str(OUT),
                          actual_field_size=P, required_field_size_gt=6)))
    assert not failures


if __name__ == '__main__':
    main()
