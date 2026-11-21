#!/usr/bin/env python3
"""Independent, fixed-input C029x audit; no original mathematical imports.

Dense Q[s][X] reconstruction, original-order endpoint replay and separate
formal reciprocal-series logarithmic derivative. All comparisons are exact.
"""
from fractions import Fraction as R
from math import factorial, comb
from pathlib import Path
import hashlib
import json
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
OUT = HERE / 'consecutive-hermite-audit-2056.json'
TARGET = "Independently audit C029x's fixed degree-6/7 Newton-sum principal-minor certificate with unchanged constants, both Newton cases, complete padding and rational witnesses, using a separate logarithmic-derivative reconstruction."
data = {'target': TARGET, 'status': 'STARTED', 'checks': {},
        'scope': 'N=6,7; original constants; principal indices 0,1,2 only',
        'classification': 'REPRODUCTION', 'comparisons': {}}


def verify(name, ok):
    data['checks'][name] = bool(ok)


def same(name, actual, expected):
    verify(name, actual == expected)
    data['comparisons'][name] = 'EXACT_MATCH' if actual == expected else 'MISMATCH'


def save(stage):
    data['status'] = stage
    data['failures'] = [k for k, v in data['checks'].items() if not v]
    OUT.write_text(json.dumps(data, indent=2) + '\n')


def interval(obj):
    return R(obj['lower']), R(obj['upper'])


def encode_iv(a):
    return {'lower': str(a[0]), 'upper': str(a[1])}


ZERO = (R(0), R(0))
ONE = (R(1), R(1))


def plus(a, b):
    return a[0]+b[0], a[1]+b[1]


def times(a, b):
    endpoints = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return min(endpoints), max(endpoints)


def scaled(a, v):
    return (a[0]*v, a[1]*v) if v >= 0 else (a[1]*v, a[0]*v)


def minus(a, b):
    return a[0]-b[1], a[1]-b[0]


def inverse(a):
    if a[0] <= 0 <= a[1]:
        raise ArithmeticError('nonseparated division')
    return 1/a[1], 1/a[0]


def contains(a, b):
    return a[0] <= b[0] <= b[1] <= a[1]


