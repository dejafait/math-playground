"""Full positive-witness replay, independent of the C++ discovery equations.

All arithmetic is in the actual prime subfield, hence embeds in F_(97^20).
Save every relevant eight-moment vector, quotient and gate. No census claim.
"""
from itertools import combinations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
MOD = 97


def product(values):
    result = 1
    for x in values:
        result = result*x % MOD
    return result


def moment(error):
    return [sum(e*pow(int(x), j, MOD) for x, e in error.items()) % MOD
            for j in range(1, 9)]


def solve(matrix, rhs):
    n = len(rhs)
    rows = [list(row)+[v] for row, v in zip(matrix, rhs)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if rows[i][j] % MOD)
        rows[j], rows[pivot] = rows[pivot], rows[j]
        t = pow(rows[j][j] % MOD, -1, MOD)
        rows[j] = [v*t % MOD for v in rows[j]]
        for i in range(n):
            if i != j:
                t = rows[i][j]
                rows[i] = [(v-t*w) % MOD for v, w in zip(rows[i], rows[j])]
    return [row[-1] for row in rows]


def recover(support, syndrome):
    values = solve([[pow(x, j, MOD) for x in support] for j in range(1, 5)],
                   syndrome[:4])
    error = dict(zip(support, values))
    return error, [(v-w) % MOD for v, w in zip(moment(error), syndrome)]


def polynomial(roots):
    coeff = [1]
    for x in roots:
        out = [0]*(len(coeff)+1)
        for j, c in enumerate(coeff):
            out[j] = (out[j]-x*c) % MOD
            out[j+1] = (out[j+1]+c) % MOD
        coeff = out
    return coeff


def recurrence(support, syndrome):
    coeff = polynomial(support)
    return [sum(c*syndrome[i+j] for j, c in enumerate(coeff)) % MOD
            for i in range(4)]


