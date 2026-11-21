#!/usr/bin/env python3
"""Fixed q=t^2+1/4, full U_6 range screen; exact rational certificates.

No parameter sampling, root-count algorithm or new input precision.
Run from riemann: python3 scripts/pollaczek/quadratic_differential_range_2030.py
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json

import tilted_bezoutian_n6_2014 as alg

base = alg.base
ROOT = Path(__file__).parent
OUTPUT = ROOT / 'quadratic-differential-range-2030.json'
PINNED = {
    'tilted-boundary-metric-2010.json': '361e31b72ad348b17f6c2ac785c20f5ab73e27796025bd724af208543e0feaf7',
    'tilted_boundary_metric_2010.py': '21cc4fb70b084fde19c62d74a7edb04a2bcdb38fe1a376ea5e7de6d3edbb58fc',
    'tilted_bezoutian_n6_2014.py': 'af87c4ec40ea6a93ddb0d9fe3915dd6c2fa403d4729e48639c1b94247ac42709',
}


def main():
    checks = {}
    cert = {
        'target': 'U_6=(t^2+1/4)h\u2032+2alpha*t*h; alpha>=0, real quintic h',
        'method': 'Exact coefficient elimination and Q(sqrt(2))[pi] rational enclosures',
        'normalization': 'U_6=T_6/S, S=sin(pi/8)/sqrt(2)>0; no odd terms discarded',
        'status': 'STARTED', 'checks': checks,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }

    def check(name, ok):
        checks[name] = bool(ok)

    def save(status):
        cert['status'] = status
        cert['failures'] = [k for k, v in checks.items() if not v]
        OUTPUT.write_text(json.dumps(cert, indent=2)+'\n')

    def guard(status):
        if not all(checks.values()):
            save(status)
            print('Result:', status, '; failures:', cert['failures'])
            print('Certificate:', OUTPUT.relative_to(ROOT.parent.parent))
            raise SystemExit(1)

    cert['input_sha256'] = {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                            for name in PINNED}
    for name, expected in PINNED.items():
        check('pinned_'+name, cert['input_sha256'][name] == expected)
    guard('INPUT_CHANGED')
    src = json.loads((ROOT/'tilted-boundary-metric-2010.json').read_text())
    pi_iv = tuple(F(src['pi_interval'][k]) for k in ('lower', 'upper'))
    sqrt_iv = tuple(F(src['sqrt2_interval'][k]) for k in ('lower', 'upper'))
    cert['pi_interval'], cert['sqrt2_interval'] = src['pi_interval'], src['sqrt2_interval']
    check('unchanged_input_widths', pi_iv[1]-pi_iv[0] == sqrt_iv[1]-sqrt_iv[0] == F(1, 10**60))
    check('sqrt2_squared_endpoints', 0 < sqrt_iv[0]**2 < 2 < sqrt_iv[1]**2)
    # The pi enclosure and its branch proof are the unchanged C029n input.
    bern = [F(1)]
    for m in range(1, 19):
        bern.append(-sum((comb(m+1, k)*bern[k] for k in range(m)), F(0))/(m+1))
    check('all_prior_Bernoulli', bern == list(map(F, src['bernoulli_0_through_18'])))
    phases = [(F(1), F(0)), (F(1), F(1)), (F(-1), F(0)), (F(-1), F(-1))]
    u = []
    for n in range(9):
        poly = [alg.Z]*(n+2)
        for h in range(n+1):
            c = -F(factorial(n)*4**h*(4**(h+1)-1)*2**(h+1),
                   factorial(n-h)*factorial(2*h+2))*bern[2*h+2]
            a, b = phases[(n-h) % 4]
            poly[h+1] = c*a, c*b
        u.append(alg.trim(poly))
    beta = [alg.add(alg.scale(u[n], 8*n*n+12*n+7),
                    alg.scale(u[n+2], (2*n+3)*(2*n+5)),
                    alg.scale(u[n-2], 4*n*(n-1)) if n >= 2 else []) for n in range(7)]
    weights = [F(factorial(6), factorial(6-k)*6**k) for k in range(7)]
    a = [alg.scale(beta[k], weights[k]) for k in range(7)]
    for name, actual, key in [('u', u, 'u_over_S_polynomials'),
                               ('beta', beta, 'beta_over_S_polynomials'),
                               ('a', a, 'a_over_S_polynomials')]:
        check('all_prior_'+name, actual == list(map(alg.decode, src[key])))
    check('all_prior_weights', weights == list(map(F, src['weights'])))
    p = [[F(1)]]
    for k in range(6):
        row = [F(0)]+p[k]
        if k:
            for j, c in enumerate(p[k-1]):
                row[j] -= F(2*k+1, 2)*c
        p.append([c/F(k+1) for c in row])
    check('basis_degrees_and_leads', all(len(p[k]) == k+1 and p[k][-1] == F(1, factorial(k))
                                        for k in range(7)))
    check('basis_parity', all(c == 0 for k, row in enumerate(p)
                              for j, c in enumerate(row) if (j-k) % 2))
    # Each b_i is an exact polynomial in pi; its coefficients are in Q(sqrt(2)).
    b = [alg.add(*(alg.scale(a[k], p[k][i]) for k in range(i, 7))) for i in range(7)]
    b_iv = [base.peval(c, pi_iv, sqrt_iv) for c in b]
    check('full_degree_six', b_iv[6][1] < 0)
    # Do not replace U by its even part: verify the full 7x6 operator matrix.
    # Entry [j][k] is the affine polynomial in alpha for t^j in L_alpha(t^k).
    matrix = [[[F(0), F(0)] for k in range(6)] for j in range(7)]
    for k in range(6):
        matrix[k+1][k] = [F(k), F(2)]
        if k:
            matrix[k-1][k] = [F(k, 4), F(0)]
    check('even_equations',
          [matrix[j][k] for j, k in [(0, 1), (2, 1), (2, 3), (4, 3), (4, 5), (6, 5)]]
          == [[F(1, 4), F(0)], [F(1), F(2)], [F(3, 4), F(0)],
              [F(3), F(2)], [F(5, 4), F(0)], [F(5), F(2)]])

    # F(alpha)=(b2-4(1+2alpha)b0)(3+2alpha)(5+2alpha)
    #          -(3/4)b4(5+2alpha)+(15/16)b6, necessary for range membership.
    factors = [F(15), F(16), F(4)]  # (3+2alpha)(5+2alpha)
    linear = [alg.add(b[2], alg.scale(b[0], -4)), alg.scale(b[0], -8)]
    f = [[] for j in range(4)]
    for i, c in enumerate(linear):
        for j, d in enumerate(factors):
            f[i+j] = alg.add(f[i+j], alg.scale(c, d))
    f[0] = alg.add(f[0], alg.scale(b[4], -F(15, 4)), alg.scale(b[6], F(15, 16)))
    f[1] = alg.add(f[1], alg.scale(b[4], -F(3, 2)))
    expanded = [alg.add(alg.scale(b[2], 15), alg.scale(b[0], -60),
                        alg.scale(b[4], -F(15, 4)), alg.scale(b[6], F(15, 16))),
                alg.add(alg.scale(b[2], 16), alg.scale(b[0], -184), alg.scale(b[4], -F(3, 2))),
                alg.add(alg.scale(b[2], 4), alg.scale(b[0], -144)),
                alg.scale(b[0], -32)]
    check('cubic_expansion_identity', f == expanded)
    f_iv = [base.peval(c, pi_iv, sqrt_iv) for c in f]
    f_outer = [base.outward_grid(iv, 9) for iv in f_iv]
    b_outer = [base.outward_grid(iv, 9) for iv in b_iv]
    cert.update({
        'bernoulli': list(map(base.rational, bern)),
        'u_over_S': list(map(alg.encode, u)), 'beta_over_S': list(map(alg.encode, beta)),
        'weights': list(map(base.rational, weights)), 'a_over_S': list(map(alg.encode, a)),
        'basis_p_0_to_6': [list(map(base.rational, row)) for row in p],
        'U_coefficients': list(map(alg.encode, b)),
        'U_coefficient_intervals': list(map(base.interval_json, b_iv)),
        'U_coefficient_outer_bounds': list(map(base.interval_json, b_outer)),
        'operator_matrix_affine_alpha': [[[base.rational(v) for v in entry]
                                          for entry in row] for row in matrix],
        'necessary_cubic_coefficients': list(map(alg.encode, f)),
        'necessary_cubic_intervals': list(map(base.interval_json, f_iv)),
        'necessary_cubic_outer_bounds': list(map(base.interval_json, f_outer)),
        'required': 'All four necessary-cubic coefficient upper bounds < 0 imply F(alpha)<0 for every alpha>=0',
        'domain': 'Every real alpha>=0, including zero and the unbounded tail; no sampling',
        'denominators': {'3+2alpha_lower_bound': '3/1', '5+2alpha_lower_bound': '5/1'},
        'unused_odd_equations': 'b1=2alpha*c0+c2/2; b3=(2+2alpha)c2+c4; b5=(4+2alpha)c4',
    })
    save('COEFFICIENTS_READY')
    guard('COEFFICIENT_FAILURE')
    for j in range(7):
        check('U_outer_contains_full_'+str(j), b_outer[j][0] <= b_iv[j][0] <= b_iv[j][1] <= b_outer[j][1])
    for j in range(4):
        check('F_outer_contains_full_'+str(j), f_outer[j][0] <= f_iv[j][0] <= f_iv[j][1] <= f_outer[j][1])
        check('F_strictly_negative_coefficient_'+str(j), f_outer[j][1] < 0)
    guard('SIGN_INCONCLUSIVE')
    save('EXCLUDED_ALL_ALPHA_NONNEGATIVE')
    print('Result: no compatible real quintic for any alpha>=0.')
    print('Necessary F coefficients, ascending in alpha; required each upper < 0:')
    for j, iv in enumerate(f_outer):
        print('  f_'+str(j)+': ['+base.rational(iv[0])+', '+base.rational(iv[1])+']')
    print('Checks:', len(checks), '; failures:', cert['failures'])
    print('Certificate:', OUTPUT.relative_to(ROOT.parent.parent))


if __name__ == '__main__':
    main()
