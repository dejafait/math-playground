"""Exact rational bounds for the outer-half Chebyshev response stop.

No floating point is used in any test. Adaptive boxes cover the complete
rectangle (t,c) in [0,1/2] x [-1,1]; every accepted box and bound is saved.
"""

import json
from fractions import Fraction as F
from pathlib import Path


def interval(a, b=None):
    return (F(a), F(a if b is None else b))


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    vals = [x * y for x in a for y in b]
    return min(vals), max(vals)


def div(a, b):
    if b[0] <= 0 <= b[1]:
        raise ZeroDivisionError('interval divisor contains zero')
    return mul(a, (1 / b[1], 1 / b[0]))


def square(a):
    return (F(0) if a[0] <= 0 <= a[1] else min(a[0]**2, a[1]**2),
            max(a[0]**2, a[1]**2))


R, d, U, h, Q = F(11, 8), F(5, 4), F(121, 64), F(237, 200), F(21, 20)
one = interval(1)


def bx_squared(t, c):
    # |b_t(-d)|^2, with c=Re(u).
    t2 = square(t)
    num = mul(interval(U), add(add(interval(d*d), t2), mul(interval(2*d), mul(t, c))))
    den = add(add(interval(U*U), mul(interval(d*d), t2)), mul(interval(2*U*d), mul(t, c)))
    return div(num, den)


def box_bounds(t, c):
    t2 = square(t)
    a = add(mul(interval(h/U), t2), mul(t, c))
    b = mul(interval(R), sub(one, div(t2, interval(U))))
    cc = add(interval(h), mul(t, c))
    k = div(mul(bx_squared(t, c), bx_squared(add(t, interval(F(1, 2))), c)), interval(Q*Q))
    lhs = sub(cc, mul(a, k))
    gap = sub(square(lhs), mul(square(b), k))
    return {'K': k, 'C_minus_AK': lhs, 'squared_gap': gap}


def serial(v):
    if isinstance(v, F):
        return str(v)
    if isinstance(v, dict):
        return {k: serial(w) for k, w in v.items()}
    if isinstance(v, (list, tuple)):
        return [serial(w) for w in v]
    return v


leaves, failures = [], []
stack = [(interval(0, F(1, 2)), interval(-1, 1), '')]
max_depth = 22
while stack:
    t, c, address = stack.pop()
    try:
        bounds = box_bounds(t, c)
        ok = (bounds['K'][0] > 0 and bounds['K'][1] < 1
              and bounds['C_minus_AK'][0] > 0 and bounds['squared_gap'][0] > 0)
    except ZeroDivisionError:
        bounds, ok = {}, False
    if ok:
        leaves.append({'address': address, 't': t, 'c': c, 'bounds': bounds})
        continue
    if len(address) == max_depth:
        failures.append({'address': address, 't': t, 'c': c, 'bounds': bounds})
        continue
    # Deterministic bisection: alternate the two coordinates.
    if len(address) % 2 == 0:
        mid = (t[0] + t[1]) / 2
        stack.append(((mid, t[1]), c, address + '1'))
        stack.append(((t[0], mid), c, address + '0'))
    else:
        mid = (c[0] + c[1]) / 2
        stack.append((t, (mid, c[1]), address + '1'))
        stack.append((t, (c[0], mid), address + '0'))


# Check that the saved dyadic leaves form a complete prefix partition;
# this is additional to the exhaustive recursive traversal above.
addresses = {v['address'] for v in leaves}
partition_ok = len(addresses) == len(leaves)
while addresses and '' not in addresses:
    depth = max(map(len, addresses))
    deepest = sorted(a for a in addresses if len(a) == depth)
    for a in deepest:
        if a not in addresses:
            continue
        sibling = a[:-1] + ('1' if a[-1] == '0' else '0')
        if sibling not in addresses:
            partition_ok = False
            break
        addresses.remove(a)
        addresses.remove(sibling)
        if a[:-1] in addresses:
            partition_ok = False
            break
        addresses.add(a[:-1])
    if not partition_ok:
        break
partition_ok = partition_ok and addresses == {''}

