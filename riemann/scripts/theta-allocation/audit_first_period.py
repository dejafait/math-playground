"""Independent inclusion audit of the existing C609a certificate only.

No imports from the calculation or its arithmetic implementation. All
saved cells are checked; no new mesh, period, frequency or sign search.
Decimal's specified operations remain imported, not formally verified.
"""
import decimal
import hashlib
import json
import platform
import sys
import time
from collections import Counter
from pathlib import Path

D = decimal.Decimal
DOWN = decimal.Context(prec=55, rounding=decimal.ROUND_FLOOR,
                       Emin=-999999999, Emax=999999999)
UP = decimal.Context(prec=55, rounding=decimal.ROUND_CEILING,
                     Emin=-999999999, Emax=999999999)
NEAR = decimal.Context(prec=55, rounding=decimal.ROUND_HALF_EVEN,
                       Emin=-999999999, Emax=999999999)
COUNTS = Counter()
TELEMETRY = {'divisions': 0, 'minimum_denominator_magnitude': None,
             'exp_calls': 0, 'kernel_calls': 0}


class Box:
    def __init__(self, low, high=None):
        self.low, self.high = D(low), D(low if high is None else high)
        assert self.low.is_finite() and self.high.is_finite()
        assert self.low <= self.high

    def __add__(self, other):
        other = box(other)
        return Box(DOWN.add(self.low, other.low), UP.add(self.high, other.high))

    __radd__ = __add__

    def __neg__(self):
        return Box(self.high.copy_negate(), self.low.copy_negate())

    def __sub__(self, other):
        return self + (-box(other))

    def __rsub__(self, other):
        return box(other) - self

    def __mul__(self, other):
        other = box(other)
        products = [(a, b) for a in (self.low, self.high)
                    for b in (other.low, other.high)]
        return Box(min(DOWN.multiply(a, b) for a, b in products),
                   max(UP.multiply(a, b) for a, b in products))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = box(other)
        assert other.low > 0 or other.high < 0
        magnitude = min(other.low.copy_abs(), other.high.copy_abs())
        previous = TELEMETRY['minimum_denominator_magnitude']
        TELEMETRY['minimum_denominator_magnitude'] = (
            magnitude if previous is None else min(magnitude, previous))
        TELEMETRY['divisions'] += 1
        return self * Box(DOWN.divide(D(1), other.high), UP.divide(D(1), other.low))

    def exp(self):
        TELEMETRY['exp_calls'] += 1
        return Box(NEAR.next_minus(NEAR.exp(self.low)),
                   NEAR.next_plus(NEAR.exp(self.high)))

    def square(self):
        if self.low >= 0:
            return Box(DOWN.multiply(self.low, self.low), UP.multiply(self.high, self.high))
        if self.high <= 0:
            return (-self).square()
        return Box(0, max(UP.multiply(self.low, self.low), UP.multiply(self.high, self.high)))

    def magnitude(self):
        return max(self.low.copy_abs(), self.high.copy_abs())

    def radius(self):
        return UP.divide(UP.subtract(self.high, self.low), D(2))

    def pair(self):
        return [str(self.low), str(self.high)]


def box(value):
    return value if isinstance(value, Box) else Box(value)


def read_pair(value):
    return Box(*value)


def check(condition, label):
    if not condition:
        raise AssertionError(label)
    COUNTS[label.split(':')[0]] += 1


def inclusion(saved, required, label):
    check(saved.low <= required.low <= required.high <= saved.high, label)


def pi_bound():
    def arctan(q):
        t = Box(1)/q
        term, result = t, Box(0)
        for j in range(150):
            result += ((-1)**j)*term/(2*j+1)
            term *= t.square()
        error = (term/301).high
        return result + Box(error.copy_negate(), error)
    return 16*arctan(5)-4*arctan(239)


# These are the independently differentiated polynomials displayed in L609.
POLYS = ((0, -12, 8), (0, -30, 60, -16), (0, -75, 330, -224, 32))


def kernel(u, order, pi, tails):
    check(0 <= u.low <= u.high <= 8, 'kernel_domain')
    TELEMETRY['kernel_calls'] += 1
    scale, prefactor = (2*u).exp(), (u/2).exp()
    values = [Box(0) for _ in range(order+1)]
    for n in range(1, 6):
        v = pi*(n*n)*scale
        factor = prefactor*(-v).exp()
        for j in range(order+1):
            coefficients = POLYS[j]
            p = Box(coefficients[-1])
            for coefficient in reversed(coefficients[:-1]):
                p = p*v+coefficient
            values[j] += factor*p
    values[0] += Box(0, tails[0])
    for j in range(1, order+1):
        values[j] += Box(tails[j].copy_negate(), tails[j])
    return values


