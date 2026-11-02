#!/usr/bin/env python3
"""Independent exact algebra for the L634 conceptual audit.

No notebook calculation module is imported. The six-subset calculation
constructs each entire homogeneous numerator and divides by the full
Vandermonde, rather than extracting selected alternant coefficients.
The infinite-row proof is audited in L634; this checks only finite algebra.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import factorial
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'normalized_row_margin_certificate.json'
OUT = HERE / 'normalized_row_margin_audit_certificate.json'
ZERO = (0, 0, 0, 0)
YSTAR = (F(1, 2), F(1, 2), F(-1, 2), F(-1, 2))


def accumulate(p, nu, value):
    p[nu] = p.get(nu, F(0)) + value
    if not p[nu]:
        del p[nu]


def multiply(p, q):
    out = {}
    for nu, c in p.items():
        for mu, d in q.items():
            accumulate(out, tuple(a+b for a, b in zip(nu, mu)), c*d)
    return out


def difference(i, j):
    a, b = list(ZERO), list(ZERO)
    a[i], b[j] = 1, 1
    return {tuple(a): F(1), tuple(b): F(-1)}


def divide(p, q):
    work, result = dict(p), {}
    lead = max(q)
    while work:
        top = max(work)
        degree = tuple(a-b for a, b in zip(top, lead))
        if min(degree) < 0:
            raise ArithmeticError('Nonzero polynomial remainder')
        c = work[top]/q[lead]
        accumulate(result, degree, c)
        for nu, value in q.items():
            accumulate(work, tuple(a+b for a, b in zip(nu, degree)), -c*value)
    if multiply(result, q) != p:
        raise ArithmeticError('Polynomial division replay failed')
    return result


def indices(total):
    for a in range(total+1):
        for b in range(total-a+1):
            for c in range(total-a-b+1):
                yield (a, b, c, total-a-b-c)


def differentiated_value(p, nu):
    answer = F(0)
    for power, value in p.items():
        if any(a < b for a, b in zip(power, nu)):
            continue
        term = value
        for a, b, y in zip(power, nu, YSTAR):
            term *= factorial(a)//factorial(a-b)
            term *= y**(a-b)
        answer += term
    return answer


def orbit(nu):
    return sorted(set(product(*((nu[:2], nu[1::-1]), (nu[2:], nu[:1:-1])))))


def main():
    source_bytes = SOURCE.read_bytes()
    previous = json.loads(source_bytes)
    kernel = {}
    for exponents, scale in (((7, 2, 1, 0), F(-1, 2)),
                             ((6, 3, 1, 0), F(-7, 6)),
                             ((5, 3, 2, 0), F(7, 2)),
                             ((4, 3, 2, 1), F(35, 2))):
        for perm in permutations(range(4)):
            sign = (-1)**sum(perm[i] > perm[j] for i in range(4) for j in range(i+1, 4))
            accumulate(kernel, tuple(exponents[j] for j in perm), scale*sign)
    h = {}
    for power, value in kernel.items():
        if power[1] and power[3]:
            nu = (power[0], power[1]-1, power[2], power[3]-1)
            accumulate(h, nu, value*power[1]*power[3])

    delta = {ZERO: F(1)}
    for i, j in combinations(range(4), 2):
        delta = multiply(delta, difference(i, j))
    subsets = []
    for chosen in combinations(range(4), 2):
        other = tuple(i for i in range(4) if i not in chosen)
        cross = {ZERO: F(1)}
        for i in chosen:
            for j in other:
                cross = multiply(cross, difference(i, j))
        prefactor = divide(delta, cross)
        exponentials = []
        for r in range(9):
            exponential = {}
            for nu in indices(r):
                value = F(1)
                for j, power in enumerate(nu):
                    value *= (F(1, 2) if j in chosen else F(-1, 2))**power/factorial(power)
                exponential[nu] = value
            exponentials.append(exponential)
        subsets.append((chosen, other, prefactor, exponentials))

    old_derivatives = {tuple(r['nu']): r for r in previous['all_signed_derivative_orbits']}
    old_comparisons = {tuple(r['nu']): r for r in previous['six_subset_comparison']}
    rows, divisions, maxima = [], [], [F(0)]*9
    for degree in range(9):
        for nu in indices(degree):
            members = sorted({left+right for left, right in orbit(nu)})
            values = [(-1)**sum(mu[2:])*differentiated_value(h, mu) for mu in members]
            average = sum(values, F(0))/len(members)
            maxima[degree] = max(maxima[degree], abs(average))
            old = old_derivatives[nu]
            agreement = (old['degree'] == degree and old['orbit'] == [list(mu) for mu in members]
                         and list(map(F, old['signed_derivatives'])) == values
                         and F(old['average']) == average)
            rows.append({'nu': list(nu), 'signed_derivatives': list(map(str, values)),
                         'average': str(average), 'old_entry_matches': agreement})
            if nu[0] < nu[1] or nu[2] < nu[3]:
                continue
            numerator = {}
            for chosen, other, prefactor, exponentials in subsets:
                arithmetic = {}
                for left in set((nu[:2], nu[1::-1])):
                    for right in set((nu[2:], nu[:1:-1])):
                        power = [0]*4
                        for i, k in zip(chosen+other, left+right):
                            power[i] = k
                        accumulate(arithmetic, tuple(power), F((-1)**sum(right)))
                term = multiply(multiply(prefactor, arithmetic), exponentials[8-degree])
                for power, value in term.items():
                    accumulate(numerator, power, value)
            quotient = divide(numerator, delta)
            weight = 5040*(-2*quotient.get((2, 0, 1, 1), F(0))
                           + quotient.get((1, 1, 1, 1), F(0)))
            old = old_comparisons[nu]
            expected_weight = average*len(members)
            divisions.append({'nu': list(nu), 'quotient': [
                {'nu': list(power), 'coefficient': str(value)} for power, value in sorted(quotient.items())],
                'six_subset_weight': str(weight), 'spectral_orbit_sum': str(expected_weight),
                'difference': str(weight-expected_weight),
                'old_entry_matches': (F(old['six_subset_weight']) == weight
                                      and F(old['orbit_sum']) == expected_weight
                                      and F(old['difference']) == weight-expected_weight)})

    # Independent truncated exponential by sum b(u)^j/j!, not the prior recurrence.
    b = [F(0)] + [F(4, factorial(k)) + (2 if k == 1 else 0) for k in range(1, 9)]
    power, majorant = [F(1)]+[F(0)]*8, [F(1)]+[F(0)]*8
    for j in range(1, 9):
        power = [sum((power[i]*b[k-i] for i in range(k+1)), F(0)) for k in range(9)]
        majorant = [a+c/factorial(j) for a, c in zip(majorant, power)]
    costs = [maxima[k]*majorant[k]/100**k for k in range(1, 9)]
    total = sum(costs, F(0))
    reflected = {(nu[2], nu[3], nu[0], nu[1]): (-1)**sum(nu)*value for nu, value in h.items()}
    old_h = {tuple(r['nu']): F(r['coefficient']) for r in previous['spectral_polynomial']}
    checks = {
        'homogeneous_degree_eight': all(sum(nu) == 8 for nu in h),
        'normalization_one': differentiated_value(h, ZERO) == 1,
        'pair_exchange_reflection': reflected == h,
        'whole_H_matches': h == old_h,
        'all_495_derivatives_match': len(rows) == 495 and all(r['old_entry_matches'] for r in rows),
        'all_175_full_polynomial_divisions': len(divisions) == 175,
        'all_175_weights_match_spectral_formula': all(F(r['difference']) == 0 for r in divisions),
        'all_175_previous_entries_match': all(r['old_entry_matches'] for r in divisions),
        'degree_maxima_match': maxima == list(map(F, previous['degreewise_maxima'])),
        'exponential_coefficients_match': majorant == list(map(F, previous['majorant']['coefficients'])),
        'degree_costs_match': costs == list(map(F, previous['contraction']['degree_costs'])),
        'exact_total_matches': total == F(previous['contraction']['total_exact']),
        'strictly_below_three_tenths': total < F(3, 10),
        'strictly_below_one_half': total < F(1, 2),
    }
    failures = [key for key, value in checks.items() if not value]
    report = {
        'scope': 'Independent finite algebra audit for L634; not an infinite-row, source or RH certificate.',
        'source_sha256': hashlib.sha256(source_bytes).hexdigest(),
        'method': 'Full six-subset homogeneous polynomials divided exactly by the Vandermonde; no notebook imports.',
        'derivatives': rows, 'six_subset_full_divisions': divisions,
        'degreewise_maxima': list(map(str, maxima)), 'majorant_coefficients': list(map(str, majorant)),
        'contraction': {'degree_costs': list(map(str, costs)), 'total': str(total),
                        'eventual_bound': '3/10', 'required_threshold': '1/2',
                        'slack_to_eventual_bound': str(F(3, 10)-total)},
        'checks': checks, 'failures': failures,
    }
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print(f'Independent derivative entries: {len(rows)}; complete six-subset divisions: {len(divisions)}')
    print(f'Exact row cost: {total}; eventual bound 3/10; required <1/2')
    print(f'Failures: {failures}; certificate: {OUT.relative_to(HERE.parents[1])}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