r, s, ell = F(27, 50), F(13, 200), F(34, 25)
r0sq = d*d + r*r
ellipse_max_sq = d*d + r*r + s*s*(1 + d*d/(r*r))
arc_rate = F(47, 1000) - F(45, 3784)
# asinh(s/r) >= (s/r)/sqrt(1+(s/r)^2), and sqrt(1+(13/108)^2)<101/100.
rho_log_lower = F(13, 108) * F(100, 101)
error_rate_lower = F(2, 3)*rho_log_lower - F(1, 40)

min_bounds = {
    'K_lower': min(v['bounds']['K'][0] for v in leaves),
    'K_upper': max(v['bounds']['K'][1] for v in leaves),
    'C_minus_AK_lower': min(v['bounds']['C_minus_AK'][0] for v in leaves),
    'squared_gap_lower': min(v['bounds']['squared_gap'][0] for v in leaves),
}
checks = {
    'all_boxes_pass': not failures,
    'complete_dyadic_partition': partition_ok,
    'K_strictly_between_zero_and_one': min_bounds['K_lower'] > 0 and min_bounds['K_upper'] < 1,
    'positive_unsquared_side': min_bounds['C_minus_AK_lower'] > 0,
    'positive_squared_gap': min_bounds['squared_gap_lower'] > 0,
    'pole_clearance': r0sq < (R-F(1, 100))**2,
    'arc_radius_lower': r0sq > ell*ell,
    'arc_denominator_margin': (U-r0sq)/(2*R) > F(1, 100),
    'ellipse_denominator_margin': (U-ellipse_max_sq)/(2*R) > F(1, 300),
    'low_factor_minimum': R*(ell-F(1, 2))/(U-ell*F(1, 2)) == F(1892, 1937),
    'arc_rate_beats_7_over_200': arc_rate > F(7, 200),
    'square_root_upper': 1+F(13, 108)**2 < F(101, 100)**2,
    'error_rate_beats_7_over_200': error_rate_lower > F(7, 200),
    'seven_over_200_beats_target': F(7, 200) > F(1, 32),
    'outer_shift_derivative_bound': 1/(d-1)+d/(U-d) < 6,
    'quadrature_denominator_for_n_ge_15': F(2, 3)*15*rho_log_lower > 1,
}
certificate = {
    'status': 'EXACT_RATIONAL_CERTIFICATE' if all(checks.values()) else 'FAILED',
    'domain': {'t': ['0', '1/2'], 'c': ['-1', '1'], 'Q': Q, 'half_plane_h': h},
    'leaf_count': len(leaves), 'maximum_depth_used': max(map(len, (v['address'] for v in leaves))),
    'checks': checks, 'minimum_bounds': min_bounds, 'failures': failures,
    'rates_and_geometry': {
        'arc_radius_squared': r0sq, 'ellipse_maximum_radius_squared': ellipse_max_sq,
        'arc_exponent_lower': arc_rate, 'ellipse_log_rho_lower': rho_log_lower,
        'quadrature_exponent_lower': error_rate_lower,
        'claimed_response_exponent': F(7, 200), 'required_exponent': F(1, 32),
        'exponent_margin': F(7, 200)-F(1, 32),
    },
    'development_failure': {
        'failed_claim': '(2/3)*9*(1300/10908)>1',
        'actual_value': F(2, 3)*9*rho_log_lower,
        'repair': 'State the countersequence for odd m>=5 and n=3m>=15; no n=9 claim is needed.',
        'original_certificate': 'scripts/one-sided-hankel/angular-outer-half-certificate-first-pass.json',
    },
    'leaves': leaves,
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(serial(certificate), indent=2) + '\n')
print('Exact pair boxes:', len(leaves), 'failures:', len(failures), 'max depth:', certificate['maximum_depth_used'])
print('Checks:', sum(checks.values()), '/', len(checks))
print('Response exponent:', F(7, 200), 'required:', F(1, 32), 'margin:', F(7, 200)-F(1, 32))
print('Arc lower rate:', arc_rate, 'quadrature lower rate:', error_rate_lower)
print('Failed checks:', [name for name, passed in checks.items() if not passed])
print('Full exact certificate:', out)
if not all(checks.values()):
    raise SystemExit(1)
