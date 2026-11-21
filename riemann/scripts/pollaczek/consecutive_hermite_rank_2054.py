#!/usr/bin/env python3
"""One approved N=6,7 Newton-Hermite zero-padding minor; exact rationals.

No helper imports, roots, floating arithmetic, precision or minor sweep.
Exact coefficient encoding: [X-degree, sqrt(2)-degree, rational value].
"""
from fractions import Fraction as F
from itertools import permutations
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import sys

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).parent
OUT = ROOT / 'consecutive-hermite-rank-2054.json'
TARGET = "Test rank(D_6)<=2 for D_6=H_7-diag(H_6,0) of C029m's full Jensen-weighted family by certifying the fixed principal minor on monomial indices 0,1,2 with unchanged C029n constants."
INDICES = (0, 1, 2)  # Fixed before loading any coefficients or intervals.
checks = {}
record = {'target': TARGET, 'status': 'STARTED', 'selected_indices': INDICES,
          'checks': checks, 'classification': 'POTENTIALLY_NEW; no originality claim',
          'encoding': 'Sparse Q[X,s]/(s^2-2), X=pi, s=positive sqrt(2)',
          'normalization': 'U_N=T_N/S, same positive S=sin(pi/8)/sqrt(2)',
          'precision_policy': 'Original 60-place constant intervals; no refinement; exact Fraction operations'}


def check(name, condition):
    checks[name] = bool(condition)


def save(stage):
    record['status'] = stage
    record['failures'] = [k for k, v in checks.items() if not v]
    OUT.write_text(json.dumps(record, indent=2) + '\n')
    if record['failures']:
        print(json.dumps({'status': stage, 'failures': record['failures'],
                          'certificate': str(OUT)}))
        raise SystemExit(1)


def add(*polys):
    out = {}
    for p in polys:
        for key, v in p.items():
            out[key] = out.get(key, F(0)) + v
    return {key: v for key, v in out.items() if v}


def scale(p, c):
    return {key: c*v for key, v in p.items() if c*v}


def encode(p):
    return [[i, j, str(v)] for (i, j), v in sorted(p.items())]


def decode(p):
    return {(i, j): F(row[key]) for i, row in enumerate(p)
            for j, key in enumerate(('rational', 'sqrt2')) if F(row[key])}


def iv(row):
    return F(row['lower']), F(row['upper'])


def ij(a):
    return {'lower': str(a[0]), 'upper': str(a[1])}


def ia(*args):
    return sum((a[0] for a in args), F(0)), sum((a[1] for a in args), F(0))


def isc(a, c):
    return min(c*a[0], c*a[1]), max(c*a[0], c*a[1])


def im(a, b):
    vals = [v*w for v in a for w in b]
    return min(vals), max(vals)


def reciprocal(a):
    if not (a[1] < 0 or a[0] > 0):
        raise ArithmeticError('denominator interval contains zero')
    return 1/a[1], 1/a[0]


def enclose(p, x, s):
    out = F(0), F(0)
    for i in range(max((key[0] for key in p), default=0), -1, -1):
        a, b = p.get((i, 0), F(0)), p.get((i, 1), F(0))
        out = ia(im(out, x), ia((a, a), isc(s, b)))
    return out


