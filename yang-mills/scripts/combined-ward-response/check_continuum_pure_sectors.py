"""L032 continuum spectral partial sums. Binary64 diagnostics, not certificates of sign.

The coefficients are separable derivatives of Psi. Integration by parts puts
their derivatives on trigonometric mode products, avoiding bump derivatives.
Full numerical evidence is written to disk; no omitted-mode bound is claimed.
"""
import argparse
import json
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

import numpy as np

ZERO = (0, 0, 0, 0)
PLANES = [(i, j) for i in range(4) for j in range(i + 1, 4)]


def shift(a, j, n=1):
    b = list(a)
    b[j] += n
    return tuple(b)


def coefficients(pair):
    p, q = pair
    u = [[] for _ in range(4)]
    u2 = [[] for _ in range(4)]
    u[p] = [(F(1), shift(ZERO, q))]
    u[q] = [(F(-1), shift(ZERO, p))]
    u2[p] = [(F(1, 6), shift(ZERO, q, 3))]
    u2[q] = [(F(-1, 6), shift(ZERO, p, 3))]

    def derivative(rows, j, n=1, factor=F(1)):
        return [(factor * v, shift(d, j, n)) for v, d in rows]

    w = [derivative(u[j], j) for j in range(4)]
    w2 = [derivative(u2[j], j) + derivative(u[j], j, 3, F(1, 6))
          for j in range(4)]
    s, s2 = {}, {}
    for i, j in PLANES:
        s[i, j] = derivative(u[j], i) + derivative(u[i], j)
        s2[i, j] = (derivative(u2[j], i) + derivative(u2[i], j)
                     + derivative(u[j], i, 3, F(1, 6))
                     + derivative(u[i], j, 3, F(1, 6)))
    return u, u2, w, w2, s, s2, derivative


def curl(i, j, correction=0, clover=False):
    if i == j:
        return []
    base = [(F(1), j, shift(ZERO, i)), (F(-1), i, shift(ZERO, j))]
    if not correction:
        return base
    out = [(F(1, 24), j, shift(ZERO, i, 3)),
           (F(-1, 24), i, shift(ZERO, j, 3))]
    if clover:
        for v, c, d in base:
            out.extend([(v / 8, c, shift(d, i, 2)),
                        (v / 8, c, shift(d, j, 2))])
    return out


def laplace(output, order=0):
    # d* d, not the full Hodge Laplacian.
    terms = []
    for c in range(4):
        if c == output:
            for j in range(4):
                terms.append((F(-1) if order == 0 else F(-1, 12), c,
                              shift(ZERO, j, 2 if order == 0 else 4)))
        if order == 0:
            terms.append((F(1), c, shift(shift(ZERO, output), c)))
        else:
            terms.extend([(F(1, 24), c, shift(shift(ZERO, output, 3), c)),
                          (F(1, 24), c, shift(shift(ZERO, output), c, 3))])
    return terms


def operators(pair):
    u, u2, w, w2, s, s2, derivative = coefficients(pair)
    q0 = [defaultdict(F), defaultdict(F)]
    q2 = [defaultdict(F), defaultdict(F)]
    t0, t2 = defaultdict(F), defaultdict(F)

    def weak(out, weights, left, right, factor=F(1)):
        for v, d in weights:
            for vl, cl, dl in left:
                for vr, cr, dr in right:
                    out[d, cl, dl, cr, dr] += factor * v * vl * vr

    for i, j in PLANES:
        weights = w[i] + w[j]
        weight2 = (w2[i] + w2[j] + derivative(weights, i, 2, F(1, 8))
                   + derivative(weights, j, 2, F(1, 8)))
        f0, f2 = curl(i, j), curl(i, j, 1)
        weak(q0[0], weights, f0, f0)
        weak(q2[0], weight2, f0, f0)
        weak(q2[0], weights, f2, f0)
        weak(q2[0], weights, f0, f2)
        for alpha in range(4):
            a0, b0 = curl(i, alpha), curl(j, alpha)
            a2, b2 = curl(i, alpha, 1, True), curl(j, alpha, 1, True)
            for left0, right0, left2, right2 in [(a0, b0, a2, b2),
                                                 (b0, a0, b2, a2)]:
                weak(q0[1], s[i, j], left0, right0, F(1, 2))
                weak(q2[1], s2[i, j], left0, right0, F(1, 2))
                weak(q2[1], s[i, j], left2, right0, F(1, 2))
                weak(q2[1], s[i, j], left0, right2, F(1, 2))

    for nu in range(4):
        l0, l2 = laplace(nu), laplace(nu, 1)
        # <L0 f,E2 M0 d0 h> = <E2 L0 f,M0 d0 h> by integration by
        # parts on compact coefficients. No derivatives of u are deleted.
        e2l0 = [(v / 8, c, shift(d, nu, 2)) for v, c, d in l0]
        for rho in range(4):
            f0 = curl(rho, nu)
            f2 = curl(rho, nu, 1, True)
            weak(t0, u[rho], l0, f0)
            weak(t2, u2[rho], l0, f0)
            weak(t2, u[rho], e2l0, f0)
            weak(t2, u[rho], l0, f2)
            weak(t2, u[rho], l2, f0)

    def residual(t, q):
        out = defaultdict(F)
        for (d, cl, dl, cr, dr), v in t.items():
            out[d, cl, dl, cr, dr] += v / 2
            out[d, cr, dr, cl, dl] += v / 2
        for part in q:
            for key, v in part.items():
                out[key] -= v
        return {key: v for key, v in out.items() if v}

    return [{k: v for k, v in part.items() if v} for part in q0], residual(t2, q2), residual(t0, q0)


