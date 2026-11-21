#!/usr/bin/env python3
"""Fixed actual-theta degree-six counts; exact rational interval arithmetic.

Run from riemann: python3 scripts/pollaczek/actual_theta_three_radius_2072.py
Uses the wider display intervals proved in C530a, without quadrature replay.
No radius search, precision change, midpoint roots or floating arithmetic.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'scripts/pollaczek/actual-theta-three-radius-2072.json'
INPUT = ROOT / 'lemmas/C530a-actual-theta-four-coefficient-enclosures.md'
TEMPLATE = ROOT / 'lemmas/L530-two-atom-pollaczek-outward-flow-root-loss.md'
TARGET = ('Certify the real-root counts of the actual-theta degree-six p_r '
          "at r=9/32,1/3,1 using audited C530a enclosures and L530's cubic "
          'template, or record an interval-sign obstruction.')
DISPLAY = [
    ('0.48099000592797654', '0.48099000592798365'),
    ('0.01941821719853482', '0.01941821719854973'),
    ('0.0020319448877264396', '0.0020319448877538714'),
    ('0.00031408664874727607', '0.00031408664879341623'),
]


def singleton(x):
    return F(x), F(x)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    products = [a*b for a in x for b in y]
    return min(products), max(products)


def scale(x, q):
    return mul(x, singleton(q))


def power(x, n):
    result = singleton(1)
    for _ in range(n):
        result = mul(result, x)
    return result


def divide(x, y):
    if y[0] <= 0 <= y[1]:
        raise ArithmeticError('division interval contains zero')
    return mul(x, (1/y[1], 1/y[0]))


def sign(x):
    return 1 if x[0] > 0 else -1 if x[1] < 0 else 0


def encode(x):
    return {'lower': str(x[0]), 'upper': str(x[1]), 'strict_sign': sign(x)}


def decimal_hull(x, digits):
    """Exact outward decimal display on a fixed reporting grid only."""
    grid = 10**digits
    lo = (x[0]*grid).numerator // (x[0]*grid).denominator
    hi = -((-x[1]*grid).numerator // (-x[1]*grid).denominator)

    def display(n):
        a, b = divmod(abs(n), grid)
        return ('-' if n < 0 else '') + f'{a}.{b:0{digits}d}'

    hull = (F(lo, grid), F(hi, grid))
    assert hull[0] <= x[0] <= x[1] <= hull[1]
    return {'lower': display(lo), 'upper': display(hi)}


def main():
    checks = {}

    def check(name, ok):
        checks[name] = bool(ok)

    source_text = INPUT.read_text()
    for j, endpoints in enumerate(DISPLAY):
        check(f'c{2*j}_display_endpoints_present_in_C530a',
              all(endpoint in source_text for endpoint in endpoints))
    intervals = [(F(lo), F(hi)) for lo, hi in DISPLAY]
    for j, interval in enumerate(intervals):
        check(f'c{2*j}_positive_ordered', 0 < interval[0] <= interval[1])
    check('positive_normalizing_denominator', intervals[0][0] > 0)
    if not all(checks.values()):
        raise ArithmeticError('source endpoint or normalization check failed')

    # m_0 is exactly 1, rather than the wider quotient interval c0/c0.
    ratios = [singleton(1)] + [divide(x, intervals[0]) for x in intervals[1:]]
    records = []
    for radius in [F(9, 32), F(1, 3), F(1)]:
        s = radius**2
        A, B, C = [scale(ratios[j], s**j) for j in range(1, 4)]
        d = add(singleton(1), add(scale(A, F(3, 4)),
                add(scale(B, F(21, 32)), scale(C, F(77, 128)))))
        c = add(scale(A, F(-1, 2)), add(scale(B, F(-17, 24)),
                scale(C, F(-2401, 2880))))
        b = add(scale(B, F(1, 24)), scale(C, F(25, 288)))
        a = scale(C, F(-1, 720))
        terms = {
            'b2_c2': mul(power(b, 2), power(c, 2)),
            'minus4_a_c3': scale(mul(a, power(c, 3)), -4),
            'minus4_b3_d': scale(mul(power(b, 3), d), -4),
            'minus27_a2_d2': scale(mul(power(a, 2), power(d, 2)), -27),
            'plus18_a_b_c_d': scale(mul(mul(a, b), mul(c, d)), 18),
        }
        delta = singleton(0)
        for term in terms.values():
            delta = add(delta, term)
        coefficient_signs = [sign(x) for x in (d, c, b, a)]
        required_signs = [1, -1, 1, -1]
        signs_decisive = coefficient_signs == required_signs
        nonzero_degree_and_constant = sign(a) != 0 and sign(d) != 0
        decisive = signs_decisive and nonzero_degree_and_constant and sign(delta) != 0
        count = (6 if sign(delta) == 1 else 2) if decisive else None
        label = str(radius)
        check(f'{label}_coefficient_signs_strict', signs_decisive)
        check(f'{label}_degree_and_constant_nonzero', nonzero_degree_and_constant)
        check(f'{label}_discriminant_strict', sign(delta) != 0)
        records.append({
            'radius': label, 'squared_radius': str(s),
            'scaled_moments': dict(zip(('A', 'B', 'C'), map(encode, (A, B, C)))),
            'cubic_coefficients_ascending': dict(zip(('d', 'c', 'b', 'a'),
                                                   map(encode, (d, c, b, a)))),
            'discriminant_terms': {key: encode(value) for key, value in terms.items()},
            'discriminant': encode(delta),
            'decimal_hulls': {
                'coefficients': dict(zip(('d', 'c', 'b', 'a'),
                                         [decimal_hull(x, 18) for x in (d, c, b, a)])),
                'discriminant': decimal_hull(delta, 30),
            },
            'required_coefficient_signs': required_signs,
            'actual_coefficient_signs': coefficient_signs,
            'real_t_root_count': count,
            'nonreal_t_root_count': 6-count if decisive else None,
            'all_six_t_roots_simple': True if decisive else None,
            'decision': 'CERTIFIED' if decisive else 'INTERVAL_SIGN_OBSTRUCTION',
        })
    data = {
        'target': TARGET,
        'arithmetic': 'CPython Fraction: exact integers and rational endpoints; no interval rounding',
        'coefficient_backend_trust': 'Inherited C530a CPython/libmpdec contract; no quadrature replay',
        'input_sha256': hashlib.sha256(INPUT.read_bytes()).hexdigest(),
        'template_sha256': hashlib.sha256(TEMPLATE.read_bytes()).hexdigest(),
        'input_display_strings': DISPLAY,
        'coefficient_intervals': {f'c{2*j}': encode(x) for j, x in enumerate(intervals)},
        'normalizing_denominator': encode(intervals[0]),
        'normalized_moments': {f'm{j}': encode(x) for j, x in enumerate(ratios)},
        'normalization_note': 'Shared c0 correlations are discarded only by enlarging to a box; m0=1 exactly.',
        'radii': records,
        'checks': checks,
        'failures': [name for name, passed in checks.items() if not passed],
        'scope': 'Degree six, exactly three radii; no all-degree or Xi-transfer assertion',
    }
    OUT.write_text(json.dumps(data, indent=2) + '\n')
    for record in records:
        print(f"r={record['radius']}: {record['decision']}; "
              f"real={record['real_t_root_count']}, required for hyperbolicity=6; "
              f"coefficient signs={record['actual_coefficient_signs']}; "
              f"Delta enclosure={record['decimal_hulls']['discriminant']}")
    print(f'checks={len(checks)}, failures={data["failures"]}; certificate={OUT.relative_to(ROOT)}')
    return 0 if not data['failures'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
