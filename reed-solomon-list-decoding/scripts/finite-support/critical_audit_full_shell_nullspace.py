"""L059 critical audit: complete exact evidence, no energy calculation.

Direct intersection counts reconstruct every Johnson relation quotient.
No notebook mathematical modules or numerical packages are imported.
"""
import hashlib
import json
import re
from fractions import Fraction as F
from itertools import permutations
from math import comb, factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'full-shell-nullspace-critical-audit-results.json'


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]


def main():
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    shell = NB / 'lemmas/L056-released-zero-five-shell-nonexclusion.md'
    column = NB / 'lemmas/L059-full-shell-nullspace-compatible-column.md'
    cert = ROOT / 'full-shell-nullspace-results.json'
    previous = ROOT / 'full-shell-nullspace-verification.json'
    saved = json.loads(cert.read_text())
    old = json.loads(previous.read_text())
    pattern = r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$'
    z = {(int(r), int(q)): F(v) for r, q, v in re.findall(pattern, shell.read_text(), re.M)}
    t = {(int(i), int(j)): F(v) for i, j, v in re.findall(pattern, column.read_text(), re.M)}
    free = [(i, j) for i in range(6) for j in range(6) if i+j <= 5]
    forbidden = [(i, j) for i in range(6) for j in range(6) if i+j >= 7]
    check('z_domain', set(z) == {(r, q) for r in range(6) for q in range(6) if r+q >= 5})
    check('manuscript_free_domain', set(t) == set(free))
    check('saved_free_domain_order', saved['free'] == list(map(list, free)))
    check('saved_forbidden_domain_order', saved['forbidden'] == list(map(list, forbidden)))
    d = {(r, q): v/(c(5, r)*c(63, r)*c(5, q)*c(951, q)) for (r, q), v in z.items()}
    p5, p6 = F(1, 68881143660), F(133, 9357995374380)
    check('previous_fixed_pairs', old['p5'] == enc(p5) and old['p6'] == enc(p6))
    check('previous_verification_pass', old['checks'] == 342 and old['failures'] == [])
    check('constructor_pass', saved['checks'] == 182 and saved['failures'] == [])
    factors = {}
    for n, key in [(68, 'head'), (956, 'tail')]:
        w = [c(6, i)*c(n-6, 5-i) for i in range(6)]
        # Select X' from the four regions cut out by X and the six-set U.
        quotients = [[[sum(c(i, u)*c(6-i, j-u)*c(5-i, 5-r-u)
                          *c(n-11+i, r+u-j) for u in range(6))
                       for j in range(6)] for i in range(6)] for r in range(6)]
        vectors, eigs = [], []
        Q = quotients[1]
        check(f'weights_{n}', w == saved[key]['weights'] and all(v > 0 for v in w)
              and sum(w) == c(n, 5))
        check(f'distance_one_quotient_{n}', Q == saved[key]['quotient'])
        for r in range(6):
            for i in range(6):
                check(f'quotient_rowsum_{n}_{r}_{i}', sum(quotients[r][i]) == c(5, r)*c(n-5, r))
                for j in range(6):
                    check(f'quotient_balance_{n}_{r}_{i}_{j}',
                          w[i]*quotients[r][i][j] == w[j]*quotients[r][j][i])
        for a in range(6):
            theta = (5-a)*(n-5-a)-a
            v = [F(1)]
            for i in range(5):
                v.append(((theta-Q[i][i])*v[i]-(Q[i][i-1]*v[i-1] if i else 0))/Q[i][i+1])
            leading = sum((-1)**(a-u)*c(a, u)*v[u] for u in range(a+1))/factorial(a)
            check(f'nonzero_leading_{n}_{a}', leading != 0)
            v = [x/leading for x in v]
            check(f'saved_monic_vector_{n}_{a}', list(map(enc, v)) == saved[key]['vectors'][a])
            check(f'previous_recurrence_vector_{n}_{a}',
                  [enc(x/v[0]) for x in v] == old[key+'_vectors'][a])
            for b in range(a):
                check(f'orthogonal_{n}_{a}_{b}', sum(w[i]*v[i]*vectors[b][i] for i in range(6)) == 0)
            norm = sum(w[i]*v[i]**2 for i in range(6))
            check(f'positive_norm_{n}_{a}', norm > 0)
            ev = []
            for r in range(6):
                lam = sum(quotients[r][0][j]*v[j] for j in range(6))/v[0]
                ev.append(lam)
                for i in range(6):
                    check(f'full_relation_eigenvector_{n}_{a}_{r}_{i}',
                          sum(quotients[r][i][j]*v[j] for j in range(6)) == lam*v[i])
            check(f'johnson_mode_{n}_{a}', ev[1] == theta)
            vectors.append(v)
            eigs.append(ev)
        factors[n] = {'weights': w, 'vectors': vectors, 'eigenvalues': eigs, 'quotients': quotients}

    wh, wt = factors[68]['weights'], factors[956]['weights']
    h, k = factors[68]['vectors'], factors[956]['vectors']
    ground = set(range(1024))
    D = set(range(68))
    G = (D-set(range(6))) | set(range(68, 74))
    region_records, fixed = [], {}
    check('saved_orbit_domain', [(v['i'], v['j']) for v in saved['orbits']] ==
          [(i, j) for i in range(6) for j in range(6)])
    for i in range(6):
        for j in range(6):
            X = set(range(i)) | set(range(6, 11-i))
            Y = set(range(68, 68+j)) | set(range(74, 79-j))
            E = (D-X) | Y
            supports = [D, E, G]
            check(f'actual_sizes_distances_{i}_{j}', len(X) == len(Y) == 5
                  and all(len(s) == 68 for s in supports)
                  and [len(D-E), len(D-G), len(E-G)] == [5, 6, 11-i-j])
            atoms = [sum(sum((1 << (2-a)) for a in range(3) if x in supports[a]) == mask
                         for x in ground) for mask in range(8)]
            check(f'saved_atoms_{i}_{j}', saved['orbits'][6*i+j] ==
                  {'i': i, 'j': j, 'atoms': atoms, 'multiplicity': wh[i]*wt[j]})
            eligible = [a for a in range(3) if all(len(supports[a]-supports[b]) == 5
                                                  for b in range(3) if b != a)]
            check(f'eligible_anchors_{i}_{j}', eligible == ([1] if i+j == 6 else []))
            perms = []
            for perm in permutations(range(3)):
                A, B, C = [supports[a] for a in perm]
                regions = [len(A-(B|C)), len((A&C)-B), len((A&B)-C), len(A&B&C),
                           len((B&C)-A), len(B-(A|C)), len(C-(A|B)), len(ground-(A|B|C))]
                represented = len(A-B) == len(A-C) == 5
                record = {'permutation': list(perm), 'regions': regions, 'represented': represented}
                if represented:
                    r = 5-len((A-B)&(A-C))
                    q = 5-len((B-A)&(C-A))
                    check(f'full_dictionary_{i}_{j}_{perm}', regions ==
                          [5-r, r, r, 63-r, 5-q, q, q, 951-q] and (r, q) == (6-i, i))
                    fixed[i, j] = d[r, q]
                    record.update({'relation': [r, q], 'value': enc(d[r, q])})
                perms.append(record)
            if i+j > 6:
                t[i, j] = F(0)
            elif i+j == 6:
                t[i, j] = fixed[i, j]
            check(f'column_nonnegative_{i}_{j}', t[i, j] >= 0)
            region_records.append({'i': i, 'j': j, 'atoms': atoms, 'permutations': perms})
    check('fixed_five_entries', len(fixed) == 5 and saved['fixed'] ==
          [{'i': i, 'j': j, 'value': enc(v)} for (i, j), v in fixed.items()])
    check('previous_all_column_values', old['column'] ==
          [{'i': i, 'j': j, 'value': enc(t[i, j])} for i in range(6) for j in range(6)])
    modes, zeros = [], []
    for a in range(6):
        for b in range(6):
            schur = 1+sum(v*factors[68]['eigenvalues'][a][r]*factors[956]['eigenvalues'][b][q]
                          for (r, q), v in d.items())
            if (a, b) == (0, 0):
                schur -= p5*c(68, 5)*c(956, 5)
            projection = sum(wh[i]*wt[j]*h[a][i]*k[b][j]*t[i, j]
                             for i in range(6) for j in range(6))
            shift = p6*sum(wh[i]*h[a][i] for i in range(6))*sum(wt[j]*k[b][j] for j in range(6))
            check(f'saved_spectrum_{a}_{b}', saved['modes'][6*a+b] ==
                  {'a': a, 'b': b, 'schur': enc(schur)} and schur >= 0)
            prior = old['projections'][6*a+b]
            scale = h[a][0]*k[b][0]
            check(f'previous_full_projection_{a}_{b}', prior == {'a': a, 'b': b,
                  'schur': enc(schur), 'raw': enc(projection/scale),
                  'transported': enc((projection-shift)/scale)})
            if schur == 0:
                zeros.append((a, b))
                check(f'kernel_raw_and_transported_{a}_{b}', projection == shift == 0)
            modes.append({'a': a, 'b': b, 'schur': enc(schur), 'raw': enc(projection),
                          'transported': enc(projection-shift)})
    check('constant_schur', modes[0]['schur'] == enc(F(4982733184, 5)))
    zero_text = column.read_text().split('for (a,b) in\n', 1)[1].split('This is L056', 1)[0]
    manuscript_zeros = [(int(a), int(b)) for a, b in re.findall(r'\((\d),(\d)\)', zero_text)]
    check('complete_zero_table', len(zeros) == 20 and zeros == manuscript_zeros
          and list(map(list, zeros)) == saved['zero_modes'] == old['zero_modes'])

    A, rhs = [], []
    for row, (a, b) in enumerate(zeros):
        def coeff(i, j):
            return wh[i]*wt[j]*h[a][i]*k[b][j]
        A.append([coeff(i, j) for i, j in free])
        rhs.append(-sum(coeff(i, j)*v for (i, j), v in fixed.items()))
        check(f'saved_entire_equation_{row}', list(map(enc, A[-1])) == saved['equations']['matrix'][row]
              and enc(rhs[-1]) == saved['equations']['rhs'][row])
    T = [[F(*v) for v in row] for row in saved['elimination']['transform']]
    R = [[F(*v) for v in row] for row in saved['elimination']['rref']]
    pivots = saved['elimination']['pivots']
    check('elimination_dimensions', len(T) == len(R) == 20 and all(len(r) == 20 for r in T)
          and all(len(r) == 22 for r in R))
    check('rank_pivot_count', saved['elimination']['rank'] == len(pivots) == 20
          and pivots == sorted(set(pivots)) and all(0 <= j < 21 for j in pivots)
          and saved['elimination']['inconsistent_rows'] == [])
    residuals = []
    for row in range(20):
        residual = [sum(T[row][s]*(A[s][j] if j < 21 else rhs[s]) for s in range(20))-R[row][j]
                    for j in range(22)]
        residuals.append(list(map(enc, residual)))
        for j, value in enumerate(residual):
            check(f'complete_elimination_identity_{row}_{j}', value == 0)
        for s, pivot in enumerate(pivots):
            check(f'identity_pivot_minor_{row}_{s}', R[row][pivot] == int(row == s))
    # T A has a 20-by-20 identity minor: rank(A)=20, without assuming T invertible.
    nonpivots = [j for j in range(21) if j not in pivots]
    check('unique_parameter', len(nonpivots) == 1 and free[nonpivots[0]] == (2, 3))
    parameter = nonpivots[0]
    intercept, slope = [F(0)]*21, [F(0)]*21
    slope[parameter] = F(1)
    for row, pivot in enumerate(pivots):
        intercept[pivot], slope[pivot] = R[row][-1], -R[row][parameter]
    test = saved['nonnegative_test']
    check('full_affine_data', test['parameter_coordinate'] == [2, 3]
          and test['intercept'] == list(map(enc, intercept)) and test['slope'] == list(map(enc, slope)))
    for row in range(20):
        check(f'affine_system_constant_{row}', sum(A[row][j]*intercept[j] for j in range(21)) == rhs[row])
        check(f'affine_system_slope_{row}', sum(A[row][j]*slope[j] for j in range(21)) == 0)
    lower, upper, bad, bounds = [], [], [], []
    for j, (v, s) in enumerate(zip(intercept, slope)):
        bound = None if s == 0 else -v/s
        kind = 'lower' if s > 0 else 'upper' if s < 0 else 'constant'
        if s > 0:
            lower.append((bound, free[j]))
        elif s < 0:
            upper.append((bound, free[j]))
        elif v < 0:
            bad.append(list(free[j]))
        bounds.append({'coordinate': list(free[j]), 'intercept': enc(v), 'slope': enc(s),
                       'kind': kind, 'bound': None if bound is None else enc(bound)})
    lo, hi = max(v for v, _ in lower), min(v for v, _ in upper)
    check('complete_interval_lists', test['lower_bounds'] ==
          [{'value': enc(v), 'coordinate': list(coord)} for v, coord in lower]
          and test['upper_bounds'] == [{'value': enc(v), 'coordinate': list(coord)} for v, coord in upper]
          and test['constant_negative_coordinates'] == bad == [])
    check('nonempty_interval', 0 < lo < hi and test['feasible'] is True
          and test['maximum_lower'] == enc(lo) and test['minimum_upper'] == enc(hi))
    check('active_endpoints', [coord for v, coord in lower if v == lo] == [(0, 3)]
          and [coord for v, coord in upper if v == hi] == [(0, 2)])
    interval_text = column.read_text().split('interval with lower and upper endpoints respectively', 1)[1]
    interval_fractions = re.findall(r'\d+/\d+', interval_text)[:2]
    check('manuscript_endpoints', list(map(F, interval_fractions)) == [lo, hi])
    for j, coord in enumerate(free):
        lv, hv = intercept[j]+slope[j]*lo, intercept[j]+slope[j]*hi
        check(f'both_endpoint_signs_{coord}', lv >= 0 and hv >= 0)
        check(f'complete_selected_solution_{coord}', t[coord] == lv and test['solution'][j] == enc(lv))
        bounds[j].update({'lower_endpoint_value': enc(lv), 'upper_endpoint_value': enc(hv)})
    output = {'checks': len(checks), 'check_names': checks, 'failures': failures,
              'factors': {str(n): {'weights': f['weights'], 'quotients': f['quotients'],
                                   'vectors': [list(map(enc, v)) for v in f['vectors']],
                                   'eigenvalues': [list(map(enc, v)) for v in f['eigenvalues']]}
                          for n, f in factors.items()},
              'all_regions': region_records, 'all_modes': modes,
              'equations': {'matrix': [list(map(enc, row)) for row in A], 'rhs': list(map(enc, rhs))},
              'elimination_residuals': residuals, 'all_coordinate_bounds': bounds,
              'summary': {'orbits': 36, 'free': 21, 'represented': 5, 'forbidden': 10,
                          'zero_modes': len(zeros), 'rank': len(pivots),
                          'interval': [enc(lo), enc(hi)], 'energy_tested': False},
              'source_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest()
                                for p in [shell, column, cert, previous, Path(__file__)]}}
    OUT.write_text(json.dumps(output, indent=2)+'\n')
    print(f'checks={len(checks)}; failures={failures}; orbits=36/36; kernel equations=20/20; rank=20/20')
    print(f'parameter bounds: actual [{lo}, {hi}]; required lower <= upper; all coordinates nonnegative')
    print(f'certificate={OUT.relative_to(NB)}; energy NOT TESTED')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
