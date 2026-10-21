#!/usr/bin/env python3
"""Independent exact replay of L098's arithmetic, not integer elimination."""
import hashlib
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def remainder(a, b):
    a = list(map(F, a))
    while len(a) >= len(b) and a != [0]:
        k, c = len(a) - len(b), a[-1] / b[-1]
        for j, bj in enumerate(b):
            a[k+j] -= c * bj
        trim(a)
    return a


def resultant(a, b):
    a, b = list(map(F, a)), list(map(F, b))
    m, n = len(a)-1, len(b)-1
    if n == 0:
        return b[0]**m
    if m < n:
        return (-1)**(m*n) * resultant(b, a)
    r = remainder(a, b)
    if r == [0]:
        return F(0)
    return (-1)**(m*n) * b[-1]**(m-len(r)+1) * resultant(b, r)


def determinant(a):
    # Leibniz sum accumulated by column subsets; no elimination routine.
    n, states = len(a), {0: F(1)}
    for i in range(n):
        new = {}
        for mask, value in states.items():
            for j in range(n):
                if not (mask >> j) & 1:
                    sign = (-1)**((mask >> (j+1)).bit_count())
                    key = mask | (1 << j)
                    new[key] = new.get(key, F(0)) + sign*value*a[i][j]
        states = new
    return states[(1 << n)-1]


def main():
    source = Path(__file__).with_name('octic-cube-support-certificate.json')
    raw = source.read_bytes()
    old = json.loads(raw)
    q5 = [0]*11
    q4 = [0]*9
    for power, out in ((5, q5), (4, q4)):
        for c in range(power+1):
            for b in range(power-c+1):
                a = power-b-c
                out[b+2*c] += factorial(power)//(factorial(a)*factorial(b)*factorial(c))*3**c
    complement = [(1 if k == 0 else 0) - (q5[k] if k < 11 else 0)
                  + (5*q5[k-1] if 1 <= k <= 11 else 0) for k in range(12)]
    h = complement[3:]
    hp = [i*h[i] for i in range(1, 9)]
    res = resultant(h, hp)
    disc = res/h[-1]
    rq = resultant(h, [1, 1, 3])
    matrix = [[0]*i + h[::-1] + [0]*(6-i) for i in range(7)]
    matrix += [[0]*i + hp[::-1] + [0]*(7-i) for i in range(8)]
    mult = [[F(0) for _ in range(8)] for _ in range(8)]
    for i in range(7):
        mult[i+1][i] = F(1)
    for i in range(8):
        mult[i][7] = -F(h[i], h[-1])
    norm_tests = []
    for z in range(-4, 5):
        d = determinant([[F(z if i == j else 0)-mult[i][j]
                          for j in range(8)] for i in range(8)])
        expected = sum(F(c, h[-1])*z**i for i, c in enumerate(h))
        norm_tests.append({'z': z, 'determinant': str(d), 'h_over_b': str(expected),
                           'pass': d == expected})
    norms = [F(1, h[-1]), F(5**11, h[-1])]
    scales = [F(1, 45), F(125, 9)]
    reps = [75, 15]
    checks = {
        'complement_degrees_zero_to_two_vanish': complement[:3] == [0, 0, 0],
        'all_original_coefficients': old['coefficients_ascending'] == h,
        'all_original_derivative_coefficients': old['derivative_ascending'] == hp,
        'derivative_identity': [(i+3)*c for i, c in enumerate(h)] == [165*c for c in q4],
        'all_sylvester_entries': old['sylvester_matrix'] == matrix,
        'euclidean_resultant_matches_both_original_determinants': res == old['resultant'] == F(old['rational_determinant']),
        'resultant_formula': res == 3**52*5**7*11**7,
        'quadratic_resultant': rq == 3**11,
        'discriminant_and_sign': disc == old['discriminant'] == 3**47*5**6*11**7,
        'complete_factorization': old['discriminant_factorization'] == {'3':47, '5':6, '11':7} and old['unfactored_remainder'] == 1,
        'norm_polynomial_nine_exact_values': all(r['pass'] for r in norm_tests),
        'all_norm_certificate_fields': old['norm_multipliers_I_II'] == list(map(str, norms)) and old['norm_cube_scales_I_II'] == list(map(str, scales)) and old['norm_class_representatives_I_II'] == reps,
        'both_cube_scalings': all(x == r*s**3 for x,r,s in zip(norms,reps,scales)),
    }
    replay = {
        'matrix_is_15_by_15': len(matrix) == 15 and all(len(r) == 15 for r in matrix),
        'independent_exact_determinants_agree': res == old['resultant'] == F(old['rational_determinant']),
        'discriminant_nonzero': disc != 0,
        'factorization_complete': disc == 3**47*5**6*11**7,
        'support_primes_exactly_3_5_11': disc == 3**47*5**6*11**7,
        'system_I_norm_scale': norms[0] == reps[0]*scales[0]**3,
        'system_II_norm_scale': norms[1] == reps[1]*scales[1]**3,
    }
    checks['complete_original_check_and_failure_replay'] = old['checks'] == replay and old['failures'] == [k for k,v in replay.items() if not v]
    failures = [k for k,v in checks.items() if not v]
    output = source.with_name('octic-cube-support-audit-certificate.json')
    result = {'scope': 'Full arithmetic audit only; unbounded prime cases are proved in L098.',
              'original_sha256': hashlib.sha256(raw).hexdigest(),
              'coefficients_ascending': h, 'derivative_ascending': hp,
              'quadratic_resultant': str(rq), 'resultant': str(res), 'discriminant': str(disc),
              'multiplication_by_theta': [[str(v) for v in row] for row in mult],
              'norm_polynomial_tests': norm_tests, 'original_checks_replayed': replay,
              'norm_multipliers_I_II': list(map(str, norms)), 'checks': checks, 'failures': failures}
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Audit checks: {sum(checks.values())}/{len(checks)}; original checks replayed: {sum(replay.values())}/{len(replay)}; failures: {failures}')
    print('Actual/required support: {3,5,11}/{primes dividing 5*1215*Disc(h)}')
    print('Actual/required discriminant: 3^47*5^6*11^7 / 3^47*5^6*11^7')
    print('Norm polynomial: 9/9 distinct exact evaluations; required: 9 for degree at most 8')
    print('Norm multipliers: 1/1215 = 75*(1/45)^3; 5^11/1215 = 15*(125/9)^3')
    print(f'Certificate: {output.relative_to(Path.cwd())}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
