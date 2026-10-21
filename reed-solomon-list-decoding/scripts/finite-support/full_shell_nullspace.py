"""Approved full-shell/one distance-six column test, exact arithmetic only.

Writes complete quotient bases, equations and elimination certificate.
No external packages or notebook mathematical modules are imported.
"""
import hashlib
import json
import re
from fractions import Fraction as F
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'full-shell-nullspace-results.json'


def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]


def main():
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    path = NB / 'lemmas/L056-released-zero-five-shell-nonexclusion.md'
    manuscript = path.read_text()
    z = {(int(r), int(q)): F(v) for r, q, v in re.findall(
        r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', manuscript, re.M)}
    d = {(r, q): v / (comb(5, r)*comb(63, r)*comb(5, q)*comb(951, q))
         for (r, q), v in z.items()}
    d[0, 0] = F(1)
    check('all_21_free_shell_coefficients', len(z) == 21)

    def E(n, a, r):
        def c(n, k):
            return comb(n, k) if 0 <= k <= n else 0
        return sum((-1)**h*c(a, h)*c(5-a, r-h)*c(n-5-a, r-h)
                   for h in range(r+1))

    p5 = F(1, 68881143660)
    modes = []
    for a in range(6):
        for b in range(6):
            val = sum(v*E(68, a, r)*E(956, b, q) for (r, q), v in d.items())
            if (a, b) == (0, 0):
                val -= p5*comb(68, 5)*comb(956, 5)
            modes.append({'a': a, 'b': b, 'schur': enc(val)})
            check(f'schur_nonnegative_{a}_{b}', val >= 0)
    zeros = [(v['a'], v['b']) for v in modes if v['schur'][0] == 0]
    check('positive_constant_schur', modes[0]['schur'][0] > 0)

    def basis(n):
        weights = [comb(6, i)*comb(n-6, 5-i) for i in range(6)]
        vectors = []
        quotient = []
        for i in range(6):
            down, up = i*(n-11+i), (5-i)*(6-i)
            row = [0]*6
            row[i] = 5*(n-5)-down-up
            if i:
                row[i-1] = down
            if i < 5:
                row[i+1] = up
            quotient.append(row)
        for a in range(6):
            v = [F(i**a) for i in range(6)]
            for h in vectors:
                c = sum(w*x*y for w, x, y in zip(weights, v, h)) / sum(
                    w*x*x for w, x in zip(weights, h))
                v = [x-c*y for x, y in zip(v, h)]
            theta = (5-a)*(n-5-a)-a
            check(f'quotient_eigenvector_{n}_{a}', all(
                sum(quotient[i][j]*v[j] for j in range(6)) == theta*v[i]
                for i in range(6)))
            check(f'nonzero_basis_{n}_{a}', any(v))
            vectors.append(v)
        check(f'weight_sum_{n}', sum(weights) == comb(n, 5))
        for a in range(6):
            for b in range(a):
                check(f'orthogonality_{n}_{a}_{b}', sum(
                    weights[i]*vectors[a][i]*vectors[b][i] for i in range(6)) == 0)
        return weights, vectors, quotient

    wh, h, qh = basis(68)
    wt, k, qt = basis(956)
    free = [(i, j) for i in range(6) for j in range(6) if i+j <= 5]
    fixed = {(i, 6-i): d[6-i, i] for i in range(1, 6)}
    forbidden = [(i, j) for i in range(6) for j in range(6) if i+j >= 7]
    check('36_orbits_exhausted', len(free)+len(fixed)+len(forbidden) == 36)
    # Exact full point representatives verify the claimed distance and anchor rule.
    D, U, V = set(range(68)), set(range(6)), set(range(68, 74))
    G = (D-U)|V
    orbit_records = []
    for i in range(6):
        for j in range(6):
            X = set(range(i)) | set(range(6, 11-i))
            Y = set(range(68, 68+j)) | set(range(74, 79-j))
            Eset = (D-X)|Y
            check(f'distances_{i}_{j}', len(D-Eset) == 5 and len(D-G) == 6
                  and len(Eset-G) == 11-i-j and len(Eset) == 68)
            atoms = [sum(1 for point in range(1024)
                         if (4*(point in D)+2*(point in Eset)+(point in G)) == mask)
                     for mask in range(8)]
            if i+j == 6:
                # Eset is the unique distance-five anchor.
                r = 5-len((Eset-D) & (Eset-G))
                q = 5-len((D-Eset) & (G-Eset))
                check(f'reanchored_relation_{i}_{j}', (r, q) == (6-i, i))
                # L056 common, private and pair-only atom formula at that anchor.
                ordered = [len(Eset-(D|G)), len((Eset&G)-D), len((Eset&D)-G),
                           len(Eset&D&G), len((D&G)-Eset), len(D-(Eset|G)),
                           len(G-(Eset|D)), 1024-len(Eset|D|G)]
                check(f'reanchored_atoms_{i}_{j}', ordered ==
                      [5-r, r, r, 63-r, 5-q, q, q, 951-q])
            orbit_records.append({'i': i, 'j': j, 'atoms': atoms,
                                  'multiplicity': wh[i]*wt[j]})
    A, rhs = [], []
    for a, b in zeros:
        def coeff(i, j):
            return wh[i]*wt[j]*h[a][i]*k[b][j]
        A.append([coeff(i, j) for i, j in free])
        rhs.append(-sum(coeff(i, j)*v for (i, j), v in fixed.items()))
    m, n = len(A), len(free)
    augmented = [row+[rhs[i]] for i, row in enumerate(A)]
    transform = [[F(int(i == j)) for j in range(m)] for i in range(m)]
    pivots = []
    row = 0
    for col in range(n):
        pivot = next((r for r in range(row, m) if augmented[r][col]), None)
        if pivot is None:
            continue
        augmented[row], augmented[pivot] = augmented[pivot], augmented[row]
        transform[row], transform[pivot] = transform[pivot], transform[row]
        scale = augmented[row][col]
        augmented[row] = [v/scale for v in augmented[row]]
        transform[row] = [v/scale for v in transform[row]]
        for r in range(m):
            if r != row:
                scale = augmented[r][col]
                if scale:
                    augmented[r] = [x-scale*y for x, y in zip(augmented[r], augmented[row])]
                    transform[r] = [x-scale*y for x, y in zip(transform[r], transform[row])]
        pivots.append(col)
        row += 1
        if row == m:
            break
    inconsistent = [r for r in range(m) if not any(augmented[r][:n]) and augmented[r][n]]
    for r in range(m):
        check(f'elimination_row_{r}', all(
            sum(transform[r][s]*A[s][j] for s in range(m)) == augmented[r][j]
            for j in range(n)) and sum(transform[r][s]*rhs[s] for s in range(m)) == augmented[r][n])
    data = {'input_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'modes': modes, 'zero_modes': zeros,
            'head': {'weights': wh, 'vectors': [list(map(enc, v)) for v in h], 'quotient': qh},
            'tail': {'weights': wt, 'vectors': [list(map(enc, v)) for v in k], 'quotient': qt},
            'orbits': orbit_records, 'free': free,
            'fixed': [{'i': i, 'j': j, 'value': enc(v)} for (i, j), v in fixed.items()],
            'forbidden': forbidden,
            'equations': {'matrix': [list(map(enc, r)) for r in A], 'rhs': list(map(enc, rhs))},
            'elimination': {'rank': len(pivots), 'pivots': pivots,
                            'rref': [list(map(enc, r)) for r in augmented],
                            'transform': [list(map(enc, r)) for r in transform],
                            'inconsistent_rows': inconsistent},
            'checks': len(checks), 'failures': failures}
    nonpivots = [j for j in range(n) if j not in pivots]
    if not inconsistent and len(nonpivots) == 1:
        parameter = nonpivots[0]
        intercept, slope = [F(0)]*n, [F(0)]*n
        slope[parameter] = F(1)
        for r, j in enumerate(pivots):
            intercept[j], slope[j] = augmented[r][n], -augmented[r][parameter]
        lower, upper, constant_bad = [], [], []
        for j, (v, s) in enumerate(zip(intercept, slope)):
            if s > 0:
                lower.append((-v/s, j))
            elif s < 0:
                upper.append((-v/s, j))
            elif v < 0:
                constant_bad.append(j)
        lo, hi = max(lower), min(upper) if upper else None
        feasible = not constant_bad and (hi is None or lo[0] <= hi[0])
        data['nonnegative_test'] = {
            'parameter_coordinate': free[parameter], 'intercept': list(map(enc, intercept)),
            'slope': list(map(enc, slope)),
            'lower_bounds': [{'value': enc(v), 'coordinate': free[j]} for v, j in lower],
            'upper_bounds': [{'value': enc(v), 'coordinate': free[j]} for v, j in upper],
            'constant_negative_coordinates': [free[j] for j in constant_bad],
            'maximum_lower': enc(lo[0]), 'minimum_upper': enc(hi[0]) if hi else None,
            'feasible': feasible}
        if feasible:
            parameter_value = lo[0]
            solution = [v+s*parameter_value for v, s in zip(intercept, slope)]
            check('solution_nonnegative', all(v >= 0 for v in solution))
            for r in range(m):
                check(f'full_kernel_equation_{r}', sum(A[r][j]*solution[j]
                                                       for j in range(n)) == rhs[r])
            data['nonnegative_test']['solution'] = list(map(enc, solution))
        data['checks'], data['failures'] = len(checks), failures
        print(f'nonnegative feasible={feasible}; lower={lo[0]} at {free[lo[1]]}; '
              f'upper={hi[0] if hi else None} at {free[hi[1]] if hi else None}; constant failures={constant_bad}')
    OUT.write_text(json.dumps(data, indent=2)+'\n')
    print(f'zero modes={m}; free coordinates={n}; equation rank={len(pivots)}; inconsistent rows={inconsistent}')
    print(f'checks={len(checks)}; failures={failures}; certificate={OUT.relative_to(NB)}')
    if not inconsistent and len(nonpivots) != 1:
        print('Linear equations consistent; nonnegative feasibility still untested.')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
