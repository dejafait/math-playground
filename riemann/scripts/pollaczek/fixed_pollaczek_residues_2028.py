#!/usr/bin/env python3
"""Approved fixed p_5 residue screen; exact arithmetic, fixed input precision."""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json

import tilted_bezoutian_n6_2014 as alg

base = alg.base
ROOT = Path(__file__).parent
OUTPUT = ROOT / 'fixed-pollaczek-residues-2028.json'
PINNED = {
    'tilted-boundary-metric-2010.json': '361e31b72ad348b17f6c2ac785c20f5ab73e27796025bd724af208543e0feaf7',
    'tilted-bezoutian-n6-2014.json': '6870f303d2fa8bd6ec5bd9fcde2a197d6c9987f98b6bccf048a378f3ccdedd47',
    'tilted_boundary_metric_2010.py': '21cc4fb70b084fde19c62d74a7edb04a2bcdb38fe1a376ea5e7de6d3edbb58fc',
    'tilted_bezoutian_n6_2014.py': 'af87c4ec40ea6a93ddb0d9fe3915dd6c2fa403d4729e48639c1b94247ac42709',
}


def reciprocal(a):
    if not (a[1] < 0 or a[0] > 0):
        raise ArithmeticError('Denominator not separated from zero')
    return 1/a[1], 1/a[0]


def horner(coefficients, x):
    out = (F(0), F(0))
    for c in reversed(coefficients):
        out = base.iadd(base.imul(out, x), c)
    return out


def exact_eval(p, x):
    out = F(0)
    for c in reversed(p):
        out = out*x+c
    return out


def sign(x):
    return (x > 0)-(x < 0)


def interval_sign(a):
    return 'positive' if a[0] > 0 else 'negative' if a[1] < 0 else 'unresolved'


