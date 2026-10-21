"""Verify the selected survivor directly, then classify all 1820 supports.

No imports from the producer, no cubic-ratio or recurrence solver. Uses
Vandermonde elimination on moments 1..4 and all four remaining moments.
"""
from itertools import combinations
from pathlib import Path
import json

ROOT = Path(__file__).parent
P = 97
H = tuple(x for x in range(1, P) if pow(x, 16, P) == 1)


def moment(word):
    return [sum(w*pow(int(x), j, P) for x, w in word.items()) % P for j in range(1, 9)]


def solve(k, rhs):
    a = [[pow(x, j, P) for x in k]+[rhs[j-1]] for j in range(1, 5)]
    for j in range(4):
        pivot = next(i for i in range(j, 4) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        a[j] = [x*pow(a[j][j], -1, P) % P for x in a[j]]
        for i in range(4):
            if i != j:
                factor = a[i][j]
                a[i] = [(x-factor*y) % P for x, y in zip(a[i], a[j])]
    return [a[i][-1] for i in range(4)]


def main():
    witness = json.loads((ROOT/'intersecting-singleton-result.json').read_text())['witness']
    assert witness is not None
    h, d = witness['h'], witness['d']
    y1, y2 = witness['Y']
    z1, z2 = witness['Z']
    w = witness['W']
    p, q, r = witness['p_q_r']
    rho = witness['gamma'][2]
    assert witness['gamma'] == [0, 1, rho] and rho not in (0, 1)
    assert witness['lambda_value'] == 1
    labels = [h, d, y1, y2, z1, z2, *w]
    assert len(set(labels)) == 9 and set(labels) <= set(H)
    assert p*q*(1-p-q)*r*(1-r) % P
    c = {}
    for x in labels:
        c[x] = 1
        for a in H:
            if a not in labels:
                c[x] = c[x]*(x-a) % P
    assert c == {int(x): a for x, a in witness['c'].items()}
    errors = [{int(x): a for x, a in e.items()} for e in witness['original_errors']]
    supports = [{h, d, y1, y2}, {h, d, z1, z2}, {h, *w}]
    alpha = [(1-rho) % P, rho, P-1]
    weights = [{h: p, d: r, y1: 1, y2: 1},
               {h: q, d: (1-r) % P, z1: 1, z2: 1},
               {h: (1-p-q) % P, **{x: 1 for x in w}}]
    for i, e in enumerate(errors):
        assert set(e) == supports[i] and all(e.values())
        assert all((alpha[i]*e[x]-c[x]*weights[i][x]) % P == 0 for x in e)
    intercept = moment(errors[0])
    slope = [(b-a) % P for a, b in zip(intercept, moment(errors[1]))]
    assert intercept == witness['syndrome_intercept'] and slope == witness['syndrome_slope']
    pencil = lambda t: [(a+t*b) % P for a, b in zip(intercept, slope)]
    assert moment(errors[2]) == pencil(rho)
    selected = []
    for row in witness['records']:
        k, mu, u, t, evalue = row['K'], row['mu'], row['u'], row['T'], row['E']
        assert set(k) == {y1, *row['S']}
        assert mu not in (0, 96) and evalue == (rho-(1-rho)*mu) % P and evalue
        assert t*evalue % P == rho and t not in (0, 1, rho)
        nword = {y1: -mu*c[y1] % P, y2: -mu*c[y2] % P,
                 z1: c[z1], z2: c[z2], h: c[h]*(q-mu*p) % P,
                 d: c[d]*(1-(1+mu)*r) % P}
        n = moment(nword)
        omega = solve(k, n)
        assert moment(dict(zip(k, omega))) == n == row['N_moments']
        assert omega == row['omega'] and all(omega)
        error = {x: a*pow(evalue, -1, P) % P for x, a in zip(k, omega)}
        assert error == {int(x): a for x, a in row['error'].items()}
        assert moment(error) == pencil(t) == row['error_moments']
        # All five cubic equations, directly cross multiplied.
        def value(roots, x):
            a, b, c = roots
            return (x-a)*(x-b)*(x-c) % P
        ax = {y2: -mu % P, z1: 1, z2: 1, h: (q-mu*p) % P,
              d: (1-(1+mu)*r) % P}
        assert all((ax[x]*value(row['S'], x)-u*value(w, x)) % P == 0 for x in ax)
        selected.append(dict(K=k, mu=mu, T=t, omega=omega, error=error,
                             moments=moment(error), all_eight_moments=True))
    assert len({a['T'] for a in selected}) == 3
    ss = [set(row['S']) for row in witness['records']]
    assert len(set.union(*ss)) == 8
    assert sorted(len(a & b) for a, b in combinations(ss, 2)) == [0, 0, 1]
    # Complete affine-pencil/support intersection, including rejected supports.
    records, admitted = [], []
    for k in combinations(H, 4):
        a, b = solve(k, intercept), solve(k, slope)
        ma, mb = moment(dict(zip(k, a))), moment(dict(zip(k, b)))
        ra = [(ma[j]-intercept[j]) % P for j in range(4, 8)]
        rb = [(mb[j]-slope[j]) % P for j in range(4, 8)]
        row = dict(K=k, intercept_weights=a, slope_weights=b, residual_intercept=ra,
                   residual_slope=rb)
        assert any(rb), 'persistent four-support pencil: contradicts local gates'
        j = next(j for j, v in enumerate(rb) if v)
        t = -ra[j]*pow(rb[j], -1, P) % P
        row['tested_T'] = t
        if any((x+t*y) % P for x, y in zip(ra, rb)):
            row['status'] = 'inconsistent'
        else:
            omega = [(x+t*y) % P for x, y in zip(a, b)]
            assert moment(dict(zip(k, omega))) == pencil(t)
            row.update(status='admitted', omega=omega, full_weight=all(omega))
            admitted.append(dict(K=k, T=t, error=omega, full_weight=all(omega)))
        records.append(row)
    assert len(records) == 1820
    extra = [a for a in admitted if a['T'] not in (0, 1, rho)]
    assert all(a['full_weight'] for a in admitted)
    assert len({a['T'] for a in admitted}) == len(admitted)
    for a in selected:
        assert any(a['T'] == row['T'] and a['K'] == list(row['K']) for row in extra)
    result = dict(scope='selected prime-field witness embedded in F_(97^20); complete all-support affine intersection',
                  selected=selected, complete_support_records=records, admitted=admitted,
                  summary=dict(selected_distinct_parameters=3, refutation_threshold_for_triple_exclusion=3,
                               support_checks=1820, required_support_checks=1820,
                               total_finite_bad_parameters=len(admitted), additional_parameters=len(extra),
                               threshold_for_eleven_refutation=12, all_full_weight=True,
                               exhaustive_for_selected_pencil=True, all_labelings=False, failures=[]))
    out = ROOT/'intersecting-singleton-verification.json'
    out.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print(f'selected distinct gated full-weight candidates 3/3; all-support checks 1820/1820; failures 0')
    print(f'total finite bad parameters {len(admitted)}; additional {len(extra)}; eleven-refutation threshold 12; certificate {out}')


if __name__ == '__main__':
    main()
