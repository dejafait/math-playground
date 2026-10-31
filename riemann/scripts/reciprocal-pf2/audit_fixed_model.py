"""Independent exact replay of L560; never imports or rewrites fixed_model.py.

The calculus inequalities are justified in L560, not by a grid in this file.
All arithmetic is over Q[i]. Full evidence includes every saved numeric field.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json


def g(r=0, i=0):
    return (Q(r), Q(i))


def plus(z, w):
    return (z[0] + w[0], z[1] + w[1])


def times(z, w):
    return (z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0])


def scale(z, r):
    return (z[0]*r, z[1]*r)


def conjugate(z):
    return (z[0], -z[1])


def inverse(z):
    return scale(conjugate(z), 1/(z[0]**2 + z[1]**2))


def power(z, n):
    ans = g(1)
    for _ in range(n):
        ans = times(ans, z)
    return ans


def psum(*polys):
    out = [g() for _ in range(max(map(len, polys)))]
    for p in polys:
        for j, value in enumerate(p):
            out[j] = plus(out[j], value)
    return out


def pmul(p, q):
    out = [g() for _ in range(len(p) + len(q) - 1)]
    for j, k in product(range(len(p)), range(len(q))):
        out[j+k] = plus(out[j+k], times(p[j], q[k]))
    return out


def pprod(polys):
    ans = [g(1)]
    for p in polys:
        ans = pmul(ans, p)
    return ans


def derivative(p):
    return [scale(p[j], j) for j in range(1, len(p))]


def evaluate(p, z):
    return tuple(sum(times(c, power(z, j))[k] for j, c in enumerate(p))
                 for k in (0, 1))


def show(z):
    if z[1] == 0:
        return str(z[0])
    return {'real': str(z[0]), 'imaginary': str(z[1])}


checks = []


def check(name, actual, expected):
    checks.append({'name': name, 'actual': actual, 'required': expected,
                   'pass': actual == expected})


a = g(10, Q(1, 4))
rates = [g(1), g(2), a, conjugate(a)]
A, B = Q(5126402, 7536867), -Q(2563201, 7087875)
C, D = Q(31766670568, 5935596798625), Q(247683050816, 5935596798625)
c = g(C/2, D/2)
weights = [g(A), g(B), c, conjugate(c)]
factors = [[g(1), g(), scale(inverse(power(lam, 2)), -1)]
           for lam in rates]
P = pprod(factors)
P1 = derivative(P)
P2 = derivative(P1)
check('P is real', all(z[1] == 0 for z in P), True)

# Four separate pole factors, without using the original combined numerator.
den_factors = [[power(lam, 2), g(), g(-1)] for lam in rates]
den = pprod(den_factors)
num = psum(*[[times(scale(times(lam, w), 2), term)
              for term in pprod(den_factors[:j] + den_factors[j+1:])]
             for j, (lam, w) in enumerate(zip(rates, weights))])
constant = den[0]
check('entire rational numerator', list(map(show, num)),
      [show(constant)] + ['0']*(len(num)-1))
check('denominator equals constant times defining P', list(map(show, den)),
      [show(times(constant, z)) for z in P])
check('constant', show(constant), '2563201/64')
mass = sum((times(w, inverse(lam))[0]*2 for lam, w in zip(rates, weights)))
check('direct total mass', str(mass), '1')
for j, (lam, w) in enumerate(zip(rates, weights)):
    check('pole coefficient '+str(j), show(times(w, evaluate(P1, lam))), '-1')

jets = [tuple(sum(times(w, power(scale(lam, -1), j))[k]
                  for lam, w in zip(rates, weights)) for k in (0, 1))
        for j in range(4)]
check('origin jets in the proof', list(map(show, jets)),
      ['21691949/66971775', '0', '-58953623/133943550', '0'])

b = -A*B
u = scale(times(c, power(plus(a, g(-1)), 2)), -2*A)
v = scale(times(c, power(plus(a, g(-2)), 2)), -2*B)
k = (c[0]**2 + c[1]**2)/4

# Direct ordered double multiplication f'^2 - f*f'', including diagonals.
curvature = {}
for j, h in product(range(4), repeat=2):
    rate = plus(rates[j], rates[h])
    diff = plus(times(rates[j], rates[h]), scale(power(rates[h], 2), -1))
    coefficient = times(times(weights[j], weights[h]), diff)
    curvature[rate] = plus(curvature.get(rate, g()), coefficient)
curvature = {lam: val for lam, val in curvature.items() if val != g()}
expected_curvature = {g(3): g(b), g(11, Q(1, 4)): scale(u, Q(1, 2)),
                      g(11, -Q(1, 4)): scale(conjugate(u), Q(1, 2)),
                      g(12, Q(1, 4)): scale(v, Q(1, 2)),
                      g(12, -Q(1, 4)): scale(conjugate(v), Q(1, 2)),
                      g(20): g(k)}


def exponential_table(table):
    return [{'rate': show(lam), 'coefficient': show(table[lam])}
            for lam in sorted(table)]


check('complete curvature exponential identity', exponential_table(curvature),
      exponential_table(expected_curvature))
check('conjugate sine coefficient is positive D', str(2*c[1]), str(D))
check('signs used in all envelopes',
      [A>0, B<0, C>0, D>0, b>0, u[0]<0, u[1]<0, v[0]>0, v[1]>0, k>0],
      [True]*10)
e, h = -u[0], -u[1]
bounds = {'density_scaled_lower': A+B-C-D,
          'curvature_scaled_near_lower': b-e,
          'near_envelope_derivative_margin': 8*e-h/4,
          'curvature_scaled_far_lower': b-(e+h)/256-(v[0]+v[1])/512}
for name, value in bounds.items():
    check(name+' strictly positive', value > 0, True)

p10, p110, p210 = [evaluate(q, g(10)) for q in (P, P1, P2)]
jet = plus(power(p110, 2), scale(times(p10, p210), -1))
check('negative polynomial jet', show(jet), '-7390676030193099/6569999366401')
check('jet strictly negative', jet[1] == 0 and jet[0] < 0, True)

saved_path = Path(__file__).with_name('fixed-model-certificate.json')
saved = json.loads(saved_path.read_text())
recomputed = {
    'polynomial_coefficients_ascending': list(map(show, P)),
    'density_coefficients': dict(zip(('A','B','C','D'), map(str, (A,B,C,D)))),
    'transform_identity': {
        'common_denominator_coefficients': list(map(show, den)),
        'summed_numerator_coefficients': list(map(show, num)),
        'required_constant': show(constant), 'pass': True},
    'right_derivatives_at_zero': list(map(show, jets)),
    'curvature_coefficients': dict(zip(('b','u_r','u_i','v_r','v_i','k'),
                                     map(str, (b, *u, *v, k)))),
    'global_bounds': {**{key: str(value) for key, value in bounds.items()},
        'required_lower_bound': '0', 'near_interval': '0<=x<=1',
        'far_interval': 'x>=1',
        'tail_inequalities': 'e>2 implies exp(-8x)<1/256 and exp(-9x)<1/512 for x>=1',
        'all_pass': True},
    'polynomial_jet': {'P_10': show(p10), 'Pprime_10': show(p110),
        'Psecond_10': show(p210), 'first_laguerre_10': show(jet),
        'required': 'strictly negative', 'pass': True},
    'failures': []}
for field, value in recomputed.items():
    check('saved certificate /'+field, value, saved[field])

failures = [item['name'] for item in checks if not item['pass']]
out = Path(__file__).with_name('independent-audit-certificate.json')
out.write_text(json.dumps({
    'model': 'Exactly L560; no parameter search',
    'independence': 'Four defining factors and ordered curvature double sum; original module not imported',
    'checks': checks, 'recomputed_saved_fields': recomputed, 'failures': failures,
    'analytic_obligations': 'Direct half-line integration, origin C2 matching and global envelopes are proved in L560; arithmetic replay alone is not their proof',
    'qualifications': ['No PF256 check', 'No actual-Xi transfer', 'No formal verification', 'No new theorem claimed']
}, indent=2)+'\n')
print(f'{"PASS" if not failures else "FAIL"}: {len(checks)} exact checks; failures: {len(failures)}')
for name, value in bounds.items():
    print(f'{name}: {float(value):.12g} > required 0')
print(f'polynomial jet: {float(jet[0]):.12g} < required 0')
print('failures:', failures)
print('certificate:', out)
raise SystemExit(bool(failures))
