"""Fixed C040c floor test; exact rationals, no parameter/sample search.

For x >= 0 Taylor's integral remainder gives S_41(x) <= exp(-x)
<= S_40(x), where S_n(x) = sum_{j=0}^n (-x)^j/j!.
The analytical Mellin identity and uniqueness are proved in C040d.
"""
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as Q
import json
from pathlib import Path


def bounds(x):
    term = Q(1)
    terms = [term]
    for j in range(1, 42):
        term *= -x / j
        terms.append(term)
    upper = sum(terms[:41], Q(0))
    lower = upper + terms[41]
    return lower, upper, terms


def rational(x):
    return f"{x.numerator}/{x.denominator}"


def outward(x, rounding):
    with localcontext() as ctx:
        ctx.prec = 100
        return str((Decimal(x.numerator) / Decimal(x.denominator)).quantize(
            Decimal('0.000000000001'), rounding=rounding))


a = Q(1, 20)
eta = Q(15287777, 250000000)
lambda_lo, lambda_hi = Q(4329, 1000), Q(4331, 1000)
arguments = {
    'fast': Q(199, 2) * a,
    'half': a / 2,
    'unit': a,
    'floor_at_lambda_lo': lambda_lo * a,
    'floor_at_lambda_hi': lambda_hi * a,
}
enclosures = {name: bounds(x) for name, x in arguments.items()}
k_lo = enclosures['fast'][0] + enclosures['half'][0] - enclosures['unit'][1]
k_hi = enclosures['fast'][1] + enclosures['half'][1] - enclosures['unit'][0]
floor_lo = eta * enclosures['floor_at_lambda_hi'][0]
floor_hi = eta * enclosures['floor_at_lambda_lo'][1]
d_lo, d_hi = k_lo - floor_hi, k_hi - floor_lo
intervals = {'density_at_a': (k_lo, k_hi), 'floor_uniform': (floor_lo, floor_hi),
             'deficit_uniform': (d_lo, d_hi)}
display = {name: [outward(lo, ROUND_FLOOR), outward(hi, ROUND_CEILING)]
           for name, (lo, hi) in intervals.items()}
checks = {
    'nonnegative_arguments': all(x >= 0 for x in arguments.values()),
    'ordered_exponential_bounds': all(v[0] <= v[1] for v in enclosures.values()),
    'positive_exponential_lower_bounds': all(v[0] > 0 for v in enclosures.values()),
    'lambda_order_and_eta_positive': 0 < lambda_lo < lambda_hi and eta > 0,
    'ordered_density_bounds': k_lo <= k_hi,
    'ordered_floor_bounds': floor_lo <= floor_hi,
    'ordered_deficit_bounds': d_lo <= d_hi,
    'uniform_upper_below_required_zero': d_hi < 0,
    'uniform_deficit_in_minus_00184_minus_00181': Q(-184, 10000) < d_lo <= d_hi < Q(-181, 10000),
    'displayed_decimal_enclosures_verified_as_exact_rationals': all(
        Q(display[name][0]) <= lo <= hi <= Q(display[name][1])
        for name, (lo, hi) in intervals.items()),
}
certificate = {
    'target': 'C040c fixed density, a=1/20, prescribed lambda enclosure; no retuning',
    'method': 'Taylor integral remainder: odd S_41 lower, even S_40 upper for exp(-x), x>=0',
    'parameters': {'a': rational(a), 'eta': rational(eta),
                   'lambda': [rational(lambda_lo), rational(lambda_hi)]},
    'exponentials': {name: {'x': rational(arguments[name]),
                          'lower': rational(v[0]), 'upper': rational(v[1]),
                          'terms_j_0_through_41': [rational(t) for t in v[2]]}
                     for name, v in enclosures.items()},
    'density_at_a': [rational(k_lo), rational(k_hi)],
    'floor_uniform': [rational(floor_lo), rational(floor_hi)],
    'deficit_uniform': [rational(d_lo), rational(d_hi)],
    'displayed_outward_enclosures': display,
    'required_upper_threshold': '0/1',
    'checks': checks,
    'failures': [name for name, ok in checks.items() if not ok],
}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(certificate, indent=2) + '\n')
for label, name in [('k_F(1/20)', 'density_at_a'),
                    ('floor (uniform)', 'floor_uniform'),
                    ('D(lambda) (uniform)', 'deficit_uniform')]:
    print(f'{label}: [{display[name][0]}, {display[name][1]}]')
print(f'Checks: {sum(checks.values())}/{len(checks)}; required upper threshold: 0')
print(f'Failures: {certificate["failures"]}; certificate: {path.relative_to(Path.cwd())}')
assert all(checks.values()), certificate['failures']