class Integrals:
    def __init__(self, pair, m, degree):
        self.pair, self.m = pair, m
        points, weights = np.polynomial.legendre.leggauss(degree)
        xs, ws = [], []
        for a, b in [(-3, -2.5), (-2.5, 0), (0, 2.5), (2.5, 3)]:
            xs.append((a + b) / 2 + (b - a) * points / 2)
            ws.append((b - a) * weights / 2)
        self.x, self.weights = np.concatenate(xs), np.concatenate(ws)
        x = self.x
        b1, b2 = np.zeros_like(x), np.zeros_like(x)
        t1, t2 = 9 - x*x, x*x - 25/4
        np.exp(-1/t1, out=b1, where=t1 > 0)
        np.exp(-1/t2, out=b2, where=t2 > 0)
        self.rho = b1 / (b1 + b2)
        self.omega = np.pi / 8
        self.transforms = {}
        for odd in (0, 1):
            base = self.rho * (x if odd else 1)
            self.transforms[odd] = {
                n: np.sum(self.weights * base * np.exp(1j * self.omega * n * x))
                for n in range(-2*m, 2*m + 1)}

    @lru_cache(None)
    def element(self, axis, coefficient_derivative, left_derivative,
                right_derivative, left_cos, right_cos, k, ell):
        odd = int(axis in self.pair)
        lp = k if left_cos else k + 1
        rp = ell if right_cos else ell + 1
        if (odd + coefficient_derivative + left_derivative + right_derivative + lp + rp) % 2:
            return 0.0

        def waves(index, cosine, derivative):
            if index == 0:
                return [(0, 1 / np.sqrt(8))] if cosine and derivative == 0 else []
            return [(sign * index, (0.25 if cosine else sign / (4j))
                     * np.exp(1j * sign * index * np.pi / 2)
                     * (1j * sign * index * self.omega)**derivative)
                    for sign in (-1, 1)]

        value = 0j
        for p, a in waves(k, left_cos, left_derivative):
            for q, b in waves(ell, right_cos, right_derivative):
                value += (a*b * (-1j * (p+q) * self.omega)**coefficient_derivative
                          * self.transforms[odd][p+q])
        if abs(value.imag) > 1e-8 * max(1, abs(value.real)):
            raise ArithmeticError('Non-real one-dimensional integral')
        return float(value.real)

    @lru_cache(None)
    def matrix(self, axis, r, a, b, component):
        ks = [0] if axis == 0 else list(range(1, self.m + 1))
        ls = list(range(0 if axis == component else 1, self.m + 1))
        return np.array([[self.element(axis, r, a, b, axis == 0,
                                       axis == component, k, ell)
                          for ell in ls] for k in ks])


def restricted_terms(op, component):
    return [(d, a, b, float(v)) for (d, cl, a, cr, b), v in op.items()
            if cl == 0 and cr == component and a[0] == 0]


def assemble(op, component, axial_position, integrals, shape):
    out = np.zeros(shape)
    for d, a, b, v in restricted_terms(op, component):
        axial = integrals.matrix(0, d[0], a[0], b[0], component)[0, axial_position]
        if axial == 0:
            continue
        matrices = [integrals.matrix(j, d[j], a[j], b[j], component) for j in (1, 2, 3)]
        out += v * axial * np.einsum('ab,cd,ef->abcdef', *matrices, optimize=False)
    return out