def main():
    d = json.loads((ROOT/'shared-label-pair-candidate.json').read_text())
    H = [x for x in range(1, MOD) if pow(x, 16, MOD) == 1]
    a, b, c = [d[x] for x in ('a', 'b', 'c')]
    Y, Z, W = [d[x] for x in ('Y', 'Z', 'W')]
    U = [a, b, c]+Y+Z+W
    assert len(set(U)) == 9 and set(U) <= set(H)
    outside = sorted(set(H)-set(U))
    cx = {x: product(x-h for h in outside) for x in U}
    assert all(cx.values())
    supports = [[a, b]+Y, [a, c]+Z, [b, c]+W, d['K'], d['L']]
    assert len({tuple(sorted(s)) for s in supports}) == 5
    assert all(len(set(s)) == 4 and set(s) <= set(H) for s in supports)
    intersections = [{'pair': [i, j], 'labels': sorted(set(supports[i]) & set(supports[j]))}
                     for i, j in combinations(range(5), 2)]
    assert len(intersections) == 10 and all(len(row['labels']) <= 1 for row in intersections)
    assert set(d['K']) & set(d['L']) == {a}

    # Compute L057's quotient independently by eliminating the two missing
    # recurrence columns using their first two rows, rather than G_J rows.
    projections = []
    for support, mu in zip(supports[3:], d['mu']):
        missing = [x for x in (a, b, c) if x not in support]
        assert missing == [b, c]
        columns = [recurrence(support, moment({x: 1})) for x in missing]
        raw = [recurrence(support, moment({x: cx[x] for x in pair})) for pair in (Y, Z)]
        eliminated, quotients = [], []
        for v in raw:
            coeff = solve([[col[j] for col in columns] for j in range(2)], v[:2])
            residual = [(v[j]-sum(t*col[j] for t, col in zip(coeff, columns))) % MOD
                        for j in range(4)]
            assert residual[:2] == [0, 0]
            eliminated.append(coeff)
            quotients.append(residual[2:])
        assert all(any(v) for v in quotients)
        assert all((z-mu*y) % MOD == 0 for y, z in zip(*quotients))
        assert mu not in (0, 96)
        projections.append({'support': support, 'missing': missing, 'columns': columns,
                            'raw_YZ': raw, 'eliminated_YZ': eliminated,
                            'quotient_YZ': quotients, 'mu': mu})
    assert d['mu'][0] != d['mu'][1]

    # Find an explicit p and original finite chart. No assumption that
    # arbitrary charts descend is involved in this existence assertion.
    q, r = d['q'], d['r']
    assert q not in (0, 1) and r not in (0, 1)
    witness = None
    trials = 0
    for p in range(2, 97):
        for rho in range(2, 97):
            trials += 1
            gammas, alphas = [0, 1, rho], [(1-rho) % MOD, rho, 96]
            E = [(rho-(1-rho)*mu) % MOD for mu in d['mu']]
            if not all(E):
                continue
            times = [rho*pow(e, -1, MOD) % MOD for e in E]
            assert len(set(gammas+times)) == 5
            normalized = [{a: p, b: q, **{x: 1 for x in Y}},
                          {a: (1-p) % MOD, c: r, **{x: 1 for x in Z}},
                          {b: (1-q) % MOD, c: (1-r) % MOD, **{x: 1 for x in W}}]
            base = [{x: cx[x]*v*pow(alpha, -1, MOD) % MOD for x, v in norm.items()}
                    for norm, alpha in zip(normalized, alphas)]
            bm = [moment(e) for e in base]
            assert all(all(e.values()) for e in base)
            slope = [(s1-s0) % MOD for s0, s1 in zip(bm[0], bm[1])]
            assert bm[2] == [(s0+rho*v) % MOD for s0, v in zip(bm[0], slope)]
            rows = []
            for support, T, mu, ee in zip(supports[3:], times, d['mu'], E):
                expected = [(s0+T*v) % MOD for s0, v in zip(bm[0], slope)]
                error, residual = recover(support, expected)
                if any(residual) or not all(error.values()):
                    break
                numerator = {x: -mu*cx[x] % MOD for x in Y}
                numerator.update({x: cx[x] for x in Z})
                numerator.update({a: cx[a]*(1-(1+mu)*p) % MOD,
                                  b: -mu*cx[b]*q % MOD, c: cx[c]*r % MOD})
                num_moments = moment(numerator)
                assert num_moments == [ee*v % MOD for v in expected]
                rows.append({'support': support, 'mu': mu, 'E': ee, 'T': T,
                             'actual_error': error, 'omega': {x: ee*v % MOD for x, v in error.items()},
                             'actual_moments8': moment(error), 'expected_moments8': expected,
                             'residual8': residual, 'numerator': numerator, 'numerator_moments8': num_moments})
            if len(rows) == 2:
                input_failure = []
                for support in supports:
                    _, residual = recover(support, slope)
                    assert any(residual)
                    input_failure.append({'support': support, 'slope_span_residual8': residual})
                witness = {'pqr': [p, q, r], 'gamma': gammas, 'alpha': alphas,
                           'lambda': 1, 'g': 1, 'rho': rho, 'base_errors': base,
                           'base_moments8': bm, 'syndrome_slope8': slope,
                           'recoveries': rows, 'same_support_input_failures': input_failure}
                break
        if witness is not None:
            break
    assert witness is not None, 'No full witness: candidate is not a proved result'
    report = {'scope': 'One full positive prime-subfield witness embedded in F_(97^20); no count bound',
              'H': H, 'a': a, 'b': b, 'c': c, 'Y': Y, 'Z': Z, 'W': W,
              'Q_roots': outside, 'c_x': cx, 'supports': supports,
              'intersections': intersections, 'isolated_projection_checks': projections,
              'chart_trials': trials, 'witness': witness,
              'checks': {'full_errors_actual': 5, 'full_errors_required': 5,
                         'moment_equations_actual': 40, 'moment_equations_required': 40,
                         'linear_intersections_actual': 10, 'linear_intersections_required': 10,
                         'isolated_additional_actual': 2, 'isolated_additional_required': 2,
                         'distinct_finite_parameters_actual': 5, 'distinct_finite_parameters_required': 5,
                         'same_support_failure_checks_actual': 5, 'same_support_failure_checks_required': 5,
                         'failures': 0}}
    path = ROOT/'shared-label-pair-verification.json'
    path.write_text(json.dumps(report, indent=2)+'\n')
    print('Full errors 5/5; moment equations 40/40; isolated additional 2/2; intersections 10/10.')
    print('Distinct finite parameters 5/5; same-support failures 5/5; verification failures 0/0.')
    print(f'Certificate: {path.relative_to(ROOT.parent.parent)}')


if __name__ == '__main__':
    main()
