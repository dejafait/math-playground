"""Exact rational ancillary bounds for L726; no numerical mean evidence."""
from fractions import Fraction as F
import json
from math import factorial
from pathlib import Path

R, d, A = F(11, 8), F(5, 4), F(27, 10)
N = 128

def rational_integral(cosine):
    cells = []
    lower = upper = F(0)
    for j in range(N):
        lo, hi = F(j, N) / R, F(j + 1, N) / R
        den = lambda k: 1 + 2 * cosine * k + k * k
        ends = [den(lo), den(hi)]
        dl = min(ends + ([1 - cosine * cosine] if lo <= -cosine <= hi else []))
        du = max(ends)
        fl, fu = (1 - hi * hi) / du, (1 - lo * lo) / dl
        raw_lo, raw_hi = A / d * fl / N, A / d * fu / N
        scale = 10**8
        cell_lo = F((raw_lo * scale).__floor__(), scale)
        cell_hi = F((raw_hi * scale).__ceil__(), scale)
        assert cell_lo <= raw_lo <= raw_hi <= cell_hi
        lower += cell_lo
        upper += cell_hi
        cells.append(dict(j=j, k_lo=str(lo), k_hi=str(hi),
                          denominator_lo=str(dl), denominator_hi=str(du),
                          raw_contribution_lo=str(raw_lo), raw_contribution_hi=str(raw_hi),
                          contribution_lo=str(cell_lo), contribution_hi=str(cell_hi)))
    return dict(cosine=str(cosine), lower=str(lower), upper=str(upper), cells=cells)

left = rational_integral(F(-1, 2))
right = rational_integral(F(-12, 13))
C = A / d * (1 / R - 1 / (2 * R**3))
omega_min_lo = A / d * (-1 + 2 * R * F(8, 15))
omega_star_lo = omega_min_lo - A * (d - R)**2 / (2 * d*d * R*R)
checks = {
    "left_frequency_upper_below_9_over_4": F(left["upper"]) < F(9, 4),
    "right_frequency_lower_above_4": F(right["lower"]) > 4,
    "global_derivative_coefficient_above_1_over_8": C / (1 + 1 / R)**4 > F(1, 8),
    "central_density_below_3_over_4_using_pi_above_25_over_8": F(25, 8) * C * F(5, 13) > F(4, 3),
    "omega_star_lower_above_1_plus_1_over_2000": omega_star_lo > 1 + F(1, 2000),
    "bump_lower_frequency_above_1": omega_star_lo - 2 * F(22, 7) * F(3, 81920) > 1,
    "bump_measure_below_7_over_160": 4 * F(22, 7) * F(3, 81920) < F(49, 102400),
    "central_linear_bound_below_8_over_15": 15 * F(22, 7) / (64 * F(7, 5)) < F(8, 15),
    "residual_below_7_over_60": F(28, 5) / (16 * 3) == F(7, 60),
    "total_correction_below_299_over_320": F(8, 15) + F(91, 320) + F(7, 60) == F(299, 320),
    "gaussian_exponent_above_1_over_32": F(57 * 14, 968 * 15) / (d*d) > F(1, 32),
    "exponential_taylor_polynomial_above_11_over_3": sum(F(13, 10)**j / factorial(j) for j in range(9)) > F(11, 3),
}
certificate = dict(kind="exact rational ancillary bounds, not a mean computation",
                   subdivisions=N, left=left, right=right,
                   constants=dict(C=str(C), global_derivative=str(C / (1 + 1 / R)**4),
                                  central_derivative=str(C * F(5, 13)),
                                  omega_min_lower=str(omega_min_lo),
                                  omega_star_lower=str(omega_star_lo)),
                   checks=checks, all_pass=all(checks.values()))
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(certificate, indent=2) + '\n')
print('Exact ancillary bounds:', 'PASS' if certificate['all_pass'] else 'FAIL')
print('omega(cos=-1/2): upper', float(F(left['upper'])), 'required < 2.25')
print('omega(cos=-12/13): lower', float(F(right['lower'])), 'required > 4')
print('global derivative coefficient:', float(C / (1 + 1 / R)**4), 'required > 0.125')
print('central density bound uses derivative:', float(C * F(5, 13)))
print('failures:', [k for k, v in checks.items() if not v])
print('full certificate:', path)
assert certificate['all_pass']