def calculate(m, degree):
    pairs = [(0, 2), (1, 3)]
    algebra = [operators(pair) for pair in pairs]
    integrations = [Integrals(pair, m, degree) for pair in pairs]
    sums = np.zeros((2, 2, 2, 2))  # probe, Q potential, N potential, axial-zero/positive
    zero_order_max, axial_a_max = 0.0, 0.0
    for c in range(4):
        ls = [np.arange(0 if j == c else 1, m + 1) for j in range(4)]
        ks = np.arange(1, m + 1)
        shape = (m, len(ls[1]), m, len(ls[2]), m, len(ls[3]))
        lk = (ks[:, None, None, None, None, None]**2
              + ks[None, None, :, None, None, None]**2
              + ks[None, None, None, None, :, None]**2) * (np.pi/8)**2
        ll0 = (ls[1][None, :, None, None, None, None]**2
               + ls[2][None, None, None, :, None, None]**2
               + ls[3][None, None, None, None, None, :]**2) * (np.pi/8)**2
        for axial_position, ell1 in enumerate(ls[0]):
            if ell1 % 2:
                continue
            ns = [assemble(algebra[z][1], c, axial_position, integrations[z], shape)
                  for z in (0, 1)]
            for z in (0, 1):
                n0 = assemble(algebra[z][2], c, axial_position, integrations[z], shape)
                zero_order_max = max(zero_order_max, float(np.max(np.abs(n0))))
            ll = ll0 + (ell1 * np.pi/8)**2
            weight = 8*np.exp(-(lk+ll)/16)/(lk*lk*ll)
            for i in (0, 1):
                for alpha in (0, 1):
                    q = assemble(algebra[alpha][0][i], c, axial_position, integrations[alpha], shape)
                    if c == 0 and ell1 == 0 and alpha == 0:
                        axial_a_max = max(axial_a_max, float(np.max(np.abs(q))),
                                          float(np.max(np.abs(ns[alpha]))))
                    for beta in (0, 1):
                        sums[i, alpha, beta, int(ell1 != 0)] += float(np.sum(weight*q*ns[beta]))
    return dict(cutoff=m, quadrature_degree=degree,
                mode_rule='all k in Z with 1<=k_j<=cutoff; all allowed ell components and indices <=cutoff',
                sector_values=sums.tolist(), pure_values=(sums[:, 0, 0].sum(axis=1) + sums[:, 1, 1].sum(axis=1)).tolist(),
                mixed_values=np.stack([sums[:, 0, 1].sum(axis=1), sums[:, 1, 0].sum(axis=1)], axis=1).tolist(),
                zero_order_residual_max_abs=zero_order_max,
                axial_zero_A_matrix_max_abs=axial_a_max,
                algebra_term_counts=[dict(Q3=len(a[0][0]), Q6=len(a[0][1]), N2=len(a[1]), N0=len(a[2])) for a in algebra])


def add_checks(row):
    sectors = np.array(row['sector_values'])
    row['mixed_values'] = np.stack([sectors[:, 0, 1].sum(axis=1), sectors[:, 1, 0].sum(axis=1)], axis=1).tolist()
    check_error = max(row['zero_order_residual_max_abs'], row['axial_zero_A_matrix_max_abs'],
                      float(np.max(np.abs(row['mixed_values']))))
    row['checks'] = dict(actual_max_abs=check_error, required_max_abs=1e-8, passed=check_error < 1e-8)
    return check_error


def summarize(result):
    result['actual_error_bound'] = None
    result['unresolved_checks'] = ['No rigorous quadrature enclosure.',
                                   'No bound on the entire omitted spectral sum.',
                                   'No sign or value for the infinite sum is certified.']
    rows = result['rows']
    result['quadrature_differences'] = []
    for m in sorted(set(r['cutoff'] for r in rows)):
        selected = sorted([r for r in rows if r['cutoff'] == m], key=lambda r: r['quadrature_degree'])
        if len(selected) > 1:
            difference = np.array(selected[-1]['sector_values']) - np.array(selected[0]['sector_values'])
            result['quadrature_differences'].append(dict(cutoff=m, degrees=[selected[0]['quadrature_degree'], selected[-1]['quadrature_degree']],
                actual_max_sector_change=float(np.max(np.abs(difference))),
                qualification='Observed finite-rule difference, not an error bound.'))


