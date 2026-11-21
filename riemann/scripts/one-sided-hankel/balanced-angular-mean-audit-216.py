"""Independent exact replay of L726's ancillary evidence; no finite-n mean test."""
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
from pathlib import Path
import json

source = Path(__file__).with_name('actual-angular-mean-bounds-214.json')
data = json.loads(source.read_text())
R, d, A = Q(11, 8), Q(5, 4), Q(27, 10)
failures = []


def require(condition, name):
    if not condition:
        failures.append(name)


require(data['subdivisions'] == 128, 'subdivisions')
cell_records = {}
for name, cosine in [('left', Q(-1, 2)), ('right', Q(-12, 13))]:
    block = data[name]
    require(Q(block['cosine']) == cosine, name + ':cosine')
    require(len(block['cells']) == 128, name + ':cell_count')
    lo_sum = hi_sum = Q(0)
    records = []
    for j, cell in enumerate(block['cells']):
        lo, hi = Q(j, 128) / R, Q(j + 1, 128) / R
        # Vertex form verifies the complete interval extrema, not samples.
        quadratic = lambda k: (k + cosine)**2 + 1 - cosine**2
        min_point = min(hi, max(lo, -cosine))
        denominator_lo = quadratic(min_point)
        denominator_hi = max(quadratic(lo), quadratic(hi))
        require(denominator_lo > 0 and 1 - hi**2 > 0,
                f'{name}:{j}:positive_division')
        raw_lo = A * (1 - hi**2) / (128 * d * denominator_hi)
        raw_hi = A * (1 - lo**2) / (128 * d * denominator_lo)
        floor8 = Q((raw_lo * 10**8).__floor__(), 10**8)
        ceil8 = Q((raw_hi * 10**8).__ceil__(), 10**8)
        expected = dict(j=j, k_lo=str(lo), k_hi=str(hi),
                        denominator_lo=str(denominator_lo),
                        denominator_hi=str(denominator_hi),
                        raw_contribution_lo=str(raw_lo),
                        raw_contribution_hi=str(raw_hi),
                        contribution_lo=str(floor8), contribution_hi=str(ceil8))
        require(cell == expected, f'{name}:{j}:all_fields')
        require(floor8 <= raw_lo <= raw_hi <= ceil8,
                f'{name}:{j}:outward_rounding')
        lo_sum += floor8
        hi_sum += ceil8
        records.append(expected)
    require(str(lo_sum) == block['lower'], name + ':lower_sum')
    require(str(hi_sum) == block['upper'], name + ':upper_sum')
    cell_records[name] = dict(lower=str(lo_sum), upper=str(hi_sum), cells=records)

C = A / d * (1 / R - 1 / (2 * R**3))
omega_min = A / d * (-1 + 2 * R * Q(8, 15))
omega_star = omega_min - A * (d - R)**2 / (2 * d**2 * R**2)
constants = dict(C=str(C), global_derivative=str(C / (1 + 1 / R)**4),
                 central_derivative=str(C * Q(5, 13)),
                 omega_min_lower=str(omega_min), omega_star_lower=str(omega_star))
require(constants == data['constants'], 'complete_constant_record')
checks = {
    'left_frequency_upper_below_9_over_4': Q(cell_records['left']['upper']) < Q(9, 4),
    'right_frequency_lower_above_4': Q(cell_records['right']['lower']) > 4,
    'global_derivative_coefficient_above_1_over_8': C / (1 + 1 / R)**4 > Q(1, 8),
    'central_density_below_3_over_4_using_pi_above_25_over_8': Q(25, 8) * C * Q(5, 13) > Q(4, 3),
    'omega_star_lower_above_1_plus_1_over_2000': omega_star > 1 + Q(1, 2000),
    'bump_lower_frequency_above_1': omega_star - 2 * Q(22, 7) * Q(3, 81920) > 1,
    'bump_measure_below_7_over_160': 4 * Q(22, 7) * Q(3, 81920) < Q(49, 102400),
    'central_linear_bound_below_8_over_15': 15 * Q(22, 7) / (64 * Q(7, 5)) < Q(8, 15),
    'residual_below_7_over_60': Q(28, 5) / 48 == Q(7, 60),
    'total_correction_below_299_over_320': Q(8, 15) + Q(91, 320) + Q(7, 60) == Q(299, 320),
    'gaussian_exponent_above_1_over_32': Q(57 * 14, 968 * 15) / d**2 > Q(1, 32),
    'exponential_taylor_polynomial_above_11_over_3': sum(Q(13, 10)**j / factorial(j) for j in range(9)) > Q(11, 3),
}
require(checks == data['checks'], 'complete_check_record')
for name, value in checks.items():
    require(value, name)
require(data['all_pass'] is True, 'original_all_pass')
# Extra checks of arithmetic used in the analytic specialization.
extra = dict(
    central_nonlinear=Q(25, 512) < Q(7, 60),
    high_bump_multiplier=2 * Q(22, 7) - 1 < Q(11, 2),
    maximum_ordinate_clearance=R**2 - (d**2 + Q(9, 20)**2) > Q(137, 5000),
    exponent_margin=Q(1, 16) - 2 * Q(91, 5000) == Q(261, 10000),
    correction_margin=1 - Q(299, 320) == Q(21, 320),
    log_frequency_upper=A / d * (-1 + 2 * R * Q(13, 10)) == Q(2781, 500),
)
for name, value in extra.items():
    require(value, name)
result = dict(kind='complete exact ancillary replay; analytic proof audited separately',
              source=str(source), source_sha256=sha256(source.read_bytes()).hexdigest(),
              cells_checked=256, cells=cell_records, constants=constants,
              original_checks=checks, extra_checks=extra,
              correction_budget='299/320', required_correction_budget='<1',
              exponent_margin='261/10000', required_exponent_margin='>0',
              failures=failures, all_pass=not failures)
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(result, indent=2) + '\n')
print('Ancillary audit:', 'PASS' if not failures else 'FAIL', '; cells checked: 256')
print('Correction budget: 299/320; required <1. Exponent margin: 261/10000; required >0.')
print('Frequency bounds:', cell_records['left']['upper'], '<9/4;',
      cell_records['right']['lower'], '>4')
print('Failures:', failures)
print('Full certificate:', output)
if failures:
    raise SystemExit(1)
