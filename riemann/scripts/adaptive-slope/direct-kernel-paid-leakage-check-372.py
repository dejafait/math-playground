#!/usr/bin/env python3
"""Replay finite certificates and selected independent integral evaluations."""
import importlib.util
import json
from fractions import Fraction as F
from math import comb, factorial, isqrt
from pathlib import Path

HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location('paid372', HERE/'direct-kernel-paid-leakage-372.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)
m = p.m


def polynomial(n):
    # Laguerre recurrence, independent of the antiderivative binomial formula.
    older, current = [F(1)], [F(3), F(-1)]
    for j in range(1, n+1):
        nxt = [F(0)]*(len(current)+1)
        for k, a in enumerate(current):
            nxt[k] += (2*j+3)*a
            nxt[k+1] -= a
        for k, a in enumerate(older):
            nxt[k] -= (j+2)*a
        older, current = current, [a/(j+1) for a in nxt]
    current = [a/(n+1) for a in current]
    current[0] -= F(1, n+1)
    return current


def direct_integral(poly, ar, ai, a, b):
    center, half = (a+b)/2, (b-a)/2
    shifted = [sum(poly[j]*comb(j, k)*center**(j-k)
                   for j in range(k, len(poly))) for k in range(len(poly))]
    powers = [half**k for k in range(len(poly)+130)]
    alpha = m.C(ar, ai)
    total, term = m.C(0), m.C(1)
    for k in range(129):
        moment = sum(2*d*powers[j+k+1]/(j+k+1)
                     for j, d in enumerate(shifted) if (j+k) % 2 == 0)
        total = total+term*moment
        term = term*alpha/(k+1)
    bound = (abs(ar)+abs(ai))*half
    assert bound/F(130) < F(1, 2)
    tail = 2*bound**129/factorial(129)
    polynomial_majorant = 2*half*sum(abs(d)*powers[j] for j, d in enumerate(shifted))
    radius = m.R(tail*polynomial_majorant).hi
    total = total+m.C(m.R(-radius, radius), m.R(-radius, radius))
    return m.exact_exp(ar*center, ai*center)*total


def alternate_kernel(n, c, zr, zi):
    poly, total = polynomial(n), m.C(0)
    for base in (F(-1, 8), F(-7, 8)):
        ar, ai = base-zi, zr
        total = total-(direct_integral(poly, ar, ai, c*n, c*(n+2))
                       -direct_integral(poly, ar, ai, F(n), F(n+2)))
    return total*m.exact_exp(-c*n/4)


def overlaps(a, b):
    return all(max(x.lo, y.lo) <= min(x.hi, y.hi)
               for x, y in [(a.re, b.re), (a.im, b.im)])


result = {'status': 'CHECKING', 'failures': [], 'runs': [],
          'optimality_checked': False, 'asymptotic_rate_checked': False,
          'conceptual_audit': 'PENDING'}
for n in [16, 32]:
    row = json.loads((HERE/f'direct-kernel-paid-leakage-matrix-{n}-372.json').read_text())
    cert = json.loads((HERE/f'direct-kernel-paid-leakage-{n}-372.json').read_text())
    slopes = [F(c) for c in row['slopes']]
    gammas = [F(g) for g in row['gammas']]
    assert slopes == [F(7, 4)+F(l, 8*n) for l in range(4*n+1)]
    assert gammas == [F(15, 8)+F(j, 4*n) for j in range(n+1)]
    columns = []
    for j, g in enumerate(gammas):
        col = m.kernel_column(n, slopes, g, F(0))
        assert [v.json() for v in col] == row['kernel_columns'][j]
        columns.append(col)
        if j % 8 == 0:
            print(f'n={n}: full kernel replay band column {j}/{n}', flush=True)
    target = m.kernel_column(n, slopes, F(1), F(1, 8))
    assert [v.json() for v in target] == row['target_column']
    checks = []
    # Closed endpoints and center, at both band endpoints and target.
    for index in [0, 2*n, 4*n]:
        for j in [0, n]:
            val = alternate_kernel(n, slopes[index], gammas[j], F(0))
            passed = overlaps(val, columns[j][index])
            checks.append({'slope_index': index, 'band_index': j,
                           'alternate_kernel': val.json(), 'overlap': passed})
            assert passed
        val = alternate_kernel(n, slopes[index], F(1), F(1, 8))
        passed = overlaps(val, target[index])
        checks.append({'slope_index': index, 'target': True,
                       'alternate_kernel': val.json(), 'overlap': passed})
        assert passed
    scores = []
    for candidate in cert['results']:
        weights = [(F(r), F(i)) for r, i in candidate['rational_weights']]
        assert len(weights) == len(slopes)
        # Independent EXACT rational upper bound, no Decimal square roots.
        # For each rational squared modulus q, enclose sqrt(q) at 10^-80.
        den = 10**80
        tv_upper = sum(F(isqrt((r*r+i*i).numerator*den*den//
                              (r*r+i*i).denominator)+1, den) for r, i in weights)
        assert tv_upper <= 1
        tp = m.pairing(weights, target)
        bp = [m.pairing(weights, col) for col in columns]
        assert tp.json() == candidate['target_pairing']
        assert [v.json() for v in bp] == candidate['band_pairings']
        budget = m.exp_ball(m.C(p.sqrt_bounds(m.D(n)))).re
        leakage = max(p.modulus(v).hi for v in bp)
        raw = m.LO.subtract(p.modulus(tp).lo, m.HI.multiply(budget.hi, leakage))
        score = max(m.D(0), raw)
        assert str(raw) == candidate['raw_score_lower']
        assert str(score) == candidate['E_n_lower']
        assert str(leakage) == candidate['band_modulus_upper']
        assert budget.json() == candidate['budget']
        assert str(m.LO.multiply(score, m.exact_exp(F(n, 64)).re.lo)) == candidate['scaled_lower']
        scores.append(score)
    best = max(range(len(scores)), key=lambda i: scores[i])
    assert best == cert['best_index']
    assert str(scores[best]) == cert['best_lower']
    result['runs'].append({'n': n, 'all_kernel_entries_replayed': (n+2)*(4*n+1),
                           'all_rational_candidates_replayed': len(scores),
                           'best_index': best, 'best_lower': str(scores[best]),
                           'independent_integral_checks': checks,
                           'all_assertions_passed': True})
    print(f'n={n}: {len(scores)} rational witnesses replayed; {len(checks)} independent integrals passed; best lower={scores[best]:.8E}', flush=True)
    m.exact_exp.cache_clear()
result['status'] = 'PASS_FINITE_ONLY'
path = HERE/'direct-kernel-paid-leakage-check-372.json'
p.save(path, result)
print('Failures: 0; required unbounded-subsequence rate: UNPROVED; full check:', path, flush=True)
