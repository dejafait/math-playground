#!/usr/bin/env python3
"""Independent finite arithmetic audit of L048; no cycle search or new bound."""
import json
from fractions import Fraction as Q
from math import factorial
from pathlib import Path

root = Path(__file__).resolve().parent
source = json.loads((root / 'nineteen-exact-transfer-certificate.json').read_text())
checks = []


def record(name, left, relation, right):
    left, right = Q(left), Q(right)
    # Compare integer cross products independently of Fraction ordering.
    difference = left.numerator * right.denominator - right.numerator * left.denominator
    passed = {'=': difference == 0, '<': difference < 0, '>': difference > 0}[relation]
    checks.append(dict(name=name, actual=str(left), relation=relation,
                       required=str(right), cross_product_difference=str(difference), passed=passed))


log_values = {}
for name, t in [('log2', Q(2)), ('log3', Q(3)), ('cJ', Q(11, 4))]:
    x = (t - 1) / (t + 1)
    power, partial = x, Q(0)
    for odd in range(1, 24, 2):
        partial += 2 * power / odd
        power *= x * x
    remainder = 2 * power / (25 * (1 - x * x))
    values = dict(argument=t, x=x, terms=12, lower=partial,
                  remainder_upper=remainder, upper=partial + remainder)
    for key, value in values.items():
        record(f'{name}: recomputed {key}', value, '=', Q(source['log_enclosures'][name][key]))
    log_values[name] = {key: str(value) for key, value in values.items()}

record('log2 lower', log_values['log2']['lower'], '>', Q(6931, 10000))
record('log3 upper', log_values['log3']['upper'], '<', Q(10987, 10000))
record('cJ upper', log_values['cJ']['upper'], '<', Q(41, 40))
record('delta lower: 3^2 > 2^3', 3**2, '>', 2**3)
d = Q(793, 500)
q, b = Q(189, 100), Q(31, 100)
record('delta upper', Q(10987, 6931), '<', d)
record('q enclosure', 3*d*d/4, '<', q)
record('b enclosure', d*(3*d-4)*Q(41, 40)/4, '<', b)

# Transfer unit homogeneous and unit additive responses through 18 edges.
# Sum the 19 input states before advancing; this does not use a geometric formula.
homogeneous, additive = Q(1), Q(0)
S, U = Q(0), Q(0)
for index in range(19):
    S += homogeneous
    U += additive
    if index < 18:
        homogeneous *= q
        additive = q * additive + 1
record('homogeneous sum matches certificate', S, '=', Q(source['S']))
record('additive sum matches certificate', U, '=', Q(source['U']))
record('geometric formula', S, '=', (q**19-1)/(q-1))
record('additive formula', (q-1)*U, '=', S-19)
record('S upper', S, '<', 201100)
record('positive additive contribution retained', 6*b*U, '>', 0)
record('additive upper via S', 6*b*U, '<', Q(186, 89)*S)
record('additive rational coefficient', Q(186, 89), '<', Q(21, 10))
e_partial = sum((Q(1, factorial(j)) for j in range(6)), Q(0))
record('exponential partial sum', e_partial, '=', Q(163, 60))
record('exponential lower', e_partial, '>', Q(27, 10))
record('log19 bound', Q(27, 10)**3, '>', 19)
C, M = 338460000, 225640000
record('logC bound', Q(27, 10)**20, '>', C)
record('primitive ray', Q(3, 2)*M, '=', C)
record('constant remainder', Q(8, 5)*3*19+Q(69*19, 1034), '<', 93)
record('logarithmic coefficient assembly', Q(8, 5)*Q(15, 4)*Q(133, 10), '=', Q(399, 5))
record('height sum coefficient', Q(8, 5)*Q(15, 4), '=', 6)
A = Q(399, 5)*201100
B = (6*(8+3)+Q(21, 10))*201100+93
record('A', A, '=', 16047780)
record('B', B, '=', 13695003)
record('A certificate', A, '=', Q(source['A']))
record('B certificate', B, '=', Q(source['B']))
record('derivative positive for all t >= C', A, '<', C)
record('RHS upper at C', 20*A+B, '<', C)
record('positive full-ray margin', C-20*A-B, '=', 3809397)

# Verify every stored comparison, including any unanticipated extra records.
for item in source['checks']:
    record('stored comparison: '+item['name'], item['actual'], item['relation'], item['required'])
    record('stored pass flag: '+item['name'], int(item['passed']), '=', 1)
record('source failures count', len(source['failures']), '=', 0)
failures = [item for item in checks if not item['passed']]
result = dict(scope='L048 nineteen-word arithmetic audit only; analytic proof and qualifications remain in L048',
              log_values=log_values, S=str(S), U=str(U), additive_contribution=str(6*b*U),
              A=str(A), B=str(B), C=C, rhs_upper=str(20*A+B), margin=str(C-20*A-B),
              checks=checks, failures=failures)
path = root / 'nineteen-exact-transfer-audit-certificate.json'
path.write_text(json.dumps(result, indent=2)+'\n')
print(f'checks={len(checks)}, failures={len(failures)}')
print(f'S={S}; required S < 201100')
print(f'RHS(C) < {20*A+B}; required <= {C}; margin > {C-20*A-B}')
print(f'derivative: A={A} < C={C}; failures={[item["name"] for item in failures]}')
print(f'certificate: {path.relative_to(Path.cwd())}')
if failures:
    raise SystemExit(1)