def scalar_element(op, integrals, k, ell):
    value = 0.0
    for (d, cl, a, cr, b), v in op.items():
        if cl != k[0] or cr != ell[0]:
            continue
        term = float(v)
        for axis in range(4):
            term *= integrals.element(axis, d[axis], a[axis], b[axis],
                                      axis == cl, axis == cr, k[1][axis], ell[1][axis])
        value += term
    return value


def lattice_comparison(ns):
    from haar_contraction import RelativeBox
    tests = [((0, (0, 1, 1, 1)), (0, (2, 1, 1, 1))),
             ((0, (0, 1, 1, 2)), (0, (0, 1, 1, 2))),
             ((0, (0, 1, 1, 1)), (2, (2, 1, 1, 1)))]
    algebra = [operators(p) for p in [(0, 2), (1, 3)]]
    integrals = [Integrals(p, 4, 96) for p in [(0, 2), (1, 3)]]
    expected = [sum(scalar_element(a[1], integ, k, ell) for a, integ in zip(algebra, integrals))
                for k, ell in tests]

    def mode(box, label):
        component, indices = label
        field = np.ones(box.shapes[component])
        for axis, index in enumerate(indices):
            shape = [1]*4
            shape[axis] = box.shapes[component][axis]
            positions = np.arange(box.n)+0.5 if axis == component else np.arange(1, box.n)
            if index == 0:
                wave = np.ones_like(positions)/np.sqrt(box.n)
            else:
                wave = np.sqrt(2/box.n)*(np.cos if axis == component else np.sin)(np.pi*index*positions/box.n)
            field *= wave.reshape(shape)
        fields = box.zeros()
        fields[component] = field
        return fields

    result = dict(scope='Selected full-displacement N2 entries vs independent existing lattice residual/a^4',
                  qualification='Mesh diagnostic; no convergence-rate or enclosure certificate.',
                  mode_tests=[dict(k=k, ell=ell, continuum_N2=e) for (k, ell), e in zip(tests, expected)], rows=[])
    for n in ns:
        box = RelativeBox(n)
        actual = []
        for k, ell in tests:
            right = mode(box, ell)
            residual = box.residual(right)
            actual.append(box.dot(mode(box, k), residual)/box.a**4)
        row = dict(N=n, a=box.a, lattice_entries=actual,
                   absolute_differences=[abs(v-e) for v, e in zip(actual, expected)])
        result['rows'].append(row)
        path = Path(__file__).with_name('continuum-pure-sectors-stencil-certificate.json')
        path.write_text(json.dumps(result, indent=2)+'\n')
        print(json.dumps(dict(N=n, actual_entries=actual, required_limits=expected,
                              differences=row['absolute_differences'], path=str(path))), flush=True)
        del box
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cutoffs', type=int, nargs='+', default=[4, 6, 8])
    parser.add_argument('--degrees', type=int, nargs='+', default=[32, 64])
    parser.add_argument('--lattice-check', type=int, nargs='+')
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('continuum-pure-sectors-certificate.json'))
    args = parser.parse_args()
    if args.lattice_check:
        lattice_comparison(args.lattice_check)
        return
    result = dict(scope='L032 original continuum pure/mixed sums, finite spectral cutoffs only',
                  qualification='Binary64 deterministic diagnostics; no rigorous quadrature enclosure or omitted-mode bound.',
                  rigorous_sign_certified=False, required_bound='quadrature plus full omitted-mode error < abs(I_i), not available',
                  rows=[], failures=[])
    for m in args.cutoffs:
        for degree in args.degrees:
            row = calculate(m, degree)
            result['rows'].append(row)
            check_error = add_checks(row)
            if check_error >= 1e-8:
                result['failures'].append(dict(cutoff=m, degree=degree, check_error=check_error))
            summarize(result)
            args.output.write_text(json.dumps(result, indent=2) + '\n')
            print(json.dumps(dict(cutoff=m, degree=degree, pure_values=row['pure_values'],
                                  checks=row['checks'], path=str(args.output))), flush=True)
    print(json.dumps(dict(rigorous_sign_certified=False, failures=result['failures'],
                         actual_error_bound=None, required_error_bound=result['required_bound'], path=str(args.output))))


if __name__ == '__main__':
    main()
