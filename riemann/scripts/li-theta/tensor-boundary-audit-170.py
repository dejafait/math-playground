#!/usr/bin/env python3
"""Independent finite algebra audit of L967; no numerical theta integrals.

Reconstruct from a truncated formal logarithm, polynomial division at -b,
and one-coordinate slices. Do not import the construction script or use
its tables as expected answers. Compare every saved face and full ray.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import json


def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}


def scale(p, c):
    return {k: v*c for k, v in p.items() if v*c}


def mul(p, q):
    out = {}
    for a, c in p.items():
        for b, d in q.items():
            k = tuple(x+y for x, y in zip(a, b))
            out[k] = out.get(k, F(0)) + c*d
    return {k: v for k, v in out.items() if v}


def power(p, n, size):
    out = {(0,)*size: F(1)}
    for _ in range(n):
        out = mul(out, p)
    return out


def dump(p):
    return [{"exponents": [str(x) for x in k], "coefficient": str(v)}
            for k, v in sorted(p.items())]


def parse(rows):
    out = {}
    for row in rows:
        key = tuple(F(x) for x in row['exponents'])
        if key in out:
            raise ValueError('Duplicate monomial in saved certificate')
        out[key] = F(row['coefficient'])
    return out


def coefficients(n):
    h, delta, b = F(64*9**n), F(64*9**n)-F(1, 4), F(1, 4)
    p = (n-1)//2
    # Direct B(t), then translate t=-b+y and divide by delta+y.
    B = [F(0)]*n
    for i in range(p+1):
        for j in range(p+1):
            B[n-1-i-j] += F((-1)**(i+j)*comb(n, 2*i+1)*comb(n, 2*j+1), 4**(i+j))
    shifted = [sum((B[k]*comb(k, j)*(-b)**(k-j)
                    for k in range(j, n)), F(0)) for j in range(n)]
    quotient = []
    for v in shifted:
        quotient.append((v-(quotient[-1] if quotient else 0))/delta)
    d = [F(0)] + [(-1)**(k-1)*h*quotient[n-k] for k in range(1, n+1)]
    return h, delta, d


def b_numerator(n, d):
    # log(1+Y)=sum (-1)^(ell-1) Y^ell/ell, Y=sum z_r*t^r/r!.
    # Keys contain t degree followed by exponents of z_1,...,z_n.
    Y = {}
    for r in range(1, n+1):
        k = [r]+[0]*n
        k[r] = 1
        Y[tuple(k)] = F(1, factorial(r))
    log = {}
    for ell in range(1, n+1):
        log = add(log, scale(power(Y, ell, n+1), F((-1)**(ell-1), ell)))
    out = {}
    for (k, *exps), c in log.items():
        if 1 <= k <= n:
            e = (n-sum(exps), *exps)
            out[e] = out.get(e, F(0)) + k*d[k]*c
    return {e: c for e, c in out.items() if c}


def moment(i=None, c=F(1)):
    key = [0]*5
    if i is not None:
        key[i] = 1
    return {tuple(key): F(c)} if c else {}


def substitute(poly, values, size):
    out = {}
    for exps, c in poly.items():
        term = {(0,)*size: c}
        for e, value in zip(exps, values):
            term = mul(term, power(value, e, size))
        out = add(out, term)
    return out


def H(q, r):
    # Symbolic (1/(2q) d/dq)^r cosh(q*t), no supplied closed forms.
    # Temporary keys: sign in exp(sign*q*t), t degree, Laurent q degree.
    p = {(1, 0, 0): F(1, 2), (-1, 0, 0): F(1, 2)}
    for _ in range(r):
        nxt = {}
        for (s, td, qd), c in p.items():
            nxt = add(nxt, {(s, td, qd-2): c*F(qd, 2)},
                      {(s, td+1, qd-1): c*F(s, 2)})
        p = nxt
    out = {}
    for (s, td, qd), c in p.items():
        out = add(out, {(s*q, td, 0): c*q**qd})
    return out


def dt(p):
    out = {}
    for (rate, td, kp), c in p.items():
        out = add(out, {(rate, td, kp): c*rate})
        if td:
            out = add(out, {(rate, td-1, kp): c*td})
    return out


def origin(p):
    out = {}
    for (_, td, kp), c in p.items():
        if td == 0:
            out = add(out, {(F(0), 0, kp): c})
    return out


def slice_at_one(poly, values, n):
    # For a homogeneous symmetric n-factor tensor, choose the factor
    # occupying t; the other n-1 factors are at zero.
    out = {}
    zeros = [origin(v) for v in values]
    for exps, c in poly.items():
        for r, e in enumerate(exps):
            if not e:
                continue
            term = scale(values[r], c*F(e, n))
            for s, count in enumerate(exps):
                term = mul(term, power(zeros[s], count-int(s == r), 3))
            out = add(out, term)
    return out


def audit(saved):
    n = saved['n']
    h, delta, d = coefficients(n)
    q = F(8*3**n)
    checks, failures = [], []

    def check(label, actual, expected):
        residual = add(actual, scale(expected, -1))
        checks.append({'check': label, 'residual': dump(residual)})
        if residual:
            failures.append(label)

    for k in range(1, n+1):
        check(f'd_{k}', {(): d[k]}, {(): F(saved['d'][k-1])})
    P = b_numerator(n, d)
    raw = {}
    for term in saved['raw_tensor']:
        exps = [0]*(n+1)
        h_order = None
        for tag, order in term['factors']:
            if tag == 'b':
                exps[order] += 1
            else:
                if h_order is not None:
                    raise ValueError('Multiple h factors')
                h_order = order
        key = (*exps, h_order)
        raw = add(raw, {key: F(term['coefficient'])})
    expected_raw = {(*e, 0): c for e, c in P.items()}
    expected_raw[(n,)+(0,)*n+(1,)] = -d[1]
    check('complete_original_tensor', raw, expected_raw)

    transferred = [moment(c=F(1, 2))]+[moment(r-1, 2*r) for r in range(1, n+1)]
    live_h0 = add(moment(c=F(1, 2)), moment(3, 2*delta))
    live_h1 = add(moment(3, 2), moment(4, 2*delta))
    whole = add(mul(substitute(P, transferred, 5), live_h0),
                scale(live_h1, -d[1]/2**n))
    strata = {j: {e: c for e, c in whole.items() if sum(e) == j} for j in range(n+2)}
    actual_faces = {tuple(f['live_coordinates']): parse(f['integrated_polynomial'])
                    for f in saved['all_faces']}
    expected_keys = {S for j in range(n+2) for S in combinations(range(1, n+2), j)}
    if len(saved['all_faces']) != 2**(n+1) or set(actual_faces) != expected_keys:
        failures.append('nonexhaustive or repeated saved faces')
    for S in sorted(expected_keys):
        check(f'face_{S}', actual_faces.get(S, {}), scale(strata[len(S)], F(1, comb(n+1, len(S)))))
    if [s['dimension'] for s in saved['stratum_checks']] != list(range(n+2)):
        failures.append('nonexhaustive stratum table')
    for row in saved['stratum_checks']:
        check(f"stratum_{row['dimension']}", parse(row['summed_face_polynomial']), strata[row['dimension']])
        if row['residual']:
            failures.append('saved nonzero stratum residual')

    KAPPA = {(F(0), 0, 1): F(1)}
    B = [mul(KAPPA, H(F(1, 2), 0))]+[scale(H(F(1, 2), r-1), 2*r) for r in range(1, n+1)]
    C0 = add(B[0], scale(H(q, 0), 2*delta))
    C1 = add(scale(H(q, 0), 2), scale(H(q, 1), 2*delta))
    Wzero = substitute(P, [origin(v) for v in B], 3)
    Wslice = slice_at_one(P, B, n)
    ray = scale(add(mul(C0, Wzero), scale(mul(C1, power(KAPPA, n, 3)), -d[1]),
                    scale(mul(origin(C0), Wslice), n),
                    scale(mul(mul(origin(C1), B[0]), power(KAPPA, n-1, 3)), -n*d[1])), F(1, n+1))
    check('entire_symmetrized_ray', parse(saved['ray_check']['full_ray_exponential_polynomial']), ray)
    leading = {e: c for e, c in ray.items() if e[0] >= q and e[1] >= 1}
    required = {(q, 1, n): -d[1]*delta/(2*q*(n+1))}
    check('leading_ray_term', leading, required)
    if any(e[0] > q or (e[0] == q and e[1] > 1) for e in ray):
        failures.append('undetected faster ray term')
    if not all(dk > 0 for dk in d[1:]) or not next(iter(required.values())) < 0:
        failures.append('strict sign test failed')

    for rate, max_r in [(F(1, 2), n), (q, 1)]:
        for r in range(max_r+1):
            f = H(rate, r)
            actual = add(scale(dt(dt(f)), 2), scale(f, -F(1, 2)))
            expected = scale(f, 2*(rate**2-F(1, 4)))
            if r:
                expected = add(expected, scale(H(rate, r-1), 2*r))
            check(f'operator_q{rate}_r{r}', actual, expected)
            check(f'origin_q{rate}_r{r}', origin(f), {(F(0), 0, 0): F(int(r == 0))})
            check(f'normal_q{rate}_r{r}', origin(dt(f)), {})
    return {'n': n, 'h': str(h), 'delta': str(delta), 'q': str(q),
            'reconstructed_b_numerator': dump(P),
            'checks': checks, 'faces_checked': len(actual_faces),
            'reconstructed_strata': {str(j): dump(p) for j, p in strata.items()},
            'full_ray': dump(ray), 'leading_term': dump(required),
            'failures': failures}


def main():
    source = Path(__file__).with_name('tensor-boundary-check-168.json')
    saved = json.loads(source.read_text())
    if [c['n'] for c in saved['cases']] != [2, 3]:
        raise ValueError('Unexpected source cases')
    cases = [audit(c) for c in saved['cases']]
    failures = [f"n={c['n']}: {f}" for c in cases for f in c['failures']]
    summary = {'cases': [2, 3], 'faces_checked': sum(c['faces_checked'] for c in cases),
               'exact_checks': sum(len(c['checks']) for c in cases),
               'actual_max_absolute_residual': str(max((abs(F(v['coefficient'])) for c in cases
                    for check in c['checks'] for v in check['residual']), default=F(0))),
               'required_max_absolute_residual': '0',
               'actual_ray_limit_coefficients_without_kappa_power':
                    [c['leading_term'][0]['coefficient'] for c in cases],
               'required_for_pointwise_payment': 'nonnegative kernel everywhere',
               'actual': 'negative ray limit at n=2,3 for every kappa>0',
               'failures': failures,
               'scope': 'Finite algebra audit; analytic endpoint, mass and limit justification is in L967. No integrated sign.'}
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps({'summary': summary, 'cases': cases}, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Full certificate: {output.relative_to(Path.cwd())}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
