"""Exact color polarization and actual-stencil compression diagnostics.

No cutoff limit, signed companion sum, or cancellation is certified.
The analytic compression proof is in L040; floating checks are diagnostics.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from pathlib import Path
import json

import numpy as np
from haar_contraction import RelativeBox, PLANES, gradient, gradient_adj, average, average_adj, central


def add(*terms):
    out = {}
    for p in terms:
        for key, value in p.items():
            out[key] = out.get(key, F(0)) + value
    return {key: value for key, value in out.items() if value}


def scale(c, p):
    return {key: c*value for key, value in p.items() if c*value}


def mul(p, q):
    out = {}
    for key, value in p.items():
        for other, coefficient in q.items():
            exponent = tuple(x+y for x, y in zip(key, other))
            out[exponent] = out.get(exponent, F(0)) + value*coefficient
    return out


def deriv(p, j):
    out = {}
    for key, value in p.items():
        if key[j]:
            exponent = list(key)
            exponent[j] -= 1
            out[tuple(exponent)] = value*key[j]
    return out


def dot(x, y):
    return add(*(mul(a, b) for a, b in zip(x, y)))


def scalar_contraction(u, v):
    h, l, e, b, c, f = u
    H, L, E, B, C, Fv = v
    return (-3*(h*L+l*H-2*b*B) + l*E+e*L-2*f*Fv
            +4*(h*Fv+f*H-b*C-c*B))


def color_checks():
    variables = [{tuple(int(i == j) for i in range(9)): F(1)} for j in range(9)]
    h, l, d = [variables[j:j+3] for j in (0, 3, 6)]
    cross_square = lambda x, y: add(mul(dot(x, x), dot(y, y)), scale(-1, mul(dot(x, y), dot(x, y))))
    mixed = add(mul(dot(h, h), dot(d, l)), scale(-1, mul(dot(h, l), dot(h, d))))
    q = add(scale(F(1, 8), cross_square(h, l)), scale(F(-1, 24), cross_square(l, d)), scale(F(-1, 6), mixed))
    pairs = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
    def lap(p, pair):
        r, s = pair
        return scale(1 if r == s else 2, add(*(deriv(deriv(p, 3*r+c), 3*s+c) for c in range(3))))
    rows = []
    for j, pair in enumerate(pairs):
        for k, other in enumerate(pairs):
            u, v = [F(int(m == j)) for m in range(6)], [F(int(m == k)) for m in range(6)]
            actual_polynomial = scale(-1, lap(lap(q, pair), other))
            actual = actual_polynomial.get((0,)*9, F(0))
            assert all(key == (0,)*9 for key in actual_polynomial)
            expected = scalar_contraction(u, v)
            rows.append(dict(U_entry=j, V_entry=k, actual=str(actual), required=str(expected), passed=actual == expected))
    return rows


def compressed_operators(box, phi):
    # phi has singleton axial axis. Mean is over N edge positions;
    # vertex coefficients sum over their N-1 positions.
    u = [np.sum(x, axis=0, keepdims=True)/box.n for x in box.u]
    w = [central(u[mu], mu, box.a) if mu else np.zeros_like(phi) for mu in range(4)]
    s = {(mu, nu): central(u[nu], mu, box.a)+central(u[mu], nu, box.a)
         for mu, nu in PLANES if mu > 0}
    def delta(x):
        return sum(gradient_adj(gradient(x, mu), mu) for mu in (1, 2, 3))
    def k(x):
        return sum(u[mu]*average(gradient(x, mu), mu) for mu in (1, 2, 3))/box.a
    def kt(x):
        return sum(gradient_adj(average_adj(u[mu]*x, mu), mu) for mu in (1, 2, 3))/box.a
    q3 = sum(gradient_adj(average_adj(w[mu], mu)*gradient(phi, mu), mu) for mu in (1, 2, 3))
    bars = {mu: average(gradient(phi, mu), mu) for mu in (1, 2, 3)}
    terms = {mu: np.zeros_like(phi) for mu in (1, 2, 3)}
    for (mu, nu), weight in s.items():
        terms[mu] += weight*bars[nu]/2
        terms[nu] += weight*bars[mu]/2
    q6 = sum(gradient_adj(average_adj(terms[mu], mu), mu) for mu in (1, 2, 3))
    return dict(residual=(delta(k(phi))+kt(delta(phi)))/2-q3-q6,
                triplet=q3, shear=q6)


def rebuild_weights(box):
    box.w = [central(box.u[mu], mu, box.a) for mu in range(4)]
    box.s = {(mu, nu): central(box.u[nu], mu, box.a)+central(box.u[mu], nu, box.a) for mu, nu in PLANES}
    box.triplet_weights = {(mu, nu): average_adj(average_adj(box.w[mu]+box.w[nu], mu), nu) for mu, nu in PLANES}


def compression_checks():
    n = 24
    box = RelativeBox(n)
    original = [x.copy() for x in box.u]
    rng = np.random.default_rng(550024)
    modes = np.arange(1, n)
    smooth = np.ones((1, n-1, n-1, n-1))
    for mu in (1, 2, 3):
        shape = [1]*4
        shape[mu] = n-1
        smooth *= np.sin(mu*np.pi*modes/n).reshape(shape)
    inputs = [smooth, rng.normal(size=smooth.shape)]
    rows = []
    for sector, active in [('full', (0, 1, 2, 3)), ('13', (0, 2)), ('24', (1, 3))]:
        box.u = [x.copy() if mu in active else np.zeros_like(x) for mu, x in enumerate(original)]
        rebuild_weights(box)
        for index, phi in enumerate(inputs):
            field = box.zeros()
            field[0] = np.broadcast_to(phi, box.shapes[0]).copy()
            q3, q6 = box.probe_matrices(field)
            full = dict(residual=box.residual(field), triplet=q3, shear=q6)
            reduced = compressed_operators(box, phi)
            for name, value in full.items():
                direct = np.mean(value[0], axis=0, keepdims=True)
                compressed = reduced[name]
                defect = float(np.max(np.abs(direct-compressed)))
                size = float(max(1, np.max(np.abs(direct)), np.max(np.abs(compressed))))
                tolerance = 1e-11*size
                rows.append(dict(N=n, sector=sector, operator=name, input=['smooth', 'all_frequency'][index],
                                 actual_maximum_defect=defect, required_maximum_defect=tolerance,
                                 direct_maximum=float(np.max(np.abs(direct))),
                                 passed=defect < tolerance))
                if sector == '13':
                    defect = float(max(np.max(np.abs(direct)), np.max(np.abs(compressed))))
                    rows.append(dict(N=n, sector=sector, operator=name, input=['smooth', 'all_frequency'][index],
                                     check='annihilation', actual_maximum_defect=defect,
                                     required_maximum_defect=1e-11, passed=defect < 1e-11))
    return rows


def main():
    exact, numerical = color_checks(), compression_checks()
    failures = [row for row in exact+numerical if not row['passed']]
    certificate = dict(scope='L040 color polarization and finite axial-zero compression only',
                       exact_color_basis_checks=exact, compression_diagnostics=numerical,
                       failures=failures,
                       actual_bound='Exact finite reduction; no asymptotic bound obtained',
                       required_bound='Controlled a^2-scaled companion limit; cancellation would require +48 I_i',
                       qualifications='36 exact rational color checks. N=24 compression checks use binary64 and two inputs; the full operator identity is proved analytically in L040. No sign, cutoff fit, or cancellation follows.')
    path = Path(__file__).with_name('upper-face-companion-certificate.json')
    path.write_text(json.dumps(certificate, indent=2)+'\n')
    print(f'Exact color checks: {len(exact)}; compression diagnostics: {len(numerical)}; failures: {len(failures)}')
    print('Maximum compression defect:', max(row['actual_maximum_defect'] for row in numerical))
    print('Actual: exact reduction only. Required: controlled scaled limit, +48 I_i for cancellation.')
    print('Certificate:', path)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
