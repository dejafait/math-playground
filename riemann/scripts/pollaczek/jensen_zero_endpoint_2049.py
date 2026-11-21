#!/usr/bin/env python3
"""One fixed theta=0 Newton/Hermite interval test; standard library only.

Run from riemann: python3 scripts/pollaczek/jensen_zero_endpoint_2049.py
No Jensen damping, new constant enclosure, precision fallback or root API.
"""
from fractions import Fraction as F
from itertools import permutations
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import sys

import tilted_boundary_metric_2010 as base

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
ROOT = Path(__file__).parent
PINNED = {
    'tilted-boundary-metric-2010.json':
        '361e31b72ad348b17f6c2ac785c20f5ab73e27796025bd724af208543e0feaf7',
    'tilted_boundary_metric_2010.py':
        '21cc4fb70b084fde19c62d74a7edb04a2bcdb38fe1a376ea5e7de6d3edbb58fc',
}
ZERO = (F(0), F(0))
ONE = (F(1), F(1))


def decode(p):
    return [(F(c['rational']), F(c['sqrt2'])) for c in p]


def idiv(x, y):
    if y[0] <= 0 <= y[1]:
        raise ValueError('Division interval contains zero')
    # Reciprocal reverses endpoint order on either component of R\{0}.
    return base.imul(x, (1/y[1], 1/y[0]))


def isum(xs):
    total = ZERO
    for x in xs:
        total = base.iadd(total, x)
    return total


def sign(iv):
    return 1 if iv[0] > 0 else -1 if iv[1] < 0 else 0


def short(iv):
    """Exact outward scientific bounds, never used in the calculation."""
    magnitude = max(abs(iv[0]), abs(iv[1]))
    exponent = 0
    if magnitude:
        exponent = len(str(magnitude.numerator))-len(str(magnitude.denominator))
        while magnitude < F(10)**exponent:
            exponent -= 1
        while magnitude >= F(10)**(exponent+1):
            exponent += 1
    unit = F(10)**exponent
    outer = base.outward_grid((iv[0]/unit, iv[1]/unit), 8)
    assert outer[0]*unit <= iv[0] <= iv[1] <= outer[1]*unit
    return {'power_of_ten': exponent, 'scaled_interval': base.interval_json(outer)}