def trig(t):
    check(t.magnitude() <= 5, 'direct_trig_domain')
    sine, cosine, st, ct = Box(0), Box(0), t, Box(1)
    for j in range(50):
        sine += st
        cosine += ct
        st = -st*t.square()/((2*j+2)*(2*j+3))
        ct = -ct*t.square()/((2*j+1)*(2*j+2))
    factorial = 1
    for j in range(1, 101):
        factorial *= j
    error = (Box(5**100)/factorial).high
    return sine+Box(error.copy_negate(), error), cosine+Box(error.copy_negate(), error)


def audit(c, report):
    n, m = 65536, 4096
    check(c['caps'] == {'outer_cells': n, 'tail_midpoint_cells': m, 'precision': 45,
                       'theta_terms': 5, 'cutoff': 8, 'kernel_calls': n+2*m,
                       'direct_sincos_calls': 4, 'restart_or_sweep': False}, 'fixed_caps')
    ar, enc, err = c['arithmetic'], c['enclosures'], c['error_budget']
    pi = pi_bound()
    inclusion(read_pair(ar['pi']), pi, 'pi')
    a, d, td = map(read_pair, (ar['endpoint_A'], ar['outer_width'], ar['tail_width']))
    inclusion(a, 2*read_pair(ar['pi'])/11, 'endpoint')
    inclusion(d, a/n, 'outer_width')
    inclusion(td, (8-a)/m, 'tail_width')
    check(ar['polynomials_ascending'] == [list(p) for p in POLYS], 'polynomials')
    check(ar['coefficient_bounds'] == [20, 106, 661], 'coefficient_bounds')
    tails = [(2*cj*144**(j+2)*Box(-104).exp()).high
             for j, cj in enumerate((20, 106, 661))]
    for j in range(3):
        check(tails[j] <= D(ar['theta_uniform_tails'][j]), 'theta_tail')
    check((4*Box(-39).exp()).high < D('0.5'), 'geometric_ratio')
    spatial_h, spatial_z = (10000*Box(-64).exp()).high, (1250*Box(-64).exp()).high
    check(spatial_h <= D(err['H_spatial_tail_upper']), 'spatial_H')
    check(spatial_z <= D(err['one_sided_mass_spatial_tail_upper']), 'spatial_mass')
    head, tail = c['cells']['head'], c['cells']['tail']
    check(len(head) == n and len(tail) == m, 'cell_counts')
    hs, zs, he, ze = Box(0), Box(0), Box(0), Box(0)
    for j, row in enumerate(tail):
        cell, mid, km, kp, kpp = map(read_pair, row[:5])
        left, right = a*(m-j)/m+Box(8*j)/m, a*(m-j-1)/m+Box(8*(j+1))/m
        expected_mid = a*(2*m-2*j-1)/(2*m)+Box(8*(2*j+1))/(2*m)
        inclusion(cell, Box(left.low, right.high), f'tail_cell:{j}')
        inclusion(mid, expected_mid, f'tail_midpoint:{j}')
        inclusion(cell, mid, f'tail_midpoint_inside:{j}')
        inclusion(km, kernel(mid, 0, pi, tails)[0], f'tail_k:{j}')
        derivatives = kernel(cell, 2, pi, tails)
        inclusion(kp, derivatives[1], f'tail_kprime:{j}')
        inclusion(kpp, derivatives[2], f'tail_ksecond:{j}')
        eh, ez = D(row[5]), D(row[6])
        check(eh >= (td*td*td/24*(2*kp+cell*kpp).magnitude()).high,
              f'tail_H_midpoint_error:{j}')
        check(ez >= (td*td*td/24*kpp.magnitude()).high, f'tail_mass_midpoint_error:{j}')
        hp, zp = map(read_pair, row[7:9])
        inclusion(hp, td*mid*km+Box(eh.copy_negate(), eh), f'tail_H_contribution:{j}')
        inclusion(zp, td*km+Box(ez.copy_negate(), ez), f'tail_mass_contribution:{j}')
        hs += hp
        zs += zp
        he += eh
        ze += ez
    inclusion(read_pair(enc['H_A']), hs+Box(0, err['H_spatial_tail_upper']), 'H_A_sum')
    inclusion(read_pair(enc['one_sided_tail_mass']), zs+Box(0, err['one_sided_mass_spatial_tail_upper']), 'tail_mass_sum')
    check(he.high <= D(err['H_A_midpoint_radius_upper']), 'H_A_error_sum')
    check(ze.high <= D(err['one_sided_mass_midpoint_radius_upper']), 'tail_mass_error_sum')
    report['tail_cells_checked'] = m

    # Independently enclose the true midpoint angles by angle addition.
    sin_step, cos_step = trig(11*d)
    sn, cs = trig(11*d/2)
    lip = (11*d/2).high
    minimum_k = None
    for i, row in enumerate(head):
        cell, k, kp, sine, cosine = map(read_pair, row[:5])
        inclusion(cell, Box((a*i/n).low, (a*(i+1)/n).high), f'head_cell:{i}')
        kvals = kernel(cell, 1, pi, tails)
        inclusion(k, kvals[0], f'head_k:{i}')
        inclusion(kp, kvals[1], f'head_kprime:{i}')
        check(k.low > 0, f'head_k_positive:{i}')
        minimum_k = k.low if minimum_k is None else min(minimum_k, k.low)
        inclusion(sine, sn+Box(lip.copy_negate(), lip), f'head_sine:{i}')
        inclusion(cosine, cs+Box(lip.copy_negate(), lip), f'head_cosine:{i}')
        check(max(sine.radius(), cosine.radius()) <= D(c['telemetry']['maximum_trig_box_radius']),
              f'trig_radius:{i}')
        sn, cs = sn*cos_step+cs*sin_step, cs*cos_step-sn*sin_step
    check(minimum_k == D(c['telemetry']['minimum_head_k_lower']), 'minimum_k')
    report['kernel_and_trig_head_cells_checked'] = n

    # Reconstruct the descending whole-cell H inclusion from saved boxes.
    h_right = read_pair(enc['H_A'])
    for i in range(n-1, -1, -1):
        row = head[i]
        cell, k, h = read_pair(row[0]), read_pair(row[1]), read_pair(row[5])
        increment = d*cell*k
        check(increment.low >= 0, f'H_increment_positive:{i}')
        inclusion(h, Box(h_right.low, UP.add(h_right.high, increment.high)), f'H_cell:{i}')
        h_right += increment
    inclusion(read_pair(enc['H_0']), h_right, 'H_0')

    prefixes = [Box(0) for _ in range(4)]
    maxima = [D(0) for _ in range(4)]
    totals = [Box(0) for _ in range(4)]  # layer, remainder, raw, head mass
    for i, row in enumerate(head):
        cell, k, kp, sine, cosine, h, s, t, u, v, q, layer, rem, raw = map(read_pair, row)
        fs = [k*cosine, h*cosine, cell*h*sine, cell*k*sine]
        for j, saved in enumerate((s, t, u, v)):
            inclusion(saved, prefixes[j]+Box(0, d.high)*fs[j], f'primitive_{j}:{i}')
            maxima[j] = max(maxima[j], saved.radius())
        inclusion(q, cell+h*kp/k.square(), f'q:{i}')
        inclusion(layer, 4*q*s.square(), f'layer:{i}')
        e = cosine+11*cell*sine
        inclusion(rem, 4*(e*(k*t-h*s)-11*cosine*(k*u-h*v)), f'remainder:{i}')
        inclusion(raw, layer+rem, f'raw_cell:{i}')
        totals = [total+d*value for total, value in zip(totals, (layer, rem, raw, k))]
        prefixes = [p+d*f for p, f in zip(prefixes, fs)]
    for j in range(4):
        inclusion(read_pair(enc['primitives_at_A_S_T_U_V'][j]), prefixes[j], 'primitive_at_A')
        check(maxima[j] <= D(err['maximum_whole_cell_primitive_radii_S_T_U_V'][j]), 'primitive_radius')
    for total, key in zip(totals, ('integrated_layer_raw', 'integrated_remainder_raw',
                                  'Z_squared_integral_G', 'one_sided_head_mass')):
        inclusion(read_pair(enc[key]), total, f'head_aggregate:{key}')
    z, raw, normalized = map(read_pair, (enc['Z'], enc['Z_squared_integral_G'], enc['integral_G']))
    inclusion(z, 2*(read_pair(enc['one_sided_head_mass'])+read_pair(enc['one_sided_tail_mass'])), 'normalization_Z')
    check(z.low > 0, 'Z_positive')
    inclusion(normalized, raw/z.square(), 'normalized_integral')
    check(normalized.low > 0, 'positive_lower_endpoint')
    for key, allowance in [('integrated_layer_raw', 'integrated_layer_raw_radius'),
                           ('integrated_remainder_raw', 'integrated_remainder_raw_radius'),
                           ('Z_squared_integral_G', 'total_raw_radius_upper'),
                           ('integral_G', 'total_normalized_radius_upper')]:
        check(read_pair(enc[key]).radius() <= D(err[allowance]), 'reported_radius')
    check((Box(err['integrated_layer_raw_radius'])+Box(err['integrated_remainder_raw_radius'])).high
          <= D(err['sum_raw_component_radii_upper']), 'component_radius_sum')
    check(D(err['total_raw_radius_upper']) <= D(err['sum_raw_component_radii_upper']), 'raw_radius_budget')
    check(c['test']['failures'] == [], 'original_no_failures')
    check(c['telemetry']['kernel_calls_by_order'] == [m, n, m], 'original_kernel_counts')
    check(c['telemetry']['head_cells_completed'] == n and c['telemetry']['tail_cells_completed'] == m,
          'original_completed_counts')
    for name, signals in c['runtime']['signals'].items():
        check(not any(value for key, value in signals.items() if key not in ('Inexact', 'Rounded')),
              f'original_signals:{name}')
    report['head_algebra_and_prefix_cells_checked'] = n
    report['independent_pi'] = pi.pair()
    report['minimum_saved_k_lower'] = str(minimum_k)
    report['Z'] = z.pair()
    report['integral_G'] = normalized.pair()
    report['required_positive_lower_threshold'] = '0'
    report['actual_lower_endpoint'] = str(normalized.low)
    report['original_negative_test_required_upper_threshold'] = '0'
    report['actual_upper_endpoint'] = str(normalized.high)
    report['complete_error_budget_checked'] = err


