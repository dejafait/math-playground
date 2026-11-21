"""Exact scalar bounds for the C681c two-construction saddle obstruction.

This certifies constants only. The uniform saddle proof and all norm/pole
hypotheses are in C681c; no finite numerical fit is a proof input.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
source = HERE / 'positive-cone-contour-certificate.py'
prefix = source.read_text().split('def floor_scaled', 1)[0]
ns = {}
exec(compile(prefix, str(source), 'exec'), ns)
add, neg, mul = (ns[k] for k in ('add', 'neg', 'mul'))
logq, atanq, kernel = (ns[k] for k in ('logq', 'atanq', 'kernel'))
c = ns['C_INTERVAL']
d, U, r = Q(5, 4), Q(121, 64), Q(9, 20)
SCALE = 10**15
records, failures, riemann = [], [], []


def outward(interval):
    lo, hi = interval
    return (Q((lo.numerator*SCALE)//lo.denominator, SCALE),
            Q(-((-hi.numerator*SCALE)//hi.denominator), SCALE))


def check(name, interval, lower=None, upper=None):
    bounds = outward(interval)
    passed = ((lower is None or bounds[0] > lower)
              and (upper is None or bounds[1] < upper))
    records.append(dict(name=name, actual=[str(v) for v in bounds],
                        required_lower=None if lower is None else str(lower),
                        required_upper=None if upper is None else str(upper),
                        strict=True, passed=passed))
    if not passed:
        failures.append(name)


def fprime(s):
    A = d-s
    return add(add(logq(A/(A-1)), mul(logq(U/(U-A)), U/(A*A))),
               (-1/A, -1/A))


def derivative(s, kind):
    result = add(fprime(s), mul(c, -2 if kind == 'robin' else -1))
    if kind == 'finite_product':
        result = add(result, (-Q(6, 5)*s, -Q(6, 5)*s))
        result = add(result, mul(atanq(r/s), -Q(20, 27)))
    return result


check('c', c, Q(23, 20), Q(5, 4))
check('fprime_zero', fprime(Q(0)), None, Q(11, 5))
check('delta_2c_minus_fprime_zero', add(mul(c, 2), neg(fprime(Q(0)))),
      Q(0), Q(11, 50))
check('fprime_left', fprime(-Q(1, 8)), Q(7, 4), None)
check('K_left_at_zero_height', kernel(Q(1, 8), Q(0)), None, -Q(1, 8))
check('K_top_at_zero_real_part', kernel(Q(0), Q(1, 2)), None, -Q(3, 10))
for kind in ('robin', 'finite_product'):
    check(kind+'_derivative_at_1_20', derivative(Q(1, 20), kind), None, Q(0))
    check(kind+'_derivative_at_1_10', derivative(Q(1, 10), kind), Q(0), None)


def monotone_integral(name, A, numerator_kind, lower=None, upper=None):
    count = 256
    def value(t):
        if numerator_kind == 'denominator':
            return 1/((A-t)**2+Q(1, 4))
        return t*t/(U-A*t)**2
    # Both integrands increase on [0,1]; exact left/right Riemann sums.
    left = [value(Q(j, count))/count for j in range(count)]
    right = [value(Q(j+1, count))/count for j in range(count)]
    # Save a complete outward-rounded contribution list for reproducibility.
    lower_terms = [outward((v, v))[0] for v in left]
    upper_terms = [outward((v, v))[1] for v in right]
    bounds = (sum(lower_terms), sum(upper_terms))
    riemann.append(dict(name=name, A=str(A), kind=numerator_kind,
                        partition_count=count, scale=SCALE,
                        lower_term_numerators=[int(v*SCALE) for v in lower_terms],
                        upper_term_numerators=[int(v*SCALE) for v in upper_terms],
                        integral_bounds=[str(v) for v in bounds]))
    check(name, bounds, lower, upper)


monotone_integral('broad_denominator_integral', Q(11, 8),
                  'denominator', Q(11, 10), None)
monotone_integral('broad_numerator_integral', Q(11, 8),
                  'numerator', None, Q(3, 5))
monotone_integral('right_denominator_integral', Q(6, 5),
                  'denominator', Q(3, 2), None)
monotone_integral('right_numerator_integral', Q(5, 4),
                  'numerator', None, Q(1, 2))

arithmetic = {
    'curvature_lower': Q(16, 5)-Q(3, 5),
    'curvature_upper_before_rounding': 1/Q(3, 20)-1/Q(23, 20),
    'finite_product_extra_curvature_lower': Q(20, 27)*r/(r*r+Q(1, 100))-Q(6, 5),
    'finite_product_vertical_drop_lower': Q(1, 2)+Q(10, 27)*r/(Q(1, 100)+Q(19, 20)**2)-Q(3, 5),
    'rate_barrier': Q(11, 50)**2/(2*Q(13, 5)),
    'chosen_eventual_rate': Q(19, 2000),
    'required_rate': Q(1, 100),
    'finite_product_top_upper': Q(21, 20)*Q(1, 10)+3*Q(1, 10)**2+Q(3, 20)-Q(3, 10),
    'finite_product_left_upper': -Q(7, 32)+Q(5, 32)-Q(1, 8)+Q(3, 20),
    'robin_top_upper': Q(1, 50)-Q(1, 4)*Q(2, 5)**2,
}
check('extra_curvature_positive', (arithmetic['finite_product_extra_curvature_lower'],)*2,
      Q(0), None)
check('vertical_drop_above_2_25', (arithmetic['finite_product_vertical_drop_lower'],)*2,
      Q(2, 25), None)
check('barrier_below_eventual_rate', (arithmetic['rate_barrier'],)*2,
      None, arithmetic['chosen_eventual_rate'])
check('eventual_rate_below_required', (arithmetic['chosen_eventual_rate'],)*2,
      None, arithmetic['required_rate'])
check('curvature_upper_below_six',
      (arithmetic['curvature_upper_before_rounding'],)*2, None, Q(6))
check('finite_product_top_below_minus_barrier',
      (arithmetic['finite_product_top_upper'],)*2, None, -arithmetic['rate_barrier'])
check('finite_product_left_below_minus_barrier',
      (arithmetic['finite_product_left_upper'],)*2, None, -arithmetic['rate_barrier'])
check('robin_top_below_minus_barrier',
      (arithmetic['robin_top_upper'],)*2, None, -arithmetic['rate_barrier'])

result = dict(
    scope='Scalar constants for an asymptotic proof, not a sampled residual certificate',
    source=str(source.name), helper_prefix_sha256=hashlib.sha256(prefix.encode()).hexdigest(),
    generator_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    arithmetic='Exact Fraction operations; outward rational rounding only for saved values',
    checks=records, riemann_sums=riemann,
    exact_arithmetic={k: str(v) for k, v in arithmetic.items()},
    failures=failures, passed=not failures)
output = HERE / 'positive-blend-saddle-certificate.json'
output.write_text(json.dumps(result, indent=2)+'\n')
print(f'Checks: {len(records)}; failures: {len(failures)}')
print('Rate barrier:', arithmetic['rate_barrier'], '; eventual lower-bound rate:',
      arithmetic['chosen_eventual_rate'], '; target requires >', arithmetic['required_rate'])
for record in records:
    print(record['name'], record['actual'], 'required:',
          record['required_lower'], '< value <', record['required_upper'],
          'PASS' if record['passed'] else 'FAIL')
print('Certificate:', output)
if failures:
    raise SystemExit(1)