def main():
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)

    hashes = {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
              for name in PINNED}
    for name, required in PINNED.items():
        check('pinned_'+name, hashes[name] == required)
    if not all(checks.values()):
        raise RuntimeError('Changed assessed input; stop before calculation')
    source = json.loads((ROOT/'tilted-boundary-metric-2010.json').read_text())
    check('source_no_failures', not source['failures'] and all(source['checks'].values()))
    pi_iv = tuple(F(source['pi_interval'][k]) for k in ('lower', 'upper'))
    sqrt_iv = tuple(F(source['sqrt2_interval'][k]) for k in ('lower', 'upper'))
    check('fixed_input_widths', pi_iv[1]-pi_iv[0] == sqrt_iv[1]-sqrt_iv[0] == F(1, 10**60))
    check('sqrt_squared_endpoints', 0 < sqrt_iv[0]**2 < 2 < sqrt_iv[1]**2)

    bernoulli = [F(1)]
    for m in range(1, 19):
        bernoulli.append(-sum((comb(m+1, k)*bernoulli[k] for k in range(m)), F(0))/(m+1))
    check('all_bernoulli_match', bernoulli == list(map(F, source['bernoulli_0_through_18'])))
    phases = [(F(1), F(0)), (F(1), F(1)), (F(-1), F(0)), (F(-1), F(-1))]
    u = []
    rational_denominators = []
    for n in range(9):
        poly = [base.ZERO]*(n+2)
        for h in range(n+1):
            denominator = factorial(n-h)*factorial(2*h+2)
            rational_denominators.append(denominator)
            factor = -F(factorial(n)*4**h*(4**(h+1)-1)*2**(h+1), denominator)*bernoulli[2*h+2]
            a, b = phases[(n-h) % 4]
            poly[h+1] = factor*a, factor*b
        u.append(poly)
    q = []
    for n in range(7):
        poly = base.padd(base.pscale(u[n], 8*n*n+12*n+7),
                         base.pscale(u[n+2], (2*n+3)*(2*n+5)))
        if n >= 2:
            poly = base.padd(poly, base.pscale(u[n-2], 4*n*(n-1)))
        q.append(poly)
    check('all_source_denominators_positive', all(x > 0 for x in rational_denominators))
    check('all_u_exact_match', u == list(map(decode, source['u_over_S_polynomials'])))
    check('all_q_exact_match', q == list(map(decode, source['beta_over_S_polynomials'])))
    q_iv = [base.peval(poly, pi_iv, sqrt_iv) for poly in q]
    check('all_q_enclosures_match', [base.interval_json(iv) for iv in q_iv] == source['beta_over_S_intervals'])
    check('undamped_top_nonzero', q_iv[6][1] < 0)

    p = [[F(1)]]
    for k in range(6):
        poly = [F(0)]+p[k]
        if k:
            for j, c in enumerate(p[k-1]):
                poly[j] -= F(2*k+1, 2)*c
        p.append([c/(k+1) for c in poly])
        # Check the recurrence coefficient by coefficient, not at test points.
        lhs = [c*(k+1) for c in p[k+1]]
        rhs = [F(0)]+p[k]
        if k:
            for j, c in enumerate(p[k-1]):
                rhs[j] -= F(2*k+1, 2)*c
        check('basis_recurrence_'+str(k), lhs == rhs)
    check('basis_degrees_and_leading_coefficients',
          all(len(p[k]) == k+1 and p[k][k] == F(1, factorial(k)) for k in range(7)))
    b = []
    for j in range(7):
        poly = []
        for k in range(j, 7):
            poly = base.padd(poly, base.pscale(q[k], p[k][j]))
        b.append(poly)
    b_iv = [base.peval(poly, pi_iv, sqrt_iv) for poly in b]
    check('leading_coefficient_identity', b[6] == base.pscale(q[6], F(1, 720)))
    check('actual_degree_six', b_iv[6][1] < 0)
    check('normalization_denominator_excludes_zero', sign(b_iv[6]) != 0)
    if not all(checks.values()):
        raise RuntimeError('Coefficient/degree check failed before normalization')

    # c[0]=1 exactly, c[i]=b[6-i]/b[6], i=1,...,6.
    c = [ONE]+[idiv(b_iv[6-i], b_iv[6]) for i in range(1, 7)]
    s = [(F(6), F(6))]
    newton_records = []
    for j in range(1, 11):
        if j <= 6:
            terms = [base.imul(c[i], s[j-i]) for i in range(1, j)]
            terms.append(base.iscale(c[j], F(j)))
            expression = '-(sum_(i=1)^(j-1) c_i*s_(j-i) + j*c_j)'
        else:
            terms = [base.imul(c[i], s[j-i]) for i in range(1, 7)]
            expression = '-sum_(i=1)^6 c_i*s_(j-i)'
        s.append(base.iscale(isum(terms), F(-1)))
        newton_records.append({'j': j, 'formula': expression,
                               'unsigned_terms': [base.interval_json(iv) for iv in terms],
                               's_j': base.interval_json(s[j])})
    h = [[s[i+j] for j in range(6)] for i in range(6)]
    check('hermite_symmetry', h == [list(row) for row in zip(*h)])
    minors = []
    for n in range(1, 7):
        total = ZERO
        records = []
        for perm in permutations(range(n)):
            inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
            parity = (-1)**inversions
            product = ONE
            for i, j in enumerate(perm):
                product = base.imul(product, h[i][j])
            signed = base.iscale(product, F(parity))
            total = base.iadd(total, signed)
            records.append({'permutation_zero_based': list(perm), 'sign': parity,
                            'signed_product_interval': base.interval_json(signed)})
        check('complete_permutation_count_'+str(n), len(records) == factorial(n))
        minors.append({'minor': n, 'terms': records, 'interval': base.interval_json(total),
                       'sign': sign(total), 'readable_outer_enclosure': short(total)})
    failures = [name for name, ok in checks.items() if not ok]
    unresolved = [m['minor'] for m in minors if not m['sign']]
    signs = [m['sign'] for m in minors]
    complete = not failures and not unresolved
    seq = [1]+signs
    negative = sum(seq[i] != seq[i+1] for i in range(6)) if complete else None
    inertia = {'positive': 6-negative, 'negative': negative, 'zero': 0} if complete else None
    result = ('FINITE_PASS' if negative <= 1 else 'CEILING_COUNTEREXAMPLE') if complete else 'INCONCLUSIVE'
    certificate = {
        'target': 'P_{6,0}=sum_(k=0)^6 beta_k*p_k; fixed undamped endpoint only',
        'reproduction': 'python3 scripts/pollaczek/jensen_zero_endpoint_2049.py',
        'method': 'Exact rational intervals; Newton identities; complete Leibniz sums; Jacobi only if all minors separate',
        'normalization': 'U=P_{6,0}/S, S=sin(pi/8)/sqrt(2)>0; monic polynomial U/b_6',
        'input_sha256': hashes, 'required_sha256': PINNED,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'pi_interval': base.interval_json(pi_iv), 'sqrt2_interval': base.interval_json(sqrt_iv),
        'source_formula_denominators': rational_denominators,
        'bernoulli_0_to_18': list(map(str, bernoulli)),
        'u_over_S_polynomials': [base.poly_json(poly) for poly in u],
        'q_polynomials': [base.poly_json(poly) for poly in q],
        'q_intervals': [base.interval_json(iv) for iv in q_iv],
        'weights': ['1']*7,
        'basis_p_0_to_6': [list(map(str, row)) for row in p],
        'basis_recurrence_denominators': list(range(1, 7)),
        'monomial_coefficients_ascending': [base.poly_json(poly) for poly in b],
        'monomial_intervals': [base.interval_json(iv) for iv in b_iv],
        'normalization_denominator': base.interval_json(b_iv[6]),
        'normalization_denominator_readable': short(b_iv[6]),
        'monic_coefficients_descending': [base.interval_json(iv) for iv in c],
        'actual_degree': 6,
        'newton_records': newton_records,
        'newton_sums_0_to_10': [base.interval_json(iv) for iv in s],
        'hermite_matrix': [[base.interval_json(iv) for iv in row] for row in h],
        'minors': minors, 'leading_determinant_signs': signs,
        'determinant_outer_enclosures': [m['readable_outer_enclosure'] for m in minors],
        'unresolved_determinants': unresolved, 'actual_inertia': inertia,
        'distinct_nonreal_pairs': negative,
        'distinct_real_roots': 6-2*negative if complete else None,
        'required_ceiling': 1, 'ceiling_holds_at_endpoint': negative <= 1 if complete else None,
        'checks': checks, 'failures': failures, 'result': result,
        'scope': 'One theta=0 member; no whole-path, eventual-N, convergence or RH conclusion',
    }
    out = ROOT/'jensen-zero-endpoint-2049.json'
    out.write_text(json.dumps(certificate, indent=2)+'\n')
    print('Result:', result, '; inertia:', inertia)
    print('Actual negative index:', negative, '; required ceiling:', 1, '; minor signs:', signs)
    print('Unresolved minors:', unresolved, '; failures:', failures)
    print('Certificate:', out.relative_to(Path.cwd()))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