def main():
    directory = Path(__file__).resolve().parent
    path = directory/'first-period-certificate.json'
    output = directory/'first-period-independent-audit.json'
    assert not output.exists(), 'Preserve the independent audit report'
    original_bytes = path.read_bytes()
    c = json.loads(original_bytes)
    report = {'status': 'IN_PROGRESS', 'failures': [], 'precision': 55,
              'scope': 'Only the existing x=11 first-period C609a certificate; all cells; no search',
              'limitations': 'Independently coded interval inclusion audit; shared Decimal backend and named source inputs remain imported, not formal verification',
              'original_certificate_sha256': hashlib.sha256(original_bytes).hexdigest(),
              'auditor_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    started = time.monotonic()
    try:
        for filename, key in [('certify.py', 'core_sha256'), ('first_period.py', 'script_sha256')]:
            check(hashlib.sha256((directory/filename).read_bytes()).hexdigest() == c['sources'][key],
                  f'source_hash:{filename}')
        audit(c, report)
        for name, ctx in [('DOWN', DOWN), ('UP', UP), ('NEAR', NEAR)]:
            check(not any(value for signal, value in ctx.flags.items()
                          if signal.__name__ not in ('Inexact', 'Rounded')), f'audit_signals:{name}')
        check(path.read_bytes() == original_bytes, 'original_certificate_unchanged')
        report['status'] = 'INDEPENDENT_ALL_CELL_INCLUSION_AUDIT_PASS'
    except Exception as error:
        report['status'] = 'INDEPENDENT_AUDIT_FAILED'
        report['failures'].append(f'{type(error).__name__}: {error}')
    report['checks_completed_by_category'] = dict(COUNTS)
    report['telemetry'] = {key: str(value) if isinstance(value, D) else value
                           for key, value in TELEMETRY.items()}
    report['runtime'] = {
        'python': sys.version, 'implementation': platform.python_implementation(),
        'c_backend': D is __import__('_decimal').Decimal,
        'decimal_version': getattr(decimal, '__version__', 'unavailable'),
        'libmpdec_version': getattr(decimal, '__libmpdec_version__', 'unavailable'),
        'contexts': {name: str(ctx) for name, ctx in [('DOWN', DOWN), ('UP', UP), ('NEAR', NEAR)]},
        'flags': {name: {signal.__name__: value for signal, value in ctx.flags.items()}
                  for name, ctx in [('DOWN', DOWN), ('UP', UP), ('NEAR', NEAR)]},
        'elapsed_seconds': time.monotonic()-started}
    with output.open('x') as stream:
        json.dump(report, stream, indent=2)
        stream.write('\n')
    print(json.dumps({key: report.get(key) for key in
                      ('status', 'tail_cells_checked', 'kernel_and_trig_head_cells_checked',
                       'head_algebra_and_prefix_cells_checked', 'actual_lower_endpoint',
                       'required_positive_lower_threshold', 'actual_upper_endpoint', 'failures')}, indent=2))
    print(f'Full audit report: {output}')
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
