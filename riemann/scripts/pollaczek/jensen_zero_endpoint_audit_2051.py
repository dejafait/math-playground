#!/usr/bin/env python3
"""Independent fixed-input C029w replay; no original helper imports.

Sparse Q[pi,sqrt(2)] construction and exact rational interval arithmetic.
All reconstructed products/endpoints are retained, not only pass flags.
"""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import sys

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(1))
PINNED = {
    'tilted-boundary-metric-2010.json':
        '361e31b72ad348b17f6c2ac785c20f5ab73e27796025bd724af208543e0feaf7',
    'tilted_boundary_metric_2010.py':
        '21cc4fb70b084fde19c62d74a7edb04a2bcdb38fe1a376ea5e7de6d3edbb58fc',
}


def poly_add(*ps):
    ans = {}
    for p in ps:
        for key, v in p.items():
            ans[key] = ans.get(key, Q(0)) + v
    return {k: v for k, v in ans.items() if v}


def poly_scale(p, scalar):
    return {k: v*scalar for k, v in p.items() if v*scalar}


def poly_read(p):
    return {(i, j): Q(c[name]) for i, c in enumerate(p)
            for j, name in enumerate(('rational', 'sqrt2')) if Q(c[name])}


def poly_save(p):
    return [{'pi_degree': i, 'sqrt2_degree': j, 'coefficient': str(v)}
            for (i, j), v in sorted(p.items())]


def read_iv(v):
    return Q(v['lower']), Q(v['upper'])


def save_iv(v):
    return {'lower': str(v[0]), 'upper': str(v[1])}


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def times(a, b):
    corners = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return min(corners), max(corners)


def scale(a, t):
    ends = (a[0]*t, a[1]*t)
    return min(ends), max(ends)


def total(terms):
    terms = list(terms)
    return tuple(sum((v[j] for v in terms), Q(0)) for j in (0, 1))


def horner(p, pi, root2):
    ans = ZERO
    for k in range(max((i for i, _ in p), default=0), -1, -1):
        rational = p.get((k, 0), Q(0))
        coefficient = add((rational, rational), scale(root2, p.get((k, 1), Q(0))))
        ans = add(times(ans, pi), coefficient)
    return ans


def perms_with_sign(available, prefix=(), parity=1):
    # Selecting the r-th remaining column creates exactly r inversions
    # with columns selected on later rows. Each ordered selection occurs once.
    if not available:
        yield prefix, parity
    for r, col in enumerate(available):
        yield from perms_with_sign(available[:r]+available[r+1:],
                                   prefix+(col,), parity*((-1)**r))


def sign(iv):
    return 1 if iv[0] > 0 else -1 if iv[1] < 0 else 0


