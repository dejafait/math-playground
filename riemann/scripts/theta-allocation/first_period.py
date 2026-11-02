"""One capped real-interval test of integral_0^(2*pi/11) G_11(a) da.

The full domain/inclusion proof is in the dated calculation working note.
Imports only L609's arithmetic/series machinery; never invokes its main.
No floating values or preview enter any mathematical enclosure.
"""
import decimal
import hashlib
import json
import platform
import sys
import time
from pathlib import Path

import certify as base

I, D, UP, DN, RN = base.I, base.D, base.UP, base.DN, base.RN
N, M, X = 65536, 4096, 11
OUTPUT = Path(__file__).with_name('first-period-certificate.json')


def main():
    assert not OUTPUT.exists(), 'Do not overwrite or restart this single capped run'
    started = time.monotonic()
    telemetry = {'kernel_calls_by_order': [0, 0, 0], 'division_calls': 0,
                 'minimum_denominator_magnitude': None, 'exp_calls': 0,
                 'exp_input_min': None, 'exp_input_max': None,
                 'kernel_domain_min': None, 'kernel_domain_max': None,
                 'minimum_head_k_lower': None, 'head_cells_completed': 0,
                 'tail_cells_completed': 0, 'direct_sincos_calls': 0,
                 'maximum_direct_sincos_argument': D(0),
                 'maximum_trig_box_radius': D(0)}
    original_div, original_exp, original_init = I.__truediv__, I.exp, I.__init__

    def checked_init(self, lo, hi=None):
        original_init(self, lo, hi)
        assert self.lo.is_finite() and self.hi.is_finite() and self.lo <= self.hi

    def checked_div(self, other):
        other = base.cv(other)
        telemetry['division_calls'] += 1
        assert other.lo > 0 or other.hi < 0
        mag = min(other.lo.copy_abs(), other.hi.copy_abs())
        old = telemetry['minimum_denominator_magnitude']
        telemetry['minimum_denominator_magnitude'] = mag if old is None else min(old, mag)
        return original_div(self, other)

    def checked_exp(self):
        telemetry['exp_calls'] += 1
        for key, val, op in [('exp_input_min', self.lo, min),
                             ('exp_input_max', self.hi, max)]:
            old = telemetry[key]
            telemetry[key] = val if old is None else op(old, val)
        return original_exp(self)

    I.__init__, I.__truediv__, I.exp = checked_init, checked_div, checked_exp

    def kernel(u, order=0):
        assert 0 <= u.lo <= u.hi <= 8
        telemetry['kernel_calls_by_order'][order] += 1
        assert sum(telemetry['kernel_calls_by_order']) <= N + 2*M
        for key, val, op in [('kernel_domain_min', u.lo, min),
                             ('kernel_domain_max', u.hi, max)]:
            old = telemetry[key]
            telemetry[key] = val if old is None else op(old, val)
        return base.kernel(u, order)

    def sincos(u):
        telemetry['direct_sincos_calls'] += 1
        assert telemetry['direct_sincos_calls'] <= 4
        telemetry['maximum_direct_sincos_argument'] = max(
            telemetry['maximum_direct_sincos_argument'], u.magnitude())
        return base.sincos(u)

    A = 2*base.PI/X
    assert 0 < A.lo < A.hi < 1
    d = A/N
    tail_d = (8-A)/M
    ha, tail_mass, h_error, mass_error = I(0), I(0), I(0), I(0)
    tail_rows = []
    # Affine endpoint construction preserves the actual [A,8] domain.
    for j in range(M):
        left = A*((I(M-j))/M) + I(8*j)/M
        right = A*((I(M-j-1))/M) + I(8*(j+1))/M
        mid = A*((I(2*M-2*j-1))/(2*M)) + I(8*(2*j+1))/(2*M)
        cell = I(left.lo, right.hi)
        km = kernel(mid)[0]
        ks = kernel(cell, 2)
        eh = (base.power(tail_d, 3)/24*(2*ks[1]+cell*ks[2]).magnitude()).hi
        ez = (base.power(tail_d, 3)/24*ks[2].magnitude()).hi
        hpart = tail_d*mid*km + I(eh.copy_negate(), eh)
        zpart = tail_d*km + I(ez.copy_negate(), ez)
        ha += hpart
        tail_mass += zpart
        h_error += eh
        mass_error += ez
        tail_rows.append([cell.pair(), mid.pair(), km.pair(),
                          ks[1].pair(), ks[2].pair(), str(eh), str(ez),
                          hpart.pair(), zpart.pair()])
        telemetry['tail_cells_completed'] += 1
    spatial_h = (10000*I(-64).exp()).hi
    spatial_mass = (1250*I(-64).exp()).hi
    ha += I(0, spatial_h)
    tail_mass += I(0, spatial_mass)
    assert ha.lo > 0 and tail_mass.lo > 0

    sin_step, cos_step = sincos(X*d)
    sin_mid, cos_mid = sincos(X*d/2)
    lip = (X*d/2).hi
    head = []
    head_mass = I(0)
    for j in range(N):
        left, right = A*j/N, A*(j+1)/N
        cell = I(left.lo, right.hi)
        k, kp = kernel(cell, 1)
        assert k.lo > 0, 'A whole evaluation box failed positive-k separation'
        old = telemetry['minimum_head_k_lower']
        telemetry['minimum_head_k_lower'] = k.lo if old is None else min(old, k.lo)
        sn = sin_mid+I(lip.copy_negate(), lip)
        cs = cos_mid+I(lip.copy_negate(), lip)
        telemetry['maximum_trig_box_radius'] = max(
            telemetry['maximum_trig_box_radius'], sn.radius(), cs.radius())
        head_mass += d*k
        head.append([cell, k, kp, sn, cs])
        sin_mid, cos_mid = (sin_mid*cos_step+cos_mid*sin_step,
                           cos_mid*cos_step-sin_mid*sin_step)

    # The same true A defines all cell endpoints. Descending induction
    # encloses H everywhere, not merely at midpoint samples.
    h_right = ha
    for row in reversed(head):
        cell, k, _, _, _ = row
        incr = d*cell*k
        assert incr.lo >= 0
        hb = I(h_right.lo, UP.add(h_right.hi, incr.hi))
        row.append(hb)
        h_right += incr

    prefixes = [I(0) for _ in range(4)]  # S, T, U, V
    partial_length = I(0, d.hi)
    layer_total, remainder_total, raw_total = I(0), I(0), I(0)
    maximum_primitive_radii = [D(0) for _ in range(4)]
    head_rows = []
    for row in head:
        a, k, kp, sn, cs, h = row
        fs = [k*cs, h*cs, a*h*sn, a*k*sn]
        boxes = [p+partial_length*f for p, f in zip(prefixes, fs)]
        s, t, u, v = boxes
        q = a+h*kp/k.square()
        layer = 4*q*s.square()
        e = cs+X*a*sn
        remainder = 4*(e*(k*t-h*s)-X*cs*(k*u-h*v))
        raw_cell = layer+remainder
        layer_total += d*layer
        remainder_total += d*remainder
        raw_total += d*raw_cell
        prefixes = [p+d*f for p, f in zip(prefixes, fs)]
        maximum_primitive_radii = [max(old, p.radius())
                                   for old, p in zip(maximum_primitive_radii, boxes)]
        head_rows.append([a.pair(), k.pair(), kp.pair(), sn.pair(), cs.pair(),
                          h.pair(), *[p.pair() for p in boxes], q.pair(),
                          layer.pair(), remainder.pair(), raw_cell.pair()])
        telemetry['head_cells_completed'] += 1

    z = 2*(head_mass+tail_mass)
    assert z.lo > 0
    normalized = raw_total/z.square()
    flags = {name: {signal.__name__: value for signal, value in ctx.flags.items()}
             for name, ctx in [('DN', DN), ('UP', UP), ('RN', RN)]}
    failures = []
    for name, signals in flags.items():
        for signal, raised in signals.items():
            if raised and signal not in ('Inexact', 'Rounded'):
                failures.append(f'{name}: unexpected arithmetic signal {signal}')
    assert telemetry['kernel_calls_by_order'] == [M, N, M]
    assert telemetry['head_cells_completed'] == N and telemetry['tail_cells_completed'] == M
    if failures:
        status = 'ARITHMETIC_FAILURE_INCONCLUSIVE'
    elif normalized.hi < 0:
        status = 'CERTIFIED_NEGATIVE'
    elif normalized.lo >= 0:
        status = 'CERTIFIED_NONNEGATIVE_REJECTS_SELECTED_NEGATIVE_WITNESS'
    else:
        status = 'ZERO_STRADDLING_INCONCLUSIVE'
        failures.append('Finite enclosure straddles zero; this run does not decide the sign')
    certificate = {
        'status': status,
        'scope': 'Only x=11, first complete outer period, unchanged L609 allocation',
        'run_count': 1,
        'caps': {'outer_cells': N, 'tail_midpoint_cells': M, 'precision': base.PREC,
                 'theta_terms': 5, 'cutoff': 8, 'kernel_calls': N+2*M,
                 'direct_sincos_calls': 4, 'restart_or_sweep': False},
        'arithmetic': {'method': 'L609 unchanged directed Decimal core; exact negation; widened nearest exp',
                       'pi': base.PI.pair(), 'endpoint_A': A.pair(),
                       'outer_width': d.pair(), 'tail_width': tail_d.pair(),
                       'theta_uniform_tails': [str(t) for t in base.TAILS],
                       'polynomials_ascending': base.POLYS,
                       'coefficient_bounds': base.COEFFICIENT_BOUNDS},
        'enclosures': {'H_A': ha.pair(), 'H_0': h_right.pair(),
                       'one_sided_tail_mass': tail_mass.pair(),
                       'one_sided_head_mass': head_mass.pair(), 'Z': z.pair(),
                       'primitives_at_A_S_T_U_V': [p.pair() for p in prefixes],
                       'integrated_layer_raw': layer_total.pair(),
                       'integrated_remainder_raw': remainder_total.pair(),
                       'Z_squared_integral_G': raw_total.pair(),
                       'integral_G': normalized.pair()},
        'error_budget': {'H_A_midpoint_radius_upper': str(h_error.hi),
                         'one_sided_mass_midpoint_radius_upper': str(mass_error.hi),
                         'H_spatial_tail_upper': str(spatial_h),
                         'one_sided_mass_spatial_tail_upper': str(spatial_mass),
                         'maximum_whole_cell_primitive_radii_S_T_U_V':
                             [str(r) for r in maximum_primitive_radii],
                         'integrated_layer_raw_radius': str(layer_total.radius()),
                         'integrated_remainder_raw_radius': str(remainder_total.radius()),
                         'sum_raw_component_radii_upper': str(UP.add(layer_total.radius(), remainder_total.radius())),
                         'total_raw_radius_upper': str(raw_total.radius()),
                         'total_normalized_radius_upper': str(normalized.radius()),
                         'interpretation': 'All input, box, tail, midpoint, endpoint and rounding errors included; component radii overlap those sources, not additional unpaid errors'},
        'test': {'required_upper_bound': '0', 'actual_upper_bound': str(normalized.hi),
                 'actual_lower_bound': str(normalized.lo), 'failures': failures,
                 'all_head_k_boxes_positive': telemetry['minimum_head_k_lower'] > 0,
                 'Z_numerically_positive': z.lo > 0,
                 'all_parameter_cells_covered': True},
        'runtime': {'python': sys.version, 'implementation': platform.python_implementation(),
                    'decimal_version': decimal.__version__,
                    'libmpdec_version': decimal.__libmpdec_version__,
                    'c_backend_identity': decimal.Decimal is __import__('_decimal').Decimal,
                    'contexts': {name: str(ctx) for name, ctx in [('DN', DN), ('UP', UP), ('RN', RN)]},
                    'signals': flags, 'elapsed_seconds_before_serialization': time.monotonic()-started},
        'telemetry': {k: str(v) if isinstance(v, D) else v for k, v in telemetry.items()},
        'sources': {'core_path': 'scripts/theta-allocation/certify.py',
                    'core_sha256': hashlib.sha256(Path(base.__file__).read_bytes()).hexdigest(),
                    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    'inclusion_proof': 'drafts/2026-11-01-theta-first-period-calculation-working.md'},
        'cell_column_order': {
            'tail': ['u_cell', 'u_midpoint', 'k_midpoint', 'k_prime_cell', 'k_second_cell',
                     'H_error_radius', 'mass_error_radius', 'H_contribution', 'mass_contribution'],
            'head': ['a_cell', 'k_cell', 'k_prime_cell', 'sin_cell', 'cos_cell', 'H_cell',
                     'S_cell', 'T_cell', 'U_cell', 'V_cell', 'q_cell', 'layer_cell_raw',
                     'remainder_cell_raw', 'G_cell_raw']},
        'cells': {'tail': tail_rows, 'head': head_rows}}
    with OUTPUT.open('x') as stream:
        json.dump(certificate, stream, separators=(',', ':'))
        stream.write('\n')
    print(json.dumps({'status': status, 'integral_G': normalized.pair(),
                      'required_upper_bound': '0',
                      'total_propagated_radius_upper': str(normalized.radius()),
                      'failures': failures, 'certificate': str(OUTPUT)}, indent=2))


if __name__ == '__main__':
    main()
