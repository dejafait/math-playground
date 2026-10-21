"""Independent complete replay of L109's small fixed certificate.

No producer imports. Run from the active notebook with python3.
This checks four fixed supports, not arbitrary t=0 profiles.
"""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import hashlib
import json
import subprocess
import sys

P = 97
ROOT = Path(__file__).parent
SOURCE = ROOT / 'zero-anchor-support-filter.json'
OUT = ROOT / 'zero-anchor-critical-audit.json'


def det_exact(matrix):
    """Rational Gaussian elimination, independent of producer's Bareiss path."""
    a = [[Fraction(x) for x in row] for row in matrix]
    out = Fraction(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            out = -out
        value = a[j][j]
        out *= value
        a[j] = [x / value for x in a[j]]
        for i in range(j + 1, len(a)):
            factor = a[i][j]
            a[i] = [x - factor * y for x, y in zip(a[i], a[j])]
    assert out.denominator == 1
    return out.numerator


def rank(matrix):
    a = [[x % P for x in row] for row in matrix]
    row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col], -1, P)
        a[row] = [x * inv % P for x in a[row]]
        for i in range(len(a)):
            if i != row:
                factor = a[i][col]
                a[i] = [(x - factor * y) % P for x, y in zip(a[i], a[row])]
        row += 1
        if row == len(a):
            break
    return row


def polynomial(roots):
    out = [1]
    for root in roots:
        new = [0] * (len(out) + 1)
        for d, coeff in enumerate(out):
            new[d] = (new[d] - root * coeff) % P
            new[d + 1] = (new[d + 1] + coeff) % P
        out = new
    return out


def evaluate(coeffs, x):
    value = 0
    for coeff in reversed(coeffs):
        value = (value * x + coeff) % P
    return value


