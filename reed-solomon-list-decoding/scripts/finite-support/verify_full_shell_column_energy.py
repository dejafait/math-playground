"""Independent residual/bilinear verifier for full-shell column energy.

No constructor imports, spectral inversion, optimizer or floating point.
Reconstructs the actual weighted quotient from point-region counts;
certifies saved inverse vectors by full operator residuals and computes
the energy polynomial directly by bilinear products.
"""
import hashlib
import json
import re
from fractions import Fraction as F
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'full-shell-column-energy-verification.json'


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

    path = ROOT / 'full-shell-column-energy-results.json'
    data = json.loads(path.read_text())
    old = json.loads((ROOT / 'full-shell-nullspace-results.json').read_text())
    manuscript = (NB / 'lemmas/L056-released-zero-five-shell-nonexclusion.md').read_text()
    z = {(int(r), int(q)): F(v) for r, q, v in re.findall(
        r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', manuscript, re.M)}
    d = {(r, q): val/(c(5, r)*c(63, r)*c(5, q)*c(951, q)) for (r, q), val in z.items()}
    d[0, 0] = F(1)
    p5, p6 = F(1, 68881143660), F(133, 9357995374380)
    check('constructor_pass', data['failures'] == [])
    check('source_hashes', all(hashlib.sha256((NB / name).read_bytes()).hexdigest() == value
                               for name, value in data['source_hashes'].items()))
    orbits = [(i, j) for i in range(6) for j in range(6)]
    weights = [c(6, i)*c(62, 5-i)*c(6, j)*c(950, 5-j) for i, j in orbits]
    check('weights', weights == data['weights'])
    def count(n, r, i, ip):
        # X' takes u from X cap U, ip-u from U\X,
        # 5-r-u from X\U, r+u-ip from the remaining region.
        return sum(c(i, u)*c(6-i, ip-u)*c(5-i, 5-r-u)*c(n-11+i, r+u-ip)
                   for u in range(6))
    R = [[sum(value*count(68, r, i, ip)*count(956, q, j, jp)
              for (r, q), value in d.items())-p5*weights[col]
          for col, (ip, jp) in enumerate(orbits)] for i, j in orbits]
    for row in range(36):
        check(f'full_action_row_{row}', list(map(enc, R[row])) == data['weighted_shell_action'][row])
    free = [tuple(x) for x in old['free']]
    t0 = dict(zip(free, [F(*x) for x in old['nonnegative_test']['intercept']]))
    t1 = dict(zip(free, [F(*x) for x in old['nonnegative_test']['slope']]))
    for ij in orbits:
        i, j = ij
        if i+j == 6:
            t0[ij], t1[ij] = d[6-i, i], F(0)
        elif i+j >= 7:
            t0[ij], t1[ij] = F(0), F(0)
    v0, v1 = [t0[ij]-p6 for ij in orbits], [t1[ij] for ij in orbits]
    y0 = [F(*x) for x in data['inverse_action']['intercept']]
    y1 = [F(*x) for x in data['inverse_action']['slope']]
    residuals = []
    for row, ij in enumerate(orbits):
        entry = data['column_affine'][row]
        check(f'full_affine_{row}', (entry['i'], entry['j']) == ij
              and entry['intercept'] == enc(t0[ij]) and entry['slope'] == enc(t1[ij]))
        r0 = sum(R[row][col]*y0[col] for col in range(36))-v0[row]
        r1 = sum(R[row][col]*y1[col] for col in range(36))-v1[row]
        residuals.append([enc(r0), enc(r1)])
        check(f'inverse_residual_{row}', r0 == 0 and r1 == 0
              and residuals[-1] == data['inverse_action']['residuals'][row])
    # A solution of R*y=v suffices for the energy, since v is perpendicular
    # to ker R. Also verify these solutions lie in its orthogonal complement.
    for a, b in old['zero_modes']:
        hh = [F(*x) for x in old['head']['vectors'][a]]
        kk = [F(*x) for x in old['tail']['vectors'][b]]
        H = [hh[i]*kk[j] for i, j in orbits]
        check(f'inverse_zero_projection_{a}_{b}', all(
            sum(w*x*h for w, x, h in zip(weights, yy, H)) == 0 for yy in [y0, y1]))
    def dot(x, y):
        return sum(w*u*v for w, u, v in zip(weights, x, y))
    A = p5*dot(v1, y1)
    B = p5*(dot(v0, y1)+dot(v1, y0))
    C = p6*p6+p5*dot(v0, y0)
    check('all_quadratic_coefficients', list(map(enc, [A, B, C])) == data['quadratic_ABC'])
    lo = F(*old['nonnegative_test']['maximum_lower'])
    hi = F(*old['nonnegative_test']['minimum_upper'])
    opt = data['optimization']
    check('interval', enc(lo) == opt['lower'] and enc(hi) == opt['upper'])
    check('strict_positive_curvature', A > 0)
    s = -B/(2*A)
    check('strict_interior_stationary', lo < s < hi and enc(s) == opt['stationary'] == opt['minimizer'])
    minimum = C-B*B/(4*A)
    check('exact_completed_square', C == minimum+A*s*s and B == -2*A*s)
    check('minimum_and_diagonal', enc(minimum) == opt['minimum_energy'] and opt['required_diagonal'] == enc(p6)
          and opt['diagonal_minus_minimum'] == enc(p6-minimum) and 0 < minimum < p6 and opt['passes'])
    for endpoint, stored in zip([lo, hi], opt['endpoint_energies']):
        check(f'endpoint_energy_{endpoint == lo}', enc(A*endpoint*endpoint+B*endpoint+C) == stored
              and A*endpoint*endpoint+B*endpoint+C > minimum)
    for row, ij in enumerate(orbits):
        t = t0[ij]+t1[ij]*s
        check(f'minimizing_column_{row}', t >= 0 and opt['minimizing_column'][row] ==
              {'i': ij[0], 'j': ij[1], 'value': enc(t)})
    def bounds(x, scale):
        low = x.numerator*scale//x.denominator
        return [enc(F(low, scale)), enc(F(low+1, scale))]
    ratio_bounds = bounds(minimum/p6, 10**18)
    parameter_bounds = bounds(s, 10**24)
    check('strict_displayed_bounds', F(*ratio_bounds[0]) < minimum/p6 < F(*ratio_bounds[1])
          and F(*parameter_bounds[0]) < s < F(*parameter_bounds[1]))
    check('useful_strict_ratio_bound', F(199, 10**11) < minimum/p6 < F(200, 10**11))
    result = {'input_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
              'weighted_inverse_residuals': residuals, 'quadratic_ABC': list(map(enc, [A, B, C])),
              'minimizer': enc(s), 'minimum_energy': enc(minimum), 'required_diagonal': enc(p6),
              'ratio_bounds': ratio_bounds, 'parameter_bounds': parameter_bounds,
              'completed_square_verified': True, 'checks': len(checks), 'failures': failures}
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(f'checks={len(checks)}; failures={failures}; certificate={OUT.relative_to(NB)}')
    print(f'exact minimum/diagonal in [{F(*ratio_bounds[0])},{F(*ratio_bounds[1])}); required < 1')
    print(f'minimizer in [{F(*parameter_bounds[0])},{F(*parameter_bounds[1])}); interior={lo < s < hi}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
