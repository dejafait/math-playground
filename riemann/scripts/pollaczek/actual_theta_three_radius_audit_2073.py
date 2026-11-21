#!/usr/bin/env python3
"""Independent fixed-radius audit. No imports from the original generator.

Parse the audited C530a table, rebuild basis coefficients by recurrence,
reconstruct all certificate intervals, and also use a Sylvester determinant.
No quadrature replay, coefficient refinement or additional radius is used.
"""
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'lemmas/C530a-actual-theta-four-coefficient-enclosures.md'
TEMPLATE = ROOT / 'lemmas/L530-two-atom-pollaczek-outward-flow-root-loss.md'
CLAIM = ROOT / 'lemmas/C530b-actual-theta-degree-six-three-radius-counts.md'
ORIGINAL = ROOT / 'scripts/pollaczek/actual-theta-three-radius-2072.json'
OUT = ROOT / 'scripts/pollaczek/actual-theta-three-radius-audit-2073.json'


class Box:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = Q(lo), Q(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = other if isinstance(other, Box) else Box(other)
        return Box(self.lo + other.lo, self.hi + other.hi)

    def __mul__(self, other):
        other = other if isinstance(other, Box) else Box(other)
        candidates = (self.lo*other.lo, self.lo*other.hi,
                      self.hi*other.lo, self.hi*other.hi)
        return Box(min(candidates), max(candidates))

    def reciprocal(self):
        assert self.hi < 0 or self.lo > 0
        return Box(1/self.hi, 1/self.lo)

    def sign(self):
        return 1 if self.lo > 0 else -1 if self.hi < 0 else 0

    def encode(self):
        return dict(lower=str(self.lo), upper=str(self.hi), strict_sign=self.sign())

    def hull(self, places):
        scale = 10**places
        lower = (self.lo * scale) // 1
        upper = -((-self.hi * scale) // 1)

        def show(n):
            integer, decimal = divmod(abs(n), scale)
            return ('-' if n < 0 else '') + str(integer) + '.' + str(decimal).zfill(places)

        assert Q(lower, scale) <= self.lo <= self.hi <= Q(upper, scale)
        return dict(lower=show(lower), upper=show(upper))


def multiply_all(items):
    result = Box(1)
    for item in items:
        result = result * item
    return result


def determinant(matrix):
    # Complete permutation formula; sign is the parity of the inversion count.
    result = Box(0)
    for perm in permutations(range(len(matrix))):
        inversions = sum(perm[i] > perm[j] for i in range(len(perm))
                         for j in range(i+1, len(perm)))
        term = multiply_all([matrix[i][perm[i]] for i in range(len(perm))])
        result = result + term * (-1 if inversions % 2 else 1)
    return result


def main():
    checks = {}

    def check(label, condition):
        checks[label] = bool(condition)

    original = json.loads(ORIGINAL.read_text())
    text = SOURCE.read_text()
    claim = CLAIM.read_text()
    rows = re.findall(r'^\| c([0246]) \| ([0-9.]+) \| ([0-9.]+) \|$', text, re.M)
    check('exactly_four_ordered_source_rows', [r[0] for r in rows] == ['0', '2', '4', '6'])
    assert checks['exactly_four_ordered_source_rows']
    coefficients = [Box(lo, hi) for _, lo, hi in rows]
    check('input_hash_matches', original['input_sha256'] == hashlib.sha256(SOURCE.read_bytes()).hexdigest())
    check('template_hash_matches', original['template_sha256'] == hashlib.sha256(TEMPLATE.read_bytes()).hexdigest())
    check('all_source_intervals_positive', all(x.lo > 0 for x in coefficients))
    check('source_strings_exact', original['input_display_strings'] == [[lo, hi] for _, lo, hi in rows])
    for j, box in enumerate(coefficients):
        check(f'c{2*j}_complete_interval', original['coefficient_intervals'][f'c{2*j}'] == box.encode())
    check('normalizing_denominator', original['normalizing_denominator'] == coefficients[0].encode())
    moments = [Box(1)] + [x * coefficients[0].reciprocal() for x in coefficients[1:]]
    check('complete_normalized_moments', original['normalized_moments'] == {
        f'm{j}': box.encode() for j, box in enumerate(moments)})

    # Ordinary exact polynomials in t. (n+1)g_(n+1)=t*g_n-(n+1/2)g_(n-1).
    basis = [[Q(1)], [Q(0), Q(1)]]
    for n in range(1, 6):
        shifted = [Q(0)] + basis[n]
        previous = basis[n-1] + [Q(0)] * (len(shifted)-len(basis[n-1]))
        basis.append([(a - Q(2*n+1, 2)*b)/(n+1) for a, b in zip(shifted, previous)])
    check('even_basis_parity', all(basis[2*j][k] == 0 for j in range(4)
                                  for k in range(1, 2*j+1, 2)))
    radii = [Q(9, 32), Q(1, 3), Q(1)]
    check('exactly_prescribed_radii', [r['radius'] for r in original['radii']] == list(map(str, radii)))
    records = []
    for radius, old in zip(radii, original['radii']):
        label = str(radius)
        weighted = [moments[j] * radius**(2*j) for j in range(4)]
        check(label+'_squared_radius', old['squared_radius'] == str(radius**2))
        check(label+'_complete_scaled_moments', old['scaled_moments'] == {
            key: val.encode() for key, val in zip(('A', 'B', 'C'), weighted[1:])})
        cubic = []
        for power in range(0, 7, 2):
            value = Box(0)
            for j in range(power//2, 4):
                value = value + weighted[j] * ((-1)**j * basis[2*j][power])
            cubic.append(value)
        d, c, b, a = cubic
        encoded_cubic = dict(zip(('d', 'c', 'b', 'a'), (x.encode() for x in cubic)))
        check(label+'_complete_cubic_intervals', old['cubic_coefficients_ascending'] == encoded_cubic)
        check(label+'_strict_coefficient_signs', [x.sign() for x in cubic] == [1, -1, 1, -1])
        terms = {
            'b2_c2': multiply_all([b, b, c, c]),
            'minus4_a_c3': multiply_all([a, c, c, c]) * -4,
            'minus4_b3_d': multiply_all([b, b, b, d]) * -4,
            'minus27_a2_d2': multiply_all([a, a, d, d]) * -27,
            'plus18_a_b_c_d': multiply_all([a, b, c, d]) * 18,
        }
        for key, value in terms.items():
            check(label+'_'+key+'_complete_interval', old['discriminant_terms'][key] == value.encode())
        delta = Box(0)
        for term in terms.values():
            delta = delta + term
        check(label+'_complete_discriminant', old['discriminant'] == delta.encode())
        # Two shifted cubic rows and three shifted derivative rows.
        zero = Box(0)
        matrix = [[a,b,c,d,zero], [zero,a,b,c,d],
                  [a*3,b*2,c,zero,zero], [zero,a*3,b*2,c,zero],
                  [zero,zero,a*3,b*2,c]]
        resultant = determinant(matrix)
        delta_resultant = resultant * -1 * a.reciprocal()
        check(label+'_two_independent_negative_discriminants', delta.hi < 0 and delta_resultant.hi < 0)
        hulls = {'coefficients': dict(zip(('d','c','b','a'), (x.hull(18) for x in cubic))),
                 'discriminant': delta.hull(30)}
        check(label+'_complete_reporting_hulls', old['decimal_hulls'] == hulls)
        coefficient_row = '| ' + label + ' | ' + ' | '.join(
            '['+x['lower']+','+x['upper']+']' for x in hulls['coefficients'].values()) + ' |'
        check(label+'_canonical_coefficient_table', coefficient_row in claim)
        scaled = delta * 10**30
        lower_integer, upper_integer = scaled.lo // 1, -((-scaled.hi) // 1)
        check(label+'_canonical_discriminant_table',
              f'| {label} | {lower_integer} | {upper_integer} |' in claim)
        decisive = all(x.sign() == sign for x, sign in zip(cubic, [1,-1,1,-1])) and delta.hi < 0
        check(label+'_saved_root_and_multiplicity_claims', decisive
              and old['real_t_root_count'] == 2 and old['nonreal_t_root_count'] == 4
              and old['all_six_t_roots_simple'] is True and old['decision'] == 'CERTIFIED'
              and old['required_coefficient_signs'] == [1,-1,1,-1]
              and old['actual_coefficient_signs'] == [1,-1,1,-1])
        records.append(dict(radius=label, cubic_coefficients_ascending=encoded_cubic,
                            discriminant_terms={k:v.encode() for k,v in terms.items()},
                            discriminant=delta.encode(), resultant=resultant.encode(),
                            discriminant_via_resultant=delta_resultant.encode(),
                            discriminant_hull=delta.hull(30),
                            resultant_discriminant_hull=delta_resultant.hull(30),
                            coefficient_hulls=hulls['coefficients'],
                            real_t_roots=2 if decisive else None,
                            nonreal_t_roots=4 if decisive else None))
    check('original_failure_list_empty', original['failures'] == [])
    check('original_eighteen_checks_all_true', len(original['checks']) == 18
          and all(value is True for value in original['checks'].values()))
    failures = [k for k,v in checks.items() if not v]
    result = dict(arithmetic='Exact Fraction intervals; independent code, recurrence and determinant',
                  original_sha256=hashlib.sha256(ORIGINAL.read_bytes()).hexdigest(),
                  input_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                  template_sha256=hashlib.sha256(TEMPLATE.read_bytes()).hexdigest(),
                  coefficient_intervals={f'c{2*j}':v.encode() for j,v in enumerate(coefficients)},
                  normalized_moments={f'm{j}':v.encode() for j,v in enumerate(moments)},
                  even_basis_ascending=[[str(v) for v in basis[2*j]] for j in range(4)],
                  radii=records, checks=checks, failures=failures,
                  qualifications='C530a backend contract retained; no quadrature replay or general root-preservation claim')
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    for record in records:
        print(f"r={record['radius']}: Delta={record['discriminant_hull']}; "
              f"independent resultant Delta={record['resultant_discriminant_hull']}; "
              f"required upper<0; real roots={record['real_t_roots']}, initialization requires 6")
    print(f'checks={len(checks)}, failures={failures}; certificate={OUT.relative_to(ROOT)}')
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
