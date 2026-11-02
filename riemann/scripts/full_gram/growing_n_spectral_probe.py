#!/usr/bin/env python3
"""Exploratory full-tail spectral extraction; floating output is not a proof.

The geometric denominator is contracted by moments through degree eight,
never by a tail cutoff. Outputs include complete finite matrices, local
normalization diagnostics, and the tested coefficient directions.
Run from riemann: PYTHONDONTWRITEBYTECODE=1 python3 scripts/full_gram/growing_n_spectral_probe.py
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial, gcd, log, sqrt
from pathlib import Path
import json
import numpy as np

from signed_germ import add, alternant, partitions, signed_from_polynomial, divide_exact, mul, DELTA
from spectral_lift_n2 import derivative, evaluate, YSTAR, SIGNS

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'scripts/full_gram/growing_n_spectral_probe_certificate.json'


def spectral_kernel():
    kernel = {}
    for partition in partitions(4):
        lam = partition+(0,)*(4-len(partition))
        powers = tuple(lam[i]+3-i for i in range(4))
        alt = alternant(powers)
        schur = divide_exact(alt, DELTA)
        den = 1
        for e in powers:
            den *= factorial(e)
        c = F(5040)*signed_from_polynomial(schur, 4)/den
        for nu, value in alt.items():
            add(kernel, nu, c*value)
    return derivative(kernel, (0, 1, 0, 1))


def directional_derivative(poly):
    out = {}
    for i in range(4):
        nu = tuple(int(i == j) for j in range(4))
        for powers, c in derivative(poly, nu).items():
            add(out, powers, -SIGNS[i]*c)
    return out


H = spectral_kernel()
DERIVATIVES = [H]
for _ in range(8):
    DERIVATIVES.append(directional_derivative(DERIVATIVES[-1]))


@lru_cache(None)
def factors(n):
    out = []
    p = 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            out.append((p, e))
        p += 1
    if n > 1:
        out.append((n, 1))
    return tuple(out)


def local_numerator(p, e):
    # R_e numerator: sigma_e - x ab(c+d)sigma_(e-1)
    #                         + x^2 a^2 b^2 cd sigma_(e-2).
    # All exponent vectors are for (alpha,beta,gamma,delta).
    assert e >= 1
    terms = {}
    for k in range(e+1):
        add(terms, (k, e-k, 0, 0), F(1))
    for k in range(e):
        for side in (2, 3):
            v = [k+1, e-k, 0, 0]
            v[side] = 1
            add(terms, tuple(v), -F(1, p))
    for k in range(e-1):
        add(terms, (k+2, e-k, 1, 1), F(1, p*p))
    return terms


def geometric_moments(p):
    # Normalized geometric law, P(J=j)=(1-x)x^j, x=p^-2.
    x = F(1, p*p)
    moments = [F(1)]
    for k in range(1, 9):
        moments.append(x/(1-x)*sum((comb(k, r)*moments[r] for r in range(k)), F(0)))
    return moments


def summed_tail_moments(primes, L):
    result = np.zeros(9)
    result[0] = 1.0
    normalization = 1.0
    for p in primes:
        gm = geometric_moments(p)
        scale = log(p)/L
        local = np.array([float(gm[k])*scale**k for k in range(9)])
        result = np.array([sum(comb(k, j)*result[k-j]*local[j] for j in range(k+1)) for k in range(9)])
        normalization /= 1-1/(p*p)
    return result, normalization


def evaluate_many(poly, points):
    result = np.zeros(len(points))
    for nu, c in poly.items():
        term = np.full(len(points), float(c))
        for i, e in enumerate(nu):
            if e:
                term *= points[:, i]**e
        result += term
    return result


@lru_cache(None)
def arithmetic_entry(h, k, L):
    if h == k == 1:
        return 1.0, 1.0, 1, 0.0
    assert gcd(h, k) == 1
    # If the first coefficient index has p^e, the second divisor pair
    # gets the increased exponent, and conversely.
    entries = [(p, e, True) for p, e in factors(h)]
    entries += [(p, e, False) for p, e in factors(k)]
    shifts = [np.zeros(4)]
    coefficients = [1.0]
    gram = 1.0
    for p, e, swap in entries:
        terms = local_numerator(p, e)
        local = [(nu[2:]+nu[:2] if swap else nu, float(c)) for nu, c in terms.items()]
        scale = log(p)/L
        shifts, coefficients = (
            [old+scale*np.array(nu) for old in shifts for nu, _ in local],
            [old*c for old in coefficients for _, c in local],
        )
        gram *= p**(-e/2)*(1+e*(p-1)/(p+1))
    shifts = np.array(shifts)
    coefficients = np.array(coefficients)
    moments, normalizer = summed_tail_moments([p for p, _, _ in entries], L)
    points = np.array(list(map(float, YSTAR)))-shifts*np.array(SIGNS)
    values = sum(moments[j]/factorial(j)*evaluate_many(DERIVATIVES[j], points) for j in range(9))
    value = normalizer*np.dot(coefficients, values)/sqrt(h*k)
    zero_shift = normalizer*np.sum(coefficients)/sqrt(h*k)
    return float(value), gram, len(coefficients), abs(zero_shift-gram)


def local_phi(p, e):
    t = 1/sqrt(p)
    C = (1-1/p)**3/(1+1/p)
    if e == 0:
        return {0: 1.0}
    if e == 1:
        s = (1-1/p)/(1+1/p)
        rho = 2*t/(1+1/p)
        return {0: -rho/s, 1: 1/s}
    return {e: 1/sqrt(C), e-1: -2*t/sqrt(C), e-2: t*t/sqrt(C)}


def gram_basis(N):
    basis = np.zeros((N, N))
    for n in range(1, N+1):
        expansion = {1: 1.0}
        for p, e in factors(n):
            expansion = {m*p**j: c*v for m, c in expansion.items() for j, v in local_phi(p, e).items()}
        for m, c in expansion.items():
            basis[m-1, n-1] = c
    return basis


def one_test(N):
    # Interior of the interval where floor(exp(L/100))=N, avoiding
    # floating ambiguities in an endpoint equality.
    L = 100*log(N+0.5)
    Q, G = np.zeros((N, N)), np.zeros((N, N))
    max_normalization_error = 0.0
    max_translation_count = 0
    for m in range(1, N+1):
        for n in range(m, N+1):
            g = gcd(m, n)
            if m == n:
                value, gram, count, err = 1.0, 1.0, 1, 0.0
            else:
                value, gram, count, err = arithmetic_entry(m//g, n//g, L)
            Q[m-1, n-1] = Q[n-1, m-1] = value
            G[m-1, n-1] = G[n-1, m-1] = gram
            max_normalization_error = max(max_normalization_error, err)
            max_translation_count = max(max_translation_count, count)
    basis = gram_basis(N)
    transformed = basis.T@Q@basis
    transformed = (transformed+transformed.T)/2
    gram_error = float(np.max(np.abs(basis.T@G@basis-np.eye(N))))
    eig, vectors = np.linalg.eigh(transformed)
    defect = transformed-np.eye(N)
    v = 1/np.sqrt(np.arange(1, N+1))
    weighted_rows = np.abs(defect)@v/v
    # The symmetric weighted quadratic estimate uses the same row
    # expression for this symmetric real matrix.
    y = vectors[:, 0]
    a = basis@y
    rayleigh = float(a@Q@a/(a@G@a))
    residual = float(np.linalg.norm(transformed@y-eig[0]*y))
    return {
        'N': N, 'L': L, 'log_N_over_L': log(N)/L,
        'required_lower_bound': 0.5,
        'minimum_generalized_eigenvalue_preview': float(eig[0]),
        'maximum_generalized_eigenvalue_preview': float(eig[-1]),
        'minimum_direction_rayleigh_preview': rayleigh,
        'maximum_weighted_absolute_row_preview': float(np.max(weighted_rows)),
        'row_bound_sufficient_threshold': 0.5,
        'worst_row_index': int(np.argmax(weighted_rows))+1,
        'normalization_error_float': max_normalization_error,
        'orthonormal_basis_error_float': gram_error,
        'minimum_eigenpair_residual_float': residual,
        'max_finite_numerator_translations': max_translation_count,
        'full_Q_matrix_float': Q.tolist(),
        'full_G_matrix_float': G.tolist(),
        'full_Gram_basis_matrix_float': basis.tolist(),
        'full_transformed_Q_matrix_float': transformed.tolist(),
        'all_weighted_absolute_rows_float': weighted_rows.tolist(),
        'minimum_eigenvector_Gram_basis_float': y.tolist(),
        'minimum_eigenvector_original_coefficients_float': a.tolist(),
        'all_generalized_eigenvalues_preview': eig.tolist(),
    }


def main():
    # Exact algebra diagnostics for the scalar polynomial and N=2.
    exact_checks = {
        'degree_eight': all(sum(nu) == 8 for nu in H),
        'constant_amplitude': evaluate(H, YSTAR) == 1,
        'pair_exchange_reflection_symmetry': {
            nu[2:]+nu[:2]: c*(-1)**sum(nu) for nu, c in H.items()} == H,
    }
    recurrence_rows = []
    for p in range(2, 65):
        if factors(p) != ((p, 1),):
            continue
        prev2 = {(0, 0, 0, 0): F(1), (1, 1, 1, 1): -F(1, p*p)}
        prev1 = local_numerator(p, 1)
        e, power = 1, p
        while power <= 64:
            formula = local_numerator(p, e)
            actual_zero = sum(formula.values(), F(0))
            required_zero = (1-F(1, p*p))*(1+F(e*(p-1), p+1))
            recurrence_rows.append({'p': p, 'e': e,
                                    'recurrence_match': formula == prev1,
                                    'zero_shift_numerator': str(actual_zero),
                                    'required_zero_shift_numerator': str(required_zero)})
            nxt = mul({(1, 0, 0, 0): F(1), (0, 1, 0, 0): F(1)}, prev1)
            for nu, c in mul({(1, 1, 0, 0): F(-1)}, prev2).items():
                add(nxt, nu, c)
            prev2, prev1 = prev1, nxt
            e, power = e+1, power*p
    exact_checks['all_used_prime_power_numerators'] = all(
        r['recurrence_match'] and r['zero_shift_numerator'] == r['required_zero_shift_numerator']
        for r in recurrence_rows)
    from spectral_lift_n2 import translation_extraction, LEFT, moments, EXPECTED
    n2, _ = translation_extraction(H, LEFT, moments(8))
    exact_checks['all_nine_n2_coefficients'] = tuple(n2) == EXPECTED
    records = [one_test(N) for N in (2, 4, 8, 16, 32, 64)]
    failures = [name for name, ok in exact_checks.items() if not ok]
    for row in records:
        if max(row['normalization_error_float'], row['orthonormal_basis_error_float'], row['minimum_eigenpair_residual_float']) > 1e-8:
            failures.append(f"N={row['N']} floating diagnostic tolerance exceeded")
    summary = [{k: row[k] for k in (
        'N', 'L', 'minimum_generalized_eigenvalue_preview',
        'maximum_generalized_eigenvalue_preview',
        'maximum_weighted_absolute_row_preview', 'worst_row_index',
        'orthonormal_basis_error_float', 'minimum_eigenpair_residual_float')}
        for row in records]
    certificate = {
        'status': 'EXPLORATORY FLOATING PREVIEW; NOT A CERTIFIED INEQUALITY',
        'target': 'Q_(N,L)>= (1/2+epsilon) Gamma uniformly in growing N and all complex a',
        'method': 'Vandermonde spectral polynomial; exact degree-eight geometric-moment identities with floating logarithms and matrix arithmetic; no arithmetic-tail cutoff',
        'spectral_polynomial_exact': [{'power': list(nu), 'coefficient': str(c)} for nu, c in sorted(H.items())],
        'normalized_geometric_moments_exact': {str(p): [str(x) for x in geometric_moments(p)] for p in range(2, 65) if factors(p) == ((p, 1),)},
        'n2_coefficients_exact': [str(x) for x in n2],
        'prime_power_recurrence_exact': recurrence_rows,
        'exact_checks': exact_checks,
        'summary': summary, 'tests': records, 'failures': failures,
        'required': {'all_coefficients': True, 'all_sufficiently_large_L': True, 'fixed_epsilon_positive': True},
        'unresolved': ['No interval enclosure of floating calculations.', 'Only N<=64 was tested.', 'No uniform Gram norm domination or epsilon was proved.', 'No coefficient obstruction to the actual inequality was found.', 'Input and source manuscript audits remain separate.'],
    }
    OUT.write_text(json.dumps(certificate, indent=2)+'\n')
    for row in summary:
        print(f"N={row['N']:2d}: min Q/Gamma preview={row['minimum_generalized_eigenvalue_preview']:.10f}; required >0.5 with a uniform reserve; weighted row preview={row['maximum_weighted_absolute_row_preview']:.10f}")
    print(f'Exact normalization/N=2 checks: {exact_checks}; failures: {failures}')
    print('Growing-N target: unresolved; previews are not proofs or uniform evidence.')
    print(f'Full certificate: {OUT.relative_to(ROOT)}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
