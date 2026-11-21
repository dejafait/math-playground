#!/usr/bin/env python3
"""Exact rational certificate for the highest-moment lattice contour.

All enclosures and pass/fail comparisons use integers or Fractions. The
analytic proof supplies the residue identity and derivative bounds. The
series-enclosure implementation follows the notebook's earlier contour
certificates, with the present radial term and lattice damping retained.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

SCALE, SAVE_SCALE, DEGREE = 10**40, 10**12, 100
d, R, U = Q(5, 4), Q(11, 8), Q(121, 64)
b, r, alpha = Q(9, 100), Q(9, 20), Q(27, 10)
REQUIRED = -Q(7, 200)
V_DEN = 80
POSITION_STEP = Q(3, 100)
failures = []


def add(a, c):
    return a[0]+c[0], a[1]+c[1]


def mul(a, c):
    return (a[0]*c, a[1]*c) if c >= 0 else (a[1]*c, a[0]*c)


def log_unit(v):
    assert 1 <= v <= 2
    z = (v-1)/(v+1)
    term, total = z, Q(0)
    for j in range(32):
        total += 2*term/(2*j+1)
        term *= z*z
    return total, total+2*term/(65*(1-z*z))


LOG2 = log_unit(Q(2))


def logq(v):
    assert v > 0
    k = 0
    while v < 1:
        v *= 2
        k -= 1
    while v > 2:
        v /= 2
        k += 1
    return add(log_unit(v), mul(LOG2, k))


def floor_scaled(v, scale=SCALE):
    return (v.numerator*scale)//v.denominator


def ceil_scaled(v):
    return -((-v.numerator*SAVE_SCALE)//v.denominator)


def cmul(a, c):
    return a[0]*c[0]-a[1]*c[1], a[0]*c[1]+a[1]*c[0]


def series_fixed(z):
    """Floored Re sum_{k=1}^100 z^k/(k(k+1))."""
    assert z[0]*z[0]+z[1]*z[1] <= Q(81, 100)
    zr, zi = floor_scaled(z[0]), floor_scaled(z[1])
    assert abs(zr)+abs(zi) < 3*SCALE//2
    pr, pi, total = SCALE, 0, 0
    for k in range(1, DEGREE+1):
        pr, pi = (pr*zr-pi*zi)//SCALE, (pr*zi+pi*zr)//SCALE
        total += pr//(k*(k+1))
    return total


round_error = (6*(Q(3, 2)**DEGREE-1)+DEGREE)/SCALE
tail_error = Q(9, 10)**(DEGREE+1) / Q((DEGREE+1)*(DEGREE+2), 10)
four_series_error = 4*(round_error+tail_error)
interpolation_error = Q(8, 8)*POSITION_STEP**2+Q(130, 8*V_DEN**2)

points = []
for sign in (-1, 1):
    for j in range(-V_DEN, V_DEN+1):
        v = Q(j, V_DEN)
        ur, ui = sign*(1-v*v)/(1+v*v), 2*v/(1+v*v)
        # These two series depend on the angle only.
        base = -series_fixed((-ur/d, -ui/d)) + series_fixed((-d*ur/U, d*ui/U))
        points.append((sign, j, ur, ui, base))

rows = []
global_upper = None
max_witness = None


def certify_line(kind, s, y):
    global global_upper, max_witness
    a = (-d+s, y)
    a2 = a[0]*a[0]+a[1]*a[1]
    inverse_a = (a[0]/a2, -a[1]/a2)
    constant = add(mul(logq(d*d/a2), Q(1, 2)), mul(logq(a2/U), Q(1, 6)))
    const_upper = constant[1]-Q(20, 9)*max(s, 0)+four_series_error
    for sign in (-1, 1):
        saved = []
        for sigma, j, ur, ui, base in points:
            if sigma != sign:
                continue
            approximation = (series_fixed(cmul((ur, ui), inverse_a))+base
                             -series_fixed(cmul(a, (ur/U, -ui/U))))
            saved.append(ceil_scaled(const_upper+Q(approximation, SCALE)))
        sampled_upper = Q(max(saved), SAVE_SCALE)
        certified_upper = sampled_upper+interpolation_error
        row = {'kind': kind, 's': str(s), 'y': str(y), 'real_part_sign': sign,
               'v_denominator': V_DEN, 'sample_scale': SAVE_SCALE,
               'sample_upper_numerators': saved,
               'sampled_max_upper': str(sampled_upper),
               'interpolation_error': str(interpolation_error),
               'certified_upper': str(certified_upper)}
        rows.append(row)
        if global_upper is None or certified_upper > global_upper:
            global_upper = certified_upper
            max_witness = {'row_index': len(rows)-1, 'kind': kind, 's': str(s),
                           'y': str(y), 'real_part_sign': sign,
                           'v_numerator': saved.index(max(saved))-V_DEN,
                           'sampled_max_upper': str(sampled_upper),
                           'interpolation_error': str(interpolation_error),
                           'certified_upper': str(certified_upper)}
        if certified_upper >= REQUIRED:
            failures.append(f'row {len(rows)-1}: contour upper bound fails')


for s in (-b, b):
    for j in range(16):
        certify_line('vertical', s, j*POSITION_STEP)
for j in range(7):
    certify_line('horizontal', -b+j*POSITION_STEP, r)

checks = [
    ('maximum parameter modulus squared', (d+b)**2+r*r, '<', Q(9, 4)),
    ('minimum parameter modulus', d-b, '>', Q(1)),
    ('inverse parameter modulus', 1/(d-b), '<', Q(9, 10)),
    ('parameter over U modulus', Q(3, 2)/U, '<', Q(9, 10)),
    ('sum f_t absolute bound', 4+Q(25, 4)+Q(96, 25)+Q(80, 41), '<', Q(17)),
    ('radial missing-power charge', mul(logq(U/(d-b)**2), Q(1, 2))[1], '<', Q(1)),
    ('g first y derivative', Q(25, 4)+Q(64, 25)+Q(25, 87), '<', Q(10)),
    ('g second position derivative', Q(625, 116)+Q(4096, 3025)+Q(625, 2523), '<', Q(8)),
    ('g second v derivative', 8*(4+Q(25, 4)+Q(96, 25)+Q(80, 41)), '<', Q(130)),
    ('fixed-point rounding error', round_error, '<', Q(1, 10**20)),
    ('four-series error', four_series_error, '<', Q(1, 10**6)),
    ('finite product and height charge', 17+1+10*Q(27, 20), '<', Q(32)),
    ('contour length over h per n', 4*(b+r)/alpha, '=', Q(4, 5)),
    ('anchor log lower bound', logq(Q(11, 10))[0], '>', Q(19, 200)),
    ('anchor exponent gap', Q(19, 600)-Q(1, 32), '=', Q(1, 2400)),
    ('remainder exponent gap', Q(7, 200)-Q(1, 32), '=', Q(3, 800)),
    ('contour maximum', global_upper, '<', REQUIRED),
]
check_rows = []
for name, lhs, op, rhs in checks:
    passed = {'<': lhs < rhs, '>': lhs > rhs, '=': lhs == rhs}[op]
    check_rows.append({'name': name, 'lhs': str(lhs), 'op': op, 'rhs': str(rhs), 'passed': passed})
    if not passed:
        failures.append(name)

# Enumerate and check the complete mesh, including the kink s=0.
expected_positions = [(kind, str(s), str(y), sign)
                      for kind, positions in [
                          ('vertical', [(s, j*POSITION_STEP) for s in (-b, b) for j in range(16)]),
                          ('horizontal', [(-b+j*POSITION_STEP, r) for j in range(7)])]
                      for s, y in positions for sign in (-1, 1)]
actual_positions = [(z['kind'], z['s'], z['y'], z['real_part_sign']) for z in rows]
mesh_pass = (actual_positions == expected_positions and len(rows) == 78
             and all(len(z['sample_upper_numerators']) == 161 for z in rows)
             and 15*POSITION_STEP == r and 6*POSITION_STEP == 2*b
             and -b+3*POSITION_STEP == 0)
if not mesh_pass:
    failures.append('complete mesh coverage')

output = Path(__file__).with_suffix('.json')
certificate = {
    'status': 'PASS' if not failures else 'FAIL', 'failures': failures,
    'scope': 'All boundary positions and all angular u via the stated interpolation proof.',
    'required_upper': str(REQUIRED), 'actual_upper': str(global_upper),
    'maximum': max_witness, 'checks': check_rows,
    'mesh': {'passed': mesh_pass, 'row_count': len(rows),
             'sample_count': sum(len(z['sample_upper_numerators']) for z in rows),
             'position_step': str(POSITION_STEP), 'v_step': str(Q(1, V_DEN)),
             'interpolation_error': str(interpolation_error),
             'all_nonnegative_y_and_both_semicircles': True,
             'horizontal_kink_is_a_mesh_line': True},
    'series': {'scale': SCALE, 'degree': DEGREE, 'save_scale': SAVE_SCALE,
               'round_error': str(round_error), 'tail_error': str(tail_error),
               'four_series_error': str(four_series_error)},
    'rows': rows,
}
output.write_text(json.dumps(certificate, indent=2)+'\n')
print(f"status={certificate['status']}; all {certificate['mesh']['sample_count']} rational samples "
      f"and {len(checks)} arithmetic checks processed")
print(f"actual contour upper={global_upper} ({float(global_upper):.12g}); required < {REQUIRED}")
print(f"failures={failures}; full certificate: {output}")
raise SystemExit(1 if failures else 0)
