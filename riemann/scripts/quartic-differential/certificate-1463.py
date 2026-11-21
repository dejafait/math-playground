"""Exact arithmetic for C020m; Walsh preservation is a cited theorem input."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


def trim(a):
    a = list(map(F, a))
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([c * x for x in a])


def derivative(a, k=1):
    for _ in range(k):
        a = trim([i * a[i] for i in range(1, len(a))] or [0])
    return a


def multiply(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i+j] += ai * bj
    return trim(c)


def remainder(a, b):
    a, b = trim(a), trim(b)
    if b == [0]:
        raise ZeroDivisionError
    while a != [0] and len(a) >= len(b):
        shift, c = len(a)-len(b), a[-1]/b[-1]
        a = add(a, [F(0)] * shift + scale(b, -c))
    return a


def sturm(a):
    seq = [trim(a), derivative(a)]
    while seq[-1] != [0]:
        r = scale(remainder(seq[-2], seq[-1]), -1)
        if r == [0]:
            break
        seq.append(r)
    def signs(side):
        return [int(v[-1] > 0)*2-1 if side == 1 or (len(v)-1) % 2 == 0
                else -(int(v[-1] > 0)*2-1) for v in seq]
    def variations(s):
        return sum(a != b for a, b in zip(s, s[1:]))
    minus, plus = signs(-1), signs(1)
    return {
        'sequence_low_to_high': [[str(c) for c in v] for v in seq],
        'signs_at_minus_infinity': minus,
        'signs_at_plus_infinity': plus,
        'variations_minus': variations(minus),
        'variations_plus': variations(plus),
        'distinct_real_roots': variations(minus)-variations(plus),
        'gcd_with_derivative_degree': len(seq[-1])-1,
    }


q = list(map(F, [1, 0, -1, 0])) + [F(3, 2)]
p = list(map(F, [-1, 0, 15, 0, 1]))
h = list(map(F, [36, 0, -12, 0, 1]))
expected = list(map(F, [5, 0, 3, 0, 1]))


def apply(a):
    total = [F(0)]
    for k, c in enumerate(q):
        total = add(total, scale(derivative(a, k), c))
    return total


def walsh(a):
    # Theorem 3.3: sum (4-k)! b_(4-k) a^(k); divide by 4!.
    total = [F(0)]
    for k in range(5):
        c = F(factorial(4-k), factorial(4)) * h[4-k]
        total = add(total, scale(derivative(a, k), c))
    return total


basis = [[F(0)]*k + [F(1)] for k in range(5)]
normalization = [apply(a) == walsh(a) for a in basis]
ps, os, hs = sturm(p), sturm(expected), sturm(h)
checks = {
    'rational_symbol_q0_one_degree_at_most_four': q[0] == 1 and len(q)-1 <= 4,
    'monic_rational_quartic': len(p) == 5 and p[-1] == 1,
    'appell_identity': apply(basis[4]) == h,
    'appell_square_factorization': multiply([-6, 0, 1], [-6, 0, 1]) == h,
    'walsh_normalization_on_entire_quartic_basis': all(normalization),
    'output_identity': apply(p) == expected,
    'input_squarefree': ps['gcd_with_derivative_degree'] == 0,
    'output_squarefree': os['gcd_with_derivative_degree'] == 0,
    'input_exactly_two_nonreal_counted_with_multiplicity': ps['distinct_real_roots'] == 2,
    'output_exactly_four_nonreal_counted_with_multiplicity': os['distinct_real_roots'] == 0,
    'appell_two_distinct_real_roots': hs['distinct_real_roots'] == 2,
}
failures = [k for k, passed in checks.items() if not passed]
certificate = {
    'coefficient_order': 'ascending powers; exact rational strings',
    'symbol_q': list(map(str, q)), 'input_p': list(map(str, p)),
    'appell_h': list(map(str, h)), 'output': list(map(str, apply(p))),
    'walsh_basis_identity': normalization,
    'sturm': {'input': ps, 'output': os, 'appell': hs},
    'actual': {'input_nonreal_multiplicity_count': 4-ps['distinct_real_roots'],
               'output_nonreal_multiplicity_count': 4-os['distinct_real_roots']},
    'required': {'input_nonreal_multiplicity_count': 2,
                 'output_nonreal_multiplicity_count': 4},
    'universal_preservation': {
        'input': 'Craven--Csordas1983 Theorem3.3 and remarks(1),(3), pp.257--258',
        'proof': 'C020m: closed-half-plane Walsh specialization; no simplicity assumption',
        'limitation': 'the script checks the exact map and root counts, not the imported theorem'},
    'checks': checks, 'failures': failures,
}
path = Path(__file__).with_name('certificate-1463.json')
path.write_text(json.dumps(certificate, indent=2) + '\n')
print('actual:', certificate['actual'])
print('required:', certificate['required'])
print('Walsh normalization basis checks:', normalization)
print('failures:', failures)
print('full certificate:', path)
if failures:
    raise SystemExit(1)