def run():
    raw = SOURCE.read_bytes()
    saved = json.loads(raw)
    failures, checks = [], []

    def check(label, actual, expected):
        passed = actual == expected
        checks.append({'check': label, 'passed': passed})
        if not passed:
            failures.append({'check': label, 'actual': actual, 'expected': expected})

    replay = subprocess.run([sys.executable, str(ROOT / 'zero_anchor_support_filter.py')],
                            capture_output=True, text=True)
    check('producer replay exit status', replay.returncode, 0)
    check('producer certificate reproduced byte for byte', SOURCE.read_bytes() == raw, True)

    # Generate the subgroup by powers, not the producer's root-membership scan.
    h = sorted({pow(8, j, P) for j in range(16)})
    s = [1, 8, 12, 18, 22, 27, 33]
    jset = sorted(set(h) - set(s))
    supports = [([1, 8], [47, 50]), ([12, 18], [64, 70]),
                ([22, 27], [75, 79]), ([1, 33], [85, 89])]
    pairs = list(combinations(s, 2))
    check('subgroup order', len(h), 16)
    check('subgroup generator order', pow(8, 8, P), 96)
    check('modulus', saved['modulus'], P)
    check('H', saved['H'], h)
    check('S', saved['S'], s)
    check('J', saved['J'], jset)
    check('all 21 column pairs', saved['column_pairs'], [list(x) for x in pairs])
    check('four saved blocks', len(saved['blocks']), 4)
    blocks, quotient_maps, gs, pivots = [], [], [], []
    for number, (i, k) in enumerate(supports):
        coeffs = polynomial(sorted(set(jset) - set(k)))
        g = {x: evaluate(coeffs, x) for x in h}
        gs.append(g)
        observed = sorted(set(s) - set(i))
        z = observed[0]
        pivots.append(z)
        check(f'block {number} exact seven-root codeword',
              [x for x in h if not g[x]], sorted(set(jset) - set(k)))
        # Ratio quotient d_x(w)=w_x/g(x)-w_z/g(z).
        # Original c_x=g(z)g(x)d_x; its wedge row scales by g(z)^2 g(x)g(y).
        d = {x: [((pow(g[x], -1, P) if a == x else 0)
                    - (pow(g[z], -1, P) if a == z else 0)) % P
                   for a in s] for x in observed[1:]}
        quotient_maps.append(list(d.values()))
        covectors = [[value * g[z] * g[x] % P for value in d[x]]
                     for x in observed[1:]]
        matrix = []
        for x, y in combinations(observed[1:], 2):
            scale = g[z] * g[z] * g[x] * g[y] % P
            matrix.append([scale * (d[x][s.index(a)] * d[y][s.index(b)]
                                    - d[x][s.index(b)] * d[y][s.index(a)]) % P
                           for a, b in pairs])
        blocks.append(matrix)
        expected = {'I': i, 'K': k, 'pivot': z,
                    'covectors': covectors, 'matrix': matrix}
        check(f'block {number} every saved field and entry', saved['blocks'][number], expected)
        check(f'block {number} quotient rank', rank(list(d.values())), 4)
        check(f'block {number} exterior rank', rank(matrix), 6)

    matrix = [row for block in blocks for row in block]
    prefix = [rank(matrix[:6 * n]) for n in range(1, 5)]
    minor = matrix[:21]
    integer_det = det_exact(minor)
    check('prefix ranks', prefix, [6, 12, 18, 21])
    check('saved prefix ranks', saved['prefix_ranks'], prefix)
    check('saved actual rank', saved['actual_rank'], 21)
    check('required exclusion rank', saved['required_exclusion_rank'], 21)
    check('complete minor row indices', saved['minor_row_indices_zero_based'], list(range(21)))
    check('all 441 minor entries', saved['minor'], minor)
    check('integer determinant', integer_det, -87637416100784452193048153074475550000)
    check('saved integer determinant', saved['integer_minor_determinant'], integer_det)
    check('saved modular determinant', saved['minor_determinant'], integer_det % P)
    check('nonzero determinant residue', integer_det % P, 28)
    intersections = [len(set(i + k) & set(ii + kk))
                     for (i, k), (ii, kk) in combinations(supports, 2)]
    check('all six support intersections', saved['pair_intersections'], intersections)
    check('pairwise linearity', max(intersections) <= 1, True)

    endpoints = [[(gs[n][x] + (x in supports[n][0])) % P for x in s]
                 for n in range(2)]
    u, v = endpoints[0], [(b - a) % P for a, b in zip(*endpoints)]
    p = {(a, b): (u[s.index(a)] * v[s.index(b)]
                   - u[s.index(b)] * v[s.index(a)]) % P for a, b in pairs}

    def alt(a, b):
        return 0 if a == b else (p[a, b] if a < b else -p[b, a]) % P

    plucker = [(alt(a, b) * alt(c, d) - alt(a, c) * alt(b, d)
                + alt(a, d) * alt(b, c)) % P for a, b, c, d in combinations(s, 4)]
    check('all 35 Plucker equations', plucker, [0] * 35)
    reconstruction_pivots = []
    for a, b in pairs:
        if not alt(a, b):
            continue
        uu = {x: alt(x, b) * pow(alt(a, b), -1, P) % P for x in s}
        vv = {x: alt(a, x) for x in s}
        check(f'decomposable reconstruction pivot {a},{b}',
              [(uu[x] * vv[y] - uu[y] * vv[x]) % P for x, y in pairs], list(p.values()))
        reconstruction_pivots.append([a, b])

    weights, moments, projective_gates, locator_evaluations = [], [], [], []
    for n, (i, k) in enumerate(supports[:2]):
        error = {x: (1 if x in i else -gs[n][x]) % P for x in sorted(i + k)}
        weights.append({str(x): value for x, value in error.items()})
        residuals = [sum(((endpoints[n][s.index(x)] if x in s else 0) - error.get(x, 0))
                         * pow(x, d, P) for x in h) % P for d in range(1, 9)]
        moments.append(residuals)
        check(f'control {n} all eight moments', residuals, [0] * 8)
        qu = [sum(c * a for c, a in zip(row, u)) % P for row in quotient_maps[n]]
        qv = [sum(c * a for c, a in zip(row, v)) % P for row in quotient_maps[n]]
        restriction_rank = rank([[a, b] for a, b in zip(qu, qv)])
        check(f'control {n} projected rank one', restriction_rank, 1)
        check(f'control {n} finite direction', [(a + n * b) % P for a, b in zip(qu, qv)], [0] * 4)
        lam = endpoints[n][s.index(pivots[n])] * pow(gs[n][pivots[n]], -1, P) % P
        check(f'control {n} nonzero lambda', lam, 1)
        check(f'control {n} both overlap weights',
              [(endpoints[n][s.index(x)] - lam * gs[n][x]) % P for x in i], [1, 1])
        check(f'control {n} four nonzero weights', all(error.values()), True)
        syndromes = [sum(endpoints[n][s.index(x)] * pow(x, d, P) for x in s) % P
                     for d in range(1, 9)]
        hankel = [[syndromes[a + b] for b in range(4)] for a in range(4)]
        determinant = det_exact(hankel) % P
        check(f'control {n} actual D nonzero', determinant != 0, True)
        locator_rows = [[syndromes[a + b] for b in range(5)] for a in range(4)]
        locators = {x: det_exact(locator_rows + [[pow(x, d, P) for d in range(5)]]) % P for x in h}
        expected_locators = {x: determinant * evaluate(polynomial(sorted(error)), x) % P for x in h}
        check(f'control {n} all sixteen actual locator values', locators, expected_locators)
        locator_evaluations.append({'D': determinant, 'locators': locators})
        projective_gates.append({'rank': restriction_rank, 'lambda': lam,
                                 'original_alpha': 1, 'original_beta': n})
    check('every locator has a nonzero control value',
          all(any(row['locators'][x] for row in locator_evaluations) for x in h), True)
    residuals = [sum(a * b for a, b in zip(row, p.values())) % P for row in matrix[:12]]
    expected_control = {'u': u, 'v': v, 'bivector': list(p.values()),
                        'matrix_residuals': residuals, 'errors': weights,
                        'moment_residuals': moments}
    check('entire saved positive control', saved['positive_control'], expected_control)
    check('all twelve control matrix residuals', residuals, [0] * 12)
    check('saved producer failures', saved['failures'], [])
    out = {'scope': 'L109 audit: four fixed rows and complete two-row positive control only',
           'source_sha256': hashlib.sha256(raw).hexdigest(),
           'producer_replay': {'returncode': replay.returncode,
                               'stdout': replay.stdout.strip(), 'stderr': replay.stderr.strip()},
           'independence': 'No producer imports; subgroup powers, polynomial Horner values, ratio quotients, column RREF, rational determinant and actual locator determinants.',
           'actual_rank': prefix[-1], 'required_exclusion_rank': 21,
           'prefix_ranks': prefix, 'integer_minor_determinant': integer_det,
           'minor_determinant_mod_97': integer_det % P,
           'complete_rebuilt_matrix': matrix, 'checks': checks,
           'reconstruction_pivots': reconstruction_pivots,
           'positive_control_projective_gates': projective_gates,
           'positive_control_locator_evaluations': locator_evaluations,
           'failures': failures}
    OUT.write_text(json.dumps(out, indent=2) + '\n')
    print(f'Checks {len(checks)}; rank {prefix[-1]}/21; minor {integer_det % P}; '
          f'failures {len(failures)}; certificate {OUT}')
    if failures:
        print('Failed checks: ' + ', '.join(f['check'] for f in failures))
        raise SystemExit(1)


if __name__ == '__main__':
    run()
