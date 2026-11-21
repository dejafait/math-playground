"""Exact algebra for the approved r=4 full-B comparison; no numerical sign proof."""
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
from math import comb
import json


def det(a):
    n = len(a)
    out = Q(0)
    for p in permutations(range(n)):
        term = Q((-1) ** sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n)))
        for i in range(n):
            term *= a[i][p[i]]
        out += term
    return out


def op(p):
    out = [Q(0)] * (len(p) + 1)
    for k, a in enumerate(p):
        out[k] += k * a
        out[k + 1] -= a
    return out


q = [[Q(-3, 2), Q(1)]]
for j in range(3):
    q.append(op(q[-1]))
a = [p + [Q(0)] * (5 - len(p)) for p in q]
coeff = {}
for missing in range(5):
    degrees = [j for j in range(5) if j != missing]
    coeff[4 - missing] = det([[row[j] for j in degrees] for row in a])


def elementary(xs, k):
    out = [Q(1)] + [Q(0)] * k
    for x in xs:
        for j in range(k, 0, -1):
            out[j] += x * out[j - 1]
    return out[k]


def value(xs):
    return sum(coeff[k] * elementary(xs, k) for k in range(5))


examples = []
for xs in ([Q(3)] * 4, [Q(22, 7)] * 4, [Q(4)] * 4, [Q(6)] * 4,
           [Q(4), Q(5), Q(6), Q(7)]):
    examples.append({'x': list(map(str, xs)), 'P': str(value(xs))})
points = [Q(3), Q(4), Q(6), Q(9)]
lhs = det([[sum(c * x**j for j, c in enumerate(row)) for x in points] for row in a])
vand = Q(1)
for i in range(4):
    for j in range(i + 1, 4):
        vand *= points[j] - points[i]
check = lhs == vand * value(points)
shifted = {j: sum(coeff[k] * comb(4 - j, k - j) * Q(3)**(k - j)
                  for k in range(j, 5)) for j in range(5)}
relative = {j: shifted[j] / Q(3)**(4-j) for j in range(5)}
lower = min(relative.values())
remainder = {j: shifted[j] - Q(19, 72) * Q(3)**(4-j) for j in range(5)}
assert check and lower == Q(19, 72) and all(v >= 0 for v in remainder.values())
result = {'status': 'exact polynomial algebra only; uniform comparison unresolved',
          'operator': 'x*d/dx-x', 'q_coefficients': [[str(c) for c in p] for p in q],
          'P_elementary_coefficients': {str(k): str(v) for k, v in sorted(coeff.items())},
          'examples': examples, 'sample_identity_check': check,
          'P_shifted_at_3_coefficients': {str(k): str(v) for k, v in shifted.items()},
          'shifted_coefficient_ratios': {str(k): str(v) for k, v in relative.items()},
          'lower_relative_to_product': str(lower),
          'P_minus_19_over_72_product_shifted_coefficients': {str(k): str(v) for k,v in remainder.items()},
          'required': 'S_(4,m)(B)>0 and relative complete-theta error<1/2, all m>=M4,u>=0',
          'failures': ['No complete-theta relative determinant error bound uniform in m and u.']}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(result, indent=2) + '\n')
print('P elementary coefficients:', result['P_elementary_coefficients'])
print('Exact sample identity:', check)
print('P shifted at 3:', result['P_shifted_at_3_coefficients'])
print('Certified polynomial lower factor:', lower)
print('Actual: signed base lower factor 19/72; theta error unbounded by this check. Required:', result['required'])
print('Unresolved:', result['failures'][0])
print('Certificate:', path)
