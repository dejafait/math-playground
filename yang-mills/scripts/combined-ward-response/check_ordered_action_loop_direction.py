"""Exact two-edge Taylor/Wick checks and actual forest spectral samples.

The all-mesh bounds are proved in L027. Samples do not evaluate either
original-probe contraction or the complete response.
"""

from fractions import Fraction as F
from itertools import product
from functools import lru_cache
from pathlib import Path
import json
import numpy as np

DIM = 9  # six link/color variables, then formal A,B,D
ZERO = (0,) * DIM


def add(*polys):
    out = {}
    for p in polys:
        for e, c in p.items():
            out[e] = out.get(e, F(0)) + c
    return {e: c for e, c in out.items() if c}


def scale(c, p):
    return {e: c * v for e, v in p.items() if c * v}


def mul(p, q):
    out = {}
    for e, c in p.items():
        for f, d in q.items():
            g = tuple(a + b for a, b in zip(e, f))
            out[g] = out.get(g, F(0)) + c * d
    return {e: c for e, c in out.items() if c}


def dot(u, v):
    return add(*(mul(a, b) for a, b in zip(u, v)))


def deriv(p, i):
    out = {}
    for e, c in p.items():
        if e[i]:
            f = list(e)
            f[i] -= 1
            out[tuple(f)] = c * e[i]
    return out


def dump(p):
    return {','.join(map(str, e)): str(c) for e, c in sorted(p.items())}


variables = [{tuple(int(i == k) for i in range(DIM)): F(1)} for k in range(DIM)]
u, v = variables[:3], variables[3:6]
A, B, D = variables[6:]
uu, vv, uv = dot(u, u), dot(v, v), dot(u, v)
# Independently multiply the scalar parts of two SU(2) exponential series.
trace4 = add(scale(F(1, 384), mul(uu, uu)), scale(F(1, 384), mul(vv, vv)),
             scale(F(1, 64), mul(uu, vv)),
             scale(F(1, 96), mul(uv, add(uu, vv))))
sum_norm = add(uu, vv, scale(2, uv))
q_trace = add(scale(-4, trace4), scale(F(1, 96), mul(sum_norm, sum_norm)))
q_cross = scale(F(-1, 24), add(mul(uu, vv), scale(-1, mul(uv, uv))))
cov = [[{} for _ in range(6)] for _ in range(6)]
for c in range(3):
    cov[c][c], cov[c+3][c+3] = A, B
    cov[c][c+3] = cov[c+3][c] = D


def contraction(p):
    return scale(F(1, 2), add(*(mul(cov[i][j], deriv(deriv(p, i), j))
                               for i, j in product(range(6), repeat=2))))


q2 = contraction(q_trace)
q2_expected = scale(F(-1, 12), add(mul(B, uu), mul(A, vv), scale(-2, mul(D, uv))))
checks = [
    {'type': 'trace_quartic_minus_radial', 'defect': dump(add(q_trace, scale(-1, q_cross))),
     'passed': q_trace == q_cross},
    {'type': 'quadratic_wick_polynomial', 'actual': dump(q2), 'required': dump(q2_expected),
     'passed': q2 == q2_expected},
]
# Full normal-order identity: q=:q:+:Q2:+E[q].
constant = scale(F(1, 2), contraction(q2))
constant_expected = scale(F(-1, 4), add(mul(A, B), scale(-1, mul(D, D))))
wick4 = add(q_trace, scale(-1, q2), constant)
wick2 = add(q2, scale(-1, contraction(q2)))
identity_defect = add(wick4, wick2, constant, scale(-1, q_trace))
checks.append({'type': 'normal_order_identity', 'constant': dump(constant),
               'required_constant': dump(constant_expected), 'defect': dump(identity_defect),
               'passed': constant == constant_expected and not identity_defect})


def substitute_parameters(p, aa, bb, dd):
    out = {}
    for e, c in p.items():
        f = e[:6]
        out[f] = out.get(f, F(0)) + c * aa**e[6] * bb**e[7] * dd**e[8]
    return {e: c for e, c in out.items() if c}


for aa, bb, dd in ((F(2), F(3), F(-1)), (F(1), F(1), F(-1)), (F(5), F(7), F(0))):
    covariance = [[F(0) for _ in range(6)] for _ in range(6)]
    for c in range(3):
        covariance[c][c], covariance[c+3][c+3] = aa, bb
        covariance[c][c+3] = covariance[c+3][c] = dd

    @lru_cache(None)
    def moment(e):
        if not sum(e):
            return F(1)
        if sum(e) % 2:
            return F(0)
        i = next(k for k, count in enumerate(e) if count)
        left = list(e)
        left[i] -= 1
        total = F(0)
        for j, count in enumerate(left):
            if count:
                tail = left.copy()
                tail[j] -= 1
                total += count * covariance[i][j] * moment(tuple(tail))
        return total

    def expect(p):
        return sum(c * moment(e) for e, c in substitute_parameters(p, aa, bb, dd).items())

    values = [expect(q_trace), expect(wick4), expect(wick2)]
    required = [-(aa * bb - dd**2) / 4, F(0), F(0)]
    checks.append({'type': 'exact_gaussian_moments', 'A_B_D': list(map(str, (aa, bb, dd))),
                   'actual': list(map(str, values)), 'required': list(map(str, required)),
                   'passed': values == required})


