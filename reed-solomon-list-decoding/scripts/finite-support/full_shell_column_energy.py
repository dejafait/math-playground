"""L059 whole-interval generalized-Schur energy, exact rational arithmetic.

Uses audited affine input; reconstructs all relation quotients and verifies
inverse action in the orbit-size inner product. Writes full certificates.
"""
import hashlib
import json
import re
from fractions import Fraction as F
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'full-shell-column-energy-results.json'


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]


def bound(x, scale=10**6):
    low = x.numerator*scale//x.denominator
    return [enc(F(low, scale)), enc(F(low+1, scale))]


def main():
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    shell = NB / 'lemmas/L056-released-zero-five-shell-nonexclusion.md'
    original = ROOT / 'full-shell-nullspace-results.json'
    verification = ROOT / 'full-shell-nullspace-verification.json'
    source = json.loads(original.read_text())
    verified = json.loads(verification.read_text())
    check('prior_certificates_pass', not source['failures'] and not verified['failures'])
    check('unchanged_shell_hash', source['input_sha256'] == hashlib.sha256(shell.read_bytes()).hexdigest())
    z = {(int(r), int(q)): F(v) for r, q, v in re.findall(
        r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', shell.read_text(), re.M)}
    check('complete_shell_domain', set(z) == {(r, q) for r in range(6) for q in range(6) if r+q >= 5})
    d = {(r, q): val/(c(5, r)*c(63, r)*c(5, q)*c(951, q)) for (r, q), val in z.items()}
    d[0, 0] = F(1)
    p5, p6 = F(1, 68881143660), F(133, 9357995374380)
    check('unchanged_pairs', verified['p5'] == enc(p5) and verified['p6'] == enc(p6) and 0 < p5 and 0 < p6 < 1)
    factors = {}
    for n, key in [(68, 'head'), (956, 'tail')]:
        weights = [c(6, i)*c(n-6, 5-i) for i in range(6)]
        quotients = [[[sum(c(i, u)*c(6-i, j-u)*c(5-i, 5-r-u)*c(n-11+i, r+u-j)
                           for u in range(6)) for j in range(6)] for i in range(6)] for r in range(6)]
        vectors, norms, eigenvalues = [], [], []
        Q = quotients[1]
        check(f'weights_{n}', weights == source[key]['weights'] and all(w > 0 for w in weights)
              and sum(weights) == c(n, 5))
        for a in range(6):
            theta = (5-a)*(n-5-a)-a
            v = [F(1)]
            for i in range(5):
                v.append(((theta-Q[i][i])*v[i]-(Q[i][i-1]*v[i-1] if i else 0))/Q[i][i+1])
            old = [F(*x) for x in source[key]['vectors'][a]]
            check(f'normalized_basis_{n}_{a}', v == [x/old[0] for x in old])
            for b in range(a):
                check(f'orthogonal_{n}_{a}_{b}', sum(weights[i]*v[i]*vectors[b][i] for i in range(6)) == 0)
            norm = sum(weights[i]*v[i]**2 for i in range(6))
            check(f'positive_norm_{n}_{a}', norm > 0)
            ev = []
            for r in range(6):
                value = sum((-1)**h*c(a, h)*c(5-a, r-h)*c(n-5-a, r-h) for h in range(r+1))
                ev.append(value)
                check(f'full_relation_action_{n}_{a}_{r}', all(
                    sum(quotients[r][i][j]*v[j] for j in range(6)) == value*v[i] for i in range(6)))
            vectors.append(v)
            norms.append(norm)
            eigenvalues.append(ev)
        factors[n] = (weights, vectors, norms, eigenvalues, quotients)
    wh, h, nh, eh, qh = factors[68]
    wt, k, nt, et, qt = factors[956]
    orbits = [(i, j) for i in range(6) for j in range(6)]
    W = [wh[i]*wt[j] for i, j in orbits]
    S = sum(W)
    # Q is the ACTUAL action on orbit-constant functions, not a symmetric
    # matrix in the unweighted Euclidean inner product.
    R = [[sum(value*qh[r][i][ip]*qt[q][j][jp] for (r, q), value in d.items())-p5*W[col]
          for col, (ip, jp) in enumerate(orbits)] for i, j in orbits]
    for row in range(36):
        check(f'weighted_self_adjoint_{row}', all(W[row]*R[row][col] == W[col]*R[col][row] for col in range(36)))
    affine = source['nonnegative_test']
    free = [tuple(x) for x in source['free']]
    check('complete_column_partition', set(free) == {ij for ij in orbits if sum(ij) <= 5}
          and len(source['fixed']) == 5 and len(source['forbidden']) == 10)
    intercept = dict(zip(free, [F(*x) for x in affine['intercept']]))
    slope = dict(zip(free, [F(*x) for x in affine['slope']]))
    for i, j in orbits:
        if i+j == 6:
            intercept[i, j], slope[i, j] = d[6-i, i], F(0)
        elif i+j >= 7:
            intercept[i, j], slope[i, j] = F(0), F(0)
    for fixed in source['fixed']:
        ij = (fixed['i'], fixed['j'])
        check(f'represented_entry_{ij}', intercept[ij] == F(*fixed['value']) and slope[ij] == 0)
    lo, hi = F(*affine['maximum_lower']), F(*affine['minimum_upper'])
    check('complete_interval', affine['parameter_coordinate'] == [2, 3] and affine['feasible']
          and not affine['constant_negative_coordinates'] and lo <= hi
          and intercept[2, 3] == 0 and slope[2, 3] == 1)
    actual_lower, actual_upper = [], []
    for i, j in free:
        v, s = intercept[i, j], slope[i, j]
        if s > 0:
            actual_lower.append(-v/s)
        elif s < 0:
            actual_upper.append(-v/s)
        else:
            check(f'constant_nonnegative_{i}_{j}', v >= 0)
        check(f'nonnegative_both_endpoints_{i}_{j}', v+s*lo >= 0 and v+s*hi >= 0)
    check('exact_interval_exhaustion', max(actual_lower) == lo and min(actual_upper) == hi)
    v0, v1 = [intercept[ij]-p6 for ij in orbits], [slope[ij] for ij in orbits]
    mode_records = []
    inverse0, inverse1 = [F(0)]*36, [F(0)]*36
    A, B, C = F(0), F(0), p6*p6
    for a in range(6):
        for b in range(6):
            H = [h[a][i]*k[b][j] for i, j in orbits]
            norm = nh[a]*nt[b]
            val = sum(value*eh[a][r]*et[b][q] for (r, q), value in d.items())
            if (a, b) == (0, 0):
                val -= p5*S
            check(f'saved_spectrum_{a}_{b}', enc(val) == source['modes'][6*a+b]['schur'] and val >= 0)
            check(f'compressed_mode_action_{a}_{b}', all(
                sum(R[row][col]*H[col] for col in range(36)) == val*H[row] for row in range(36)))
            f0 = sum(w*x*y for w, x, y in zip(W, v0, H))
            f1 = sum(w*x*y for w, x, y in zip(W, v1, H))
            check(f'product_norm_{a}_{b}', norm == sum(w*x*x for w, x in zip(W, H)))
            if val == 0:
                check(f'whole_affine_kernel_{a}_{b}', f0 == 0 and f1 == 0)
                terms = [F(0)]*3
            else:
                terms = [p5*f1*f1/(norm*val), 2*p5*f0*f1/(norm*val), p5*f0*f0/(norm*val)]
                A += terms[0]
                B += terms[1]
                C += terms[2]
                for row in range(36):
                    inverse0[row] += f0*H[row]/(norm*val)
                    inverse1[row] += f1*H[row]/(norm*val)
            mode_records.append({'a': a, 'b': b, 'eigenvalue': enc(val), 'norm': enc(norm),
                                 'projection_intercept': enc(f0), 'projection_slope': enc(f1),
                                 'energy_coefficients_ABC': list(map(enc, terms))})
    residuals = []
    for row in range(36):
        r0 = sum(R[row][col]*inverse0[col] for col in range(36))-v0[row]
        r1 = sum(R[row][col]*inverse1[col] for col in range(36))-v1[row]
        check(f'inverse_residual_{row}', r0 == 0 and r1 == 0)
        residuals.append([enc(r0), enc(r1)])
    check('inverse_energy_coefficients',
          A == p5*sum(w*x*y for w, x, y in zip(W, v1, inverse1))
          and B == p5*sum(w*(x*y+u*v) for w, x, y, u, v in zip(W, v0, inverse1, v1, inverse0))
          and C == p6*p6+p5*sum(w*x*y for w, x, y in zip(W, v0, inverse0)))
    check('nonnegative_curvature', A >= 0)
    stationary = -B/(2*A) if A else None
    if A:
        minimizer = max(lo, min(hi, stationary))
    else:
        minimizer = lo if B >= 0 else hi
    def energy(s):
        return A*s*s+B*s+C
    minimum = energy(minimizer)
    derivative = 2*A*minimizer+B
    check('optimality_whole_interval', lo <= minimizer <= hi
          and derivative*(lo-minimizer) >= 0 and derivative*(hi-minimizer) >= 0)
    check('endpoint_energy_comparisons', minimum <= energy(lo) and minimum <= energy(hi))
    check('minimum_column_nonnegative', all(intercept[ij]+slope[ij]*minimizer >= 0 for ij in orbits))
    ratio = minimum/p6
    passing = minimum <= p6
    certificate = {
        'source_hashes': {str(path.relative_to(NB)): hashlib.sha256(path.read_bytes()).hexdigest()
                          for path in [shell, original, verification]},
        'pairs': {'p5': enc(p5), 'p6': enc(p6)}, 'weights': W, 'shell_size': S,
        'column_affine': [{'i': i, 'j': j, 'intercept': enc(intercept[i, j]), 'slope': enc(slope[i, j])}
                          for i, j in orbits],
        'factors': {str(n): {'weights': factors[n][0], 'vectors': [list(map(enc, v)) for v in factors[n][1]],
                            'norms': list(map(enc, factors[n][2])), 'eigenvalues': factors[n][3],
                            'quotients': factors[n][4]} for n in factors},
        'weighted_shell_action': [list(map(enc, row)) for row in R], 'modes': mode_records,
        'inverse_action': {'intercept': list(map(enc, inverse0)), 'slope': list(map(enc, inverse1)),
                           'residuals': residuals},
        'quadratic_ABC': list(map(enc, [A, B, C])),
        'optimization': {'lower': enc(lo), 'upper': enc(hi), 'stationary': enc(stationary) if stationary is not None else None,
                         'minimizer': enc(minimizer), 'derivative': enc(derivative),
                         'endpoint_energies': list(map(enc, [energy(lo), energy(hi)])), 'minimum_energy': enc(minimum),
                         'required_diagonal': enc(p6), 'diagonal_minus_minimum': enc(p6-minimum),
                         'energy_over_diagonal': enc(ratio), 'ratio_bounds': bound(ratio), 'passes': passing,
                         'minimizing_column': [{'i': i, 'j': j, 'value': enc(intercept[i, j]+slope[i, j]*minimizer)}
                                               for i, j in orbits]},
        'checks': len(checks), 'failures': failures}
    OUT.write_text(json.dumps(certificate, indent=2)+'\n')
    print(f'checks={len(checks)}; failures={failures}; certificate={OUT.relative_to(NB)}')
    print(f'curvature positive={A > 0}; stationary in interval={stationary is not None and lo <= stationary <= hi}; '
          f'minimum at lower={minimizer == lo}; minimum at upper={minimizer == hi}')
    bounds = bound(ratio)
    print(f'minimum/required diagonal in [{F(*bounds[0])},{F(*bounds[1])}); PSD energy passes={passing}; required diagonal={p6}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
