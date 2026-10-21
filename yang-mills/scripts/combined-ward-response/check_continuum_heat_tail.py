"""Exact rational evaluation of L033's omitted-mode heat-moment bound.

This does not evaluate any signed partial sum or certify its quadrature.
All bound computations use fractions; displayed decimals are rounded up.
"""
import argparse
import json
from fractions import Fraction as F
from pathlib import Path


HEAT = F(9, 1024)
POLYNOMIAL_CONSTANTS = [11584512, 46338048]


def inverse_exp_upper(x, degree):
    term = F(1)
    total = term
    for j in range(1, degree + 1):
        term *= x / j
        total += term
    return 1 / total


def rounded_upper(value, digits=12):
    if value == 0:
        return F(0), dict(decimal_upper='0', numerator='0', denominator='1')
    exponent = len(str(value.numerator)) - len(str(value.denominator))
    power = F(10) ** exponent
    while value < power:
        exponent -= 1
        power /= 10
    while value >= 10 * power:
        exponent += 1
        power *= 10
    scale = F(10) ** (exponent - digits + 1)
    scaled = value / scale
    mantissa = (scaled.numerator + scaled.denominator - 1) // scaled.denominator
    upper = mantissa * scale
    assert upper >= value
    chars = str(mantissa)
    display = chars[0] + '.' + chars[1:] + 'e' + str(exponent + len(chars) - digits)
    return upper, dict(decimal_upper=display, numerator=str(upper.numerator),
                       denominator=str(upper.denominator))


def tail_moment(p, cutoff, degree):
    first = cutoff + 1
    ratio = F(first + 1, first) ** p * inverse_exp_upper(HEAT * (2 * first + 1), degree)
    if ratio >= 1:
        _, ratio_record = rounded_upper(ratio)
        raise ValueError(f'Geometric moment ratio upper={ratio_record["decimal_upper"]} >= required 1: p={p}, cutoff={cutoff}')
    value = first ** p * inverse_exp_upper(HEAT * first * first, degree) / (1 - ratio)
    upper, record = rounded_upper(value)
    ratio_upper, ratio_record = rounded_upper(ratio)
    assert ratio_upper < 1
    return upper, dict(power=p, cutoff=cutoff, upper=record,
                       geometric_ratio_upper=ratio_record, exact_ratio_less_than_one=True)


def full_moment(p, finite_cutoff, degree):
    # 0**0=1 is the intended convention for S_0.
    finite = sum((rounded_upper(n ** p * inverse_exp_upper(HEAT * n * n, degree))[0]
                  for n in range(finite_cutoff + 1)), F(0))
    tail, tail_record = tail_moment(p, finite_cutoff, degree)
    upper, record = rounded_upper(finite + tail)
    return upper, dict(power=p, finite_cutoff=finite_cutoff, upper=record,
                       remaining_tail=tail_record)


def verify_existing_expansion():
    from check_continuum_pure_sectors import operators
    rows = []
    for pair in [(0, 2), (1, 3)]:
        qs, n2, _ = operators(pair)
        values = []
        for name, op, expected, required in [('Q3', qs[0], 4, F(192)),
                                             ('Q6', qs[1], 4, F(768)),
                                             ('N2', n2, 6, F(6704, 3))]:
            degrees = sorted({sum(d) + sum(a) + sum(b) for d, _, a, _, b in op})
            assert degrees == [expected]
            weighted = sum((abs(v) * 2 ** sum(d) for (d, _, _, _, _), v in op.items()), F(0))
            assert weighted <= required
            values.append(dict(operator=name, total_derivative_degrees=degrees,
                               weighted_l1_exact=dict(numerator=str(weighted.numerator), denominator=str(weighted.denominator)),
                               required_upper=dict(numerator=str(required.numerator), denominator=str(required.denominator)),
                               bound_passed=True))
        rows.append(dict(pair=pair, operators=values))
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cutoffs', type=int, nargs='+', default=[12, 64, 80, 96, 112, 128])
    parser.add_argument('--taylor-degree', type=int, default=160)
    parser.add_argument('--moment-cutoff', type=int, default=160)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('continuum-heat-tail-certificate.json'))
    args = parser.parse_args()
    # Numerical partial sums from step 045 are comparators, not lower bounds.
    comparators = [F('290.672016726'), F('1854.720139835')]
    s0, r0 = full_moment(0, args.moment_cutoff, args.taylor_degree)
    s10, r10 = full_moment(10, args.moment_cutoff, args.taylor_degree)
    certificate = dict(scope='Both L032 pure sectors; every omitted k or ell coordinate, all ell components.',
                       method='L033 analytic estimate, evaluated with exact rational arithmetic and outward decimal rounding.',
                       heat_lower=dict(numerator='9', denominator='1024'), polynomial_constants=POLYNOMIAL_CONSTANTS,
                       taylor_degree=args.taylor_degree, full_moments=[r0, r10],
                       finite_sum_comparators=[str(x) for x in comparators],
                       qualification='Comparators are binary64 cutoff-12 diagnostics, not certified infinite-sum values.',
                       expansion_checks=verify_existing_expansion(), rows=[], failures=[],
                       rigorous_sign_certified=False,
                       unresolved=['No signed evaluation at the cutoff required by this bound.',
                                   'No certified finite-sum coefficient quadrature or rounding enclosure.',
                                   'Other terms of the complete Ward coefficient remain uncontrolled.'])
    for cutoff in args.cutoffs:
        try:
            t0, rt0 = tail_moment(0, cutoff, args.taylor_degree)
            t10, rt10 = tail_moment(10, cutoff, args.taylor_degree)
        except ValueError as error:
            certificate['failures'].append(dict(cutoff=cutoff, error=str(error)))
            continue
        radial_tail = 7 ** 4 * (7 * t10 * s0 ** 6 + 42 * s10 * t0 * s0 ** 5)
        bounds = [rounded_upper(constant * radial_tail) for constant in POLYNOMIAL_CONSTANTS]
        row = dict(cutoff=cutoff, moment_tails=[rt0, rt10], omitted_sum_upper=[record for _, record in bounds],
                   comparison_only_cutoff12_values=[str(x) for x in comparators],
                   required_for_sign='Tail plus quadrature and rounding < certified retained absolute value at the same cutoff; retained enclosure unavailable.',
                   less_than_cutoff12_diagnostic=[bound < ref for (bound, _), ref in zip(bounds, comparators)],
                   less_than_one=[bound < 1 for bound, _ in bounds],
                   qualification='The cutoff-specific omitted sum is bounded; comparison to cutoff 12 cannot transfer a sign to this cutoff.')
        certificate['rows'].append(row)
        print(json.dumps(dict(cutoff=cutoff, actual_omitted_sum_upper=[record['decimal_upper'] for _, record in bounds],
                              comparison_only_cutoff12_values=row['comparison_only_cutoff12_values'],
                              smaller_than_cutoff12_diagnostic=row['less_than_cutoff12_diagnostic'],
                              required_for_sign=row['required_for_sign'], path=str(args.output))), flush=True)
    args.output.write_text(json.dumps(certificate, indent=2) + '\n')
    print(json.dumps(dict(failures=certificate['failures'], rigorous_sign_certified=False,
                         actual_quadrature_error_bound=None, required_quadrature_bound='Combined tail + quadrature + rounding < certified retained absolute value.',
                         path=str(args.output))), flush=True)


if __name__ == '__main__':
    main()
