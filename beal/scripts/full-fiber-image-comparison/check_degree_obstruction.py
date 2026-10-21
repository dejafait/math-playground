"""Exact coefficient certificate for L040; no p-adic sampling cutoff."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
SOURCE = BASE.parent / 'five-isogeny-modular-norm/norm-certificate.json'


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a): c[i] += v
    for i, v in enumerate(b): c[i] += v
    return c


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b): c[i+j] += v*w
    return c


def power(a, n):
    c = [1]
    for _ in range(n): c = mul(c, a)
    return c


def mod(a): return [v % 5 for v in a]
def ev(a, x): return sum(v*x**i for i, v in enumerate(a))


def det_mod(matrix):
    a = [mod(row) for row in matrix]
    d = 1
    for j in range(len(a)):
        k = next((k for k in range(j, len(a)) if a[k][j]), None)
        if k is None: return 0
        if k != j:
            a[k], a[j] = a[j], a[k]
            d = -d
        v = a[j][j]
        d = d*v % 5
        for k in range(j+1, len(a)):
            c = a[k][j]*pow(v, -1, 5) % 5
            a[k] = [(x-c*y) % 5 for x, y in zip(a[k], a[j])]
    return d % 5


def resultant_matrix(a, b):
    m, n = len(a)-1, len(b)-1
    return ([[0]*i + a[::-1] + [0]*(n-i-1) for i in range(n)] +
            [[0]*i + b[::-1] + [0]*(m-i-1) for i in range(m)])


c = json.loads(SOURCE.read_text())['polynomials_ascending']
h, J, d = c['h'], c['jcoef'], c['d']
h3 = power(h, 3)
checks = {'d_exact': d == power([-16, 1], 11),
          'h_monic_degree4': len(h) == 5 and h[-1] == 1,
          'J_degree_at_most11': len(J) <= 12,
          'F_monic_degree12': len(h3) == 13 and h3[-1] == 1}
cases = {}
for s, p, q, e in [(0, [1, 1, 1], [2, 4, 1], 3),
                    (3, [2, 0, 3, 1], [4, 4, 4, 1], 2)]:
    F = mod(add(add(h3, [s*v for v in J]), [-s*s*v for v in d]))
    blocks = [mod(power(p, e)), mod(power(q, e))]
    matrix = resultant_matrix(*blocks)
    resultant = det_mod(matrix)
    checks[f'residue_{s}_full_product'] = mod(mul(*blocks)) == F
    checks[f'residue_{s}_coprime_blocks'] = resultant != 0
    checks[f'residue_{s}_degree_bound'] = [len(b)-1 for b in blocks] == [6, 6]
    cases[str(s)] = {'F_mod5': F, 'base_factors': [p, q],
                     'multiplicity': e, 'blocks': blocks,
                     'sylvester_matrix': matrix, 'resultant_mod5': resultant,
                     'block_degrees': [len(b)-1 for b in blocks]}

checks['h16_unit'] = ev(h, 16) % 5 == 1
checks['J16_unit'] = ev(J, 16) % 5 == 1
# G_s(w)=s^-2 w^12 F(1/w,s), for v(s)<0. Its only surviving
# coefficient contribution modulo 5 is -w^12 d(1/w).
Gbar = mod([0] + [-v for v in d[::-1]])
expected_Gbar = mod([0] + [-v for v in power([1, -16], 11)])
checks['reciprocal_reduction'] = Gbar == expected_Gbar
checks['reciprocal_zero_simple'] = Gbar[0] == 0 and Gbar[1] == 4
checks['nonintegral_integral_x_reduction'] = mod([-v for v in d]) == mod([-v for v in power([-1, 1], 11)])
certificate = {
    'source': str(SOURCE.relative_to(BASE.parent.parent)),
    'polynomials_ascending': {'h': h, 'J': J, 'd': d},
    'integral_branch_cases': cases,
    'nonintegral_case': {'h16': ev(h, 16), 'J16': ev(J, 16),
                         'G_mod5': Gbar, 'G_mod5_expected': expected_Gbar,
                         'root_residue': 0, 'derivative_mod5': Gbar[1],
                         'scalar_valuation': '-n with n>0',
                         'degree11_point_valuation_equation': '11*v5(x-16)=n'},
    'bounds': {'block_degree_max_actual': 6, 'degree11_root_required': 11,
               'whole_fiber_dimension_actual': 12, 'whole_fiber_dimension_required': 12},
    'checks': checks, 'failures': [k for k, ok in checks.items() if not ok]}
path = BASE / 'degree-obstruction-certificate.json'
path.write_text(json.dumps(certificate, indent=2) + '\n')
print(f'Checks: {sum(checks.values())}/{len(checks)}; failures: {certificate["failures"]}')
print('Integral branch block bound: actual=6, degree required=11; total=12/12')
print('Nonintegral Hensel derivative mod 5: actual=4, required=nonzero; 11*v5(x-16)=n')
print(f'Certificate: {path.relative_to(BASE.parent.parent)}')
if certificate['failures']: raise SystemExit(1)