def spectral_sample(n):
    """Signed active-edge covariance for plane (1,2), tail (j,j,j,j)."""
    j = n // 2
    eigen = 4 * np.sin(np.pi * np.arange(n) / (2*n))**2
    ks = [np.arange(n), *[np.arange(1, n) for _ in range(3)]]
    denominator = sum(eigen[k].reshape(tuple(-1 if r == axis else 1 for r in range(4)))
                      for axis, k in enumerate(ks))
    k = ks[0]
    pref = []
    for level in (j, j+1):
        wave = np.empty(n)
        wave[0] = level / np.sqrt(n)
        wave[1:] = (np.sqrt(2/n) * np.sin(np.pi * k[1:] * level / n)
                    / (2 * np.sin(np.pi * k[1:] / (2*n))))
        pref.append(wave)
    transverse = np.sqrt(2/n) * (np.sin(np.pi * ks[1] * (j+1)/n)
                                - np.sin(np.pi * ks[1] * j/n))
    base = transverse[None, :, None, None]**2
    for axis in (2, 3):
        shape = tuple(-1 if r == axis else 1 for r in range(4))
        base = base * (np.sqrt(2/n)*np.sin(np.pi*ks[axis]*j/n)).reshape(shape)**2
    path = [[float(np.sum(base * (pref[r]*pref[s])[:, None, None, None] / denominator))
             for s in range(2)] for r in range(2)]
    dks = [np.arange(1, n), np.arange(n), np.arange(1, n), np.arange(1, n)]
    direct_den = sum(eigen[k].reshape(tuple(-1 if r == axis else 1 for r in range(4)))
                     for axis, k in enumerate(dks))
    base = np.ones(tuple(len(k) for k in dks))
    for axis in (1, 2, 3):
        if axis == 1:
            wave = np.sqrt(2/n) * np.cos(np.pi*dks[axis]*(j+.5)/n)
            wave[0] = 1 / np.sqrt(n)
        else:
            wave = np.sqrt(2/n) * np.sin(np.pi*dks[axis]*j/n)
        base *= (wave**2).reshape(tuple(-1 if r == axis else 1 for r in range(4)))
    waves = [np.sqrt(2/n)*np.sin(np.pi*dks[0]*level/n) for level in (j, j+1)]
    direct = [[float(np.sum(base * (waves[r]*waves[s])[:, None, None, None] / direct_den))
               for s in range(2)] for r in range(2)]
    total = np.array(path) + np.array(direct)
    aa, bb, dd = float(total[1, 1]), float(total[0, 0]), float(-total[0, 1])
    ee, ff = aa + bb + 2*dd, aa + bb - 2*dd
    matrix = -np.array([[bb, -dd], [-dd, aa]]) / 12
    norm = float(np.max(np.abs(np.linalg.eigvalsh(matrix))))
    required = [(2*j+1)/192, (2*j+17)/12]
    alpha_bounds = [(2*j-3)/192, (2*j+17)/24]
    ok = (j/8 <= bb <= j+8 and (j+1)/8 <= aa <= j+9
          and -1e-10 <= ee <= 1+1e-10 and aa*bb >= dd**2-1e-10
          and required[0] <= norm <= required[1]
          and alpha_bounds[0] <= ff/48 <= alpha_bounds[1]
          and (aa-bb)**2 <= ee*ff+1e-10)
    return {'type': 'actual_relative_spectrum', 'N': n, 'j': j, 'A': aa, 'B': bb, 'D': dd,
            'curvature_variance_E': ee, 'required_E_bounds': [0, 1],
            'negative_quadratic_matrix': matrix.tolist(), 'norm': norm,
            'required_norm_bounds': required, 'curvature_square_coefficient_magnitude': ff/48,
            'required_coefficient_bounds': alpha_bounds,
            'cross_coefficient_squared': (aa-bb)**2, 'required_cross_upper': ee*ff,
            'passed': bool(ok)}


checks.extend(spectral_sample(n) for n in (4, 8, 16, 32))
failures = [i for i, check in enumerate(checks) if not check['passed']]
destination = Path(__file__).with_name('ordered-action-loop-direction-certificate.json')
destination.write_text(json.dumps({'scope': 'Exact algebra and finite spectral samples; analytic bounds in L027; no probe response or full logarithm.',
                                   'checks': checks, 'failures': failures}, indent=2) + '\n')
print(f'Exact algebra/moment checks: {sum(c["passed"] for c in checks[:6])}/6')
for check in checks[6:]:
    print(f'N={check["N"]}: norm={check["norm"]:.9g}, required={check["required_norm_bounds"]}; '
          f'E={check["curvature_variance_E"]:.9g}, required=[0,1]; '
          f'alpha={check["curvature_square_coefficient_magnitude"]:.9g}, '
          f'required={check["required_coefficient_bounds"]}; passed={check["passed"]}')
print(f'Failures={failures}; certificate={destination}')
if failures:
    raise SystemExit(1)
