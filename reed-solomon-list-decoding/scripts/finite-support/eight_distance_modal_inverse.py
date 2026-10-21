"""Small-block inverse proposal for the same immutable fixed column.

The full original action residual, rather than trust in modal inversion,
certifies this vector. This is an alternative solve of the same target.
"""
import json
import sys
from fractions import Fraction as F
from math import lcm
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
OUT = ROOT/'eight-distance-modal-inverse-results.json'


def enc(x):
    if isinstance(x, F):
        return [x.numerator, x.denominator]
    if isinstance(x, dict):
        return {str(k): enc(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [enc(v) for v in x]
    return x


def range_solve(B, b):
    rows = [[F(*x) for x in row]+[v] for row, v in zip(B, b)]
    pivots = []
    n = len(b)
    for j in range(n):
        r = len(pivots)
        p = next((p for p in range(r, n) if rows[p][j]), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        d = rows[r][j]
        rows[r] = [x/d for x in rows[r]]
        for s in range(n):
            if s != r:
                v = rows[s][j]
                rows[s] = [x-v*y for x, y in zip(rows[s], rows[r])]
        pivots.append(j)
    if any(row[-1] for row in rows[len(pivots):]):
        raise ValueError('Inconsistent modal inverse')
    z = [F(0)]*n
    for r, j in enumerate(pivots):
        z[j] = rows[r][-1]
    return z


def main():
    got = json.loads((ROOT/'eight-distance-fixed-column-energy-results.json').read_text())
    data = json.loads((ROOT/'eight-distance-full-base-kernel-results.json').read_text())
    os, W = got['orbits'], got['weights']
    b = [F(*v) for v in got['column']]
    factors = {(r['n'], r['layer']): [[F(*x) for x in row] for row in r['basis']]
               for r in data['factor_bases']}
    z, modes = [F(0)]*150, []
    for block in data['blocks']:
        a, bb = block['mode']
        ls = block['layers']
        rhs = []
        for l, norm in zip(ls, block['norms']):
            rhs.append(b[0] if l == 0 else sum(w*y*factors[68, l][a][i]*factors[956, l][bb][j]
                for (m, i, j), w, y in zip(os, W, b) if m == l)/F(*norm))
        local = range_solve(block['action'], rhs)
        for t, (l, i, j) in enumerate(os):
            if l in ls:
                z[t] += local[ls.index(l)]*(F(1) if l == 0 else factors[68, l][a][i]*factors[956, l][bb][j])
        modes.append({'mode': block['mode'], 'layers': ls, 'rhs': rhs, 'inverse': local})
    print('All 64 small-block solves completed; checking full original action.', flush=True)
    Q = [[F(*x) for x in row] for row in got['action']]
    zd = lcm(*(x.denominator for x in z))
    zi = [int(x*zd) for x in z]
    residuals = []
    for row, v in zip(Q, b):
        d = lcm(*(x.denominator for x in row))
        residuals.append(F(sum(int(x*d)*y for x, y in zip(row, zi)), d*zd)-v)
    terms = [w*x*y for w, x, y in zip(W, b, z)]
    energy, p8 = sum(terms), F(16792471, 1181138102168120460)
    ratio = energy/p8
    lo = F(ratio.numerator*10**12//ratio.denominator, 10**12)
    hi = lo+F(1, 10**12)
    failures = [str(i) for i, v in enumerate(residuals) if v]
    if energy < 0:
        failures.append('negative_energy')
    verdict = 'PSD_EXTENSION' if energy <= p8 else 'FIXED_COLUMN_REJECTED'
    out = {'modes': modes, 'inverse_action': z, 'inverse_residuals': residuals,
           'weighted_energy_contributions': terms, 'energy': energy, 'energy_ratio': ratio,
           'required_diagonal': p8, 'schur_remainder': p8-energy, 'failures': failures,
           'summary': {'verdict': verdict, 'all_150_original_residuals_zero': not any(residuals),
                       'ratio_interval': [lo, hi], 'required_ratio_upper_bound': 1,
                       'failures': len(failures)}}
    OUT.write_text(json.dumps(enc(out), indent=2)+'\n')
    print('Energy/p8 in [', lo, ',', hi, '); required <= 1; verdict:', verdict)
    print('All 150 original residuals zero:', not any(residuals), '; failures:', failures)
    print('Full certificate:', OUT.relative_to(ROOT.parent.parent))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
