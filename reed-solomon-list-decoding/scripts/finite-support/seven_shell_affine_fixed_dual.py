"""One approved affine-family test. Fraction certificates, unchanged L067 dual.

Reuses established input certificates and source beta formula. The complete
family domain, presentations, range identities and quadratic are saved before
the optimization attempt. No optimizer status is a mathematical certificate.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from verify_simultaneous_seven_shell import C, beta
from seven_distance_full_base_kernel import atoms, atom_orders, rref
from simultaneous_five_six_shell import solve

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'seven-shell-affine-fixed-dual-results.json'


def enc(x):
    if isinstance(x, F):
        return [x.numerator, x.denominator]
    if isinstance(x, dict):
        return {k: enc(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [enc(v) for v in x]
    return x


def av(x):
    return [F(x), F(0), F(0), F(0)]


def add(x, y, scale=F(1)):
    return [a+scale*b for a, b in zip(x, y)]


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), F(0))


def outer(x):
    return [[a*b for b in x] for a in x]


def matadd(x, y, scale=F(1)):
    return [add(a, b, scale) for a, b in zip(x, y)]


def interval(x, d=10**6):
    k = x.numerator*d//x.denominator
    return [str(F(k, d)), str(F(k+1, d))]


def main():
    paths = [ROOT/'simultaneous-shell-ordinary-scalars-results.json',
             ROOT/'seven-distance-full-base-kernel-results.json',
             ROOT/'simultaneous-seven-shell-results.json']
    old, col, fixed = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    out = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
           'checks': checks, 'failures': failures}

    def save(stage):
        out['stage'] = stage
        OUT.write_text(json.dumps(enc(out), indent=2)+'\n')

    check('input_failures', all(not d['failures'] for d in [old, col, fixed]))
    for k, d in enumerate([old, col, fixed]):
        check(f'input_hashes_{k}', all(hashlib.sha256((NB/p).read_bytes()).hexdigest() == h
              for p, h in d.get('source_hashes', d.get('input_hashes', {})).items()))
    pairs = [F(*x) for x in old['pairs_through_12']]
    p7 = pairs[7]
    check('normalization', F(*old['rho']) > 0 and p7 == F(3539, 248922676958508))
    cs = [F(*v) for v in col['affine']['intercept']]
    slopes = [[F(*v) for v in row] for row in col['affine']['slopes']]
    fs = [[v]+row for v, row in zip(cs, slopes)]
    check('parameter_indices', col['affine']['free_indices'] == [27, 33, 42])
    for row, rhs in zip(col['equations'], col['rhs']):
        got = [sum(F(*e)*f[k] for e, f in zip(row, fs)) for k in range(4)]
        check(f'original_kernel_equation_{len(checks)}', got == av(F(*rhs)))
    base = {tuple(row['type']): av(F(*row['y'])) for row in old['types']}
    column = []
    for row in col['column']:
        v = [p7*x for x in fs[row['variable']]] if row['kind'] == 'free' else av(F(*row['value']))
        column.append(v)
        if row['orbit'] != [0, 0, 0]:
            l, i, j = row['orbit']
            base[l, 7, i, j] = v
        if row['kind'] != 'free':
            check(f'fixed_nonnegative_{len(column)}', v[0] >= 0)

    # Canonical complete atom keys collect EVERY affine equality, before
    # checking whether these are identities on the single-column family.
    dictionary, equality_rows = {}, []
    for typ, value in base.items():
        key = min(map(tuple, atom_orders(atoms(*typ))))
        if key in dictionary:
            equality_rows.append(add(value, dictionary[key], -1))
        else:
            dictionary[key] = value
    records, free = [], []
    for l, m in [(5, 5), (5, 6), (6, 6), (5, 7), (6, 7), (7, 7)]:
        for i, j in it.product(range(l+1), repeat=2):
            typ = (l, m, i, j)
            orders = atom_orders(atoms(*typ))
            key = min(map(tuple, orders))
            assigned, presentations = [], []
            for aa in orders:
                ab, ac, bc = aa[4]+aa[5], aa[4]+aa[6], aa[2]+aa[6]
                check(f'valid_region_{len(checks)}', min(aa) >= 0 and sum(aa) == 1024
                      and all(sum(v for k, v in enumerate(aa) if k & bit) == 68 for bit in [1, 2, 4]))
                value, origin = None, None
                if 0 in [ab, ac, bc]:
                    value, origin = av(pairs[max(ab, ac, bc)]), 'Boolean'
                elif any(1 <= h <= 4 for h in [ab, ac, bc]):
                    value, origin = av(0), 'forbidden'
                else:
                    kk = (*sorted([ab, ac]), aa[4], aa[3])
                    if kk in base:
                        value, origin = base[kk], 'prescribed'
                if value is not None:
                    assigned.append(value)
                presentations.append({'atoms': aa, 'distances': [ab, ac, bc], 'origin': origin, 'affine': value})
            if key in dictionary:
                assigned.append(dictionary[key])
            if assigned:
                value = assigned[0]
                equality_rows.extend(add(v, value, -1) for v in assigned[1:])
                dictionary[key] = value
                base[typ] = value
            else:
                value = None
                check(f'free_new_only_{typ}', l == m == 7)
                free.append((7-i, 7-j))
            records.append({'type': typ, 'key': key, 'affine': value, 'presentations': presentations})
    eqs = sorted(set(tuple(r) for r in equality_rows if any(r)))
    check('no_additional_consistency_equalities', not eqs)
    free.sort()
    check('36_free_new', free == [(r, q) for r in range(8) for q in range(8) if r+q >= 7])
    out.update({'domain': {'nonnegative_free': fs, 'equality_rows': eqs,
                           'all_equality_residuals': equality_rows},
                'affine_column': column, 'records': records, 'free_new': free})
    save('domain_checked')
    print(f'Domain: {len(records)} types, {6*len(records)} presentations, {len(fs)} affine inequalities, additional equalities={len(eqs)}; failures={failures}', flush=True)
    if failures:
        return

    h = list(map(F, [1, F(20435,441), F(13481000,13671), F(2688040,217),
                     F(1307664259,13671), F(5294968393,13671), 0, 0]))
    k = [F(49,100880416043264), F(7665,38718903137024), F(17301,551968803584),
         F(5461349,2754064239872)]+[F(0)]*4
    dual = [x*y for x, y in it.product(h, k)]
    check('unchanged_dual', dual == [F(*v) for v in fixed['exact']['dual']])
    check('dual_nonnegative', all(x >= 0 for x in dual) and sum(x>0 for x in dual) == 24)
    sizes = {l: C(68,l)*C(956,l) for l in [5,6,7]}
    modes, total_cost, total_fixed = [], [[F(0)]*4 for _ in range(4)], av(0)
    w0 = -cs[4]/slopes[4][2]
    oldpoint = [F(1), F(0), F(0), w0]
    for a, b in it.product(range(8), repeat=2):
        idx = 8*a+b
        layers = [l for l in [5,6] if max(a,b) <= l]
        d7 = C(68-2*a,7-a)*C(956-2*b,7-b)

        def block(l, m):
            ans = av(0)
            for i, j in it.product(range(min(l,m)+1), repeat=2):
                ans = add(ans, base[min(l,m),max(l,m),i,j],
                          beta(68,l,m,a,i)*beta(956,l,m,b,j))
            if a == b == 0:
                ans[0] -= pairs[l]*pairs[m]*sizes[l]*sizes[m]
            return ans

        B = [[block(l,m)[0] for m in layers] for l in layers]
        cross = [block(l,7) for l in layers]
        check(f'old_base_{a}_{b}', B == [[F(*x) for x in row] for row in fixed['modes'][idx]['base']])
        check(f'old_cross_{a}_{b}', [dot(t,oldpoint) for t in cross] == [F(*v) for v in fixed['modes'][idx]['cross']])
        cost = [[F(0)]*4 for _ in range(4)]
        ranges, pivots = [], []
        if len(layers) == 2:
            x, off, z = B[0][0], B[0][1], B[1][1]
            u, v = cross
            pivots.append(x)
            if x > 0:
                cost = matadd(cost, outer(u), 1/x)
                z, v = z-off*off/x, add(v,u,-off/x)
            else:
                ranges.extend([u, av(off)])
        elif layers:
            z, v = B[0][0], cross[0]
        else:
            z, v = F(0), av(0)
        pivots.append(z)
        check(f'positive_old_pivots_{a}_{b}', all(x >= 0 for x in pivots))
        if z > 0:
            cost = matadd(cost, outer(v), 1/z)
        else:
            ranges.append(v)
        check(f'full_affine_range_{a}_{b}', all(not any(r) for r in ranges))
        cost = [[x/(p7*d7) for x in row] for row in cost]
        check(f'old_cost_{a}_{b}', dot(oldpoint,[dot(row,oldpoint) for row in cost]) == F(*fixed['modes'][idx]['required']))
        f = av(0)
        for r in range(8):
            for q in range(8-r):
                if r+q <= 6:
                    eigen_product = F(beta(68,7,7,a,7-r)*beta(956,7,7,b,7-q),d7)
                    f = add(f,base[7,7,7-r,7-q],eigen_product/p7)
        anchor = p7*sizes[7] if a == b == 0 else F(0)
        f[0] -= anchor
        total_fixed = add(total_fixed,f,dual[idx])
        total_cost = matadd(total_cost,cost,dual[idx])
        modes.append({'mode':[a,b], 'layers':layers, 'B':B, 'cross':cross,
                      'pivots':pivots, 'range_residuals':ranges, 'required_quadratic':cost,
                      'fixed_minus_anchor_affine':f, 'D7':d7})
    cancellations = []
    for r,q in free:
        value = sum(dual[8*a+b]*F(beta(68,7,7,a,7-r)*beta(956,7,7,b,7-q),
                     C(68-2*a,7-a)*C(956-2*b,7-b)) for a,b in it.product(range(8),repeat=2))
        cancellations.append(value)
    check('all_36_dual_cancellations', not any(cancellations))
    M = [[-x for x in row] for row in total_cost]
    M[0][0] += total_fixed[0]
    for j in range(1,4):
        M[0][j] += total_fixed[j]/2
        M[j][0] += total_fixed[j]/2
    original = dot(oldpoint,[dot(row,oldpoint) for row in M])
    check('original_fixed_dual_value', original == F(*fixed['exact']['fixed_value']))
    out.update({'modes':modes, 'dual':dual, 'cancellations':cancellations,
                'total_cost_quadratic':total_cost,'total_fixed_affine':total_fixed,
                'objective_matrix':M,'original_point':oldpoint,'original_value':original})
    save('quadratic_saved')
    print(f'All 64 affine ranges and 36 cancellations checked; original value in {interval(original)}; failures={failures}', flush=True)
    if failures:
        return
    H = [[-M[i][j] for j in range(1,4)] for i in range(1,4)]
    g = M[0][1:]
    try:
        stationary = solve(H,g)
    except ValueError:
        rr, piv, _ = rref([row+[v] for row,v in zip(H,g)])
        consistent = 3 not in piv
        nulls = []
        hr, hp, _ = rref(H)
        for j in range(3):
            if j not in hp:
                v = [F(int(k == j)) for k in range(3)]
                for i,k in enumerate(hp):
                    v[k] = -hr[i][j]
                nulls.append(v)
        out['singular_hessian'] = {'H':H,'g':g,'rref':hr,'pivots':hp,'nulls':nulls,
                                   'linear_null_slopes':[dot(g,v) for v in nulls],
                                   'stationarity_consistent':consistent}
        save('singular_hessian_analyzed')
        print('Hessian rank:',len(hp),'stationarity consistent:',consistent,
              'linear null signs:',[int(dot(g,v)>0)-int(dot(g,v)<0) for v in nulls],flush=True)
        if not consistent:
            out['summary'] = {'checks':len(checks),'failures':len(failures),
                              'verdict':'UNRESOLVED_LINEAR_NULL_DIRECTION'}
            save('completed')
            print('Linear null direction: domain-constrained calculation required; certificate:',OUT.relative_to(NB))
            return
        stationary = [F(0)]*3
        for i,j in enumerate(piv):
            stationary[j] = rr[i][-1]
    point = [F(1)]+stationary
    value = dot(point,[dot(row,point) for row in M])
    signs = [dot(f,point) for f in fs]
    # Exact positive-pivot square decomposition, permitting zero coordinates
    # before the first positive pivot. A zero diagonal alone is not a stop.
    schur = [row[:] for row in H]
    ld_pivots, square_factors = [], []
    for _ in range(3):
        j = next((j for j in range(3) if schur[j][j] > 0), None)
        if j is None:
            break
        pivot = schur[j][j]
        v = [row[j] for row in schur]
        ld_pivots.append(pivot)
        square_factors.append({'pivot_coordinate':j,'pivot':pivot,'vector':v})
        schur = matadd(schur,outer(v),-1/pivot)
    check('hessian_positive_semidefinite', all(x == 0 for row in schur for x in row))
    check('stationarity', all(dot(row,stationary) == v for row,v in zip(H,g)))
    check('completed_square_constant', value == M[0][0]+dot(g,stationary))
    verdict = 'UNIFORM_STRICTLY_NEGATIVE' if value < 0 else ('ADMISSIBLE_NONNEGATIVE' if min(signs) >= 0 else 'UNRESOLVED_CONSTRAINED')
    out['optimization'] = {'H':H,'g':g,'positive_pivots':ld_pivots,'square_factors':square_factors,
                           'stationary':stationary,'value':value,'free_values':signs,
                           'verdict':verdict,'value_interval':interval(value)}
    out['summary'] = {'checks':len(checks),'failures':len(failures),'verdict':verdict,
                      'value_interval':interval(value),'required_sign':'<0 throughout domain',
                      'value_exactly_zero':value == 0,'positive_free_coordinates':sum(x>0 for x in signs),
                      'zero_free_coordinates':[j for j,x in enumerate(signs) if x == 0],
                      'stationary_parameters_nonzero':[j for j,x in enumerate(stationary) if x],
                      'stationary_negative_coordinates':[j for j,x in enumerate(signs) if x<0]}
    save('completed')
    print(f'{verdict}: unconstrained upper value in {interval(value)}, exactly_zero={value == 0}; stationary nonnegative={sum(x>=0 for x in signs)}/49; checks={len(checks)}; failures={failures}')
    print('Certificate:',OUT.relative_to(NB))


if __name__ == '__main__':
    main()
