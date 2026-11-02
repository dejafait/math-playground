#!/usr/bin/env python3
"""Exact scalar checks for the two-offset contour; not an analytic proof."""
from fractions import Fraction as F
from pathlib import Path
import json


def rat(x):
    return str(x.numerator) + '/' + str(x.denominator)


U = F(121, 64)
d = F(5, 4)
R = F(11, 8)
b = F(1, 50)
c = F(1, 200)
Y = F(9, 20)
cells = 256
rows = {}
for label, e in [('lower_e', d-b), ('R', R)]:
    values = []
    for j in range(cells+1):
        t = F(j, cells)
        values.append(1/(e-t) + t/(U-e*t))
    left = sum(values[:-1])/cells
    right = sum(values[1:])/cells
    scale = 10**12
    left_down = F((left*scale).__floor__(), scale)
    right_up = F((right*scale).__ceil__(), scale)
    rows[label] = {
        'e': rat(e),
        'values': [rat(v) for v in values],
        'left': rat(left),
        'right': rat(right),
        'left_down': rat(left_down),
        'right_up': rat(right_up),
    }

L0 = F(24, 689)
L1 = F(24, 289)
lower_side_rate = (L0+L1)/2 - F(11, 5)*b
upper_side_rate = F(7296, 397001)
omega_upper = F(220, 189)  # 10*pi/27 < 220/189, using pi < 22/7
omega_lower = F(10, 9)    # 10*pi/27 > 10/9, using pi > 3
epsilon = F(1, 3000)
checks = {}


def check(name, actual, required, relation):
    if relation == '<':
        ok = actual < required
    elif relation == '>':
        ok = actual > required
    elif relation == '<=':
        ok = actual <= required
    elif relation == '=':
        ok = actual == required
    else:
        raise ValueError(relation)
    checks[name] = {'actual': rat(actual), 'required': rat(required),
                    'relation': relation, 'pass': ok}


check('g_lower_e_upper', F(rows['lower_e']['right_up']), F(11, 5), '<')
check('g_R_lower', F(rows['R']['left_down']), F(9, 5), '>')
check('original_pole_clearance', d*d+Y*Y, F(273, 200)**2, '<')
check('full_rectangle_spatial_radius', (d+c)**2+Y*Y, F(16, 9), '<')
check('half_ratio_quadratic', 9*d*d/8, U, '<')
check('lower_side_rate', lower_side_rate, F(1, 100), '>')
check('upper_side_rate', upper_side_rate, F(1, 100), '>')
check('side_parity_charge', (L1-L0)/2, F(1), '<')
check('upper_product_riemann_charge', F(128, 33)*c, F(1), '<')
check('tail_rate', (2*omega_lower-F(11, 5))*b, epsilon, '>')
check('shifted_top_rate', (F(9, 5)-omega_upper)*c, epsilon, '>')
check('shifted_side_rate', F(1, 100)-omega_upper*c, epsilon, '>')
check('unshifted_top_rate', F(9, 5)*c, epsilon, '>')
check('unshifted_side_rate', F(1, 100), epsilon, '>')
check('minimum_side_position_n27', Y-F(27, 20*27), F(2, 5), '=')
check('horizontal_kernel_clearance_n183', omega_lower*183*c, F(1), '>')
check('omega_linear_constant', omega_upper, F(6, 5), '<')
check('top_and_side_length', 2*Y+2*(b+c), F(1), '<')
check('spatial_geometric_bound', 1/(1-F(4, 3)/R), F(33), '=')
check('total_error_constant', F(2376+792+1188, 5), F(1000), '<')
paid_rate = F(1, 16)-2*F(91, 5000)
check('paid_rate', paid_rate, F(0), '>')
assert paid_rate == F(261, 10000)

failures = [name for name, item in checks.items() if not item['pass']]
out = Path(__file__).with_suffix('.json')
certificate = {
    'status': 'PASS' if not failures else 'FAIL',
    'scope': 'Exact rational scalar checks only; contour, residues, all-frequency '
             'identity and analytic uniformity are proved in the canonical lemma.',
    'parameters': {'b': rat(b), 'c': rat(c), 'epsilon': rat(epsilon),
                   'pi_bounds': '3 < pi < 22/7', 'cells': cells},
    'quadrature': rows,
    'checks': checks,
    'failures': failures,
    'summary': {
        'g_lower_e_upper': rows['lower_e']['right_up'],
        'g_R_lower': rows['R']['left_down'],
        'lower_side_rate': rat(lower_side_rate),
        'upper_side_rate': rat(upper_side_rate),
        'tail_rate_lower': rat((2*omega_lower-F(11, 5))*b),
        'shifted_top_rate_lower': rat((F(9, 5)-omega_upper)*c),
        'shifted_side_rate_lower': rat(F(1, 100)-omega_upper*c),
        'required_error_rate': rat(epsilon),
        'paid_excess_rate': rat(paid_rate),
        'all_checks_pass': not failures,
    },
}
out.write_text(json.dumps(certificate, indent=2)+'\n')
print(certificate['status'])
for name, item in checks.items():
    print(f"{name}: {item['actual']} {item['relation']} {item['required']} "
          f"{'PASS' if item['pass'] else 'FAIL'}")
print('failures:', failures)
print('certificate:', out.relative_to(Path.cwd()))
raise SystemExit(bool(failures))
