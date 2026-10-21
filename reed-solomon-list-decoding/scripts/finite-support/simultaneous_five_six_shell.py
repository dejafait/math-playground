"""Approved fixed simultaneous-shell test; Decimal proposes, Fraction certifies.

Complete anchor-presentation and beta-block reconstruction. No mathematical
verdict is inferred from simplex status. All exact evidence is written to disk.
"""
import hashlib
import itertools
import json
import re
from decimal import Decimal, localcontext
from fractions import Fraction as F
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'simultaneous-five-six-shell-results.json'


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]


def solve(matrix, rhs):
    n = len(rhs)
    a = [[F(x) for x in row]+[F(b)] for row, b in zip(matrix, rhs)]
    for k in range(n):
        p = next((r for r in range(k, n) if a[r][k]), None)
        if p is None:
            raise ValueError('singular proposed basis')
        a[k], a[p] = a[p], a[k]
        v = a[k][k]
        a[k] = [x/v for x in a[k]]
        for r in range(k+1, n):
            v = a[r][k]
            if v:
                a[r] = [x-v*y for x, y in zip(a[r], a[k])]
    x = [F(0)]*n
    for k in reversed(range(n)):
        x[k] = a[k][-1]-sum(a[k][j]*x[j] for j in range(k+1, n))
    return x


def beta(n, i, j, k, t):
    # Terms with u>min(i,j) vanish; k<=u<=n-k remains enforced.
    return sum((-1)**(u-t)*c(u, t)*c(n-2*k, u-k)
               *c(n-k-u, i-u)*c(n-k-u, j-u)
               for u in range(max(k, t), min(i, j, n-k)+1))


def eigen(n, layer, a, r):
    return sum((-1)**h*c(a, h)*c(layer-a, r-h)*c(n-layer-a, r-h)
               for h in range(r+1))


def propose(A, rhs):
    """Phase I with one artificial column -1, then zero objective.

    This is basis discovery only. Certificate validation below reconstructs
    every retained inequality with exact arithmetic.
    """
    m, n = len(rhs), len(A[0])
    with localcontext() as ctx:
        ctx.prec = 180
        dec = lambda x: Decimal(x.numerator)/Decimal(x.denominator)
        D = [[dec(x) for x in row]+[Decimal(-1), dec(b)] for row, b in zip(A, rhs)]
        D += [[Decimal(0)]*(n+2), [Decimal(0)]*n+[Decimal(1), Decimal(0)]]
        B, N = list(range(n, n+m)), list(range(n))+[-1]
        eps = Decimal('1e-135')
        trace = []

        def pivot(r, s):
            inv = 1/D[r][s]
            for i in range(m+2):
                if i != r:
                    for j in range(n+2):
                        if j != s:
                            D[i][j] -= D[r][j]*D[i][s]*inv
            for j in range(n+2):
                if j != s:
                    D[r][j] *= inv
            for i in range(m+2):
                if i != r:
                    D[i][s] *= -inv
            D[r][s] = inv
            trace.append({'enter': N[s], 'leave': B[r], 'row': r})
            B[r], N[s] = N[s], B[r]

        def optimize(phase):
            obj = m+1 if phase == 1 else m
            for iteration in range(1000):
                options = [j for j in range(n+1) if phase == 1 or N[j] != -1]
                s = min(options, key=lambda j: (D[obj][j], N[j]))
                if D[obj][s] >= -eps:
                    return 'optimal'
                rows = [i for i in range(m) if D[i][s] > eps]
                if not rows:
                    return 'unbounded_or_scaling_failure'
                r = min(rows, key=lambda i: (D[i][-1]/D[i][s], B[i]))
                pivot(r, s)
            return 'iteration_limit'

        r = min(range(m), key=lambda i: D[i][-1])
        status = 'feasible_proposal'
        if D[r][-1] < -eps:
            pivot(r, n)
            status = optimize(1)
            if status == 'optimal' and D[m+1][-1] < -eps:
                status = 'infeasible_proposal'
            elif status == 'optimal':
                status = 'feasible_proposal'
                if -1 in B:
                    r = B.index(-1)
                    options = [j for j in range(n+1) if abs(D[r][j]) > eps and N[j] != -1]
                    if options:
                        pivot(r, min(options, key=lambda j: N[j]))
        return {'status': status, 'basis': B, 'trace': trace,
                'phase_one_value': str(D[m+1][-1])}


