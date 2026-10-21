"""Step 200: complete exact L060 manuscript/certificate audit.

No notebook imports. Rebuilds quotient counts by enumerating four region
occupancies, bases by weighted Gram--Schmidt, and range inverses by spectral
projection. Checks every load-bearing field of both original certificates.
The full-space justification uses the separately audited L056/L059 inputs.
"""
import hashlib
import json
import re
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'full-shell-column-energy-critical-audit.json'


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]


def main():
    checks, failures = [], []

    def check(name, condition):
        checks.append(name)
        if not condition:
            failures.append(name)

    def read(name):
        return json.loads((ROOT / name).read_text())

    data = read('full-shell-column-energy-results.json')
    verified = read('full-shell-column-energy-verification.json')
    old = read('full-shell-nullspace-results.json')
    ms = (NB / 'lemmas/L060-full-shell-one-column-psd-extension.md').read_text()
    shell = (NB / 'lemmas/L056-released-zero-five-shell-nonexclusion.md').read_text()
    check('original_complete_failure_lists', data['failures'] == verified['failures'] == old['failures'] == [])
    check('original_check_counts', data['checks'] == 372 and verified['checks'] == 177)
    for path, digest in data['source_hashes'].items():
        check('source_hash_' + path, hashlib.sha256((NB / path).read_bytes()).hexdigest() == digest)
    check('verification_input_hash', verified['input_sha256'] == hashlib.sha256(
        (ROOT / 'full-shell-column-energy-results.json').read_bytes()).hexdigest())
    p5, p6 = F(1, 68881143660), F(133, 9357995374380)
    check('positive_pair_normalization', 0 < p5 < 1 and 0 < p6 < 1 and data['pairs'] == {'p5': enc(p5), 'p6': enc(p6)})
    check('manuscript_pairs', 'p_5=1/68881143660' in ms and 'p_6=133/9357995374380' in ms)
    z = {(int(r), int(q)): F(v) for r, q, v in re.findall(
        r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', shell, re.M)}
    check('complete_z_domain', set(z) == {(r, q) for r in range(6) for q in range(6) if r+q >= 5})
    d = {(r, q): z[r, q]/(c(5, r)*c(63, r)*c(5, q)*c(951, q)) for r, q in z}
    d[0, 0] = F(1)
    factors = {}
    factor_records = {}
    for n in [68, 956]:
        weights = [c(6, i)*c(n-6, 5-i) for i in range(6)]
        Q = [[[0]*6 for _ in range(6)] for _ in range(6)]
        # Choose X' in the four disjoint regions; infer the relation and
        # destination class only after the complete occupancy choice.
        for i in range(6):
            sizes = [i, 6-i, 5-i, n-11+i]
            for a, b, cc, dd in product(range(6), repeat=4):
                if a+b+cc+dd != 5:
                    continue
                count = c(sizes[0], a)*c(sizes[1], b)*c(sizes[2], cc)*c(sizes[3], dd)
                Q[5-a-cc][i][a+b] += count
        saved = data['factors'][str(n)]
        check(f'factor_weights_{n}', weights == saved['weights'] and sum(weights) == c(n, 5))
        for r, i, j in product(range(6), repeat=3):
            check(f'factor_count_{n}_{r}_{i}_{j}', Q[r][i][j] == saved['quotients'][r][i][j])
            check(f'factor_adjoint_{n}_{r}_{i}_{j}', weights[i]*Q[r][i][j] == weights[j]*Q[r][j][i])
        for r, i in product(range(6), repeat=2):
            check(f'factor_row_sum_{n}_{r}_{i}', sum(Q[r][i]) == c(5, r)*c(n-5, r))
        basis, norms, eigen = [], [], []
        for a in range(6):
            h = [F(i**a) for i in range(6)]
            for v, norm in zip(basis, norms):
                proj = sum(w*x*y for w, x, y in zip(weights, h, v))/norm
                h = [x-proj*y for x, y in zip(h, v)]
            norm = sum(w*x*x for w, x in zip(weights, h))
            check(f'positive_factor_norm_{n}_{a}', norm > 0 and h[0] != 0)
            normalized = [x/h[0] for x in h]
            check(f'factor_vector_{n}_{a}', list(map(enc, normalized)) == saved['vectors'][a])
            check(f'factor_norm_{n}_{a}', enc(norm/h[0]**2) == saved['norms'][a])
            ev = [sum((-1)**ell*c(a, ell)*c(5-a, r-ell)*c(n-5-a, r-ell)
                      for ell in range(r+1)) for r in range(6)]
            check(f'factor_eigenvalues_{n}_{a}', ev == saved['eigenvalues'][a])
            for r, i in product(range(6), repeat=2):
                check(f'factor_action_{n}_{a}_{r}_{i}', sum(Q[r][i][j]*h[j] for j in range(6)) == ev[r]*h[i])
            basis.append(h)
            norms.append(norm)
            eigen.append(ev)
        factors[n] = weights, Q, basis, norms, eigen
        factor_records[str(n)] = {'weights': weights, 'quotients': Q,
                                 'monic_basis': [list(map(enc, h)) for h in basis],
                                 'monic_norms': list(map(enc, norms)), 'eigenvalues': eigen}
    wh, Qh, hh, nh, eh = factors[68]
    wt, Qt, ht, nt, et = factors[956]
    orbits = list(product(range(6), repeat=2))
    W = [wh[i]*wt[j] for i, j in orbits]
    S = c(68, 5)*c(956, 5)
    check('actual_shell_size', sum(W) == S == data['shell_size'] and W == data['weights'])
    R = [[sum(value*Qh[r][i][ip]*Qt[q][j][jp] for (r, q), value in d.items())-p5*W[col]
          for col, (ip, jp) in enumerate(orbits)] for i, j in orbits]
    for row, col in product(range(36), repeat=2):
        check(f'shell_action_{row}_{col}', enc(R[row][col]) == data['weighted_shell_action'][row][col])
        check(f'shell_adjoint_{row}_{col}', W[row]*R[row][col] == W[col]*R[col][row])
    free = [tuple(ij) for ij in old['free']]
    check('free_partition', len(free) == 21 and set(free) == {ij for ij in orbits if sum(ij) <= 5})
    t0 = dict(zip(free, map(lambda x: F(*x), old['nonnegative_test']['intercept'])))
    t1 = dict(zip(free, map(lambda x: F(*x), old['nonnegative_test']['slope'])))
    for i, j in orbits:
        if i+j == 6:
            t0[i, j], t1[i, j] = d[6-i, i], F(0)
        elif i+j > 6:
            t0[i, j], t1[i, j] = F(0), F(0)
        check(f'column_affine_{i}_{j}', data['column_affine'][6*i+j] ==
              {'i': i, 'j': j, 'intercept': enc(t0[i, j]), 'slope': enc(t1[i, j])})
    lo = max(-t0[ij]/t1[ij] for ij in free if t1[ij] > 0)
    hi = min(-t0[ij]/t1[ij] for ij in free if t1[ij] < 0)
    for ij in orbits:
        check(f'interval_nonnegative_{ij}', t0[ij]+t1[ij]*lo >= 0 and t0[ij]+t1[ij]*hi >= 0)
    check('parameter_coordinate', t0[2, 3] == 0 and t1[2, 3] == 1)
    check('manuscript_interval', lo == F(3826948593076525737749263, 221908927759242896073805386355372500)
          and hi == F(689512027427211313039687769, 826754522994296083897677764417880000)
          and str(lo) in ms and str(hi) in ms and lo < hi)
    v0, v1 = [t0[ij]-p6 for ij in orbits], [t1[ij] for ij in orbits]
    dot = lambda x, y: sum(w*a*b for w, a, b in zip(W, x, y))
    y0, y1 = [F(0)]*36, [F(0)]*36
    A, B, C = F(0), F(0), p6*p6
    mode_records, zeros, eigenvectors = [], [], []
    for a, b in orbits:
        H = [hh[a][i]*ht[b][j] for i, j in orbits]
        norm = dot(H, H)
        val = sum(value*eh[a][r]*et[b][q] for (r, q), value in d.items())
        if (a, b) == (0, 0):
            val -= p5*S
        eigenvectors.append((H, val))
        f, g = dot(v0, H), dot(v1, H)
        check(f'product_norm_{a}_{b}', norm == nh[a]*nt[b] and norm > 0)
        for row in range(36):
            check(f'product_action_{a}_{b}_{row}', sum(R[row][col]*H[col] for col in range(36)) == val*H[row])
        check(f'nonnegative_spectrum_{a}_{b}', val >= 0 and enc(val) == old['modes'][6*a+b]['schur'])
        terms = [F(0)]*3
        if val == 0:
            zeros.append([a, b])
            check(f'complete_affine_zero_projection_{a}_{b}', f == g == 0)
        else:
            terms = [p5*g*g/(norm*val), 2*p5*f*g/(norm*val), p5*f*f/(norm*val)]
            A += terms[0]
            B += terms[1]
            C += terms[2]
            y0 = [x+f*h/(norm*val) for x, h in zip(y0, H)]
            y1 = [x+g*h/(norm*val) for x, h in zip(y1, H)]
        scale = H[0]
        expected = {'a': a, 'b': b, 'eigenvalue': enc(val), 'norm': enc(norm/scale**2),
                    'projection_intercept': enc(f/scale), 'projection_slope': enc(g/scale),
                    'energy_coefficients_ABC': list(map(enc, terms))}
        check(f'complete_saved_mode_{a}_{b}', expected == data['modes'][6*a+b])
        mode_records.append(expected)
    check('complete_zero_modes', len(zeros) == 20 and zeros == old['zero_modes'])
    check('positive_constant_mode', F(*mode_records[0]['eigenvalue']) == F(4982733184, 5))
    residuals = []
    for row in range(36):
        residuals.append([enc(sum(R[row][col]*yy[col] for col in range(36))-vv[row])
                          for yy, vv in [(y0, v0), (y1, v1)]])
        check(f'range_inverse_{row}', enc(y0[row]) == data['inverse_action']['intercept'][row]
              and enc(y1[row]) == data['inverse_action']['slope'][row])
        check(f'inverse_residual_{row}', residuals[-1] == [[0, 1], [0, 1]]
              == data['inverse_action']['residuals'][row] == verified['weighted_inverse_residuals'][row])
    for index, (H, val) in enumerate(eigenvectors):
        if val == 0:
            check(f'inverse_kernel_orthogonality_{index}', dot(y0, H) == dot(y1, H) == 0)
    check('bilinear_coefficients', [A, B, C] ==
          [p5*dot(v1, y1), p5*(dot(v0, y1)+dot(v1, y0)), p6*p6+p5*dot(v0, y0)])
    manuscript_coefficients = {key: F(value) for key, value in re.findall(
        r'^\| (A|B0|C0) \| (-?[0-9]+/[0-9]+) \|$', ms, re.M)}
    check('every_manuscript_coefficient', manuscript_coefficients == dict(zip(['A', 'B0', 'C0'], [A, B, C])))
    check('all_saved_coefficients', list(map(enc, [A, B, C])) == data['quadratic_ABC'] == verified['quadratic_ABC'])
    s = -B/(2*A)
    minimum = C-B*B/(4*A)
    ratio = minimum/p6
    opt = data['optimization']
    check('strict_interior_unique_minimum', A > 0 and lo < s < hi)
    check('completed_square_all_real_parameters', B == -2*A*s and C == minimum+A*s*s)
    expected_opt = {'lower': enc(lo), 'upper': enc(hi), 'stationary': enc(s), 'minimizer': enc(s),
                    'derivative': enc(0), 'endpoint_energies': [enc(A*x*x+B*x+C) for x in [lo, hi]],
                    'minimum_energy': enc(minimum), 'required_diagonal': enc(p6),
                    'diagonal_minus_minimum': enc(p6-minimum), 'energy_over_diagonal': enc(ratio),
                    'passes': True, 'minimizing_column': [
                        {'i': i, 'j': j, 'value': enc(t0[i, j]+s*t1[i, j])} for i, j in orbits]}
    for key, value in expected_opt.items():
        check('optimization_' + key, value == opt[key])
    def bounds(value, scale):
        floor = value.numerator*scale//value.denominator
        return [enc(F(floor, scale)), enc(F(floor+1, scale))]
    check('original_ratio_display', opt['ratio_bounds'] == bounds(ratio, 10**6))
    check('verification_fields', verified['minimizer'] == enc(s) and verified['minimum_energy'] == enc(minimum)
          and verified['required_diagonal'] == enc(p6) and verified['completed_square_verified'] is True
          and verified['ratio_bounds'] == bounds(ratio, 10**18) and verified['parameter_bounds'] == bounds(s, 10**24))
    check('all_strict_displayed_bounds', F(199, 10**11) < ratio < F(200, 10**11) < 1
          and F(1992907587, 10**18) < ratio < F(498226897, 250000000000000000)
          and F(14530655098541, 500000000000000000000000) < s
          < F(29061310197083, 1000000000000000000000000))
    # Specific generalized-Schur assembly: w=(p6,y), A'=diag(1,p5 R).
    # A'w=b' and w^T A'w=E are checked at the actual minimizing column.
    y = [a+s*b for a, b in zip(y0, y1)]
    v = [a+s*b for a, b in zip(v0, v1)]
    Ry = [sum(row[col]*y[col] for col in range(36)) for row in R]
    for row, ij in enumerate(orbits):
        check(f'enlarged_column_range_{row}', p5*Ry[row] == p5*v[row])
        check(f'minimizing_column_nonnegative_{row}', t0[ij]+s*t1[ij] >= 0)
    check('enlarged_schur_energy', p6*p6+p5*dot(y, Ry) == minimum and 0 < minimum < p6)
    check('both_endpoint_energies', all(A*x*x+B*x+C > minimum for x in [lo, hi]))
    result = {'input_hashes': {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in
                              ['full-shell-column-energy-results.json', 'full-shell-column-energy-verification.json',
                               'full-shell-nullspace-results.json']},
              'manuscript_hashes': {name: hashlib.sha256((NB / name).read_bytes()).hexdigest() for name in
                                   ['lemmas/L056-released-zero-five-shell-nonexclusion.md',
                                    'lemmas/L059-full-shell-nullspace-compatible-column.md',
                                    'lemmas/L060-full-shell-one-column-psd-extension.md']},
              'factors': factor_records, 'actual_weights': W, 'shell_size': S,
              'weighted_shell_action': [list(map(enc, row)) for row in R], 'modes': mode_records,
              'inverse_intercept': list(map(enc, y0)), 'inverse_slope': list(map(enc, y1)),
              'inverse_residuals': residuals, 'zero_modes': zeros,
              'quadratic_ABC': list(map(enc, [A, B, C])), 'optimization': expected_opt,
              'ratio_bounds': bounds(ratio, 10**18), 'parameter_bounds': bounds(s, 10**24),
              'checks': len(checks), 'check_names': checks, 'failures': failures}
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(f'checks={len(checks)}; failures={failures}; certificate={OUT.relative_to(NB)}')
    print(f'minimum/diagonal strictly between {F(*result["ratio_bounds"][0])} and '
          f'{F(*result["ratio_bounds"][1])}; required < 1; diagonal={p6}')
    print(f'complete modes: {len(zeros)} zero, {36-len(zeros)} positive; unique minimum strictly interior={lo < s < hi}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
