"""Exact residue and cardinality evidence; uniform proof is in L060.

No p-adic sampling, external packages, or class-group assumptions.
Polynomials have ascending coefficients; finite-field arithmetic is mod 5.
"""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
SOURCE = BASE.parent / 'five-isogeny-modular-norm/norm-certificate.json'


def trim(a):
    a = [int(v) % 5 for v in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a): c[i] += v
    for i, v in enumerate(b): c[i] += v
    return trim(c)


def scale(a, k): return trim([k*v for v in a])


def mul(a, b):
    c = [0] * (len(a)+len(b)-1)
    for i, u in enumerate(a):
        for j, v in enumerate(b): c[i+j] += u*v
    return trim(c)


def power(a, n):
    c = [1]
    for _ in range(n): c = mul(c, a)
    return c


def divmodp(a, b):
    a, b = trim(a), trim(b)
    assert b != [0]
    q = [0] * max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        k = len(a)-len(b)
        t = a[-1]*pow(b[-1], -1, 5) % 5
        q[k] = t
        a = add(a, [0]*k+scale(b, -t))
    return trim(q), a


def bezout(a, b):
    r0, r1, u0, u1, v0, v1 = a, b, [1], [0], [0], [1]
    while r1 != [0]:
        q, r = divmodp(r0, r1)
        r0, r1 = r1, r
        u0, u1 = u1, add(u0, scale(mul(q, u1), -1))
        v0, v1 = v1, add(v0, scale(mul(q, v1), -1))
    t = pow(r0[-1], -1, 5)
    return scale(r0, t), scale(u0, t), scale(v0, t)


def deriv(a): return trim([i*a[i] for i in range(1, len(a))])
def ev(a, x): return sum(int(v)*x**i for i, v in enumerate(a))


c = json.loads(SOURCE.read_text())['polynomials_ascending']
h, J, d, b, a = [trim(c[k]) for k in ['h', 'jcoef', 'd', 'b', 'a']]
checks, cases = {}, {}
for s in [1, 2, 4]:
    F = add(add(power(h, 3), scale(J, s)), scale(d, -s*s))
    case = {'F_mod5': F, 'bezout': {}}
    for label, p in [('derivative', deriv(F)), ('b', b), ('d', d)]:
        g, u, v = bezout(F, p)
        case['bezout'][label] = {'gcd': g, 'u': u, 'v': v, 'p': p}
        checks[f'{s}_{label}_identity'] = add(mul(u, F), mul(v, p)) == g
        if label in ('derivative', 'b'):
            checks[f'{s}_{label}_unit_gcd'] = g == [1]
    cases[str(s)] = case

nonintegral = {'five_power_eleven_mod_eleven': pow(5, 11, 11),
               'J16_mod5': ev(c['jcoef'], 16) % 5,
               'h16_mod5': ev(c['h'], 16) % 5}
lower = {'point': [16, -61], 'curve_y_derivative': -121,
         'curve_x_rhs_derivative': 726, 'dy_dx': -6,
         'f': -1331, 'df_dx': -231, 'log_derivative_mod5': 1}
checks['lower_on_curve'] = (-61)**2-61 == 16**3-16**2-10*16-20
checks['lower_implicit_derivative'] = -121*(-6) == 726
checks['lower_f'] = (16-4)*(-61)-4*16**2+30*16-55 == -1331
checks['lower_df'] = (16-4)*(-6)-61-8*16+30 == -231
checks['lower_log_derivative_unit'] = (-231)*pow(-1331, -1, 5) % 5 == 1
checks['eleventh_power_bijective'] = nonintegral['five_power_eleven_mod_eleven'] != 1
checks['nonintegral_units'] = nonintegral['J16_mod5'] == nonintegral['h16_mod5'] == 1

units = [i for i in range(125) if i % 5]
fifths = sorted({pow(i, 5, 125) for i in units})
kernel = [i for i in units if pow(i, 5, 125) == 1]
unit_quotient = {'modulus': 125, 'unit_count': len(units),
                 'fifth_power_residues': fifths, 'fifth_power_kernel': kernel,
                 'unit_class_upper_bound': len(units)//len(fifths)}
checks['rational_unit_quotient_bound'] = len(units) == 100 and len(fifths) == 20
checks['rational_unit_kernel'] = kernel == [1, 26, 51, 76, 101]
bounds = {'unrestricted_constructed_unit_classes': 5**11,
          'norm_class_upper_bound': 5,
          'norm_slice_lower_bound': 5**10,
          'integral_scalar_residues': [2, 4],
          'scalar_lifts_per_residue_mod125': 25,
          'root_upper_bound_per_residue': 12,
          'whole_fiber_upper_bound': 2*25*12}
checks['strict_cardinality_separation'] = bounds['whole_fiber_upper_bound'] < bounds['norm_slice_lower_bound']

out = {'source': str(SOURCE.relative_to(BASE.parent.parent)),
       'cases': cases, 'nonintegral': nonintegral, 'lower_bound_data': lower,
       'rational_unit_quotient': unit_quotient, 'bounds': bounds,
       'checks': checks, 'failures': [k for k, v in checks.items() if not v]}
path = BASE / 'bounds-certificate.json'
path.write_text(json.dumps(out, indent=2)+'\n')
print('Checks:', len(checks), 'failures:', out['failures'])
for s, case in cases.items():
    print('Scalar residue', s, 'gcds:',
          {k: v['gcd'] for k, v in case['bezout'].items()})
print('Nonintegral:', nonintegral)
print('Actual whole-fiber upper bound:', bounds['whole_fiber_upper_bound'],
      'required below:', bounds['norm_slice_lower_bound'])
print('Certificate:', path.relative_to(BASE.parent.parent))
assert not out['failures']