def main():
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    paths = [NB / 'lemmas/L056-released-zero-five-shell-nonexclusion.md',
             ROOT / 'full-shell-column-energy-results.json',
             ROOT / 'full-shell-column-energy-critical-audit.json']
    shelltext = paths[0].read_text()
    energy, audit = [json.loads(p.read_text()) for p in paths[1:]]
    check('prior_complete_energy_certificates', energy['failures'] == [] and audit['failures'] == [])
    check('unchanged_energy_inputs', all(hashlib.sha256((NB/name).read_bytes()).hexdigest() == h
                                       for name, h in energy['source_hashes'].items()))
    p5, p6 = F(1, 68881143660), F(133, 9357995374380)
    check('fixed_positive_pairs', energy['pairs'] == {'p5': enc(p5), 'p6': enc(p6)} and p5 > 0 and p6 > 0)
    z5 = {(int(r), int(q)): F(x) for r, q, x in re.findall(
        r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', shelltext, re.M)}
    check('five_shell_complete_coefficients', set(z5) == {(r, q) for r in range(6) for q in range(6) if r+q >= 5})
    d5 = {(r, q): x/(c(5, r)*c(63, r)*c(5, q)*c(951, q)) for (r, q), x in z5.items()}
    d5[0, 0] = F(1)
    t = {(row['i'], row['j']): F(*row['value']) for row in energy['optimization']['minimizing_column']}
    star = F(*energy['optimization']['minimizer'])
    for row in energy['column_affine']:
        check(f'minimizing_column_{row["i"]}_{row["j"]}',
              t[row['i'], row['j']] == F(*row['intercept'])+star*F(*row['slope']))
    fixed6 = {(r, 5-r): (p5/p6)*t[5-r, r] for r in range(6)}
    free6 = [(r, q) for r in range(7) for q in range(7) if r+q >= 6]
    check('six_shell_partition', len(free6) == 28 and len(fixed6) == 6)

    # All relation types in all three blocks, with every anchor ordering.
    Dset = set(range(68))
    records, presentations, collisions = [], 0, []
    orbit_values = {}
    for l, m in [(5, 5), (5, 6), (6, 6)]:
        U, V = set(range(m)), set(range(68, 68+m))
        G = (Dset-U)|V
        for i, j in itertools.product(range(min(l, m)+1), repeat=2):
            X = set(range(i))|set(range(m, m+l-i))
            Y = set(range(68, 68+j))|set(range(68+m, 68+m+l-j))
            E = (Dset-X)|Y
            supports = [Dset, E, G]
            check(f'point_cardinalities_{l}_{m}_{i}_{j}', all(len(s) == 68 for s in supports))
            assigned = []
            details = []
            for order in itertools.permutations(range(3)):
                A, B, C = [supports[h] for h in order]
                ab, ac, bc = len(A-B), len(A-C), len(B-C)
                value = None
                origin = None
                if len({frozenset(s) for s in [A, B, C]}) == 2:
                    distance = max(ab, ac, bc)
                    value, origin = {5: p5, 6: p6}[distance], 'Boolean_pair'
                elif any(1 <= h <= 4 for h in [ab, ac, bc]):
                    value, origin = F(0), 'forbidden'
                elif ab == ac == 5:
                    r = 5-len((A-B)&(A-C))
                    q = 5-len((B-A)&(C-A))
                    value, origin = p5*d5.get((r, q), F(0)), 'L056'
                elif sorted([ab, ac]) == [5, 6]:
                    B5, C6 = (B, C) if ab == 5 else (C, B)
                    ii = len((A-B5)&(A-C6))
                    jj = len((B5-A)&(C6-A))
                    value, origin = p5*t[ii, jj], 'L060'
                if value is not None:
                    assigned.append(value)
                    presentations += 1
                atoms = [sum(1 for h in range(1024) if
                             4*(h in A)+2*(h in B)+(h in C) == mask) for mask in range(8)]
                details.append({'order': list(order), 'atoms': atoms,
                                'distances': [ab, ac, bc], 'origin': origin,
                                'value': enc(value) if value is not None else None})
            check(f'anchor_consistency_{l}_{m}_{i}_{j}', len(set(assigned)) <= 1)
            # Canonical full-region orbit key, modulo all support permutations.
            key = min(tuple(row['atoms']) for row in details)
            if assigned:
                if key in orbit_values and orbit_values[key] != assigned[0]:
                    collisions.append([l, m, i, j])
                orbit_values[key] = assigned[0]
            expected = None
            if (l, m) == (5, 5):
                expected = p5*d5.get((5-i, 5-j), F(0))
            elif (l, m) == (5, 6):
                expected = p5*t[i, j]
            elif (i, j) == (6, 6):
                expected = p6
            elif 1 <= 12-i-j <= 4:
                expected = F(0)
            elif 12-i-j == 5:
                expected = p6*fixed6[6-i, 6-j]
            check(f'prescribed_dictionary_{l}_{m}_{i}_{j}',
                  (expected is None and not assigned) or
                  (expected is not None and assigned and all(x == expected for x in assigned)))
            records.append({'layers': [l, m], 'intersections': [i, j],
                            'presentations': details, 'value': enc(expected) if expected is not None else None})
    check('no_cross_relation_conflict', not collisions)

    # Exact source beta blocks after eliminating the positive anchor.
    S5, S6 = c(68, 5)*c(956, 5), c(68, 6)*c(956, 6)
    modes, A, rhs = [], [], []
    for a, b in itertools.product(range(7), repeat=2):
        D6 = c(68-2*a, 6-a)*c(956-2*b, 6-b)
        check(f'positive_six_rescaling_{a}_{b}', D6 > 0)
        C55, C56, required = F(0), F(0), F(0)
        if a <= 5 and b <= 5:
            D5 = c(68-2*a, 5-a)*c(956-2*b, 5-b)
            for n, k in [(68, a), (956, b)]:
                for r in range(6):
                    check(f'beta_five_norm_{a}_{b}_{n}_{r}',
                          beta(n, 5, 5, k, 5-r) == c(n-2*k, 5-k)*eigen(n, 5, k, r))
            lam = sum(x*eigen(68, 5, a, r)*eigen(956, 5, b, q) for (r, q), x in d5.items())
            if (a, b) == (0, 0):
                lam -= p5*S5
            C55 = p5*D5*lam
            check(f'known_five_spectrum_{a}_{b}', enc(lam) == energy['modes'][6*a+b]['eigenvalue'] and lam >= 0)
            C56 = p5*sum(beta(68, 5, 6, a, i)*beta(956, 5, 6, b, j)*x for (i, j), x in t.items())
            if (a, b) == (0, 0):
                C56 -= p5*p6*S5*S6
            if C55 == 0:
                check(f'complete_cross_range_{a}_{b}', C56 == 0)
            else:
                required = C56*C56/C55/(p6*D6)
        H = {(r, q): F(eigen(68, 6, a, r)*eigen(956, 6, b, q),
                            c(6, r)*c(62, r)*c(6, q)*c(950, q))
             for r, q in free6+list(fixed6)}
        for n, k in [(68, a), (956, b)]:
            for r in range(7):
                check(f'beta_six_norm_{a}_{b}_{n}_{r}',
                      beta(n, 6, 6, k, 6-r) == c(n-2*k, 6-k)*eigen(n, 6, k, r))
        fixed_contribution = sum(fixed6[r, q]*eigen(68, 6, a, r)*eigen(956, 6, b, q) for r, q in fixed6)
        anchor = p6*S6 if (a, b) == (0, 0) else F(0)
        bound = 1+fixed_contribution-anchor-required
        A.append([-H[r, q] for r, q in free6])
        rhs.append(bound)
        modes.append({'a': a, 'b': b, 'five_block': enc(C55), 'cross_block': enc(C56),
                      'six_rescaling': D6, 'coupling_requirement': enc(required),
                      'anchor_correction': enc(anchor), 'fixed_contribution': enc(fixed_contribution),
                      'rhs': enc(bound)})
    mh = [c(68, a)-c(68, a-1) for a in range(7)]
    mt = [c(956, b)-c(956, b-1) for b in range(7)]
    check('complete_six_space_dimension', sum(x*y for x in mh for y in mt) == S6)
    check('complete_five_space_dimension', sum(x*y for x in mh[:6] for y in mt[:6]) == S5)
    check('all_mode_multiplicities_positive', all(x > 0 for x in mh+mt))
    # Independent normalization check against every audited one-column
    # projection. Transitivity makes each mode's energy its trace/S6.
    for row in modes:
        a, b = row['a'], row['b']
        if a <= 5 and b <= 5:
            old = energy['modes'][6*a+b]
            lam, norm = F(*old['eigenvalue']), F(*old['norm'])
            projection = F(*old['projection_intercept'])+star*F(*old['projection_slope'])
            contribution = p5*projection*projection/(norm*lam) if lam else F(0)
            check(f'cross_normalization_energy_{a}_{b}', contribution ==
                  p6*mh[a]*mt[b]*F(*row['coupling_requirement'])/S6)
    check('complete_energy_trace', p6*p6+p6*sum(
        mh[row['a']]*mt[row['b']]*F(*row['coupling_requirement']) for row in modes)/S6
        == F(*energy['optimization']['minimum_energy']))
    discovery = propose(A, rhs) if not failures else {'status': 'input_failure', 'basis': [], 'trace': []}
    exact = {}
    verdict = 'UNRESOLVED'
    n, m = len(free6), len(modes)
    if discovery['basis']:
        basis = discovery['basis']
        rows = [i for i in range(m) if n+i not in basis]
        columns = sorted(j for j in basis if j < n)
        if discovery['status'] == 'infeasible_proposal' and -1 in columns:
            matrix = [[F(-1) if j == -1 else A[i][j] for j in columns] for i in rows]
            costs = [F(-1) if j == -1 else F(0) for j in columns]
            ys = solve(list(map(list, zip(*matrix))), costs)
            y = [F(0)]*m
            for i, x in zip(rows, ys):
                y[i] = x
            sums = [sum(y[i]*A[i][j] for i in range(m)) for j in range(n)]
            value = sum(x*b for x, b in zip(y, rhs))
            valid = all(x >= 0 for x in y+sums) and value < 0
            exact = {'kind': 'FARKAS', 'active_rows': rows, 'active_columns': columns,
                     'dual': list(map(enc, y)), 'column_sums': list(map(enc, sums)),
                     'fixed_value': enc(value), 'valid': valid}
            if valid:
                verdict = 'EXCLUDED'
        elif discovery['status'] == 'feasible_proposal' and -1 not in columns:
            xs = solve([[A[i][j] for j in columns] for i in rows], [rhs[i] for i in rows])
            x = [F(0)]*n
            for j, v in zip(columns, xs):
                x[j] = v
            slacks = [b-sum(v*w for v, w in zip(row, x)) for row, b in zip(A, rhs)]
            valid = all(v >= 0 for v in x+slacks)
            exact = {'kind': 'PRIMAL', 'active_rows': rows, 'active_columns': columns,
                     'z': list(map(enc, x)), 'slacks': list(map(enc, slacks)), 'valid': valid}
            if valid:
                verdict = 'FEASIBLE'
    result = {'source_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'pairs': {'p5': enc(p5), 'p6': enc(p6)}, 'minimizer': enc(star),
              'presentations': records, 'prescribed_orbit_count': len(orbit_values),
              'presentation_count': presentations, 'collisions': collisions,
              'six_shell': {'size': S6, 'free_relations': free6,
                            'fixed_coefficients': [{'r': r, 'q': q, 'value': enc(v)} for (r, q), v in fixed6.items()]},
              'modes': modes, 'matrix': [list(map(enc, row)) for row in A], 'rhs': list(map(enc, rhs)),
              'discovery': discovery, 'exact': exact,
              'summary': {'checks': len(checks), 'fixed_consistency': not collisions and
                          not any('consistency' in x or 'dictionary' in x for x in failures),
                          'verdict': verdict}, 'check_names': checks, 'failures': failures}
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(f'checks={len(checks)}; implementation/input failures={failures}; full certificate={OUT.relative_to(NB)}')
    print(f'presentation types={len(records)}, prescribed presentations={presentations}; conflicts={len(collisions)}')
    print(f'complete modes={m}/49; nonnegative free coordinates={n}/28; discovery={discovery["status"]}; pivots={len(discovery["trace"])}')
    print(f'exact verdict={verdict}; exact certificate kind={exact.get("kind")}; certified={exact.get("valid", False)}')
    if exact.get('kind') == 'FARKAS':
        value = F(*exact['fixed_value'])
        k = value.numerator*10**6//value.denominator
        print(f'exact dual value in [{F(k, 10**6)},{F(k+1, 10**6)}); required >=0')
    if exact.get('kind') == 'PRIMAL':
        print(f'exact nonnegative variables/slacks={sum(F(*v)>=0 for v in exact["z"])}/28,{sum(F(*v)>=0 for v in exact["slacks"])}/49; required=28,49')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
