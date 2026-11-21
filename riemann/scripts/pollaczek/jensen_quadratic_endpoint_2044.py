#!/usr/bin/env python3
"""One fixed N=6 test, exact Q(sqrt(2))[pi] and rational intervals.

Run from riemann: python3 scripts/pollaczek/jensen_quadratic_endpoint_2044.py
The 2010 helper is imported for exact arithmetic only; its main is not run.
No precision increase, sweep, root count or fitted correction is performed.
"""
from fractions import Fraction as F
from math import comb, factorial, isqrt
from pathlib import Path
import hashlib
import json

import tilted_boundary_metric_2010 as h


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == h.ZERO:
        p.pop()
    return p


def sub(a, b):
    return trim(h.padd(a, h.pscale(b, -1)))


def radd(a, b):
    return [(a[i] if i < len(a) else F(0)) +
            (b[i] if i < len(b) else F(0))
            for i in range(max(len(a), len(b)))]


def rscale(p, c):
    return [c*x for x in p]


def basis_expand(coefficients, basis):
    """Field-valued basis coefficients -> monomial-in-t coefficients."""
    out = [[h.ZERO] for _ in range(len(coefficients))]
    for k, coefficient in enumerate(coefficients):
        for j, scalar in enumerate(basis[k]):
            out[j] = trim(h.padd(out[j], h.pscale(coefficient, scalar)))
    return out


def basis_convert(monomials, basis):
    """Triangular elimination using lc(p_k)=1/k!, exact in the field."""
    remainder = [trim(p) for p in monomials]
    coefficients = [[h.ZERO] for _ in remainder]
    for k in reversed(range(len(remainder))):
        coefficients[k] = trim(h.pscale(remainder[k], 1/basis[k][k]))
        for j, scalar in enumerate(basis[k]):
            remainder[j] = sub(remainder[j], h.pscale(coefficients[k], scalar))
    return coefficients, remainder


def field_vector_json(vector):
    return [h.poly_json(trim(p)) for p in vector]