def outward(a, places):
    unit = 10**places
    lo, hi = a[0]*unit, a[1]*unit
    return R(lo.numerator//lo.denominator, unit), R(-((-hi.numerator)//hi.denominator), unit)


# Polynomials are dense lists of pairs (rational, sqrt2 coefficient).
def trim(p):
    while len(p) > 1 and p[-1] == (0, 0):
        p.pop()
    return p


def linear_combination(terms):
    out = [(R(0), R(0)) for _ in range(max((len(p) for c, p in terms), default=1))]
    for c, p in terms:
        for i, (a, b) in enumerate(p):
            out[i] = out[i][0]+c*a, out[i][1]+c*b
    return trim(out)


def dense_read(rows):
    return trim([(R(row['rational']), R(row['sqrt2'])) for row in rows])


def sparse_read(rows):
    out = [(R(0), R(0)) for _ in range(max((row[0] for row in rows), default=0)+1)]
    for i, j, c in rows:
        a = list(out[i])
        a[j] = R(c)
        out[i] = tuple(a)
    return trim(out)


def encode_poly(p):
    return [[str(a), str(b)] for a, b in p]


def evaluate(p, pi, sqrt2):
    value = ZERO
    for a, b in reversed(p):
        value = plus(times(value, pi), plus((a, a), scaled(sqrt2, b)))
    return value


# Formal polynomials in independent c_1,...,c_d, encoded by exponent tuples.
def formal_add(a, b, factor=1):
    out = dict(a)
    for e, v in b.items():
        out[e] = out.get(e, 0)+factor*v
        if out[e] == 0:
            del out[e]
    return out


def formal_mul(a, b):
    out = {}
    for e, v in a.items():
        for f, w in b.items():
            g = tuple(x+y for x, y in zip(e, f))
            out[g] = out.get(g, 0)+v*w
    return {e: v for e, v in out.items() if v}


def encode_formal(p):
    return [[list(e), v] for e, v in sorted(p.items())]


def formal_log_derivative(degree, limit):
    one = {(0,)*degree: 1}
    q = [one]
    for j in range(degree):
        e = [0]*degree
        e[j] = 1
        q.append({tuple(e): 1})
    reciprocal = [one]
    for k in range(1, limit+1):
        value = {}
        for j in range(1, min(k, degree)+1):
            value = formal_add(value, formal_mul(q[j], reciprocal[k-j]), -1)
        reciprocal.append(value)
    numerator = [{e: (degree-j)*v for e, v in q[j].items() if degree-j}
                 for j in range(degree+1)]
    result = []
    for k in range(limit+1):
        value = {}
        for j in range(min(k, degree)+1):
            value = formal_add(value, formal_mul(numerator[j], reciprocal[k-j]))
        result.append(value)
    residuals, inverse_residuals = [], []
    for k in range(limit+1):
        product, iproduct = {}, {}
        for j in range(min(k, degree)+1):
            product = formal_add(product, formal_mul(q[j], result[k-j]))
            iproduct = formal_add(iproduct, formal_mul(q[j], reciprocal[k-j]))
        residuals.append(formal_add(product, numerator[k] if k <= degree else {}, -1))
        inverse_residuals.append(formal_add(iproduct, one if k == 0 else {}, -1))
    return q, reciprocal, numerator, result, residuals, inverse_residuals


def formal_evaluate(p, c):
    value = ZERO
    for e, v in sorted(p.items()):
        term = ONE
        for j, power in enumerate(e, 1):
            for _ in range(power):
                term = times(term, c[j])
        value = plus(value, scaled(term, v))
    return value


def products(matrix):
    # Explicit Leibniz terms avoid the original permutation enumeration helper.
    choices = [((0, 1, 2), 1), ((0, 2, 1), -1), ((1, 0, 2), -1),
               ((1, 2, 0), 1), ((2, 0, 1), 1), ((2, 1, 0), -1)]
    rows, total = [], ZERO
    for perm, sign in choices:
        value = ONE
        for i in range(3):
            value = times(value, matrix[i][perm[i]])
        signed = scaled(value, sign)
        rows.append({'permutation': list(perm), 'sign': sign,
                     'unsigned_product': encode_iv(value), 'signed_product': encode_iv(signed)})
        total = plus(total, signed)
    return rows, total


def main():
    filenames = ['tilted-boundary-metric-2010.json', 'tilted-affine-quotient-residual-2022.json',
                 'consecutive-hermite-rank-2054.json', 'tilted-boundary-metric-audit-2012.json',
                 'tilted-affine-residual-audit-2024.json']
    blobs = [(HERE/name).read_bytes() for name in filenames]
    data['input_sha256'] = dict(zip(filenames, [hashlib.sha256(b).hexdigest() for b in blobs]))
    data['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    source, previous, claimed, audit2012, audit2024 = [json.loads(b) for b in blobs]
    source_hash = data['input_sha256'][filenames[0]]
    same('fixed_C029n_hash', source_hash, '361e31b72ad348b17f6c2ac785c20f5ab73e27796025bd724af208543e0feaf7')
    same('audit2012_input', audit2012['input_sha256'], source_hash)
    for name in filenames[:2]:
        same('claimed_pin_'+name, claimed['input_sha256'][name], data['input_sha256'][name])
        same('audit2024_pin_'+name, audit2024['input_sha256'][name], data['input_sha256'][name])
    same('original_script_hash', claimed['script_sha256'],
         hashlib.sha256((HERE/'consecutive_hermite_rank_2054.py').read_bytes()).hexdigest())
    for name, obj in zip(filenames, (source, previous, claimed, audit2012, audit2024)):
        verify('no_recorded_failure_'+name, not obj['failures'] and all(obj['checks'].values()))
    verify('prior_complete_certification', not previous['incomplete_certification'])
    pi, sqrt2 = interval(source['pi_interval']), interval(source['sqrt2_interval'])
    for key in ('pi_interval', 'sqrt2_interval'):
        same('unchanged_'+key, claimed[key], source[key])
        same('previous_'+key, previous[key], source[key])
    verify('sqrt2_integer_proof', 0 < sqrt2[0] and sqrt2[0]**2 < 2 < sqrt2[1]**2)
    atan_rows, atan_intervals = [], []
    for d, key in ((5, 'atan5'), (239, 'atan239')):
        terms = [R((-1)**j, (2*j+1)*d**(2*j+1)) for j in range(48)]
        total, error = sum(terms, R(0)), R(1, 97*d**97)
        row = source[key]
        same(key+'_all_terms', list(map(R, row['terms'])), terms)
        verify(key+'_all_metadata', row['term_count'] == 48 and R(row['argument']) == R(1, d)
               and R(row['partial_sum']) == total and R(row['positive_remainder_upper']) == error)
        atan_rows.append({'denominator': d, 'terms': list(map(str, terms)),
                          'sum': str(total), 'error': str(error)})
        atan_intervals.append((total, total+error))
    machin = minus(scaled(atan_intervals[0], 16), scaled(atan_intervals[1], 4))
    same('complete_machin_source', machin, interval(source['pi_machin_interval']))
    same('complete_machin_claim', machin, interval(claimed['machin_interval']))
    verify('machin_enclosed', contains(pi, machin))
    data['constants'] = {'pi': encode_iv(pi), 'sqrt2': encode_iv(sqrt2),
                         'arctangents': atan_rows, 'machin': encode_iv(machin),
                         'analytic_input': 'C029n Machin angle branch and integral remainder proof, imported'}

    # z/(exp(z)-1): invert the rational series (exp(z)-1)/z.
    inv_exp = [R(1)]
    for k in range(1, 21):
        inv_exp.append(-sum((inv_exp[k-j]/factorial(j+1) for j in range(1, k+1)), R(0)))
    bernoulli = [inv_exp[k]*factorial(k) for k in range(21)]
    verify('all_B_defining_recurrences', bernoulli[0] == 1 and all(
        (k+1)*bernoulli[k]+sum(comb(k+1, j)*bernoulli[j] for j in range(k)) == 0
        for k in range(1, 21)))
    same('B0_to_B20_previous', bernoulli, list(map(R, previous['bernoulli_0_to_20'])))
    same('B0_to_B20_claim', bernoulli, list(map(R, claimed['bernoulli_0_to_20'])))
    verify('B1_B20_values', bernoulli[1] == -R(1, 2) and bernoulli[20] == -R(174611, 330))
    phases = [(1, 0), (1, 1), (-1, 0), (-1, -1)]
    v = []
    for k in range(10):
        poly = [(R(0), R(0))]*(k+2)
        for h in range(k+1):
            r, s = phases[(k-h) % 4]
            value = -R(factorial(k)*4**h*(4**(h+1)-1)*2**(h+1),
                       factorial(k-h)*factorial(2*h+2))*bernoulli[2*h+2]
            poly[h+1] = value*r, value*s
        v.append(trim(poly))
    beta = []
    for k in range(8):
        terms = [(8*k*k+12*k+7, v[k]), ((2*k+3)*(2*k+5), v[k+2])]
        if k > 1:
            terms.append((4*k*(k-1), v[k-2]))
        beta.append(linear_combination(terms))
    same('all_v_previous', v, list(map(dense_read, previous['u_over_S_polynomials'])))
    same('all_beta_previous', beta, list(map(dense_read, previous['beta_over_S_polynomials'])))
    same('all_v_source', v[:9], list(map(dense_read, source['u_over_S_polynomials'])))
    same('all_beta_source', beta[:7], list(map(dense_read, source['beta_over_S_polynomials'])))
    same('all_v_claim', v, list(map(sparse_read, claimed['v_0_to_9'])))
    same('all_beta_claim', beta, list(map(sparse_read, claimed['beta_over_S_0_to_7'])))
    basis = [[R(1)]]
    for k in range(1, 8):
        row = [R(0)]*(k+1)
        for i in range(k+1):
            row[i] = ((basis[k-1][i-1] if i > 0 else 0)
                      - R(2*k-1, 2)*(basis[k-2][i] if k >= 2 and i < k-1 else 0))/k
        basis.append(row)
    same('all_basis_previous', basis, [list(map(R, row)) for row in previous['basis_p_0_to_7']])
    same('all_basis_claim', basis, [list(map(R, row)) for row in claimed['basis_p_0_to_7']])
    verify('all_basis_degrees', all(len(p) == k+1 and p[-1] == R(1, factorial(k)) for k, p in enumerate(basis)))
    data['coefficients'] = {'bernoulli': list(map(str, bernoulli)),
                             'v': list(map(encode_poly, v)), 'beta': list(map(encode_poly, beta)),
                             'basis': [list(map(str, row)) for row in basis]}
    data['degrees'] = {}
    matrices, alternate_matrices = {}, {}
    for n in (6, 7):
        key = str(n)
        weights = [R(1)]
        for k in range(1, n+1):
            weights.append(weights[-1]*R(n-k+1, n))
        jensen = [linear_combination([(weights[k], beta[k])]) for k in range(n+1)]
        monomial = [linear_combination([(basis[k][i], jensen[k]) for k in range(i, n+1)]) for i in range(n+1)]
        stored = claimed['polynomials'][key]
        same(key+'_weights_previous', weights, list(map(R, previous['weights'][key])))
        same(key+'_weights_claim', weights, list(map(R, stored['weights'])))
        for label, polynomials, previous_key, claim_key in (
                ('Jensen', jensen, 'Jensen_coefficients', 'Jensen_coefficients'),
                ('monomial', monomial, 'U_monomial_coefficients', 'monomial_coefficients')):
            same(key+'_'+label+'_previous', polynomials, list(map(dense_read, previous[previous_key][key])))
            same(key+'_'+label+'_claim', polynomials, list(map(sparse_read, stored[claim_key])))
        enclosed = [evaluate(p, pi, sqrt2) for p in monomial]
        same(key+'_all_coefficient_endpoints', enclosed, list(map(interval, stored['coefficient_intervals'])))
        same(key+'_leading_previous', enclosed[-1], interval(previous['leading_coefficient_intervals'][key]))
        same(key+'_leading_claim', enclosed[-1], interval(stored['leading_interval']))
        same(key+'_leading_outer', outward(enclosed[-1], 12), interval(stored['leading_outer']))
        verify(key+'_actual_degree', len(monomial) == n+1 and
               (enclosed[-1][1] < 0 if n == 6 else enclosed[-1][0] > 0) and stored['actual_degree'] == n)
        lead_inv = inverse(enclosed[-1])
        c = [ONE]+[times(enclosed[n-j], lead_inv) for j in range(1, n+1)]
        sums = [(R(n), R(n))]
        cases = []
        for k in range(1, 2*n-1):
            total = ZERO
            for j in range(1, k if k <= n else n+1):
                total = plus(total, times(c[j], sums[k-j]))
            if k <= n:
                total = plus(total, scaled(c[k], k))
                cases.append('k<=degree: k*c_k, no c_k*s_0 term')
            else:
                cases.append('k>degree: all degree terms, no k*c_k term')
            sums.append(scaled(total, -1))
        newton = claimed['Newton'][key]
        same(key+'_leading_reciprocal', lead_inv, interval(newton['leading_reciprocal']))
        same(key+'_every_monic_coefficient', c, list(map(interval, newton['monic_coefficients_c0_to_cd'])))
        same(key+'_both_case_metadata', cases, newton['cases_k1_onward'])
        same(key+'_every_Newton_endpoint', sums, list(map(interval, newton['s0_to_s2d_minus2'])))
        q, rec, num, formal, residuals, iresiduals = formal_log_derivative(n, 2*n-2)
        verify(key+'_all_formal_inverse_identities', not any(iresiduals))
        verify(key+'_all_log_derivative_coefficient_identities', not any(residuals))
        # Independently check the original recurrence as a formal identity too.
        formal_residuals = []
        for k in range(1, 2*n-1):
            residual = dict(formal[k])
            for j in range(1, k if k <= n else n+1):
                residual = formal_add(residual, formal_mul(q[j], formal[k-j]))
            if k <= n:
                residual = formal_add(residual, q[k], k)
            formal_residuals.append(residual)
        verify(key+'_all_formal_Newton_identities_both_cases', not any(formal_residuals))
        alternate = [formal_evaluate(p, c) for p in formal]
        comparisons = [{'k': k, 'alternate_contains_replay': contains(a, b),
                        'replay_contains_alternate': contains(b, a),
                        'intersection_nonempty': max(a[0], b[0]) <= min(a[1], b[1])}
                       for k, (a, b) in enumerate(zip(alternate, sums))]
        verify(key+'_both_reconstructions_compatible', all(row['intersection_nonempty'] for row in comparisons))
        # Compatibility is supplementary only: original endpoints were checked in full above.
        verify(key+'_all_interval_orders', all(a[0] <= a[1] for a in enclosed+c+sums+alternate))
        matrix = [[sums[i+j] for j in range(n)] for i in range(n)]
        alt_matrix = [[alternate[i+j] for j in range(n)] for i in range(n)]
        same(key+'_every_H_entry', matrix, [[interval(a) for a in row] for row in newton['H']])
        verify(key+'_H_dimensions_and_symmetry', len(matrix) == n and all(len(row) == n for row in matrix)
               and all(matrix[i][j] == matrix[j][i] for i in range(n) for j in range(n)))
        matrices[n], alternate_matrices[n] = matrix, alt_matrix
        data['degrees'][key] = {'weights': list(map(str, weights)),
            'Jensen': list(map(encode_poly, jensen)), 'monomial': list(map(encode_poly, monomial)),
            'coefficient_intervals': list(map(encode_iv, enclosed)), 'actual_degree': n,
            'leading_reciprocal': encode_iv(lead_inv), 'monic': list(map(encode_iv, c)),
            'replay_moments': list(map(encode_iv, sums)), 'cases': cases,
            'formal_Q': list(map(encode_formal, q)), 'formal_inverse': list(map(encode_formal, rec)),
            'formal_nQ_minus_zQprime': list(map(encode_formal, num)),
            'formal_log_derivative': list(map(encode_formal, formal)),
            'formal_inverse_residuals': list(map(encode_formal, iresiduals)),
            'formal_defining_residuals': list(map(encode_formal, residuals)),
            'formal_Newton_residuals': list(map(encode_formal, formal_residuals)),
            'alternate_moments': list(map(encode_iv, alternate)), 'enclosure_comparisons': comparisons,
            'H': [[encode_iv(a) for a in row] for row in matrix]}
        same(key+'_all_compact_moments', list(map(lambda a: encode_iv(outward(a, 6)), sums)),
             claimed['compact_evidence']['moments_outer'][key])
        save('RECONSTRUCTION_N'+key+'_SAVED')
    pad = [[matrices[6][i][j] if max(i, j) < 6 else ZERO for j in range(7)] for i in range(7)]
    diff = [[minus(matrices[7][i][j], pad[i][j]) for j in range(7)] for i in range(7)]
    alt_pad = [[alternate_matrices[6][i][j] if max(i, j) < 6 else ZERO for j in range(7)] for i in range(7)]
    alt_diff = [[minus(alternate_matrices[7][i][j], alt_pad[i][j]) for j in range(7)] for i in range(7)]
    minor = [row[:3] for row in diff[:3]]
    for label, actual, key in [('padding', pad, 'padded_H6'), ('D6', diff, 'D6'), ('minor', minor, 'fixed_minor')]:
        same('all_'+label+'_entries', actual, [[interval(a) for a in row] for row in claimed[key]])
        verify(label+'_dimensions_symmetry', len(actual) == (3 if label == 'minor' else 7)
               and all(len(row) == len(actual) for row in actual)
               and all(actual[i][j] == actual[j][i] for i in range(len(actual)) for j in range(len(actual))))
    same('indices_unchanged', claimed['selected_indices'], [0, 1, 2])
    same('D00_one', diff[0][0], ONE)
    raw_terms, determinant = products(minor)
    same('all_six_raw_products_complete', raw_terms, claimed['determinant']['six_permutation_products'])
    same('full_raw_determinant_endpoints', determinant, interval(claimed['determinant']['full_interval']))
    tight = outward(determinant, 6)
    same('tight_outer_endpoints', tight, interval(claimed['determinant']['outer_interval']))
    same('tight_lemma_bound', tight, (-R('348399239655.059699'), -R('348399239655.059698')))
    verify('tight_contains_raw', contains(tight, determinant))
    verify('raw_strict_sign', determinant[1] < 0 and claimed['determinant']['excludes_zero'])
    coarse = [[outward(a, 6) for a in row] for row in minor]
    witness = claimed['compact_evidence']
    same('entire_coarse_table', [[encode_iv(a) for a in row] for row in coarse], witness['minor_outer'])
    b, c, d, e = [(R(lo), R(hi)) for lo, hi in
                  [('87.125396', '87.125397'), ('-4307.805192', '-4307.805191'),
                   ('742928.520301', '742928.520302'), ('-57256421.023079', '-57256421.023078')]]
    same('entire_lemma_table', coarse, [[ONE, b, c], [b, c, d], [c, d, e]])
    coarse_terms, coarse_det = products(coarse)
    compact_terms = [{k: v for k, v in term.items() if k != 'unsigned_product'} for term in coarse_terms]
    same('all_six_coarse_products_complete', compact_terms, witness['six_signed_products'])
    same('coarse_sum_complete', coarse_det, interval(witness['determinant_interval']))
    same('coarse_outer_complete', outward(coarse_det, 0), interval(witness['determinant_outer']))
    same('coarse_lemma_exact_sum', coarse_det,
         (-R(348399246479522365753352756777, 10**18), -R(348399229857130669120730436873, 10**18)))
    verify('each_table_entry_contains_raw', all(contains(coarse[i][j], minor[i][j]) for i in range(3) for j in range(3)))
    verify('all_six_coarse_products_contain_raw', all(contains(interval(a['signed_product']), interval(b['signed_product']))
           for a, b in zip(coarse_terms, raw_terms)))
    verify('coarse_sum_contains_full_raw', contains(coarse_det, determinant))
    verify('strict_integer_sign_comparison', coarse_det[1].numerator < -348399000000*coarse_det[1].denominator
           and witness['upper_less_than_minus_348399000000'] and witness['excludes_zero'])
    alt_terms, alt_det = products([row[:3] for row in alt_diff[:3]])
    data['matrices'] = {'padding': [[encode_iv(a) for a in row] for row in pad],
        'D6': [[encode_iv(a) for a in row] for row in diff],
        'alternate_D6': [[encode_iv(a) for a in row] for row in alt_diff],
        'minor': [[encode_iv(a) for a in row] for row in minor]}
    data['determinant'] = {'all_raw_products': raw_terms, 'full_raw': encode_iv(determinant),
        'tight': encode_iv(tight), 'alternate_products': alt_terms, 'alternate_full': encode_iv(alt_det),
        'alternate_outer': encode_iv(outward(alt_det, 6)),
        'alternate_contains_replay': contains(alt_det, determinant),
        'replay_contains_alternate': contains(determinant, alt_det)}
    data['compact_witness'] = {'minor': [[encode_iv(a) for a in row] for row in coarse],
        'six_signed_products': compact_terms, 'sum': encode_iv(coarse_det),
        'strict_sign_threshold': '-348399000000',
        'positive_threshold_gap': str(-348399000000-coarse_det[1])}
    data['required'] = 'Every saved endpoint/identity/witness matches; determinant upper<0'
    data['result'] = 'AUDITED rank(D6)>=3 at this fixed pair only' if all(data['checks'].values()) else 'AUDIT FAILED; preserve mismatches'
    save('COMPLETE')
    print(json.dumps({'status': data['status'], 'checks_passed': sum(data['checks'].values()),
        'checks_total': len(data['checks']), 'actual_degrees': [6, 7],
        'tight_bound': encode_iv(tight), 'alternate_outer': encode_iv(outward(alt_det, 6)),
        'required': data['required'], 'failures': data['failures'], 'result': data['result'], 'certificate': str(OUT)}))
    if data['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        data['exception'] = type(exc).__name__+': '+str(exc)
        verify('exception_free', False)
        save('ERROR')
        print(json.dumps({'status': 'ERROR', 'failures': data['failures'], 'exception': data['exception'], 'certificate': str(OUT)}))
        raise
