#!/usr/bin/env python3
"""Exact scalar checks for C663b; analytic saddle/tail proof is in the lemma."""
from fractions import Fraction as F
import json
from pathlib import Path

dest = Path(__file__).with_suffix('.json')
d, e0, U, Y = F(5, 4), F(117, 100), F(121, 64), F(9, 20)
N, scale = 256, 10**12
out = {'status': 'INCOMPLETE', 'scope': 'Exact rational scalar inequalities only; no numerical saddle or finite-family screen.',
       'checks': {}, 'failures': [], 'riemann_rows': {}}

def check(label, condition):
    out['checks'][label] = bool(condition)
    if not condition:
        out['failures'].append(label)

def h(e, t):
    return 1/(e-t) + t/(U-e*t)

def sums(e, label):
    rows = []
    for j in range(N+1):
        value = h(e, F(j, N))
        low = value.numerator*scale//value.denominator
        high = -(-value.numerator*scale//value.denominator)
        rows.append({'j': j, 'value': str(value), 'lower_scaled': low, 'upper_scaled': high})
        check(label+'_rounding_'+str(j), F(low, scale) <= value <= F(high, scale))
    out['riemann_rows'][label] = rows
    return (F(sum(r['lower_scaled'] for r in rows[:-1]), N*scale),
            F(sum(r['upper_scaled'] for r in rows[1:]), N*scale))

gd_lo, gd_hi = sums(d, 'd')
ge_lo, ge_hi = sums(e0, 'e0')
check('g_d_lower', gd_lo > F(21, 10))
check('g_d_upper', gd_hi < F(11, 5))
check('g_e0_lower', ge_lo > F(7, 3))
check('lambda_lower_from_pi_gt_3', F(11, 5) < F(20, 9))
check('lambda_upper_from_pi_lt_22_over_7', F(440, 189) < F(7, 3))
check('b_over_A_at_most_half', F(9, 8)*d*d < U)
check('curvature_at_least_12_over_5', F(3, 4)*(1/(d-1)-1/d) == F(12, 5))
check('A_upper_6', 1/(e0-1) < 6)
check('A_lower_4_over_5', 1/d == F(4, 5))
check('gaussian_denominator_below_9', 1+36*Y*Y < 9)
check('gaussian_decay_at_least_1_over_40', F(6, 25)/9 > F(1, 40))
bmax = d-e0
rho = F(7, 30)*bmax-F(6, 5)*bmax*bmax
rho_star, gamma, kappa = F(261, 20000), F(29, 1000), F(91, 5000)
check('rate_quadratic_increasing', F(7, 30)-F(12, 5)*bmax > 0)
check('rate_value', rho == F(103, 9375))
check('sufficient_rate', rho < rho_star)
check('side_remainder_smaller', rho < gamma)
check('paid_arc_margin', F(1, 16)-2*kappa-2*rho == F(619, 150000))
out['summary'] = {'cells_per_integral': N, 'rows_per_integral': N+1,
    'g_d_enclosure': [str(gd_lo), str(gd_hi)], 'g_e0_enclosure': [str(ge_lo), str(ge_hi)],
    'required_g_d': '21/10 < g(d) < 11/5', 'required_g_e0': 'g(e0) > 7/3',
    'rho_upper': str(rho), 'required_rho_below': str(rho_star),
    'strict_rate_margin': str(rho_star-rho), 'side_error_gap': str(gamma-rho),
    'paid_arc_linear_margin': str(F(1, 16)-2*kappa-2*rho),
    'limitations': 'Does not verify the contour identity, signed Gaussian convergence, source theorems, or an effective onset.'}
out['status'] = 'PASS' if not out['failures'] else 'FAIL'
dest.write_text(json.dumps(out, indent=2)+'\n')
print(out['status'], ': exact 256-cell bounds at both endpoints')
print('g(d):', gd_lo, '<= g(d) <=', gd_hi, '; required (21/10, 11/5)')
print('g(e0) >=', ge_lo, '; required > 7/3')
print('rho <=', rho, '; required <', rho_star, '; margin', rho_star-rho)
print('Paid arc linear margin:', F(1, 16)-2*kappa-2*rho)
print('Failures:', out['failures'], '; complete certificate:', dest)
if out['failures']:
    raise SystemExit(1)
