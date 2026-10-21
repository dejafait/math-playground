"""Fixed L066 columns, joint ordinary moment/PSD test. Exact certificates only."""
import hashlib
import itertools as it
import json
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

from simultaneous_five_six_shell import c, enc, eigen, beta, propose, solve
from seven_distance_full_base_kernel import atoms, atom_orders

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'simultaneous-seven-shell-results.json'
beta = lru_cache(None)(beta)
eigen = lru_cache(None)(eigen)


def main():
    paths = [ROOT/'simultaneous-shell-ordinary-scalars-results.json',
             ROOT/'seven-distance-full-base-kernel-results.json',
             ROOT/'seven-distance-fixed-column-energy-results.json']
    old, col, energy = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    check('prior_failures', all(not x['failures'] for x in [old, col, energy]))
    for x in [old, col, energy]:
        check('prior_hashes_'+str(len(checks)), all(
            hashlib.sha256((NB/p).read_bytes()).hexdigest() == h
            for p, h in x.get('source_hashes', x.get('input_hashes')).items()))
    p = [F(*v) for v in old['pairs_through_12']]
    check('rho_and_p7', F(*old['rho']) > 0 and p[7] == F(3539, 248922676958508))
    base = {tuple(row['type']): F(*row['y']) for row in old['types']}
    intercept = [F(*v) for v in col['affine']['intercept']]
    slopes = [[F(*v) for v in row] for row in col['affine']['slopes']]
    w = -intercept[4]/slopes[4][2]
    f = [x+w*s[2] for x, s in zip(intercept, slopes)]
    check('fixed_parameters', col['affine']['free_indices'] == [27, 33, 42]
          and col['chosen_parameters'] == [enc(0), enc(0), enc(w)])
    column = [p[7]*f[row['variable']] if row['kind'] == 'free'
              else F(*row['value']) for row in col['column']]
    check('whole_immutable_column', list(map(enc, column)) == col['complete_column'])
    for row, y in zip(col['column'][1:], column[1:]):
        l, i, j = row['orbit']
        base[l, 7, i, j] = y

    # First exhaust every presentation of the immutable entries.
    dictionary, collisions = {}, []
    for (l, m, i, j), y in base.items():
        key = min(map(tuple, atom_orders(atoms(l, m, i, j))))
        if key in dictionary and dictionary[key] != y:
            collisions.append([l, m, i, j])
        dictionary[key] = y
    records, free = [], []
    for l, m in [(5, 5), (5, 6), (6, 6), (5, 7), (6, 7), (7, 7)]:
        for i, j in it.product(range(l+1), repeat=2):
            aa = atoms(l, m, i, j)
            orders = atom_orders(aa)
            key = min(map(tuple, orders))
            assigned, details = [], []
            for perm in orders:
                ab, ac, bc = perm[4]+perm[5], perm[4]+perm[6], perm[2]+perm[6]
                check('region_'+str(len(checks)), min(perm) >= 0 and sum(perm) == 1024
                      and all(sum(v for k, v in enumerate(perm) if k & bit) == 68 for bit in [1, 2, 4]))
                y, origin = None, None
                if 0 in [ab, ac, bc]:
                    y, origin = p[max(ab, ac, bc)], 'Boolean'
                elif any(1 <= h <= 4 for h in [ab, ac, bc]):
                    y, origin = F(0), 'forbidden'
                else:
                    kk = (*sorted([ab, ac]), perm[4], perm[3])
                    if kk in base:
                        y, origin = base[kk], 'immutable'
                if y is not None:
                    assigned.append(y)
                details.append({'atoms': perm, 'distances': [ab, ac, bc],
                                'origin': origin, 'value': enc(y) if y is not None else None})
            if key in dictionary:
                assigned.append(dictionary[key])
            check('consistent_'+str((l, m, i, j)), len(set(assigned)) <= 1)
            if assigned:
                y = assigned[0]
                dictionary[key] = y
                base[l, m, i, j] = y
                check('nonnegative_'+str((l, m, i, j)), y >= 0)
            else:
                y = None
                check('only_new_free_'+str((l, m, i, j)), l == m == 7)
                free.append((7-i, 7-j))
            records.append({'type': [l, m, i, j], 'key': list(key),
                            'presentations': details, 'value': enc(y) if y is not None else None})
    free.sort()
    check('no_immutable_collisions', not collisions)
    check('free_36', free == [(r, q) for r in range(8) for q in range(8) if r+q >= 7])
    out = {'source_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
           'rho': old['rho'], 'p7': enc(p[7]), 'records': records, 'free': free,
           'checks': checks, 'failures': failures, 'stage': 'consistency_checked'}
    OUT.write_text(json.dumps(out, indent=2)+'\n')
    print(f'Consistency: {len(records)} types, {len(records)*6} presentations; {len(free)} free; failures={failures}', flush=True)
    if failures:
        return

    sizes = {l: c(68, l)*c(956, l) for l in [5, 6, 7]}
    A, rhs, modes = [], [], []
    for a, b in it.product(range(8), repeat=2):
        layers = [l for l in [5, 6] if a <= l and b <= l]
        D7 = c(68-2*a, 7-a)*c(956-2*b, 7-b)

        def block(l, m):
            ans = sum(beta(68, l, m, a, i)*beta(956, l, m, b, j)*base[l, m, i, j]
                      for i, j in it.product(range(l+1), repeat=2))
            return ans-p[l]*p[m]*sizes[l]*sizes[m] if a == b == 0 else ans

        B = [[block(min(l, m), max(l, m)) for m in layers] for l in layers]
        cross = [block(l, 7) for l in layers]
        # Explicit singular elimination on the old block and the entire cross.
        pivots, transformed, cost = [], [], F(0)
        if len(layers) == 2:
            x, t, z = B[0][0], B[0][1], B[1][1]
            u, v = cross
            check(f'old_pivot_{a}_{b}', x >= 0)
            if x:
                cost += u*u/x
                z, v = z-t*t/x, v-t*u/x
            else:
                check(f'old_zero_{a}_{b}', t == u == 0)
            pivots.append(x)
            transformed.append(u)
        elif len(layers) == 1:
            z, v = B[0][0], cross[0]
        else:
            z, v = F(0), F(0)
        check(f'old_last_pivot_{a}_{b}', z >= 0)
        if z:
            cost += v*v/z
        else:
            check(f'last_kernel_{a}_{b}', v == 0)
        if layers:
            pivots.append(z)
            transformed.append(v)
        required = cost/(p[7]*D7)
        fixed = sum(base[7, 7, i, j]/p[7]*eigen(68, 7, a, 7-i)*eigen(956, 7, b, 7-j)
                    for i, j in it.product(range(8), repeat=2) if (7, 7, i, j) in base)
        anchor = p[7]*sizes[7] if a == b == 0 else F(0)
        H = [F(eigen(68, 7, a, r)*eigen(956, 7, b, q),
               c(7, r)*c(61, r)*c(7, q)*c(949, q)) for r, q in free]
        A.append([-h for h in H])
        bound = fixed-anchor-required
        rhs.append(bound)
        modes.append({'mode': [a, b], 'layers': layers, 'base': [list(map(enc, row)) for row in B],
                      'cross': list(map(enc, cross)), 'pivots': list(map(enc, pivots)),
                      'transformed_cross': list(map(enc, transformed)), 'D7': D7,
                      'required': enc(required), 'fixed': enc(fixed), 'anchor': enc(anchor)})
    multiplicity = lambda a, b: (c(68, a)-c(68, a-1))*(c(956, b)-c(956, b-1))
    for l in [5, 6, 7]:
        check(f'full_dimension_{l}', sum(multiplicity(a, b) for a, b in it.product(range(l+1), repeat=2)) == sizes[l])
    trace = p[7]**2+p[7]*sum(multiplicity(*row['mode'])*F(*row['required']) for row in modes)/sizes[7]
    check('L066_complete_energy_trace', trace == F(*energy['summary']['energy']))
    out.update({'stage': 'exact_system_saved', 'modes': modes, 'matrix': [list(map(enc, row)) for row in A],
                'rhs': list(map(enc, rhs)), 'trace_energy': enc(trace)})
    OUT.write_text(json.dumps(out, indent=2)+'\n')
    print(f'Full modes={len(modes)}/64; energy trace agrees={enc(trace)==energy["summary"]["energy"]}; failures={failures}', flush=True)
    if failures:
        return
    discovery = propose(A, rhs)
    out['discovery'] = discovery
    OUT.write_text(json.dumps(out, indent=2)+'\n')
    n, m = len(free), len(modes)
    basis = discovery['basis']
    rows = [i for i in range(m) if n+i not in basis]
    columns = sorted(j for j in basis if j < n)
    exact, verdict = {}, 'UNRESOLVED'
    if discovery['status'] == 'feasible_proposal' and -1 not in columns:
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
    elif discovery['status'] == 'infeasible_proposal' and -1 in columns:
        matrix = [[F(-1) if j == -1 else A[i][j] for j in columns] for i in rows]
        costs = [F(-1) if j == -1 else F(0) for j in columns]
        ys = solve(list(map(list, zip(*matrix))), costs)
        y = [F(0)]*m
        for i, v in zip(rows, ys):
            y[i] = v
        sums = [sum(y[i]*A[i][j] for i in range(m)) for j in range(n)]
        value = sum(v*b for v, b in zip(y, rhs))
        valid = all(v >= 0 for v in y+sums) and value < 0
        exact = {'kind': 'FARKAS', 'active_rows': rows, 'active_columns': columns,
                 'dual': list(map(enc, y)), 'column_sums': list(map(enc, sums)),
                 'fixed_value': enc(value), 'valid': valid}
        if valid:
            verdict = 'EXCLUDED'
    out.update({'stage': 'completed', 'exact': exact, 'summary': {'verdict': verdict,
                'checks': len(checks), 'failures': len(failures), 'types': len(records),
                'modes': len(modes), 'free': len(free)}})
    OUT.write_text(json.dumps(out, indent=2)+'\n')
    print(f'Exact verdict={verdict}; {exact.get("kind")}; valid={exact.get("valid")}; failures={failures}')
    if exact.get('kind') == 'PRIMAL':
        print(f'Nonnegative variables={sum(v>=0 for v in x)}/{n}; remainders={sum(v>=0 for v in slacks)}/{m}; zero remainders={sum(v==0 for v in slacks)}')
    elif exact.get('kind') == 'FARKAS':
        k = value.numerator*10**6//value.denominator
        print(f'Fixed dual value in [{F(k, 10**6)},{F(k+1, 10**6)}); required >=0; nonnegative weights={sum(v>=0 for v in y)}/{m}; canceled columns={sum(v==0 for v in sums)}/{n}')
    print('Certificate:', OUT.relative_to(NB))


if __name__ == '__main__':
    main()