def main():
    checks, failures = {}, []

    def check(name, value):
        checks[name] = bool(value)
        if not value:
            failures.append(name)

    source_path = Path(__file__).with_name('tilted-boundary-metric-2010.json')
    source = json.loads(source_path.read_text())
    check('input_certificate_no_failures', source['failures'] == [])
    pi_interval = tuple(F(source['pi_interval'][key]) for key in ('lower', 'upper'))
    sqrt2_interval = tuple(F(source['sqrt2_interval'][key]) for key in ('lower', 'upper'))
    # Reproduce, without changing, the existing C029n enclosures.
    atan5, atan5_data = h.arctan_bounds(5, 48)
    atan239, atan239_data = h.arctan_bounds(239, 48)
    machin = h.iadd(h.iscale(atan5, 16), h.iscale(atan239, -4))
    check('unchanged_pi_interval', pi_interval == h.outward_grid(machin, 60))
    scale = 10**60
    b = isqrt(2*scale**2)
    check('unchanged_sqrt2_interval', sqrt2_interval == (F(b, scale), F(b+1, scale)))
    check('sqrt2_squared_endpoints', 0 < sqrt2_interval[0]**2 < 2 < sqrt2_interval[1]**2)

    bernoulli = [F(1)]
    for m in range(1, 19):
        bernoulli.append(-sum((comb(m+1,k)*bernoulli[k] for k in range(m)), F(0))/(m+1))
    check('unchanged_bernoulli_table', [h.rational(x) for x in bernoulli] ==
          source['bernoulli_0_through_18'])
    phases = [(F(1),F(0)), (F(1),F(1)), (F(-1),F(0)), (F(-1),F(-1))]
    u = []
    for n in range(9):
        p = [h.ZERO] * (n+2)
        for j in range(n+1):
            c = (-F(factorial(n)) * 4**j * (4**(j+1)-1) * bernoulli[2*j+2] * 2**(j+1)
                 / (factorial(n-j)*factorial(2*j+2)))
            a, b = phases[(n-j) % 4]
            p[j+1] = (c*a, c*b)
        u.append(p)
    check('all_nine_u_match_C029n', field_vector_json(u) == source['u_over_S_polynomials'])

    beta = []
    for k in range(7):
        p = h.padd(h.pscale(u[k], 8*k*k+12*k+7),
                   h.pscale(u[k+2], (2*k+3)*(2*k+5)))
        if k >= 2:
            p = h.padd(p, h.pscale(u[k-2], 4*k*(k-1)))
        beta.append(trim(p))
    check('all_seven_beta_match_C029n', field_vector_json(beta) == source['beta_over_S_polynomials'])
    weights = [F(factorial(6), factorial(6-k)*6**k) if k <= 6 else F(0)
               for k in range(11)]

    # Build p_0,...,p_10 using only recurrence (2), no negative index.
    basis = [[F(1)], [F(0), F(1)]]
    for k in range(1, 10):
        basis.append(rscale(radd([F(0)]+basis[k],
                                rscale(basis[k-1], -F(2*k+1,2))), F(1,k+1)))
    check('basis_leading_coefficients', all(p[-1] == F(1,factorial(k))
                                          for k,p in enumerate(basis)))

    # Column n is the basis coefficient vector of (1+4t^2)p_n.
    multiplication_formula, multiplication_direct = [], []
    for n in range(9):
        column = [F(0)] * 11
        column[n+2] = F(4*(n+1)*(n+2))
        column[n] = F(8*n*n+12*n+7)
        if n >= 2:
            column[n-2] = F((2*n-1)*(2*n+1))
        multiplication_formula.append(column)
        qp = radd(basis[n], [F(0), F(0)]+rscale(basis[n], 4))
        mono = [[(v,F(0))] for v in qp] + [[h.ZERO]]*(11-len(qp))
        converted, remainder = basis_convert(mono, basis)
        direct = [p[0][0] for p in converted]
        check('multiplication_all_components_rational_n'+str(n),
              all(p == [(direct[k],F(0))] for k,p in enumerate(converted)))
        check('multiplication_elimination_zero_n'+str(n),
              all(p == [h.ZERO] for p in remainder))
        check('source9_equals_recurrence2_n'+str(n), direct == column)
        multiplication_direct.append(direct)

    def multiply_q(vector):
        out = [[h.ZERO] for _ in range(11)]
        for n,p in enumerate(vector):
            for k,c in enumerate(multiplication_formula[n]):
                out[k] = trim(h.padd(out[k], h.pscale(p,c)))
        return out

    qA = multiply_q(u)
    u_mono = basis_expand(u, basis)
    direct_qA_mono = [[h.ZERO] for _ in range(11)]
    for j,p in enumerate(u_mono):
        direct_qA_mono[j] = trim(h.padd(direct_qA_mono[j], p))
        direct_qA_mono[j+2] = trim(h.padd(direct_qA_mono[j+2], h.pscale(p,4)))
    direct_qA, rem = basis_convert(direct_qA_mono, basis)
    check('full_qA_independent_polynomial_match', direct_qA == qA and all(p == [h.ZERO] for p in rem))
    JqA = [trim(h.pscale(p,weights[k])) for k,p in enumerate(qA)]
    Ju = [trim(h.pscale(p,weights[k])) for k,p in enumerate(u)]
    qJu = multiply_q(Ju)
    R = [sub(a,b) for a,b in zip(JqA,qJu)]
    T = [trim(h.pscale(beta[k],weights[k])) if k <= 6 else [h.ZERO] for k in range(11)]
    identity_residual = [sub(a,b) for a,b in zip(JqA,T)]
    check('full_numerator_JqA_equals_T6', all(p == [h.ZERO] for p in identity_residual))
    check('R_has_no_modes_above_8', all(p == [h.ZERO] for p in R[9:]))

    bulk = {}
    for k in (2,3,4):
        interval = h.peval(R[k], pi_interval, sqrt2_interval)
        exact_zero = R[k] == [h.ZERO]
        sign = ('zero' if exact_zero else 'positive' if interval[0] > 0 else
                'negative' if interval[1] < 0 else 'unresolved')
        bulk[str(k)] = {'polynomial_over_S': h.poly_json(R[k]),
                        'interval_over_S': h.interval_json(interval),
                        'readable_outer_interval_over_S': h.interval_json(h.outward_grid(interval,12)),
                        'exact_zero': exact_zero, 'sign': sign}
    result = ('IMPLEMENTATION_FAILURE' if failures else
              'ENDPOINT_ONLY_ANSATZ_REJECTED' if any(v['sign'] in ('positive','negative') for v in bulk.values()) else
              'FINITE_PASS_ONLY' if all(v['exact_zero'] for v in bulk.values()) else 'INCONCLUSIVE')
    out = Path(__file__).with_name('jensen-quadratic-endpoint-2044.json')
    certificate = {
        'target': 'Fixed N=6: R=J6((1+4t^2)A8)-(1+4t^2)J6(A8); bulk p2,p3,p4 zero?',
        'normalization': 'S=sin(pi/8)/sqrt(2)>0; every field vector divided by S',
        'field_encoding': 'ascending pi powers, each rational+sqrt2*sqrt(2); vectors ascending p_k unless named monomial',
        'reproduction': 'python3 scripts/pollaczek/jensen_quadratic_endpoint_2044.py',
        'input_hashes': {str(p.relative_to(Path.cwd())): hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in (source_path.resolve(), Path(h.__file__).resolve(), Path(__file__).resolve())},
        'pi_interval': h.interval_json(pi_interval), 'sqrt2_interval': h.interval_json(sqrt2_interval),
        'atan5': atan5_data, 'atan239': atan239_data, 'pi_machin_interval': h.interval_json(machin),
        'bernoulli_0_through_18': [h.rational(x) for x in bernoulli],
        'u_over_S': field_vector_json(u), 'beta_over_S': field_vector_json(beta),
        'p_basis_monomial': [[h.rational(v) for v in p] for p in basis],
        'weights': [h.rational(w) for w in weights],
        'multiplication_formula_columns': [[h.rational(v) for v in p] for p in multiplication_formula],
        'multiplication_direct_columns': [[h.rational(v) for v in p] for p in multiplication_direct],
        'qA_over_S': field_vector_json(qA), 'qA_direct_over_S': field_vector_json(direct_qA),
        'qA_monomial_over_S': field_vector_json(direct_qA_mono),
        'JqA_over_S': field_vector_json(JqA), 'Ju_over_S': field_vector_json(Ju),
        'qJu_over_S': field_vector_json(qJu), 'R_over_S': field_vector_json(R),
        'T6_over_S': field_vector_json(T), 'numerator_identity_residual': field_vector_json(identity_residual),
        'bulk': bulk, 'required_bounds': 'All p2,p3,p4 coefficients exactly zero; one strict nonzero interval rejects',
        'checks': checks, 'failures': failures, 'result': result,
        'scope': 'One fixed test only; no uniform index, auxiliary hyperbolicity or RH conclusion.'}
    out.write_text(json.dumps(certificate,indent=2)+'\n')
    print('Result:', result)
    print('Required:', certificate['required_bounds'])
    for k,v in bulk.items():
        print('p'+k+'/S:', v['readable_outer_interval_over_S'], ';', v['sign'])
    print('Numerator identity:', checks['full_numerator_JqA_equals_T6'])
    print('Checks:', len(checks), '; failures:', failures)
    print('Certificate:', out.relative_to(Path.cwd()))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
