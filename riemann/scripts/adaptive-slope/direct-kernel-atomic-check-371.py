#!/usr/bin/env python3
"""Replay all rational witnesses; cross-check kernels by a second integral formula."""
import importlib.util
import json
from fractions import Fraction as F
from math import comb, factorial, isqrt
from pathlib import Path

HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location('atomic371', HERE/'direct-kernel-atomic-371.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def polynomial(n):
    # Independent Laguerre three-term recurrence, not the binomial formula.
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


def direct_integral(p, ar, ai, a, b):
    center, half = (a+b)/2, (b-a)/2
    shifted = [sum(p[j]*comb(j, k)*center**(j-k) for j in range(k, len(p)))
               for k in range(len(p))]
    powers = [half**k for k in range(len(p)+130)]
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
    p, total = polynomial(n), m.C(0)
    for base in (F(-1, 8), F(-7, 8)):
        ar, ai = base-zi, zr
        total = total-(direct_integral(p, ar, ai, c*n, c*(n+2))
                       -direct_integral(p, ar, ai, F(n), F(n+2)))
    return total*m.exact_exp(-c*n/4)


def decode(v):
    return m.C(m.R(*v['re']), m.R(*v['im']))


def overlaps(a, b):
    return all(max(x.lo, y.lo) <= min(x.hi, y.hi)
               for x, y in [(a.re, b.re), (a.im, b.im)])


source = HERE/'direct-kernel-atomic-371.json'
data = json.loads(source.read_text())
result = {'status': 'CHECKING', 'failures': [], 'runs': []}
thresholds = {4: m.D('0.00015754'), 8: m.D('0.00000019683'),
              12: m.D('0.0000000012461'), 16: m.D('0.0000000000036086')}
for row in data['runs']:
    n = row['n']
    slopes = [F(c) for c in row['slopes']]
    gammas = [F(g) for g in row['gammas']]
    assert slopes == [F(7, 4)+F(l, 2*(n+1)) for l in range(n+2)]
    assert gammas == [F(15, 8)+F(j, 4*n) for j in range(n+1)]
    weights = [(F(r), F(i)) for r, i in row['rational_weights']]
    assert len(weights) == len(slopes)
    assert sum(abs(r)+abs(i) for r, i in weights) == 1
    columns = [m.kernel_column(n, slopes, g, F(0)) for g in gammas]
    target = m.kernel_column(n, slopes, F(1), F(1, 8))
    assert [[v.json() for v in col] for col in columns] == row['kernel_columns']
    assert [v.json() for v in target] == row['target_column']
    tp = m.pairing(weights, target)
    bp = [m.pairing(weights, col) for col in columns]
    assert tp.json() == row['target_pairing']
    assert [p.json() for p in bp] == row['band_pairings']
    leakage = max(p.upper_abs() for p in bp)
    den = 10**80
    root = isqrt(n*den*den)
    budget_upper = m.exp_ball(m.C(m.R(m.R(F(root, den)).lo,
                                    m.R(F(root+1, den)).hi))).re.hi
    lower = max(m.D(0), m.LO.subtract(tp.lower_abs(), m.HI.multiply(budget_upper, leakage)))
    assert str(lower) == row['E_n_lower']
    assert lower > thresholds[n]
    # Check every n=4 band entry; larger n: two band corners and central target.
    cases = [(c, g, F(0), columns[j][l]) for j, g in enumerate(gammas)
             for l, c in enumerate(slopes)] if n == 4 else [
        (slopes[0], gammas[0], F(0), columns[0][0]),
        (slopes[-1], gammas[-1], F(0), columns[-1][-1])]
    cases += [(slopes[len(slopes)//2], F(1), F(1, 8), target[len(slopes)//2])]
    checks = []
    for c, zr, zi, val in cases:
        alternate = alternate_kernel(n, c, zr, zi)
        passed = overlaps(val, alternate)
        checks.append({'c': str(c), 'z': [str(zr), str(zi)],
                       'alternate_integral': alternate.json(), 'overlap': passed})
        if not passed:
            result['failures'].append({'n': n, 'c': str(c), 'z': [str(zr), str(zi)]})
    result['runs'].append({'n': n, 'replay_exact': True,
                           'claimed_safe_lower': str(thresholds[n]),
                           'all_n_rate_checked': False, 'cross_checks': checks})
    print(f'n={n}: all rational weights/kernel entries/pairings replayed; {len(checks)} independent integral comparisons; safe lower>{thresholds[n]}', flush=True)
    m.exact_exp.cache_clear()
result['status'] = 'PASS_FINITE_ONLY' if not result['failures'] else 'FAIL'
out = HERE/'direct-kernel-atomic-check-371.json'
out.write_text(json.dumps(result, indent=2)+'\n')
print('Failures:', len(result['failures']), '; required asymptotic rate remains UNPROVED')
print('Full check certificate:', out)
if result['failures']:
    raise SystemExit(1)