def main():
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)

    old_path = HERE/'jensen-zero-endpoint-2049.json'
    old = json.loads(old_path.read_text())
    src = json.loads((HERE/'tilted-boundary-metric-2010.json').read_text())
    hashes = {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in PINNED}
    check('assessed_inputs_unchanged', hashes == PINNED == old['input_sha256'] == old['required_sha256'])
    check('calculation_script_hash', hashlib.sha256((HERE/'jensen_zero_endpoint_2049.py').read_bytes()).hexdigest() == old['script_sha256'])
    check('prior_checks_pass', all(old['checks'].values()) and not old['failures'] and not old['unresolved_determinants'])
    pi, root2 = read_iv(src['pi_interval']), read_iv(src['sqrt2_interval'])
    check('unchanged_fixed_intervals', pi == read_iv(old['pi_interval']) and root2 == read_iv(old['sqrt2_interval']))
    check('fixed_interval_widths', pi[1]-pi[0] == root2[1]-root2[0] == Q(1, 10**60))
    check('sqrt2_endpoint_squares', 0 < root2[0]**2 < 2 < root2[1]**2)
    # Containment of pi in this exact interval is the audited2012/C029n input.
    # This audit neither changes it nor assumes an unproved decimal constant.
    if not all(checks.values()):
        raise RuntimeError('Assessed fixed input changed; no dependent replay authorized')

    bern = [Q(1)]
    for m in range(1, 19):
        bern.append(-sum((Q(comb(m+1, k))*bern[k] for k in range(m)), Q(0))/Q(m+1))
    check('bernoulli_complete', bern == list(map(Q, src['bernoulli_0_through_18'])) == list(map(Q, old['bernoulli_0_to_18'])))
    phases = ((1, 0), (1, 1), (-1, 0), (-1, -1))
    denominators, u = [], []
    for n in range(9):
        terms = []
        for h in range(n+1):
            den = factorial(n-h)*factorial(2*h+2)
            denominators.append(den)
            value = -Q(factorial(n)*4**h*(4**(h+1)-1)*2**(h+1), den)*bern[2*h+2]
            terms.append({(h+1, j): value*t for j, t in enumerate(phases[(n-h) % 4]) if t})
        u.append(poly_add(*terms))
    check('all_source_denominators', all(d > 0 for d in denominators) and denominators == old['source_formula_denominators'])
    check('all_u_exact_coefficients', u == list(map(poly_read, src['u_over_S_polynomials'])) == list(map(poly_read, old['u_over_S_polynomials'])))
    q = []
    for k in range(7):
        q.append(poly_add(poly_scale(u[k], 8*k*k+12*k+7),
                          poly_scale(u[k+2], (2*k+3)*(2*k+5)),
                          poly_scale(u[k-2], 4*k*(k-1)) if k >= 2 else {}))
    check('all_q_exact_coefficients', q == list(map(poly_read, src['beta_over_S_polynomials'])) == list(map(poly_read, old['q_polynomials'])))
    qi = [horner(v, pi, root2) for v in q]
    check('all_q_complete_endpoints', qi == list(map(read_iv, old['q_intervals'])) == list(map(read_iv, src['beta_over_S_intervals'])))
    check('all_seven_weights_one', list(map(Q, old['weights'])) == [Q(1)]*7)

    # Basis stored sparsely in t, separately from source pi/sqrt(2) polynomials.
    basis = [{0: Q(1)}]
    for k in range(6):
        row = {j+1: v/Q(k+1) for j, v in basis[k].items()}
        if k:
            for j, v in basis[k-1].items():
                row[j] = row.get(j, Q(0))-Q(2*k+1, 2*(k+1))*v
        basis.append({j: v for j, v in row.items() if v})
    dense_basis = [[p.get(j, Q(0)) for j in range(k+1)] for k, p in enumerate(basis)]
    check('basis_all_coefficients', dense_basis == [list(map(Q, p)) for p in old['basis_p_0_to_6']])
    check('basis_degrees_leading_and_denominators', all(max(p) == k and p[k] == Q(1, factorial(k)) for k, p in enumerate(basis)) and old['basis_recurrence_denominators'] == list(range(1, 7)))
    b = [poly_add(*(poly_scale(q[k], basis[k].get(j, Q(0))) for k in range(7))) for j in range(7)]
    check('all_monomial_exact_coefficients', b == list(map(poly_read, old['monomial_coefficients_ascending'])))
    check('leading_exact_identity', b[6] == poly_scale(q[6], Q(1, 720)))
    bi = [horner(v, pi, root2) for v in b]
    check('all_monomial_complete_endpoints', bi == list(map(read_iv, old['monomial_intervals'])))
    check('normalization_complete_endpoints', bi[6] == read_iv(old['normalization_denominator']))
    check('actual_degree_six_before_division', bi[6][1] < 0 and old['actual_degree'] == 6)
    if not all(checks.values()):
        raise RuntimeError('Coefficient mismatch; stop before dependent normalization')

    # b6 is strictly negative, so reciprocal order reverses, with no zero pole.
    reciprocal = (1/bi[6][1], 1/bi[6][0])
    c = [ONE]+[times(bi[6-i], reciprocal) for i in range(1, 7)]
    check('all_monic_complete_endpoints', c == list(map(read_iv, old['monic_coefficients_descending'])))
    s = [(Q(6), Q(6))]
    newton = []
    for j in range(1, 11):
        terms = [times(c[k], s[j-k]) for k in range(1, min(j, 7))]
        if j <= 6:
            terms.append(scale(c[j], Q(j)))
        s.append(scale(total(terms), Q(-1)))
        rec = old['newton_records'][j-1]
        expected_formula = ('-(sum_(i=1)^(j-1) c_i*s_(j-i) + j*c_j)' if j <= 6
                            else '-sum_(i=1)^6 c_i*s_(j-i)')
        check('newton_terms_and_sum_'+str(j), rec['j'] == j and rec['formula'] == expected_formula and terms == list(map(read_iv, rec['unsigned_terms'])) and s[j] == read_iv(rec['s_j']))
        newton.append({'j': j, 'unsigned_terms': list(map(save_iv, terms)), 'sum': save_iv(s[j])})
    check('all_eleven_newton_sums', s == list(map(read_iv, old['newton_sums_0_to_10'])) and len(old['newton_records']) == 10)
    h = [[s[i+j] for j in range(6)] for i in range(6)]
    check('all_hermite_entries', h == [[read_iv(v) for v in row] for row in old['hermite_matrix']])
    check('hermite_real_symmetric', h == list(map(list, zip(*h))))

    required_bounds = [((Q(6), Q(6)), 0),
                       ((Q('3.37023139'), Q('3.37023140')), 3),
                       ((Q('8.10122066'), Q('8.10122067')), 7),
                       ((Q('-8.59941170'), Q('-8.59941169')), 13),
                       ((Q('-6.63531988'), Q('-6.63531987')), 20),
                       ((Q('-1.63766052'), Q('-1.63766051')), 27)]
    rebuilt, signs = [], []
    for n in range(1, 7):
        reference = old['minors'][n-1]
        terms = []
        for perm, parity in perms_with_sign(tuple(range(n))):
            product = ONE
            # Reverse row order to avoid replaying the original loop verbatim.
            for i in range(n-1, -1, -1):
                product = times(product, s[i+perm[i]])
            terms.append((perm, parity, scale(product, Q(parity))))
        columns = [p for p, _, _ in terms]
        check('permutation_coverage_'+str(n), len(terms) == len(set(columns)) == factorial(n) and all(sorted(p) == list(range(n)) for p in columns))
        check('independent_parities_'+str(n), all(e == (-1)**sum(p[i] > p[j] for i in range(n) for j in range(i+1, n)) for p, e, _ in terms))
        stored = [(tuple(t['permutation_zero_based']), t['sign'], read_iv(t['signed_product_interval'])) for t in reference['terms']]
        check('every_signed_product_endpoint_'+str(n), terms == stored)
        delta = total(v for _, _, v in terms)
        check('determinant_complete_endpoints_'+str(n), reference['minor'] == n and delta == read_iv(reference['interval']))
        bounds, exponent = required_bounds[n-1]
        outer = tuple(v*Q(10)**exponent for v in bounds)
        check('canonical_outer_bounds_'+str(n), outer[0] <= delta[0] <= delta[1] <= outer[1])
        r = reference['readable_outer_enclosure']
        saved_outer = tuple(v*Q(10)**r['power_of_ten'] for v in read_iv(r['scaled_interval']))
        check('saved_outer_bounds_'+str(n), saved_outer[0] <= delta[0] <= delta[1] <= saved_outer[1])
        signs.append(sign(delta))
        check('strict_sign_'+str(n), signs[-1] != 0 and signs[-1] == reference['sign'])
        rebuilt.append({'n': n, 'terms': [{'permutation': p, 'sign': e, 'interval': save_iv(v)} for p, e, v in terms],
                        'interval': save_iv(delta), 'sign': signs[-1],
                        'required_outer_bounds': save_iv(outer)})
    check('six_minors_and_stated_signs', len(old['minors']) == 6 and signs == old['leading_determinant_signs'] == [1, 1, 1, -1, -1, -1])
    seq = [1]+signs
    negative = sum(a != b for a, b in zip(seq, seq[1:])) if all(signs) else None
    inertia = {'positive': 6-negative, 'negative': negative, 'zero': 0} if negative is not None else None
    check('claimed_inertia_and_root_counts', inertia == old['actual_inertia'] == {'positive': 5, 'negative': 1, 'zero': 0} and old['distinct_nonreal_pairs'] == negative and old['distinct_real_roots'] == 4)
    check('ceiling_one_only_at_endpoint', old['required_ceiling'] == 1 and old['ceiling_holds_at_endpoint'] is True and negative == 1)
    leading_required = (Q('-8.04778826e-5'), Q('-8.04778825e-5'))
    check('canonical_leading_bounds', leading_required[0] <= bi[6][0] <= bi[6][1] <= leading_required[1])
    failures = [k for k, v in checks.items() if not v]
    report = {
        'result': 'PASS' if not failures else 'FAIL', 'checks': checks, 'failures': failures,
        'method': 'Independent sparse source/basis reconstruction; rational interval Newton identities; recursive signed-permutation products without original helpers',
        'reproduction': 'python3 scripts/pollaczek/jensen_zero_endpoint_audit_2051.py',
        'input_certificate_sha256': hashlib.sha256(old_path.read_bytes()).hexdigest(),
        'pinned_source_sha256': hashes,
        'audit_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'pi_interval': save_iv(pi), 'sqrt2_interval': save_iv(root2),
        'source_formula_denominators': denominators, 'bernoulli_0_to_18': list(map(str, bern)),
        'u_over_S_polynomials': list(map(poly_save, u)), 'q_polynomials': list(map(poly_save, q)),
        'q_intervals': list(map(save_iv, qi)), 'weights': ['1']*7,
        'basis_p_0_to_6': [[str(v) for v in row] for row in dense_basis],
        'monomial_coefficients': list(map(poly_save, b)), 'monomial_intervals': list(map(save_iv, bi)),
        'normalization_divisor': save_iv(bi[6]), 'normalization_reciprocal': save_iv(reciprocal),
        'monic_coefficients': list(map(save_iv, c)), 'newton_records': newton,
        'newton_sums_0_to_10': list(map(save_iv, s)),
        'hermite_matrix': [[save_iv(v) for v in row] for row in h], 'minors': rebuilt,
        'signed_product_count': sum(len(m['terms']) for m in rebuilt),
        'actual_inertia': inertia, 'actual_negative_index': negative, 'required_ceiling': 1,
        'unresolved_minors': [j+1 for j, e in enumerate(signs) if not e],
        'canonical_leading_outer_bounds': save_iv(leading_required),
        'scope': 'Fixed degree six, theta zero only; no homotopy, eventual index, convergence or RH claim',
    }
    path = HERE/'jensen-zero-endpoint-audit-2051.json'
    path.write_text(json.dumps(report, indent=2)+'\n')
    print('Result:', report['result'], '; checks:', len(checks), '; failures:', failures)
    print('Complete products:', report['signed_product_count'], '; required:', sum(factorial(n) for n in range(1, 7)))
    print('Minor signs:', signs, '; inertia:', inertia)
    print('Actual negative index:', negative, '; required ceiling:', 1, '; unresolved:', report['unresolved_minors'])
    for m, (bounds, exponent) in zip(rebuilt, required_bounds):
        print('Delta', m['n'], ': actual full enclosure contained in', tuple(map(str, bounds)), '*10^', exponent)
    print('Full reconstructed evidence:', path.relative_to(Path.cwd()))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
