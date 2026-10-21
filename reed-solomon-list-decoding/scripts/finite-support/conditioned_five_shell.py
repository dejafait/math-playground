"""One fixed L053 shell: exact complete product spectrum, no retuning."""
import json
from fractions import Fraction as Q
from math import comb
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / 'conditioned-five-shell-results.json'


def enc(x):
    return [x.numerator, x.denominator]


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def factor(n):
    return [[sum((-1)**h * choose(a, h) * choose(5-a, r-h)
                 * choose(n-5-a, r-h) for h in range(r+1))
             for r in range(6)] for a in range(6)]


def main():
    lp = json.loads((ROOT / 'delsarte-lp-results.json').read_text())
    p = [Q(1)] + [Q(0)] * 4 + [
        Q(z['numerator'], z['denominator']) / (2*comb(68, i)*comb(956, i))
        for i, z in zip(range(5, 69), lp['exact']['primal'])]
    old = json.loads((ROOT / 'selected-triple-sdp-results.json').read_text())
    assert list(map(enc, p)) == old['p'] and p[5] > 0 and p[68] > 0
    alpha = p[5]**2 / p[68]
    # c is the shell block after division by rho, not conditional orbit counts.
    c = [[p[5] if r+q == 0 else Q(0) if r+q < 5 or (r, q) == (2, 3)
          else alpha*p[r+q] for q in range(6)] for r in range(6)]
    factors = {n: factor(n) for n in (68, 956)}
    mult = {n: [choose(n, a)-choose(n, a-1) for a in range(6)]
            for n in (68, 956)}
    size = comb(68, 5)*comb(956, 5)
    modes = []
    for a in range(6):
        for b in range(6):
            eigen = sum(c[r][q]*factors[68][a][r]*factors[956][b][q]
                        for r in range(6) for q in range(6))
            correction = p[5]**2*size if (a, b) == (0, 0) else Q(0)
            modes.append({'a': a, 'b': b, 'multiplicity': mult[68][a]*mult[956][b],
                          'shell_over_rho': enc(eigen),
                          'shell_scaled': enc(eigen/alpha),
                          'anchor_correction_over_rho': enc(correction),
                          'schur_over_rho': enc(eigen-correction),
                          'schur_scaled': enc((eigen-correction)/alpha)})
    negatives = [[z['a'], z['b']] for z in modes if Q(*z['schur_over_rho']) < 0]
    data = {'parameters': {'n': 1024, 'w': 68, 'tail': 956, 'shell_distance': 5,
                           'p': list(map(enc, p)), 'alpha': enc(alpha), 'size': size,
                           'anchor_over_rho': [1, 1], 'anchor_shell_over_rho': enc(p[5])},
            'coefficient_table_over_rho': [[enc(x) for x in row] for row in c],
            'coefficient_table_scaled': [[enc(x/alpha) for x in row] for row in c],
            'factors': [{'n': n, 'eigenmatrix': factors[n], 'multiplicities': mult[n]}
                        for n in (68, 956)],
            'modes': modes,
            'summary': {'mode_count': len(modes), 'dimension_sum': sum(z['multiplicity'] for z in modes),
                        'negative_modes': negatives, 'anchored_psd': not negatives,
                        'verdict': 'FIXED_TRIAL_EXCLUDED' if negatives else 'SHELL_PASSES'},
            'failures': []}
    assert len(modes) == 36 and data['summary']['dimension_sum'] == size
    assert sum(Q(*z['shell_over_rho'])*z['multiplicity'] for z in modes) == size*p[5]
    OUT.write_text(json.dumps(data, separators=(',', ':'))+'\n')
    print('Actual/required product modes: 36/36; dimension:', size)
    print('Exact negative Schur modes:', negatives, '; required for PSD: none')
    print('Arithmetic failures: 0; fixed-trial verdict:', data['summary']['verdict'])
    print('Certificate:', OUT)


if __name__ == '__main__':
    main()