def main():
    checks = {}
    cert = {'target': 'Monic Q=U_6/l_6, P=120p_5; at most one positive simple-pole residue',
            'status': 'STARTED', 'checks': checks,
            'development_note': 'Initial run stopped before root work with TypeError: Q intervals used exact polynomials rather than evaluated coefficient intervals; corrected to b_iv. No mathematical bound failed.',
            'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

    def check(name, ok):
        checks[name] = bool(ok)

    def save(status):
        cert['status'] = status
        cert['failures'] = [k for k, v in checks.items() if not v]
        OUTPUT.write_text(json.dumps(cert, indent=2)+'\n')

    def guard(stage):
        if not all(checks.values()):
            save(stage)
            print('Result:', stage, '; failures:', cert['failures'])
            print('Certificate:', OUTPUT.relative_to(ROOT.parent.parent))
            raise SystemExit(1)

    cert['input_sha256'] = {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                            for name in PINNED}
    for name, expected in PINNED.items():
        check('pinned_'+name, cert['input_sha256'][name] == expected)
    guard('INPUT_CHANGED')
    src = json.loads((ROOT/'tilted-boundary-metric-2010.json').read_text())
    prior = json.loads((ROOT/'tilted-bezoutian-n6-2014.json').read_text())
    pi_iv = tuple(F(src['pi_interval'][k]) for k in ('lower', 'upper'))
    sqrt_iv = tuple(F(src['sqrt2_interval'][k]) for k in ('lower', 'upper'))
    cert['pi_interval'], cert['sqrt2_interval'] = src['pi_interval'], src['sqrt2_interval']
    check('unchanged_widths', pi_iv[1]-pi_iv[0] == sqrt_iv[1]-sqrt_iv[0] == F(1, 10**60))
    check('sqrt2_squared_endpoints', 0 < sqrt_iv[0]**2 < 2 < sqrt_iv[1]**2)

    # Reconstruct precisely the finite C029n inputs, including every odd term.
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
    check('all_prior_basis', p == [list(map(F, row)) for row in prior['basis_p_0_to_6']])
    check('basis_degrees_and_leads', all(len(p[k]) == k+1 and p[k][-1] == F(1, factorial(k))
                                        for k in range(7)))
    b = [alg.add(*(alg.scale(a[k], p[k][i]) for k in range(i, 7))) for i in range(7)]
    check('all_prior_U_coefficients', b == list(map(alg.decode, prior['U_monomial_coefficients'])))
    b_iv = [base.peval(c, pi_iv, sqrt_iv) for c in b]
    lead = b_iv[6]
    check('degree_six_negative_lead', lead[1] < 0)
    guard('COEFFICIENT_FAILURE')
    q_iv = [base.imul(c, reciprocal(lead)) for c in b_iv[:6]]+[(F(1), F(1))]
    P = [120*c for c in p[5]]
    dp = [(i+1)*P[i+1] for i in range(5)]
    check('P_monic_degree_five', len(P) == 6 and P[-1] == 1)
    check('P_explicit', P == [F(0), F(531, 4), F(0), F(-35), F(0), F(1)])
    cert.update({'bernoulli': list(map(base.rational, bern)),
                 'u_over_S': list(map(alg.encode, u)), 'beta_over_S': list(map(alg.encode, beta)),
                 'weights': list(map(base.rational, weights)), 'a_over_S': list(map(alg.encode, a)),
                 'basis_p_0_to_6': [list(map(base.rational, row)) for row in p],
                 'U_coefficients': list(map(alg.encode, b)),
                 'U_coefficient_intervals': list(map(base.interval_json, b_iv)),
                 'leading_coefficient_interval': base.interval_json(lead),
                 'Q_coefficient_intervals': list(map(base.interval_json, q_iv)),
                 'Q_exact_representation': 'Q_i=U_i/U_6 for i<6; Q_6=1',
                 'P': list(map(base.rational, P)), 'P_derivative': list(map(base.rational, dp))})
    save('COEFFICIENTS_READY')
    guard('REFERENCE_FAILURE')

    grid = [(F(j, 16), exact_eval(P, F(j, 16))) for j in range(-256, 257)]
    cert['grid'] = [{'x': base.rational(x), 'P': base.rational(v)} for x, v in grid]
    initial = [(x, x) for x, v in grid if v == 0]
    initial += [(x, y) for (x, v), (y, w) in zip(grid, grid[1:]) if v*w < 0]
    initial.sort()
    check('five_disjoint_grid_roots', len(initial) == 5 and
          all(initial[i][1] < initial[i+1][0] for i in range(4)))
    guard('GRID_INCOMPLETE')
    records = []
    for j, (lo, hi) in enumerate(initial):
        steps = []
        start = (lo, hi)
        for iteration in range(30):
            if lo == hi:
                break
            mid = (lo+hi)/2
            fm = exact_eval(P, mid)
            steps.append({'iteration': iteration+1, 'midpoint': base.rational(mid), 'P_midpoint': base.rational(fm)})
            if fm == 0:
                lo = hi = mid
            elif exact_eval(P, lo)*fm < 0:
                hi = mid
            else:
                lo = mid
        fl, fh = exact_eval(P, lo), exact_eval(P, hi)
        check(f'root_{j}_endpoint_evidence', fl == fh == 0 if lo == hi else fl*fh < 0)
        check(f'root_{j}_refinement_limit', len(steps) <= 30 and start[0] <= lo <= hi <= start[1])
        x_iv = lo, hi
        derivative = horner([(c, c) for c in dp], x_iv)
        check(f'root_{j}_simple_derivative', interval_sign(derivative) != 'unresolved')
        q_value = horner(q_iv, x_iv)
        u_value = horner(b_iv, x_iv)
        q_alt = base.imul(u_value, reciprocal(lead))
        check(f'root_{j}_Q_enclosures_overlap', max(q_value[0], q_alt[0]) <= min(q_value[1], q_alt[1]))
        record = {'j': j, 'initial_bracket': base.interval_json(start),
                  'refinements': steps, 'bracket': base.interval_json(x_iv),
                  'P_at_lower': base.rational(fl), 'P_at_upper': base.rational(fh),
                  'P_derivative_interval': base.interval_json(derivative),
                  'Q_interval': base.interval_json(q_value),
                  'Q_via_U_interval': base.interval_json(q_alt)}
        if interval_sign(derivative) == 'unresolved':
            record.update({'residue_interval': None, 'sign': 'unresolved'})
        else:
            residue = base.imul(q_value, reciprocal(derivative))
            outer = base.outward_grid(residue, 3)
            check(f'root_{j}_outer_contains_full', outer[0] <= residue[0] <= residue[1] <= outer[1])
            record.update({'residue_interval': base.interval_json(residue),
                           'residue_outer_bound': base.interval_json(outer),
                           'sign': interval_sign(residue)})
        records.append(record)
        cert['roots'] = records
        save('RESIDUES_IN_PROGRESS')
    check('five_final_disjoint_brackets', all(F(records[j]['bracket']['upper']) <
          F(records[j+1]['bracket']['lower']) for j in range(4)))
    counts = {s: sum(r['sign'] == s for r in records) for s in ('positive', 'negative', 'unresolved')}
    cert['counts'] = counts
    cert['required'] = {'poles': 5, 'resolved_signs_for_pass': 5, 'max_positive_for_pass': 1,
                        'positive_for_rejection': 2, 'max_bisections_per_bracket': 30}
    guard('CERTIFICATE_FAILURE')
    result = ('BASELINE_REJECTED' if counts['positive'] >= 2 else
              'FINITE_SCREEN_PASSED' if counts['unresolved'] == 0 else 'INCONCLUSIVE')
    save(result)
    print('Result:', result)
    print('Poles:', len(records), '/ required 5; resolved:', 5-counts['unresolved'], '/ required 5')
    print('Positive residues:', counts['positive'], '/ required <=1; negative:', counts['negative'])
    print('Failures:', cert['failures'])
    print('Certificate:', OUTPUT.relative_to(ROOT.parent.parent))


if __name__ == '__main__':
    main()
