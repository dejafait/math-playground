"""Independent exact audit of every L716 moment and compact-path cell.

Uses the logarithmic derivative of (1+w)^k exp(S_k(w)) directly,
instead of the original exponential-coefficient/binomial convolution.
Uses a finer grid of interval numbers (2^128), longer Taylor series,
and complex Horner evaluation instead of summing successive powers.
The analytic applicability and unbounded tail are audited in L716.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
original_path = HERE / 'resolvent-tail-certificate-181.json'
original_bytes = original_path.read_bytes()
original = json.loads(original_bytes)
S = 1 << 128
K = 80
U, p, b, A, alpha = F(121, 64), F(3, 10), F(2, 5), F(27, 10), F(11, 8)
failures = []
checks = {}

def require(name, condition):
    checks[name] = bool(condition)
    if not condition:
        failures.append(name)

def val(row):
    return F(row['numerator'], row['denominator'])

def enc(x):
    x = F(x)
    return {'numerator': x.numerator, 'denominator': x.denominator,
            'decimal_preview': float(x)}

def floor_at_scale(x):
    return (x*S).numerator // (x*S).denominator

def ceil_at_scale(x):
    quotient, remainder = divmod((x*S).numerator, (x*S).denominator)
    return quotient + bool(remainder)

def bracket(lo, hi=None):
    lo = F(lo)
    hi = lo if hi is None else F(hi)
    assert lo <= hi
    return floor_at_scale(lo), ceil_at_scale(hi)

def plus(a, c):
    return a[0]+c[0], a[1]+c[1]

def minus(a, c):
    return a[0]-c[1], a[1]-c[0]

def times(a, c):
    products = [F(x*y, S*S) for x in a for y in c]
    return bracket(min(products), max(products))

def ctimes(a, c):
    return (minus(times(a[0], c[0]), times(a[1], c[1])),
            plus(times(a[0], c[1]), times(a[1], c[0])))

def saved_interval(a):
    return [enc(F(a[0], S)), enc(F(a[1], S))]

def contained(a, old):
    return val(old[0]) <= F(a[0], S) <= F(a[1], S) <= val(old[1])

def exponential(r):
    assert 0 <= r <= 1
    upper = sum(((-r)**j / factorial(j) for j in range(45)), F(0))
    lower = upper-r**45/factorial(45)
    return bracket(lower, upper)

def sincos(r):
    assert 0 <= r <= 1
    sin_upper = sum(((-1)**j*r**(2*j+1)/factorial(2*j+1)
                     for j in range(23)), F(0))
    cos_upper = sum(((-1)**j*r**(2*j)/factorial(2*j)
                     for j in range(23)), F(0))
    return (bracket(sin_upper-r**47/factorial(47), sin_upper),
            bracket(cos_upper-r**46/factorial(46), cos_upper))

def logarithm(r):
    assert r > 1
    a = (r-1)/(r+1)
    lower = 2*sum((a**(2*j+1)/F(2*j+1) for j in range(16)), F(0))
    return lower, lower+2*a**33/(33*(1-a*a))

require('original_source_hash', original['script_sha256'] == hashlib.sha256(
    (HERE/'resolvent-tail-certificate-181.py').read_bytes()).hexdigest())
require('original_dimensions', len(original['moment_rows']) == K
        and len(original['grid_rows']) == 401
        and original['parameters']['moment_cutoff'] == K
        and original['parameters']['grid_points'] == 401
        and original['parameters']['scale'] == 1 << 120
        and val(original['parameters']['grid_spacing']) == F(1, 500))

moments = []
moment_rows = []
E = exponential(1/(2*U))
power = bracket(1)
for k in range(1, K+1):
    # D_l is the coefficient of w^(l-1) in the logarithmic derivative.
    D = [F(0)] + [k*(-1)**(l+1) +
         F(l*k*(-1)**(l+1), l+2)/U**(l+1) for l in range(1, k)]
    coeffs = [F(1)]
    for m in range(1, k):
        coeffs.append(sum((D[l]*coeffs[m-l] for l in range(1, m+1)), F(0))/m)
    c = coeffs[k-1]/k
    power = times(power, E)
    interval = times(bracket(c), power)
    old = original['moment_rows'][k-1]
    coefficient_matches = old['k'] == k and c == val(old['rational_coefficient'])
    interval_contained = contained(interval, old['moment_enclosure'])
    require(f'moment_{k}_coefficient', coefficient_matches)
    require(f'moment_{k}_enclosure', interval_contained)
    require(f'moment_{k}_range', 0 < interval[0] <= interval[1] < S)
    moments.append(interval)
    moment_rows.append({'k': k, 'independent_rational_coefficient': enc(c),
                        'independent_enclosure': saved_interval(interval),
                        'coefficient_matches': coefficient_matches,
                        'inside_original_enclosure': interval_contained})

tail, lipschitz, mesh = 5*F(9, 10)**81, F(45, 2), F(9, 400)
require('original_analytic_costs',
        val(original['analytic_bounds']['series_tail']) == tail and
        val(original['analytic_bounds']['G_lipschitz']) == lipschitz and
        val(original['analytic_bounds']['nearest_grid_error']) == mesh)

rows = []
for j in range(401):
    x = F(2, 5)+F(j, 500)
    sine, cosine = sincos(b*x)
    r = exponential(p*x)
    z = times(r, cosine), times(r, (-sine[1], -sine[0]))
    accumulator = bracket(0), bracket(0)
    for m in reversed(moments):
        product = ctimes(z, accumulator)
        accumulator = plus(product[0], m), product[1]
    polynomial = ctimes(z, accumulator)
    result = minus(times(bracket(p), polynomial[0]), times(bracket(b), polynomial[1]))
    old = original['grid_rows'][j]
    is_contained = contained(result, old['partial_sum'])
    require(f'cell_{j}_x', val(old['x']) == x)
    require(f'cell_{j}_enclosure', is_contained)
    require(f'cell_{j}_costs', val(old['upper_in_nearest_cell']) ==
            val(old['partial_sum'][1])+tail+mesh)
    upper = F(result[1], S)+tail+mesh
    require(f'cell_{j}_bound', upper < F(4, 3))
    rows.append({'j': j, 'x': enc(x), 'independent_partial_sum': saved_interval(result),
                 'inside_original_enclosure': is_contained,
                 'upper_with_tail_and_mesh': enc(upper), 'required_upper': enc(F(4, 3))})

old_worst = max(original['grid_rows'], key=lambda r: val(r['upper_in_nearest_cell']))
require('original_worst_row', original['worst_cell'] == old_worst)
old_upper = val(old_worst['upper_in_nearest_cell'])
printed_M = F(143309089951166564695849146572596572514780254635826974054275429128688156899539220671638561517,
              109951162777600000000000000000000000000000000000000000000000000000000000000000000000000000000)
require('canonical_exact_M', old_upper == printed_M and old_upper < F(4, 3))
worst = max(rows, key=lambda r: val(r['upper_with_tail_and_mesh']))
new_upper = val(worst['upper_with_tail_and_mesh'])

log1, log2 = logarithm(F(9, 5)), logarithm(F(201, 121))
omega = [A*(log1[j]-F(4, 5)+F(121, 100)*log2[j]) for j in (0, 1)]
old_omega = [val(x) for x in original['parameters']['omega_enclosure']]
require('omega_contained', old_omega[0] <= omega[0] <= omega[1] <= old_omega[1])
require('whole_bump_endpoints', (omega[0]-F(1, 3000))/A > F(2, 5)
        and (omega[1]+F(1, 3000))/A < F(6, 5))
require('compact_radius', F(exponential(F(3, 25))[1], S) < F(9, 10))
require('unbounded_radius', F(exponential(F(9, 25))[1], S) < F(7, 10))
require('unbounded_root_tail', F(1, 2)*F(7, 10)/(1-F(7, 10)) == F(7, 6)
        and F(7, 6) < F(4, 3))
require('analytic_margins', F(65, 48)-F(4, 3) == F(1, 48)
        and alpha-F(65, 48) == F(1, 48) and alpha-F(4, 3) == F(1, 24)
        and alpha+F(1, 2)*F(9, 10)/(1-F(9, 10)) == F(47, 8))

expected_original_actuals = {
    'moment_lower': min(val(r['moment_enclosure'][0]) for r in original['moment_rows']),
    'moment_upper': max(val(r['moment_enclosure'][1]) for r in original['moment_rows']),
    'whole_bump_x_above_two_fifths': (old_omega[0]-F(1, 3000))/A,
    'whole_bump_x_below_six_fifths': (old_omega[1]+F(1, 3000))/A,
    'entire_compact_G_upper': old_upper,
    'large_x_G_upper': F(7, 6),
    'eventual_integrable_margin': F(1, 48)}
expected_original_thresholds = {
    'moment_lower': ('>', F(0)), 'moment_upper': ('<', F(1)),
    'whole_bump_x_above_two_fifths': ('>', F(2, 5)),
    'whole_bump_x_below_six_fifths': ('<', F(6, 5)),
    'compact_radius': ('<', F(9, 10)), 'large_x_radius': ('<', F(7, 10)),
    'entire_compact_G_upper': ('<', F(4, 3)),
    'large_x_G_upper': ('<', F(4, 3)),
    'eventual_integrable_margin': ('>=', F(1, 48))}
require('original_check_names', set(original['checks']) == set(expected_original_thresholds))
for name, row in original['checks'].items():
    actual, required, relation = val(row['actual']), val(row['required']), row['relation']
    expected_relation, expected_required = expected_original_thresholds[name]
    require(f'original_{name}_threshold', relation == expected_relation and required == expected_required)
    if name in expected_original_actuals:
        require(f'original_{name}_actual', actual == expected_original_actuals[name])
    else:
        # Recompute the exact original degree-40 upper endpoint and rounding.
        argument = F(3, 25) if name == 'compact_radius' else F(9, 25)
        upper = sum(((-argument)**j/factorial(j) for j in range(41)), F(0))
        scaled = upper*(1 << 120)
        quotient, remainder = divmod(scaled.numerator, scaled.denominator)
        require(f'original_{name}_actual', actual == F(quotient+bool(remainder), 1 << 120))
    passed = {'<': actual < required, '>': actual > required,
              '<=': actual <= required, '>=': actual >= required}[relation]
    require(f'original_{name}_truth', passed and row['passed'] is True)
require('original_no_failures', original['failures'] == [])
require('original_preserved', original_path.read_bytes() == original_bytes)

result = {
    'purpose': __doc__,
    'audit_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'original_certificate_sha256': hashlib.sha256(original_bytes).hexdigest(),
    'original_script_sha256': original['script_sha256'],
    'parameters': {'scale': S, 'moments': K, 'grid_points': len(rows)},
    'moment_rows': moment_rows, 'grid_rows': rows,
    'omega_enclosure': [enc(x) for x in omega],
    'bounds': {'original_M': enc(old_upper), 'independent_M': enc(new_upper),
               'required_M': enc(F(4, 3)), 'series_tail': enc(tail),
               'mesh_cost': enc(mesh), 'unbounded_G': enc(F(7, 6)),
               'eventual_majorant_decay': enc(F(1, 48)),
               'limiting_denominator_real_part': enc(F(1, 24)),
               'limiting_ratio_lower_modulus': enc(F(8, 47))},
    'worst_cell': worst, 'checks': checks, 'failures': failures,
    'qualifications': ['All exact input rows were consumed and verified; decimal previews are unused.',
                       'Analytic derivation and uniform-in-n passage require the canonical L716 audit.',
                       'No effective onset, signed bump rate or Xi conclusion.']}
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(result, indent=2)+'\n')
print(f'Moments: {K}/{K}; cells: {len(rows)}/401; exact checks: {sum(checks.values())}/{len(checks)}')
print(f'Compact bound: actual {float(new_upper):.14g} < required {float(F(4, 3)):.14g}')
print(f'Unbounded bound: actual 7/6 < required 4/3; eventual damping: actual 1/48 >= required 1/48')
print(f'Failures: {failures}; original certificate preserved; full certificate: {output}')
if failures:
    raise SystemExit(1)
