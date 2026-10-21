#!/usr/bin/env python3
"""Exact arithmetic cross-check of L079; not a bundle-existence test."""
from fractions import Fraction
from math import isqrt
from pathlib import Path
import json


# (rank, coefficient of k in c_1, coefficient of eta in ch_2), k^2=-14.
def add(*chars):
    return tuple(sum(c[i] for c in chars) for i in range(3))


def tensor(a, b):
    r, x, z = a
    s, y, w = b
    return (r*s, r*y+s*x, r*w+s*z-14*x*y)


def dual(a):
    r, x, z = a
    return (r, -x, z)


def exterior(a):
    r, x, z = a
    return (r*(r-1)//2, (r-1)*x, (r-2)*z-7*x*x)


def euler(a):
    return 2*a[0]+a[2]


failures = []


def check(name, actual, required):
    if actual != required:
        failures.append({'check': name, 'actual': actual, 'required': required})


p, t, mixed_square = -9, -10, 156
square = 2*p*t+mixed_square
ch4 = Fraction(square, 12)
g = (-(p+4), 0, -(ch4+2*t))
h = (-(t+4), 0, -(ch4+2*p))
chi_f = 8+2*(p+t)+ch4
check('full square', square, 336)
check('forced fourth character', ch4, 28)
check('p_2 positive image', g, (5, 0, -8))
check('p_1 positive image', h, (6, 0, -10))
check('absolute versus p_2 Euler', chi_f, -euler(g))
check('absolute versus p_1 Euler', chi_f, -euler(h))

stable = {
    'K4': (4, 0, -8), 'E4': (2, 0, -4), 'K3': (3, 0, -8),
    'J5': (5, 0, -10), 'J4': (4, 0, -10),
    'E5': (2, 0, -5), 'E_plus': (2, 1, -5),
    'E_minus': (2, -1, -5),
}
expected_simple_middle = [34, 10, 32, 52, 50, 14, 0, 0]
simple_results = {}
for (name, c), expected in zip(stable.items(), expected_simple_middle):
    chi = euler(tensor(c, dual(c)))
    middle = 2-chi
    check(name+' simple middle', middle, expected)
    if middle < 0 or middle % 2:
        failures.append({'check': name+' simple nonnegative/even', 'actual': middle})
    simple_results[name] = {'character': c, 'chi_end': chi, 'middle': middle,
                            'required_middle_lower_bound': 0, 'required_parity': 0}

o = (1, 0, 0)
cases = [
    ('G_K4', [o, stable['K4']], 0, (0, 4, 0), 2),
    ('G_E4x2', [o, stable['E4'], stable['E4']], 3, (3, 10, 3), 5),
    ('G_K3', [o, o, stable['K3']], 1, (1, 6, 1), 5),
    ('H_J5', [o, stable['J5']], 0, (0, 10, 0), 2),
    ('H_J4', [o, o, stable['J4']], 1, (1, 12, 1), 5),
    ('H_E5x2', [o, o, stable['E5'], stable['E5']], 4, (4, 18, 4), 8),
    ('H_dual_pair', [o, o, stable['E_plus'], stable['E_minus']], 2, (2, 14, 2), 6),
]
case_results = {}
for name, blocks, skew_sections, expected_adj, end_sections in cases:
    total = add(*blocks)
    target = g if name.startswith('G') else h
    check(name+' character', total, target)
    # Independently compare the whole-bundle exterior formula against
    # Lambda^2 of a direct sum, keeping every first-class cross term.
    terms = [exterior(c) for c in blocks]
    terms += [tensor(a, b) for i, a in enumerate(blocks) for b in blocks[i+1:]]
    whole_adj = exterior(total)
    check(name+' exterior direct-sum identity', add(*terms), whole_adj)
    adj_cohom = (skew_sections, 2*skew_sections-euler(whole_adj), skew_sections)
    check(name+' adjoint cohomology', adj_cohom, expected_adj)
    end_middle = 2*end_sections-euler(tensor(total, dual(total)))
    trivial_count = sum(c == o for c in blocks)
    image_cohom = (trivial_count, 2*trivial_count-euler(total), trivial_count)
    block_middle = sum(-euler(c) for c in blocks if c != o)
    check(name+' additive image cohomology', image_cohom[1], block_middle)
    if adj_cohom[1] < 0 or adj_cohom[1] % 2 or end_middle < 0 or end_middle % 2:
        failures.append({'check': name+' total index bound/parity'})
    case_results[name] = {'character': total, 'image_cohomology': image_cohom,
                         'adjoint_character': whole_adj, 'adjoint_cohomology': adj_cohom,
                         'end_sections': end_sections, 'end_middle': end_middle}

# Exact quadratic bounds cover all integer first-class coefficients,
# rather than extrapolating from a bounded numerical scan.
bounds = {'G': Fraction(10, 14), 'H': Fraction(14, 14)}
allowed = {}
for name, bound in bounds.items():
    radius = isqrt(bound.numerator // bound.denominator)
    allowed[name] = list(range(-radius, radius+1))
check('G full integer first-class domain', allowed['G'], [0])
check('H full integer first-class domain', allowed['H'], [-1, 0, 1])

certificate = {
    'target': 'L079 (-13,-14) necessary-image arithmetic only',
    'signed_grr': {'p': p, 't': t, 'mixed_square': mixed_square, 'full_square': square,
                   'ch4': ch4, 'G': g, 'H': h, 'chi_F': chi_f},
    'simple_indices': simple_results, 'case_indices': case_results,
    'exact_first_class_bounds': {'r_squared_bounds': bounds, 'allowed_integers': allowed},
    'failures': failures, 'passed': not failures,
    'limitations': 'No fibre/base-change/preservation proof, source verification, topology or existence is certified by this arithmetic check.',
}
path = Path(__file__).with_name('orthogonal_image_indices_certificate.json')
path.write_text(json.dumps(certificate, indent=2, default=str)+'\n')
minimum_simple = min(r['middle'] for r in simple_results.values())
minimum_adjoint = min(r['adjoint_cohomology'][1] for r in case_results.values())
print('PASS' if not failures else 'FAIL', 'L079 exact HRR/character/index cross-check')
print(f'Actual minimum simple middle={minimum_simple}; required >=0 and even.')
print(f'Actual minimum adjoint middle={minimum_adjoint}; required >=0 and even.')
print(f'Actual allowed first-class coefficients: G={allowed["G"]}, H={allowed["H"]}.')
print(f'Failures={len(failures)}; full certificate: {path}')
raise SystemExit(bool(failures))
