"""L128 actual full-displacement physical tensors; numerics are diagnostics.

Retains both displacement sectors, all rectangular-cutoff relative modes,
the constant axial prefix and both shear polarizations. Saves every tensor
factor and signed contraction. Quadrature/arithmetic inclusion is missing.
"""
import argparse
import hashlib
import json
from itertools import combinations
from fractions import Fraction
from math import factorial
from pathlib import Path

import numpy as np

from check_continuum_first_pair import coefficients, rule

ROOT = Path(__file__).parent


def evaluate(cutoff, space_degree, time_degree, label):
    x, wx = rule([(-3, -2.5), (-2.5, 2.5), (2.5, 3)], space_degree)
    co = coefficients(x)
    freq = {'E': np.arange(cutoff + 1) * np.pi / 8,
            'V': np.arange(1, cutoff + 1) * np.pi / 8}
    basis = {}
    for typ in ('E', 'V'):
        angles = np.outer(x + 4, freq[typ])
        if typ == 'E':
            b = np.cos(angles) / 2
            db = -np.sin(angles) * freq[typ] / 2
            b[:, 0] = 1 / np.sqrt(8)
            prefix = np.empty_like(b)
            prefix[:, 0] = (x + 4) / np.sqrt(8)
            prefix[:, 1:] = np.sin(angles[:, 1:]) / (2 * freq[typ][None, 1:])
            basis[typ, 'prefix'] = prefix
        else:
            b = np.sin(angles) / 2
            db = np.cos(angles) * freq[typ] / 2
        basis[typ, 'b'], basis[typ, 'd'] = b, db
        basis[typ, 'dd'] = -b * freq[typ]**2
    types = lambda alpha: tuple('E' if j == alpha else 'V' for j in range(4))
    ordinary = lambda alpha: tuple((t, 'b') for t in types(alpha))
    derivative = {'r': 'rp', 'f': 'fp', 'fp': 'fpp'}
    u = {0: [(1, ('f', 'r', 'fp', 'r'))],
         1: [(1, ('r', 'f', 'r', 'fp'))],
         2: [(-1, ('fp', 'r', 'f', 'r'))],
         3: [(-1, ('r', 'fp', 'r', 'f'))]}

    def deriv(terms, axis):
        result = []
        for sign, factors in terms:
            factors = list(factors)
            factors[axis] = derivative[factors[axis]]
            result.append((sign, tuple(factors)))
        return result

    w = {a: deriv(u[a], a) for a in range(4)}
    shear = {(a, b): deriv(u[b], a) + deriv(u[a], b)
             for a, b in combinations(range(4), 2)}
    matrices, matrix_keys, integral_cache = [], [], {}

    def integral(left, weight, right, ell):
        key = left, weight, right, ell
        if key not in integral_cache:
            values = co[weight] * ((x + 4) if ell else 1)
            mat = basis[left].T @ ((wx * values)[:, None] * basis[right])
            integral_cache[key] = len(matrices)
            matrices.append(mat)
            matrix_keys.append(key)
        return integral_cache[key]

    def circulation(a, b):
        if a > b:
            return [(alpha, -s, rows) for alpha, s, rows in circulation(b, a)]
        result = []
        for alpha, axis, sign in ((b, a, 1), (a, b, -1)):
            rows = list(ordinary(alpha))
            rows[axis] = (types(alpha)[axis], 'd')
            result.append((alpha, sign, tuple(rows)))
        return result

    def lift(a):
        rows = list(ordinary(0))
        rows[0], rows[a] = ('E', 'prefix'), ('V', 'd')
        return [(a, 1, ordinary(a)), (0, -1, tuple(rows))]

    def differentiated_lift(a, axis):
        result = []
        for alpha, sign, factors in lift(a):
            factors = list(factors)
            typ, order = factors[axis]
            factors[axis] = (typ, 'dd' if order == 'd' else 'd')
            result.append((alpha, sign, tuple(factors)))
        return result

    q = {3: [], 6: []}
    m = {name: [] for name in ('D', 'X', 'A', 'C')}

    def add(destination, left, right, coeffs, scale=1, ell=False):
        for sign, coeff in coeffs:
            for alpha, sl, rows in left:
                for beta, sr, cols in right:
                    ids = [integral(a, c, b, ell and j == 0)
                           for j, (a, c, b) in enumerate(zip(rows, coeff, cols))]
                    destination.append((alpha, beta, scale * sign * sl * sr, ids))

    for a, b in combinations(range(4), 2):
        curl = circulation(a, b)
        add(q[3], curl, curl, w[a] + w[b])
        for c in range(4):
            if c in (a, b):
                continue
            left, right = circulation(a, c), circulation(b, c)
            add(q[6], left, right, shear[a, b], .5)
            add(q[6], right, left, shear[a, b], .5)
    div_t = sum((w[a] for a in (1, 2, 3)), [])
    for a in (1, 2, 3):
        add(m['D'], lift(a), lift(a), div_t, ell=True)
        add(m['A'], lift(a), lift(a), w[a], ell=True)
        for b in (1, 2, 3):
            du = deriv(u[a], b)
            add(m['X'], lift(a), lift(b), du, ell=True)
            add(m['X'], lift(b), lift(a), du, ell=True)
            if a != b:
                # C=sum c u_a V_(k,b) (curl V_l)_(ab).
                # Curl deletes the prefix exactly. Symmetrize both orders.
                curl = circulation(a, b)
                add(m['C'], lift(b), curl, u[a], .5, ell=True)
                add(m['C'], curl, lift(b), u[a], .5, ell=True)

    if cutoff <= 3:
        m['tau_direct'] = []
        for a in (1, 2, 3):
            for b in (1, 2, 3):
                first, second = lift(a), differentiated_lift(b, b)
                add(m['tau_direct'], first, second, u[a], .5, ell=True)
                add(m['tau_direct'], second, first, u[a], .5, ell=True)
                first, second = lift(b), differentiated_lift(a, b)
                add(m['tau_direct'], first, second, u[a], -.5, ell=True)
                add(m['tau_direct'], second, first, u[a], -.5, ell=True)

    panels = [(0, 1 / 32)] + [(2.**j, 2.**(j + 1)) for j in range(-5, 7)]
    t, wt = rule(panels, time_degree)
    t += 1 / 16
    heat = {typ: np.exp(-np.outer(t, f * f)) for typ, f in freq.items()}
    cache, terms, values = {}, [], {}
    for probe in (3, 6):
        values[probe] = {}
        for name, rows in m.items():
            total = 0.
            for im, (alpha, beta, cm, mm) in enumerate(rows):
                for iq, (ba, al, cq, qq) in enumerate(q[probe]):
                    if (alpha, beta) != (al, ba):
                        continue
                    product = np.ones((len(t), len(t)))
                    for j in range(4):
                        ta, tb = types(alpha)[j], types(beta)[j]
                        key = mm[j], qq[j], ta, tb
                        if key not in cache:
                            cache[key] = heat[ta] @ (matrices[mm[j]] * matrices[qq[j]].T) @ heat[tb].T
                        product *= cache[key]
                    value = float(cm * cq * (wt @ product @ wt))
                    total += value
                    terms.append(dict(probe=probe, tensor=name, M=im, Q=iq,
                                      coefficient=cm * cq, value=value))
            values[probe][name] = total
        values[probe]['tau_from_IBP'] = (values[probe]['D'] - values[probe]['X'] / 2
                                        + 2 * values[probe]['C'])
    checks = []
    if cutoff <= 3:
        for probe in (3, 6):
            actual = abs(values[probe]['tau_direct'] - values[probe]['tau_from_IBP'])
            required = 1e-7 * max(1, abs(values[probe]['tau_direct']))
            checks.append(dict(name=f'physical_IBP_{probe}', actual_error=actual,
                               required_error=required, passed=actual <= required))
    # The K<=3 dense formula uses exact diagonal inverse weights, independent
    # of the double-time rule, but shares the uncertified spatial integrals.
    if cutoff <= 3:
        sizes = [int(np.prod([len(freq[typ]) for typ in types(a)])) for a in range(4)]
        cuts = np.cumsum([0, *sizes])

        def assemble(rows):
            dense = np.zeros((cuts[-1], cuts[-1]))
            for a, b, c, ids in rows:
                block = np.ones((1, 1))
                for idx in ids:
                    block = np.kron(block, matrices[idx])
                dense[cuts[a]:cuts[a + 1], cuts[b]:cuts[b + 1]] += c * block
            return dense

        lam = np.concatenate([sum(np.meshgrid(*[freq[typ]**2 for typ in types(a)],
                                              indexing='ij')).ravel() for a in range(4)])
        f = np.exp(-lam / 16) / lam
        for probe in (3, 6):
            qd = assemble(q[probe])
            for name, rows in m.items():
                md = assemble(rows)
                direct = float(np.sum(md * qd.T * f[:, None] * f[None, :]))
                error = abs(direct - values[probe][name])
                required = 2e-9 * max(1, abs(direct))
                checks.append(dict(name=f'dense_inverse_{probe}_{name}',
                                   direct_value=direct, actual_error=error,
                                   required_error=required, passed=error <= required))
    archive = dict(x=x, spatial_weights=wx, time_nodes=t, time_weights=wt)
    archive.update({f'coefficient_{a}': b for a, b in co.items()})
    archive.update({f'basis_{a}_{b}': c for (a, b), c in basis.items()})
    archive.update({f'matrix_{idx}': mat for idx, mat in enumerate(matrices)})
    factor_path = ROOT / f'physical-h-{label}-factors.npz'
    np.savez_compressed(factor_path, **archive)
    # Exact analytic constants and heat-tail formula are proved in L132.
    volume_ell = 1296 * 7
    constants = {'D': volume_ell * 3025 * 3 / 4,
                 'X': volume_ell * 34182 * 9 / 2,
                 'A': volume_ell * 3025 * 3 / 4,
                 'C': volume_ell * 165 * 6 / 32}
    common = 2 * (4 * 12**4) * (16 * 12**3) * 512 / (9 * cutoff) * np.exp(-9 * cutoff**2 / 1024)
    tails = {p: {name: const * norm * common for name, const in constants.items()}
             for p, norm in ((3, 6050), (6, 1640736))}
    exact_tails = {}
    if cutoff == 96:
        partial = sum((Fraction(3**j, factorial(j)) for j in range(9)), Fraction(0))
        checks.append(dict(name='positive_Taylor_e_cubed',
                           exact_lower_num=str(partial.numerator),
                           exact_lower_den=str(partial.denominator),
                           required_lower=20, passed=partial > 20))
        common_exact = 2 * (4 * 12**4) * (16 * 12**3) * Fraction(512, 9 * 96)
        for probe, norm in ((3, 6050), (6, 1640736)):
            exact_tails[probe] = {}
            for name, const in constants.items():
                upper = Fraction(int(const)) * norm * common_exact / 20**27
                exact_tails[probe][name] = dict(num=str(upper.numerator), den=str(upper.denominator))
                checks.append(dict(name=f'exact_spectral_tail_{probe}_{name}',
                                   actual_upper_preview=float(upper), required_upper=5e-11,
                                   passed=upper < Fraction(5, 10**11)))
    return dict(cutoff=cutoff, spatial_degree=space_degree, time_degree=time_degree,
                implementation_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                values_diagnostic=values, exterior_tail_bound_preview=tails,
                exact_K96_tail_upper_bounds=exact_tails,
                checks=checks, failures=[c for c in checks if not c['passed']],
                tensors=dict(M=m, Q=q), matrix_keys=matrix_keys, terms=terms,
                factor_path=str(factor_path.relative_to(ROOT.parent.parent)),
                missing_error_bounds=['spatial quadrature', 'retained time quadrature',
                                      'floating arithmetic'],
                qualification='Uncertified diagnostics; no actual-probe sign or full compensation follows.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cutoff', type=int, required=True)
    parser.add_argument('--space-degree', type=int, required=True)
    parser.add_argument('--time-degree', type=int, required=True)
    parser.add_argument('--label', required=True)
    args = parser.parse_args()
    result = evaluate(args.cutoff, args.space_degree, args.time_degree, args.label)
    path = ROOT / f'physical-h-{args.label}-certificate.json'
    path.write_text(json.dumps(result, indent=2) + '\n')
    print('Actual full-probe contractions (uncertified):', result['values_diagnostic'])
    print('Analytic omitted-spectrum bounds (preview):', result['exterior_tail_bound_preview'])
    print('Required sign-certification error: below the absolute contracted value; actual retained error: unbounded')
    print('Diagnostic failures / checks:', len(result['failures']), '/', len(result['checks']))
    print('Full certificate:', path)
    print('Full factors:', result['factor_path'])
    if result['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