def grid(a, digits):
    unit = 10**digits
    lo = (a[0]*unit).numerator // (a[0]*unit).denominator
    hi = -((-a[1]*unit).numerator // (-a[1]*unit).denominator)
    out = F(lo, unit), F(hi, unit)
    assert out[0] <= a[0] <= a[1] <= out[1]
    return out


def main():
    names = ('tilted-boundary-metric-2010.json',
             'tilted-affine-quotient-residual-2022.json')
    raw = {name: (ROOT/name).read_bytes() for name in names}
    record['input_sha256'] = {name: hashlib.sha256(data).hexdigest()
                              for name, data in raw.items()}
    record['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    source, prior = [json.loads(raw[name]) for name in names]
    check('C029n_pinned', record['input_sha256'][names[0]] ==
          '361e31b72ad348b17f6c2ac785c20f5ab73e27796025bd724af208543e0feaf7')
    check('C029q_pins_C029n', prior['input_sha256'][names[0]] == record['input_sha256'][names[0]])
    check('prior_checks', all(source['checks'].values()) and source['failures'] == []
          and all(prior['checks'].values()) and prior['failures'] == []
          and prior['incomplete_certification'] == [])
    x, s = iv(source['pi_interval']), iv(source['sqrt2_interval'])
    record['pi_interval'], record['sqrt2_interval'] = ij(x), ij(s)
    check('unchanged_constants', prior['pi_interval'] == source['pi_interval']
          and prior['sqrt2_interval'] == source['sqrt2_interval'])
    check('sqrt2_squared_endpoints', 0 < s[0] and s[0]**2 < 2 < s[1]**2)
    atan = []
    for d, key in ((5, 'atan5'), (239, 'atan239')):
        terms = [F((-1)**j, (2*j+1)*d**(2*j+1)) for j in range(48)]
        partial, error = sum(terms, F(0)), F(1, 97*d**97)
        stored = source[key]
        check(key+'_full_evidence', stored['term_count'] == 48
              and F(stored['argument']) == F(1, d)
              and list(map(F, stored['terms'])) == terms
              and F(stored['partial_sum']) == partial
              and F(stored['positive_remainder_upper']) == error)
        atan.append((partial, partial+error))
    machin = ia(isc(atan[0], 16), isc(atan[1], -4))
    record['machin_interval'] = ij(machin)
    record['constant_proof'] = 'C029n Machin branch/integral proof; exact finite arithmetic replay here'
    check('machin_containment', machin == iv(source['pi_machin_interval'])
          and x[0] <= machin[0] <= machin[1] <= x[1])
    bern = [F(1)]
    for j in range(1, 21):
        bern.append(-sum((comb(j+1, k)*bern[k] for k in range(j)), F(0))/(j+1))
    check('B0_to_B20', bern == list(map(F, prior['bernoulli_0_to_20']))
          and bern[20] == F(-174611, 330))
    phase = ((1, 0), (1, 1), (-1, 0), (-1, -1))
    v = []
    for n in range(10):
        poly = {}
        for h in range(n+1):
            a, b = phase[(n-h) % 4]
            factor = -F(factorial(n)*4**h*(4**(h+1)-1)*2**(h+1),
                        factorial(n-h)*factorial(2*h+2))*bern[2*h+2]
            poly = add(poly, {(h+1, 0): factor*a, (h+1, 1): factor*b})
        v.append(poly)
    beta = [add(scale(v[k], 8*k*k+12*k+7),
                scale(v[k+2], (2*k+3)*(2*k+5)),
                scale(v[k-2], 4*k*(k-1)) if k >= 2 else {}) for k in range(8)]
    check('all_v_beta_match_C029q', v == list(map(decode, prior['u_over_S_polynomials']))
          and beta == list(map(decode, prior['beta_over_S_polynomials'])))
    check('all_v_beta_match_C029n', v[:9] == list(map(decode, source['u_over_S_polynomials']))
          and beta[:7] == list(map(decode, source['beta_over_S_polynomials'])))
    p = [[F(1)]]
    for k in range(7):
        row = [F(0)] + p[k]
        if k:
            for i, a in enumerate(p[k-1]):
                row[i] -= F(2*k+1, 2)*a
        p.append([a/(k+1) for a in row])
    check('basis_matches_C029q', p == [list(map(F, row)) for row in prior['basis_p_0_to_7']])
    check('basis_degrees', all(len(p[k]) == k+1 and p[k][k] == F(1, factorial(k))
                               for k in range(8)))
    record.update({'bernoulli_0_to_20': list(map(str, bern)),
                   'v_0_to_9': list(map(encode, v)), 'beta_over_S_0_to_7': list(map(encode, beta)),
                   'basis_p_0_to_7': [list(map(str, row)) for row in p]})
    polynomials, coefficient_intervals = {}, {}
    record['polynomials'] = {}
    for n in (6, 7):
        weights = [F(factorial(n), factorial(n-k)*n**k) for k in range(n+1)]
        a = [scale(beta[k], weights[k]) for k in range(n+1)]
        b = [add(*(scale(a[k], p[k][i]) for k in range(i, n+1))) for i in range(n+1)]
        check(f'N{n}_all_exact_coefficients', weights == list(map(F, prior['weights'][str(n)]))
              and a == list(map(decode, prior['Jensen_coefficients'][str(n)]))
              and b == list(map(decode, prior['U_monomial_coefficients'][str(n)])))
        intervals = [enclose(coef, x, s) for coef in b]
        leading = intervals[n]
        check(f'N{n}_actual_degree', leading[1] < 0 if n == 6 else leading[0] > 0)
        check(f'N{n}_leading_matches_C029q', leading == iv(prior['leading_coefficient_intervals'][str(n)]))
        polynomials[n], coefficient_intervals[n] = b, intervals
        record['polynomials'][str(n)] = {'weights': list(map(str, weights)),
            'Jensen_coefficients': list(map(encode, a)), 'monomial_coefficients': list(map(encode, b)),
            'coefficient_intervals': list(map(ij, intervals)), 'actual_degree': n,
            'leading_interval': ij(leading), 'leading_outer': ij(grid(leading, 12))}
    save('COEFFICIENTS_AND_FIXED_INDICES_SAVED')

    # Cited Newton identities; c[j] is coefficient of t^(n-j) after monic normalization.
    moments, H = {}, {}
    record['Newton'] = {}
    for n in (6, 7):
        b = coefficient_intervals[n]
        inverse = reciprocal(b[n])
        c = [(F(1), F(1))] + [im(b[n-j], inverse) for j in range(1, n+1)]
        sums = [(F(n), F(n))]
        cases = []
        for k in range(1, 2*n-1):
            if k <= n:
                value = ia(*(im(c[j], sums[k-j]) for j in range(1, k)), isc(c[k], k))
                cases.append('k<=degree: k*c_k, no c_k*s_0 term')
            else:
                value = ia(*(im(c[j], sums[k-j]) for j in range(1, n+1)))
                cases.append('k>degree: all degree terms, no k*c_k term')
            sums.append(isc(value, -1))
        matrix = [[sums[i+j] for j in range(n)] for i in range(n)]
        moments[n], H[n] = sums, matrix
        check(f'N{n}_moment_count_and_multiplicity', len(sums) == 2*n-1 and sums[0] == (F(n), F(n)))
        check(f'N{n}_all_intervals_ordered', all(lo <= hi for lo, hi in sums+c))
        record['Newton'][str(n)] = {'leading_reciprocal': ij(inverse),
            'monic_coefficients_c0_to_cd': list(map(ij, c)), 'cases_k1_onward': cases,
            's0_to_s2d_minus2': list(map(ij, sums)),
            'H': [[ij(val) for val in row] for row in matrix]}
        save(f'MOMENTS_N{n}_SAVED')
    padded = [[H[6][i][j] if i < 6 and j < 6 else (F(0), F(0))
               for j in range(7)] for i in range(7)]
    difference = [[ia(H[7][i][j], isc(padded[i][j], -1)) for j in range(7)] for i in range(7)]
    minor = [[difference[i][j] for j in INDICES] for i in INDICES]
    check('D00_exactly_one', difference[0][0] == (F(1), F(1)))
    record['padded_H6'] = [[ij(val) for val in row] for row in padded]
    record['D6'] = [[ij(val) for val in row] for row in difference]
    record['fixed_minor'] = [[ij(val) for val in row] for row in minor]
    save('FULL_MATRICES_SAVED_BEFORE_DETERMINANT')

    terms, products = [], []
    for perm in permutations(range(3)):
        inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i+1, 3))
        sign = (-1)**inversions
        value = (F(1), F(1))
        for i in range(3):
            value = im(value, minor[i][perm[i]])
        signed = isc(value, sign)
        terms.append({'permutation': perm, 'sign': sign, 'unsigned_product': ij(value),
                      'signed_product': ij(signed)})
        products.append(signed)
    determinant = ia(*products)
    outer = grid(determinant, 6)
    separated = determinant[1] < 0 or determinant[0] > 0
    record['determinant'] = {'six_permutation_products': terms,
        'full_interval': ij(determinant), 'outer_interval': ij(outer),
        'required': 'lower>0 or upper<0', 'excludes_zero': separated}
    record['result'] = ('rank(D6)>=3; prescribed rank<=2 ansatz rejected at this pair only'
                        if separated else 'INCONCLUSIVE: no upper rank bound; stop without escalation')
    check('six_signed_terms', len(terms) == 6 and sum(t['sign'] == 1 for t in terms) == 3)
    # A short independently usable interval witness; outward coarsening only.
    # No source precision or selected minor changes. Retain every rational product.
    short_minor = [[grid(val, 6) for val in row] for row in minor]
    short_terms, short_products = [], []
    for perm in permutations(range(3)):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(3) for j in range(i+1, 3))
        value = (F(1), F(1))
        for i in range(3):
            value = im(value, short_minor[i][perm[i]])
        signed = isc(value, sign)
        short_products.append(signed)
        short_terms.append({'permutation': perm, 'sign': sign, 'signed_product': ij(signed)})
    short_det = ia(*short_products)
    check('short_minor_contains_full', all(short_minor[i][j][0] <= minor[i][j][0]
          <= minor[i][j][1] <= short_minor[i][j][1] for i in range(3) for j in range(3)))
    check('short_determinant_contains_full', short_det[0] <= determinant[0]
          <= determinant[1] <= short_det[1])
    check('short_witness_sign_agrees', not separated or
          (short_det[1] < 0 if determinant[1] < 0 else short_det[0] > 0))
    record['compact_evidence'] = {
        'rounding': 'Exact outward rounding to 10^(-6), after full calculation; not refined input constants',
        'moments_outer': {str(n): [ij(grid(val, 6)) for val in moments[n]] for n in (6, 7)},
        'minor_outer': [[ij(val) for val in row] for row in short_minor],
        'six_signed_products': short_terms, 'determinant_interval': ij(short_det),
        'determinant_outer': ij(grid(short_det, 0)),
        'upper_less_than_minus_348399000000': short_det[1] < -348399000000,
        'excludes_zero': short_det[1] < 0 or short_det[0] > 0}
    # Zero containment is a permitted inconclusive outcome, never a fabricated failure or upper bound.
    save('COMPLETE')
    print(json.dumps({'status': record['status'], 'actual_degrees': [6, 7],
        'leading_outer_bounds': {str(n): record['polynomials'][str(n)]['leading_outer'] for n in (6, 7)},
        'fixed_indices': INDICES, 'determinant_outer': ij(outer), 'required': 'exclude zero',
        'excludes_zero': separated, 'result': record['result'], 'failures': record['failures'],
        'checks_passed': sum(checks.values()), 'certificate': str(OUT)}))


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        record['exception'] = f'{type(exc).__name__}: {exc}'
        check('exception_free', False)
        save('ERROR')
